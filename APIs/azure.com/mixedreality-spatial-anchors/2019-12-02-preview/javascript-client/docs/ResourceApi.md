# MixedReality.ResourceApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**spatialAnchorsAccountsCreate**](ResourceApi.md#spatialAnchorsAccountsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MixedReality/spatialAnchorsAccounts/{accountName} | 
[**spatialAnchorsAccountsDelete**](ResourceApi.md#spatialAnchorsAccountsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MixedReality/spatialAnchorsAccounts/{accountName} | 
[**spatialAnchorsAccountsGet**](ResourceApi.md#spatialAnchorsAccountsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MixedReality/spatialAnchorsAccounts/{accountName} | 
[**spatialAnchorsAccountsListByResourceGroup**](ResourceApi.md#spatialAnchorsAccountsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MixedReality/spatialAnchorsAccounts | 
[**spatialAnchorsAccountsListBySubscription**](ResourceApi.md#spatialAnchorsAccountsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.MixedReality/spatialAnchorsAccounts | 
[**spatialAnchorsAccountsUpdate**](ResourceApi.md#spatialAnchorsAccountsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MixedReality/spatialAnchorsAccounts/{accountName} | 



## spatialAnchorsAccountsCreate

> SpatialAnchorsAccount spatialAnchorsAccountsCreate(subscriptionId, resourceGroupName, accountName, apiVersion, spatialAnchorsAccount)



Creating or Updating a Spatial Anchors Account.

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
let spatialAnchorsAccount = new MixedReality.SpatialAnchorsAccount(); // SpatialAnchorsAccount | Spatial Anchors Account parameter.
apiInstance.spatialAnchorsAccountsCreate(subscriptionId, resourceGroupName, accountName, apiVersion, spatialAnchorsAccount, (error, data, response) => {
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
 **spatialAnchorsAccount** | [**SpatialAnchorsAccount**](SpatialAnchorsAccount.md)| Spatial Anchors Account parameter. | 

### Return type

[**SpatialAnchorsAccount**](SpatialAnchorsAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## spatialAnchorsAccountsDelete

> spatialAnchorsAccountsDelete(subscriptionId, resourceGroupName, accountName, apiVersion)



Delete a Spatial Anchors Account.

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
apiInstance.spatialAnchorsAccountsDelete(subscriptionId, resourceGroupName, accountName, apiVersion, (error, data, response) => {
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


## spatialAnchorsAccountsGet

> SpatialAnchorsAccount spatialAnchorsAccountsGet(subscriptionId, resourceGroupName, accountName, apiVersion)



Retrieve a Spatial Anchors Account.

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
apiInstance.spatialAnchorsAccountsGet(subscriptionId, resourceGroupName, accountName, apiVersion, (error, data, response) => {
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

[**SpatialAnchorsAccount**](SpatialAnchorsAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## spatialAnchorsAccountsListByResourceGroup

> SpatialAnchorsAccountPage spatialAnchorsAccountsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



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
apiInstance.spatialAnchorsAccountsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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

[**SpatialAnchorsAccountPage**](SpatialAnchorsAccountPage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## spatialAnchorsAccountsListBySubscription

> SpatialAnchorsAccountPage spatialAnchorsAccountsListBySubscription(subscriptionId, apiVersion)



List Spatial Anchors Accounts by Subscription

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
apiInstance.spatialAnchorsAccountsListBySubscription(subscriptionId, apiVersion, (error, data, response) => {
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

[**SpatialAnchorsAccountPage**](SpatialAnchorsAccountPage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## spatialAnchorsAccountsUpdate

> SpatialAnchorsAccount spatialAnchorsAccountsUpdate(subscriptionId, resourceGroupName, accountName, apiVersion, spatialAnchorsAccount)



Updating a Spatial Anchors Account

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
let spatialAnchorsAccount = new MixedReality.SpatialAnchorsAccount(); // SpatialAnchorsAccount | Spatial Anchors Account parameter.
apiInstance.spatialAnchorsAccountsUpdate(subscriptionId, resourceGroupName, accountName, apiVersion, spatialAnchorsAccount, (error, data, response) => {
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
 **spatialAnchorsAccount** | [**SpatialAnchorsAccount**](SpatialAnchorsAccount.md)| Spatial Anchors Account parameter. | 

### Return type

[**SpatialAnchorsAccount**](SpatialAnchorsAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

