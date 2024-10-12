# SeaBreezeManagementClient.VolumesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**volumeCreate**](VolumesApi.md#volumeCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/volumes/{volumeResourceName} | Creates or updates a volume resource.
[**volumeDelete**](VolumesApi.md#volumeDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/volumes/{volumeResourceName} | Deletes the volume resource.
[**volumeGet**](VolumesApi.md#volumeGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/volumes/{volumeResourceName} | Gets the volume resource with the given name.
[**volumeListByResourceGroup**](VolumesApi.md#volumeListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/volumes | Gets all the volume resources in a given resource group.
[**volumeListBySubscription**](VolumesApi.md#volumeListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ServiceFabricMesh/volumes | Gets all the volume resources in a given subscription.



## volumeCreate

> VolumeResourceDescription volumeCreate(subscriptionId, apiVersion, resourceGroupName, volumeResourceName, volumeResourceDescription)

Creates or updates a volume resource.

Creates a volume resource with the specified name, description and properties. If a volume resource with the same name exists, then it is updated with the specified description and properties.

### Example

```javascript
import SeaBreezeManagementClient from 'sea_breeze_management_client';
let defaultClient = SeaBreezeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeaBreezeManagementClient.VolumesApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
let apiVersion = "'2018-09-01-preview'"; // String | The version of the API. This parameter is required and its value must be `2018-09-01-preview`.
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let volumeResourceName = "volumeResourceName_example"; // String | The identity of the volume.
let volumeResourceDescription = new SeaBreezeManagementClient.VolumeResourceDescription(); // VolumeResourceDescription | Description for creating a Volume resource.
apiInstance.volumeCreate(subscriptionId, apiVersion, resourceGroupName, volumeResourceName, volumeResourceDescription, (error, data, response) => {
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
 **subscriptionId** | **String**| The customer subscription identifier | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;. | [default to &#39;2018-09-01-preview&#39;]
 **resourceGroupName** | **String**| Azure resource group name | 
 **volumeResourceName** | **String**| The identity of the volume. | 
 **volumeResourceDescription** | [**VolumeResourceDescription**](VolumeResourceDescription.md)| Description for creating a Volume resource. | 

### Return type

[**VolumeResourceDescription**](VolumeResourceDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## volumeDelete

> volumeDelete(subscriptionId, apiVersion, resourceGroupName, volumeResourceName)

Deletes the volume resource.

Deletes the volume resource identified by the name.

### Example

```javascript
import SeaBreezeManagementClient from 'sea_breeze_management_client';
let defaultClient = SeaBreezeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeaBreezeManagementClient.VolumesApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
let apiVersion = "'2018-09-01-preview'"; // String | The version of the API. This parameter is required and its value must be `2018-09-01-preview`.
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let volumeResourceName = "volumeResourceName_example"; // String | The identity of the volume.
apiInstance.volumeDelete(subscriptionId, apiVersion, resourceGroupName, volumeResourceName, (error, data, response) => {
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
 **subscriptionId** | **String**| The customer subscription identifier | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;. | [default to &#39;2018-09-01-preview&#39;]
 **resourceGroupName** | **String**| Azure resource group name | 
 **volumeResourceName** | **String**| The identity of the volume. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## volumeGet

> VolumeResourceDescription volumeGet(subscriptionId, apiVersion, resourceGroupName, volumeResourceName)

Gets the volume resource with the given name.

Gets the information about the volume resource with the given name. The information include the description and other properties of the volume.

### Example

```javascript
import SeaBreezeManagementClient from 'sea_breeze_management_client';
let defaultClient = SeaBreezeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeaBreezeManagementClient.VolumesApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
let apiVersion = "'2018-09-01-preview'"; // String | The version of the API. This parameter is required and its value must be `2018-09-01-preview`.
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let volumeResourceName = "volumeResourceName_example"; // String | The identity of the volume.
apiInstance.volumeGet(subscriptionId, apiVersion, resourceGroupName, volumeResourceName, (error, data, response) => {
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
 **subscriptionId** | **String**| The customer subscription identifier | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;. | [default to &#39;2018-09-01-preview&#39;]
 **resourceGroupName** | **String**| Azure resource group name | 
 **volumeResourceName** | **String**| The identity of the volume. | 

### Return type

[**VolumeResourceDescription**](VolumeResourceDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## volumeListByResourceGroup

> VolumeResourceDescriptionList volumeListByResourceGroup(subscriptionId, apiVersion, resourceGroupName)

Gets all the volume resources in a given resource group.

Gets the information about all volume resources in a given resource group. The information include the description and other properties of the Volume.

### Example

```javascript
import SeaBreezeManagementClient from 'sea_breeze_management_client';
let defaultClient = SeaBreezeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeaBreezeManagementClient.VolumesApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
let apiVersion = "'2018-09-01-preview'"; // String | The version of the API. This parameter is required and its value must be `2018-09-01-preview`.
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
apiInstance.volumeListByResourceGroup(subscriptionId, apiVersion, resourceGroupName, (error, data, response) => {
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
 **subscriptionId** | **String**| The customer subscription identifier | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;. | [default to &#39;2018-09-01-preview&#39;]
 **resourceGroupName** | **String**| Azure resource group name | 

### Return type

[**VolumeResourceDescriptionList**](VolumeResourceDescriptionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## volumeListBySubscription

> VolumeResourceDescriptionList volumeListBySubscription(subscriptionId, apiVersion)

Gets all the volume resources in a given subscription.

Gets the information about all volume resources in a given resource group. The information include the description and other properties of the volume.

### Example

```javascript
import SeaBreezeManagementClient from 'sea_breeze_management_client';
let defaultClient = SeaBreezeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeaBreezeManagementClient.VolumesApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
let apiVersion = "'2018-09-01-preview'"; // String | The version of the API. This parameter is required and its value must be `2018-09-01-preview`.
apiInstance.volumeListBySubscription(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The customer subscription identifier | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;. | [default to &#39;2018-09-01-preview&#39;]

### Return type

[**VolumeResourceDescriptionList**](VolumeResourceDescriptionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

