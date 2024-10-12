# DataPipelinesApi.GoogleCloudDatapipelinesV1DataflowJobDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currentWorkers** | **Number** | Output only. The current number of workers used to run the jobs. Only set to a value if the job is still running. | [optional] [readonly] 
**resourceInfo** | **{String: Number}** | Cached version of all the metrics of interest for the job. This value gets stored here when the job is terminated. As long as the job is running, this field is populated from the Dataflow API. | [optional] 
**sdkVersion** | [**GoogleCloudDatapipelinesV1SdkVersion**](GoogleCloudDatapipelinesV1SdkVersion.md) |  | [optional] 


