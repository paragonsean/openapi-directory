# MixedReality.ResourceApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**remoteRenderingAccountsCreate**](ResourceApi.md#remoteRenderingAccountsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MixedReality/remoteRenderingAccounts/{accountName} | 
[**remoteRenderingAccountsDelete**](ResourceApi.md#remoteRenderingAccountsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MixedReality/remoteRenderingAccounts/{accountName} | 
[**remoteRenderingAccountsGet**](ResourceApi.md#remoteRenderingAccountsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MixedReality/remoteRenderingAccounts/{accountName} | 
[**remoteRenderingAccountsListByResourceGroup**](ResourceApi.md#remoteRenderingAccountsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MixedReality/remoteRenderingAccounts | 
[**remoteRenderingAccountsListBySubscription**](ResourceApi.md#remoteRenderingAccountsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.MixedReality/remoteRenderingAccounts | 
[**remoteRenderingAccountsUpdate**](ResourceApi.md#remoteRenderingAccountsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MixedReality/remoteRenderingAccounts/{accountName} | 



## remoteRenderingAccountsCreate

> RemoteRenderingAccount remoteRenderingAccountsCreate(subscriptionId, resourceGroupName, accountName, apiVersion, remoteRenderingAccount)



Creating or Updating a Remote Rendering Account.

### Example

```javascript
import MixedReality from 'mixed_reality';
let defaultClient = MixedReality.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MixedReality.ResourceApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Name of an Mixed Reality Account.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let remoteRenderingAccount = new MixedReality.RemoteRenderingAccount(); // RemoteRenderingAccount | Remote Rendering Account parameter.
apiInstance.remoteRenderingAccountsCreate(subscriptionId, resourceGroupName, accountName, apiVersion, remoteRenderingAccount, (error, data, response) => {
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
 **remoteRenderingAccount** | [**RemoteRenderingAccount**](RemoteRenderingAccount.md)| Remote Rendering Account parameter. | 

### Return type

[**RemoteRenderingAccount**](RemoteRenderingAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## remoteRenderingAccountsDelete

> remoteRenderingAccountsDelete(subscriptionId, resourceGroupName, accountName, apiVersion)



Delete a Remote Rendering Account.

### Example

```javascript
import MixedReality from 'mixed_reality';
let defaultClient = MixedReality.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MixedReality.ResourceApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Name of an Mixed Reality Account.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.remoteRenderingAccountsDelete(subscriptionId, resourceGroupName, accountName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
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

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## remoteRenderingAccountsGet

> RemoteRenderingAccount remoteRenderingAccountsGet(subscriptionId, resourceGroupName, accountName, apiVersion)



Retrieve a Remote Rendering Account.

### Example

```javascript
import MixedReality from 'mixed_reality';
let defaultClient = MixedReality.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MixedReality.ResourceApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Name of an Mixed Reality Account.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.remoteRenderingAccountsGet(subscriptionId, resourceGroupName, accountName, apiVersion, (error, data, response) => {
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

[**RemoteRenderingAccount**](RemoteRenderingAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## remoteRenderingAccountsListByResourceGroup

> RemoteRenderingAccountPage remoteRenderingAccountsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



List Resources by Resource Group

### Example

```javascript
import MixedReality from 'mixed_reality';
let defaultClient = MixedReality.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MixedReality.ResourceApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.remoteRenderingAccountsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. | 

### Return type

[**RemoteRenderingAccountPage**](RemoteRenderingAccountPage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## remoteRenderingAccountsListBySubscription

> RemoteRenderingAccountPage remoteRenderingAccountsListBySubscription(subscriptionId, apiVersion)



List Remote Rendering Accounts by Subscription

### Example

```javascript
import MixedReality from 'mixed_reality';
let defaultClient = MixedReality.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MixedReality.ResourceApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.remoteRenderingAccountsListBySubscription(subscriptionId, apiVersion, (error, data, response) => {
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


## remoteRenderingAccountsUpdate

> RemoteRenderingAccount remoteRenderingAccountsUpdate(subscriptionId, resourceGroupName, accountName, apiVersion, remoteRenderingAccount)



Updating a Remote Rendering Account

### Example

```javascript
import MixedReality from 'mixed_reality';
let defaultClient = MixedReality.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MixedReality.ResourceApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let accountName = "accountName_example"; // String | Name of an Mixed Reality Account.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let remoteRenderingAccount = new MixedReality.RemoteRenderingAccount(); // RemoteRenderingAccount | Remote Rendering Account parameter.
apiInstance.remoteRenderingAccountsUpdate(subscriptionId, resourceGroupName, accountName, apiVersion, remoteRenderingAccount, (error, data, response) => {
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
 **remoteRenderingAccount** | [**RemoteRenderingAccount**](RemoteRenderingAccount.md)| Remote Rendering Account parameter. | 

### Return type

[**RemoteRenderingAccount**](RemoteRenderingAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

