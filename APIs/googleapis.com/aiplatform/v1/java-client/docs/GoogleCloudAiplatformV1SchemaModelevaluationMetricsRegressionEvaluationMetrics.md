

# GoogleCloudAiplatformV1SchemaModelevaluationMetricsRegressionEvaluationMetrics

Metrics for regression evaluation results.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**meanAbsoluteError** | **Float** | Mean Absolute Error (MAE). |  [optional] |
|**meanAbsolutePercentageError** | **Float** | Mean absolute percentage error. Infinity when there are zeros in the ground truth. |  [optional] |
|**rSquared** | **Float** | Coefficient of determination as Pearson correlation coefficient. Undefined when ground truth or predictions are constant or near constant. |  [optional] |
|**rootMeanSquaredError** | **Float** | Root Mean Squared Error (RMSE). |  [optional] |
|**rootMeanSquaredLogError** | **Float** | Root mean squared log error. Undefined when there are negative ground truth values or predictions. |  [optional] |



