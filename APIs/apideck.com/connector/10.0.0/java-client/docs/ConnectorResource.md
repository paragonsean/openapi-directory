

# ConnectorResource


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customFieldsSupported** | **Boolean** | Indicates if custom fields are supported on this resource. |  [optional] |
|**downstreamId** | **String** | ID of the resource in the Connector&#39;s API (downstream) |  [optional] |
|**downstreamName** | **String** | Name of the resource in the Connector&#39;s API (downstream) |  [optional] |
|**downstreamUnsupportedOperations** | **List&lt;String&gt;** | List of operations that are not supported on the downstream. |  [optional] |
|**id** | **String** | ID of the resource, typically a lowercased version of name. |  [optional] |
|**name** | **String** | Name of the resource (plural) |  [optional] |
|**pagination** | [**PaginationCoverage**](PaginationCoverage.md) |  |  [optional] |
|**paginationSupported** | **Boolean** | Indicates if pagination (cursor and limit parameters) is supported on the list endpoint of the resource. |  [optional] |
|**status** | **ResourceStatus** |  |  [optional] |
|**supportedFields** | [**List&lt;SupportedProperty&gt;**](SupportedProperty.md) | Supported fields on the detail endpoint. |  [optional] |
|**supportedFilters** | **List&lt;String&gt;** | Supported filters on the list endpoint of the resource. |  [optional] |
|**supportedListFields** | [**List&lt;SupportedProperty&gt;**](SupportedProperty.md) | Supported fields on the list endpoint. |  [optional] |
|**supportedOperations** | **List&lt;String&gt;** | List of supported operations on the resource. |  [optional] |
|**supportedSortBy** | **List&lt;String&gt;** | Supported sorting properties on the list endpoint of the resource. |  [optional] |



