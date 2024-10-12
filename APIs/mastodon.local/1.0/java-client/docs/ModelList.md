

# ModelList

Represents a list of some users that the authenticated user follows.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The internal database ID of the list. Cast from an integer, but not guaranteed to be a number. |  |
|**repliesPolicy** | [**RepliesPolicyEnum**](#RepliesPolicyEnum) | The user-defined title of the list. |  |
|**title** | **String** | The user-defined title of the list. |  |



## Enum: RepliesPolicyEnum

| Name | Value |
|---- | -----|
| FOLLOWED | &quot;followed&quot; |
| LIST | &quot;list&quot; |
| NONE | &quot;none&quot; |



