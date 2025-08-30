# 📘 Concepts & Revision — Kaggle Playground S3E1 (California Housing)

This file is for quick revision of the workflow, concepts, and key takeaways.

---

## 🏗️ Project Workflow

1. **EDA**
   - Target: `MedHouseVal` (median house value, capped at 5.0).
   - Strongest correlation: `MedInc` (~0.70).
   - Geography (`Latitude`, `Longitude`) strongly shapes housing value.
   - Other features (HouseAge, Population, AveOccup) are weak contributors.

2. **Models Tried**
   - Linear Regression → RMSE ~0.75
   - Ridge & Lasso → RMSE ~0.74
   - Decision Tree (depth=5) → RMSE ~0.70
   - Random Forest → RMSE ~0.61
   - XGBoost (baseline) → RMSE ~0.594
   - XGBoost (tuned) → RMSE ~0.589 (✅ best)
   - Feature engineering (ratios, log target) → negligible gain

3. **Final Submission**
   - Tuned XGBoost
   - Public LB: ~0.575
   - Private LB: ~0.5697
   - Very close to leaderboard top (~0.552)

---

## 🔑 Key Concepts Revised

- **RMSE (Root Mean Squared Error)**  
  Measures error magnitude. Lower = better. Sensitive to outliers.  
  Formula:  
  \[
  RMSE = \sqrt{\frac{1}{n} \sum (y_{true} - y_{pred})^2}
  \]

- **Regularisation (Ridge vs Lasso)**  
  - Ridge: shrinks coefficients (L2 penalty).  
  - Lasso: can zero out coefficients (L1 penalty).  

- **Trees & Ensembles**  
  - Decision Tree → high variance (overfits easily).  
  - Random Forest → bagging reduces variance.  
  - XGBoost → boosting reduces bias + variance via sequential trees.

- **Feature Importance**  
  - Gain: how much a feature reduces error.  
  - MedInc >> Latitude, Longitude >> all others.  

- **Partial Dependence Plots (PDPs)**  
  Show marginal effect of features on predictions.  
  - MedInc → positive slope.  
  - Latitude → higher lat = lower value.  
  - Longitude → west coast (lower lon) = higher value.

- **Feature Engineering Lessons**  
  - Ratios (e.g., RoomsPerHousehold) didn’t add much.  
  - Log-transform target didn’t help (target capped at 5).  
  - Most signal already captured by MedInc + geo.  

---

## 🚀 Next Steps (for S3E2)
- Shift mindset to **classification** (metrics: ROC-AUC, accuracy).  
- Baseline = Logistic Regression.  
- Ensembles: Random Forest, XGBoost, LightGBM.  
- Try categorical handling (encoding, boosting with `enable_categorical=True`).  

---

## 🙌 Reflection
- Learned how to build a full ML pipeline from scratch.  
- Understood model comparison and why boosting shines.  
- Gained interpretability skills (feature importance, PDPs).  
- Practiced feature engineering & saw limits of “obvious” features.  
- Closed the loop with a real Kaggle submission (LB score ~0.57).
