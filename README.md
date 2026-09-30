# SWEAT tutorials

## Objective

Gain an overview of the approaches and tools developed by the TRISHNA Ecosystem Stress group for estimating evapotranspiration and water stress in ecosystems.

## Tutorial content

### What is the TRISHNA mission?

- Description of the mission characteristics and instruments.
- Description of the products distributed, particularly products for estimating biophysical variables.

### How is evapotranspiration estimated in TRISHNA?

- Introduction to evapotranspiration
- Description of the evapotranspiration algorithms selected for the TRISHNA mission:
   
  - STIC (Surface Temperature Initiated Closure)
  - EVASPA (EVapotranspiration Assessment from SPAce)
    
- Presentation of their advantages and limitations.
- Presentation of SWEAT (Spatial Waterstress Evapotranspiration Assessment for TRISHNA)
- Exploring these algorithms through notebooks to understand how they work and how to interpret their results.

### From daily product to time series 

- Description of the calculation of evapotranspiration time series.
- Presentation of the algorithm used for interpolation and extrapolation, using notebooks.


## Tutorial instruction

### Prerequisites

Software to install

- git
- pixi

### Installation

*For Windows users, please use the PowerShell terminal*

#### Clone this repository

```bash
git clone https://github.com/esarrazin/sweat-tutorials.git
```

#### Install

1. Access to the directory
```bash
cd sweat-tutorials
```

2. Install the environment
```bash
pixi install
```

##### Troubleshooting for MacOS

*For MacOS users, if you encounter problem with openmp during installation.*

*Install LLVM via brew*
```bash
brew install llvm libomp
```

*Export variables to define paths to Clang and related libraries installed*
```bash
export CC=/opt/homebrew/opt/llvm/bin/clang
export CXX=/opt/homebrew/opt/llvm/bin/clang++
export LDFLAGS="-L/opt/homebrew/opt/llvm/lib -L/opt/homebrew/opt/libomp/lib"
export CPPFLAGS="-I/opt/homebrew/opt/llvm/include -I/opt/homebrew/opt/libomp/include"
```

### Run jupyter notebook

Navigate to the tutorial directory

1. Activate the environment
```bash
pixi shell
```

2. Launch jupyter lab
```bash
jupyter lab
```


