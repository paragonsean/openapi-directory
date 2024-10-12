

# RegisterDomainResponse

Defines the fields that are included in the response body of a request to the [RegisterDomain](https://developer.squareup.com/reference/square_2021-08-18/apple-pay-api/register-domain) endpoint.  Either `errors` or `status` are present in a given response (never both).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errors** | [**List&lt;Error&gt;**](Error.md) | Any errors that occurred during the request. |  [optional] |
|**status** | **String** | The status of the domain registration.  See [RegisterDomainResponseStatus](https://developer.squareup.com/reference/square_2021-08-18/enums/RegisterDomainResponseStatus) for possible values. |  [optional] |



