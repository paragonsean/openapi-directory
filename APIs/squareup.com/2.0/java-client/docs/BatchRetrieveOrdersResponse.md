

# BatchRetrieveOrdersResponse

Defines the fields that are included in the response body of a request to the `BatchRetrieveOrders` endpoint.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errors** | [**List&lt;Error&gt;**](Error.md) | Any errors that occurred during the request. |  [optional] |
|**orders** | [**List&lt;Order&gt;**](Order.md) | The requested orders. This will omit any requested orders that do not exist. |  [optional] |



