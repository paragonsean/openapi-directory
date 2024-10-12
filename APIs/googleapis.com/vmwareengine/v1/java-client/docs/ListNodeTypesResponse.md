

# ListNodeTypesResponse

Response message for VmwareEngine.ListNodeTypes

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | A token, which can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. |  [optional] |
|**nodeTypes** | [**List&lt;NodeType&gt;**](NodeType.md) | A list of Node Types. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations that could not be reached when making an aggregated query using wildcards. |  [optional] |



