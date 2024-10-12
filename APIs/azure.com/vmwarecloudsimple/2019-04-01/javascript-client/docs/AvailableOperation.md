# VMwareCloudSimple.AvailableOperation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display** | [**AvailableOperationDisplay**](AvailableOperationDisplay.md) |  | [optional] 
**isDataAction** | **Boolean** | Indicating whether the operation is a data action or not | [optional] [default to false]
**name** | **String** | {resourceProviderNamespace}/{resourceType}/{read|write|delete|action} | [optional] 
**origin** | **String** | The origin of operation | [optional] 
**properties** | [**AvailableOperationDisplayPropertyServiceSpecification**](AvailableOperationDisplayPropertyServiceSpecification.md) |  | [optional] 



## Enum: OriginEnum


* `user` (value: `"user"`)

* `system` (value: `"system"`)

* `user,system` (value: `"user,system"`)




