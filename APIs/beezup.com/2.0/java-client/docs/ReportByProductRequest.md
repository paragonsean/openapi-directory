

# ReportByProductRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advancedFilters** | [**ReportAdvancedFilters**](ReportAdvancedFilters.md) |  |  |
|**beginPeriodUtcDate** | **OffsetDateTime** | The begin date period you want to get the report. It&#39;s required only in case of custom period type ! |  |
|**categoryFilter** | [**BeezUPCommonCatalogCategoryFilter**](BeezUPCommonCatalogCategoryFilter.md) |  |  [optional] |
|**channelId** | **String** | The channel identifier |  [optional] |
|**endPeriodUtcDate** | **OffsetDateTime** | The end date period you want to get the report. It&#39;s required only in case of custom period type ! |  |
|**performanceIndicatorFilters** | [**List&lt;PerformanceIndicatorFilter&gt;**](PerformanceIndicatorFilter.md) |  |  [optional] |
|**periodType** | **ReportFilterPeriodType** |  |  |
|**orderBy** | **PerformanceIndicatorType** |  |  [optional] |
|**orderByDirection** | **OrderByDirection** |  |  [optional] |
|**pageNumber** | **Integer** | Indicates the page number |  [optional] |
|**pageSize** | **Integer** | Indicate the item count per page |  [optional] |
|**analyticsProductColumnFilters** | [**AnalyticsProductColumnFilters**](AnalyticsProductColumnFilters.md) |  |  [optional] |
|**productColumnsToDisplay** | **List&lt;String&gt;** |  |  [optional] |
|**productState** | **ProductStateFilter** |  |  |



