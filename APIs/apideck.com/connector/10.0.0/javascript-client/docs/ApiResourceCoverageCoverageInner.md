# ConnectorApi.ApiResourceCoverageCoverageInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**downstreamId** | **String** | ID of the resource in the Connector&#39;s API (downstream) | [optional] 
**downstreamName** | **String** | Name of the resource in the Connector&#39;s API (downstream) | [optional] 
**pagination** | [**PaginationCoverage**](PaginationCoverage.md) |  | [optional] 
**paginationSupported** | **Boolean** | Indicates if pagination (cursor and limit parameters) is supported on the list endpoint of the resource. | [optional] 
**supportedFields** | [**[SupportedProperty]**](SupportedProperty.md) | Supported fields on the detail endpoint. | [optional] 
**supportedFilters** | **[String]** | Supported filters on the list endpoint of the resource. | [optional] 
**supportedListFields** | [**[SupportedProperty]**](SupportedProperty.md) | Supported fields on the list endpoint. | [optional] 
**supportedOperations** | **[String]** | List of supported operations on the resource. | [optional] 
**supportedSortBy** | **[String]** | Supported sorting properties on the list endpoint of the resource. | [optional] 


