

# GoogleCloudRetailV2ImportUserEventsResponse

Response of the ImportUserEventsRequest. If the long running operation was successful, then this message is returned by the google.longrunning.Operations.response field if the operation was successful.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errorSamples** | [**List&lt;GoogleRpcStatus&gt;**](GoogleRpcStatus.md) | A sample of errors encountered while processing the request. |  [optional] |
|**errorsConfig** | [**GoogleCloudRetailV2ImportErrorsConfig**](GoogleCloudRetailV2ImportErrorsConfig.md) |  |  [optional] |
|**importSummary** | [**GoogleCloudRetailV2UserEventImportSummary**](GoogleCloudRetailV2UserEventImportSummary.md) |  |  [optional] |



