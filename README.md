# LICHEN

**Light-chain Immunoglobulin sequence generation Conditioned on the Heavy chain and Experimental Needs**

<!--- INSTALL --->
## Install

Follow the steps below to download the code and the necessary packages.

```
# Clone the repo
git clone https://github.com:HenrietteCapel/LICHEN.git
cd LICHEN/

# Create your virtual env e.g.
conda create -n LICHEN_env

# Install required packages
conda install anaconda::pip
conda install -c conda-forge biopython -y
conda install conda-forge::pytorch

# ANARCII
conda install conda-forge::anarcii

# AbLang2
pip install ablang2

# LICHEN
pip install .

```

**Humatch** - and therefore **ANARCI** - are optional packages only required when you want to perform automatic filtering on humanness.
If you would like to use Humatch it is recommended to install python 3.9 and the cpuonly version of pytorch. Note that this means when filtering by Humatch LICHEN can only be run on a CPU.

```
## Install with optional packages (Humatch + ANARCI)
# Clone the repo
git clone https://github.com:HenrietteCapel/LICHEN.git
cd LICHEN/

# Install LICHEN with python3.9
conda create -n LICHEN_env python=3.9

# Install the other packages
conda install anaconda::pip
conda install -c conda-forge biopython -y

# Install cpuonly version of pytorch
conda install pytorch cpuonly -c pytorch

# ANARCII
conda install conda-forge::anarcii

# AbLang2
pip install ablang2

# Humatch
cd LICHEN #Humatch and ANARCI need to be installed within the LICHEN folder
git clone https://github.com/oxpig/Humatch.git
cd Humatch/
pip install .
conda install -c bioconda hmmer=3.3.2 -y
cd ..
git clone https://github.com/oxpig/ANARCI.git
cd ANARCI
python setup.py install
```

The **model weights** can be downloaded from <a href="https://doi.org/10.5281/zenodo.15917096">Zenodo</a>

<!--- Example usage within python --->
## Example usage within python
LICHEN generates light sequences for a given heavy sequence. Additional information regarding perferred light sequence type (e.g. kappa), V-gene family (e.g. IGKV1), and V-gene (e.g. IGKV1-39) usage can be provided to the model as well as light sequence seed of any length. 
Moreover, preffered usage of CDR sequences can be provided in any combination (e.g. only CDRL3) according to both IMGT and Kabat numbering scheme definitions. When generating sequences with CDRs grafted, LICHEN will automatically check correctness of the CDR placing based on ANARCII. 

Generated light sequence can be automatically filtered on duplicates ("redundancy"), sequences which can be numbered by <a href="https://doi.org/10.1101/2025.04.16.648720">ANARCII</a>, sequences which are human according to <a href="https://doi.org/10.1080/19420862.2024.2434121">Humatch</a>, and the most likely sequences according to <a href="https://doi.org/10.1093/bioinformatics/btae618">AbLang2</a>. Moreover, the most diverse ("diversity") sequences can be selected (based on AbLang2 scores).

LICHEN also allows for two heavy sequences as input, to generate a common light sequence.

Log likelihood and perplexity scores for a given heavy and light sequence can also be extracted from the model. 

For all use cases, first the model need to be loaded in python.
```
from lichen import LICHEN
lichen_model = LICHEN('path/to/model/model_weights.pt') # change to locally stored model path
```
Using a one or multiple CPUs can be requested with the parameters:  
**cpu**: Use a CPU if True, and GPU (if available) if False.  
**ncpu**: Number of CPUs to be used, default to all available CPUs.

### Generating light sequences for a single heavy sequence
Light sequences can be generated directly for a single heavy sequence using the **light_generation** function. This function takes the following parameters as input:  

**input**: the heavy sequence  
**germline_seed**: Type, V-gene family, or V-genes to use provided in a list, multiple are allowed (e.g. ['IGKV1', 'IGKV2'] or ['IGKV1', 'K']).
When multiple provided a random chosen selected seed will be used.  
**custom_seed**: Custom seed to use. Provided as string (e.g 'DIQMT').  
**cdrs**: Containing the CDRL1, CDRL2, and CDRL3 for additional information available. Provided as list of length three (e.g. if only CDRL3 known [None, None, 'QRYNRAPYT']).    
**numbering_scheme**: Numbering scheme CDR definition used when CDRs provided. Either 'IMGT' or 'Kabat'.   
**n**: Number of light sequences requested per heavy sequence.  
**filtering**: Filtering methods to apply. Available options are 'redundancy', 'diversity', 'ANARCII', 'Humatch', and 'AbLang2'. Provided in a list (e.g. ['ANARCII']).    
**verbose**: Enable verbose output.  

```
lichen_model.light_generation('EVQLLESGGEVKKPGASVKVSCRASGYTFRNYGLTWVRQAPGQGLEWMGWISAYNGNTNYAQKFQGRVTLTTDTSTSTAYMELRSLRSDDTAVYFCARDVPGHGAAFMDVWGTGTTVTVSS', germline_seed=['IGKV1'], n=2)
```

### Generating light sequences for multiple heavy sequences
Light sequences can be generated for multiple heavy sequences using the **light_generation_bulk** function and providing the input data in a pandas dataframe. 
This dataframe should contain a column **"heavy"** containing the heavy sequences. 
Optional additional information can be passed in the columns **"germline_seed"**, **"custom_seed"**, **"cdrs"**, and **"filtering"** in the same format as indicated above. 

