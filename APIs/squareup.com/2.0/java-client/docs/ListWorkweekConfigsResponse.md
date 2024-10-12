

# ListWorkweekConfigsResponse

The response to a request for a set of `WorkweekConfig` objects. The response contains the requested `WorkweekConfig` objects and might contain a set of `Error` objects if the request resulted in errors.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cursor** | **String** | The value supplied in the subsequent request to fetch the next page of &#x60;EmployeeWage&#x60; results. |  [optional] |
|**errors** | [**List&lt;Error&gt;**](Error.md) | Any errors that occurred during the request. |  [optional] |
|**workweekConfigs** | [**List&lt;WorkweekConfig&gt;**](WorkweekConfig.md) | A page of &#x60;EmployeeWage&#x60; results. |  [optional] |



