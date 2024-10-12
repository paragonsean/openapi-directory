# DiscoveryEngineApi.GoogleCloudDiscoveryengineV1Engine

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chatEngineConfig** | [**GoogleCloudDiscoveryengineV1EngineChatEngineConfig**](GoogleCloudDiscoveryengineV1EngineChatEngineConfig.md) |  | [optional] 
**chatEngineMetadata** | [**GoogleCloudDiscoveryengineV1EngineChatEngineMetadata**](GoogleCloudDiscoveryengineV1EngineChatEngineMetadata.md) |  | [optional] 
**commonConfig** | [**GoogleCloudDiscoveryengineV1EngineCommonConfig**](GoogleCloudDiscoveryengineV1EngineCommonConfig.md) |  | [optional] 
**createTime** | **String** | Output only. Timestamp the Recommendation Engine was created at. | [optional] [readonly] 
**dataStoreIds** | **[String]** | The data stores associated with this engine. For SOLUTION_TYPE_SEARCH and SOLUTION_TYPE_RECOMMENDATION type of engines, they can only associate with at most one data store. If solution_type is SOLUTION_TYPE_CHAT, multiple DataStores in the same Collection can be associated here. Note that when used in CreateEngineRequest, one DataStore id must be provided as the system will use it for necessary initializations. | [optional] 
**displayName** | **String** | Required. The display name of the engine. Should be human readable. UTF-8 encoded string with limit of 1024 characters. | [optional] 
**industryVertical** | **String** | The industry vertical that the engine registers. The restriction of the Engine industry vertical is based on DataStore: If unspecified, default to &#x60;GENERIC&#x60;. Vertical on Engine has to match vertical of the DataStore liniked to the engine. | [optional] 
**name** | **String** | Immutable. The fully qualified resource name of the engine. This field must be a UTF-8 encoded string with a length limit of 1024 characters. Format: &#x60;projects/{project_number}/locations/{location}/collections/{collection}/engines/{engine}&#x60; engine should be 1-63 characters, and valid characters are /a-z0-9*_/. Otherwise, an INVALID_ARGUMENT error is returned. | [optional] 
**searchEngineConfig** | [**GoogleCloudDiscoveryengineV1EngineSearchEngineConfig**](GoogleCloudDiscoveryengineV1EngineSearchEngineConfig.md) |  | [optional] 
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




