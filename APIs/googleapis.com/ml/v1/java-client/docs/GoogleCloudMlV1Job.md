

# GoogleCloudMlV1Job

Represents a training or prediction job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. When the job was created. |  [optional] |
|**endTime** | **String** | Output only. When the job processing was completed. |  [optional] |
|**errorMessage** | **String** | Output only. The details of a failure or a cancellation. |  [optional] |
|**etag** | **byte[]** | &#x60;etag&#x60; is used for optimistic concurrency control as a way to help prevent simultaneous updates of a job from overwriting each other. It is strongly suggested that systems make use of the &#x60;etag&#x60; in the read-modify-write cycle to perform job updates in order to avoid race conditions: An &#x60;etag&#x60; is returned in the response to &#x60;GetJob&#x60;, and systems are expected to put that etag in the request to &#x60;UpdateJob&#x60; to ensure that their change will be applied to the same version of the job. |  [optional] |
|**jobId** | **String** | Required. The user-specified id of the job. |  [optional] |
|**jobPosition** | **String** | Output only. It&#39;s only effect when the job is in QUEUED state. If it&#39;s positive, it indicates the job&#39;s position in the job scheduler. It&#39;s 0 when the job is already scheduled. |  [optional] [readonly] |
|**labels** | **Map&lt;String, String&gt;** | Optional. One or more labels that you can add, to organize your jobs. Each label is a key-value pair, where both the key and the value are arbitrary strings that you supply. For more information, see the documentation on using labels. |  [optional] |
|**predictionInput** | [**GoogleCloudMlV1PredictionInput**](GoogleCloudMlV1PredictionInput.md) |  |  [optional] |
|**predictionOutput** | [**GoogleCloudMlV1PredictionOutput**](GoogleCloudMlV1PredictionOutput.md) |  |  [optional] |
|**startTime** | **String** | Output only. When the job processing was started. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The detailed state of a job. |  [optional] |
|**trainingInput** | [**GoogleCloudMlV1TrainingInput**](GoogleCloudMlV1TrainingInput.md) |  |  [optional] |
|**trainingOutput** | [**GoogleCloudMlV1TrainingOutput**](GoogleCloudMlV1TrainingOutput.md) |  |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| QUEUED | &quot;QUEUED&quot; |
| PREPARING | &quot;PREPARING&quot; |
| RUNNING | &quot;RUNNING&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| FAILED | &quot;FAILED&quot; |
| CANCELLING | &quot;CANCELLING&quot; |
| CANCELLED | &quot;CANCELLED&quot; |



