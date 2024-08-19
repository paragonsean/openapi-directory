

# CreateCustomerCardResponse

Defines the fields that are included in the response body of a request to the `CreateCustomerCard` endpoint.  Either `errors` or `card` is present in a given response (never both).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**card** | [**Card**](Card.md) |  |  [optional] |
|**errors** | [**List&lt;Error&gt;**](Error.md) | Any errors that occurred during the request. |  [optional] |



