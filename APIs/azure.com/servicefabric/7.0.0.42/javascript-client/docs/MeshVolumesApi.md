# ServiceFabricClientApis.MeshVolumesApi

All URIs are relative to *http://azure.local:19080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**meshVolumeCreateOrUpdate**](MeshVolumesApi.md#meshVolumeCreateOrUpdate) | **PUT** /Resources/Volumes/{volumeResourceName} | Creates or updates a Volume resource.
[**meshVolumeDelete**](MeshVolumesApi.md#meshVolumeDelete) | **DELETE** /Resources/Volumes/{volumeResourceName} | Deletes the Volume resource.
[**meshVolumeGet**](MeshVolumesApi.md#meshVolumeGet) | **GET** /Resources/Volumes/{volumeResourceName} | Gets the Volume resource with the given name.
[**meshVolumeList**](MeshVolumesApi.md#meshVolumeList) | **GET** /Resources/Volumes | Lists all the volume resources.



## meshVolumeCreateOrUpdate

> VolumeResourceDescription meshVolumeCreateOrUpdate(apiVersion, volumeResourceName, volumeResourceDescription)

Creates or updates a Volume resource.

Creates a Volume resource with the specified name, description and properties. If Volume resource with the same name exists, then it is updated with the specified description and properties.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.MeshVolumesApi();
let apiVersion = "'6.4-preview'"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
let volumeResourceName = "volumeResourceName_example"; // String | The identity of the volume.
let volumeResourceDescription = new ServiceFabricClientApis.VolumeResourceDescription(); // VolumeResourceDescription | Description for creating a Volume resource.
apiInstance.meshVolumeCreateOrUpdate(apiVersion, volumeResourceName, volumeResourceDescription, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;. | [default to &#39;6.4-preview&#39;]
 **volumeResourceName** | **String**| The identity of the volume. | 
 **volumeResourceDescription** | [**VolumeResourceDescription**](VolumeResourceDescription.md)| Description for creating a Volume resource. | 

### Return type

[**VolumeResourceDescription**](VolumeResourceDescription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## meshVolumeDelete

> meshVolumeDelete(apiVersion, volumeResourceName)

Deletes the Volume resource.

Deletes the Volume resource identified by the name.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.MeshVolumesApi();
let apiVersion = "'6.4-preview'"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
let volumeResourceName = "volumeResourceName_example"; // String | The identity of the volume.
apiInstance.meshVolumeDelete(apiVersion, volumeResourceName, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;. | [default to &#39;6.4-preview&#39;]
 **volumeResourceName** | **String**| The identity of the volume. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## meshVolumeGet

> VolumeResourceDescription meshVolumeGet(apiVersion, volumeResourceName)

Gets the Volume resource with the given name.

Gets the information about the Volume resource with the given name. The information include the description and other properties of the Volume.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.MeshVolumesApi();
let apiVersion = "'6.4-preview'"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
let volumeResourceName = "volumeResourceName_example"; // String | The identity of the volume.
apiInstance.meshVolumeGet(apiVersion, volumeResourceName, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;. | [default to &#39;6.4-preview&#39;]
 **volumeResourceName** | **String**| The identity of the volume. | 

### Return type

[**VolumeResourceDescription**](VolumeResourceDescription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## meshVolumeList

> PagedVolumeResourceDescriptionList meshVolumeList(apiVersion)

Lists all the volume resources.

Gets the information about all volume resources in a given resource group. The information include the description and other properties of the Volume.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.MeshVolumesApi();
let apiVersion = "'6.4-preview'"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
apiInstance.meshVolumeList(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;. | [default to &#39;6.4-preview&#39;]

### Return type

[**PagedVolumeResourceDescriptionList**](PagedVolumeResourceDescriptionList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

