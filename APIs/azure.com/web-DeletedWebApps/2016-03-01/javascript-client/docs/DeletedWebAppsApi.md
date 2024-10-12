# DeletedWebAppsApiClient.DeletedWebAppsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deletedWebAppsList**](DeletedWebAppsApi.md#deletedWebAppsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/deletedSites | Get all deleted apps for a subscription.



## deletedWebAppsList

> DeletedWebAppCollection deletedWebAppsList(subscriptionId, apiVersion)

Get all deleted apps for a subscription.

Get all deleted apps for a subscription.

### Example

```javascript
import DeletedWebAppsApiClient from 'deleted_web_apps_api_client';
let defaultClient = DeletedWebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DeletedWebAppsApiClient.DeletedWebAppsApi();
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.deletedWebAppsList(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**DeletedWebAppCollection**](DeletedWebAppCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

