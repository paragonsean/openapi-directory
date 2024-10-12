# MediaServicesManagementClient.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mediaServiceCheckNameAvailability**](DefaultApi.md#mediaServiceCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Media/CheckNameAvailability | 
[**mediaServiceCreate**](DefaultApi.md#mediaServiceCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{mediaServiceName} | 
[**mediaServiceDelete**](DefaultApi.md#mediaServiceDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{mediaServiceName} | 
[**mediaServiceGet**](DefaultApi.md#mediaServiceGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{mediaServiceName} | 
[**mediaServiceListByResourceGroup**](DefaultApi.md#mediaServiceListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices | 
[**mediaServiceListKeys**](DefaultApi.md#mediaServiceListKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{mediaServiceName}/listKeys | 
[**mediaServiceRegenerateKey**](DefaultApi.md#mediaServiceRegenerateKey) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{mediaServiceName}/regenerateKey | 
[**mediaServiceSyncStorageKeys**](DefaultApi.md#mediaServiceSyncStorageKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{mediaServiceName}/syncStorageKeys | 
[**mediaServiceUpdate**](DefaultApi.md#mediaServiceUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{mediaServiceName} | 
[**operationsList**](DefaultApi.md#operationsList) | **GET** /providers/Microsoft.Media/operations | 



## mediaServiceCheckNameAvailability

> CheckNameAvailabilityOutput mediaServiceCheckNameAvailability(subscriptionId, apiVersion, parameters)



Checks whether the Media Service resource name is available. The name must be globally unique.

### Example

```javascript
import MediaServicesManagementClient from 'media_services_management_client';
let defaultClient = MediaServicesManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MediaServicesManagementClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-10-01.
let parameters = new MediaServicesManagementClient.CheckNameAvailabilityInput(); // CheckNameAvailabilityInput | Properties needed to check the availability of a name.
apiInstance.mediaServiceCheckNameAvailability(subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-10-01. | 
 **parameters** | [**CheckNameAvailabilityInput**](CheckNameAvailabilityInput.md)| Properties needed to check the availability of a name. | 

### Return type

[**CheckNameAvailabilityOutput**](CheckNameAvailabilityOutput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## mediaServiceCreate

> MediaService mediaServiceCreate(subscriptionId, apiVersion, resourceGroupName, mediaServiceName, parameters)



Creates a Media Service.

### Example

```javascript
import MediaServicesManagementClient from 'media_services_management_client';
let defaultClient = MediaServicesManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MediaServicesManagementClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-10-01.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
let mediaServiceName = "mediaServiceName_example"; // String | Name of the Media Service.
let parameters = new MediaServicesManagementClient.MediaService(); // MediaService | Media Service properties needed for creation.
apiInstance.mediaServiceCreate(subscriptionId, apiVersion, resourceGroupName, mediaServiceName, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-10-01. | 
 **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | 
 **mediaServiceName** | **String**| Name of the Media Service. | 
 **parameters** | [**MediaService**](MediaService.md)| Media Service properties needed for creation. | 

### Return type

[**MediaService**](MediaService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## mediaServiceDelete

> mediaServiceDelete(subscriptionId, apiVersion, resourceGroupName, mediaServiceName)



Deletes a Media Service.

### Example

```javascript
import MediaServicesManagementClient from 'media_services_management_client';
let defaultClient = MediaServicesManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MediaServicesManagementClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-10-01.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
let mediaServiceName = "mediaServiceName_example"; // String | Name of the Media Service.
apiInstance.mediaServiceDelete(subscriptionId, apiVersion, resourceGroupName, mediaServiceName, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-10-01. | 
 **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | 
 **mediaServiceName** | **String**| Name of the Media Service. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mediaServiceGet

> MediaService mediaServiceGet(subscriptionId, apiVersion, resourceGroupName, mediaServiceName)



Gets a Media Service.

### Example

```javascript
import MediaServicesManagementClient from 'media_services_management_client';
let defaultClient = MediaServicesManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MediaServicesManagementClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-10-01.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
let mediaServiceName = "mediaServiceName_example"; // String | Name of the Media Service.
apiInstance.mediaServiceGet(subscriptionId, apiVersion, resourceGroupName, mediaServiceName, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-10-01. | 
 **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | 
 **mediaServiceName** | **String**| Name of the Media Service. | 

### Return type

[**MediaService**](MediaService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mediaServiceListByResourceGroup

> MediaServiceCollection mediaServiceListByResourceGroup(subscriptionId, apiVersion, resourceGroupName)



Lists all of the Media Services in a resource group.

### Example

```javascript
import MediaServicesManagementClient from 'media_services_management_client';
let defaultClient = MediaServicesManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MediaServicesManagementClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-10-01.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
apiInstance.mediaServiceListByResourceGroup(subscriptionId, apiVersion, resourceGroupName, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-10-01. | 
 **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | 

### Return type

[**MediaServiceCollection**](MediaServiceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mediaServiceListKeys

> ServiceKeys mediaServiceListKeys(subscriptionId, apiVersion, resourceGroupName, mediaServiceName)



Lists the keys for a Media Service.

### Example

```javascript
import MediaServicesManagementClient from 'media_services_management_client';
let defaultClient = MediaServicesManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MediaServicesManagementClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-10-01.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
let mediaServiceName = "mediaServiceName_example"; // String | Name of the Media Service.
apiInstance.mediaServiceListKeys(subscriptionId, apiVersion, resourceGroupName, mediaServiceName, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-10-01. | 
 **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | 
 **mediaServiceName** | **String**| Name of the Media Service. | 

### Return type

[**ServiceKeys**](ServiceKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mediaServiceRegenerateKey

> RegenerateKeyOutput mediaServiceRegenerateKey(subscriptionId, apiVersion, resourceGroupName, mediaServiceName, parameters)



Regenerates a primary or secondary key for a Media Service.

### Example

```javascript
import MediaServicesManagementClient from 'media_services_management_client';
let defaultClient = MediaServicesManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MediaServicesManagementClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-10-01.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
let mediaServiceName = "mediaServiceName_example"; // String | Name of the Media Service.
let parameters = new MediaServicesManagementClient.RegenerateKeyInput(); // RegenerateKeyInput | Properties needed to regenerate the Media Service key.
apiInstance.mediaServiceRegenerateKey(subscriptionId, apiVersion, resourceGroupName, mediaServiceName, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-10-01. | 
 **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | 
 **mediaServiceName** | **String**| Name of the Media Service. | 
 **parameters** | [**RegenerateKeyInput**](RegenerateKeyInput.md)| Properties needed to regenerate the Media Service key. | 

### Return type

[**RegenerateKeyOutput**](RegenerateKeyOutput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## mediaServiceSyncStorageKeys

> mediaServiceSyncStorageKeys(subscriptionId, apiVersion, resourceGroupName, mediaServiceName, parameters)



Synchronizes storage account keys for a storage account associated with the Media Service account.

### Example

```javascript
import MediaServicesManagementClient from 'media_services_management_client';
let defaultClient = MediaServicesManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MediaServicesManagementClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-10-01.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
let mediaServiceName = "mediaServiceName_example"; // String | Name of the Media Service.
let parameters = new MediaServicesManagementClient.SyncStorageKeysInput(); // SyncStorageKeysInput | Properties needed to synchronize the keys for a storage account to the Media Service.
apiInstance.mediaServiceSyncStorageKeys(subscriptionId, apiVersion, resourceGroupName, mediaServiceName, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-10-01. | 
 **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | 
 **mediaServiceName** | **String**| Name of the Media Service. | 
 **parameters** | [**SyncStorageKeysInput**](SyncStorageKeysInput.md)| Properties needed to synchronize the keys for a storage account to the Media Service. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## mediaServiceUpdate

> MediaService mediaServiceUpdate(subscriptionId, apiVersion, resourceGroupName, mediaServiceName, parameters)



Updates a Media Service.

### Example

```javascript
import MediaServicesManagementClient from 'media_services_management_client';
let defaultClient = MediaServicesManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MediaServicesManagementClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-10-01.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
let mediaServiceName = "mediaServiceName_example"; // String | Name of the Media Service.
let parameters = new MediaServicesManagementClient.MediaService(); // MediaService | Media Service properties needed for update.
apiInstance.mediaServiceUpdate(subscriptionId, apiVersion, resourceGroupName, mediaServiceName, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-10-01. | 
 **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | 
 **mediaServiceName** | **String**| Name of the Media Service. | 
 **parameters** | [**MediaService**](MediaService.md)| Media Service properties needed for update. | 

### Return type

[**MediaService**](MediaService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## operationsList

> OperationListResult operationsList(apiVersion)



Lists all of the available Media Services REST API operations.

### Example

```javascript
import MediaServicesManagementClient from 'media_services_management_client';
let defaultClient = MediaServicesManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MediaServicesManagementClient.DefaultApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-10-01.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-10-01. | 

### Return type

[**OperationListResult**](OperationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

