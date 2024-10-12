# AzureMediaServices.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assetsCreateOrUpdate**](DefaultApi.md#assetsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/assets/{assetName} | Create or update an Asset
[**assetsDelete**](DefaultApi.md#assetsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/assets/{assetName} | Delete an Asset.
[**assetsGet**](DefaultApi.md#assetsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/assets/{assetName} | Get an Asset
[**assetsGetEncryptionKey**](DefaultApi.md#assetsGetEncryptionKey) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/assets/{assetName}/getEncryptionKey | Gets the Asset storage key
[**assetsList**](DefaultApi.md#assetsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/assets | List Assets
[**assetsListContainerSas**](DefaultApi.md#assetsListContainerSas) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/assets/{assetName}/listContainerSas | List the Asset URLs
[**assetsUpdate**](DefaultApi.md#assetsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/assets/{assetName} | Update an Asset



## assetsCreateOrUpdate

> Asset assetsCreateOrUpdate(subscriptionId, resourceGroupName, accountName, assetName, apiVersion, parameters)

Create or update an Asset

Creates or updates an Asset in the Media Services account

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let assetName = "assetName_example"; // String | The Asset name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
let parameters = new AzureMediaServices.Asset(); // Asset | The request parameters
apiInstance.assetsCreateOrUpdate(subscriptionId, resourceGroupName, accountName, assetName, apiVersion, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | 
 **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | 
 **accountName** | **String**| The Media Services account name. | 
 **assetName** | **String**| The Asset name. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 
 **parameters** | [**Asset**](Asset.md)| The request parameters | 

### Return type

[**Asset**](Asset.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## assetsDelete

> assetsDelete(subscriptionId, resourceGroupName, accountName, assetName, apiVersion)

Delete an Asset.

Deletes an Asset in the Media Services account

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let assetName = "assetName_example"; // String | The Asset name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.assetsDelete(subscriptionId, resourceGroupName, accountName, assetName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | 
 **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | 
 **accountName** | **String**| The Media Services account name. | 
 **assetName** | **String**| The Asset name. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## assetsGet

> Asset assetsGet(subscriptionId, resourceGroupName, accountName, assetName, apiVersion)

Get an Asset

Get the details of an Asset in the Media Services account

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let assetName = "assetName_example"; // String | The Asset name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.assetsGet(subscriptionId, resourceGroupName, accountName, assetName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | 
 **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | 
 **accountName** | **String**| The Media Services account name. | 
 **assetName** | **String**| The Asset name. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 

### Return type

[**Asset**](Asset.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## assetsGetEncryptionKey

> AssetStorageEncryptionKey assetsGetEncryptionKey(subscriptionId, resourceGroupName, accountName, assetName, apiVersion)

Gets the Asset storage key

Gets the Asset storage encryption keys used to decrypt content created by version 2 of the Media Services API

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let assetName = "assetName_example"; // String | The Asset name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.assetsGetEncryptionKey(subscriptionId, resourceGroupName, accountName, assetName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | 
 **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | 
 **accountName** | **String**| The Media Services account name. | 
 **assetName** | **String**| The Asset name. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 

### Return type

[**AssetStorageEncryptionKey**](AssetStorageEncryptionKey.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## assetsList

> AssetCollection assetsList(subscriptionId, resourceGroupName, accountName, apiVersion, opts)

List Assets

List Assets in the Media Services account with optional filtering and ordering

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
let opts = {
  'filter': "filter_example", // String | Restricts the set of items returned.
  'top': 56, // Number | Specifies a non-negative integer n that limits the number of items returned from a collection. The service returns the number of available items up to but not greater than the specified value n.
  'orderby': "orderby_example" // String | Specifies the key by which the result collection should be ordered.
};
apiInstance.assetsList(subscriptionId, resourceGroupName, accountName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | 
 **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | 
 **accountName** | **String**| The Media Services account name. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 
 **filter** | **String**| Restricts the set of items returned. | [optional] 
 **top** | **Number**| Specifies a non-negative integer n that limits the number of items returned from a collection. The service returns the number of available items up to but not greater than the specified value n. | [optional] 
 **orderby** | **String**| Specifies the key by which the result collection should be ordered. | [optional] 

### Return type

[**AssetCollection**](AssetCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## assetsListContainerSas

> AssetContainerSas assetsListContainerSas(subscriptionId, resourceGroupName, accountName, assetName, apiVersion, parameters)

List the Asset URLs

Lists storage container URLs with shared access signatures (SAS) for uploading and downloading Asset content. The signatures are derived from the storage account keys.

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let assetName = "assetName_example"; // String | The Asset name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
let parameters = new AzureMediaServices.ListContainerSasInput(); // ListContainerSasInput | The request parameters
apiInstance.assetsListContainerSas(subscriptionId, resourceGroupName, accountName, assetName, apiVersion, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | 
 **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | 
 **accountName** | **String**| The Media Services account name. | 
 **assetName** | **String**| The Asset name. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 
 **parameters** | [**ListContainerSasInput**](ListContainerSasInput.md)| The request parameters | 

### Return type

[**AssetContainerSas**](AssetContainerSas.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## assetsUpdate

> Asset assetsUpdate(subscriptionId, resourceGroupName, accountName, assetName, apiVersion, parameters)

Update an Asset

Updates an existing Asset in the Media Services account

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let assetName = "assetName_example"; // String | The Asset name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
let parameters = new AzureMediaServices.Asset(); // Asset | The request parameters
apiInstance.assetsUpdate(subscriptionId, resourceGroupName, accountName, assetName, apiVersion, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | 
 **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | 
 **accountName** | **String**| The Media Services account name. | 
 **assetName** | **String**| The Asset name. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 
 **parameters** | [**Asset**](Asset.md)| The request parameters | 

### Return type

[**Asset**](Asset.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

