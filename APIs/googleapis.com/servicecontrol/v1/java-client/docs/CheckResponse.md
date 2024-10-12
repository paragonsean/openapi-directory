

# CheckResponse

Response message for the Check method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**checkErrors** | [**List&lt;CheckError&gt;**](CheckError.md) | Indicate the decision of the check. If no check errors are present, the service should process the operation. Otherwise the service should use the list of errors to determine the appropriate action. |  [optional] |
|**checkInfo** | [**CheckInfo**](CheckInfo.md) |  |  [optional] |
|**operationId** | **String** | The same operation_id value used in the CheckRequest. Used for logging and diagnostics purposes. |  [optional] |
|**quotaInfo** | [**QuotaInfo**](QuotaInfo.md) |  |  [optional] |
|**serviceConfigId** | **String** | The actual config id used to process the request. |  [optional] |
|**serviceRolloutId** | **String** | The current service rollout id used to process the request. |  [optional] |



