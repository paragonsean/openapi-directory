# PaylocityApi.CustomFieldsApi

All URIs are relative to *https://api.paylocity.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAllCustomFieldsByCategory**](CustomFieldsApi.md#getAllCustomFieldsByCategory) | **GET** /v2/companies/{companyId}/customfields/{category} | Get All Custom Fields



## getAllCustomFieldsByCategory

> [CustomFieldDefinition] getAllCustomFieldsByCategory(companyId, category)

Get All Custom Fields

Get All Custom Fields for the selected company

### Example

```javascript
import PaylocityApi from 'paylocity_api';
let defaultClient = PaylocityApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: paylocity_auth
let paylocity_auth = defaultClient.authentications['paylocity_auth'];
paylocity_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PaylocityApi.CustomFieldsApi();
let companyId = "companyId_example"; // String | Company Id
let category = "category_example"; // String | Custom Fields Category
apiInstance.getAllCustomFieldsByCategory(companyId, category, (error, data, response) => {
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
 **category** | **String**| Custom Fields Category | 

### Return type

[**[CustomFieldDefinition]**](CustomFieldDefinition.md)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

