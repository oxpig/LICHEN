import argparse
import sys
import os
import pandas as pd
from typing import Union, List, Optional
from ast import literal_eval

from lichen import LICHEN

parser = argparse.ArgumentParser(
    description="Run LICHEN to generate a light sequence for a given heavy sequence."
)
parser.add_argument(
    "input", 
    type=str,
    help="Input sequence as a string, "
    "or path to a fasta or csv file."
)
parser.add_argument(
    "-m",
    "--path_model",
    type=str,
    default=f'{os.getcwd()}/model/model_weights.pt',
    help=(
        "Path to model weights "
        "(default: ./model/model_weights.pt)."
    ),
)
parser.add_argument(
    "-c",
    "--cpu",
    default=False,
    help="Run on CPU only, even if a GPU is available.",
)
parser.add_argument(
    "--ncpu",
    type=int,
    default=-1,
    help=("Number of CPU threads to use "
          "(default: -1, uses all available CPUs)."
    )
)
parser.add_argument(
    "--germline_seed",
    nargs="+",
    default=None,
    help="Type, V-gene family, or V-genes to use (e.g.: IGKV1 IGKV2) "
    "(default: None).",
)
parser.add_argument(
    "--custom_seed",
    type=str,
    default=None,
    help="Custom seed to use (e.g. DIQMTQ) "
    "(default: None).",
)
parser.add_argument(
    "--cdrl1",
    type=str,
    default=None,
    help=(
        "Amino acid sequence of CDRL1 in either Kabat or IMGT definition "
        "(default: None)."
    ),
)
parser.add_argument(
    "--cdrl2",
    type=str,
    default=None,
    help=(
        "Amino acid sequence of CDRL2 in either Kabat or IMGT definition "
        "(default: None)."
    ),
)
parser.add_argument(
    "--cdrl3",
    type=str,
    default=None,
    help=(
        "Amino acid sequence of CDRL3 in either Kabat or IMGT definition "
        "(default: None)."
    ),
)
parser.add_argument(
    "--numbering_scheme",
    type=str,
    choices=["IMGT", "Kabat"],
    default="IMGT",
    help=(
        "Numbering scheme to used for CDR definition when CDR grafting "
        "either 'IMGT' or 'Kabat' "
        "(default: IMGT)."
    ),
)
parser.add_argument(
    "-n",
    "--repeats",
    type=int,
    default=1,
    help=(
        " Number of light sequences requested per heavy sequence "
        "(default: 1)."
    ),
)
parser.add_argument(
    "--filtering",
    nargs="+",
    default=None,
    help=(
        "Filtering steps to perform. Options are: 'redundancy', 'diversity', 'ANARCII', 'Humatch', 'AbLang2', "
        "and combinations thereof (except 'diversity' and 'AbLang2', which defaults to 'diversity'). "
        "When filtering requested 10 times more sequences will be generated than "
        "requested to apply filtering on "
        "(default: None)."
    ),
)
parser.add_argument(
    "-o",
    "--output",
    type=str,
    default=None,
    metavar="FILE",
    help="Specify the output file (must end in .csv) (default: None)." \
    "If no output file provided the output will be printed in the following format: " \
    "<FASTA HEADER | HEAVY> (<REPEAT>) : <OUTPUT>.",
)
parser.add_argument(
    "-v", "--verbose", action="store_true", help="Enable verbose output."
)


def main(args=None):
    args = parser.parse_args(args)

    # Check if model weights stored
    if not os.path.exists(os.path.dirname(args.path_model)):
        raise FileNotFoundError(f"No model weights found in: {args.path_model}, " 
                                "please save model weights (see https://github.com/oxpig/LICHEN) "
                                "and provide path to these weights.")

    # Process CDRS if given
    cdrs = [args.cdrl1, args.cdrl2, args.cdrl3]

    # Load the model
    lichen_model = LICHEN(args.path_model, cpu=args.cpu, ncpu=args.ncpu)

    # Check type of input and run generation
    try:
        if os.path.exists(os.path.dirname(args.input)):
            if args.input.endswith(".fasta"):
                from Bio import SeqIO
                # Process data in fasta
                names = []
                input_seqs = []
                for record in SeqIO.parse(args.input, "fasta"):
                    names.append(record.id)
                    input_seqs.append(str(record.seq))
                df = pd.DataFrame({'heavy': input_seqs,
                                   'germline_seed': [args.germline_seed]*len(input_seqs),
                                   'custom_seed': [args.custom_seed]*len(input_seqs),
                                   'cdrs': [cdrs]*len(input_seqs),
                                   'filtering': [args.filtering]*len(input_seqs)})
                
                # Run LICHEN
                result = lichen_model.light_generation_bulk(
                    input = df, 
                    numbering_scheme = args.numbering_scheme,
                    n = args.repeats,
                    verbose = args.verbose
                    )
                
                # Process output
                names = [x for xs in [[name]*args.repeats for name in names] for x in xs]
                result.insert(0, 'names', names)
                result = result.reset_index(drop=False).rename(columns={'index': 'repeat'})

            elif args.input.endswith(".csv"):
                # Load the input
                df = pd.read_csv(args.input, 
                                 converters={"germline_seed": literal_eval, "cdrs": literal_eval, "filtering": literal_eval})
                
                # Run LICHEN
                if args.verbose:
                    print('Using parameters as provided in the input file')
                result = lichen_model.light_generation_bulk(
                    input = df, 
                    numbering_scheme = args.numbering_scheme,
                    n = args.repeats,
                    verbose = args.verbose
                    )
                
                 # Process output
                result = result.reset_index(drop=False).rename(columns={'index': 'repeat'})
            else:
                raise ValueError("Input file must end in .csv, or .fasta.")
        elif args.input.endswith(".fasta") or args.input.endswith(".csv"):
            raise FileNotFoundError(f"Input file provided does not exist: {args.input}")
        else:
            # Run LICHEN
            result = lichen_model.light_generation(
                input = args.input,
                germline_seed = args.germline_seed,
                custom_seed = args.custom_seed,
                cdrs = cdrs,
                numbering_scheme = args.numbering_scheme,
                n = args.repeats,
                filtering = args.filtering,
                verbose = args.verbose
                )
    except TypeError as e:
        sys.exit(str(e))

    # Write output
    if not args.output:
        if args.input.endswith(".fasta"):
            for index, row in result.iterrows():
                print(f'{row["names"]} ({index+1}): {row["generated_light"]}')
        elif args.input.endswith(".csv"):
            for index, row in result.iterrows():
                print(f'{row["heavy"]} ({index+1}): {row["generated_light"]}')
        else:
            for i in range(len(result)):
                print(f'{args.input} ({i+1}): {result[i]}')
    elif args.input.endswith(".csv") or args.input.endswith(".fasta") and args.output.endswith(".csv"):
        if args.verbose:
            print(f'Saving output to: {args.output}')
        result.to_csv(args.output)
    elif type(result) == list and args.output.endswith(".csv"):
        df_result = pd.DataFrame({'repeat': list(range(1, args.repeats+1)),
                                  'heavy': [args.input]*args.repeats,
                                  'generated_light': result
                                  })
        if args.verbose:
            print(f'Saving output to: {args.output}')
        df_result.to_csv(args.output)
    else:
        raise ValueError("Output file must end in .csv")
    

if __name__ == "__main__":
    main()