# Bitcoin Price Analysis & NBA Team Data Exploration

## Overview
This Python script performs two main tasks:
1. Fetches and processes **Bitcoin price data** using the CoinGecko API to create a **candlestick-like dataset**.
2. Extracts **NBA team and game data** using the NBA API and visualizes team performance.

## Features
- Fetches the **last 30 days of Bitcoin price data** in USD using the `pycoingecko` library.
- Converts timestamps to readable dates and creates a **candlestick dataset** showing daily price movements (min, max, open, close).
- Retrieves the list of **NBA teams** using `nba_api.stats.static` and converts it into a structured DataFrame.
- Filters data to focus on the **Golden State Warriors** (or any other specified team).
- Fetches recent games played by the selected team and **visualizes performance trends**.

## Prerequisites
Ensure you have the required Python packages installed:
```bash
pip install pandas matplotlib pycoingecko nba_api
```

## Usage
Run the script using:
```bash
python script.py
```

### Expected Output:
- A **DataFrame** displaying Bitcoin price trends.
- A **filtered DataFrame** showing NBA teams.
- A **game statistics plot** displaying `Plus_Minus` for home and away games.

## Issues & Improvements
- **Bug in `groupby()` function**: `data.groupby(data.Date.dt.data)` should use `.dt.date` instead of `.dt.data`.
- **Incorrect variable reference (`id_warriors`)**: Should be extracted properly from `df_warriors`.
- **Game plots (`games_home` and `games_away`)**: They need correct filtering before plotting.

## Contributions
Feel free to contribute by fixing bugs, optimizing API calls, or adding more data visualizations.

## License
This project is open-source under the MIT License.
