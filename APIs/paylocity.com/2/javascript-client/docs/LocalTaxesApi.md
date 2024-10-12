# PaylocityApi.LocalTaxesApi

All URIs are relative to *https://api.paylocity.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addLocalTax**](LocalTaxesApi.md#addLocalTax) | **POST** /v2/companies/{companyId}/employees/{employeeId}/localTaxes | Add new local tax
[**deleteLocalTaxByTaxCode**](LocalTaxesApi.md#deleteLocalTaxByTaxCode) | **DELETE** /v2/companies/{companyId}/employees/{employeeId}/localTaxes/{taxCode} | Delete local tax by tax code
[**getAllLocalTaxes**](LocalTaxesApi.md#getAllLocalTaxes) | **GET** /v2/companies/{companyId}/employees/{employeeId}/localTaxes | Get all local taxes
[**getLocalTaxByTaxCode**](LocalTaxesApi.md#getLocalTaxByTaxCode) | **GET** /v2/companies/{companyId}/employees/{employeeId}/localTaxes/{taxCode} | Get local taxes by tax code



## addLocalTax

> addLocalTax(companyId, employeeId, localTax)

Add new local tax

Sends new employee local tax information directly to Web Pay.

### Example

```javascript
import PaylocityApi from 'paylocity_api';
let defaultClient = PaylocityApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: paylocity_auth
let paylocity_auth = defaultClient.authentications['paylocity_auth'];
paylocity_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PaylocityApi.LocalTaxesApi();
let companyId = "companyId_example"; // String | Company Id
let employeeId = "employeeId_example"; // String | Employee Id
let localTax = new PaylocityApi.LocalTax(); // LocalTax | LocalTax Model
apiInstance.addLocalTax(companyId, employeeId, localTax, (error, data, response) => {
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
 **localTax** | [**LocalTax**](LocalTax.md)| LocalTax Model | 

### Return type

null (empty response body)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteLocalTaxByTaxCode

> deleteLocalTaxByTaxCode(companyId, employeeId, taxCode)

Delete local tax by tax code

Delete local tax by tax code

### Example

```javascript
import PaylocityApi from 'paylocity_api';
let defaultClient = PaylocityApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: paylocity_auth
let paylocity_auth = defaultClient.authentications['paylocity_auth'];
paylocity_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PaylocityApi.LocalTaxesApi();
let companyId = "companyId_example"; // String | Company Id
let employeeId = "employeeId_example"; // String | Employee Id
let taxCode = "taxCode_example"; // String | Tax Code
apiInstance.deleteLocalTaxByTaxCode(companyId, employeeId, taxCode, (error, data, response) => {
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
 **taxCode** | **String**| Tax Code | 

### Return type

null (empty response body)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllLocalTaxes

> [LocalTax] getAllLocalTaxes(companyId, employeeId)

Get all local taxes

Returns all local taxes for the selected employee.

### Example

```javascript
import PaylocityApi from 'paylocity_api';
let defaultClient = PaylocityApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: paylocity_auth
let paylocity_auth = defaultClient.authentications['paylocity_auth'];
paylocity_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PaylocityApi.LocalTaxesApi();
let companyId = "companyId_example"; // String | Company Id
let employeeId = "employeeId_example"; // String | Employee Id
apiInstance.getAllLocalTaxes(companyId, employeeId, (error, data, response) => {
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

[**[LocalTax]**](LocalTax.md)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLocalTaxByTaxCode

> [LocalTax] getLocalTaxByTaxCode(companyId, employeeId, taxCode)

Get local taxes by tax code

Returns all local taxes with the provided tax code for the selected employee.

### Example

```javascript
import PaylocityApi from 'paylocity_api';
let defaultClient = PaylocityApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: paylocity_auth
let paylocity_auth = defaultClient.authentications['paylocity_auth'];
paylocity_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PaylocityApi.LocalTaxesApi();
let companyId = "companyId_example"; // String | Company Id
let employeeId = "employeeId_example"; // String | Employee Id
let taxCode = "taxCode_example"; // String | Tax Code
apiInstance.getLocalTaxByTaxCode(companyId, employeeId, taxCode, (error, data, response) => {
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
 **taxCode** | **String**| Tax Code | 

### Return type

[**[LocalTax]**](LocalTax.md)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

