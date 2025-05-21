# AAFR (Ali Alagrami Fresco Reconstruction)

# 1) Description
This repository is a fork of the [AAFR](https://github.com/RePAIRProject/AAFR) (Ali Alagrami Fresco Reconstruction, Reassembling Broken Objects using Breaking Curves) framework, originally developed within the [RePAIR project](https://www.repairproject.eu/).

This fork has been adapted and extended slightly for the purposes of my bachelor's thesis, particularly in the context of testing on additional datasets.

For more details, including data preparation or installation steps, please refer to the original project’s [README](https://github.com/RePAIRProject/AAFR/blob/master/README.md) file. 
This page provides demo instructions, and a summary of relevant adjustments made for this fork.

# 2) Installation insights
This fork was run on Ubuntu 24.10 with Python 3.12.7.
To ensure smooth installation, I modified the requirements.txt file.

# 3) Demo Run

You can test the reassembly process on several prepared examples:
- DrinkBottle
- Statue
- RePAIR Fresco
- FigurineS3
- FigurineS4
- Pot
- DAM Fresco

Data sources: 
- DrinkBottle, Statue: [breaking bad dataset](https://breaking-bad-dataset.github.io/)
- RePAIR Fresco: [repair dataset](https://drive.google.com/drive/folders/1G4ffmH5lxEqITZMNValiModByYUAO6yk)
- FigurineS3, FigurineS4, Pot, DAM Fresco: provided by the Department of Archaeology and Museology at Masaryk University

To run your chosen demo, use the following script:
```bash
python assemble_fragments.py --cfg assemble_cfg_demo --demo EXAMPLE_NAME --f FAST
```

You can also run the script without the --f FAST flag, which will use the default (slower) reassembly code.

For more details on the output format and the results available in the results folders, refer to the original authors' demo in the [demo file](demo.md).