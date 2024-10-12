# DataPipelinesApi.GoogleCloudDatapipelinesV1LaunchTemplateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gcsPath** | **String** | A Cloud Storage path to the template from which to create the job. Must be a valid Cloud Storage URL, beginning with &#39;gs://&#39;. | [optional] 
**launchParameters** | [**GoogleCloudDatapipelinesV1LaunchTemplateParameters**](GoogleCloudDatapipelinesV1LaunchTemplateParameters.md) |  | [optional] 
**location** | **String** | The [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) to which to direct the request. | [optional] 
**projectId** | **String** | Required. The ID of the Cloud Platform project that the job belongs to. | [optional] 
**validateOnly** | **Boolean** | If true, the request is validated but not actually executed. Defaults to false. | [optional] 


