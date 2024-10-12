# VertexAiApi.GoogleCloudAiplatformV1SchemaModelevaluationMetricsForecastingEvaluationMetrics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meanAbsoluteError** | **Number** | Mean Absolute Error (MAE). | [optional] 
**meanAbsolutePercentageError** | **Number** | Mean absolute percentage error. Infinity when there are zeros in the ground truth. | [optional] 
**quantileMetrics** | [**[GoogleCloudAiplatformV1SchemaModelevaluationMetricsForecastingEvaluationMetricsQuantileMetricsEntry]**](GoogleCloudAiplatformV1SchemaModelevaluationMetricsForecastingEvaluationMetricsQuantileMetricsEntry.md) | The quantile metrics entries for each quantile. | [optional] 
**rSquared** | **Number** | Coefficient of determination as Pearson correlation coefficient. Undefined when ground truth or predictions are constant or near constant. | [optional] 
**rootMeanSquaredError** | **Number** | Root Mean Squared Error (RMSE). | [optional] 
**rootMeanSquaredLogError** | **Number** | Root mean squared log error. Undefined when there are negative ground truth values or predictions. | [optional] 
**rootMeanSquaredPercentageError** | **Number** | Root Mean Square Percentage Error. Square root of MSPE. Undefined/imaginary when MSPE is negative. | [optional] 
**weightedAbsolutePercentageError** | **Number** | Weighted Absolute Percentage Error. Does not use weights, this is just what the metric is called. Undefined if actual values sum to zero. Will be very large if actual values sum to a very small number. | [optional] 


