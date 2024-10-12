# HetznerCloudApi.ImagesApi

All URIs are relative to *https://api.hetzner.cloud/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**imagesGet**](ImagesApi.md#imagesGet) | **GET** /images | Get all Images
[**imagesIdDelete**](ImagesApi.md#imagesIdDelete) | **DELETE** /images/{id} | Delete an Image
[**imagesIdGet**](ImagesApi.md#imagesIdGet) | **GET** /images/{id} | Get an Image
[**imagesIdPut**](ImagesApi.md#imagesIdPut) | **PUT** /images/{id} | Update an Image



## imagesGet

> ImagesGet200Response imagesGet(opts)

Get all Images

Returns all Image objects. You can select specific Image types only and sort the results by using URI parameters.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.ImagesApi();
let opts = {
  'sort': "sort_example", // String | Can be used multiple times.
  'type': "type_example", // String | Can be used multiple times.
  'status': "status_example", // String | Can be used multiple times. The response will only contain Images matching the status.
  'boundTo': "boundTo_example", // String | Can be used multiple times. Server ID linked to the Image. Only available for Images of type `backup`
  'includeDeprecated': true, // Boolean | Can be used multiple times.
  'name': "name_example", // String | Can be used to filter resources by their name. The response will only contain the resources matching the specified name
  'labelSelector': "labelSelector_example", // String | Can be used to filter resources by labels. The response will only contain resources matching the label selector.
  'architecture': "architecture_example" // String | Return only Images with the given architecture.
};
apiInstance.imagesGet(opts, (error, data, response) => {
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
 **sort** | **String**| Can be used multiple times. | [optional] 
 **type** | **String**| Can be used multiple times. | [optional] 
 **status** | **String**| Can be used multiple times. The response will only contain Images matching the status. | [optional] 
 **boundTo** | **String**| Can be used multiple times. Server ID linked to the Image. Only available for Images of type &#x60;backup&#x60; | [optional] 
 **includeDeprecated** | **Boolean**| Can be used multiple times. | [optional] 
 **name** | **String**| Can be used to filter resources by their name. The response will only contain the resources matching the specified name | [optional] 
 **labelSelector** | **String**| Can be used to filter resources by labels. The response will only contain resources matching the label selector. | [optional] 
 **architecture** | **String**| Return only Images with the given architecture. | [optional] 

### Return type

[**ImagesGet200Response**](ImagesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## imagesIdDelete

> imagesIdDelete(id)

Delete an Image

Deletes an Image. Only Images of type &#x60;snapshot&#x60; and &#x60;backup&#x60; can be deleted.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.ImagesApi();
let id = 56; // Number | ID of the Image
apiInstance.imagesIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| ID of the Image | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## imagesIdGet

> ImagesIdGet200Response imagesIdGet(id)

Get an Image

Returns a specific Image object.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.ImagesApi();
let id = 56; // Number | ID of the Image
apiInstance.imagesIdGet(id, (error, data, response) => {
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
 **id** | **Number**| ID of the Image | 

### Return type

[**ImagesIdGet200Response**](ImagesIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## imagesIdPut

> ImagesIdGet200Response imagesIdPut(id, opts)

Update an Image

Updates the Image. You may change the description, convert a Backup Image to a Snapshot Image or change the Image labels. Only Images of type &#x60;snapshot&#x60; and &#x60;backup&#x60; can be updated.  Note that when updating labels, the current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body. 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.ImagesApi();
let id = 56; // Number | ID of the Image
let opts = {
  'updateImageRequest': new HetznerCloudApi.UpdateImageRequest() // UpdateImageRequest | 
};
apiInstance.imagesIdPut(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Image | 
 **updateImageRequest** | [**UpdateImageRequest**](UpdateImageRequest.md)|  | [optional] 

### Return type

[**ImagesIdGet200Response**](ImagesIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

