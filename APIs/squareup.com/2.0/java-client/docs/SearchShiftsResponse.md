

# SearchShiftsResponse

The response to a request for `Shift` objects. The response contains the requested `Shift` objects and might contain a set of `Error` objects if the request resulted in errors.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cursor** | **String** | An opaque cursor for fetching the next page. |  [optional] |
|**errors** | [**List&lt;Error&gt;**](Error.md) | Any errors that occurred during the request. |  [optional] |
|**shifts** | [**List&lt;Shift&gt;**](Shift.md) | Shifts. |  [optional] |



