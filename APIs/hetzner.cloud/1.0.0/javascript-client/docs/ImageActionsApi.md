# HetznerCloudApi.ImageActionsApi

All URIs are relative to *https://api.hetzner.cloud/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**imagesIdActionsActionIdGet**](ImageActionsApi.md#imagesIdActionsActionIdGet) | **GET** /images/{id}/actions/{action_id} | Get an Action for an Image
[**imagesIdActionsChangeProtectionPost**](ImageActionsApi.md#imagesIdActionsChangeProtectionPost) | **POST** /images/{id}/actions/change_protection | Change Image Protection
[**imagesIdActionsGet**](ImageActionsApi.md#imagesIdActionsGet) | **GET** /images/{id}/actions | Get all Actions for an Image



## imagesIdActionsActionIdGet

> ActionResponse imagesIdActionsActionIdGet(id, actionId)

Get an Action for an Image

Returns a specific Action for an Image.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.ImageActionsApi();
let id = 56; // Number | ID of the Image
let actionId = 56; // Number | ID of the Action
apiInstance.imagesIdActionsActionIdGet(id, actionId, (error, data, response) => {
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
 **actionId** | **Number**| ID of the Action | 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## imagesIdActionsChangeProtectionPost

> ActionResponse imagesIdActionsChangeProtectionPost(id, opts)

Change Image Protection

Changes the protection configuration of the Image. Can only be used on snapshots.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.ImageActionsApi();
let id = 56; // Number | ID of the Image
let opts = {
  'imagesIdActionsChangeProtectionPostRequest': new HetznerCloudApi.ImagesIdActionsChangeProtectionPostRequest() // ImagesIdActionsChangeProtectionPostRequest | 
};
apiInstance.imagesIdActionsChangeProtectionPost(id, opts, (error, data, response) => {
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
 **imagesIdActionsChangeProtectionPostRequest** | [**ImagesIdActionsChangeProtectionPostRequest**](ImagesIdActionsChangeProtectionPostRequest.md)|  | [optional] 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## imagesIdActionsGet

> ActionsResponse imagesIdActionsGet(id, opts)

Get all Actions for an Image

Returns all Action objects for an Image. You can sort the results by using the &#x60;sort&#x60; URI parameter, and filter them with the &#x60;status&#x60; parameter.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.ImageActionsApi();
let id = 56; // Number | ID of the Image
let opts = {
  'sort': "sort_example", // String | Can be used multiple times.
  'status': "status_example" // String | Can be used multiple times, the response will contain only Actions with specified statuses
};
apiInstance.imagesIdActionsGet(id, opts, (error, data, response) => {
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
 **sort** | **String**| Can be used multiple times. | [optional] 
 **status** | **String**| Can be used multiple times, the response will contain only Actions with specified statuses | [optional] 

### Return type

[**ActionsResponse**](ActionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

