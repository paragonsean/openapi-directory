# HetznerCloudApi.VolumeActionsApi

All URIs are relative to *https://api.hetzner.cloud/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**volumesIdActionsActionIdGet**](VolumeActionsApi.md#volumesIdActionsActionIdGet) | **GET** /volumes/{id}/actions/{action_id} | Get an Action for a Volume
[**volumesIdActionsAttachPost**](VolumeActionsApi.md#volumesIdActionsAttachPost) | **POST** /volumes/{id}/actions/attach | Attach Volume to a Server
[**volumesIdActionsChangeProtectionPost**](VolumeActionsApi.md#volumesIdActionsChangeProtectionPost) | **POST** /volumes/{id}/actions/change_protection | Change Volume Protection
[**volumesIdActionsDetachPost**](VolumeActionsApi.md#volumesIdActionsDetachPost) | **POST** /volumes/{id}/actions/detach | Detach Volume
[**volumesIdActionsGet**](VolumeActionsApi.md#volumesIdActionsGet) | **GET** /volumes/{id}/actions | Get all Actions for a Volume
[**volumesIdActionsResizePost**](VolumeActionsApi.md#volumesIdActionsResizePost) | **POST** /volumes/{id}/actions/resize | Resize Volume



## volumesIdActionsActionIdGet

> ActionResponse volumesIdActionsActionIdGet(id, actionId)

Get an Action for a Volume

Returns a specific Action for a Volume.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.VolumeActionsApi();
let id = 56; // Number | ID of the Volume
let actionId = 56; // Number | ID of the Action
apiInstance.volumesIdActionsActionIdGet(id, actionId, (error, data, response) => {
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
 **actionId** | **Number**| ID of the Action | 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## volumesIdActionsAttachPost

> ActionResponse volumesIdActionsAttachPost(id, opts)

Attach Volume to a Server

Attaches a Volume to a Server. Works only if the Server is in the same Location as the Volume.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.VolumeActionsApi();
let id = 56; // Number | ID of the Volume
let opts = {
  'attachVolumeRequest': new HetznerCloudApi.AttachVolumeRequest() // AttachVolumeRequest | 
};
apiInstance.volumesIdActionsAttachPost(id, opts, (error, data, response) => {
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
 **attachVolumeRequest** | [**AttachVolumeRequest**](AttachVolumeRequest.md)|  | [optional] 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## volumesIdActionsChangeProtectionPost

> ActionResponse volumesIdActionsChangeProtectionPost(id, opts)

Change Volume Protection

Changes the protection configuration of a Volume.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.VolumeActionsApi();
let id = 56; // Number | ID of the Volume
let opts = {
  'volumesIdActionsChangeProtectionPostRequest': new HetznerCloudApi.VolumesIdActionsChangeProtectionPostRequest() // VolumesIdActionsChangeProtectionPostRequest | 
};
apiInstance.volumesIdActionsChangeProtectionPost(id, opts, (error, data, response) => {
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
 **volumesIdActionsChangeProtectionPostRequest** | [**VolumesIdActionsChangeProtectionPostRequest**](VolumesIdActionsChangeProtectionPostRequest.md)|  | [optional] 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## volumesIdActionsDetachPost

> ActionResponse volumesIdActionsDetachPost(id)

Detach Volume

Detaches a Volume from the Server it’s attached to. You may attach it to a Server again at a later time.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.VolumeActionsApi();
let id = 56; // Number | ID of the Volume
apiInstance.volumesIdActionsDetachPost(id, (error, data, response) => {
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

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## volumesIdActionsGet

> ActionsResponse volumesIdActionsGet(id, opts)

Get all Actions for a Volume

Returns all Action objects for a Volume. You can &#x60;sort&#x60; the results by using the sort URI parameter, and filter them with the &#x60;status&#x60; parameter.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.VolumeActionsApi();
let id = 56; // Number | ID of the Volume
let opts = {
  'sort': "sort_example", // String | Can be used multiple times.
  'status': "status_example" // String | Can be used multiple times, the response will contain only Actions with specified statuses
};
apiInstance.volumesIdActionsGet(id, opts, (error, data, response) => {
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
 **sort** | **String**| Can be used multiple times. | [optional] 
 **status** | **String**| Can be used multiple times, the response will contain only Actions with specified statuses | [optional] 

### Return type

[**ActionsResponse**](ActionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## volumesIdActionsResizePost

> ActionResponse volumesIdActionsResizePost(id, opts)

Resize Volume

Changes the size of a Volume. Note that downsizing a Volume is not possible.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.VolumeActionsApi();
let id = 56; // Number | ID of the Volume
let opts = {
  'volumesIdActionsResizePostRequest': new HetznerCloudApi.VolumesIdActionsResizePostRequest() // VolumesIdActionsResizePostRequest | 
};
apiInstance.volumesIdActionsResizePost(id, opts, (error, data, response) => {
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
 **volumesIdActionsResizePostRequest** | [**VolumesIdActionsResizePostRequest**](VolumesIdActionsResizePostRequest.md)|  | [optional] 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

