# Asana.StatusUpdateCompact

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **String** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resourceType** | **String** | The base type of this resource. | [optional] [readonly] 
**resourceSubtype** | **String** | The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning. The &#x60;resource_subtype&#x60;s for &#x60;status&#x60; objects represent the type of their parent. | [optional] [readonly] 
**title** | **String** | The title of the status update. | [optional] 



## Enum: ResourceSubtypeEnum


* `project_status_update` (value: `"project_status_update"`)

* `portfolio_status_update` (value: `"portfolio_status_update"`)

* `goal_status_update` (value: `"goal_status_update"`)




