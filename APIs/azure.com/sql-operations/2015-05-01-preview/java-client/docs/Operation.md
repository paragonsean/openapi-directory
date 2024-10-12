

# Operation

SQL REST API operation definition.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**display** | [**OperationDisplay**](OperationDisplay.md) |  |  [optional] |
|**name** | **String** | The name of the operation being performed on this particular object. |  [optional] [readonly] |
|**origin** | [**OriginEnum**](#OriginEnum) | The intended executor of the operation. |  [optional] [readonly] |
|**properties** | **Map&lt;String, Object&gt;** | Additional descriptions for the operation. |  [optional] [readonly] |



## Enum: OriginEnum

| Name | Value |
|---- | -----|
| USER | &quot;user&quot; |
| SYSTEM | &quot;system&quot; |



