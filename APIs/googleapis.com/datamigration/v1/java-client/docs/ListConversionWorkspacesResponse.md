

# ListConversionWorkspacesResponse

Response message for 'ListConversionWorkspaces' request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**conversionWorkspaces** | [**List&lt;ConversionWorkspace&gt;**](ConversionWorkspace.md) | The list of conversion workspace objects. |  [optional] |
|**nextPageToken** | **String** | A token which can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations that could not be reached. |  [optional] |



