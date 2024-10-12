

# GoogleCloudDialogflowV2Version

You can create multiple versions of your agent and publish them to separate environments. When you edit an agent, you are editing the draft agent. At any point, you can save the draft agent as an agent version, which is an immutable snapshot of your agent. When you save the draft agent, it is published to the default environment. When you create agent versions, you can publish them to custom environments. You can create a variety of custom environments for: - testing - development - production - etc. For more information, see the [versions and environments guide](https://cloud.google.com/dialogflow/docs/agents-versions).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. The creation time of this version. This field is read-only, i.e., it cannot be set by create and update methods. |  [optional] [readonly] |
|**description** | **String** | Optional. The developer-provided description of this version. |  [optional] |
|**name** | **String** | Output only. The unique identifier of this agent version. Supported formats: - &#x60;projects//agent/versions/&#x60; - &#x60;projects//locations//agent/versions/&#x60; |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | Output only. The status of this version. This field is read-only and cannot be set by create and update methods. |  [optional] [readonly] |
|**versionNumber** | **Integer** | Output only. The sequential number of this version. This field is read-only which means it cannot be set by create and update methods. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| VERSION_STATUS_UNSPECIFIED | &quot;VERSION_STATUS_UNSPECIFIED&quot; |
| IN_PROGRESS | &quot;IN_PROGRESS&quot; |
| READY | &quot;READY&quot; |
| FAILED | &quot;FAILED&quot; |



