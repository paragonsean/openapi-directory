

# GoogleCloudContactcenterinsightsV1IssueModelInputDataConfig

Configs for the input data used to create the issue model.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**filter** | **String** | A filter to reduce the conversations used for training the model to a specific subset. |  [optional] |
|**medium** | [**MediumEnum**](#MediumEnum) | Medium of conversations used in training data. This field is being deprecated. To specify the medium to be used in training a new issue model, set the &#x60;medium&#x60; field on &#x60;filter&#x60;. |  [optional] |
|**trainingConversationsCount** | **String** | Output only. Number of conversations used in training. Output only. |  [optional] [readonly] |



## Enum: MediumEnum

| Name | Value |
|---- | -----|
| MEDIUM_UNSPECIFIED | &quot;MEDIUM_UNSPECIFIED&quot; |
| PHONE_CALL | &quot;PHONE_CALL&quot; |
| CHAT | &quot;CHAT&quot; |



