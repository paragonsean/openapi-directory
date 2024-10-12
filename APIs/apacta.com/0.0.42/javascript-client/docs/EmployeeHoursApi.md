# Apacta.EmployeeHoursApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**employeeHoursGet**](EmployeeHoursApi.md#employeeHoursGet) | **GET** /employee_hours | Used to retrieve details about the logged in user&#39;s hours



## employeeHoursGet

> EmployeeHoursGet200Response employeeHoursGet(dateFrom, dateTo)

Used to retrieve details about the logged in user&#39;s hours

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.EmployeeHoursApi();
let dateFrom = "dateFrom_example"; // String | Date formatted as Y-m-d (2016-06-28)
let dateTo = "dateTo_example"; // String | Date formatted as Y-m-d (2016-06-28)
apiInstance.employeeHoursGet(dateFrom, dateTo, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dateFrom** | **String**| Date formatted as Y-m-d (2016-06-28) | 
 **dateTo** | **String**| Date formatted as Y-m-d (2016-06-28) | 

### Return type

[**EmployeeHoursGet200Response**](EmployeeHoursGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

