# AzureMapsResourceProvider.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountsCreateOrUpdate**](DefaultApi.md#accountsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Maps/accounts/{accountName} | 
[**accountsDelete**](DefaultApi.md#accountsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Maps/accounts/{accountName} | 
[**accountsGet**](DefaultApi.md#accountsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Maps/accounts/{accountName} | 
[**accountsListByResourceGroup**](DefaultApi.md#accountsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Maps/accounts | 
[**accountsListBySubscription**](DefaultApi.md#accountsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Maps/accounts | 
[**accountsListKeys**](DefaultApi.md#accountsListKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Maps/accounts/{accountName}/listKeys | 
[**accountsListOperations**](DefaultApi.md#accountsListOperations) | **GET** /providers/Microsoft.Maps/operations | 
[**accountsMove**](DefaultApi.md#accountsMove) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/moveResources | 
[**accountsRegenerateKeys**](DefaultApi.md#accountsRegenerateKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Maps/accounts/{accountName}/regenerateKey | 
[**accountsUpdate**](DefaultApi.md#accountsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Maps/accounts/{accountName} | 



## accountsCreateOrUpdate

> MapsAccount accountsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, accountName, mapsAccountCreateParameters)



Create or update a Maps Account. A Maps Account holds the keys which allow access to the Maps REST APIs.

### Example

```javascript
import AzureMapsResourceProvider from 'azure_maps_resource_provider';
let defaultClient = AzureMapsResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMapsResourceProvider.DefaultApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource Group.
let accountName = "accountName_example"; // String | The name of the Maps Account.
let mapsAccountCreateParameters = new AzureMapsResourceProvider.MapsAccountCreateParameters(); // MapsAccountCreateParameters | The new or updated parameters for the Maps Account.
apiInstance.accountsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, accountName, mapsAccountCreateParameters, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the Azure Resource Group. | 
 **accountName** | **String**| The name of the Maps Account. | 
 **mapsAccountCreateParameters** | [**MapsAccountCreateParameters**](MapsAccountCreateParameters.md)| The new or updated parameters for the Maps Account. | 

### Return type

[**MapsAccount**](MapsAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## accountsDelete

> accountsDelete(apiVersion, subscriptionId, resourceGroupName, accountName)



Delete a Maps Account.

### Example

```javascript
import AzureMapsResourceProvider from 'azure_maps_resource_provider';
let defaultClient = AzureMapsResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMapsResourceProvider.DefaultApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource Group.
let accountName = "accountName_example"; // String | The name of the Maps Account.
apiInstance.accountsDelete(apiVersion, subscriptionId, resourceGroupName, accountName, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the Azure Resource Group. | 
 **accountName** | **String**| The name of the Maps Account. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsGet

> MapsAccount accountsGet(apiVersion, subscriptionId, resourceGroupName, accountName)



Get a Maps Account.

### Example

```javascript
import AzureMapsResourceProvider from 'azure_maps_resource_provider';
let defaultClient = AzureMapsResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMapsResourceProvider.DefaultApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource Group.
let accountName = "accountName_example"; // String | The name of the Maps Account.
apiInstance.accountsGet(apiVersion, subscriptionId, resourceGroupName, accountName, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the Azure Resource Group. | 
 **accountName** | **String**| The name of the Maps Account. | 

### Return type

[**MapsAccount**](MapsAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsListByResourceGroup

> MapsAccounts accountsListByResourceGroup(apiVersion, subscriptionId, resourceGroupName)



Get all Maps Accounts in a Resource Group

### Example

```javascript
import AzureMapsResourceProvider from 'azure_maps_resource_provider';
let defaultClient = AzureMapsResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMapsResourceProvider.DefaultApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource Group.
apiInstance.accountsListByResourceGroup(apiVersion, subscriptionId, resourceGroupName, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the Azure Resource Group. | 

### Return type

[**MapsAccounts**](MapsAccounts.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsListBySubscription

> MapsAccounts accountsListBySubscription(apiVersion, subscriptionId)



Get all Maps Accounts in a Subscription

### Example

```javascript
import AzureMapsResourceProvider from 'azure_maps_resource_provider';
let defaultClient = AzureMapsResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMapsResourceProvider.DefaultApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.accountsListBySubscription(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**MapsAccounts**](MapsAccounts.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsListKeys

> MapsAccountKeys accountsListKeys(apiVersion, subscriptionId, resourceGroupName, accountName)



Get the keys to use with the Maps APIs. A key is used to authenticate and authorize access to the Maps REST APIs. Only one key is needed at a time; two are given to provide seamless key regeneration.

### Example

```javascript
import AzureMapsResourceProvider from 'azure_maps_resource_provider';
let defaultClient = AzureMapsResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMapsResourceProvider.DefaultApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource Group.
let accountName = "accountName_example"; // String | The name of the Maps Account.
apiInstance.accountsListKeys(apiVersion, subscriptionId, resourceGroupName, accountName, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the Azure Resource Group. | 
 **accountName** | **String**| The name of the Maps Account. | 

### Return type

[**MapsAccountKeys**](MapsAccountKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsListOperations

> MapsOperations accountsListOperations(apiVersion)



List operations available for the Maps Resource Provider

### Example

```javascript
import AzureMapsResourceProvider from 'azure_maps_resource_provider';
let defaultClient = AzureMapsResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMapsResourceProvider.DefaultApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.accountsListOperations(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**MapsOperations**](MapsOperations.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsMove

> accountsMove(apiVersion, subscriptionId, resourceGroupName, moveRequest)



Moves Maps Accounts from one ResourceGroup (or Subscription) to another

### Example

```javascript
import AzureMapsResourceProvider from 'azure_maps_resource_provider';
let defaultClient = AzureMapsResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMapsResourceProvider.DefaultApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains Maps Account to move.
let moveRequest = new AzureMapsResourceProvider.MapsAccountsMoveRequest(); // MapsAccountsMoveRequest | The details of the Maps Account move.
apiInstance.accountsMove(apiVersion, subscriptionId, resourceGroupName, moveRequest, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group that contains Maps Account to move. | 
 **moveRequest** | [**MapsAccountsMoveRequest**](MapsAccountsMoveRequest.md)| The details of the Maps Account move. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## accountsRegenerateKeys

> MapsAccountKeys accountsRegenerateKeys(apiVersion, subscriptionId, resourceGroupName, accountName, keySpecification)



Regenerate either the primary or secondary key for use with the Maps APIs. The old key will stop working immediately.

### Example

```javascript
import AzureMapsResourceProvider from 'azure_maps_resource_provider';
let defaultClient = AzureMapsResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMapsResourceProvider.DefaultApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource Group.
let accountName = "accountName_example"; // String | The name of the Maps Account.
let keySpecification = new AzureMapsResourceProvider.MapsKeySpecification(); // MapsKeySpecification | Which key to regenerate:  primary or secondary.
apiInstance.accountsRegenerateKeys(apiVersion, subscriptionId, resourceGroupName, accountName, keySpecification, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the Azure Resource Group. | 
 **accountName** | **String**| The name of the Maps Account. | 
 **keySpecification** | [**MapsKeySpecification**](MapsKeySpecification.md)| Which key to regenerate:  primary or secondary. | 

### Return type

[**MapsAccountKeys**](MapsAccountKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## accountsUpdate

> MapsAccount accountsUpdate(apiVersion, subscriptionId, resourceGroupName, accountName, mapsAccountUpdateParameters)



Updates a Maps Account. Only a subset of the parameters may be updated after creation, such as Sku and Tags.

### Example

```javascript
import AzureMapsResourceProvider from 'azure_maps_resource_provider';
let defaultClient = AzureMapsResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMapsResourceProvider.DefaultApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource Group.
let accountName = "accountName_example"; // String | The name of the Maps Account.
let mapsAccountUpdateParameters = new AzureMapsResourceProvider.MapsAccountUpdateParameters(); // MapsAccountUpdateParameters | The updated parameters for the Maps Account.
apiInstance.accountsUpdate(apiVersion, subscriptionId, resourceGroupName, accountName, mapsAccountUpdateParameters, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the Azure Resource Group. | 
 **accountName** | **String**| The name of the Maps Account. | 
 **mapsAccountUpdateParameters** | [**MapsAccountUpdateParameters**](MapsAccountUpdateParameters.md)| The updated parameters for the Maps Account. | 

### Return type

[**MapsAccount**](MapsAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

