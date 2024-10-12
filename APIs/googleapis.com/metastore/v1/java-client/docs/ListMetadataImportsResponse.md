

# ListMetadataImportsResponse

Response message for DataprocMetastore.ListMetadataImports.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metadataImports** | [**List&lt;MetadataImport&gt;**](MetadataImport.md) | The imports in the specified service. |  [optional] |
|**nextPageToken** | **String** | A token that can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations that could not be reached. |  [optional] |



