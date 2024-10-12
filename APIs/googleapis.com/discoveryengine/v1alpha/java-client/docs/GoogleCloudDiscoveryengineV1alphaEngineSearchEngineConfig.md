

# GoogleCloudDiscoveryengineV1alphaEngineSearchEngineConfig

Configurations for a Search Engine.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**searchAddOns** | [**List&lt;SearchAddOnsEnum&gt;**](#List&lt;SearchAddOnsEnum&gt;) | The add-on that this search engine enables. |  [optional] |
|**searchTier** | [**SearchTierEnum**](#SearchTierEnum) | The search feature tier of this engine. Different tiers might have different pricing. To learn more, please check the pricing documentation. Defaults to SearchTier.SEARCH_TIER_STANDARD if not specified. |  [optional] |



## Enum: List&lt;SearchAddOnsEnum&gt;

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;SEARCH_ADD_ON_UNSPECIFIED&quot; |
| LLM | &quot;SEARCH_ADD_ON_LLM&quot; |



## Enum: SearchTierEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;SEARCH_TIER_UNSPECIFIED&quot; |
| STANDARD | &quot;SEARCH_TIER_STANDARD&quot; |
| ENTERPRISE | &quot;SEARCH_TIER_ENTERPRISE&quot; |



