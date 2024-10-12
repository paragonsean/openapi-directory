# ResourceHealthMetadataApiClient.ResourceHealthMetadataApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resourceHealthMetadataGetBySite**](ResourceHealthMetadataApi.md#resourceHealthMetadataGetBySite) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/resourceHealthMetadata/default | Gets the category of ResourceHealthMetadata to use for the given site
[**resourceHealthMetadataGetBySiteSlot**](ResourceHealthMetadataApi.md#resourceHealthMetadataGetBySiteSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/resourceHealthMetadata/default | Gets the category of ResourceHealthMetadata to use for the given site
[**resourceHealthMetadataList**](ResourceHealthMetadataApi.md#resourceHealthMetadataList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/resourceHealthMetadata | List all ResourceHealthMetadata for all sites in the subscription.
[**resourceHealthMetadataListByResourceGroup**](ResourceHealthMetadataApi.md#resourceHealthMetadataListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/resourceHealthMetadata | List all ResourceHealthMetadata for all sites in the resource group in the subscription.
[**resourceHealthMetadataListBySite**](ResourceHealthMetadataApi.md#resourceHealthMetadataListBySite) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/resourceHealthMetadata | Gets the category of ResourceHealthMetadata to use for the given site as a collection
[**resourceHealthMetadataListBySiteSlot**](ResourceHealthMetadataApi.md#resourceHealthMetadataListBySiteSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/resourceHealthMetadata | Gets the category of ResourceHealthMetadata to use for the given site as a collection



## resourceHealthMetadataGetBySite

> ResourceHealthMetadata resourceHealthMetadataGetBySite(resourceGroupName, name, subscriptionId, apiVersion)

Gets the category of ResourceHealthMetadata to use for the given site

Description for Gets the category of ResourceHealthMetadata to use for the given site

### Example

```javascript
import ResourceHealthMetadataApiClient from 'resource_health_metadata_api_client';
let defaultClient = ResourceHealthMetadataApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceHealthMetadataApiClient.ResourceHealthMetadataApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.resourceHealthMetadataGetBySite(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ResourceHealthMetadata**](ResourceHealthMetadata.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourceHealthMetadataGetBySiteSlot

> ResourceHealthMetadata resourceHealthMetadataGetBySiteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets the category of ResourceHealthMetadata to use for the given site

Description for Gets the category of ResourceHealthMetadata to use for the given site

### Example

```javascript
import ResourceHealthMetadataApiClient from 'resource_health_metadata_api_client';
let defaultClient = ResourceHealthMetadataApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceHealthMetadataApiClient.ResourceHealthMetadataApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.resourceHealthMetadataGetBySiteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ResourceHealthMetadata**](ResourceHealthMetadata.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourceHealthMetadataList

> ResourceHealthMetadataCollection resourceHealthMetadataList(subscriptionId, apiVersion)

List all ResourceHealthMetadata for all sites in the subscription.

Description for List all ResourceHealthMetadata for all sites in the subscription.

### Example

```javascript
import ResourceHealthMetadataApiClient from 'resource_health_metadata_api_client';
let defaultClient = ResourceHealthMetadataApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceHealthMetadataApiClient.ResourceHealthMetadataApi();
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.resourceHealthMetadataList(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ResourceHealthMetadataCollection**](ResourceHealthMetadataCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourceHealthMetadataListByResourceGroup

> ResourceHealthMetadataCollection resourceHealthMetadataListByResourceGroup(resourceGroupName, subscriptionId, apiVersion)

List all ResourceHealthMetadata for all sites in the resource group in the subscription.

Description for List all ResourceHealthMetadata for all sites in the resource group in the subscription.

### Example

```javascript
import ResourceHealthMetadataApiClient from 'resource_health_metadata_api_client';
let defaultClient = ResourceHealthMetadataApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceHealthMetadataApiClient.ResourceHealthMetadataApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.resourceHealthMetadataListByResourceGroup(resourceGroupName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ResourceHealthMetadataCollection**](ResourceHealthMetadataCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourceHealthMetadataListBySite

> ResourceHealthMetadataCollection resourceHealthMetadataListBySite(resourceGroupName, name, subscriptionId, apiVersion)

Gets the category of ResourceHealthMetadata to use for the given site as a collection

Description for Gets the category of ResourceHealthMetadata to use for the given site as a collection

### Example

```javascript
import ResourceHealthMetadataApiClient from 'resource_health_metadata_api_client';
let defaultClient = ResourceHealthMetadataApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceHealthMetadataApiClient.ResourceHealthMetadataApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.resourceHealthMetadataListBySite(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ResourceHealthMetadataCollection**](ResourceHealthMetadataCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourceHealthMetadataListBySiteSlot

> ResourceHealthMetadataCollection resourceHealthMetadataListBySiteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets the category of ResourceHealthMetadata to use for the given site as a collection

Description for Gets the category of ResourceHealthMetadata to use for the given site as a collection

### Example

```javascript
import ResourceHealthMetadataApiClient from 'resource_health_metadata_api_client';
let defaultClient = ResourceHealthMetadataApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceHealthMetadataApiClient.ResourceHealthMetadataApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.resourceHealthMetadataListBySiteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ResourceHealthMetadataCollection**](ResourceHealthMetadataCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

