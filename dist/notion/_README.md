# Notion version — import guide

1. In Notion: `Import` → `CSV` → select each file in this folder.
2. Each becomes a database. Set property types:
   - Date → Date · Fee/Amount/Miles → Number · Status/Category → Select · Paid/Deductible → Checkbox
3. Add these **formula** properties inside Notion:
   - Signing Log → `Net profit` = `prop("Fee paid") - (prop("Miles") * 0.70) - (prop("Print pages") * 0.1) - prop("Other cost")`
     (replace 0.70 with the current IRS mileage rate)
   - Mileage Log → `Deduction` = `prop("Miles") * 0.70`
4. Create linked views: 'Unpaid' (filter Status = Invoiced), 'This month', 'By company'.
5. Build a Dashboard page with linked databases + `Sum` rollups for fees, profit and miles.
