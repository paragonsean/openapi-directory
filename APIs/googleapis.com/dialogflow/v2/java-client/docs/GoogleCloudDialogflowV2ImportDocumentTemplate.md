

# GoogleCloudDialogflowV2ImportDocumentTemplate

The template used for importing documents.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**knowledgeTypes** | [**List&lt;KnowledgeTypesEnum&gt;**](#List&lt;KnowledgeTypesEnum&gt;) | Required. The knowledge type of document content. |  [optional] |
|**metadata** | **Map&lt;String, String&gt;** | Metadata for the document. The metadata supports arbitrary key-value pairs. Suggested use cases include storing a document&#39;s title, an external URL distinct from the document&#39;s content_uri, etc. The max size of a &#x60;key&#x60; or a &#x60;value&#x60; of the metadata is 1024 bytes. |  [optional] |
|**mimeType** | **String** | Required. The MIME type of the document. |  [optional] |



## Enum: List&lt;KnowledgeTypesEnum&gt;

| Name | Value |
|---- | -----|
| KNOWLEDGE_TYPE_UNSPECIFIED | &quot;KNOWLEDGE_TYPE_UNSPECIFIED&quot; |
| FAQ | &quot;FAQ&quot; |
| EXTRACTIVE_QA | &quot;EXTRACTIVE_QA&quot; |
| ARTICLE_SUGGESTION | &quot;ARTICLE_SUGGESTION&quot; |
| AGENT_FACING_SMART_REPLY | &quot;AGENT_FACING_SMART_REPLY&quot; |



