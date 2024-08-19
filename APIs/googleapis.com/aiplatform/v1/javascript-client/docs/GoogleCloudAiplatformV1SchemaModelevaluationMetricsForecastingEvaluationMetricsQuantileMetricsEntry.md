# VertexAiApi.GoogleCloudAiplatformV1SchemaModelevaluationMetricsForecastingEvaluationMetricsQuantileMetricsEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**observedQuantile** | **Number** | This is a custom metric that calculates the percentage of true values that were less than the predicted value for that quantile. Only populated when optimization_objective is minimize-quantile-loss and each entry corresponds to an entry in quantiles The percent value can be used to compare with the quantile value, which is the target value. | [optional] 
**quantile** | **Number** | The quantile for this entry. | [optional] 
**scaledPinballLoss** | **Number** | The scaled pinball loss of this quantile. | [optional] 


