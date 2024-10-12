# CampaignManager360Api.ReportReachCriteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activities** | [**Activities**](Activities.md) |  | [optional] 
**customRichMediaEvents** | [**CustomRichMediaEvents**](CustomRichMediaEvents.md) |  | [optional] 
**dateRange** | [**DateRange**](DateRange.md) |  | [optional] 
**dimensionFilters** | [**[DimensionValue]**](DimensionValue.md) | The list of filters on which dimensions are filtered. Filters for different dimensions are ANDed, filters for the same dimension are grouped together and ORed. | [optional] 
**dimensions** | [**[SortedDimension]**](SortedDimension.md) | The list of dimensions the report should include. | [optional] 
**enableAllDimensionCombinations** | **Boolean** | Whether to enable all reach dimension combinations in the report. Defaults to false. If enabled, the date range of the report should be within the last 42 days. | [optional] 
**metricNames** | **[String]** | The list of names of metrics the report should include. | [optional] 
**reachByFrequencyMetricNames** | **[String]** | The list of names of Reach By Frequency metrics the report should include. | [optional] 


