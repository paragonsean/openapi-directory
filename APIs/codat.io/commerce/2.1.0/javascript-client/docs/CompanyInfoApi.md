# CommerceApi.CompanyInfoApi

All URIs are relative to *https://api.codat.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCompanyInfo**](CompanyInfoApi.md#getCompanyInfo) | **GET** /companies/{companyId}/connections/{connectionId}/data/commerce-info | Get company info



## getCompanyInfo

> CompanyInfo getCompanyInfo(companyId, connectionId)

Get company info

Retrieve information about the company, as seen in the commerce platform.  This may include information like addresses, tax registration details and social media or website information.

### Example

```javascript
import CommerceApi from 'commerce_api';
let defaultClient = CommerceApi.ApiClient.instance;
// Configure API key authorization: auth_header
let auth_header = defaultClient.authentications['auth_header'];
auth_header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//auth_header.apiKeyPrefix = 'Token';

let apiInstance = new CommerceApi.CompanyInfoApi();
let companyId = "8a210b68-6988-11ed-a1eb-0242ac120002"; // String | 
let connectionId = "2e9d2c44-f675-40ba-8049-353bfcb5e171"; // String | 
apiInstance.getCompanyInfo(companyId, connectionId, (error, data, response) => {
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
 **connectionId** | **String**|  | 

### Return type

[**CompanyInfo**](CompanyInfo.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

