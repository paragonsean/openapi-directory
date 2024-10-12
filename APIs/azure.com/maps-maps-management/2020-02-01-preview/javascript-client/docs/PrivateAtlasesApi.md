# AzureMapsResourceProvider.PrivateAtlasesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**privateAtlasesCreateOrUpdate**](PrivateAtlasesApi.md#privateAtlasesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Maps/accounts/{accountName}/privateAtlases/{privateAtlasName} | 
[**privateAtlasesDelete**](PrivateAtlasesApi.md#privateAtlasesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Maps/accounts/{accountName}/privateAtlases/{privateAtlasName} | 
[**privateAtlasesGet**](PrivateAtlasesApi.md#privateAtlasesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Maps/accounts/{accountName}/privateAtlases/{privateAtlasName} | 
[**privateAtlasesListByAccount**](PrivateAtlasesApi.md#privateAtlasesListByAccount) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Maps/accounts/{accountName}/privateAtlases | 
[**privateAtlasesUpdate**](PrivateAtlasesApi.md#privateAtlasesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Maps/accounts/{accountName}/privateAtlases/{privateAtlasName} | 



## privateAtlasesCreateOrUpdate

> PrivateAtlas privateAtlasesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, accountName, privateAtlasName, privateAtlasCreateParameters)



Create or update a Private Atlas resource. Private Atlas resource will enable the usage of Azure resources to build a custom set of mapping data. It requires an account to exist before it can be created.

### Example

```javascript
import AzureMapsResourceProvider from 'azure_maps_resource_provider';
let defaultClient = AzureMapsResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMapsResourceProvider.PrivateAtlasesApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let accountName = "accountName_example"; // String | The name of the Maps Account.
let privateAtlasName = "privateAtlasName_example"; // String | The name of the Private Atlas instance.
let privateAtlasCreateParameters = new AzureMapsResourceProvider.PrivateAtlasCreateParameters(); // PrivateAtlasCreateParameters | The new or updated parameters for the Private Atlas resource.
apiInstance.privateAtlasesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, accountName, privateAtlasName, privateAtlasCreateParameters, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **accountName** | **String**| The name of the Maps Account. | 
 **privateAtlasName** | **String**| The name of the Private Atlas instance. | 
 **privateAtlasCreateParameters** | [**PrivateAtlasCreateParameters**](PrivateAtlasCreateParameters.md)| The new or updated parameters for the Private Atlas resource. | 

### Return type

[**PrivateAtlas**](PrivateAtlas.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateAtlasesDelete

> privateAtlasesDelete(apiVersion, subscriptionId, resourceGroupName, accountName, privateAtlasName)



Delete a Private Atlas resource.

### Example

```javascript
import AzureMapsResourceProvider from 'azure_maps_resource_provider';
let defaultClient = AzureMapsResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMapsResourceProvider.PrivateAtlasesApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let accountName = "accountName_example"; // String | The name of the Maps Account.
let privateAtlasName = "privateAtlasName_example"; // String | The name of the Private Atlas instance.
apiInstance.privateAtlasesDelete(apiVersion, subscriptionId, resourceGroupName, accountName, privateAtlasName, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **accountName** | **String**| The name of the Maps Account. | 
 **privateAtlasName** | **String**| The name of the Private Atlas instance. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateAtlasesGet

> PrivateAtlas privateAtlasesGet(apiVersion, subscriptionId, resourceGroupName, accountName, privateAtlasName)



Get a Private Atlas resource.

### Example

```javascript
import AzureMapsResourceProvider from 'azure_maps_resource_provider';
let defaultClient = AzureMapsResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMapsResourceProvider.PrivateAtlasesApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let accountName = "accountName_example"; // String | The name of the Maps Account.
let privateAtlasName = "privateAtlasName_example"; // String | The name of the Private Atlas instance.
apiInstance.privateAtlasesGet(apiVersion, subscriptionId, resourceGroupName, accountName, privateAtlasName, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **accountName** | **String**| The name of the Maps Account. | 
 **privateAtlasName** | **String**| The name of the Private Atlas instance. | 

### Return type

[**PrivateAtlas**](PrivateAtlas.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateAtlasesListByAccount

> PrivateAtlasList privateAtlasesListByAccount(apiVersion, subscriptionId, resourceGroupName, accountName)



Get all Private Atlas instances for an Azure Map Account

### Example

```javascript
import AzureMapsResourceProvider from 'azure_maps_resource_provider';
let defaultClient = AzureMapsResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMapsResourceProvider.PrivateAtlasesApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let accountName = "accountName_example"; // String | The name of the Maps Account.
apiInstance.privateAtlasesListByAccount(apiVersion, subscriptionId, resourceGroupName, accountName, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **accountName** | **String**| The name of the Maps Account. | 

### Return type

[**PrivateAtlasList**](PrivateAtlasList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateAtlasesUpdate

> PrivateAtlas privateAtlasesUpdate(apiVersion, subscriptionId, resourceGroupName, accountName, privateAtlasName, privateAtlasUpdateParameters)



Updates the Private Atlas resource. Only a subset of the parameters may be updated after creation, such as Tags.

### Example

```javascript
import AzureMapsResourceProvider from 'azure_maps_resource_provider';
let defaultClient = AzureMapsResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMapsResourceProvider.PrivateAtlasesApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let accountName = "accountName_example"; // String | The name of the Maps Account.
let privateAtlasName = "privateAtlasName_example"; // String | The name of the Private Atlas instance.
let privateAtlasUpdateParameters = new AzureMapsResourceProvider.PrivateAtlasUpdateParameters(); // PrivateAtlasUpdateParameters | The updated parameters for the Private Atlas.
apiInstance.privateAtlasesUpdate(apiVersion, subscriptionId, resourceGroupName, accountName, privateAtlasName, privateAtlasUpdateParameters, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **accountName** | **String**| The name of the Maps Account. | 
 **privateAtlasName** | **String**| The name of the Private Atlas instance. | 
 **privateAtlasUpdateParameters** | [**PrivateAtlasUpdateParameters**](PrivateAtlasUpdateParameters.md)| The updated parameters for the Private Atlas. | 

### Return type

[**PrivateAtlas**](PrivateAtlas.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

