# ContactCenterAiInsightsApi.GoogleCloudContactcenterinsightsV1IssueModelInputDataConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **String** | A filter to reduce the conversations used for training the model to a specific subset. | [optional] 
**medium** | **String** | Medium of conversations used in training data. This field is being deprecated. To specify the medium to be used in training a new issue model, set the &#x60;medium&#x60; field on &#x60;filter&#x60;. | [optional] 
**trainingConversationsCount** | **String** | Output only. Number of conversations used in training. Output only. | [optional] [readonly] 



## Enum: MediumEnum


* `MEDIUM_UNSPECIFIED` (value: `"MEDIUM_UNSPECIFIED"`)

* `PHONE_CALL` (value: `"PHONE_CALL"`)

* `CHAT` (value: `"CHAT"`)




