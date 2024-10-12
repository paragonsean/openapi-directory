

# GoogleCloudDialogflowV2Environment

You can create multiple versions of your agent and publish them to separate environments. When you edit an agent, you are editing the draft agent. At any point, you can save the draft agent as an agent version, which is an immutable snapshot of your agent. When you save the draft agent, it is published to the default environment. When you create agent versions, you can publish them to custom environments. You can create a variety of custom environments for: - testing - development - production - etc. For more information, see the [versions and environments guide](https://cloud.google.com/dialogflow/docs/agents-versions).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**agentVersion** | **String** | Optional. The agent version loaded into this environment. Supported formats: - &#x60;projects//agent/versions/&#x60; - &#x60;projects//locations//agent/versions/&#x60; |  [optional] |
|**description** | **String** | Optional. The developer-provided description for this environment. The maximum length is 500 characters. If exceeded, the request is rejected. |  [optional] |
|**fulfillment** | [**GoogleCloudDialogflowV2Fulfillment**](GoogleCloudDialogflowV2Fulfillment.md) |  |  [optional] |
|**name** | **String** | Output only. The unique identifier of this agent environment. Supported formats: - &#x60;projects//agent/environments/&#x60; - &#x60;projects//locations//agent/environments/&#x60; The environment ID for the default environment is &#x60;-&#x60;. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The state of this environment. This field is read-only, i.e., it cannot be set by create and update methods. |  [optional] [readonly] |
|**textToSpeechSettings** | [**GoogleCloudDialogflowV2TextToSpeechSettings**](GoogleCloudDialogflowV2TextToSpeechSettings.md) |  |  [optional] |
|**updateTime** | **String** | Output only. The last update time of this environment. This field is read-only, i.e., it cannot be set by create and update methods. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| STOPPED | &quot;STOPPED&quot; |
| LOADING | &quot;LOADING&quot; |
| RUNNING | &quot;RUNNING&quot; |



