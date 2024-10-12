

# RetrieveCustomerGroupResponse

Defines the fields that are included in the response body of a request to the [RetrieveCustomerGroup](https://developer.squareup.com/reference/square_2021-08-18/customer-groups-api/retrieve-customer-group) endpoint.  Either `errors` or `group` is present in a given response (never both).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errors** | [**List&lt;Error&gt;**](Error.md) | Any errors that occurred during the request. |  [optional] |
|**group** | [**CustomerGroup**](CustomerGroup.md) |  |  [optional] |



