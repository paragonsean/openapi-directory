# MixedReality.KeyApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**remoteRenderingAccountsGetKeys**](KeyApi.md#remoteRenderingAccountsGetKeys) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MixedReality/remoteRenderingAccounts/{accountName}/keys | 
[**remoteRenderingAccountsRegenerateKeys**](KeyApi.md#remoteRenderingAccountsRegenerateKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MixedReality/remoteRenderingAccounts/{accountName}/keys | 



## remoteRenderingAccountsGetKeys

> RemoteRenderingAccountsGetKeys200Response remoteRenderingAccountsGetKeys(subscriptionId, resourceGroupName, accountName, apiVersion)



Get Both of the 2 Keys of a Remote Rendering Account

### Example

```javascript
import MixedReality from 'mixed_reality';
let defaultClient = MixedReality.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MixedReality.KeyApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Name of an Mixed Reality Account.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.remoteRenderingAccountsGetKeys(subscriptionId, resourceGroupName, accountName, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Name of an Mixed Reality Account. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 

### Return type

[**RemoteRenderingAccountsGetKeys200Response**](RemoteRenderingAccountsGetKeys200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## remoteRenderingAccountsRegenerateKeys

> RemoteRenderingAccountsGetKeys200Response remoteRenderingAccountsRegenerateKeys(subscriptionId, resourceGroupName, accountName, apiVersion, regenerate)



Regenerate specified Key of a Remote Rendering Account

### Example

```javascript
import MixedReality from 'mixed_reality';
let defaultClient = MixedReality.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MixedReality.KeyApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Name of an Mixed Reality Account.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let regenerate = new MixedReality.RemoteRenderingAccountsRegenerateKeysRequest(); // RemoteRenderingAccountsRegenerateKeysRequest | Required information for key regeneration.
apiInstance.remoteRenderingAccountsRegenerateKeys(subscriptionId, resourceGroupName, accountName, apiVersion, regenerate, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **accountName** | **String**| Name of an Mixed Reality Account. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **regenerate** | [**RemoteRenderingAccountsRegenerateKeysRequest**](RemoteRenderingAccountsRegenerateKeysRequest.md)| Required information for key regeneration. | 

### Return type

[**RemoteRenderingAccountsGetKeys200Response**](RemoteRenderingAccountsGetKeys200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

