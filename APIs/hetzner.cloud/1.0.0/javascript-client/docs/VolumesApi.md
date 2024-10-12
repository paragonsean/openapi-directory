# HetznerCloudApi.VolumesApi

All URIs are relative to *https://api.hetzner.cloud/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**volumesGet**](VolumesApi.md#volumesGet) | **GET** /volumes | Get all Volumes
[**volumesIdDelete**](VolumesApi.md#volumesIdDelete) | **DELETE** /volumes/{id} | Delete a Volume
[**volumesIdGet**](VolumesApi.md#volumesIdGet) | **GET** /volumes/{id} | Get a Volume
[**volumesIdPut**](VolumesApi.md#volumesIdPut) | **PUT** /volumes/{id} | Update a Volume
[**volumesPost**](VolumesApi.md#volumesPost) | **POST** /volumes | Create a Volume



## volumesGet

> VolumesGet200Response volumesGet(opts)

Get all Volumes

Gets all existing Volumes that you have available.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.VolumesApi();
let opts = {
  'status': "status_example", // String | Can be used multiple times. The response will only contain Volumes matching the status.
  'sort': "sort_example", // String | Can be used multiple times.
  'name': "name_example", // String | Can be used to filter resources by their name. The response will only contain the resources matching the specified name
  'labelSelector': "labelSelector_example" // String | Can be used to filter resources by labels. The response will only contain resources matching the label selector.
};
apiInstance.volumesGet(opts, (error, data, response) => {
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
 **status** | **String**| Can be used multiple times. The response will only contain Volumes matching the status. | [optional] 
 **sort** | **String**| Can be used multiple times. | [optional] 
 **name** | **String**| Can be used to filter resources by their name. The response will only contain the resources matching the specified name | [optional] 
 **labelSelector** | **String**| Can be used to filter resources by labels. The response will only contain resources matching the label selector. | [optional] 

### Return type

[**VolumesGet200Response**](VolumesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## volumesIdDelete

> volumesIdDelete(id)

Delete a Volume

Deletes a volume. All Volume data is irreversibly destroyed. The Volume must not be attached to a Server and it must not have delete protection enabled.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.VolumesApi();
let id = "id_example"; // String | ID of the Volume
apiInstance.volumesIdDelete(id, (error, data, response) => {
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
 **id** | **String**| ID of the Volume | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## volumesIdGet

> VolumesIdGet200Response volumesIdGet(id)

Get a Volume

Gets a specific Volume object.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.VolumesApi();
let id = 56; // Number | ID of the Volume
apiInstance.volumesIdGet(id, (error, data, response) => {
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
 **id** | **Number**| ID of the Volume | 

### Return type

[**VolumesIdGet200Response**](VolumesIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## volumesIdPut

> VolumesIdGet200Response volumesIdPut(id, opts)

Update a Volume

Updates the Volume properties.  Note that when updating labels, the volume’s current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body. 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.VolumesApi();
let id = "id_example"; // String | ID of the Volume to update
let opts = {
  'updateVolumeRequest': new HetznerCloudApi.UpdateVolumeRequest() // UpdateVolumeRequest | 
};
apiInstance.volumesIdPut(id, opts, (error, data, response) => {
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
 **id** | **String**| ID of the Volume to update | 
 **updateVolumeRequest** | [**UpdateVolumeRequest**](UpdateVolumeRequest.md)|  | [optional] 

### Return type

[**VolumesIdGet200Response**](VolumesIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## volumesPost

> VolumesPost201Response volumesPost(opts)

Create a Volume

Creates a new Volume attached to a Server. If you want to create a Volume that is not attached to a Server, you need to provide the &#x60;location&#x60; key instead of &#x60;server&#x60;. This can be either the ID or the name of the Location this Volume will be created in. Note that a Volume can be attached to a Server only in the same Location as the Volume itself.  Specifying the Server during Volume creation will automatically attach the Volume to that Server after it has been initialized. In that case, the &#x60;next_actions&#x60; key in the response is an array which contains a single &#x60;attach_volume&#x60; action.  The minimum Volume size is 10GB and the maximum size is 10TB (10240GB).  A volume’s name can consist of alphanumeric characters, dashes, underscores, and dots, but has to start and end with an alphanumeric character. The total length is limited to 64 characters. Volume names must be unique per Project.  #### Call specific error codes  | Code                                | Description                                         | |-------------------------------------|-----------------------------------------------------| | &#x60;no_space_left_in_location&#x60;         | There is no volume space left in the given location | 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.VolumesApi();
let opts = {
  'createVolumeRequest': {"automount":false,"format":"xfs","labels":{"labelkey":"value"},"location":"nbg1","name":"test-database","size":42} // CreateVolumeRequest | 
};
apiInstance.volumesPost(opts, (error, data, response) => {
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
 **createVolumeRequest** | [**CreateVolumeRequest**](CreateVolumeRequest.md)|  | [optional] 

### Return type

[**VolumesPost201Response**](VolumesPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

