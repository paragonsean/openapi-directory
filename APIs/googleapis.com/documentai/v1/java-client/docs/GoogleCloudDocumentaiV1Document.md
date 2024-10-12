

# GoogleCloudDocumentaiV1Document

Document represents the canonical document resource in Document AI. It is an interchange format that provides insights into documents and allows for collaboration between users and Document AI to iterate and optimize for quality.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**content** | **byte[]** | Optional. Inline document content, represented as a stream of bytes. Note: As with all &#x60;bytes&#x60; fields, protobuffers use a pure binary representation, whereas JSON representations use base64. |  [optional] |
|**entities** | [**List&lt;GoogleCloudDocumentaiV1DocumentEntity&gt;**](GoogleCloudDocumentaiV1DocumentEntity.md) | A list of entities detected on Document.text. For document shards, entities in this list may cross shard boundaries. |  [optional] |
|**entityRelations** | [**List&lt;GoogleCloudDocumentaiV1DocumentEntityRelation&gt;**](GoogleCloudDocumentaiV1DocumentEntityRelation.md) | Placeholder. Relationship among Document.entities. |  [optional] |
|**error** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  |  [optional] |
|**mimeType** | **String** | An IANA published [media type (MIME type)](https://www.iana.org/assignments/media-types/media-types.xhtml). |  [optional] |
|**pages** | [**List&lt;GoogleCloudDocumentaiV1DocumentPage&gt;**](GoogleCloudDocumentaiV1DocumentPage.md) | Visual page layout for the Document. |  [optional] |
|**revisions** | [**List&lt;GoogleCloudDocumentaiV1DocumentRevision&gt;**](GoogleCloudDocumentaiV1DocumentRevision.md) | Placeholder. Revision history of this document. |  [optional] |
|**shardInfo** | [**GoogleCloudDocumentaiV1DocumentShardInfo**](GoogleCloudDocumentaiV1DocumentShardInfo.md) |  |  [optional] |
|**text** | **String** | Optional. UTF-8 encoded text in reading order from the document. |  [optional] |
|**textChanges** | [**List&lt;GoogleCloudDocumentaiV1DocumentTextChange&gt;**](GoogleCloudDocumentaiV1DocumentTextChange.md) | Placeholder. A list of text corrections made to Document.text. This is usually used for annotating corrections to OCR mistakes. Text changes for a given revision may not overlap with each other. |  [optional] |
|**textStyles** | [**List&lt;GoogleCloudDocumentaiV1DocumentStyle&gt;**](GoogleCloudDocumentaiV1DocumentStyle.md) | Styles for the Document.text. |  [optional] |
|**uri** | **String** | Optional. Currently supports Google Cloud Storage URI of the form &#x60;gs://bucket_name/object_name&#x60;. Object versioning is not supported. For more information, refer to [Google Cloud Storage Request URIs](https://cloud.google.com/storage/docs/reference-uris). |  [optional] |



