

# ListPrivateConnectionsResponse

Response message for VmwareEngine.ListPrivateConnections

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | A token, which can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. |  [optional] |
|**privateConnections** | [**List&lt;PrivateConnection&gt;**](PrivateConnection.md) | A list of private connections. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Unreachable resources. |  [optional] |



