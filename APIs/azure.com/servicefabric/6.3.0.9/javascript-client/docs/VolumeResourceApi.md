# ServiceFabricClientApis.VolumeResourceApi

All URIs are relative to *http://azure.local:19080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createVolumeResource**](VolumeResourceApi.md#createVolumeResource) | **PUT** /Resources/Volumes/{volumeResourceName} | Creates or updates a volume resource.
[**deleteVolumeResource**](VolumeResourceApi.md#deleteVolumeResource) | **DELETE** /Resources/Volumes/{volumeResourceName} | Deletes the volume resource.
[**getVolumeResource**](VolumeResourceApi.md#getVolumeResource) | **GET** /Resources/Volumes/{volumeResourceName} | Gets the volume resource.



## createVolumeResource

> createVolumeResource(apiVersion, volumeResourceName, volumeResourceDescription)

Creates or updates a volume resource.

Creates a volume resource with the specified name and description. If a volume with the same name already exists, then its description is updated to the one indicated in this request.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.VolumeResourceApi();
let apiVersion = "'6.3-preview'"; // String | The version of the API. This parameter is required and its value must be '6.3-preview'.
let volumeResourceName = "volumeResourceName_example"; // String | Service Fabric volume resource name.
let volumeResourceDescription = new ServiceFabricClientApis.VolumeResourceDescription(); // VolumeResourceDescription | Description for creating a volume resource.
apiInstance.createVolumeResource(apiVersion, volumeResourceName, volumeResourceDescription, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.3-preview&#39;. | [default to &#39;6.3-preview&#39;]
 **volumeResourceName** | **String**| Service Fabric volume resource name. | 
 **volumeResourceDescription** | [**VolumeResourceDescription**](VolumeResourceDescription.md)| Description for creating a volume resource. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteVolumeResource

> deleteVolumeResource(apiVersion, volumeResourceName)

Deletes the volume resource.

Deletes the volume identified by the name.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.VolumeResourceApi();
let apiVersion = "'6.3-preview'"; // String | The version of the API. This parameter is required and its value must be '6.3-preview'.
let volumeResourceName = "volumeResourceName_example"; // String | Service Fabric volume resource name.
apiInstance.deleteVolumeResource(apiVersion, volumeResourceName, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.3-preview&#39;. | [default to &#39;6.3-preview&#39;]
 **volumeResourceName** | **String**| Service Fabric volume resource name. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVolumeResource

> VolumeResourceDescription getVolumeResource(apiVersion, volumeResourceName)

Gets the volume resource.

Gets the information about the volume resource with a given name. This information includes the volume description and other runtime information.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.VolumeResourceApi();
let apiVersion = "'6.3-preview'"; // String | The version of the API. This parameter is required and its value must be '6.3-preview'.
let volumeResourceName = "volumeResourceName_example"; // String | Service Fabric volume resource name.
apiInstance.getVolumeResource(apiVersion, volumeResourceName, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.3-preview&#39;. | [default to &#39;6.3-preview&#39;]
 **volumeResourceName** | **String**| Service Fabric volume resource name. | 

### Return type

[**VolumeResourceDescription**](VolumeResourceDescription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

