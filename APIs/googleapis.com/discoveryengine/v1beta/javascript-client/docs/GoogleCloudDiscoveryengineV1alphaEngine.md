# DiscoveryEngineApi.GoogleCloudDiscoveryengineV1alphaEngine

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowMultipleDataStoresSearchEngine** | **Boolean** | Whether the search engine can associate with multiple data stores. If true, the generic search engine can associate with one or more data stores. This is an input-only field. | [optional] 
**chatEngineConfig** | [**GoogleCloudDiscoveryengineV1alphaEngineChatEngineConfig**](GoogleCloudDiscoveryengineV1alphaEngineChatEngineConfig.md) |  | [optional] 
**chatEngineMetadata** | [**GoogleCloudDiscoveryengineV1alphaEngineChatEngineMetadata**](GoogleCloudDiscoveryengineV1alphaEngineChatEngineMetadata.md) |  | [optional] 
**commonConfig** | [**GoogleCloudDiscoveryengineV1alphaEngineCommonConfig**](GoogleCloudDiscoveryengineV1alphaEngineCommonConfig.md) |  | [optional] 
**createTime** | **String** | Output only. Timestamp the Recommendation Engine was created at. | [optional] [readonly] 
**dataStoreIds** | **[String]** | The data stores associated with this engine. For SOLUTION_TYPE_SEARCH and SOLUTION_TYPE_RECOMMENDATION type of engines, they can only associate with at most one data store. If solution_type is SOLUTION_TYPE_CHAT, multiple DataStores in the same Collection can be associated here. Note that when used in CreateEngineRequest, one DataStore id must be provided as the system will use it for necessary initializations. | [optional] 
**displayName** | **String** | Required. The display name of the engine. Should be human readable. UTF-8 encoded string with limit of 1024 characters. | [optional] 
**industryVertical** | **String** | The industry vertical that the engine registers. The restriction of the Engine industry vertical is based on DataStore: If unspecified, default to &#x60;GENERIC&#x60;. Vertical on Engine has to match vertical of the DataStore liniked to the engine. | [optional] 
**mediaRecommendationEngineConfig** | [**GoogleCloudDiscoveryengineV1alphaEngineMediaRecommendationEngineConfig**](GoogleCloudDiscoveryengineV1alphaEngineMediaRecommendationEngineConfig.md) |  | [optional] 
**name** | **String** | Immutable. The fully qualified resource name of the engine. This field must be a UTF-8 encoded string with a length limit of 1024 characters. Format: &#x60;projects/{project_number}/locations/{location}/collections/{collection}/engines/{engine}&#x60; engine should be 1-63 characters, and valid characters are /a-z0-9*_/. Otherwise, an INVALID_ARGUMENT error is returned. | [optional] 
**recommendationMetadata** | [**GoogleCloudDiscoveryengineV1alphaEngineRecommendationMetadata**](GoogleCloudDiscoveryengineV1alphaEngineRecommendationMetadata.md) |  | [optional] 
**searchEngineConfig** | [**GoogleCloudDiscoveryengineV1alphaEngineSearchEngineConfig**](GoogleCloudDiscoveryengineV1alphaEngineSearchEngineConfig.md) |  | [optional] 
**similarDocumentsConfig** | **Object** | Additional config specs for a &#x60;similar-items&#x60; engine. | [optional] 
**solutionType** | **String** | Required. The solutions of the engine. | [optional] 
**updateTime** | **String** | Output only. Timestamp the Recommendation Engine was last updated. | [optional] [readonly] 



## Enum: IndustryVerticalEnum


* `INDUSTRY_VERTICAL_UNSPECIFIED` (value: `"INDUSTRY_VERTICAL_UNSPECIFIED"`)

* `GENERIC` (value: `"GENERIC"`)

* `MEDIA` (value: `"MEDIA"`)





## Enum: SolutionTypeEnum


* `UNSPECIFIED` (value: `"SOLUTION_TYPE_UNSPECIFIED"`)

* `RECOMMENDATION` (value: `"SOLUTION_TYPE_RECOMMENDATION"`)

* `SEARCH` (value: `"SOLUTION_TYPE_SEARCH"`)

* `CHAT` (value: `"SOLUTION_TYPE_CHAT"`)




