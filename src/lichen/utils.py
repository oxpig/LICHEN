import numpy as np
import pandas as pd
from typing import Union, List, Optional


MAP_FR1_FR3 = {'NI': ['SL'],
               'AI': ['SL']*7+['TL']*6,
               'QT': ['NK']*1+['TR']*2,
               'QP': ['NK']*3+['GQ']*4+['QQ']*2+['HQ']*1+['SK']*3,
               'DI': ['SL']*38+['TL']*5+['NL']*44+['RL']*1+['DL']*2+['NH']*1+['NR']*9+['SR']*4+['NK']*3+['YR']*2+['TR']*3,
               'RP': ['QL']*2,
               'SY': ['KR']*4+['ER']*10+['NR']*4+['DR']*4,
               'DV': ['NR']*2+['NW']*1+['QS']*1,
               'QA': ['NR']*6+['QQ']*5+['HQ']*1+['NK']*4,
               'EI': ['NR']*8+['TR']*13+['SR']*4+['IR']*1+['QS']*4,
               'LP': ['SK']*1,
               'SS': ['NR']*2+['VQ']*2+['DR']*1,
               'VI': ['TL']*3,
               'ET': ['TL']*2,
               'NF': ['QR']*4,
               'QS': ['LL']*1+['NR']*11+['KR']*14+['QR']*7+['NW']*3+['TR']*4+['TQ']*1+['TC']*1,
               'QL': ['SK']*2}

MAP_CDRS_FR1_IMGT = pd.DataFrame({'CDR1': ['SSNIGNNA', 'SSNIGAGYD', 'SSNIGAGYD', 'SSNIGAGYD', 'SSDMGNYA', 'SSDMGNYA', 'SSNIGSNT', 'SSNIGSNT', 'SSNIGSNT', 'SSNIGSNT', 'SSNIGSNY', 'SSNIGSNY', 'SSNIGSNY', 'SSNIGAGYV', 'SSNIGNNY', 
                                           'SSNIGNNY', 'SSNTGTGYN', 'SNNVGNQG', 'SNIVGNQG', 'SNNVGNQG', 'SNNVGNQG', 'SNIVGNQG', 'SNNAGNQG', 'SDLSVGGKN', 'SDLSVGGKN', 'SSDVGGYNY', 'SSDVGGYNY', 'SSDVGGYNY', 'SSDVGSYNL', 'SSDVGGYNY', 
                                           'SSDVGGYNY', 'SSDVGSYNR', 'SSDVGSYNR', 'SSDVGSYNR', 'SSDVGSYNR', 'SSDVGSYNL', 'SSDVGSYNL', 'SSDVGSYNL', 'SSDVGGYNY', 'SSDVGDYDH', 'SSDVGDYDH', 'SSDVGDYDH', 'SSDIGGYDL', 'SSDIGGYDL', 
                                           'SSDVGSYDY', 'SSDVGSYDY', 'SSDVGGYNY', 'SSDVGGYNY', 'SSDVGGYNY', 'KLGDKY', 'KLGDKY', 'ALPKKY', 'ALPKKY', 'ALPKKY', 'NIGSKA', 'NIGSKA', 'VLRDNY', 'VLRDNY', 'ALPKKY', 'SLRSYY', 'SLRSYY', 
                                           'NIGSKS', 'NIGSKS', 'NIGSKS', 'NIGSKS', 'VLGENY', 'VLGKNY', 'ALPKQY', 'ALPKQY', 'ALPKQY', 'VLAKKY', 'SIEDSV', 'SIEDSV', 'SMEGSY', 'NIGSKN', 'NLGYKS', 'SEHSTYT', 'SGHSSYI', 'SGHSSYI', 
                                           'SGHSSYI', 'SGHSSYA', 'SGHSSYA', 'SDINVGSYN', 'SDINVGSYN', 'SDINVSSYN', 'SGINVGTYR', 'SGINVGTYR', 'SGINVGTYR', 'SGINVGTYR', 'SGINVGTYR', 'SGINVGTYR', 'SGINVGTYR', 'SGINLGSYR', 'SGISVGSYR', 
                                           'SGFSVGDFW', 'SGSIASNY', 'SGSIASNY', 'SGSIASNY', 'SGSIASNY', 'TGAVTSGYY', 'TGAVTSGHY', 'TGAVTSGHY', 'TGAVTSGHY', 'TGAVTSGHY', 'SGSVSTSYY', 'SGSVSTSYY', 'SGSVSTSHY', 'SGYSNYK', 'SGYSNYK', 
                                           'SGYSNYK', 'QGISSW', 'QGISSW', 'QGISSA', 'QGISSA', 'QGISNY', 'QGISNY', 'QGIRND', 'QGIRND', 'QGISNY', 'QGISNY', 'QGISNY', 'QGISNY', 'QDISNY', 'QGISSY', 'QSISSY', 'QSISSY', 'QSISSW', 
                                           'QSISSW', 'QSISSW', 'QSISSW', 'QSISSW', 'QGIRND', 'QGIRND', 'QGISSY', 'QGISSY', 'QGISSY', 'QGISSY', 'QGISSY', 'QGISSY', 'QGISSY', 'QGISNS', 'QGISNN', 'QGISNN', 'QGISNN', 'QGISNN', 
                                           'QGISNN', 'QGISNN', 'QGISNN', 'QGISNN', 'QGISNG', 'QSIYNY', 'QGISNN', 'QGISNN', 'QSIYNY', 'QSIYNY', 'QGISNN', 'QGISNN', 'QGISNN', 'QGISNN', 'QGIINN', 'QGISSW', 'QGISSW', 'QGISSA', 
                                           'QGISSA', 'QGISSW', 'QGISSW', 'QGISNY', 'QDISNY', 'QGISSY', 'QSISSY', 'EGISSN', 'EGISSN', 'QGISSY', 'QGISSY', 'QGISSY', 'QGISSY', 'QGISSY', 'QSLLHSNGYTY', 'QSLVHSDGNTY', 'QSLVHSDGNTY', 
                                           'QSLLHSNGYNY', 'QSLLHSDGKTY', 'QSLLHSDGKTY', 'QSLLHSDGKTY', 'QSLVYSDGNTY', 'QSLVHSDGNTY', 'QSLLHSDGNTY', 'QSLLHSDGNTY', 'QSLLDSDDGNTY', 'RSLLHSNGNTY', 'ESLLDTDDEYTY', 'QSLLHSNGYTY', 
                                           'QSLVHSDGNTY', 'QSLLHSDGYTY', 'QSLLHSDGYTY', 'QSLLHSDGYTY', 'QSLLHSNGYNY', 'QSLLHSDGKTY', 'QSLLHSDGKTY', 'QSLVYSDGNTY', 'QSLLDSDDGNTY', 'QSVSSY', 'QSVSSY', 'QSVSSN', 'QSVSSN', 'QSVSSSY', 
                                           'QSVSSSY', 'QSVSSSY', 'QSVSSSY', 'QSVSSSY', 'QSVSSSY', 'QSVSSSY', 'QSVSSSY', 'QSVSSSY', 'QSVSSSY', 'QGVSSY', 'QSVSSY', 'QGVSSN', 'QSVSSN', 'QSVSSN', 'QSVSSN', 'QSVSSSY', 'QSVSSSY', 
                                           'QSVSSSY', 'QSVLYSSNNKNY', 'QSVLYSSNNKNY', 'QSVLYSSNNKNY', 'QDIDDD', 'QDIDDD', 'QSIGSS', 'QSIGSS', 'QSIGSS', 'QSIGSS', 'EGIGNY', 'ESVSFLGINL'],
                                  'CDR2': ['YDD', 'GNS', 'GNS', 'GNS', 'ENN', 'ENN', 'SNN', 'SNN', 'SNN', 'RNN', 'RNN', 'SNN', 'RNN', 'GNS', 'DNN', 'ENN', 'GDK', 'RNN', 'RNN', 'RNN', 'RNN', 'RNN', 'RNN', 'HYSDSDK', 'HYSDSDK', 
                                           'DVS', 'DVS', 'EVS', 'EGS', 'DVS', 'EVS', 'EVS', 'EVS', 'EVS', 'EVS', 'EGS', 'EVS', 'EGS', 'DVS', 'NVN', 'NVN', 'NVN', 'DVA', 'DVG', 'NVN', 'NVN', 'EVS', 'EVS', 'EVS', 'QDS', 'QDS', 
                                           'EDS', 'KDS', 'EDS', 'SDS', 'SDS', 'KDG', 'KDG', 'KDS', 'GKN', 'GKN', 'YDS', 'DDS', 'DDS', 'YDS', 'EDS', 'EDS', 'KDS', 'KDS', 'KDS', 'KDS', 'LNS', 'LNS', 'DSS', 'RDS', 'RDN', 'VKSDGSH', 
                                           'LEGSGSY', 'LEGSGSY', 'LEGSGSY', 'LNSDGSH', 'LNSDGSH', 'YYSDSDK', 'YYSDSDK', 'YYSDSDK', 'YKSDSDK', 'YKSDSDK', 'YKSDSDK', 'YKSDSDK', 'YKSDSDK', 'YKSDSDK', 'YKSDSDK', 'YYSDSSK', 'YYSDSDK', 
                                           'YHSDSNK', 'EDN', 'EDN', 'EDN', 'EDN', 'STS', 'DTS', 'DTS', 'DTS', 'DTS', 'STN', 'STN', 'SPN', 'VGTGGIVG', 'VGTGGIVG', 'VGTGGIVG', 'AAS', 'AAS', 'DAS', 'DAS', 'AAS', 'AAS', 'AAS', 'AAS', 
                                           'AAS', 'AAS', 'AAS', 'AAS', 'DAS', 'SAS', 'AAS', 'AAS', 'DAS', 'DAS', 'KAS', 'KAS', 'KAS', 'AAS', 'AAS', 'AAS', 'AAS', 'AAS', 'AAS', 'AAS', 'AAS', 'AAS', 'AAS', 'AAS', 'AAS', 'AAS', 'AAS', 
                                           'AAS', 'AAP', 'AAP', 'AAS', 'AAS', 'RAS', 'AAS', 'AAS', 'RAS', 'RAS', 'AAS', 'AAS', 'AAS', 'AAS', 'AAS', 'AAS', 'AAS', 'DAS', 'DAS', 'AAS', 'AAS', 'AAS', 'DAS', 'SAS', 'AAS', 'DAK', 
                                           'DAK', 'YAS', 'AAS', 'AAS', 'AAS', 'AAS', 'RVS', 'KIS', 'KIS', 'LGS', 'EVS', 'EVS', 'EVS', 'KVS', 'KVS', 'TIS', 'TIS', 'TLS', 'KVS', 'EVS', 'RVS', 'KVS', 'EVS', 'EVS', 'EVS', 'LGS', 
                                           'EVS', 'EVS', 'KVS', 'TLS', 'DAS', 'DAS', 'GAS', 'GAS', 'GAS', 'GAS', 'GAS', 'GAS', 'GAS', 'GAS', 'GAS', 'GAS', 'GAS', 'GAS', 'DAS', 'DAS', 'DAS', 'GAS', 'GAS', 'GAS', 'DAS', 'DAS', 
                                           'GAS', 'WAS', 'WAS', 'WAS', 'EAT', 'EAT', 'YAS', 'YAS', 'YAS', 'YAS', 'YAS', 'QAS'],
                                  'startFR1': ['QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QA', 'QA', 'QA', 'QA', 'QA', 'QA', 'RP', 'RP', 'QS', 'QS', 'QS', 'QS', 
                                               'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'SY', 'SY', 'SY', 'SY', 'SY', 'SY', 'SY', 'SY', 'SY', 
                                               'SY', 'SS', 'SS', 'SY', 'SY', 'SY', 'SY', 'SY', 'SY', 'SY', 'SY', 'SY', 'SY', 'SS', 'SS', 'SS', 'SY', 'SY', 'LP', 'QP', 'QP', 'QP', 'QL', 'QL', 'QP', 'QP', 'QP', 'QP', 'QP', 
                                               'QA', 'QA', 'QA', 'QA', 'QA', 'QP', 'QA', 'QP', 'NF', 'NF', 'NF', 'NF', 'QT', 'QA', 'QA', 'QA', 'QA', 'QT', 'QT', 'QS', 'QP', 'QP', 'QP', 'DI', 'DI', 'AI', 'AI', 'DI', 'DI', 
                                               'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'AI', 'AI', 'AI', 'AI', 'AI', 'AI', 'DI', 'DI', 'AI', 'DI', 'DI', 'DI', 'DI', 'DI', 
                                               'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'AI', 'AI', 'DI', 'DI', 'NI', 'DI', 'DI', 'DI', 'DI', 'DI', 'AI', 'VI', 
                                               'AI', 'VI', 'VI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DV', 'DV', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'EI', 'EI', 'EI', 'DI', 'DI', 'DI', 'DV', 'DI', 'EI', 'EI', 
                                               'EI', 'EI', 'EI', 'EI', 'EI', 'EI', 'EI', 'EI', 'EI', 'EI', 'EI', 'EI', 'EI', 'EI', 'EI', 'EI', 'EI', 'EI', 'EI', 'EI', 'EI', 'DI', 'DI', 'DI', 'ET', 'ET', 'EI', 'EI', 'EI', 
                                               'EI', 'DV', 'DI']})
