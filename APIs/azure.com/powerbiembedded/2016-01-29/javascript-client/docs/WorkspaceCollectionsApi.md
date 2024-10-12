# PowerBiEmbeddedManagementClient.WorkspaceCollectionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workspaceCollectionsCheckNameAvailability**](WorkspaceCollectionsApi.md#workspaceCollectionsCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.PowerBI/locations/{location}/checkNameAvailability | 
[**workspaceCollectionsCreate**](WorkspaceCollectionsApi.md#workspaceCollectionsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PowerBI/workspaceCollections/{workspaceCollectionName} | 
[**workspaceCollectionsDelete**](WorkspaceCollectionsApi.md#workspaceCollectionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PowerBI/workspaceCollections/{workspaceCollectionName} | 
[**workspaceCollectionsGetAccessKeys**](WorkspaceCollectionsApi.md#workspaceCollectionsGetAccessKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PowerBI/workspaceCollections/{workspaceCollectionName}/listKeys | 
[**workspaceCollectionsGetByName**](WorkspaceCollectionsApi.md#workspaceCollectionsGetByName) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PowerBI/workspaceCollections/{workspaceCollectionName} | 
[**workspaceCollectionsListByResourceGroup**](WorkspaceCollectionsApi.md#workspaceCollectionsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PowerBI/workspaceCollections | 
[**workspaceCollectionsListBySubscription**](WorkspaceCollectionsApi.md#workspaceCollectionsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.PowerBI/workspaceCollections | 
[**workspaceCollectionsMigrate**](WorkspaceCollectionsApi.md#workspaceCollectionsMigrate) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/moveResources | 
[**workspaceCollectionsRegenerateKey**](WorkspaceCollectionsApi.md#workspaceCollectionsRegenerateKey) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PowerBI/workspaceCollections/{workspaceCollectionName}/regenerateKey | 
[**workspaceCollectionsUpdate**](WorkspaceCollectionsApi.md#workspaceCollectionsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PowerBI/workspaceCollections/{workspaceCollectionName} | 



## workspaceCollectionsCheckNameAvailability

> CheckNameResponse workspaceCollectionsCheckNameAvailability(subscriptionId, location, apiVersion, body)



Verify the specified Power BI Workspace Collection name is valid and not already in use.

### Example

```javascript
import PowerBiEmbeddedManagementClient from 'power_bi_embedded_management_client';

let apiInstance = new PowerBiEmbeddedManagementClient.WorkspaceCollectionsApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let location = "location_example"; // String | Azure location
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let body = new PowerBiEmbeddedManagementClient.CheckNameRequest(); // CheckNameRequest | Check name availability request
apiInstance.workspaceCollectionsCheckNameAvailability(subscriptionId, location, apiVersion, body, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **location** | **String**| Azure location | 
 **apiVersion** | **String**| Client Api Version. | 
 **body** | [**CheckNameRequest**](CheckNameRequest.md)| Check name availability request | 

### Return type

[**CheckNameResponse**](CheckNameResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## workspaceCollectionsCreate

> WorkspaceCollection workspaceCollectionsCreate(subscriptionId, resourceGroupName, workspaceCollectionName, apiVersion, body)



Creates a new Power BI Workspace Collection with the specified properties. A Power BI Workspace Collection contains one or more workspaces, and can be used to provision keys that provide API access to those workspaces.

### Example

```javascript
import PowerBiEmbeddedManagementClient from 'power_bi_embedded_management_client';

let apiInstance = new PowerBiEmbeddedManagementClient.WorkspaceCollectionsApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group
let workspaceCollectionName = "workspaceCollectionName_example"; // String | Power BI Embedded Workspace Collection name
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let body = new PowerBiEmbeddedManagementClient.CreateWorkspaceCollectionRequest(); // CreateWorkspaceCollectionRequest | Create workspace collection request
apiInstance.workspaceCollectionsCreate(subscriptionId, resourceGroupName, workspaceCollectionName, apiVersion, body, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Azure resource group | 
 **workspaceCollectionName** | **String**| Power BI Embedded Workspace Collection name | 
 **apiVersion** | **String**| Client Api Version. | 
 **body** | [**CreateWorkspaceCollectionRequest**](CreateWorkspaceCollectionRequest.md)| Create workspace collection request | 

### Return type

[**WorkspaceCollection**](WorkspaceCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## workspaceCollectionsDelete

> workspaceCollectionsDelete(subscriptionId, resourceGroupName, workspaceCollectionName, apiVersion)



Delete a Power BI Workspace Collection.

### Example

```javascript
import PowerBiEmbeddedManagementClient from 'power_bi_embedded_management_client';

let apiInstance = new PowerBiEmbeddedManagementClient.WorkspaceCollectionsApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group
let workspaceCollectionName = "workspaceCollectionName_example"; // String | Power BI Embedded Workspace Collection name
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.workspaceCollectionsDelete(subscriptionId, resourceGroupName, workspaceCollectionName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Azure resource group | 
 **workspaceCollectionName** | **String**| Power BI Embedded Workspace Collection name | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspaceCollectionsGetAccessKeys

> WorkspaceCollectionAccessKeys workspaceCollectionsGetAccessKeys(subscriptionId, resourceGroupName, workspaceCollectionName, apiVersion)



Retrieves the primary and secondary access keys for the specified Power BI Workspace Collection.

### Example

```javascript
import PowerBiEmbeddedManagementClient from 'power_bi_embedded_management_client';

let apiInstance = new PowerBiEmbeddedManagementClient.WorkspaceCollectionsApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group
let workspaceCollectionName = "workspaceCollectionName_example"; // String | Power BI Embedded Workspace Collection name
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.workspaceCollectionsGetAccessKeys(subscriptionId, resourceGroupName, workspaceCollectionName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Azure resource group | 
 **workspaceCollectionName** | **String**| Power BI Embedded Workspace Collection name | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**WorkspaceCollectionAccessKeys**](WorkspaceCollectionAccessKeys.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspaceCollectionsGetByName

> WorkspaceCollection workspaceCollectionsGetByName(subscriptionId, resourceGroupName, workspaceCollectionName, apiVersion)



Retrieves an existing Power BI Workspace Collection.

### Example

```javascript
import PowerBiEmbeddedManagementClient from 'power_bi_embedded_management_client';

let apiInstance = new PowerBiEmbeddedManagementClient.WorkspaceCollectionsApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group
let workspaceCollectionName = "workspaceCollectionName_example"; // String | Power BI Embedded Workspace Collection name
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.workspaceCollectionsGetByName(subscriptionId, resourceGroupName, workspaceCollectionName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Azure resource group | 
 **workspaceCollectionName** | **String**| Power BI Embedded Workspace Collection name | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**WorkspaceCollection**](WorkspaceCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspaceCollectionsListByResourceGroup

> WorkspaceCollectionList workspaceCollectionsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



Retrieves all existing Power BI workspace collections in the specified resource group.

### Example

```javascript
import PowerBiEmbeddedManagementClient from 'power_bi_embedded_management_client';

let apiInstance = new PowerBiEmbeddedManagementClient.WorkspaceCollectionsApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.workspaceCollectionsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Azure resource group | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**WorkspaceCollectionList**](WorkspaceCollectionList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspaceCollectionsListBySubscription

> WorkspaceCollectionList workspaceCollectionsListBySubscription(subscriptionId, apiVersion)



Retrieves all existing Power BI workspace collections in the specified subscription.

### Example

```javascript
import PowerBiEmbeddedManagementClient from 'power_bi_embedded_management_client';

let apiInstance = new PowerBiEmbeddedManagementClient.WorkspaceCollectionsApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.workspaceCollectionsListBySubscription(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**WorkspaceCollectionList**](WorkspaceCollectionList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspaceCollectionsMigrate

> workspaceCollectionsMigrate(subscriptionId, resourceGroupName, apiVersion, body)



Migrates an existing Power BI Workspace Collection to a different resource group and/or subscription.

### Example

```javascript
import PowerBiEmbeddedManagementClient from 'power_bi_embedded_management_client';

let apiInstance = new PowerBiEmbeddedManagementClient.WorkspaceCollectionsApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let body = new PowerBiEmbeddedManagementClient.MigrateWorkspaceCollectionRequest(); // MigrateWorkspaceCollectionRequest | Workspace migration request
apiInstance.workspaceCollectionsMigrate(subscriptionId, resourceGroupName, apiVersion, body, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Azure resource group | 
 **apiVersion** | **String**| Client Api Version. | 
 **body** | [**MigrateWorkspaceCollectionRequest**](MigrateWorkspaceCollectionRequest.md)| Workspace migration request | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## workspaceCollectionsRegenerateKey

> WorkspaceCollectionAccessKeys workspaceCollectionsRegenerateKey(subscriptionId, resourceGroupName, workspaceCollectionName, apiVersion, body)



Regenerates the primary or secondary access key for the specified Power BI Workspace Collection.

### Example

```javascript
import PowerBiEmbeddedManagementClient from 'power_bi_embedded_management_client';

let apiInstance = new PowerBiEmbeddedManagementClient.WorkspaceCollectionsApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group
let workspaceCollectionName = "workspaceCollectionName_example"; // String | Power BI Embedded Workspace Collection name
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let body = new PowerBiEmbeddedManagementClient.WorkspaceCollectionAccessKey(); // WorkspaceCollectionAccessKey | Access key to regenerate
apiInstance.workspaceCollectionsRegenerateKey(subscriptionId, resourceGroupName, workspaceCollectionName, apiVersion, body, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Azure resource group | 
 **workspaceCollectionName** | **String**| Power BI Embedded Workspace Collection name | 
 **apiVersion** | **String**| Client Api Version. | 
 **body** | [**WorkspaceCollectionAccessKey**](WorkspaceCollectionAccessKey.md)| Access key to regenerate | 

### Return type

[**WorkspaceCollectionAccessKeys**](WorkspaceCollectionAccessKeys.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## workspaceCollectionsUpdate

> WorkspaceCollection workspaceCollectionsUpdate(subscriptionId, resourceGroupName, workspaceCollectionName, apiVersion, body)



Update an existing Power BI Workspace Collection with the specified properties.

### Example

```javascript
import PowerBiEmbeddedManagementClient from 'power_bi_embedded_management_client';

let apiInstance = new PowerBiEmbeddedManagementClient.WorkspaceCollectionsApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group
let workspaceCollectionName = "workspaceCollectionName_example"; // String | Power BI Embedded Workspace Collection name
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let body = new PowerBiEmbeddedManagementClient.UpdateWorkspaceCollectionRequest(); // UpdateWorkspaceCollectionRequest | Update workspace collection request
apiInstance.workspaceCollectionsUpdate(subscriptionId, resourceGroupName, workspaceCollectionName, apiVersion, body, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Azure resource group | 
 **workspaceCollectionName** | **String**| Power BI Embedded Workspace Collection name | 
 **apiVersion** | **String**| Client Api Version. | 
 **body** | [**UpdateWorkspaceCollectionRequest**](UpdateWorkspaceCollectionRequest.md)| Update workspace collection request | 

### Return type

[**WorkspaceCollection**](WorkspaceCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

