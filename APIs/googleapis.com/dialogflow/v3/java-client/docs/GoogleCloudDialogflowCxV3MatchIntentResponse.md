

# GoogleCloudDialogflowCxV3MatchIntentResponse

Response of MatchIntent.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currentPage** | [**GoogleCloudDialogflowCxV3Page**](GoogleCloudDialogflowCxV3Page.md) |  |  [optional] |
|**matches** | [**List&lt;GoogleCloudDialogflowCxV3Match&gt;**](GoogleCloudDialogflowCxV3Match.md) | Match results, if more than one, ordered descendingly by the confidence we have that the particular intent matches the query. |  [optional] |
|**text** | **String** | If natural language text was provided as input, this field will contain a copy of the text. |  [optional] |
|**transcript** | **String** | If natural language speech audio was provided as input, this field will contain the transcript for the audio. |  [optional] |
|**triggerEvent** | **String** | If an event was provided as input, this field will contain a copy of the event name. |  [optional] |
|**triggerIntent** | **String** | If an intent was provided as input, this field will contain a copy of the intent identifier. Format: &#x60;projects//locations//agents//intents/&#x60;. |  [optional] |



