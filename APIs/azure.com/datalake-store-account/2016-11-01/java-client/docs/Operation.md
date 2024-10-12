

# Operation

An available operation for Data Lake Store.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**display** | [**OperationDisplay**](OperationDisplay.md) |  |  [optional] |
|**name** | **String** | The name of the operation. |  [optional] [readonly] |
|**origin** | [**OriginEnum**](#OriginEnum) | The intended executor of the operation. |  [optional] [readonly] |



## Enum: OriginEnum

| Name | Value |
|---- | -----|
| USER | &quot;user&quot; |
| SYSTEM | &quot;system&quot; |
| USER_SYSTEM | &quot;user,system&quot; |



