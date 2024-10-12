

# ApiResourceCoverageCoverageInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**downstreamId** | **String** | ID of the resource in the Connector&#39;s API (downstream) |  [optional] |
|**downstreamName** | **String** | Name of the resource in the Connector&#39;s API (downstream) |  [optional] |
|**pagination** | [**PaginationCoverage**](PaginationCoverage.md) |  |  [optional] |
|**paginationSupported** | **Boolean** | Indicates if pagination (cursor and limit parameters) is supported on the list endpoint of the resource. |  [optional] |
|**supportedFields** | [**List&lt;SupportedProperty&gt;**](SupportedProperty.md) | Supported fields on the detail endpoint. |  [optional] |
|**supportedFilters** | **List&lt;String&gt;** | Supported filters on the list endpoint of the resource. |  [optional] |
|**supportedListFields** | [**List&lt;SupportedProperty&gt;**](SupportedProperty.md) | Supported fields on the list endpoint. |  [optional] |
|**supportedOperations** | **List&lt;String&gt;** | List of supported operations on the resource. |  [optional] |
|**supportedSortBy** | **List&lt;String&gt;** | Supported sorting properties on the list endpoint of the resource. |  [optional] |



