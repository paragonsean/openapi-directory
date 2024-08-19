

# AppServiceEnvironmentsListOperations200ResponseInner

An operation on a resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdTime** | **OffsetDateTime** | Time when operation has started. |  [optional] |
|**errors** | [**List&lt;AppServiceEnvironmentsListOperations200ResponseInnerErrorsInner&gt;**](AppServiceEnvironmentsListOperations200ResponseInnerErrorsInner.md) | Any errors associate with the operation. |  [optional] |
|**expirationTime** | **OffsetDateTime** | Time when operation will expire. |  [optional] |
|**geoMasterOperationId** | **UUID** | Applicable only for stamp operation ids. |  [optional] |
|**id** | **String** | Operation ID. |  [optional] |
|**modifiedTime** | **OffsetDateTime** | Time when operation has been updated. |  [optional] |
|**name** | **String** | Operation name. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The current status of the operation. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| IN_PROGRESS | &quot;InProgress&quot; |
| FAILED | &quot;Failed&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| TIMED_OUT | &quot;TimedOut&quot; |
| CREATED | &quot;Created&quot; |



