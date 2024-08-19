

# GoogleCloudAiplatformV1ListHyperparameterTuningJobsResponse

Response message for JobService.ListHyperparameterTuningJobs

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hyperparameterTuningJobs** | [**List&lt;GoogleCloudAiplatformV1HyperparameterTuningJob&gt;**](GoogleCloudAiplatformV1HyperparameterTuningJob.md) | List of HyperparameterTuningJobs in the requested page. HyperparameterTuningJob.trials of the jobs will be not be returned. |  [optional] |
|**nextPageToken** | **String** | A token to retrieve the next page of results. Pass to ListHyperparameterTuningJobsRequest.page_token to obtain that page. |  [optional] |



