# ContentApiForShopping.BestSellers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categoryId** | **String** | Google product category ID to calculate the ranking for, represented in [Google&#39;s product taxonomy](https://support.google.com/merchants/answer/6324436). If a &#x60;WHERE&#x60; condition on &#x60;best_sellers.category_id&#x60; is not specified in the query, rankings for all top-level categories are returned. | [optional] 
**countryCode** | **String** | Country where the ranking is calculated. A &#x60;WHERE&#x60; condition on &#x60;best_sellers.country_code&#x60; is required in the query. | [optional] 
**previousRank** | **String** | Popularity rank in the previous week or month. | [optional] 
**previousRelativeDemand** | **String** | Estimated demand in relation to the item with the highest popularity rank in the same category and country in the previous week or month. | [optional] 
**rank** | **String** | Popularity on Shopping ads and free listings, in the selected category and country, based on the estimated number of units sold. | [optional] 
**relativeDemand** | **String** | Estimated demand in relation to the item with the highest popularity rank in the same category and country. | [optional] 
**relativeDemandChange** | **String** | Change in the estimated demand. Whether it rose, sank or remained flat. | [optional] 
**reportDate** | [**ModelDate**](ModelDate.md) |  | [optional] 
**reportGranularity** | **String** | Granularity of the report. The ranking can be done over a week or a month timeframe. A &#x60;WHERE&#x60; condition on &#x60;best_sellers.report_granularity&#x60; is required in the query. | [optional] 



## Enum: PreviousRelativeDemandEnum


* `RELATIVE_DEMAND_UNSPECIFIED` (value: `"RELATIVE_DEMAND_UNSPECIFIED"`)

* `VERY_LOW` (value: `"VERY_LOW"`)

* `LOW` (value: `"LOW"`)

* `MEDIUM` (value: `"MEDIUM"`)

* `HIGH` (value: `"HIGH"`)

* `VERY_HIGH` (value: `"VERY_HIGH"`)





## Enum: RelativeDemandEnum


* `RELATIVE_DEMAND_UNSPECIFIED` (value: `"RELATIVE_DEMAND_UNSPECIFIED"`)

* `VERY_LOW` (value: `"VERY_LOW"`)

* `LOW` (value: `"LOW"`)

* `MEDIUM` (value: `"MEDIUM"`)

* `HIGH` (value: `"HIGH"`)

* `VERY_HIGH` (value: `"VERY_HIGH"`)





## Enum: RelativeDemandChangeEnum


* `RELATIVE_DEMAND_CHANGE_TYPE_UNSPECIFIED` (value: `"RELATIVE_DEMAND_CHANGE_TYPE_UNSPECIFIED"`)

* `SINKER` (value: `"SINKER"`)

* `FLAT` (value: `"FLAT"`)

* `RISER` (value: `"RISER"`)





## Enum: ReportGranularityEnum


* `REPORT_GRANULARITY_UNSPECIFIED` (value: `"REPORT_GRANULARITY_UNSPECIFIED"`)

* `WEEKLY` (value: `"WEEKLY"`)

* `MONTHLY` (value: `"MONTHLY"`)




