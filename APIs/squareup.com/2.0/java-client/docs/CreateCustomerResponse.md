

# CreateCustomerResponse

Defines the fields that are included in the response body of a request to the `CreateCustomer` endpoint.  Either `errors` or `customer` is present in a given response (never both).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customer** | [**Customer**](Customer.md) |  |  [optional] |
|**errors** | [**List&lt;Error&gt;**](Error.md) | Any errors that occurred during the request. |  [optional] |



