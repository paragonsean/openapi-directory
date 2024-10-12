# PowerBiEmbeddedManagementClient.CheckNameResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **String** | Message indicating an unavailable name due to a conflict, or a description of the naming rules that are violated. | [optional] 
**nameAvailable** | **Boolean** | Specifies a Boolean value that indicates whether the specified Power BI Workspace Collection name is available to use. | [optional] 
**reason** | **String** | Reason why the workspace collection name cannot be used. | [optional] 



## Enum: ReasonEnum


* `Unavailable` (value: `"Unavailable"`)

* `Invalid` (value: `"Invalid"`)




