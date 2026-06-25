

import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def evaluate_model(name, model, X_tr, y_tr, X_te, y_te):  # good formulas
    """Fit model, print metrics, return dict of results."""
    model.fit(X_tr, y_tr)
    y_pred = model.predict(X_te)
    
    rmse = np.sqrt(mean_squared_error(y_te, y_pred))
    mae = mean_absolute_error(y_te, y_pred)
    r2 = r2_score(y_te, y_pred)
    
    print(f"\n{'-'*40}")
    print(f" {name}")
    print(f" RMSE : {rmse:>10.4f}")
    print(f" MAE  : {mae:>10.4f}")
    print(f" R2   : {r2:>10.4f}")
    
    return {"Model": name, "RMSE": round(rmse, 4), "MAE": round(mae, 4), "R2": round(r2, 4)} 