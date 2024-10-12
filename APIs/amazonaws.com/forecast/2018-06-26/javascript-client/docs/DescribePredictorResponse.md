# AmazonForecastService.DescribePredictorResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**predictorArn** | **String** |  | [optional] 
**predictorName** | **String** |  | [optional] 
**algorithmArn** | **String** |  | [optional] 
**autoMLAlgorithmArns** | **Array** |  | [optional] 
**forecastHorizon** | **Number** |  | [optional] 
**forecastTypes** | **Array** |  | [optional] 
**performAutoML** | **Boolean** |  | [optional] 
**autoMLOverrideStrategy** | [**AutoMLOverrideStrategy**](AutoMLOverrideStrategy.md) |  | [optional] 
**performHPO** | **Boolean** |  | [optional] 
**trainingParameters** | **Object** |  | [optional] 
**evaluationParameters** | [**CreatePredictorRequestEvaluationParameters**](CreatePredictorRequestEvaluationParameters.md) |  | [optional] 
**hPOConfig** | [**DescribePredictorResponseHPOConfig**](DescribePredictorResponseHPOConfig.md) |  | [optional] 
**inputDataConfig** | [**CreatePredictorRequestInputDataConfig**](CreatePredictorRequestInputDataConfig.md) |  | [optional] 
**featurizationConfig** | [**CreatePredictorRequestFeaturizationConfig**](CreatePredictorRequestFeaturizationConfig.md) |  | [optional] 
**encryptionConfig** | [**CreateDatasetRequestEncryptionConfig**](CreateDatasetRequestEncryptionConfig.md) |  | [optional] 
**predictorExecutionDetails** | [**DescribePredictorResponsePredictorExecutionDetails**](DescribePredictorResponsePredictorExecutionDetails.md) |  | [optional] 
**estimatedTimeRemainingInMinutes** | **Number** |  | [optional] 
**isAutoPredictor** | **Boolean** |  | [optional] 
**datasetImportJobArns** | **Array** |  | [optional] 
**status** | **String** |  | [optional] 
**message** | **String** |  | [optional] 
**creationTime** | **Date** |  | [optional] 
**lastModificationTime** | **Date** |  | [optional] 
**optimizationMetric** | [**OptimizationMetric**](OptimizationMetric.md) |  | [optional] 


