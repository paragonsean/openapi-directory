

# Operation

Represents an operation returned by the GetOperations request

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**display** | [**OperationInfo**](OperationInfo.md) |  |  [optional] |
|**name** | **String** | Name of the operation |  [optional] |
|**origin** | [**OriginEnum**](#OriginEnum) | Origin of the operation |  [optional] |
|**properties** | **Object** | Properties of the operation |  [optional] |



## Enum: OriginEnum

| Name | Value |
|---- | -----|
| USER | &quot;User&quot; |
| SYSTEM | &quot;System&quot; |
| USER_AND_SYSTEM | &quot;UserAndSystem&quot; |



