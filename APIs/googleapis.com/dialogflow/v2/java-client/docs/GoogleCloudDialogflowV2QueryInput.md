

# GoogleCloudDialogflowV2QueryInput

Represents the query input. It can contain either: 1. An audio config which instructs the speech recognizer how to process the speech audio. 2. A conversational query in the form of text. 3. An event that specifies which intent to trigger.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**audioConfig** | [**GoogleCloudDialogflowV2InputAudioConfig**](GoogleCloudDialogflowV2InputAudioConfig.md) |  |  [optional] |
|**event** | [**GoogleCloudDialogflowV2EventInput**](GoogleCloudDialogflowV2EventInput.md) |  |  [optional] |
|**text** | [**GoogleCloudDialogflowV2TextInput**](GoogleCloudDialogflowV2TextInput.md) |  |  [optional] |