MAP_CDRS_FR1_KABAT = pd.DataFrame({'CDR1': ['SGSSSNIGNNAVN', 'TGSSSNIGAGYDVH', 'TGSSSNIGAGYDVH', 'TGSSSNIGAGYDVH', 'SGSSSDMGNYAVS', 'SGSSSDMGNYAVS', 'SGSSSNIGSNTVN', 'SGSSSNIGSNTVN', 'SGSSSNIGSNTVN', 'SGSSSNIGSNTVN', 
                                            'SGSSSNIGSNYVY', 'SGSSSNIGSNYVY', 'SGSSSNIGSNYVY', 'TGSSSNIGAGYVVH', 'SGSSSNIGNNYVS', 'SGSSSNIGNNYVS', 'TGSSSNTGTGYNVN', 'TGNSNNVGNQGAA', 'TGNSNIVGNQGAA', 'TGNSNNVGNQGAA', 
                                            'TGNSNNVGNQGAA', 'TGNSNIVGNQGAA', 'TGNSNNAGNQGAA', 'TLSSDLSVGGKNMF', 'TLSSDLSVGGKNMF', 'TGTSSDVGGYNYVS', 'TGTSSDVGGYNYVS', 'TGTSSDVGGYNYVS', 'TGTSSDVGSYNLVS', 'TGTSSDVGGYNYVS', 
                                            'TGTSSDVGGYNYVS', 'TGTSSDVGSYNRVS', 'TGTSSDVGSYNRVS', 'TGTSSDVGSYNRVS', 'TGTSSDVGSYNRVS', 'TGTSSDVGSYNLVS', 'TGTSSDVGSYNLVS', 'TGTSSDVGSYNLVS', 'TGTSSDVGGYNYVS', 'TGTSSDVGDYDHVF', 
                                            'TGTSSDVGDYDHVF', 'TGTSSDVGDYDHVF', 'TGTSSDIGGYDLVS', 'TGTSSDIGGYDLVS', 'TGTSSDVGSYDYVS', 'TGTSSDVGSYDYVS', 'TGTSSDVGGYNYVS', 'TGTSSDVGGYNYVS', 'TGTSSDVGGYNYVS', 'SGDKLGDKYAC', 
                                            'SGDKLGDKYAC', 'SGDALPKKYAY', 'SGDALPKKYAY', 'SGDALPKKYAY', 'GGNNIGSKAVH', 'GGNNIGSKAVH', 'SGDVLRDNYAD', 'SGDVLRDNYAD', 'SGEALPKKYAY', 'QGDSLRSYYAS', 'QGDSLRSYYAS', 'GGNNIGSKSVH', 
                                            'GGNNIGSKSVH', 'GGNNIGSKSVH', 'GGNNIGSKSVH', 'SGDVLGENYAD', 'SGDVLGKNYAD', 'SGDALPKQYAY', 'SGDALPKQYAY', 'SGDALPKQYAY', 'SGDVLAKKYAR', 'QGDSIEDSVVN', 'QGDSIEDSVVN', 'QGDSMEGSYEH', 
                                            'GGNNIGSKNVH', 'GGNNLGYKSVH', 'TLSSEHSTYTIE', 'TLSSGHSSYIIA', 'TLSSGHSSYIIA', 'TLSSGHSSYIIA', 'TLSSGHSSYAIA', 'TLSSGHSSYAIA', 'TLPSDINVGSYNIY', 'TLPSDINVGSYNIY', 'TLPSDINVSSYNIY', 
                                            'TLRSGINVGTYRIY', 'TLRSGINVGTYRIY', 'TLRSGINVGTYRIY', 'TLRSGINVGTYRIY', 'TLRSGINVGTYRIY', 'TLCSGINVGTYRIY', 'TLRSGINVGTYRIY', 'TLRSGINLGSYRIF', 'TLRSGISVGSYRIY', 'MLSSGFSVGDFWIR', 
                                            'TRSSGSIASNYVQ', 'TGSSGSIASNYVQ', 'TRSSGSIASNYVQ', 'TRSSGSIASNYVQ', 'ASSTGAVTSGYYPN', 'GSSTGAVTSGHYPY', 'GSSTGAVTSGHYPY', 'GSSTGAVTSGHYPY', 'GSSTGAVTSGHYPY', 'GLSSGSVSTSYYPS', 
                                            'GLSSGSVSTSYYPS', 'ALSSGSVSTSHYPR', 'TLSSGYSNYKVD', 'TLSSGYSNYKVD', 'TLSSGYSNYKVD', 'RASQGISSWLA', 'RASQGISSWLA', 'RASQGISSALA', 'RASQGISSALA', 'RASQGISNYLA', 'RASQGISNYLA', 
                                            'RASQGIRNDLG', 'RASQGIRNDLG', 'RASQGISNYLA', 'RASQGISNYLA', 'RASQGISNYLA', 'RASQGISNYLA', 'QASQDISNYLN', 'RVSQGISSYLN', 'RASQSISSYLN', 'RASQSISSYLN', 'RASQSISSWLA', 'RASQSISSWLA', 
                                            'RASQSISSWLA', 'RASQSISSWLA', 'RASQSISSWLA', 'RASQGIRNDLG', 'RASQGIRNDLG', 'RASQGISSYLA', 'RASQGISSYLA', 'RASQGISSYLA', 'RASQGISSYLA', 'RASQGISSYLA', 'WASQGISSYLA', 'RASQGISSYLA', 
                                            'RASQGISNSLA', 'RASQGISNNLN', 'RASQGISNNLN', 'RASQGISNNLN', 'RASQGISNNLN', 'RASQGISNNLN', 'RASQGISNNLN', 'RASQGISNNLN', 'RASQGISNNLN', 'RASQGISNGLS', 'QASQSIYNYLN', 'RASQGISNNLN', 
                                            'RASQGISNNLN', 'QASQSIYNYLN', 'QASQSIYNYLN', 'RASQGISNNLN', 'RASQGISNNLN', 'RVSQGISNNLN', 'RASQGISNNLN', 'RASQGIINNLN', 'RASQGISSWLA', 'RASQGISSWLA', 'RASQGISSALA', 'RASQGISSALA', 
                                            'RASQGISSWLA', 'RARQGISSWLA', 'RARQGISNYLA', 'QASQDISNYLN', 'RVSQGISSYLN', 'RASQSISSYLN', 'WASEGISSNLA', 'WASEGISSNLA', 'WASQGISSYLA', 'RMSQGISSYLA', 'RMSQGISSYLA', 'RMSQGISSYLA', 
                                            'RMSQGISSYLA', 'RSSQSLLHSNGYTYLH', 'RSSQSLVHSDGNTYLS', 'RSSQSLVHSDGNTYLS', 'RSSQSLLHSNGYNYLD', 'KSSQSLLHSDGKTYLY', 'KSSQSLLHSDGKTYLY', 'KSSQSLLHSDGKTYLY', 'RSSQSLVYSDGNTYLN', 
                                            'RSSQSLVHSDGNTYLN', 'RSSQSLLHSDGNTYLD', 'RSSQSLLHSDGNTYLD', 'RSSQSLLDSDDGNTYLD', 'RSSRSLLHSNGNTYLH', 'RSSESLLDTDDEYTYLN', 'RSSQSLLHSNGYTYLH', 'RSSQSLVHSDGNTYLS', 'RSSQSLLHSDGYTYLY', 
                                            'RSSQSLLHSDGYTYLY', 'RSSQSLLHSDGYTYLY', 'RSSQSLLHSNGYNYLD', 'KSSQSLLHSDGKTYLY', 'KSSQSLLHSDGKTYLY', 'RSSQSLVYSDGNTYLN', 'RSSQSLLDSDDGNTYLD', 'RASQSVSSYLA', 'RASQSVSSYLA', 'RASQSVSSNLA', 
                                            'RASQSVSSNLA', 'RASQSVSSSYLA', 'RASQSVSSSYLA', 'RASQSVSSSYLT', 'RASQSVSSSYLS', 'RASQSVSSSYLT', 'RASQSVSSSYLT', 'RASQSVSSSYLT', 'RASQSVSSSYLT', 'RASQSVSSSYLS', 'RASQSVSSSYLS', 'RASQGVSSYLA', 
                                            'RASQSVSSYLA', 'RASQGVSSNLA', 'RASQSVSSNLA', 'RASQSVSSNLA', 'RASQSVSSNLA', 'GASQSVSSSYLA', 'RASQSVSSSYLA', 'RASQSVSSSYLS', 'KSSQSVLYSSNNKNYLA', 'KSSQSVLYSSNNKNYLA', 'KSSQSVLYSSNNKNYLA', 
                                            'KASQDIDDDMN', 'KASQDIDDDMN', 'RASQSIGSSLH', 'RASQSIGSSLH', 'RASQSIGSSLH', 'RASQSIGSSLH', 'QASEGIGNYLY', 'RASESVSFLGINLIH'],
                                   'CDR2': ['YDDLLPS', 'GNSNRPS', 'GNSNRPS', 'GNSNRPS', 'ENNKRPS', 'ENNKRPS', 'SNNQRPS', 'SNNQRPS', 'SNNQRPS', 'RNNQRPS', 'RNNQRPS', 'SNNQRPS', 'RNNQRPS', 'GNSNRPS', 'DNNKRPS', 'ENNKRPS', 'GDKNWAS', 
                                            'RNNNRPS', 'RNNNRPS', 'RNNNRPS', 'RNNNRPS', 'RNNNRPS', 'RNNNRPS', 'HYSDSDKQLGP', 'HYSDSDKQLGP', 'DVSKRPS', 'DVSKRPS', 'EVSNRPS', 'EGSKRPS', 'DVSNRPS', 'EVSNRPS', 'EVSNRPS', 'EVSNRPS', 'EVSNRPS', 
                                            'EVSNRPS', 'EGSKRPS', 'EVSKRPS', 'EGSKRPS', 'DVSKRPS', 'NVNTRPS', 'NVNTRPS', 'NVNTRPS', 'DVANWPS', 'DVGNWPS', 'NVNTQPS', 'NVNTRPS', 'EVSKRPS', 'EVSKRPS', 'EVSKRPS', 'QDSKRPS', 'QDSERPS', 'EDSKRPS', 
                                            'KDSKRPS', 'EDSKRPS', 'SDSNRPS', 'SDSNRPS', 'KDGERPS', 'KDGERPS', 'KDSERPS', 'GKNNRPS', 'GKNNRPS', 'YDSDRPS', 'DDSDRPS', 'DDSDRPS', 'YDSDRPS', 'EDSERYP', 'EDSERYP', 'KDSERPS', 'KDSERPS', 'KDSERPS', 
                                            'KDSERPS', 'LNSVQSS', 'LNSVQSS', 'DSSDRPS', 'RDSNRPS', 'RDNNRPS', 'VKSDGSHSKGD', 'LEGSGSYNKGS', 'LEGSGSYNKGS', 'LEGSGSYNKGS', 'LNSDGSHSKGD', 'LNSDGSHSKGD', 'YYSDSDKGQGS', 'YYSDSDKGQGS', 
                                            'YYSDSDKGQGS', 'YKSDSDKQQGS', 'YKSDSDKQQGS', 'YKSDSDKQQGS', 'YKSDSDKQQGS', 'YKSDSDKQQGS', 'YKSDSDKQQGS', 'YKSDSDKQQGS', 'YYSDSSKHQGS', 'YYSDSDKHQGS', 'YHSDSNKGQGS', 'EDNQRPS', 'EDNQRPS', 
                                            'EDNQRPS', 'EDNQRPS', 'STSNKHS', 'DTSNKHS', 'DTSNKHS', 'DTSNKHS', 'DTSNKHS', 'STNTRSS', 'STNTRSS', 'SPNTCPS', 'VGTGGIVGSKGD', 'VGTGGIVGSKGD', 'VGTGGIVGSKGD', 'AASSLQS', 'AASSLQS', 'DASSLES', 
                                            'DASSLES', 'AASSLQS', 'AASSLQS', 'AASSLQS', 'AASSLQS', 'AASSLQS', 'AASTLQS', 'AASTLQS', 'AASTLQS', 'DASNLET', 'SASNLQS', 'AASSLQS', 'AASSLQS', 'DASSLES', 'DASSLES', 'KASSLES', 'KASSLES', 'KASSLES', 
                                            'AASSLQS', 'AASSLQS', 'AASTLQS', 'AASTLQS', 'AASTLQS', 'AASTLQS', 'AASTLQS', 'AASTLQS', 'AASTLQS', 'AASRLES', 'AASSLQS', 'AASSLQS', 'AASSLQS', 'AASSLQS', 'AASSLQS', 'AAPSLQS', 'AAPSLQS', 'AASSLQS', 
                                            'AASSLQS', 'RASSLQR', 'AASSLQS', 'AASSLQS', 'RASSLQR', 'RASSLQR', 'AASSLQS', 'AASSLQS', 'AASSLQS', 'AASSLQS', 'AASSLQS', 'AASSLQS', 'AASSLQS', 'DASSLES', 'DASSLES', 'AASSLQS', 'AASSLQS', 'AASSLQS', 
                                            'DASNLET', 'SASNLQS', 'AASSLQS', 'DAKDLHP', 'DAKDLHP', 'YASSLQS', 'AASTLQS', 'AASTLQS', 'AASTLQS', 'AASTLQS', 'RVSNHLS', 'KISNRFS', 'KISNRFS', 'LGSNRAS', 'EVSSRFS', 'EVSSRFS', 'EVSSRFS', 'KVSNRDS', 
                                            'KVSNRDS', 'TISNKFY', 'TISNKFY', 'TLSYRAS', 'KVSNRFS', 'EVSNRAS', 'RVSSRFS', 'KVSNRFS', 'EVSNRFS', 'EVSNRFS', 'EVSNRFS', 'LGSNRAS', 'EVSNRFS', 'EVSNRFS', 'KVSNWDS', 'TLSYRAS', 'DASNRAT', 'DASNRAT', 
                                            'GASTRAT', 'GASTRAT', 'GASSRAT', 'GASSRAT', 'GASTRAT', 'GASTRAT', 'GASTRAT', 'GASTRAT', 'GASTRAT', 'GASTRAT', 'GASTRAT', 'GASTRAT', 'DASNRAT', 'DASNRAT', 'DASNRAT', 'GASTRAT', 'GASTRAT', 'GASIRAT', 
                                            'DASSRAT', 'DASSRAT', 'GASTRAT', 'WASTRES', 'WASTRES', 'WASTRES', 'EATTLVP', 'EATTLVP', 'YASQSFS', 'YASQSIS', 'YASQSFS', 'YASQSIS', 'YASQSIS', 'QASNKDT'],
                                   'startFR1': ['QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QA', 'QA', 'QA', 'QA', 'QA', 'QA', 'RP', 'RP', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 
                                                'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'QS', 'SY', 'SY', 'SY', 'SY', 'SY', 'SY', 'SY', 'SY', 'SY', 'SY', 'SS', 'SS', 'SY', 'SY', 'SY', 
                                                'SY', 'SY', 'SY', 'SY', 'SY', 'SY', 'SY', 'SS', 'SS', 'SS', 'SY', 'SY', 'LP', 'QP', 'QP', 'QP', 'QL', 'QL', 'QP', 'QP', 'QP', 'QP', 'QP', 'QA', 'QA', 'QA', 'QA', 'QA', 'QP', 'QA', 'QP', 'NF', 
                                                'NF', 'NF', 'NF', 'QT', 'QA', 'QA', 'QA', 'QA', 'QT', 'QT', 'QS', 'QP', 'QP', 'QP', 'DI', 'DI', 'AI', 'AI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 
                                                'DI', 'DI', 'DI', 'AI', 'AI', 'AI', 'AI', 'AI', 'AI', 'DI', 'DI', 'AI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 
                                                'DI', 'DI', 'AI', 'AI', 'DI', 'DI', 'NI', 'DI', 'DI', 'DI', 'DI', 'DI', 'AI', 'VI', 'AI', 'VI', 'VI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 'DV', 'DV', 'DI', 'DI', 'DI', 'DI', 'DI', 'DI', 
                                                'DI', 'EI', 'EI', 'EI', 'DI', 'DI', 'DI', 'DV', 'DI', 'EI', 'EI', 'EI', 'EI', 'EI', 'EI', 'EI', 'EI', 'EI', 'EI', 'EI', 'EI', 'EI', 'EI', 'EI', 'EI', 'EI', 'EI', 'EI', 'EI', 'EI', 'EI', 'EI', 
                                                'DI', 'DI', 'DI', 'ET', 'ET', 'EI', 'EI', 'EI', 'EI', 'DV', 'DI']})

