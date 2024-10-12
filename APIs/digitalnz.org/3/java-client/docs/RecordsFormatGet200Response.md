

# RecordsFormatGet200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**facets** | **Map&lt;String, Map&lt;String, Integer&gt;&gt;** | Each field you request from the list of facetable fields will be returned as separate elements. Each of those will contain a sorted list of elements that are made up of a value (eg collection name, subject, date) and the number of results associated with that value.    |  [optional] |
|**page** | **Integer** | Current page. |  [optional] |
|**perPage** | **Integer** | Requested amount of records shown per page of results. |  [optional] |
|**records** | [**List&lt;Record&gt;**](Record.md) |  |  [optional] |
|**requestUrl** | **String** | The URL of current page of results. |  [optional] |
|**resultCount** | **Integer** | Total number of matching search results. |  [optional] |



