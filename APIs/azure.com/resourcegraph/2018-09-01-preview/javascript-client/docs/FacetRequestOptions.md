# AzureResourceGraph.FacetRequestOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**top** | **Number** | The maximum number of facet rows that should be returned. | [optional] 
**filter** | **String** | Specifies the filter condition for the &#39;where&#39; clause which will be run on main query&#39;s result, just before the actual faceting. | [optional] 
**sortBy** | **String** | The column name or query expression to sort on. Defaults to count if not present. | [optional] 
**sortOrder** | **String** | The sorting order by the selected column (count by default). | [optional] [default to &#39;desc&#39;]



## Enum: SortOrderEnum


* `asc` (value: `"asc"`)

* `desc` (value: `"desc"`)




