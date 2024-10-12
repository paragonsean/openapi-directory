

# Operation

Operation entity.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**display** | [**OperationDisplay**](OperationDisplay.md) |  |  [optional] |
|**name** | **String** | Name of the operation. Format: {resourceProviderNamespace}/{resourceType}/{read|write|delete|action} |  [optional] [readonly] |
|**origin** | **String** | Origin of the operation. Can be : user|system|user,system |  [optional] [readonly] |
|**properties** | **Object** | Operation properties. |  [optional] |



