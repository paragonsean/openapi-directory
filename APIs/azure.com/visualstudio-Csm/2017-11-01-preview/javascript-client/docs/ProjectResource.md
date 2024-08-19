# VisualStudioResourceProviderClient.ProjectResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **String** | Kind of project resource | [optional] 
**properties** | [**ProjectResourceProperties**](ProjectResourceProperties.md) |  | [optional] 
**id** | **String** | Unique identifier of the resource. | [optional] [readonly] 
**location** | **String** | Resource location. | [optional] 
**name** | **String** | Resource name. | [optional] [readonly] 
**tags** | **{String: String}** | Resource tags. | [optional] 
**type** | **String** | Resource type. | [optional] [readonly] 



## Enum: KindEnum


* `project` (value: `"project"`)

* `bootstrappedProject` (value: `"bootstrappedProject"`)




