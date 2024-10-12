# AzureResourceGraph.QueryRequestOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip** | **Number** | The number of rows to skip from the beginning of the results. Overrides the next page offset when &#x60;&#x60;&#x60;$skipToken&#x60;&#x60;&#x60; property is present. | [optional] 
**skipToken** | **String** | Continuation token for pagination, capturing the next page size and offset, as well as the context of the query. | [optional] 
**top** | **Number** | The maximum number of rows that the query should return. Overrides the page size when &#x60;&#x60;&#x60;$skipToken&#x60;&#x60;&#x60; property is present. | [optional] 
**resultFormat** | **String** | Defines in which format query result returned. | [optional] 



## Enum: ResultFormatEnum


* `table` (value: `"table"`)

* `objectArray` (value: `"objectArray"`)




