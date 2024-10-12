# DialogflowApi.GoogleCloudDialogflowV2beta1ExportAgentRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agentUri** | **String** | Optional. The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI to export the agent to. The format of this URI must be &#x60;gs:///&#x60;. If left unspecified, the serialized agent is returned inline. Dialogflow performs a write operation for the Cloud Storage object on the caller&#39;s behalf, so your request authentication must have write permissions for the object. For more information, see [Dialogflow access control](https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage). | [optional] 


