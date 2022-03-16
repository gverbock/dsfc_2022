# Make you own transformer
from sklearn.base import BaseEstimator, TransformerMixin


class CustomizedTransformer(BaseEstimator, TransformerMixin):
    """Remove the features from a list from the dataframe.

    Similar to DropFeatures from feature_engine but allowing the
    features not to be present in the dataframe.
    """

    def __init__(self, min_number_values):
        """Initiate the class."""
        self.min_number_values = min_number_values

    def fit(self, X, y=None):
        """Assess the features to filter out."""
        self.features_to_drop_ = []
        
        for feature in X.columns:
            number_of_distinct_values = len(set(X[feature]))
            
            if number_of_distinct_values < self.min_number_values:
                self.features_to_drop_.append(feature)
    
        return self

    def transform(self, df):
        """Apply the filter."""
        return df.drop(columns=self.features_to_drop_)