MAP_TYPE_SEED = {'L': ['QS']*42+['SY']*22+['QA']*16+['QP']*13+['SS']*5+['NF']*4+['QT']*3+['RP']*2+['SV']*2+['QL']*2+['SA']*1+['LP']*1+['VT']*1,
                 'K': ['DI']*72+['EI']*30+['AI']*13+['DV']*4+['VI']*3+['ET']*2+['NI']*1+['AS']*1}

MAP_GENE_FAM_SEED = {'IGKV5': ['ETTLTQSPAF', 'ETTLTQSPAF'], 
                 'IGLV1': ['QSVLTQPPSV', 'QSVLTQPPSV', 'QSVVTQPPSV', 'QSVVTQPPSV', 'QSVLTQPPSV', 'QSVLTQPPSV', 'QSVLTQPPSA', 'QSVLTQPPSA', 
                           'QSVLTQPPSA', 'QSVLTQPPSA', 'QSVLTQPPSA', 'QSVLTQPPSA', 'QSVLTQPPSA', 'QSVLTQPPSV', 'QSVLTQPPSV', 'QSVLTQPPSV', 'QSVLTQPPSV'], 
                 'IGLV8': ['QTVVTQEPSF', 'QTVVTQEPSF', 'VTQEPSFSVS', 'QSVVTQEPSL'], 
                 'IGKV3': ['EIVLTQSPAT', 'EIVLTQSPAT', 'EIVMTQSPAT', 'EIVMTQSPAT', 'EIVLTQSPGT', 'EIVLTQSPAT', 'EIVMTQSPPT', 'EIVMTQSPPT', 'EIVMTQSPPT', 
                           'EIVMTQSPPT', 'EIVMTQSPPT', 'EIVMAQSPPT', 'EIVMTQSPAT', 'EIVMTQSPAT', 'EIVLTQSPAT', 'EIVLTQSPAT', 'EIVLTQSPAT', 'EIVMTQSPAT', 
                           'EIVMMQSPAT', 'EIVMTQSPAT', 'EIVLTQSPAT', 'EIVLTQSPAT', 'EIVMTQSPAT'], 
                 'IGLV9': ['QPVLTQPPSA', 'QPVLTQPPSA', 'QPVLTQPPSA'], 
                 'IGLV3': ['SYELTQPPSV', 'SYELTQPPSV', 'SYELTQPPSV', 'SYELTQPPSV', 'SYELTQPPSV', 'SYELTQPHSV', 'SYELTQPHSV', 'SYELTQPPAV', 'SYELTQPPAV', 
                           'SYELTQPPSV', 'SSELTQDPAV', 'SSELTQDPAV', 'SYVLTQPPSV', 'SYVLTQPPSV', 'SYVLTQPPSV', 'SYVLTQPPSV', 'SYELTQLPSV', 'SYELTQLPSV', 
                           'SYELMQPPSV', 'SYELTQPPSV', 'SYELTQPPSV', 'SYELTQPSSV', 'SSELSQEPAV', 'SSELSQEPAV', 'SSGPTQVPAV', 'SYELTQPLSV', 'SYELTQPLSV'], 
                 'IGLV4': ['LPVLTQPPSA', 'QPVLTQSSSA', 'QPVLTQSSSA', 'QPVLTQSSSA', 'QLVLTQSPSA', 'QLVLTQSPSA'], 
                 'IGKV7': ['DIVLTQSPAS'], 
                 'IGLV10': ['QAGLTQPPSV', 'QAGLTQPPSV', 'QAGLTQPPSV', 'QAGLTQPPSV', 'QAGLTQPPSV', 'QAGLTQPPSV'], 
                 'IGKV4': ['DIVMTQSPDS', 'DIVMTQSPDS', 'DIVMTQSPDS'], 
                 'IGKV2': ['DIVMTQTPPS', 'DIVMTQTPLS', 'DIVMTQTPLS', 'DIVMTQSPLS', 'DIVMTQTPLS', 'DIVMTQTPLS', 'DIVMTQTPLS', 'DVVMTQSPLS', 'DVVMTQSPLS', 
                           'DIVMTQHLLS', 'DIVMTQHLLS', 'DIVMTQTPLS', 'ASISCRSSQS', 'DILLTQTPLS', 'DIVMTQTPLS', 'DIVMTQTPPS', 'DIVMTQTPLS', 'EIVMTQTPLS', 
                           'EIVMTQTPLS', 'EIVMTQTPLS', 'DIVMTQSPLS', 'DIVMTQTPLS', 'DIVMTQTPLS', 'DVVMTQSPLS', 'DIVMTQTPLS'], 
                 'IGLV7': ['QTVVTQEPSL', 'QAVVTQEPSL', 'QAVVTQEPSL', 'QAVVTQEPSL', 'QAVVTQEPSL'], 
                 'IGKV1': ['DIQMTQSPSS', 'DIQMTQSPSS', 'AIQLTQSPSS', 'AIQLTQSPSS', 'DIQMTQSPSS', 'DIQMTQSPSS', 'DIQMTQSPSS', 'DIQMTQSPSS', 'DIQMTQSPSA', 
                           'DIQMTQSPSS', 'DIQMTQSPSS', 'DIQMTQSPSS', 'DIQMTQSPSS', 'DIQLTQSPSS', 'DIQMTQSPSS', 'DIQMTQSPSF', 'DIQMTQSPST', 'DIQMTQSPST', 
                           'DIQMTQSPST', 'DIQMTQSPST', 'DIQMTQSPST', 'AIQMTQSPSS', 'AIQMTQSPSS', 'AIRMTQSPSS', 'AIRITQSPSS', 'AIRMTQSPSS', 'AIRMTQSPSS', 
                           'DIQLTQSPSF', 'DIQLTQSPSF', 'AIQLTQSPSS', 'DIQMTQSPSS', 'DIQMTQSPSS', 'DIQMTQSPSS', 'DIQMTQSPSS', 'DIQMTQSPSS', 'DIQMTQSPSS', 
                           'DIQMTQSPSS', 'DIQMTQSPSS', 'DIQMTQSPSS', 'DIQVTQSPSS', 'DIQMTQPPSS', 'DIQMTQSPSS', 'DIQMTQSPSS', 'DIQMTQPPSS', 'DIQMTQPPSS', 
                           'DIQMTQSPSS', 'DIQMTQSPSS', 'DIQMTQSPSS', 'DIQMTQSPSS', 'DIQMTQSPSS', 'DIQMTQSPSS', 'DIQMTQSPSS', 'AIQLTQSPSS', 'AIQLTQSPSS', 
                           'DIQMTQSPSS', 'DIQMTQSPSS', 'NIQMTQSPSA', 'DIQMTQSPSS', 'DIQLTQSPSS', 'DIQMTQSPSS', 'DIQMIQSPSF', 'DIQMTQSPSF', 'AIRMTQSPFS', 
                           'VIWMTQSPSL', 'AIWMTQSPSL', 'VIWMTQSPSL', 'VIWMTQSPSL'], 
                 'IGLV6': ['NFMLTQPHSV', 'NFMLTQPHSV', 'NFMLTQPHSV', 'NFMLTQPHSV'], 
                 'IGLV2': ['QSALTQPRSV', 'QSALTQPRSV', 'SVSGSPGQSV', 'QSALTQPASV', 'QSALTQPASV', 'QSALTQPASV', 'SVSGSPGQSI', 'QSALTQPASV', 'QSALTQPPSV', 
                           'QSALTQPPSV', 'QSALTQPPSV', 'QSALTQPPSV', 'QSALTQPASV', 'QSALTQPASV', 'QSALTQPASV', 'QSALTQPASV', 'QSALTQPPFV', 'QSALTQPPFV', 
                           'QSALTQPPFV', 'QSVLTQPRSV', 'QSVLTQPRSV', 'QSALIQPPSV', 'QSALIQPPSV', 'QSALTQPPSA', 'QSALTQPPSA', 'SASGSPGQSV', 'QSALTQPPSA'], 
                 'IGLV5': ['QPVLTQPPSS', 'QPVLTQPPSS', 'QPVLTQPPSS', 'QPVLTQPTSL', 'QPVLTQPTSL', 'QAVLTQPASL', 'QAVLTQPSSL', 'QAVLTQPSSL', 'QAVLTQPSSL', 
                           'QAVLTQLASL', 'QPVLTQPTSL', 'QAVLTQPTSL', 'QPVLTQPSSH'], 
                 'IGLV11': ['RPVLTQPPSL', 'RPVLTQPPSL'], 
                 'IGKV6': ['EIVLTQSPDF', 'EIVLTQSPDF', 'EIVLTQSPDF', 'EIVLTQSPDF', 'DVVMTQSPAF']}

