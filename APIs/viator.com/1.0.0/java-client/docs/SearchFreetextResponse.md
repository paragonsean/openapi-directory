

# SearchFreetextResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**searchType** | [**SearchTypeEnum**](#SearchTypeEnum) | **indicator** of the entity type for *this* result that is *one of*:   - &#x60;\&quot;PRODUCT\&quot;&#x60;: a tour / activity   - &#x60;\&quot;DESTINATION\&quot;&#x60;: continent, country, city, region   - &#x60;\&quot;ATTRACTION\&quot;&#x60;: an attraction within a destination (only available to partners with SEO access)   - &#x60;\&quot;RECOMMENDATION\&quot;&#x60;: an attraction within a destination (only available to partners with SEO access)  |  [optional] |
|**sortOrder** | **Integer** | **sort order** for *this* data object |  [optional] |



## Enum: SearchTypeEnum

| Name | Value |
|---- | -----|
| PRODUCT | &quot;PRODUCT&quot; |
| DESTINATION | &quot;DESTINATION&quot; |
| ATTRACTION | &quot;ATTRACTION&quot; |
| RECOMMENDATION | &quot;RECOMMENDATION&quot; |



