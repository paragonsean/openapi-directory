# PaylocityApi.SensitiveDataApi

All URIs are relative to *https://api.paylocity.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addOrUpdateSensitiveData**](SensitiveDataApi.md#addOrUpdateSensitiveData) | **PUT** /v2/companies/{companyId}/employees/{employeeId}/sensitivedata | Add/update sensitive data
[**getSensitiveData**](SensitiveDataApi.md#getSensitiveData) | **GET** /v2/companies/{companyId}/employees/{employeeId}/sensitivedata | Get sensitive data



## addOrUpdateSensitiveData

> addOrUpdateSensitiveData(companyId, employeeId, sensitiveData)

Add/update sensitive data

Sends new or updated employee sensitive data information directly to Web Pay.

### Example

```javascript
import PaylocityApi from 'paylocity_api';
let defaultClient = PaylocityApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: paylocity_auth
let paylocity_auth = defaultClient.authentications['paylocity_auth'];
paylocity_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PaylocityApi.SensitiveDataApi();
let companyId = "companyId_example"; // String | Company Id
let employeeId = "employeeId_example"; // String | Employee Id
let sensitiveData = new PaylocityApi.SensitiveData(); // SensitiveData | Sensitive Data Model
apiInstance.addOrUpdateSensitiveData(companyId, employeeId, sensitiveData, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **companyId** | **String**| Company Id | 
 **employeeId** | **String**| Employee Id | 
 **sensitiveData** | [**SensitiveData**](SensitiveData.md)| Sensitive Data Model | 

### Return type

null (empty response body)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getSensitiveData

> [SensitiveData] getSensitiveData(companyId, employeeId)

Get sensitive data

Gets employee sensitive data information directly from Web Pay.

### Example

```javascript
import PaylocityApi from 'paylocity_api';
let defaultClient = PaylocityApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: paylocity_auth
let paylocity_auth = defaultClient.authentications['paylocity_auth'];
paylocity_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PaylocityApi.SensitiveDataApi();
let companyId = "companyId_example"; // String | Company Id
let employeeId = "employeeId_example"; // String | Employee Id
apiInstance.getSensitiveData(companyId, employeeId, (error, data, response) => {
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
 **companyId** | **String**| Company Id | 
 **employeeId** | **String**| Employee Id | 

### Return type

[**[SensitiveData]**](SensitiveData.md)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

