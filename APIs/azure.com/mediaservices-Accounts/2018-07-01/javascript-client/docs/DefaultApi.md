# AzureMediaServices.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**locationsCheckNameAvailability**](DefaultApi.md#locationsCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Media/locations/{locationName}/checkNameAvailability | Check Name Availability
[**mediaservicesCreateOrUpdate**](DefaultApi.md#mediaservicesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName} | Create or update a Media Services account
[**mediaservicesDelete**](DefaultApi.md#mediaservicesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName} | Delete a Media Services account.
[**mediaservicesGet**](DefaultApi.md#mediaservicesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName} | Get a Media Services account
[**mediaservicesGetBySubscription**](DefaultApi.md#mediaservicesGetBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Media/mediaservices/{accountName} | Get a Media Services account
[**mediaservicesList**](DefaultApi.md#mediaservicesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices | List Media Services accounts
[**mediaservicesListBySubscription**](DefaultApi.md#mediaservicesListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Media/mediaservices | List Media Services accounts
[**mediaservicesSyncStorageKeys**](DefaultApi.md#mediaservicesSyncStorageKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/syncStorageKeys | Synchronizes Storage Account Keys
[**mediaservicesUpdate**](DefaultApi.md#mediaservicesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName} | Update a Media Services account
[**operationsList**](DefaultApi.md#operationsList) | **GET** /providers/Microsoft.Media/operations | List Operations



## locationsCheckNameAvailability

> EntityNameAvailabilityCheckOutput locationsCheckNameAvailability(subscriptionId, locationName, apiVersion, parameters)

Check Name Availability

Checks whether the Media Service resource name is available.

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let locationName = "locationName_example"; // String | The name of the location
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
let parameters = new AzureMediaServices.CheckNameAvailabilityInput(); // CheckNameAvailabilityInput | The request parameters
apiInstance.locationsCheckNameAvailability(subscriptionId, locationName, apiVersion, parameters, (error, data, response) => {
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
 **locationName** | **String**| The name of the location | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 
 **parameters** | [**CheckNameAvailabilityInput**](CheckNameAvailabilityInput.md)| The request parameters | 

### Return type

[**EntityNameAvailabilityCheckOutput**](EntityNameAvailabilityCheckOutput.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## mediaservicesCreateOrUpdate

> MediaService mediaservicesCreateOrUpdate(subscriptionId, resourceGroupName, accountName, apiVersion, parameters)

Create or update a Media Services account

Creates or updates a Media Services account

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
let parameters = new AzureMediaServices.MediaService(); // MediaService | The request parameters
apiInstance.mediaservicesCreateOrUpdate(subscriptionId, resourceGroupName, accountName, apiVersion, parameters, (error, data, response) => {
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
 **parameters** | [**MediaService**](MediaService.md)| The request parameters | 

### Return type

[**MediaService**](MediaService.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## mediaservicesDelete

> mediaservicesDelete(subscriptionId, resourceGroupName, accountName, apiVersion)

Delete a Media Services account.

Deletes a Media Services account

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.mediaservicesDelete(subscriptionId, resourceGroupName, accountName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mediaservicesGet

> MediaService mediaservicesGet(subscriptionId, resourceGroupName, accountName, apiVersion)

Get a Media Services account

Get the details of a Media Services account

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.mediaservicesGet(subscriptionId, resourceGroupName, accountName, apiVersion, (error, data, response) => {
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

### Return type

[**MediaService**](MediaService.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mediaservicesGetBySubscription

> SubscriptionMediaService mediaservicesGetBySubscription(subscriptionId, accountName, apiVersion)

Get a Media Services account

Get the details of a Media Services account

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.mediaservicesGetBySubscription(subscriptionId, accountName, apiVersion, (error, data, response) => {
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
 **accountName** | **String**| The Media Services account name. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 

### Return type

[**SubscriptionMediaService**](SubscriptionMediaService.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mediaservicesList

> MediaServiceCollection mediaservicesList(subscriptionId, resourceGroupName, apiVersion)

List Media Services accounts

List Media Services accounts in the resource group

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.mediaservicesList(subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 

### Return type

[**MediaServiceCollection**](MediaServiceCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mediaservicesListBySubscription

> SubscriptionMediaServiceCollection mediaservicesListBySubscription(subscriptionId, apiVersion)

List Media Services accounts

List Media Services accounts in the subscription.

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.mediaservicesListBySubscription(subscriptionId, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 

### Return type

[**SubscriptionMediaServiceCollection**](SubscriptionMediaServiceCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mediaservicesSyncStorageKeys

> mediaservicesSyncStorageKeys(subscriptionId, resourceGroupName, accountName, apiVersion, parameters)

Synchronizes Storage Account Keys

Synchronizes storage account keys for a storage account associated with the Media Service account.

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
let parameters = new AzureMediaServices.SyncStorageKeysInput(); // SyncStorageKeysInput | The request parameters
apiInstance.mediaservicesSyncStorageKeys(subscriptionId, resourceGroupName, accountName, apiVersion, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 
 **parameters** | [**SyncStorageKeysInput**](SyncStorageKeysInput.md)| The request parameters | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## mediaservicesUpdate

> MediaService mediaservicesUpdate(subscriptionId, resourceGroupName, accountName, apiVersion, parameters)

Update a Media Services account

Updates an existing Media Services account

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
let parameters = new AzureMediaServices.MediaService(); // MediaService | The request parameters
apiInstance.mediaservicesUpdate(subscriptionId, resourceGroupName, accountName, apiVersion, parameters, (error, data, response) => {
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
 **parameters** | [**MediaService**](MediaService.md)| The request parameters | 

### Return type

[**MediaService**](MediaService.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## operationsList

> OperationCollection operationsList(apiVersion)

List Operations

Lists all the Media Services operations.

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.operationsList(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 

### Return type

[**OperationCollection**](OperationCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

