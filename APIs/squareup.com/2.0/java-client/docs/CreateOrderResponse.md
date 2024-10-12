

# CreateOrderResponse

Defines the fields that are included in the response body of a request to the `CreateOrder` endpoint.  Either `errors` or `order` is present in a given response, but never both.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errors** | [**List&lt;Error&gt;**](Error.md) | Any errors that occurred during the request. |  [optional] |
|**order** | [**Order**](Order.md) |  |  [optional] |



