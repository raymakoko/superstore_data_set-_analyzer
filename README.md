# Superstore Profit Prediction
## Introduction:
The Superstore dataset contains 9,994 retail transaction across  the  us from 2014-2017. 
The goal of this project is  to understand  the drivers of Profit and build a predictive model that can flag at-risk orders before they are fulfilled

## EDA summary
Key findings from our exploratory analysis:
- Profit rises with sales, but the relationship is not linear; several low-sales transactions produce negative profit, showing that revenue alone is not enough to guarantee margin.
- Discounts appear to be a major margin pressure point, with higher discount bands showing weaker average profitability.
- Categories and regions are not equally profitable, which suggests that product mix and market focus can materially affect results.
- The time-series view shows that profitability is volatile over time, so business decisions should be reviewed regularly rather than relying on a single monthly snapshot.

## Modelling Approach
We tested 3 regression algorithms: Linear Regression (baseline), Random Forest and Gradient Boosting. Both tree-based models were tuned with cross-validated search.

## Results
| Model                       |  RMSE  |   MAE  |  R2    |   
|-----------------------------|--------|--------|--------|
| Linear Regression           |  79.09 | 38.61  | 0.3899 | 
| Random Forest (tuned)       |  49.50 | 19.36  | 0.7611 |
| Gradient Boosting (tuned)   |  51.31 | 19.19  | 0.7432 |

The tuned Gradient Boosting/ Random Forest model achieved the lowest RMSE of 19.19  and 19.36, explaining 74%/76% of variance in Profit on the hold-out test set.  

## Recommendations
- Reduce reliance on heavy discounting where possible, because discount levels are associated with weaker profitability.
- Focus sales and promotional efforts on the categories, regions, and shipping options that generate stronger margins rather than simply higher revenue.
- Use the predictive model to flag low-profit orders early so teams can intervene before margin erosion becomes significant.
- Continue monitoring profit trends over time and review pricing, shipping, and product mix decisions regularly to protect margin stability.


