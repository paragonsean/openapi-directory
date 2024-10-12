

# TextSentimentEvaluationMetrics

Model evaluation metrics for text sentiment problems.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotationSpecId** | **List&lt;String&gt;** | Output only. The annotation spec ids used for this evaluation. Deprecated . |  [optional] |
|**confusionMatrix** | [**ConfusionMatrix**](ConfusionMatrix.md) |  |  [optional] |
|**f1Score** | **Float** | Output only. The harmonic mean of recall and precision. |  [optional] |
|**linearKappa** | **Float** | Output only. Linear weighted kappa. Only set for the overall model evaluation, not for evaluation of a single annotation spec. |  [optional] |
|**meanAbsoluteError** | **Float** | Output only. Mean absolute error. Only set for the overall model evaluation, not for evaluation of a single annotation spec. |  [optional] |
|**meanSquaredError** | **Float** | Output only. Mean squared error. Only set for the overall model evaluation, not for evaluation of a single annotation spec. |  [optional] |
|**precision** | **Float** | Output only. Precision. |  [optional] |
|**quadraticKappa** | **Float** | Output only. Quadratic weighted kappa. Only set for the overall model evaluation, not for evaluation of a single annotation spec. |  [optional] |
|**recall** | **Float** | Output only. Recall. |  [optional] |