MAP_GENE_SEED = {'IGLV1-36': ['QSVLTQPPSV'], 'IGLV1-40': ['QSVLTQPPSV', 'QSVVTQPPSV', 'QSVVTQPPSV'], 
                     'IGLV1-41': ['QSVLTQPPSV', 'QSVLTQPPSV'], 'IGLV1-44': ['QSVLTQPPSA', 'QSVLTQPPSA', 'QSVLTQPPSA', 'QSVLTQPPSA'], 
                     'IGLV1-47': ['QSVLTQPPSA', 'QSVLTQPPSA', 'QSVLTQPPSA'], 'IGLV1-50': ['QSVLTQPPSV'], 'IGLV1-51': ['QSVLTQPPSV', 'QSVLTQPPSV'], 
                     'IGLV1-62': ['QSVLTQPPSV'], 'IGLV10-54': ['QAGLTQPPSV', 'QAGLTQPPSV', 'QAGLTQPPSV', 'QAGLTQPPSV', 'QAGLTQPPSV', 'QAGLTQPPSV'], 
                     'IGLV11-55': ['RPVLTQPPSL', 'RPVLTQPPSL'], 'IGLV2-11': ['QSALTQPRSV', 'QSALTQPRSV', 'SVSGSPGQSV'], 
                     'IGLV2-14': ['QSALTQPASV', 'QSALTQPASV', 'QSALTQPASV', 'SVSGSPGQSI', 'QSALTQPASV'], 
                     'IGLV2-18': ['QSALTQPPSV', 'QSALTQPPSV', 'QSALTQPPSV', 'QSALTQPPSV'], 'IGLV2-23': ['QSALTQPASV', 'QSALTQPASV', 'QSALTQPASV', 'QSALTQPASV'], 
                     'IGLV2-33': ['QSALTQPPFV', 'QSALTQPPFV', 'QSALTQPPFV'], 'IGLV2-34': ['QSVLTQPRSV', 'QSVLTQPRSV'], 'IGLV2-5': ['QSALIQPPSV', 'QSALIQPPSV'], 
                     'IGLV2-8': ['QSALTQPPSA', 'QSALTQPPSA', 'SASGSPGQSV', 'QSALTQPPSA'], 'IGLV3-1': ['SYELTQPPSV', 'SYELTQPPSV'], 
                     'IGLV3-10': ['SYELTQPPSV', 'SYELTQPPSV', 'SYELTQPPSV'], 'IGLV3-12': ['SYELTQPHSV', 'SYELTQPHSV'], 'IGLV3-13': ['SYELTQPPAV', 'SYELTQPPAV'], 
                     'IGLV3-16': ['SYELTQPPSV'], 'IGLV3-19': ['SSELTQDPAV', 'SSELTQDPAV'], 'IGLV3-21': ['SYVLTQPPSV', 'SYVLTQPPSV', 'SYVLTQPPSV', 'SYVLTQPPSV'], 
                     'IGLV3-22': ['SYELTQLPSV', 'SYELTQLPSV'], 'IGLV3-25': ['SYELMQPPSV', 'SYELTQPPSV', 'SYELTQPPSV'], 'IGLV3-27': ['SYELTQPSSV'], 
                     'IGLV3-31': ['SSELSQEPAV', 'SSELSQEPAV'], 'IGLV3-32': ['SSGPTQVPAV'], 'IGLV3-9': ['SYELTQPLSV', 'SYELTQPLSV'], 'IGLV4-3': ['LPVLTQPPSA'], 
                     'IGLV4-60': ['QPVLTQSSSA', 'QPVLTQSSSA', 'QPVLTQSSSA'], 'IGLV4-69': ['QLVLTQSPSA', 'QLVLTQSPSA'], 'IGLV5-37': ['QPVLTQPPSS', 'QPVLTQPPSS', 'QPVLTQPPSS'], 
                     'IGLV5-39': ['QPVLTQPTSL', 'QPVLTQPTSL'], 'IGLV5-45': ['QAVLTQPASL', 'QAVLTQPSSL', 'QAVLTQPSSL', 'QAVLTQPSSL', 'QAVLTQLASL'], 
                     'IGLV5-48': ['QPVLTQPTSL', 'QAVLTQPTSL'], 'IGLV5-52': ['QPVLTQPSSH'], 'IGLV6-57': ['NFMLTQPHSV', 'NFMLTQPHSV', 'NFMLTQPHSV', 'NFMLTQPHSV'], 
                     'IGLV7-43': ['QTVVTQEPSL'], 'IGLV7-46': ['QAVVTQEPSL', 'QAVVTQEPSL', 'QAVVTQEPSL', 'QAVVTQEPSL'], 'IGLV8-61': ['QTVVTQEPSF', 'QTVVTQEPSF', 'VTQEPSFSVS'], 
                     'IGLV8/OR8-1': ['QSVVTQEPSL'], 'IGLV9-49': ['QPVLTQPPSA', 'QPVLTQPPSA', 'QPVLTQPPSA'], 'IGKV1-12': ['DIQMTQSPSS', 'DIQMTQSPSS'], 
                     'IGKV1-13': ['AIQLTQSPSS', 'AIQLTQSPSS'], 'IGKV1-16': ['DIQMTQSPSS', 'DIQMTQSPSS'], 'IGKV1-17': ['DIQMTQSPSS', 'DIQMTQSPSS', 'DIQMTQSPSA'], 
                     'IGKV1-27': ['DIQMTQSPSS', 'DIQMTQSPSS', 'DIQMTQSPSS'], 'IGKV1-33': ['DIQMTQSPSS'], 'IGKV1-37': ['DIQLTQSPSS'], 'IGKV1-39': ['DIQMTQSPSS', 'DIQMTQSPSF'], 
                     'IGKV1-5': ['DIQMTQSPST', 'DIQMTQSPST', 'DIQMTQSPST', 'DIQMTQSPST', 'DIQMTQSPST'], 'IGKV1-6': ['AIQMTQSPSS', 'AIQMTQSPSS'], 
                     'IGKV1-8': ['AIRMTQSPSS', 'AIRITQSPSS', 'AIRMTQSPSS', 'AIRMTQSPSS'], 'IGKV1-9': ['DIQLTQSPSF', 'DIQLTQSPSF', 'AIQLTQSPSS'], 
                     'IGKV1-NL1': ['DIQMTQSPSS'], 'IGKV1/OR-2': ['DIQMTQSPSS'], 'IGKV1/OR-3': ['DIQMTQSPSS'], 'IGKV1/OR-4': ['DIQMTQSPSS'], 'IGKV1/OR1-1': ['DIQMTQSPSS'], 
                     'IGKV1/OR10-1': ['DIQMTQSPSS'], 'IGKV1/OR15-118': ['DIQMTQSPSS'], 'IGKV1/OR2-0': ['DIQMTQSPSS'], 'IGKV1/OR2-1': ['DIQMTQSPSS'], 'IGKV1/OR2-108': ['DIQVTQSPSS'], 
                     'IGKV1/OR2-11': ['DIQMTQPPSS'], 'IGKV1/OR2-118': ['DIQMTQSPSS'], 'IGKV1/OR2-2': ['DIQMTQSPSS'], 'IGKV1/OR2-3': ['DIQMTQPPSS'], 'IGKV1/OR2-9': ['DIQMTQPPSS'], 
                     'IGKV1/OR22-5': ['DIQMTQSPSS', 'DIQMTQSPSS'], 'IGKV1/OR9-1': ['DIQMTQSPSS'], 'IGKV1/OR9-2': ['DIQMTQSPSS'], 'IGKV1/ORY-1': ['DIQMTQSPSS'], 
                     'IGKV1D-12': ['DIQMTQSPSS', 'DIQMTQSPSS'], 'IGKV1D-13': ['AIQLTQSPSS', 'AIQLTQSPSS'], 'IGKV1D-16': ['DIQMTQSPSS', 'DIQMTQSPSS'], 'IGKV1D-17': ['NIQMTQSPSA'], 
                     'IGKV1D-33': ['DIQMTQSPSS'], 'IGKV1D-37': ['DIQLTQSPSS'], 'IGKV1D-39': ['DIQMTQSPSS'], 'IGKV1D-42': ['DIQMIQSPSF', 'DIQMTQSPSF'], 'IGKV1D-43': ['AIRMTQSPFS'], 
                     'IGKV1D-8': ['VIWMTQSPSL', 'AIWMTQSPSL', 'VIWMTQSPSL', 'VIWMTQSPSL'], 'IGKV2-18': ['DIVMTQTPPS'], 'IGKV2-24': ['DIVMTQTPLS', 'DIVMTQTPLS'], 'IGKV2-28': ['DIVMTQSPLS'], 
                     'IGKV2-29': ['DIVMTQTPLS', 'DIVMTQTPLS', 'DIVMTQTPLS'], 'IGKV2-30': ['DVVMTQSPLS', 'DVVMTQSPLS'], 'IGKV2-4': ['DIVMTQHLLS', 'DIVMTQHLLS'], 
                     'IGKV2-40': ['DIVMTQTPLS', 'ASISCRSSQS'], 'IGKV2/OR2-7D': ['DILLTQTPLS'], 'IGKV2/OR22-4': ['DIVMTQTPLS'], 'IGKV2D-18': ['DIVMTQTPPS'], 
                     'IGKV2D-24': ['DIVMTQTPLS'], 'IGKV2D-26': ['EIVMTQTPLS', 'EIVMTQTPLS', 'EIVMTQTPLS'], 'IGKV2D-28': ['DIVMTQSPLS'], 'IGKV2D-29': ['DIVMTQTPLS', 'DIVMTQTPLS'], 
                     'IGKV2D-30': ['DVVMTQSPLS'], 'IGKV2D-40': ['DIVMTQTPLS'], 'IGKV3-11': ['EIVLTQSPAT', 'EIVLTQSPAT'], 'IGKV3-15': ['EIVMTQSPAT', 'EIVMTQSPAT'], 
                     'IGKV3-20': ['EIVLTQSPGT', 'EIVLTQSPAT'], 'IGKV3-7': ['EIVMTQSPPT', 'EIVMTQSPPT', 'EIVMTQSPPT', 'EIVMTQSPPT', 'EIVMTQSPPT', 'EIVMAQSPPT'], 
                     'IGKV3/OR2-268': ['EIVMTQSPAT', 'EIVMTQSPAT'], 'IGKV3D-11': ['EIVLTQSPAT', 'EIVLTQSPAT', 'EIVLTQSPAT'], 'IGKV3D-15': ['EIVMTQSPAT', 'EIVMMQSPAT', 'EIVMTQSPAT'], 
                     'IGKV3D-20': ['EIVLTQSPAT', 'EIVLTQSPAT'], 'IGKV3D-7': ['EIVMTQSPAT'], 'IGKV4-1': ['DIVMTQSPDS', 'DIVMTQSPDS', 'DIVMTQSPDS'], 'IGKV5-2': ['ETTLTQSPAF', 'ETTLTQSPAF'], 
                     'IGKV6-21': ['EIVLTQSPDF', 'EIVLTQSPDF'], 'IGKV6D-21': ['EIVLTQSPDF', 'EIVLTQSPDF'], 'IGKV6D-41': ['DVVMTQSPAF'], 'IGKV7-3': ['DIVLTQSPAS']}

