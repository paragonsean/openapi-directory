# CampaignManager360Api.ReportCrossDimensionReachCriteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**breakdown** | [**[SortedDimension]**](SortedDimension.md) | The list of dimensions the report should include. | [optional] 
**dateRange** | [**DateRange**](DateRange.md) |  | [optional] 
**dimension** | **String** | The dimension option. | [optional] 
**dimensionFilters** | [**[DimensionValue]**](DimensionValue.md) | The list of filters on which dimensions are filtered. | [optional] 
**metricNames** | **[String]** | The list of names of metrics the report should include. | [optional] 
**overlapMetricNames** | **[String]** | The list of names of overlap metrics the report should include. | [optional] 
**pivoted** | **Boolean** | Whether the report is pivoted or not. Defaults to true. | [optional] 



## Enum: DimensionEnum


* `ADVERTISER` (value: `"ADVERTISER"`)

* `CAMPAIGN` (value: `"CAMPAIGN"`)

* `SITE_BY_ADVERTISER` (value: `"SITE_BY_ADVERTISER"`)

* `SITE_BY_CAMPAIGN` (value: `"SITE_BY_CAMPAIGN"`)




