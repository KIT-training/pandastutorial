import pandas as pd

# link = 'https://docs.google.com/spreadsheets/d/1m2O4UXtTvBvphlgmRKGshrq8-s5fSb8GCdRoL9YAWTY/edit?usp=sharing'
sheet_name = 'Musung PC info'
sheet_id = '1m2O4UXtTvBvphlgmRKGshrq8-s5fSb8GCdRoL9YAWTY'
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"



data = pd.read_csv(url)
print(data)