# Definitions for liabilities
LIST_LIABILITIES = ["N-linked glycosylation (NXS/T X not P),fv,N[^P][ST]",
                    "Met oxidation (M),cdrs;verniers,M",
                    "Trp oxidation (W),cdrs;verniers,W",
                    "Asn deamidation (NG NS NT),cdrs;verniers,N[GST]",
                    "Asp isomerisation (DG DS DT DD DH),cdrs;verniers,D[GSTDH]",
                    "Lysine Glycation (KE KD EK ED),cdrs;verniers,KE|KD|EK|ED",
                    "N-terminal glutamate (VH and VL) (E),nterminus,E",
                    "Integrin binding (RGD RYD LDV),fv,RGD|RYD|LDV",
                    "CD11c/CD18 binding (GPR),fv,GPR",
                    "Fragmentation (DP),cdrs;verniers,DP"]
IMGT_LVERNIERS =[4, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 41, 42, 52, 53, 55, 84, 94, 118]
IMGT_CDR1 = list(range(27, 38+1))
IMGT_CDR2 = list(range(56, 65+1))
IMGT_CDR2 = list(range(105, 117+1))
IMGT_CDRs = [IMGT_CDR1, IMGT_CDR2, IMGT_CDR2]

class FILTERING():
    """Initialise FILTERING"""

    def __init__(self, device, ncpu):
        super().__init__()
        # Install anarcii
        try:
            from anarcii import Anarcii
            import io
            import sys
        except ImportError as e:
            raise ImportError(
                """
                ANARCII is required to run this function.
                Please install it using the instructions in the README.
                """
            ) from e
        # Run ANARCII while silencing its output
        text_trap = io.StringIO()
        sys.stdout = text_trap
        self.anarcii_model = Anarcii(seq_type="antibody", batch_size=1, cpu=True, ncpu=ncpu, mode="speed", verbose=False)
        sys.stdout = sys.__stdout__

        # Install AbLang2
        try:
            import ablang2
            import warnings
        except ImportError as e:
            raise ImportError(
                """
                AbLang2 is required to run this function.
                Please install it using the instructions in the README.
                """
            ) from e
        # Ignore UserWarning    
        warnings.filterwarnings("ignore", category=FutureWarning)
        self.ablang2_model = ablang2.pretrained(ncpu=ncpu, device=device)
        
        
    def passing_anarcii_filtering(self, generated_light_sequence, light_cdr, light_cdr_scheme):
        """Run ANARCII and determine if the sequence can be numbered and is recognised
        as a light chain. If CDRs are provided correctness of grafting into the 
        generated sequence is checked.
    
        Parameter
        ---------
        generated_light_sequence : str
            The generated light seqeunce
        light_cdr :  None or list
            Containing the CDRs.
        light_cdr_scheme : 'IMGT' or 'Kabat'
            The numbering scheme definition of the CDRs.
        """
        sequence = [('generated_light', generated_light_sequence)]
        results =  self.anarcii_model.number(sequence)
        legacy_format = self.anarcii_model.to_legacy()

        numbering, alignment_details, _ = legacy_format
        
        if not numbering[0]:
            return False
        elif alignment_details[0][0]['chain_type'] not in ['K', 'L']: # Could be 'H' for heavy and 'F' for failing
            return False
        else:
            if light_cdr:
                # Check generated CDRs are provided CDRS
                cdr1_gen, cdr2_gen, cdr3_gen = self._extract_cdrs(numbering[0][0][0], light_cdr_scheme) # this is a list of the format: [((1, ' '), 'D'), ((2, ' '), 'I') ..]
                if light_cdr[0] and light_cdr[0] != cdr1_gen:
                    return False
                if light_cdr[1] and light_cdr[1] != cdr2_gen:
                    return False
                if light_cdr[2] and light_cdr[2] != cdr3_gen:
                    return False
                else:
                    return True
            else:
                # Passed the ANARCI test and CDRs not given
                return True

    def _extract_cdrs(self, sequence_numbering, light_cdr_scheme):
        """Given a number sequence, determine the CDRs according to CDR definition
        of provided numbering scheme.
        
        Parameters
        ----------
        sequence_numbering : list
            ANARCII numbered sequence.
        light_cdr_scheme : 'IMGT' or 'Kabat'
            The numbering scheme definition of the CDRs.
        """
        if light_cdr_scheme == 'Kabat':
            cdr1_pos = list(range(24, 40+1))
            cdr2_pos = list(range(56, 69+1))
            cdr3_pos = list(range(105, 117+1))
        else:
            # IMGT defintion
            cdr1_pos = list(range(27, 38+1))
            cdr2_pos = list(range(56, 65+1))
            cdr3_pos = list(range(105, 117+1))
            
        cdr1_gen, cdr2_gen, cdr3_gen = '', '', ''
        for number in sequence_numbering:
            if number[0][0] in cdr1_pos:
                cdr1_gen += number[1]
            elif number[0][0] in cdr2_pos:
                cdr2_gen += number[1]
            elif number[0][0] in cdr3_pos:
                cdr3_gen += number[1]
        # Remove the '-' indicating no amino acid
        return cdr1_gen.replace('-', ''), cdr2_gen.replace('-', ''), cdr3_gen.replace('-', '')
    
    def passing_humatch(self, generated_light_sequence):
        """Run Humatch to determine if the generated sequence is human.
        Human is defined if the Humatch score for a light V-gene
        is higher than 0.95."""

        try:
            import os
            import importlib.resources as pkg_resources
            from Humatch.align import get_padded_seq
            from Humatch.model import load_cnn
            from Humatch.classify import predict_from_list_of_seq_strs, get_class_and_score_of_max_predictions_only
        except ImportError as e:
            raise ImportError(
                """
                Humatch is required to run this function.
                Please install it using the instructions in the README.
                """
            ) from e

        light_seq_pad = get_padded_seq(generated_light_sequence)
        base_path = str(pkg_resources.files("lichen")).split('/src')[0]
        weights_dir = os.path.join(base_path, "Humatch", "Humatch", "trained_models")
        cnn_light = load_cnn(os.path.join(weights_dir, "light.weights.h5"), "light")
        predictions_light = predict_from_list_of_seq_strs([light_seq_pad], cnn_light)
        output_humatch = get_class_and_score_of_max_predictions_only(predictions_light, "light")
        threshold = 0.95
        if output_humatch[0][1]>threshold and output_humatch[0][0][0] in ['k', 'l']:
            return True
        else:
            return False
    
    def AbLang2_confidence(self, list_lights, n):
        """Calculates the confidence (log likelihood) of the light sequences
        according to AbLang2.
        """
        list_sequences = [['', x] for x in list_lights]
        
        # Calculate the confidence
        results = self.ablang2_model(list_sequences, mode='confidence')
        confidence = np.exp(-results)
        
        # Add confidence to the dataframe
        df = pd.DataFrame({'light_sequence': list_lights, 'AbLang2_confidence': confidence})
        df = df.sort_values(by='AbLang2_confidence', ascending=False)[:n]

        return df['light_sequence'].to_list()

    def diversity_AbLang2(self, list_lights, n):
        """Calculates the confidence (log likelihood) of the light sequences
        according to AbLang2 and select most diverse light sequences based
        on these scores.
        """
        list_sequences = [['', x] for x in list_lights]
        
        # Calculate the confidence
        results = self.ablang2_model(list_sequences, mode='confidence')
        confidence = np.exp(-results)
        
        # Add confidence to the dataframe to pair light sequence and score
        df = pd.DataFrame({'light_sequence': list_lights, 'AbLang2_confidence': confidence})

        # Sort and select evenly spaced values
        all_scores = df['AbLang2_confidence'].to_list()
        all_scores.sort()
        idx = np.round(np.linspace(0, len(all_scores) - 1, n)).astype(int)
        return [df[df['AbLang2_confidence']==all_scores[i]].iloc[0]['light_sequence'] for i in idx]
    
