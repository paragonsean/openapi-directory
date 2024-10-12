# DialogflowApi.GoogleCloudDialogflowV2AnalyzeContentRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assistQueryParams** | [**GoogleCloudDialogflowV2AssistQueryParameters**](GoogleCloudDialogflowV2AssistQueryParameters.md) |  | [optional] 
**cxParameters** | **{String: Object}** | Additional parameters to be put into Dialogflow CX session parameters. To remove a parameter from the session, clients should explicitly set the parameter value to null. Note: this field should only be used if you are connecting to a Dialogflow CX agent. | [optional] 
**eventInput** | [**GoogleCloudDialogflowV2EventInput**](GoogleCloudDialogflowV2EventInput.md) |  | [optional] 
**queryParams** | [**GoogleCloudDialogflowV2QueryParameters**](GoogleCloudDialogflowV2QueryParameters.md) |  | [optional] 
**replyAudioConfig** | [**GoogleCloudDialogflowV2OutputAudioConfig**](GoogleCloudDialogflowV2OutputAudioConfig.md) |  | [optional] 
**requestId** | **String** | A unique identifier for this request. Restricted to 36 ASCII characters. A random UUID is recommended. This request is only idempotent if a &#x60;request_id&#x60; is provided. | [optional] 
**suggestionInput** | [**GoogleCloudDialogflowV2SuggestionInput**](GoogleCloudDialogflowV2SuggestionInput.md) |  | [optional] 
**textInput** | [**GoogleCloudDialogflowV2TextInput**](GoogleCloudDialogflowV2TextInput.md) |  | [optional] 


