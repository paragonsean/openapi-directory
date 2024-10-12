# ConnectorApi.ConnectorResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customFieldsSupported** | **Boolean** | Indicates if custom fields are supported on this resource. | [optional] 
**downstreamId** | **String** | ID of the resource in the Connector&#39;s API (downstream) | [optional] 
**downstreamName** | **String** | Name of the resource in the Connector&#39;s API (downstream) | [optional] 
**downstreamUnsupportedOperations** | **[String]** | List of operations that are not supported on the downstream. | [optional] 
**id** | **String** | ID of the resource, typically a lowercased version of name. | [optional] 
**name** | **String** | Name of the resource (plural) | [optional] 
**pagination** | [**PaginationCoverage**](PaginationCoverage.md) |  | [optional] 
**paginationSupported** | **Boolean** | Indicates if pagination (cursor and limit parameters) is supported on the list endpoint of the resource. | [optional] 
**status** | [**ResourceStatus**](ResourceStatus.md) |  | [optional] 
**supportedFields** | [**[SupportedProperty]**](SupportedProperty.md) | Supported fields on the detail endpoint. | [optional] 
**supportedFilters** | **[String]** | Supported filters on the list endpoint of the resource. | [optional] 
**supportedListFields** | [**[SupportedProperty]**](SupportedProperty.md) | Supported fields on the list endpoint. | [optional] 
**supportedOperations** | **[String]** | List of supported operations on the resource. | [optional] 
**supportedSortBy** | **[String]** | Supported sorting properties on the list endpoint of the resource. | [optional] 


