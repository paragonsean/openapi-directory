

# BestSellers

Fields related to the [Best sellers reports](https://support.google.com/merchants/answer/9488679).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**categoryId** | **String** | Google product category ID to calculate the ranking for, represented in [Google&#39;s product taxonomy](https://support.google.com/merchants/answer/6324436). If a &#x60;WHERE&#x60; condition on &#x60;best_sellers.category_id&#x60; is not specified in the query, rankings for all top-level categories are returned. |  [optional] |
|**countryCode** | **String** | Country where the ranking is calculated. A &#x60;WHERE&#x60; condition on &#x60;best_sellers.country_code&#x60; is required in the query. |  [optional] |
|**previousRank** | **String** | Popularity rank in the previous week or month. |  [optional] |
|**previousRelativeDemand** | [**PreviousRelativeDemandEnum**](#PreviousRelativeDemandEnum) | Estimated demand in relation to the item with the highest popularity rank in the same category and country in the previous week or month. |  [optional] |
|**rank** | **String** | Popularity on Shopping ads and free listings, in the selected category and country, based on the estimated number of units sold. |  [optional] |
|**relativeDemand** | [**RelativeDemandEnum**](#RelativeDemandEnum) | Estimated demand in relation to the item with the highest popularity rank in the same category and country. |  [optional] |
|**relativeDemandChange** | [**RelativeDemandChangeEnum**](#RelativeDemandChangeEnum) | Change in the estimated demand. Whether it rose, sank or remained flat. |  [optional] |
|**reportDate** | [**Date**](Date.md) |  |  [optional] |
|**reportGranularity** | [**ReportGranularityEnum**](#ReportGranularityEnum) | Granularity of the report. The ranking can be done over a week or a month timeframe. A &#x60;WHERE&#x60; condition on &#x60;best_sellers.report_granularity&#x60; is required in the query. |  [optional] |



## Enum: PreviousRelativeDemandEnum

| Name | Value |
|---- | -----|
| RELATIVE_DEMAND_UNSPECIFIED | &quot;RELATIVE_DEMAND_UNSPECIFIED&quot; |
| VERY_LOW | &quot;VERY_LOW&quot; |
| LOW | &quot;LOW&quot; |
| MEDIUM | &quot;MEDIUM&quot; |
| HIGH | &quot;HIGH&quot; |
| VERY_HIGH | &quot;VERY_HIGH&quot; |



## Enum: RelativeDemandEnum

| Name | Value |
|---- | -----|
| RELATIVE_DEMAND_UNSPECIFIED | &quot;RELATIVE_DEMAND_UNSPECIFIED&quot; |
| VERY_LOW | &quot;VERY_LOW&quot; |
| LOW | &quot;LOW&quot; |
| MEDIUM | &quot;MEDIUM&quot; |
| HIGH | &quot;HIGH&quot; |
| VERY_HIGH | &quot;VERY_HIGH&quot; |



## Enum: RelativeDemandChangeEnum

| Name | Value |
|---- | -----|
| RELATIVE_DEMAND_CHANGE_TYPE_UNSPECIFIED | &quot;RELATIVE_DEMAND_CHANGE_TYPE_UNSPECIFIED&quot; |
| SINKER | &quot;SINKER&quot; |
| FLAT | &quot;FLAT&quot; |
| RISER | &quot;RISER&quot; |



## Enum: ReportGranularityEnum

| Name | Value |
|---- | -----|
| REPORT_GRANULARITY_UNSPECIFIED | &quot;REPORT_GRANULARITY_UNSPECIFIED&quot; |
| WEEKLY | &quot;WEEKLY&quot; |
| MONTHLY | &quot;MONTHLY&quot; |



