# SquareConnectApi.EmployeesApi

All URIs are relative to *https://connect.squareup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2EmployeesGet**](EmployeesApi.md#v2EmployeesGet) | **GET** /v2/employees | ListEmployees
[**v2EmployeesIdGet**](EmployeesApi.md#v2EmployeesIdGet) | **GET** /v2/employees/{id} | RetrieveEmployee



## v2EmployeesGet

> ListEmployeesResponse v2EmployeesGet(opts)

ListEmployees



### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.EmployeesApi();
let opts = {
  'locationId': "locationId_example", // String | 
  'status': "status_example", // String | Specifies the EmployeeStatus to filter the employee by.
  'limit': 56, // Number | The number of employees to be returned on each page.
  'cursor': "cursor_example" // String | The token required to retrieve the specified page of results.
};
apiInstance.v2EmployeesGet(opts, (error, data, response) => {
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
 **locationId** | **String**|  | [optional] 
 **status** | **String**| Specifies the EmployeeStatus to filter the employee by. | [optional] 
 **limit** | **Number**| The number of employees to be returned on each page. | [optional] 
 **cursor** | **String**| The token required to retrieve the specified page of results. | [optional] 

### Return type

[**ListEmployeesResponse**](ListEmployeesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## v2EmployeesIdGet

> RetrieveEmployeeResponse v2EmployeesIdGet(id)

RetrieveEmployee



### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.EmployeesApi();
let id = "id_example"; // String | UUID for the employee that was requested.
apiInstance.v2EmployeesIdGet(id, (error, data, response) => {
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
 **id** | **String**| UUID for the employee that was requested. | 

### Return type

[**RetrieveEmployeeResponse**](RetrieveEmployeeResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

