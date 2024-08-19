

# FindMatchesMetrics

The evaluation metrics for the find matches algorithm. The quality of your machine learning transform is measured by getting your transform to predict some matches and comparing the results to known matches from the same dataset. The quality metrics are based on a subset of your data, so they are not precise.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**areaUnderPRCurve** | [**Double**](Double.md) |  |  [optional] |
|**precision** | [**Double**](Double.md) |  |  [optional] |
|**recall** | [**Double**](Double.md) |  |  [optional] |
|**F1** | [**Double**](Double.md) |  |  [optional] |
|**confusionMatrix** | [**FindMatchesMetricsConfusionMatrix**](FindMatchesMetricsConfusionMatrix.md) |  |  [optional] |
|**columnImportances** | [**List**](List.md) |  |  [optional] |



