

# GoogleCloudDialogflowV2beta1QueryInput

Represents the query input. It can contain either: 1. An audio config which instructs the speech recognizer how to process the speech audio. 2. A conversational query in the form of text. 3. An event that specifies which intent to trigger.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**audioConfig** | [**GoogleCloudDialogflowV2beta1InputAudioConfig**](GoogleCloudDialogflowV2beta1InputAudioConfig.md) |  |  [optional] |
|**dtmf** | [**GoogleCloudDialogflowV2beta1TelephonyDtmfEvents**](GoogleCloudDialogflowV2beta1TelephonyDtmfEvents.md) |  |  [optional] |
|**event** | [**GoogleCloudDialogflowV2beta1EventInput**](GoogleCloudDialogflowV2beta1EventInput.md) |  |  [optional] |
|**text** | [**GoogleCloudDialogflowV2beta1TextInput**](GoogleCloudDialogflowV2beta1TextInput.md) |  |  [optional] |



