🇪🇹 Ethiopia Financial Inclusion Forecast (2025–2027)
Project Overview
This project provides a data-driven forecast of financial inclusion in Ethiopia, focusing on the national goal of reaching 70% account ownership by 2027. Using historical data from 2004–2024, the analysis identifies growth drivers (like mobile money and the Fayda ID) and examines the significant gender and urban-rural gaps.

📂 Repository Structure
Plaintext
├── data/               # Raw and unified datasets (CSV/XLSX)
├── docs/               # Technical documentation & data enrichment logs
├── notebooks/          # Jupyter notebooks for EDA and Forecasting
├── venv/               # Python virtual environment (ignored by git)
├── requirements.txt    # Project dependencies
└── README.md           # You are here!
🛠️ Installation & Setup
Clone the repo: git clone <your-repo-url>

Setup Environment: ```powershell python -m venv venv .\venv\Scripts\activate pip install -r requirements.txt


📈 Key Insights (Current Progress)
The 3% Slowdown: Despite the rise of digital banking, account ownership only grew from 46% (2021) to 49% (2024).

Target Gap: To reach 70% by 2027, the growth rate must accelerate significantly from its current trajectory.

Enrichment: Data has been enriched with confidence scores and metadata to ensure forecasting accuracy.

🧪 Methodology
Data Cleaning: Unified disparate sources (World Bank Findex, NBE Reports).

EDA: Visualized historical trends and identified the "plateau" in rural adoption.

Forecasting (Upcoming): Implementing time-series models to predict 2025–2027 outcomes under different policy scenarios.

📝 Documentation
Detailed records of data modifications and source validation can be found in: docs/data_enrichment_log.md