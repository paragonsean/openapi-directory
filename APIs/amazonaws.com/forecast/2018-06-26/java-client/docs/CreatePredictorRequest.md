

# CreatePredictorRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**predictorName** | [**String**](String.md) |  |  |
|**algorithmArn** | [**String**](String.md) |  |  [optional] |
|**forecastHorizon** | [**Integer**](Integer.md) |  |  |
|**forecastTypes** | [**List**](List.md) |  |  [optional] |
|**performAutoML** | [**Boolean**](Boolean.md) |  |  [optional] |
|**autoMLOverrideStrategy** | [**AutoMLOverrideStrategy**](AutoMLOverrideStrategy.md) |  |  [optional] |
|**performHPO** | [**Boolean**](Boolean.md) |  |  [optional] |
|**trainingParameters** | [**Map**](Map.md) |  |  [optional] |
|**evaluationParameters** | [**CreatePredictorRequestEvaluationParameters**](CreatePredictorRequestEvaluationParameters.md) |  |  [optional] |
|**hpOConfig** | [**CreatePredictorRequestHPOConfig**](CreatePredictorRequestHPOConfig.md) |  |  [optional] |
|**inputDataConfig** | [**CreatePredictorRequestInputDataConfig**](CreatePredictorRequestInputDataConfig.md) |  |  |
|**featurizationConfig** | [**CreatePredictorRequestFeaturizationConfig**](CreatePredictorRequestFeaturizationConfig.md) |  |  |
|**encryptionConfig** | [**CreateDatasetRequestEncryptionConfig**](CreateDatasetRequestEncryptionConfig.md) |  |  [optional] |
|**tags** | [**List**](List.md) |  |  [optional] |
|**optimizationMetric** | [**OptimizationMetric**](OptimizationMetric.md) |  |  [optional] |



