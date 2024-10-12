# LogicAppsManagementClient.ManagedApisApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**managedApisGet**](ManagedApisApi.md#managedApisGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/locations/{location}/managedApis/{apiName} | Get managed API
[**managedApisList**](ManagedApisApi.md#managedApisList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/locations/{location}/managedApis | List managed Apis



## managedApisGet

> ApiEntity managedApisGet(location, apiName, subscriptionId, apiVersion, opts)

Get managed API

Gets a managed API.

### Example

```javascript
import LogicAppsManagementClient from 'logic_apps_management_client';
let defaultClient = LogicAppsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicAppsManagementClient.ManagedApisApi();
let location = "location_example"; // String | The location.
let apiName = "apiName_example"; // String | The managed API name.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  '_export': true // Boolean | flag showing whether to export API definition in format specified by Accept header.
};
apiInstance.managedApisGet(location, apiName, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **location** | **String**| The location. | 
 **apiName** | **String**| The managed API name. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **_export** | **Boolean**| flag showing whether to export API definition in format specified by Accept header. | [optional] 

### Return type

[**ApiEntity**](ApiEntity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## managedApisList

> ApisCollection managedApisList(location, subscriptionId, apiVersion)

List managed Apis

Gets a list of managed APIs.

### Example

```javascript
import LogicAppsManagementClient from 'logic_apps_management_client';
let defaultClient = LogicAppsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicAppsManagementClient.ManagedApisApi();
let location = "location_example"; // String | The location.
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
 **location** | **String**| The location. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ApisCollection**](ApisCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

