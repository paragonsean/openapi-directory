# Azureactivedirectory.DiagnosticSettingsCategoriesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**diagnosticSettingsCategoryList**](DiagnosticSettingsCategoriesApi.md#diagnosticSettingsCategoryList) | **GET** /providers/microsoft.aadiam/diagnosticSettingsCategories | 



## diagnosticSettingsCategoryList

> DiagnosticSettingsCategoryResourceCollection diagnosticSettingsCategoryList(apiVersion)



Lists the diagnostic settings categories for AadIam.

### Example

```javascript
import Azureactivedirectory from 'azureactivedirectory';
let defaultClient = Azureactivedirectory.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Azureactivedirectory.DiagnosticSettingsCategoriesApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.diagnosticSettingsCategoryList(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**DiagnosticSettingsCategoryResourceCollection**](DiagnosticSettingsCategoryResourceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

