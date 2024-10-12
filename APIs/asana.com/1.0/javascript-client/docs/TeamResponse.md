# Asana.TeamResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **String** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resourceType** | **String** | The base type of this resource. | [optional] [readonly] 
**name** | **String** | The name of the team. | [optional] 
**description** | **String** | [Opt In](/docs/input-output-options). The description of the team.  | [optional] 
**htmlDescription** | **String** | [Opt In](/docs/input-output-options). The description of the team with formatting as HTML.  | [optional] 
**organization** | [**TeamResponseAllOfOrganization**](TeamResponseAllOfOrganization.md) |  | [optional] 
**permalinkUrl** | **String** | A url that points directly to the object within Asana. | [optional] [readonly] 
**visibility** | **String** | The visibility of the team to users in the same organization  | [optional] 



## Enum: VisibilityEnum


* `secret` (value: `"secret"`)

* `request_to_join` (value: `"request_to_join"`)

* `public` (value: `"public"`)




