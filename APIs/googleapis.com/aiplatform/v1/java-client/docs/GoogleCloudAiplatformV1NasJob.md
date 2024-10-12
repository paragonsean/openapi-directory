

# GoogleCloudAiplatformV1NasJob

Represents a Neural Architecture Search (NAS) job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Time when the NasJob was created. |  [optional] [readonly] |
|**displayName** | **String** | Required. The display name of the NasJob. The name can be up to 128 characters long and can consist of any UTF-8 characters. |  [optional] |
|**enableRestrictedImageTraining** | **Boolean** | Optional. Enable a separation of Custom model training and restricted image training for tenant project. |  [optional] |
|**encryptionSpec** | [**GoogleCloudAiplatformV1EncryptionSpec**](GoogleCloudAiplatformV1EncryptionSpec.md) |  |  [optional] |
|**endTime** | **String** | Output only. Time when the NasJob entered any of the following states: &#x60;JOB_STATE_SUCCEEDED&#x60;, &#x60;JOB_STATE_FAILED&#x60;, &#x60;JOB_STATE_CANCELLED&#x60;. |  [optional] [readonly] |
|**error** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | The labels with user-defined metadata to organize NasJobs. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. |  [optional] |
|**name** | **String** | Output only. Resource name of the NasJob. |  [optional] [readonly] |
|**nasJobOutput** | [**GoogleCloudAiplatformV1NasJobOutput**](GoogleCloudAiplatformV1NasJobOutput.md) |  |  [optional] |
|**nasJobSpec** | [**GoogleCloudAiplatformV1NasJobSpec**](GoogleCloudAiplatformV1NasJobSpec.md) |  |  [optional] |
|**startTime** | **String** | Output only. Time when the NasJob for the first time entered the &#x60;JOB_STATE_RUNNING&#x60; state. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The detailed state of the job. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. Time when the NasJob was most recently updated. |  [optional] [readonly] |



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



