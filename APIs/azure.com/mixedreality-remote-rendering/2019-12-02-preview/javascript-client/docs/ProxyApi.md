# MixedReality.ProxyApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**remoteRenderingAccountsListBySubscription_0**](ProxyApi.md#remoteRenderingAccountsListBySubscription_0) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.MixedReality/remoteRenderingAccounts | 



## remoteRenderingAccountsListBySubscription_0

> RemoteRenderingAccountPage remoteRenderingAccountsListBySubscription_0(subscriptionId, apiVersion)



List Remote Rendering Accounts by Subscription

### Example

```javascript
import MixedReality from 'mixed_reality';
let defaultClient = MixedReality.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MixedReality.ProxyApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.remoteRenderingAccountsListBySubscription_0(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure subscription ID. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 

### Return type

[**RemoteRenderingAccountPage**](RemoteRenderingAccountPage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

