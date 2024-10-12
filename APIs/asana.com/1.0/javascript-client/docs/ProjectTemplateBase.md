# Asana.ProjectTemplateBase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **String** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resourceType** | **String** | The base type of this resource. | [optional] [readonly] 
**name** | **String** | Name of the project template. | [optional] 
**color** | **String** | Color of the project template. | [optional] 
**description** | **String** | Free-form textual information associated with the project template | [optional] 
**htmlDescription** | **String** | The description of the project template with formatting as HTML. | [optional] 
**owner** | [**UserCompact**](UserCompact.md) | The current owner of the project template, may be null. | [optional] 
**_public** | **Boolean** | True if the project template is public to its team. | [optional] 
**requestedDates** | [**[DateVariableCompact]**](DateVariableCompact.md) | Array of date variables in this project template. Calendar dates must be provided for these variables when instantiating a project. | [optional] [readonly] 
**team** | [**TeamCompact**](TeamCompact.md) |  | [optional] 



## Enum: ColorEnum


* `dark-pink` (value: `"dark-pink"`)

* `dark-green` (value: `"dark-green"`)

* `dark-blue` (value: `"dark-blue"`)

* `dark-red` (value: `"dark-red"`)

* `dark-teal` (value: `"dark-teal"`)

* `dark-brown` (value: `"dark-brown"`)

* `dark-orange` (value: `"dark-orange"`)

* `dark-purple` (value: `"dark-purple"`)

* `dark-warm-gray` (value: `"dark-warm-gray"`)

* `light-pink` (value: `"light-pink"`)

* `light-green` (value: `"light-green"`)

* `light-blue` (value: `"light-blue"`)

* `light-red` (value: `"light-red"`)

* `light-teal` (value: `"light-teal"`)

* `light-brown` (value: `"light-brown"`)

* `light-orange` (value: `"light-orange"`)

* `light-purple` (value: `"light-purple"`)

* `light-warm-gray` (value: `"light-warm-gray"`)




