# Asana.ProjectStatusResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **String** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resourceType** | **String** | The base type of this resource. | [optional] [readonly] 
**title** | **String** | The title of the project status update. | [optional] 
**color** | **String** | The color associated with the status update. | 
**htmlText** | **String** | [Opt In](/docs/input-output-options). The text content of the status update with formatting as HTML. | [optional] 
**text** | **String** | The text content of the status update. | 
**author** | [**UserCompact**](UserCompact.md) |  | [optional] 
**createdAt** | **Date** | The time at which this resource was created. | [optional] [readonly] 
**createdBy** | [**UserCompact**](UserCompact.md) |  | [optional] 
**modifiedAt** | **Date** | The time at which this project status was last modified. *Note: This does not currently reflect any changes in associations such as comments that may have been added or removed from the project status.* | [optional] [readonly] 



## Enum: ColorEnum


* `green` (value: `"green"`)

* `yellow` (value: `"yellow"`)

* `red` (value: `"red"`)

* `blue` (value: `"blue"`)




