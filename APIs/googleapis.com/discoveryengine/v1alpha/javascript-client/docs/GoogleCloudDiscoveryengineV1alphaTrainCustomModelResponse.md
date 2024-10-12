# DiscoveryEngineApi.GoogleCloudDiscoveryengineV1alphaTrainCustomModelResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errorConfig** | [**GoogleCloudDiscoveryengineV1alphaImportErrorConfig**](GoogleCloudDiscoveryengineV1alphaImportErrorConfig.md) |  | [optional] 
**errorSamples** | [**[GoogleRpcStatus]**](GoogleRpcStatus.md) | A sample of errors encountered while processing the data. | [optional] 
**modelStatus** | **String** | The trained model status. Possible values are: * **bad-data**: The training data quality is bad. * **no-improvement**: Tuning didn&#39;t improve performance. Won&#39;t deploy. * **in-progress**: Model training is in progress. * **ready**: The model is ready for serving. | [optional] 


