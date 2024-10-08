Sure! Here's a `README.md` file for your GitHub project:

---

# Estimating Bitcoin Volatility

This repository contains three Jupyter notebooks derived from three [blog posts](https://zaltarba.github.io/blog/BitcoinVolatility-1/) about estimating Bitcoin volatility. It also includes a Python script to fetch the required data necessary for the analyses.

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Data Fetching](#data-fetching)
- [Usage](#usage)
- [Notebooks Overview](#notebooks-overview)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Bitcoin, as a digital asset, exhibits significant price volatility. Understanding and estimating this volatility is crucial for investors, traders, and researchers. This project provides a comprehensive analysis through three detailed Jupyter notebooks, each corresponding to a specific method or approach discussed in individual blog posts.

## Project Structure

- `notebooks/`: Contains the three Jupyter notebooks.
- `data/`: Directory where the fetched data will be stored.
- `fetch_data.py`: Python script to download the required Bitcoin data.
- `requirements.txt`: Lists all the Python packages required to run the notebooks.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/bitcoin-volatility-estimation.git
   cd bitcoin-volatility-estimation
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

## Data Fetching

Before running the notebooks, you need to fetch the Bitcoin data:

```bash
python fetch_data.py
```

This script will download the necessary data and save it in the `data/` directory.

## Usage

1. **Launch Jupyter Notebook:**

   ```bash
   jupyter notebook
   ```

2. **Open the notebooks:**

   Navigate to the `notebooks/` directory and open the notebook you're interested in.

3. **Run the analyses:**

   Execute the cells sequentially to reproduce the results.

## Notebooks Overview

### 1. Notebook 1: **Estimating Bitcoin's Volatility Using EWMA**

- **Description:** Explores how to estimate Bitcoin's realized volatility with the EWMA estimator
- **Contents:**
  - Data preprocessing
  - Methodology explanation
  - Results and visualizations

### 2. Notebook 2: **Estimating Bitcoin's Volatility using a GARCH Model**

- **Description:** Dive into the second part of our three-part series on computing Bitcoin's volatility with Binance data.
- **Contents:**
  - Data preprocessing
  - Model Selection
  - Model Interpretation
  - Goodness of fit checks
  - Estimation and Forecasting
- **Purpose:** Build upon the first notebook to provide deeper insights on Bitcoin Volatility with this time a GARCH model framework.

## Dependencies

The project requires the following Python packages:

```plaintext
matplotlib==3.7.2
pandas==2.1.0
numpy==1.25.2
requests==2.31.0
```

These are listed in the `requirements.txt` file and can be installed using the command provided in the [Installation](#installation) section.

## Contributing

Contributions are welcome! If you have suggestions for improvements or find any issues, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
