# DialogflowApi.GoogleCloudDialogflowV2beta1Document

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **String** | The raw content of the document. This field is only permitted for EXTRACTIVE_QA and FAQ knowledge types. Note: This field is in the process of being deprecated, please use raw_content instead. | [optional] 
**contentUri** | **String** | The URI where the file content is located. For documents stored in Google Cloud Storage, these URIs must have the form &#x60;gs:///&#x60;. NOTE: External URLs must correspond to public webpages, i.e., they must be indexed by Google Search. In particular, URLs for showing documents in Google Cloud Storage (i.e. the URL in your browser) are not supported. Instead use the &#x60;gs://&#x60; format URI described above. | [optional] 
**displayName** | **String** | Required. The display name of the document. The name must be 1024 bytes or less; otherwise, the creation request fails. | [optional] 
**enableAutoReload** | **Boolean** | Optional. If true, we try to automatically reload the document every day (at a time picked by the system). If false or unspecified, we don&#39;t try to automatically reload the document. Currently you can only enable automatic reload for documents sourced from a public url, see &#x60;source&#x60; field for the source types. Reload status can be tracked in &#x60;latest_reload_status&#x60;. If a reload fails, we will keep the document unchanged. If a reload fails with internal errors, the system will try to reload the document on the next day. If a reload fails with non-retriable errors (e.g. PERMISSION_DENIED), the system will not try to reload the document anymore. You need to manually reload the document successfully by calling &#x60;ReloadDocument&#x60; and clear the errors. | [optional] 
**knowledgeTypes** | **[String]** | Required. The knowledge type of document content. | [optional] 
**latestReloadStatus** | [**GoogleCloudDialogflowV2beta1DocumentReloadStatus**](GoogleCloudDialogflowV2beta1DocumentReloadStatus.md) |  | [optional] 
**metadata** | **{String: String}** | Optional. Metadata for the document. The metadata supports arbitrary key-value pairs. Suggested use cases include storing a document&#39;s title, an external URL distinct from the document&#39;s content_uri, etc. The max size of a &#x60;key&#x60; or a &#x60;value&#x60; of the metadata is 1024 bytes. | [optional] 
**mimeType** | **String** | Required. The MIME type of this document. | [optional] 
**name** | **String** | Optional. The document resource name. The name must be empty when creating a document. Format: &#x60;projects//locations//knowledgeBases//documents/&#x60;. | [optional] 
**rawContent** | **Blob** | The raw content of the document. This field is only permitted for EXTRACTIVE_QA and FAQ knowledge types. | [optional] 
**state** | **String** | Output only. The current state of the document. | [optional] [readonly] 



## Enum: [KnowledgeTypesEnum]


* `KNOWLEDGE_TYPE_UNSPECIFIED` (value: `"KNOWLEDGE_TYPE_UNSPECIFIED"`)

* `FAQ` (value: `"FAQ"`)

* `EXTRACTIVE_QA` (value: `"EXTRACTIVE_QA"`)

* `ARTICLE_SUGGESTION` (value: `"ARTICLE_SUGGESTION"`)

* `AGENT_FACING_SMART_REPLY` (value: `"AGENT_FACING_SMART_REPLY"`)

* `SMART_REPLY` (value: `"SMART_REPLY"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `UPDATING` (value: `"UPDATING"`)

* `RELOADING` (value: `"RELOADING"`)

* `DELETING` (value: `"DELETING"`)




