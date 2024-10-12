

# SuggestedTagAndRegionQueryToken

Contains properties we need to fetch suggested tags for. For the first call, Session and continuation set to null.  Then on subsequent calls, uses the session/continuation from the previous SuggestedTagAndRegionQuery result to fetch additional results.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**continuation** | **String** | Continuation Id for database pagination. Initially null but later used to paginate. |  [optional] |
|**maxCount** | **Integer** | Maximum number of results you want to be returned in the response. |  [optional] |
|**session** | **String** | SessionId for database query. Initially set to null but later used to paginate. |  [optional] |
|**sortBy** | [**SortByEnum**](#SortByEnum) | OrderBy. Ordering mechanism for your results. |  [optional] |
|**tagIds** | **List&lt;UUID&gt;** | Existing TagIds in project to filter suggested tags on. |  [optional] |
|**threshold** | **Double** | Confidence threshold to filter suggested tags on. |  [optional] |



## Enum: SortByEnum

| Name | Value |
|---- | -----|
| UNCERTAINTY_ASCENDING | &quot;UncertaintyAscending&quot; |
| UNCERTAINTY_DESCENDING | &quot;UncertaintyDescending&quot; |



