# DialogflowApi.GoogleCloudDialogflowV2beta1ImportDocumentTemplate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**knowledgeTypes** | **[String]** | Required. The knowledge type of document content. | [optional] 
**metadata** | **{String: String}** | Metadata for the document. The metadata supports arbitrary key-value pairs. Suggested use cases include storing a document&#39;s title, an external URL distinct from the document&#39;s content_uri, etc. The max size of a &#x60;key&#x60; or a &#x60;value&#x60; of the metadata is 1024 bytes. | [optional] 
**mimeType** | **String** | Required. The MIME type of the document. | [optional] 



## Enum: [KnowledgeTypesEnum]


* `KNOWLEDGE_TYPE_UNSPECIFIED` (value: `"KNOWLEDGE_TYPE_UNSPECIFIED"`)

* `FAQ` (value: `"FAQ"`)

* `EXTRACTIVE_QA` (value: `"EXTRACTIVE_QA"`)

* `ARTICLE_SUGGESTION` (value: `"ARTICLE_SUGGESTION"`)

* `AGENT_FACING_SMART_REPLY` (value: `"AGENT_FACING_SMART_REPLY"`)

* `SMART_REPLY` (value: `"SMART_REPLY"`)




