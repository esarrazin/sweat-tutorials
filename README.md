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

### Run jupyter notebook

1. Access to the directory
```bash
cd sweat-tutorials
```

2. Activate the environment
```bash
pixi shell
```

3. Launch jupyter lab
```bash
jupyter lab
```


