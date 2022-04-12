# Make a transformer for ShapRFE

from sklearn.base import BaseEstimator, TransformerMixin

from probatus.feature_elimination import ShapRFECV
from sklearn.model_selection import RandomizedSearchCV, StratifiedKFold


class ShapRFESelector(BaseEstimator, TransformerMixin):
    def __init__(self, clf,
        step=1,
        min_features_to_select=1,
        cv=None,
        scoring="roc_auc",
        n_jobs=-1,
        verbose=0,
        random_state=None,):
        """Initiate the selector."""
        self.shap_selection = ShapRFECV(
            clf, step, min_features_to_select, cv, scoring, n_jobs, verbose, random_state
            )

    def fit(self, X, y):
        """Perform the Shap recursive feature elimination using early stopping.
        The cross-validation is performed using StratifiedShuffleSplit by default.
        """
        # Run the Shap feature elimination
        self.shap_selection.fit_compute(X, y, check_additivity=False)

        # Keep the latest model that has the requested number of features.
        self.selected_features_ = self.shap_selection.report_df.features_set.iloc[-1]


        # Assess the columns that will be dropped during transformation.
        self.features_to_drop_ = [
            col for col in X if col not in self.selected_features_
            ]

        return self

    def transform(self, df):
        """Apply the filter estimated during the fit."""
        return df.drop(columns=self.features_to_drop_)