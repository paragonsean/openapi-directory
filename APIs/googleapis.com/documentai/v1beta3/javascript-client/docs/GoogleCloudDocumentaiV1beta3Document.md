# CloudDocumentAiApi.GoogleCloudDocumentaiV1beta3Document

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **Blob** | Optional. Inline document content, represented as a stream of bytes. Note: As with all &#x60;bytes&#x60; fields, protobuffers use a pure binary representation, whereas JSON representations use base64. | [optional] 
**entities** | [**[GoogleCloudDocumentaiV1beta3DocumentEntity]**](GoogleCloudDocumentaiV1beta3DocumentEntity.md) | A list of entities detected on Document.text. For document shards, entities in this list may cross shard boundaries. | [optional] 
**entityRelations** | [**[GoogleCloudDocumentaiV1beta3DocumentEntityRelation]**](GoogleCloudDocumentaiV1beta3DocumentEntityRelation.md) | Placeholder. Relationship among Document.entities. | [optional] 
**error** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  | [optional] 
**mimeType** | **String** | An IANA published [media type (MIME type)](https://www.iana.org/assignments/media-types/media-types.xhtml). | [optional] 
**pages** | [**[GoogleCloudDocumentaiV1beta3DocumentPage]**](GoogleCloudDocumentaiV1beta3DocumentPage.md) | Visual page layout for the Document. | [optional] 
**revisions** | [**[GoogleCloudDocumentaiV1beta3DocumentRevision]**](GoogleCloudDocumentaiV1beta3DocumentRevision.md) | Placeholder. Revision history of this document. | [optional] 
**shardInfo** | [**GoogleCloudDocumentaiV1beta3DocumentShardInfo**](GoogleCloudDocumentaiV1beta3DocumentShardInfo.md) |  | [optional] 
**text** | **String** | Optional. UTF-8 encoded text in reading order from the document. | [optional] 
**textChanges** | [**[GoogleCloudDocumentaiV1beta3DocumentTextChange]**](GoogleCloudDocumentaiV1beta3DocumentTextChange.md) | Placeholder. A list of text corrections made to Document.text. This is usually used for annotating corrections to OCR mistakes. Text changes for a given revision may not overlap with each other. | [optional] 
**textStyles** | [**[GoogleCloudDocumentaiV1beta3DocumentStyle]**](GoogleCloudDocumentaiV1beta3DocumentStyle.md) | Styles for the Document.text. | [optional] 
**uri** | **String** | Optional. Currently supports Google Cloud Storage URI of the form &#x60;gs://bucket_name/object_name&#x60;. Object versioning is not supported. For more information, refer to [Google Cloud Storage Request URIs](https://cloud.google.com/storage/docs/reference-uris). | [optional] 


