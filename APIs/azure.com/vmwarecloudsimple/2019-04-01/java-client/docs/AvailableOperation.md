

# AvailableOperation

Resource provider available operation model

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**display** | [**AvailableOperationDisplay**](AvailableOperationDisplay.md) |  |  [optional] |
|**isDataAction** | **Boolean** | Indicating whether the operation is a data action or not |  [optional] |
|**name** | **String** | {resourceProviderNamespace}/{resourceType}/{read|write|delete|action} |  [optional] |
|**origin** | [**OriginEnum**](#OriginEnum) | The origin of operation |  [optional] |
|**properties** | [**AvailableOperationDisplayPropertyServiceSpecification**](AvailableOperationDisplayPropertyServiceSpecification.md) |  |  [optional] |



## Enum: OriginEnum

| Name | Value |
|---- | -----|
| USER | &quot;user&quot; |
| SYSTEM | &quot;system&quot; |
| USER_SYSTEM | &quot;user,system&quot; |



