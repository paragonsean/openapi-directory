# DataPipelinesApi.GoogleCloudDatapipelinesV1LaunchTemplateParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | [**GoogleCloudDatapipelinesV1RuntimeEnvironment**](GoogleCloudDatapipelinesV1RuntimeEnvironment.md) |  | [optional] 
**jobName** | **String** | Required. The job name to use for the created job. | [optional] 
**parameters** | **{String: String}** | The runtime parameters to pass to the job. | [optional] 
**transformNameMapping** | **{String: String}** | Map of transform name prefixes of the job to be replaced to the corresponding name prefixes of the new job. Only applicable when updating a pipeline. | [optional] 
**update** | **Boolean** | If set, replace the existing pipeline with the name specified by jobName with this pipeline, preserving state. | [optional] 


