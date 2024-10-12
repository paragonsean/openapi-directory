

# ListTcpRoutesResponse

Response returned by the ListTcpRoutes method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | If there might be more results than those appearing in this response, then &#x60;next_page_token&#x60; is included. To get the next set of results, call this method again using the value of &#x60;next_page_token&#x60; as &#x60;page_token&#x60;. |  [optional] |
|**tcpRoutes** | [**List&lt;TcpRoute&gt;**](TcpRoute.md) | List of TcpRoute resources. |  [optional] |



