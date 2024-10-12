# DataflowApi.LaunchTemplateParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | [**RuntimeEnvironment**](RuntimeEnvironment.md) |  | [optional] 
**jobName** | **String** | Required. The job name to use for the created job. The name must match the regular expression &#x60;[a-z]([-a-z0-9]{0,1022}[a-z0-9])?&#x60; | [optional] 
**parameters** | **{String: String}** | The runtime parameters to pass to the job. | [optional] 
**transformNameMapping** | **{String: String}** | Only applicable when updating a pipeline. Map of transform name prefixes of the job to be replaced to the corresponding name prefixes of the new job. | [optional] 
**update** | **Boolean** | If set, replace the existing pipeline with the name specified by jobName with this pipeline, preserving state. | [optional] 


