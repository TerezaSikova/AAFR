# AAFR (Ali Alagrami Fresco Reconstruction)

# 1) Description
This repository is a fork of the [AAFR](https://github.com/RePAIRProject/AAFR) (Ali Alagrami Fresco Reconstruction, Reassembling Broken Objects using Breaking Curves) framework, originally developed within the [RePAIR project](https://www.repairproject.eu/).

This fork has been adapted and extended slightly for my bachelor's thesis, particularly in the context of testing on additional datasets.

For more details, including data preparation or installation steps, please refer to the original project's [README](https://github.com/RePAIRProject/AAFR/blob/master/README.md) file.

# 2) Installation insights
I ran on Ubuntu 24.10 with Python 3.12.7.
To ensure smooth installation, I modified the `requirements.txt` file (particularly the numpy version).

# 3) Demo Run

You can test the reassembly process on several prepared examples:
- DrinkBottle (for comparison with the original pipeline)
- WineGlass (to get correct results, run with the --mode SB flag for segmenting breaking curves as well as regular points)
- FigurineS4 (successful reassembly on a custom dataset)
- Pot (example of a failed breaking curves detection and therefore unsuccessful reassembly on a custom dataset)

Data sources: 
- DrinkBottle, WineGlass: [Breaking Bad dataset](https://breaking-bad-dataset.github.io/)
- Pot, FigurineS4: provided by the Department of Archaeology and Museology at Masaryk University

To run your chosen demo, use the following script:
```bash
python assemble_fragments.py --cfg assemble_cfg_demo --demo EXAMPLE_NAME --f FAST
```

And for the WineGlass:

```bash
python assemble_fragments.py --cfg assemble_cfg_demo --demo WineGlass --f FAST --mode SB
```

You can also run the script without the --f FAST flag, which will use the default (slower) reassembly code.

For more details on the output format and the results in the `results` folder, refer to the original authors' demo in the [demo file](demo.md).