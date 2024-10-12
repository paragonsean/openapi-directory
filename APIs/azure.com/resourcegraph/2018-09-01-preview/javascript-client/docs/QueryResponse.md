# AzureResourceGraph.QueryResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skipToken** | **String** | When present, the value can be passed to a subsequent query call (together with the same query and subscriptions used in the current request) to retrieve the next page of data. | [optional] 
**count** | **Number** | Number of records returned in the current response. In the case of paging, this is the number of records in the current page. | 
**data** | [**Table**](Table.md) |  | 
**facets** | [**[Facet]**](Facet.md) | Query facets. | [optional] 
**resultTruncated** | **String** | Indicates whether the query results are truncated. | 
**totalRecords** | **Number** | Number of total records matching the query. | 



## Enum: ResultTruncatedEnum


* `true` (value: `"true"`)

* `false` (value: `"false"`)




