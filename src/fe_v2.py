import pandas as pd
import numpy as np


def make_features(df_in: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    """
    Feature Engineering v2 (booking-focused, defensive to missing values)

    Returns
    -------
    X : pd.DataFrame
        Model-ready feature matrix (categorical + numeric, no NaNs)
    y : pd.Series
        Target vector (hotel_cluster)
    """
    df = df_in.copy()

    # ---- Target ----
    y = df["hotel_cluster"]

    # ---- Dates → month + length_of_stay ----
    df["srch_ci_dt"] = pd.to_datetime(df["srch_ci"], errors="coerce")
    df["srch_co_dt"] = pd.to_datetime(df["srch_co"], errors="coerce")

    df["checkin_month"] = df["srch_ci_dt"].dt.month

    df["length_of_stay"] = (df["srch_co_dt"] - df["srch_ci_dt"]).dt.days
    df["length_of_stay"] = df["length_of_stay"].fillna(-1).clip(lower=-1)

    df["stay_type"] = np.where(
        df["length_of_stay"].between(0, 3),
        "short",
        np.where(df["length_of_stay"] >= 4, "long", "unknown"),
    )

    # ---- Party / family ----
    df["srch_children_cnt"] = df["srch_children_cnt"].fillna(0)
    df["has_children"] = df["srch_children_cnt"] > 0

    # ---- Distance ----
    df["distance_missing"] = df["orig_destination_distance"].isna()

    df["distance_bucket"] = pd.cut(
        df["orig_destination_distance"],
        bins=[-np.inf, 300, 1000, 3000, np.inf],
        labels=["near", "mid", "far", "very_far"],
    ).astype("object")

    df.loc[df["distance_missing"], "distance_bucket"] = "unknown"

    # ---- Feature set (v2) ----

    # ---- Destination latent features (d1–d150) ----
    import re

    dest_cols = sorted(
    [c for c in df.columns if re.fullmatch(r"d\d+", c)]
    )



    # ---- Feature set (v2) ----
    feature_cols = [
        # geo + context
        "site_name",
        "posa_continent",
        "user_location_country",
        "user_location_region",
        "srch_destination_id",
        "srch_destination_type_id",
        # search intent
        "srch_adults_cnt",
        "srch_children_cnt",
        "srch_rm_cnt",
        # time
        "checkin_month",
        "length_of_stay",
        "stay_type",
        # device / commercial context
        "is_mobile",
        "is_package",
        "channel",
        # distance engineered
        "distance_missing",
        "distance_bucket",
    ] + dest_cols


    X = df[feature_cols].copy()

    # ---- Defensive missing handling ----
    id_like = [
        "site_name",
        "posa_continent",
        "user_location_country",
        "user_location_region",
        "srch_destination_id",
        "srch_destination_type_id",
        "channel",
    ]
    for c in id_like:
        X[c] = X[c].fillna(-1).astype("int64")

    count_like = ["srch_adults_cnt", "srch_children_cnt", "srch_rm_cnt"]
    for c in count_like:
        X[c] = X[c].fillna(0).astype("int64")

    X["checkin_month"] = X["checkin_month"].fillna(0).astype("int64")
    X["length_of_stay"] = X["length_of_stay"].fillna(-1).astype("int64")

    X["stay_type"] = X["stay_type"].fillna("unknown").astype("object")
    X["distance_bucket"] = X["distance_bucket"].fillna("unknown").astype("object")

    X["distance_missing"] = X["distance_missing"].fillna(False).astype(bool)

    
    for c in dest_cols:
        X[c] = X[c].fillna(0.0).astype("float32")


    return X, y

