

# GoogleCloudDatapipelinesV1DataflowJobDetails

Pipeline job details specific to the Dataflow API. This is encapsulated here to allow for more executors to store their specific details separately.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currentWorkers** | **Integer** | Output only. The current number of workers used to run the jobs. Only set to a value if the job is still running. |  [optional] [readonly] |
|**resourceInfo** | **Map&lt;String, Double&gt;** | Cached version of all the metrics of interest for the job. This value gets stored here when the job is terminated. As long as the job is running, this field is populated from the Dataflow API. |  [optional] |
|**sdkVersion** | [**GoogleCloudDatapipelinesV1SdkVersion**](GoogleCloudDatapipelinesV1SdkVersion.md) |  |  [optional] |



