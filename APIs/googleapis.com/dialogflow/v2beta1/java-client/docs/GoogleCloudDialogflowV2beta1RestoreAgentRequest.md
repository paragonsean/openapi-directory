

# GoogleCloudDialogflowV2beta1RestoreAgentRequest

The request message for Agents.RestoreAgent.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**agentContent** | **byte[]** | Zip compressed raw byte content for agent. |  [optional] |
|**agentUri** | **String** | The URI to a Google Cloud Storage file containing the agent to restore. Note: The URI must start with \&quot;gs://\&quot;. Dialogflow performs a read operation for the Cloud Storage object on the caller&#39;s behalf, so your request authentication must have read permissions for the object. For more information, see [Dialogflow access control](https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage). |  [optional] |



