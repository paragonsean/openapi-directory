# DiscoveryEngineApi.GoogleCloudDiscoveryengineV1betaImportUserEventsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errorConfig** | [**GoogleCloudDiscoveryengineV1betaImportErrorConfig**](GoogleCloudDiscoveryengineV1betaImportErrorConfig.md) |  | [optional] 
**errorSamples** | [**[GoogleRpcStatus]**](GoogleRpcStatus.md) | A sample of errors encountered while processing the request. | [optional] 
**joinedEventsCount** | **String** | Count of user events imported with complete existing Documents. | [optional] 
**unjoinedEventsCount** | **String** | Count of user events imported, but with Document information not found in the existing Branch. | [optional] 


