# MonitorManagementClient.DiagnosticSettingsCategoriesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**diagnosticSettingsCategoryGet**](DiagnosticSettingsCategoriesApi.md#diagnosticSettingsCategoryGet) | **GET** /{resourceUri}/providers/microsoft.insights/diagnosticSettingsCategories/{name} | 
[**diagnosticSettingsCategoryList**](DiagnosticSettingsCategoriesApi.md#diagnosticSettingsCategoryList) | **GET** /{resourceUri}/providers/microsoft.insights/diagnosticSettingsCategories | 



## diagnosticSettingsCategoryGet

> DiagnosticSettingsCategoryResource diagnosticSettingsCategoryGet(resourceUri, apiVersion, name)



Gets the diagnostic settings category for the specified resource.

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.DiagnosticSettingsCategoriesApi();
let resourceUri = "resourceUri_example"; // String | The identifier of the resource.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let name = "name_example"; // String | The name of the diagnostic setting.
apiInstance.diagnosticSettingsCategoryGet(resourceUri, apiVersion, name, (error, data, response) => {
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
 **resourceUri** | **String**| The identifier of the resource. | 
 **apiVersion** | **String**| Client Api Version. | 
 **name** | **String**| The name of the diagnostic setting. | 

### Return type

[**DiagnosticSettingsCategoryResource**](DiagnosticSettingsCategoryResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## diagnosticSettingsCategoryList

> DiagnosticSettingsCategoryResourceCollection diagnosticSettingsCategoryList(resourceUri, apiVersion)



Lists the diagnostic settings categories for the specified resource.

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.DiagnosticSettingsCategoriesApi();
let resourceUri = "resourceUri_example"; // String | The identifier of the resource.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.diagnosticSettingsCategoryList(resourceUri, apiVersion, (error, data, response) => {
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
 **resourceUri** | **String**| The identifier of the resource. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**DiagnosticSettingsCategoryResourceCollection**](DiagnosticSettingsCategoryResourceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

