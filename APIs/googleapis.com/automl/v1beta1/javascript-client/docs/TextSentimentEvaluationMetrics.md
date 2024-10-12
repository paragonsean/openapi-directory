# CloudAutoMlApi.TextSentimentEvaluationMetrics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotationSpecId** | **[String]** | Output only. The annotation spec ids used for this evaluation. Deprecated . | [optional] 
**confusionMatrix** | [**ConfusionMatrix**](ConfusionMatrix.md) |  | [optional] 
**f1Score** | **Number** | Output only. The harmonic mean of recall and precision. | [optional] 
**linearKappa** | **Number** | Output only. Linear weighted kappa. Only set for the overall model evaluation, not for evaluation of a single annotation spec. | [optional] 
**meanAbsoluteError** | **Number** | Output only. Mean absolute error. Only set for the overall model evaluation, not for evaluation of a single annotation spec. | [optional] 
**meanSquaredError** | **Number** | Output only. Mean squared error. Only set for the overall model evaluation, not for evaluation of a single annotation spec. | [optional] 
**precision** | **Number** | Output only. Precision. | [optional] 
**quadraticKappa** | **Number** | Output only. Quadratic weighted kappa. Only set for the overall model evaluation, not for evaluation of a single annotation spec. | [optional] 
**recall** | **Number** | Output only. Recall. | [optional] 


