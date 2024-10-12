# CodatExpenseApi.MappingOptionsApi

All URIs are relative to *https://api.codat.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getMappingOptions**](MappingOptionsApi.md#getMappingOptions) | **GET** /companies/{companyId}/sync/expenses/mappingOptions | Mapping options



## getMappingOptions

> MappingOptions getMappingOptions(companyId)

Mapping options

Gets the expense mapping options for a companies accounting software

### Example

```javascript
import CodatExpenseApi from 'codat_expense_api';
let defaultClient = CodatExpenseApi.ApiClient.instance;
// Configure API key authorization: auth_header
let auth_header = defaultClient.authentications['auth_header'];
auth_header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//auth_header.apiKeyPrefix = 'Token';

let apiInstance = new CodatExpenseApi.MappingOptionsApi();
let companyId = "8a210b68-6988-11ed-a1eb-0242ac120002"; // String | 
apiInstance.getMappingOptions(companyId, (error, data, response) => {
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

[**MappingOptions**](MappingOptions.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

