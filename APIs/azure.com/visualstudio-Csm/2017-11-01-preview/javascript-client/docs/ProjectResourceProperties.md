# VisualStudioResourceProviderClient.ProjectResourceProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bootstrapPipelineTemplate** | [**PipelineTemplate**](PipelineTemplate.md) |  | [optional] 
**ownerUpn** | **String** | Optional UPN of the owner, on-behalf-of whom the project is being created. | [optional] 
**processTemplateId** | **String** | Process template to use in the project. | [optional] 
**tfsUniqueIdentifier** | **String** | Unique identifier of the VSTS project. | [optional] [readonly] 
**versionControlOption** | **String** | Version control to use for the default repo created in the project. | [optional] 



## Enum: ProcessTemplateIdEnum


* `Scrum` (value: `"Scrum"`)

* `Agile` (value: `"Agile"`)

* `Cmmi` (value: `"Cmmi"`)





## Enum: VersionControlOptionEnum


* `Git` (value: `"Git"`)

* `Tfvc` (value: `"Tfvc"`)




