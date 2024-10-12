

# ReportCriteria

The report criteria for a report of type \"STANDARD\".

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activities** | [**Activities**](Activities.md) |  |  [optional] |
|**customRichMediaEvents** | [**CustomRichMediaEvents**](CustomRichMediaEvents.md) |  |  [optional] |
|**dateRange** | [**DateRange**](DateRange.md) |  |  [optional] |
|**dimensionFilters** | [**List&lt;DimensionValue&gt;**](DimensionValue.md) | The list of filters on which dimensions are filtered. Filters for different dimensions are ANDed, filters for the same dimension are grouped together and ORed. |  [optional] |
|**dimensions** | [**List&lt;SortedDimension&gt;**](SortedDimension.md) | The list of standard dimensions the report should include. |  [optional] |
|**metricNames** | **List&lt;String&gt;** | The list of names of metrics the report should include. |  [optional] |



