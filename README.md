# 🏠 California Housing Price Prediction (Kaggle Playground S3E1)

This project was developed as part of my university coursework.  
It is based on the Kaggle **Playground Series S3E1** competition, using the California Housing dataset.

---

## 📊 Workflow

- Performed **EDA**: found Median Income, Latitude, and Longitude as strongest predictors.
- Tried **baseline models**: Linear, Ridge, Lasso.
- Explored **tree-based models**: Decision Tree, Random Forest.
- Built **XGBoost** models:
  - Baseline RMSE ~0.594
  - Tuned RMSE ~0.56
- Tried **feature engineering** (ratios, log-transform) → minor impact.
- Generated **final submission** with tuned XGBoost.

---

## 🚀 Results
- **Validation RMSE**: 0.589  
- **Kaggle Private LB Score**: 0.5697  
- Close to top leaderboard solutions (~0.552).

---

## 📂 Files
- `code.ipynb`: Jupyter notebook with the full pipeline.
- `submission.csv`: Final Kaggle submission file.

---

## 🙌 Acknowledgements
Competition: [Kaggle Playground Series S3E1](https://www.kaggle.com/competitions/playground-series-s3e1)
