

# RetrieveCustomerSegmentResponse

Defines the fields that are included in the response body for requests to the `RetrieveCustomerSegment` endpoint.  Either `errors` or `segment` is present in a given response (never both).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errors** | [**List&lt;Error&gt;**](Error.md) | Any errors that occurred during the request. |  [optional] |
|**segment** | [**CustomerSegment**](CustomerSegment.md) |  |  [optional] |



