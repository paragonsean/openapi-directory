

# ReportFloodlightCriteria

The report criteria for a report of type \"FLOODLIGHT\".

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customRichMediaEvents** | [**List&lt;DimensionValue&gt;**](DimensionValue.md) | The list of custom rich media events to include. |  [optional] |
|**dateRange** | [**DateRange**](DateRange.md) |  |  [optional] |
|**dimensionFilters** | [**List&lt;DimensionValue&gt;**](DimensionValue.md) | The list of filters on which dimensions are filtered. Filters for different dimensions are ANDed, filters for the same dimension are grouped together and ORed. |  [optional] |
|**dimensions** | [**List&lt;SortedDimension&gt;**](SortedDimension.md) | The list of dimensions the report should include. |  [optional] |
|**floodlightConfigId** | [**DimensionValue**](DimensionValue.md) |  |  [optional] |
|**metricNames** | **List&lt;String&gt;** | The list of names of metrics the report should include. |  [optional] |
|**reportProperties** | [**ReportFloodlightCriteriaReportProperties**](ReportFloodlightCriteriaReportProperties.md) |  |  [optional] |



