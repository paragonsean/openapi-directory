

# ListEmployeeWagesResponse

The response to a request for a set of `EmployeeWage` objects. The response contains a set of `EmployeeWage` objects.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cursor** | **String** | The value supplied in the subsequent request to fetch the next page of &#x60;EmployeeWage&#x60; results. |  [optional] |
|**employeeWages** | [**List&lt;EmployeeWage&gt;**](EmployeeWage.md) | A page of &#x60;EmployeeWage&#x60; results. |  [optional] |
|**errors** | [**List&lt;Error&gt;**](Error.md) | Any errors that occurred during the request. |  [optional] |



