

# ListSlotTypesRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**sortBy** | [**ListSlotTypesRequestSortBy**](ListSlotTypesRequestSortBy.md) |  |  [optional] |
|**filters** | [**List&lt;SlotTypeFilter&gt;**](SlotTypeFilter.md) | Provides the specification of a filter used to limit the slot types in the response to only those that match the filter specification. You can only specify one filter and only one string to filter on. |  [optional] |
|**maxResults** | **Integer** | The maximum number of slot types to return in each page of results. If there are fewer results than the max page size, only the actual number of results are returned. |  [optional] |
|**nextToken** | **String** | If the response from the &lt;code&gt;ListSlotTypes&lt;/code&gt; operation contains more results than specified in the &lt;code&gt;maxResults&lt;/code&gt; parameter, a token is returned in the response. Use that token in the &lt;code&gt;nextToken&lt;/code&gt; parameter to return the next page of results. |  [optional] |



