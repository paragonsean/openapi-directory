# VectaraRestApi.IndexingSection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customDims** | [**[VectaraindexingCustomDimension]**](VectaraindexingCustomDimension.md) | A list of custom dimension values that are included in the generated representation of all subsections (i.e. sections contains by this section). | [optional] 
**id** | **Number** | Optionally, the unique ID of this section. If set, it will be returned as metadata in query results. | [optional] 
**metadataJson** | **String** | Metadata about this section. This should be a json string. It is passed through the system, without being used at indexing time. It can be retrieved at query time. | [optional] 
**section** | [**[IndexingSection]**](IndexingSection.md) | A list of subsections. | [optional] 
**text** | **String** | The text of the section. This should never be empty. | [optional] 
**title** | **String** | Optionally, the title of the section. This may be empty. | [optional] 


