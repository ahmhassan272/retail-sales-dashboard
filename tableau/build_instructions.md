# Tableau Build Instructions (Step-by-step)

> Goal: Build a clean dashboard with 4 views — Sales over Time, Sales by Category, Top 10 Products, and Sales Map.

## 0) Connect Data
- Open **Tableau Public** → *Connect* → choose your `data/superstore.csv` or Excel file.
- Verify fields: dates recognized as Date, Sales/Profit as Number (decimal).

---

## 1) Sheet: Sales over Time
1. Drag **Order Date** to *Columns* → right-click → choose **Month**.
2. Drag **Sales** to *Rows*.
3. Change mark type to **Line**.
4. Format:
   - Title: *Sales Over Time*
   - Add a filter for **Order Date** (range) to use on dashboard.
   - Optional: add a **moving average** from the Analytics pane.

---

## 2) Sheet: Sales by Category
1. Drag **Category** to *Rows*.
2. Drag **Sales** to *Columns*.
3. Sort descending.
4. Add **Profit Ratio** (calculated field) to *Tooltip*.
5. Title: *Sales by Category*.

---

## 3) Sheet: Top 10 Products
1. Drag **Product Name** to *Rows*.
2. Drag **Sales** to *Columns*.
3. Sort descending.
4. Create a **Top N** parameter (default 10).
5. Create a filter: keep Top N by SUM([Sales]).
6. Title: *Top 10 Products*.

---

## 4) Sheet: Sales Map
1. Ensure **Country/State/City** are geographic (globe icon). If not, set the **Geographic Role**.
2. Drag **State** (or City) to the canvas—Tableau will render a map.
3. Drag **Sales** to *Color*, **Profit Ratio** to *Tooltip*.
4. Title: *Sales by Region*.

---

## 5) Assemble the Dashboard
1. Create a **Dashboard** (size ~1200 × 800).
2. Place the four sheets in this order: Time (top-left), Category (top-right), Top Products (bottom-left), Map (bottom-right).
3. Add filters (Date, Category, Region) and set them to apply to **Selected sheets** or **All using this data source**.
4. Clean styling: concise titles, sorted bars, gridlines off, readable axis.
5. **Publish** to Tableau Public; copy the link into your GitHub README.

---

## Tips
- Keep it minimal: fewer colors, clear labels, consistent fonts.
- Always sort bars; people read rankings faster than unsorted charts.
- Make tooltips useful: show Sales, Profit, Profit Ratio, and Quantity.
