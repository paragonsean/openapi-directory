

# GoogleCloudAiplatformV1beta1CustomJob

Represents a job that runs custom workloads such as a Docker container or a Python package. A CustomJob can have multiple worker pools and each worker pool can have its own machine and input spec. A CustomJob will be cleaned up once the job enters terminal state (failed or succeeded).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Time when the CustomJob was created. |  [optional] [readonly] |
|**displayName** | **String** | Required. The display name of the CustomJob. The name can be up to 128 characters long and can consist of any UTF-8 characters. |  [optional] |
|**encryptionSpec** | [**GoogleCloudAiplatformV1beta1EncryptionSpec**](GoogleCloudAiplatformV1beta1EncryptionSpec.md) |  |  [optional] |
|**endTime** | **String** | Output only. Time when the CustomJob entered any of the following states: &#x60;JOB_STATE_SUCCEEDED&#x60;, &#x60;JOB_STATE_FAILED&#x60;, &#x60;JOB_STATE_CANCELLED&#x60;. |  [optional] [readonly] |
|**error** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  |  [optional] |
|**jobSpec** | [**GoogleCloudAiplatformV1beta1CustomJobSpec**](GoogleCloudAiplatformV1beta1CustomJobSpec.md) |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | The labels with user-defined metadata to organize CustomJobs. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. |  [optional] |
|**name** | **String** | Output only. Resource name of a CustomJob. |  [optional] [readonly] |
|**startTime** | **String** | Output only. Time when the CustomJob for the first time entered the &#x60;JOB_STATE_RUNNING&#x60; state. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The detailed state of the job. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. Time when the CustomJob was most recently updated. |  [optional] [readonly] |
|**webAccessUris** | **Map&lt;String, String&gt;** | Output only. URIs for accessing [interactive shells](https://cloud.google.com/vertex-ai/docs/training/monitor-debug-interactive-shell) (one URI for each training node). Only available if job_spec.enable_web_access is &#x60;true&#x60;. The keys are names of each node in the training job; for example, &#x60;workerpool0-0&#x60; for the primary node, &#x60;workerpool1-0&#x60; for the first node in the second worker pool, and &#x60;workerpool1-1&#x60; for the second node in the second worker pool. The values are the URIs for each node&#39;s interactive shell. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;JOB_STATE_UNSPECIFIED&quot; |
| QUEUED | &quot;JOB_STATE_QUEUED&quot; |
| PENDING | &quot;JOB_STATE_PENDING&quot; |
| RUNNING | &quot;JOB_STATE_RUNNING&quot; |
| SUCCEEDED | &quot;JOB_STATE_SUCCEEDED&quot; |
| FAILED | &quot;JOB_STATE_FAILED&quot; |
| CANCELLING | &quot;JOB_STATE_CANCELLING&quot; |
| CANCELLED | &quot;JOB_STATE_CANCELLED&quot; |
| PAUSED | &quot;JOB_STATE_PAUSED&quot; |
| EXPIRED | &quot;JOB_STATE_EXPIRED&quot; |
| UPDATING | &quot;JOB_STATE_UPDATING&quot; |
| PARTIALLY_SUCCEEDED | &quot;JOB_STATE_PARTIALLY_SUCCEEDED&quot; |



