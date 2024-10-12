

# OperationsStatus

A long running operation status.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **OffsetDateTime** | The end time of the operation. |  [optional] |
|**error** | [**ExtendedErrorInfo**](ExtendedErrorInfo.md) |  |  [optional] |
|**id** | [**OperationsStatusIdentifier**](OperationsStatusIdentifier.md) |  |  [optional] |
|**percentComplete** | **BigDecimal** | The completion percentage of the operation. |  [optional] |
|**properties** | **Object** | The internal operation properties. |  [optional] |
|**responseContent** | **Object** | The content of the response. |  [optional] |
|**retryAfter** | **String** | The amount of time clients should wait.. |  [optional] |
|**startTime** | **OffsetDateTime** | The start time of the operation. |  [optional] |
|**status** | **String** | The status of the operation. |  [optional] |
|**terminalHttpStatusCode** | **String** | The terminal http status code for the operation. |  [optional] |



