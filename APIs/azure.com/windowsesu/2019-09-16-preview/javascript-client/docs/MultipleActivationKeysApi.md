# Windowsesu.MultipleActivationKeysApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**multipleActivationKeysCreate**](MultipleActivationKeysApi.md#multipleActivationKeysCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.WindowsESU/multipleActivationKeys/{multipleActivationKeyName} | 
[**multipleActivationKeysDelete**](MultipleActivationKeysApi.md#multipleActivationKeysDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.WindowsESU/multipleActivationKeys/{multipleActivationKeyName} | 
[**multipleActivationKeysGet**](MultipleActivationKeysApi.md#multipleActivationKeysGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.WindowsESU/multipleActivationKeys/{multipleActivationKeyName} | 
[**multipleActivationKeysList**](MultipleActivationKeysApi.md#multipleActivationKeysList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.WindowsESU/multipleActivationKeys | 
[**multipleActivationKeysListByResourceGroup**](MultipleActivationKeysApi.md#multipleActivationKeysListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.WindowsESU/multipleActivationKeys | 
[**multipleActivationKeysUpdate**](MultipleActivationKeysApi.md#multipleActivationKeysUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.WindowsESU/multipleActivationKeys/{multipleActivationKeyName} | 



## multipleActivationKeysCreate

> MultipleActivationKey multipleActivationKeysCreate(subscriptionId, resourceGroupName, apiVersion, multipleActivationKeyName, multipleActivationKey)



Create a MAK key.

### Example

```javascript
import Windowsesu from 'windowsesu';
let defaultClient = Windowsesu.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Windowsesu.MultipleActivationKeysApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let multipleActivationKeyName = "multipleActivationKeyName_example"; // String | The name of the MAK key.
let multipleActivationKey = new Windowsesu.MultipleActivationKey(); // MultipleActivationKey | Details of the MAK key.
apiInstance.multipleActivationKeysCreate(subscriptionId, resourceGroupName, apiVersion, multipleActivationKeyName, multipleActivationKey, (error, data, response) => {
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
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **multipleActivationKeyName** | **String**| The name of the MAK key. | 
 **multipleActivationKey** | [**MultipleActivationKey**](MultipleActivationKey.md)| Details of the MAK key. | 

### Return type

[**MultipleActivationKey**](MultipleActivationKey.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## multipleActivationKeysDelete

> multipleActivationKeysDelete(subscriptionId, resourceGroupName, apiVersion, multipleActivationKeyName)



Delete a MAK key.

### Example

```javascript
import Windowsesu from 'windowsesu';
let defaultClient = Windowsesu.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Windowsesu.MultipleActivationKeysApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let multipleActivationKeyName = "multipleActivationKeyName_example"; // String | The name of the MAK key.
apiInstance.multipleActivationKeysDelete(subscriptionId, resourceGroupName, apiVersion, multipleActivationKeyName, (error, data, response) => {
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
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **multipleActivationKeyName** | **String**| The name of the MAK key. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## multipleActivationKeysGet

> MultipleActivationKey multipleActivationKeysGet(subscriptionId, resourceGroupName, apiVersion, multipleActivationKeyName)



Get a MAK key.

### Example

```javascript
import Windowsesu from 'windowsesu';
let defaultClient = Windowsesu.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Windowsesu.MultipleActivationKeysApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let multipleActivationKeyName = "multipleActivationKeyName_example"; // String | The name of the MAK key.
apiInstance.multipleActivationKeysGet(subscriptionId, resourceGroupName, apiVersion, multipleActivationKeyName, (error, data, response) => {
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
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **multipleActivationKeyName** | **String**| The name of the MAK key. | 

### Return type

[**MultipleActivationKey**](MultipleActivationKey.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## multipleActivationKeysList

> MultipleActivationKeyList multipleActivationKeysList(subscriptionId, apiVersion)



List all Multiple Activation Keys (MAK) created for a subscription.

### Example

```javascript
import Windowsesu from 'windowsesu';
let defaultClient = Windowsesu.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Windowsesu.MultipleActivationKeysApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.multipleActivationKeysList(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

[**MultipleActivationKeyList**](MultipleActivationKeyList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## multipleActivationKeysListByResourceGroup

> MultipleActivationKeyList multipleActivationKeysListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



List all Multiple Activation Keys (MAK) in a resource group.

### Example

```javascript
import Windowsesu from 'windowsesu';
let defaultClient = Windowsesu.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Windowsesu.MultipleActivationKeysApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.multipleActivationKeysListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

[**MultipleActivationKeyList**](MultipleActivationKeyList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## multipleActivationKeysUpdate

> MultipleActivationKey multipleActivationKeysUpdate(subscriptionId, resourceGroupName, apiVersion, multipleActivationKeyName, multipleActivationKey)



Update a MAK key.

### Example

```javascript
import Windowsesu from 'windowsesu';
let defaultClient = Windowsesu.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Windowsesu.MultipleActivationKeysApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let multipleActivationKeyName = "multipleActivationKeyName_example"; // String | The name of the MAK key.
let multipleActivationKey = new Windowsesu.MultipleActivationKeyUpdate(); // MultipleActivationKeyUpdate | Details of the MAK key.
apiInstance.multipleActivationKeysUpdate(subscriptionId, resourceGroupName, apiVersion, multipleActivationKeyName, multipleActivationKey, (error, data, response) => {
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
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **multipleActivationKeyName** | **String**| The name of the MAK key. | 
 **multipleActivationKey** | [**MultipleActivationKeyUpdate**](MultipleActivationKeyUpdate.md)| Details of the MAK key. | 

### Return type

[**MultipleActivationKey**](MultipleActivationKey.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

