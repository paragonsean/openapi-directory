# AmazonDevOpsGuru.SearchOrganizationInsightsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountIds** | **[String]** | The ID of the Amazon Web Services account.  | 
**startTimeRange** | [**ListAnomaliesForInsightRequestStartTimeRange**](ListAnomaliesForInsightRequestStartTimeRange.md) |  | 
**filters** | [**SearchOrganizationInsightsRequestFilters**](SearchOrganizationInsightsRequestFilters.md) |  | [optional] 
**maxResults** | **Number** | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned &lt;code&gt;nextToken&lt;/code&gt; value. | [optional] 
**nextToken** | **String** | The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page. | [optional] 
**type** | **String** |  The type of insights you are searching for (&lt;code&gt;REACTIVE&lt;/code&gt; or &lt;code&gt;PROACTIVE&lt;/code&gt;).  | 



## Enum: TypeEnum


* `REACTIVE` (value: `"REACTIVE"`)

* `PROACTIVE` (value: `"PROACTIVE"`)




