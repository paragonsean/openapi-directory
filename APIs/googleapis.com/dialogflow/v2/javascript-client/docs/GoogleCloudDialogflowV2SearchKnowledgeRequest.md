# DialogflowApi.GoogleCloudDialogflowV2SearchKnowledgeRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation** | **String** | The conversation (between human agent and end user) where the search request is triggered. Format: &#x60;projects//locations//conversations/&#x60;. | [optional] 
**conversationProfile** | **String** | Required. The conversation profile used to configure the search. Format: &#x60;projects//locations//conversationProfiles/&#x60;. | [optional] 
**latestMessage** | **String** | The name of the latest conversation message when the request is triggered. Format: &#x60;projects//locations//conversations//messages/&#x60;. | [optional] 
**parent** | **String** | The parent resource contains the conversation profile Format: &#39;projects/&#39; or &#x60;projects//locations/&#x60;. | [optional] 
**query** | [**GoogleCloudDialogflowV2TextInput**](GoogleCloudDialogflowV2TextInput.md) |  | [optional] 
**sessionId** | **String** | The ID of the search session. The session_id can be combined with Dialogflow V3 Agent ID retrieved from conversation profile or on its own to identify a search session. The search history of the same session will impact the search result. It&#39;s up to the API caller to choose an appropriate &#x60;Session ID&#x60;. It can be a random number or some type of session identifiers (preferably hashed). The length must not exceed 36 characters. | [optional] 


