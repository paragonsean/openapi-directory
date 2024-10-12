# DialogflowApi.GoogleCloudDialogflowV2beta1Environment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agentVersion** | **String** | Optional. The agent version loaded into this environment. Supported formats: - &#x60;projects//agent/versions/&#x60; - &#x60;projects//locations//agent/versions/&#x60; | [optional] 
**description** | **String** | Optional. The developer-provided description for this environment. The maximum length is 500 characters. If exceeded, the request is rejected. | [optional] 
**fulfillment** | [**GoogleCloudDialogflowV2beta1Fulfillment**](GoogleCloudDialogflowV2beta1Fulfillment.md) |  | [optional] 
**name** | **String** | Output only. The unique identifier of this agent environment. Supported formats: - &#x60;projects//agent/environments/&#x60; - &#x60;projects//locations//agent/environments/&#x60; | [optional] [readonly] 
**state** | **String** | Output only. The state of this environment. This field is read-only, i.e., it cannot be set by create and update methods. | [optional] [readonly] 
**textToSpeechSettings** | [**GoogleCloudDialogflowV2beta1TextToSpeechSettings**](GoogleCloudDialogflowV2beta1TextToSpeechSettings.md) |  | [optional] 
**updateTime** | **String** | Output only. The last update time of this environment. This field is read-only, i.e., it cannot be set by create and update methods. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `STOPPED` (value: `"STOPPED"`)

* `LOADING` (value: `"LOADING"`)

* `RUNNING` (value: `"RUNNING"`)




