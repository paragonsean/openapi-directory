

# QueryResponse

Query result.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**$skipToken** | **String** | When present, the value can be passed to a subsequent query call (together with the same query and subscriptions used in the current request) to retrieve the next page of data. |  [optional] |
|**count** | **Long** | Number of records returned in the current response. In the case of paging, this is the number of records in the current page. |  |
|**data** | [**Table**](Table.md) |  |  |
|**facets** | [**List&lt;Facet&gt;**](Facet.md) | Query facets. |  [optional] |
|**resultTruncated** | [**ResultTruncatedEnum**](#ResultTruncatedEnum) | Indicates whether the query results are truncated. |  |
|**totalRecords** | **Long** | Number of total records matching the query. |  |



## Enum: ResultTruncatedEnum

| Name | Value |
|---- | -----|
| TRUE | &quot;true&quot; |
| FALSE | &quot;false&quot; |



