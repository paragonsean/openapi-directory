# LogicAppsManagementClient.ManagedAPIsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**managedApisGet**](ManagedAPIsApi.md#managedApisGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/locations/{location}/managedApis/{apiName} | Gets managed API
[**managedApisList**](ManagedAPIsApi.md#managedApisList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/locations/{location}/managedApis | Lists managed APIs



## managedApisGet

> ManagedApiDefinition managedApisGet(subscriptionId, location, apiName, apiVersion)

Gets managed API

Gets a managed API

### Example

```javascript
import LogicAppsManagementClient from 'logic_apps_management_client';
let defaultClient = LogicAppsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicAppsManagementClient.ManagedAPIsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let location = "location_example"; // String | The location
let apiName = "apiName_example"; // String | API name
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.managedApisGet(subscriptionId, location, apiName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id | 
 **location** | **String**| The location | 
 **apiName** | **String**| API name | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ManagedApiDefinition**](ManagedApiDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## managedApisList

> ManagedApiDefinitionCollection managedApisList(location, subscriptionId, apiVersion)

Lists managed APIs

Gets a list of managed APIs

### Example

```javascript
import LogicAppsManagementClient from 'logic_apps_management_client';
let defaultClient = LogicAppsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicAppsManagementClient.ManagedAPIsApi();
let location = "location_example"; // String | The location
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.managedApisList(location, subscriptionId, apiVersion, (error, data, response) => {
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
 **location** | **String**| The location | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ManagedApiDefinitionCollection**](ManagedApiDefinitionCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

