

# GoogleCloudDiscoveryengineV1betaImportUserEventsResponse

Response of the ImportUserEventsRequest. If the long running operation was successful, then this message is returned by the google.longrunning.Operations.response field if the operation was successful.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errorConfig** | [**GoogleCloudDiscoveryengineV1betaImportErrorConfig**](GoogleCloudDiscoveryengineV1betaImportErrorConfig.md) |  |  [optional] |
|**errorSamples** | [**List&lt;GoogleRpcStatus&gt;**](GoogleRpcStatus.md) | A sample of errors encountered while processing the request. |  [optional] |
|**joinedEventsCount** | **String** | Count of user events imported with complete existing Documents. |  [optional] |
|**unjoinedEventsCount** | **String** | Count of user events imported, but with Document information not found in the existing Branch. |  [optional] |



