

# TeamRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**gid** | **String** | Globally unique identifier of the resource, as a string. |  [optional] [readonly] |
|**resourceType** | **String** | The base type of this resource. |  [optional] [readonly] |
|**name** | **String** | The name of the team. |  [optional] |
|**description** | **String** | The description of the team.  |  [optional] |
|**htmlDescription** | **String** | The description of the team with formatting as HTML.  |  [optional] |
|**organization** | **String** | The organization/workspace the team belongs to. This must be the same organization you are in and cannot be changed once set.  |  [optional] |
|**visibility** | [**VisibilityEnum**](#VisibilityEnum) | The visibility of the team to users in the same organization  |  [optional] |



## Enum: VisibilityEnum

| Name | Value |
|---- | -----|
| SECRET | &quot;secret&quot; |
| REQUEST_TO_JOIN | &quot;request_to_join&quot; |
| PUBLIC | &quot;public&quot; |