def get_liabilities(light_seq_numbered: dict, liabilities: list, vernier: list, cdr: list):
    """Check for liabilties in the light chain sequences.
    Liabilties might be checked in the full VL, the CDRs or the vernier zone.
    
    Parameters
    ----------
    light_seq_numbered : dict
        Mapping IMGT number (including insertions) to residues
    liabilties : list
        List of liabilities each element has the format: name, region, regex
    vernier : list
        Containing IMGT positions beloning to vernier region
    cdr : list
        Containing IMGT positions belonging to CDR regions. 
    """
    import re
    
    output_liabilities = []
    for liability in liabilities:
        name, region, regex = liability.split(",")
        if region == 'fv':
            positions_to_consider = list(range(1,128+1))
        elif region == 'cdrs;verniers':
            positions_to_consider = vernier + cdr
        elif region == 'cdrs':
            positions_to_consider = cdr
        elif region == 'verniers':
            positions_to_consider = vernier
        elif region == 'nterminus':
            positions_to_consider = [1]
        else:
            print(f'{region} unknown')
            output_liabilities.append(None)
            continue

        sequence_to_consider = ''
        positions_to_consider.sort() # sort the positions list
        for pos, aa in light_seq_numbered.items():
            try:
                if int(re.search(r'\d+', pos).group()) in positions_to_consider:
                    sequence_to_consider += aa
                else:
                    sequence_to_consider += '-' # Keep these because if checking multiple consecutive aa we need to keep the order   
            except AttributeError:
                print(f'AttributeError: {pos}, {aa}')
                return None
                
        x = re.findall(regex, sequence_to_consider)
        output_liabilities.append(len(x)) # store number of observed cases of this liability
    return output_liabilities

