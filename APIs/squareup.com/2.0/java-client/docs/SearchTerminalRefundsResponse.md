

# SearchTerminalRefundsResponse



## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cursor** | **String** | The pagination cursor to be used in a subsequent request. If empty, this is the final response.  See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information. |  [optional] |
|**errors** | [**List&lt;Error&gt;**](Error.md) | Information about errors encountered during the request. |  [optional] |
|**refunds** | [**List&lt;TerminalRefund&gt;**](TerminalRefund.md) | The requested search result of &#x60;TerminalRefund&#x60; objects. |  [optional] |



