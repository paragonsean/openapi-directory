# CodatExpenseApi.ConfigurationApi

All URIs are relative to *https://api.codat.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCompanyConfiguration**](ConfigurationApi.md#getCompanyConfiguration) | **GET** /companies/{companyId}/sync/expenses/config | Get company configuration
[**saveCompanyConfiguration**](ConfigurationApi.md#saveCompanyConfiguration) | **POST** /companies/{companyId}/sync/expenses/config | Set company configuration



## getCompanyConfiguration

> CompanyConfiguration getCompanyConfiguration(companyId)

Get company configuration

Gets a companies expense sync configuration

### Example

```javascript
import CodatExpenseApi from 'codat_expense_api';
let defaultClient = CodatExpenseApi.ApiClient.instance;
// Configure API key authorization: auth_header
let auth_header = defaultClient.authentications['auth_header'];
auth_header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//auth_header.apiKeyPrefix = 'Token';

let apiInstance = new CodatExpenseApi.ConfigurationApi();
let companyId = "8a210b68-6988-11ed-a1eb-0242ac120002"; // String | 
apiInstance.getCompanyConfiguration(companyId, (error, data, response) => {
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
 **companyId** | **String**|  | 

### Return type

[**CompanyConfiguration**](CompanyConfiguration.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## saveCompanyConfiguration

> CompanyConfiguration saveCompanyConfiguration(companyId, opts)

Set company configuration

Sets a companies expense sync configuration

### Example

```javascript
import CodatExpenseApi from 'codat_expense_api';
let defaultClient = CodatExpenseApi.ApiClient.instance;
// Configure API key authorization: auth_header
let auth_header = defaultClient.authentications['auth_header'];
auth_header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//auth_header.apiKeyPrefix = 'Token';

let apiInstance = new CodatExpenseApi.ConfigurationApi();
let companyId = "8a210b68-6988-11ed-a1eb-0242ac120002"; // String | 
let opts = {
  'companyConfiguration': new CodatExpenseApi.CompanyConfiguration() // CompanyConfiguration | 
};
apiInstance.saveCompanyConfiguration(companyId, opts, (error, data, response) => {
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
 **companyId** | **String**|  | 
 **companyConfiguration** | [**CompanyConfiguration**](CompanyConfiguration.md)|  | [optional] 

### Return type

[**CompanyConfiguration**](CompanyConfiguration.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

