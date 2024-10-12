

# SearchInsightsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**startTimeRange** | [**ListAnomaliesForInsightRequestStartTimeRange**](ListAnomaliesForInsightRequestStartTimeRange.md) |  |  |
|**filters** | [**SearchInsightsRequestFilters**](SearchInsightsRequestFilters.md) |  |  [optional] |
|**maxResults** | **Integer** | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned &lt;code&gt;nextToken&lt;/code&gt; value. |  [optional] |
|**nextToken** | **String** | The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  The type of insights you are searching for (&lt;code&gt;REACTIVE&lt;/code&gt; or &lt;code&gt;PROACTIVE&lt;/code&gt;).  |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| REACTIVE | &quot;REACTIVE&quot; |
| PROACTIVE | &quot;PROACTIVE&quot; |



