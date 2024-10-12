# AmazonMacie2.GetUsageStatisticsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filterBy** | [**[UsageStatisticsFilter]**](UsageStatisticsFilter.md) | An array of objects, one for each condition to use to filter the query results. If you specify more than one condition, Amazon Macie uses an AND operator to join the conditions. | [optional] 
**maxResults** | **Number** | The maximum number of items to include in each page of the response. | [optional] 
**nextToken** | **String** | The nextToken string that specifies which page of results to return in a paginated response. | [optional] 
**sortBy** | [**GetUsageStatisticsRequestSortBy**](GetUsageStatisticsRequestSortBy.md) |  | [optional] 
**timeRange** | **String** | An inclusive time period that Amazon Macie usage data applies to. Possible values are: | [optional] 



## Enum: TimeRangeEnum


* `MONTH_TO_DATE` (value: `"MONTH_TO_DATE"`)

* `PAST_30_DAYS` (value: `"PAST_30_DAYS"`)




