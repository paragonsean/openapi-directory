

# FacetRequestOptions

The options for facet evaluation

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**$top** | **Integer** | The maximum number of facet rows that should be returned. |  [optional] |
|**filter** | **String** | Specifies the filter condition for the &#39;where&#39; clause which will be run on main query&#39;s result, just before the actual faceting. |  [optional] |
|**sortBy** | **String** | The column name or query expression to sort on. Defaults to count if not present. |  [optional] |
|**sortOrder** | [**SortOrderEnum**](#SortOrderEnum) | The sorting order by the selected column (count by default). |  [optional] |



## Enum: SortOrderEnum

| Name | Value |
|---- | -----|
| ASC | &quot;asc&quot; |
| DESC | &quot;desc&quot; |



