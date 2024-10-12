# AmazonForecastService.CreatePredictorRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**predictorName** | **String** |  | 
**algorithmArn** | **String** |  | [optional] 
**forecastHorizon** | **Number** |  | 
**forecastTypes** | **Array** |  | [optional] 
**performAutoML** | **Boolean** |  | [optional] 
**autoMLOverrideStrategy** | [**AutoMLOverrideStrategy**](AutoMLOverrideStrategy.md) |  | [optional] 
**performHPO** | **Boolean** |  | [optional] 
**trainingParameters** | **Object** |  | [optional] 
**evaluationParameters** | [**CreatePredictorRequestEvaluationParameters**](CreatePredictorRequestEvaluationParameters.md) |  | [optional] 
**hPOConfig** | [**CreatePredictorRequestHPOConfig**](CreatePredictorRequestHPOConfig.md) |  | [optional] 
**inputDataConfig** | [**CreatePredictorRequestInputDataConfig**](CreatePredictorRequestInputDataConfig.md) |  | 
**featurizationConfig** | [**CreatePredictorRequestFeaturizationConfig**](CreatePredictorRequestFeaturizationConfig.md) |  | 
**encryptionConfig** | [**CreateDatasetRequestEncryptionConfig**](CreateDatasetRequestEncryptionConfig.md) |  | [optional] 
**tags** | **Array** |  | [optional] 
**optimizationMetric** | [**OptimizationMetric**](OptimizationMetric.md) |  | [optional] 


