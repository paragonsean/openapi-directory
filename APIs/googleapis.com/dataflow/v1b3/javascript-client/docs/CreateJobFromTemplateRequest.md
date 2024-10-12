# DataflowApi.CreateJobFromTemplateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | [**RuntimeEnvironment**](RuntimeEnvironment.md) |  | [optional] 
**gcsPath** | **String** | Required. A Cloud Storage path to the template from which to create the job. Must be a valid Cloud Storage URL, beginning with &#x60;gs://&#x60;. | [optional] 
**jobName** | **String** | Required. The job name to use for the created job. | [optional] 
**location** | **String** | The [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) to which to direct the request. | [optional] 
**parameters** | **{String: String}** | The runtime parameters to pass to the job. | [optional] 


