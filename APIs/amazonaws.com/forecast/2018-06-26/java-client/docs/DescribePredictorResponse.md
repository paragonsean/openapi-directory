

# DescribePredictorResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**predictorArn** | [**String**](String.md) |  |  [optional] |
|**predictorName** | [**String**](String.md) |  |  [optional] |
|**algorithmArn** | [**String**](String.md) |  |  [optional] |
|**autoMLAlgorithmArns** | [**List**](List.md) |  |  [optional] |
|**forecastHorizon** | [**Integer**](Integer.md) |  |  [optional] |
|**forecastTypes** | [**List**](List.md) |  |  [optional] |
|**performAutoML** | [**Boolean**](Boolean.md) |  |  [optional] |
|**autoMLOverrideStrategy** | [**AutoMLOverrideStrategy**](AutoMLOverrideStrategy.md) |  |  [optional] |
|**performHPO** | [**Boolean**](Boolean.md) |  |  [optional] |
|**trainingParameters** | [**Map**](Map.md) |  |  [optional] |
|**evaluationParameters** | [**CreatePredictorRequestEvaluationParameters**](CreatePredictorRequestEvaluationParameters.md) |  |  [optional] |
|**hpOConfig** | [**DescribePredictorResponseHPOConfig**](DescribePredictorResponseHPOConfig.md) |  |  [optional] |
|**inputDataConfig** | [**CreatePredictorRequestInputDataConfig**](CreatePredictorRequestInputDataConfig.md) |  |  [optional] |
|**featurizationConfig** | [**CreatePredictorRequestFeaturizationConfig**](CreatePredictorRequestFeaturizationConfig.md) |  |  [optional] |
|**encryptionConfig** | [**CreateDatasetRequestEncryptionConfig**](CreateDatasetRequestEncryptionConfig.md) |  |  [optional] |
|**predictorExecutionDetails** | [**DescribePredictorResponsePredictorExecutionDetails**](DescribePredictorResponsePredictorExecutionDetails.md) |  |  [optional] |
|**estimatedTimeRemainingInMinutes** | [**Integer**](Integer.md) |  |  [optional] |
|**isAutoPredictor** | [**Boolean**](Boolean.md) |  |  [optional] |
|**datasetImportJobArns** | [**List**](List.md) |  |  [optional] |
|**status** | [**String**](String.md) |  |  [optional] |
|**message** | [**String**](String.md) |  |  [optional] |
|**creationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastModificationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**optimizationMetric** | [**OptimizationMetric**](OptimizationMetric.md) |  |  [optional] |



