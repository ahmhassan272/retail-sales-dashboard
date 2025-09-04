# Tableau Calculated Fields

Use these to enrich your visuals:

## Order Date (Month)
```
DATETRUNC('month', [Order Date])
```

## Profit Ratio
```
SUM([Profit]) / SUM([Sales])
```

## YoY Sales Growth
> Place this on a table or line chart with a month dimension; requires a proper table calculation setup.
```
(SUM([Sales]) - LOOKUP(SUM([Sales]), -12)) / LOOKUP(SUM([Sales]), -12)
```

## Top N Parameter (optional)
1. Create a parameter **Top N** (integer, current value 10).
2. Create a set or filter that keeps **Top N** products by SUM([Sales]).
