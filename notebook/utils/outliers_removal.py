def cap_outliers(series, lower_pct=0.01, upper_pct=0.99):
    """Cap values at the given percentile bounds."""  # formulations to remove outliers
    low = series.quantile(lower_pct)
    high= series.quantile(upper_pct)
    return series.clip(lower=low, upper=high)
