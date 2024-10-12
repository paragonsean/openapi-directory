

# RankingMetrics

Evaluation metrics used by weighted-ALS models specified by feedback_type=implicit.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**averageRank** | **Double** | Determines the goodness of a ranking by computing the percentile rank from the predicted confidence and dividing it by the original rank. |  [optional] |
|**meanAveragePrecision** | **Double** | Calculates a precision per user for all the items by ranking them and then averages all the precisions across all the users. |  [optional] |
|**meanSquaredError** | **Double** | Similar to the mean squared error computed in regression and explicit recommendation models except instead of computing the rating directly, the output from evaluate is computed against a preference which is 1 or 0 depending on if the rating exists or not. |  [optional] |
|**normalizedDiscountedCumulativeGain** | **Double** | A metric to determine the goodness of a ranking calculated from the predicted confidence by comparing it to an ideal rank measured by the original ratings. |  [optional] |