The function takse the remaining parameters as input, i.e.:  
**input**: the pandas dataframe.  
**numbering_scheme**: Numbering scheme CDR definition used when CDRs provided. Either 'IMGT' or 'Kabat'.  
**n**: Number of light sequences requested per heavy sequence.   
**verbose**: Enable verbose output.  

```
import pandas as pd
df_input = pd.DataFrame({'heavy': ['EVQLLESGGEVKKPGASVKVSCRASGYTFRNYGLTWVRQAPGQGLEWMGWISAYNGNTNYAQKFQGRVTLTTDTSTSTAYMELRSLRSDDTAVYFCARDVPGHGAAFMDVWGTGTTVTVSS','QVQLVQSGVEVKKPGASVKVSCKASGYTFTNYYMYWVRQAPGQGLEWMGGINPSNGGTNFNEKFKNRVTLTTDSSTTTAYMELKSLQFDDTAVYYCARRDYRFDMGFDYWGQGTTVTVSS'],
                         'germline_seed': [['IGLV1-36'], ['IGKV1-39']]
                         'filtering': [['ANARCII'], ['ANARCII']]})
result = lichen_model.light_generation_bulk(df_input, n=3)
```

### Generating a common light sequence for a bispecific antibody
Both functions **light_generation** and **light_generation_bulk** can take two heavy sequences at the same time to generate a common light sequences by providing the heavy sequences in a list.

```
lichen_model.light_generation(['QVQLVESGGGLVKPGGSLRLSCAASGFTFSNYYMSWVRQAPGKGLEWISYISGRGSTIFYADSVKGRITISRDNAKNSLFLQMNSLRAEDTAVYFCVKDRGGYSPYWGQGTLVTVSS', 'EVQLVESGGGLVQPGRSLRLSCAASGFTFDDYSMHWVRQAPGKGLEWVSGISWNSGSKGYADSVKGRFTISRDNAKNSLYLQMNSLRAEDTALYYCAKYGSGYGKFYHYGLDVWGQGTTVTVSS'])
```

### Extracting log likelihood scores for an antibody
The log likelihood score of a given heavy-light pairing can be extracted from the model using the **light_log_likelihood** function. 
This function takes a pandas dataframe as input with the heavy sequence in the **"heavy"** column and the light sequence in the **"light"** column.

```
import pandas as pd
df_input = pd.DataFrame({'heavy': ['EVQLLESGGEVKKPGASVKVSCRASGYTFRNYGLTWVRQAPGQGLEWMGWISAYNGNTNYAQKFQGRVTLTTDTSTSTAYMELRSLRSDDTAVYFCARDVPGHGAAFMDVWGTGTTVTVSS'],'light': ['DIQMTQSPSTLSASIGDRVTITCRASEDVRKSLAWYQHRPGKAPRVLISAVSRLKDEVPSRFRGTRSEAEYTLSITSLQPDDSGTYFCQHYHRNSTTFGGGTRVDMK']})
result = lichen_model.light_log_likelihood(df_input)
```

### Extracting perplexity scores for an antiboy
The perplexity score of a given heavy-light pairing can be extracted from the model using the **light_perplexity** function. 
This function takes a pandas dataframe as input with the heavy sequence in the **"heavy"** column and the light sequence in the **"light"** column.

```
df_input = pd.DataFrame({'heavy': ['EVQLLESGGEVKKPGASVKVSCRASGYTFRNYGLTWVRQAPGQGLEWMGWISAYNGNTNYAQKFQGRVTLTTDTSTSTAYMELRSLRSDDTAVYFCARDVPGHGAAFMDVWGTGTTVTVSS'], 'light': ['DIQMTQSPSTLSASIGDRVTITCRASEDVRKSLAWYQHRPGKAPRVLISAVSRLKDEVPSRFRGTRSEAEYTLSITSLQPDDSGTYFCQHYHRNSTTFGGGTRVDMK']})
result = lichen_model.light_perplexity(df_input)
```

## Command line usage
LICHEN can also run directly from the command line. This takes the heavy sequence, or a path to a fasta or csv file containing the heavy sequences as input. The output can be written to a csv file.
```
lichen EVQLLESGGEVKKPGASVKVSCRASGYTFRNYGLTWVRQAPGQGLEWMGWISAYNGNTNYAQKFQGRVTLTTDTSTSTAYMELRSLRSDDTAVYFCARDVPGHGAAFMDVWGTGTTVTVSS -o example_output.csv -v
```

For all command line options see:
```
lichen --help
```

## Citation
This work is described in our [paper](https://doi.org/10.1101/2025.08.06.668938):

**LICHEN: Light-chain Immunoglobulin sequence generation Conditioned on the Heavy chain and Experimental Needs**

```
@article{Capel2025,
  title = {LICHEN: Light-chain Immunoglobulin sequence generation Conditioned on the Heavy chain and Experimental Needs},
  author = {Capel, Henriette L and Ellmen, Isaac and Murray, Chris J and Mignone, Giulia and Black, Megan and Clarke, Brendan and Breen, Conor and Tierney, Sean and Dougan, Patrick and Buick, Richard J and Greenshields-Watson, Alexander and Deane, Charlotte M},
  journal = {bioRxiv},
  year={2025},
  doi = {https://doi.org/10.1101/2025.08.06.668938}
}
```
## Web tool
The live Web tool is available at https://opig.stats.ox.ac.uk/webapps/lichen/
