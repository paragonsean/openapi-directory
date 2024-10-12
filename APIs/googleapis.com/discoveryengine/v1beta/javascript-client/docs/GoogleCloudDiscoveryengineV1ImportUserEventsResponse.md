# DiscoveryEngineApi.GoogleCloudDiscoveryengineV1ImportUserEventsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errorConfig** | [**GoogleCloudDiscoveryengineV1ImportErrorConfig**](GoogleCloudDiscoveryengineV1ImportErrorConfig.md) |  | [optional] 
**errorSamples** | [**[GoogleRpcStatus]**](GoogleRpcStatus.md) | A sample of errors encountered while processing the request. | [optional] 
**joinedEventsCount** | **String** | Count of user events imported with complete existing Documents. | [optional] 
**unjoinedEventsCount** | **String** | Count of user events imported, but with Document information not found in the existing Branch. | [optional] 


