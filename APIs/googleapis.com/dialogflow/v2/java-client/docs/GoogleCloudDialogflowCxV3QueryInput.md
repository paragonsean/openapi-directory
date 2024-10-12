

# GoogleCloudDialogflowCxV3QueryInput

Represents the query input. It can contain one of: 1. A conversational query in the form of text. 2. An intent query that specifies which intent to trigger. 3. Natural language speech audio to be processed. 4. An event to be triggered. 5. DTMF digits to invoke an intent and fill in parameter value. 6. The results of a tool executed by the client.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**audio** | [**GoogleCloudDialogflowCxV3AudioInput**](GoogleCloudDialogflowCxV3AudioInput.md) |  |  [optional] |
|**dtmf** | [**GoogleCloudDialogflowCxV3DtmfInput**](GoogleCloudDialogflowCxV3DtmfInput.md) |  |  [optional] |
|**event** | [**GoogleCloudDialogflowCxV3EventInput**](GoogleCloudDialogflowCxV3EventInput.md) |  |  [optional] |
|**intent** | [**GoogleCloudDialogflowCxV3IntentInput**](GoogleCloudDialogflowCxV3IntentInput.md) |  |  [optional] |
|**languageCode** | **String** | Required. The language of the input. See [Language Support](https://cloud.google.com/dialogflow/cx/docs/reference/language) for a list of the currently supported language codes. Note that queries in the same session do not necessarily need to specify the same language. |  [optional] |
|**text** | [**GoogleCloudDialogflowCxV3TextInput**](GoogleCloudDialogflowCxV3TextInput.md) |  |  [optional] |



