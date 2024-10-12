# MySqlManagementClient.Operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display** | [**OperationDisplay**](OperationDisplay.md) |  | [optional] 
**name** | **String** | The name of the operation being performed on this particular object. | [optional] [readonly] 
**origin** | **String** | The intended executor of the operation. | [optional] [readonly] 
**properties** | **{String: Object}** | Additional descriptions for the operation. | [optional] [readonly] 



## Enum: OriginEnum


* `NotSpecified` (value: `"NotSpecified"`)

* `user` (value: `"user"`)

* `system` (value: `"system"`)




