

# GoogleCloudDiscoveryengineV1betaEngine

Metadata that describes the training and serving parameters of an Engine.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**chatEngineConfig** | [**GoogleCloudDiscoveryengineV1betaEngineChatEngineConfig**](GoogleCloudDiscoveryengineV1betaEngineChatEngineConfig.md) |  |  [optional] |
|**chatEngineMetadata** | [**GoogleCloudDiscoveryengineV1betaEngineChatEngineMetadata**](GoogleCloudDiscoveryengineV1betaEngineChatEngineMetadata.md) |  |  [optional] |
|**commonConfig** | [**GoogleCloudDiscoveryengineV1betaEngineCommonConfig**](GoogleCloudDiscoveryengineV1betaEngineCommonConfig.md) |  |  [optional] |
|**createTime** | **String** | Output only. Timestamp the Recommendation Engine was created at. |  [optional] [readonly] |
|**dataStoreIds** | **List&lt;String&gt;** | The data stores associated with this engine. For SOLUTION_TYPE_SEARCH and SOLUTION_TYPE_RECOMMENDATION type of engines, they can only associate with at most one data store. If solution_type is SOLUTION_TYPE_CHAT, multiple DataStores in the same Collection can be associated here. Note that when used in CreateEngineRequest, one DataStore id must be provided as the system will use it for necessary initializations. |  [optional] |
|**displayName** | **String** | Required. The display name of the engine. Should be human readable. UTF-8 encoded string with limit of 1024 characters. |  [optional] |
|**industryVertical** | [**IndustryVerticalEnum**](#IndustryVerticalEnum) | The industry vertical that the engine registers. The restriction of the Engine industry vertical is based on DataStore: If unspecified, default to &#x60;GENERIC&#x60;. Vertical on Engine has to match vertical of the DataStore liniked to the engine. |  [optional] |
|**name** | **String** | Immutable. The fully qualified resource name of the engine. This field must be a UTF-8 encoded string with a length limit of 1024 characters. Format: &#x60;projects/{project_number}/locations/{location}/collections/{collection}/engines/{engine}&#x60; engine should be 1-63 characters, and valid characters are /a-z0-9*_/. Otherwise, an INVALID_ARGUMENT error is returned. |  [optional] |
|**searchEngineConfig** | [**GoogleCloudDiscoveryengineV1betaEngineSearchEngineConfig**](GoogleCloudDiscoveryengineV1betaEngineSearchEngineConfig.md) |  |  [optional] |
|**solutionType** | [**SolutionTypeEnum**](#SolutionTypeEnum) | Required. The solutions of the engine. |  [optional] |
|**updateTime** | **String** | Output only. Timestamp the Recommendation Engine was last updated. |  [optional] [readonly] |



## Enum: IndustryVerticalEnum

| Name | Value |
|---- | -----|
| INDUSTRY_VERTICAL_UNSPECIFIED | &quot;INDUSTRY_VERTICAL_UNSPECIFIED&quot; |
| GENERIC | &quot;GENERIC&quot; |
| MEDIA | &quot;MEDIA&quot; |



## Enum: SolutionTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;SOLUTION_TYPE_UNSPECIFIED&quot; |
| RECOMMENDATION | &quot;SOLUTION_TYPE_RECOMMENDATION&quot; |
| SEARCH | &quot;SOLUTION_TYPE_SEARCH&quot; |
| CHAT | &quot;SOLUTION_TYPE_CHAT&quot; |



