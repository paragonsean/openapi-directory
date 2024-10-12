# LinodeApi.VolumesApi

All URIs are relative to *https://api.linode.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attachVolume**](VolumesApi.md#attachVolume) | **POST** /volumes/{volumeId}/attach | Volume Attach
[**cloneVolume**](VolumesApi.md#cloneVolume) | **POST** /volumes/{volumeId}/clone | Volume Clone
[**createVolume**](VolumesApi.md#createVolume) | **POST** /volumes | Volume Create
[**deleteVolume**](VolumesApi.md#deleteVolume) | **DELETE** /volumes/{volumeId} | Volume Delete
[**detachVolume**](VolumesApi.md#detachVolume) | **POST** /volumes/{volumeId}/detach | Volume Detach
[**getVolume**](VolumesApi.md#getVolume) | **GET** /volumes/{volumeId} | Volume View
[**getVolumes**](VolumesApi.md#getVolumes) | **GET** /volumes | Volumes List
[**resizeVolume**](VolumesApi.md#resizeVolume) | **POST** /volumes/{volumeId}/resize | Volume Resize
[**updateVolume**](VolumesApi.md#updateVolume) | **PUT** /volumes/{volumeId} | Volume Update



## attachVolume

> Volume attachVolume(volumeId, attachVolumeRequest)

Volume Attach

Attaches a Volume on your Account to an existing Linode on your Account. In order for this request to complete successfully, your User must have &#x60;read_only&#x60; or &#x60;read_write&#x60; permission to the Volume and &#x60;read_write&#x60; permission to the Linode. Additionally, the Volume and Linode must be located in the same Region. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.VolumesApi();
let volumeId = 56; // Number | ID of the Volume to attach.
let attachVolumeRequest = new LinodeApi.AttachVolumeRequest(); // AttachVolumeRequest | Volume to attach to a Linode.
apiInstance.attachVolume(volumeId, attachVolumeRequest, (error, data, response) => {
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
 **volumeId** | **Number**| ID of the Volume to attach. | 
 **attachVolumeRequest** | [**AttachVolumeRequest**](AttachVolumeRequest.md)| Volume to attach to a Linode. | 

### Return type

[**Volume**](Volume.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cloneVolume

> Volume cloneVolume(volumeId, cloneVolumeRequest)

Volume Clone

Creates a Volume on your Account. In order for this request to complete successfully, your User must have the &#x60;add_volumes&#x60; grant. The new Volume will have the same size and data as the source Volume. Creating a new Volume will incur a charge on your Account. * Only Volumes with a &#x60;status&#x60; of \&quot;active\&quot; can be cloned. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.VolumesApi();
let volumeId = 56; // Number | ID of the Volume to clone.
let cloneVolumeRequest = new LinodeApi.CloneVolumeRequest(); // CloneVolumeRequest | The requested state your Volume will be cloned into.
apiInstance.cloneVolume(volumeId, cloneVolumeRequest, (error, data, response) => {
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
 **volumeId** | **Number**| ID of the Volume to clone. | 
 **cloneVolumeRequest** | [**CloneVolumeRequest**](CloneVolumeRequest.md)| The requested state your Volume will be cloned into. | 

### Return type

[**Volume**](Volume.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createVolume

> Volume createVolume(createVolumeRequest)

Volume Create

Creates a Volume on your Account. In order for this to complete successfully, your User must have the &#x60;add_volumes&#x60; grant. Creating a new Volume will start accruing additional charges on your account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.VolumesApi();
let createVolumeRequest = new LinodeApi.CreateVolumeRequest(); // CreateVolumeRequest | The requested initial state of a new Volume.
apiInstance.createVolume(createVolumeRequest, (error, data, response) => {
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
 **createVolumeRequest** | [**CreateVolumeRequest**](CreateVolumeRequest.md)| The requested initial state of a new Volume. | 

### Return type

[**Volume**](Volume.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteVolume

> Object deleteVolume(volumeId)

Volume Delete

Deletes a Volume you have permission to &#x60;read_write&#x60;.  * **Deleting a Volume is a destructive action and cannot be undone.**  * Deleting stops billing for the Volume. You will be billed for time used within the billing period the Volume was active.  * Volumes that are migrating cannot be deleted until the migration is finished. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.VolumesApi();
let volumeId = 56; // Number | ID of the Volume to look up.
apiInstance.deleteVolume(volumeId, (error, data, response) => {
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
 **volumeId** | **Number**| ID of the Volume to look up. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## detachVolume

> Object detachVolume(volumeId)

Volume Detach

Detaches a Volume on your Account from a Linode on your Account. In order for this request to complete successfully, your User must have &#x60;read_write&#x60; access to the Volume and &#x60;read_write&#x60; access to the Linode. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.VolumesApi();
let volumeId = 56; // Number | ID of the Volume to detach.
apiInstance.detachVolume(volumeId, (error, data, response) => {
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
 **volumeId** | **Number**| ID of the Volume to detach. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVolume

> Volume getVolume(volumeId, opts)

Volume View

Get information about a single Volume. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.VolumesApi();
let volumeId = 56; // Number | ID of the Volume to look up.
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getVolume(volumeId, opts, (error, data, response) => {
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
 **volumeId** | **Number**| ID of the Volume to look up. | 
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**Volume**](Volume.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVolumes

> GetLinodeVolumes200Response getVolumes(opts)

Volumes List

Returns a paginated list of Volumes you have permission to view. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.VolumesApi();
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getVolumes(opts, (error, data, response) => {
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
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetLinodeVolumes200Response**](GetLinodeVolumes200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resizeVolume

> Volume resizeVolume(volumeId, resizeVolumeRequest)

Volume Resize

Resize an existing Volume on your Account. In order for this request to complete successfully, your User must have the &#x60;read_write&#x60; permissions to the Volume. * Volumes can only be resized up. * Only Volumes with a &#x60;status&#x60; of \&quot;active\&quot; can be resized. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.VolumesApi();
let volumeId = 56; // Number | ID of the Volume to resize.
let resizeVolumeRequest = new LinodeApi.ResizeVolumeRequest(); // ResizeVolumeRequest | The requested size to increase your Volume to.
apiInstance.resizeVolume(volumeId, resizeVolumeRequest, (error, data, response) => {
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
 **volumeId** | **Number**| ID of the Volume to resize. | 
 **resizeVolumeRequest** | [**ResizeVolumeRequest**](ResizeVolumeRequest.md)| The requested size to increase your Volume to. | 

### Return type

[**Volume**](Volume.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateVolume

> Volume updateVolume(volumeId, updateVolumeRequest)

Volume Update

Updates a Volume that you have permission to &#x60;read_write&#x60;. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.VolumesApi();
let volumeId = 56; // Number | ID of the Volume to look up.
let updateVolumeRequest = new LinodeApi.UpdateVolumeRequest(); // UpdateVolumeRequest | If any updated field fails to pass validation, the Volume will not be updated. 
apiInstance.updateVolume(volumeId, updateVolumeRequest, (error, data, response) => {
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
 **volumeId** | **Number**| ID of the Volume to look up. | 
 **updateVolumeRequest** | [**UpdateVolumeRequest**](UpdateVolumeRequest.md)| If any updated field fails to pass validation, the Volume will not be updated.  | 

### Return type

[**Volume**](Volume.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

