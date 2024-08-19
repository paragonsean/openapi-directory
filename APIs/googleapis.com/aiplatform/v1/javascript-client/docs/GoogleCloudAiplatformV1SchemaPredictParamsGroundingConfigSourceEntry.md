# VertexAiApi.GoogleCloudAiplatformV1SchemaPredictParamsGroundingConfigSourceEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enterpriseDatastore** | **String** | The uri of the Vertex AI Search data source. Deprecated. Use vertex_ai_search_datastore instead. | [optional] 
**inlineContext** | **String** | The grounding text passed inline with the Predict API. It can support up to 1 million bytes. | [optional] 
**type** | **String** | The type of the grounding checking source. | [optional] 
**vertexAiSearchDatastore** | **String** | The uri of the Vertex AI Search data source. | [optional] 



## Enum: TypeEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `WEB` (value: `"WEB"`)

* `ENTERPRISE` (value: `"ENTERPRISE"`)

* `VERTEX_AI_SEARCH` (value: `"VERTEX_AI_SEARCH"`)

* `INLINE` (value: `"INLINE"`)




