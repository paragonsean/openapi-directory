# VectaraRestApi.VectaraindexingDocument

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customDims** | [**[VectaraindexingCustomDimension]**](VectaraindexingCustomDimension.md) | A list of custom dimension values that are included in the generated representation of all sections. | [optional] 
**description** | **String** | An optional description for the document. | [optional] 
**documentId** | **String** | Client assigned document ID to this document. | [optional] 
**metadataJson** | **String** | Metadata about the document. This should be a json string, and it can be retrieved at query time. | [optional] 
**section** | [**[IndexingSection]**](IndexingSection.md) | The actual content of the document, structured as a repeating list of sections. | [optional] 
**title** | **String** | The title of the document. | [optional] 