def get_sequence_liabilities(input: Union[List, pd.DataFrame], 
                             ncpu: int =1):
    """Get sequence liabilities for the generated light sequences.

    Parameters
    ----------
    input : List pd.DataFrame
        Generated sequences for which liabilities need to be determined
    ncpu : int
        Number of CPU used for ANARCII
    """

    try:
        from anarcii import Anarcii
    except ImportError as e:
        raise ImportError(
            """
            ANARCII is required to run this function.
            Please install it using the instructions in the README.
            """
        ) from e

    # Load and run ANARCII
    anarcii_model = Anarcii(seq_type="antibody", batch_size=128, cpu=True, ncpu=ncpu, mode="accuracy", verbose=False)
    if type(input) != list:
        sequences = input['generated_light'].to_list()
    else:
        sequences = input
    anarcii_result = anarcii_model.number(sequences)

    # Extract the numbering
    list_numbering = []
    for k, v in anarcii_result.items():
        numbering_list = v['numbering']
        dict_num = {}
        for el in numbering_list:
            if el[1]!='-':
                dict_num[f'{el[0][0]}{el[0][1]}'.strip()] = el[1]
        list_numbering.append(dict_num)

    # Store output in a Dataframe
    if type(input) != list:
        df = input.copy()
        df['IMGT_numbering'] = list_numbering
    else:
        df = pd.DataFrame({'generated_light': sequences,
                          'IMGT_numbering': list_numbering})
        
    # # Get liabilities
    liability_names = [x.split(',')[0] for x in LIST_LIABILITIES]
    df[liability_names] = df.apply(lambda row: get_liabilities(row.IMGT_numbering, LIST_LIABILITIES, IMGT_LVERNIERS, [j for i in IMGT_CDRs for j in i]) if row['IMGT_numbering'] is not None else [None]*len(LIST_LIABILITIES), axis='columns', result_type='expand')

    return df