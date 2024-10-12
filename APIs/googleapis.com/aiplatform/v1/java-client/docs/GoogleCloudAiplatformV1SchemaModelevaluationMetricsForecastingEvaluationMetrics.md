

# GoogleCloudAiplatformV1SchemaModelevaluationMetricsForecastingEvaluationMetrics

Metrics for forecasting evaluation results.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**meanAbsoluteError** | **Float** | Mean Absolute Error (MAE). |  [optional] |
|**meanAbsolutePercentageError** | **Float** | Mean absolute percentage error. Infinity when there are zeros in the ground truth. |  [optional] |
|**quantileMetrics** | [**List&lt;GoogleCloudAiplatformV1SchemaModelevaluationMetricsForecastingEvaluationMetricsQuantileMetricsEntry&gt;**](GoogleCloudAiplatformV1SchemaModelevaluationMetricsForecastingEvaluationMetricsQuantileMetricsEntry.md) | The quantile metrics entries for each quantile. |  [optional] |
|**rSquared** | **Float** | Coefficient of determination as Pearson correlation coefficient. Undefined when ground truth or predictions are constant or near constant. |  [optional] |
|**rootMeanSquaredError** | **Float** | Root Mean Squared Error (RMSE). |  [optional] |
|**rootMeanSquaredLogError** | **Float** | Root mean squared log error. Undefined when there are negative ground truth values or predictions. |  [optional] |
|**rootMeanSquaredPercentageError** | **Float** | Root Mean Square Percentage Error. Square root of MSPE. Undefined/imaginary when MSPE is negative. |  [optional] |
|**weightedAbsolutePercentageError** | **Float** | Weighted Absolute Percentage Error. Does not use weights, this is just what the metric is called. Undefined if actual values sum to zero. Will be very large if actual values sum to a very small number. |  [optional] |



