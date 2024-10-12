# ConnectorApi.PaginationCoverage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limitSupport** | **Boolean** | Indicates whether the connector supports changing the page size by using the limit parameter. | [optional] 
**mode** | **String** | How pagination is implemented on this connector. Native mode means Apideck is using the pagination parameters of the connector. With virtual pagination, the connector does not support pagination, but Apideck emulates it. | [optional] 
**pagingSupport** | **Boolean** | Indicates whether the connector supports paging through results using the cursor parameter. | [optional] 



## Enum: ModeEnum


* `native` (value: `"native"`)

* `virtual` (value: `"virtual"`)




