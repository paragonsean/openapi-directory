

# ListBreakTypesResponse

The response to a request for a set of `BreakType` objects. The response contains the requested `BreakType` objects and might contain a set of `Error` objects if the request resulted in errors.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**breakTypes** | [**List&lt;BreakType&gt;**](BreakType.md) |  A page of &#x60;BreakType&#x60; results. |  [optional] |
|**cursor** | **String** | The value supplied in the subsequent request to fetch the next page of &#x60;BreakType&#x60; results. |  [optional] |
|**errors** | [**List&lt;Error&gt;**](Error.md) | Any errors that occurred during the request. |  [optional] |



