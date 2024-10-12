

# GoogleCloudDialogflowV2KnowledgeBase

A knowledge base represents a collection of knowledge documents that you provide to Dialogflow. Your knowledge documents contain information that may be useful during conversations with end-users. Some Dialogflow features use knowledge bases when looking for a response to an end-user input. For more information, see the [knowledge base guide](https://cloud.google.com/dialogflow/docs/how/knowledge-bases). Note: The `projects.agent.knowledgeBases` resource is deprecated; only use `projects.knowledgeBases`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | Required. The display name of the knowledge base. The name must be 1024 bytes or less; otherwise, the creation request fails. |  [optional] |
|**languageCode** | **String** | Language which represents the KnowledgeBase. When the KnowledgeBase is created/updated, expect this to be present for non en-us languages. When unspecified, the default language code en-us applies. |  [optional] |
|**name** | **String** | The knowledge base resource name. The name must be empty when creating a knowledge base. Format: &#x60;projects//locations//knowledgeBases/&#x60;. |  [optional] |



