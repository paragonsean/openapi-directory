

# ListAllLicenses200ResponseResultsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dependencies** | [**List&lt;ListAllLicenses200ResponseResultsInnerDependenciesInner&gt;**](ListAllLicenses200ResponseResultsInnerDependenciesInner.md) | The dependencies of projects in the organization which have the license |  |
|**id** | **String** | The identifier of the license |  |
|**instructions** | **String** | Custom instructions assigned to this license |  [optional] |
|**projects** | [**List&lt;ListAllDependencies200ResponseResultsInnerProjectsInner&gt;**](ListAllDependencies200ResponseResultsInnerProjectsInner.md) | The projects which contain the license |  |
|**severity** | [**SeverityEnum**](#SeverityEnum) | The severity assigned to this license |  [optional] |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| HIGH | &quot;high&quot; |
| MEDIUM | &quot;medium&quot; |
| LOW | &quot;low&quot; |



