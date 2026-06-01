========================================================================
INDIASHIELD - DATA ACQUISITION & FORMATTING GUIDE
========================================================================

IndiaShield is built to read military spending and arms transfer data
directly from files or fall back to high-fidelity internal estimates.
To load full external databases, follow these manual setup steps:

1. SIPRI MILITARY EXPENDITURE DATABASE
-------------------------------------
- URL: https://sipri.org/databases/milex
- Download: "SIPRI-Milex-data-1949-2024.xlsx"
- Target Sheet: "Constant (2022) USD"
- Action:
  * Open the Excel file.
  * Extract rows for the following countries:
    India, China, Pakistan, United States, Russia, France, United Kingdom,
    Israel, Saudi Arabia, Germany, Japan, Australia.
  * Keep the "Country" column and years 2000 through 2024.
  * Save the filtered rows as a CSV file.
- Save Destination: data/raw/sipri_milex.csv
- Expected Headers: Country,2000,2001,2002,...,2024

2. SIPRI ARMS TRANSFER DATABASE
-------------------------------
- URL: https://sipri.org/databases/armstransfers
- Export filters:
  * Recipient: India
  * Years: 2000-2024
- Action:
  * Query the database and download the export file (CSV or Excel).
  * Ensure the following columns exist: Year, Supplier, Recipient, Armament, SIPRI_TIV.
- Save Destination: data/raw/sipri_arms_transfer.csv
- Expected Headers: Year,Supplier,Recipient,Armament,SIPRI_TIV
