

# ProjectResourceProperties

Defines the custom properties of project resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bootstrapPipelineTemplate** | [**PipelineTemplate**](PipelineTemplate.md) |  |  [optional] |
|**ownerUpn** | **String** | Optional UPN of the owner, on-behalf-of whom the project is being created. |  [optional] |
|**processTemplateId** | [**ProcessTemplateIdEnum**](#ProcessTemplateIdEnum) | Process template to use in the project. |  [optional] |
|**tfsUniqueIdentifier** | **String** | Unique identifier of the VSTS project. |  [optional] [readonly] |
|**versionControlOption** | [**VersionControlOptionEnum**](#VersionControlOptionEnum) | Version control to use for the default repo created in the project. |  [optional] |



## Enum: ProcessTemplateIdEnum

| Name | Value |
|---- | -----|
| SCRUM | &quot;Scrum&quot; |
| AGILE | &quot;Agile&quot; |
| CMMI | &quot;Cmmi&quot; |



## Enum: VersionControlOptionEnum

| Name | Value |
|---- | -----|
| GIT | &quot;Git&quot; |
| TFVC | &quot;Tfvc&quot; |



