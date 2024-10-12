# RemoteSettingsProd.AttachmentApi

All URIs are relative to *https://firefox.settings.services.mozilla.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createAttachment**](AttachmentApi.md#createAttachment) | **POST** /buckets/{bucket_id}/collections/{collection_id}/records/{id}/attachment | 
[**deleteAttachment**](AttachmentApi.md#deleteAttachment) | **DELETE** /buckets/{bucket_id}/collections/{collection_id}/records/{id}/attachment | 



## createAttachment

> createAttachment(bucketId, collectionId, id)



### Example

```javascript
import RemoteSettingsProd from 'remote_settings_prod';

let apiInstance = new RemoteSettingsProd.AttachmentApi();
let bucketId = "bucketId_example"; // String | 
let collectionId = "collectionId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.createAttachment(bucketId, collectionId, id, (error, data, response) => {
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
 **bucketId** | **String**|  | 
 **collectionId** | **String**|  | 
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteAttachment

> deleteAttachment(bucketId, collectionId, id)



### Example

```javascript
import RemoteSettingsProd from 'remote_settings_prod';

let apiInstance = new RemoteSettingsProd.AttachmentApi();
let bucketId = "bucketId_example"; // String | 
let collectionId = "collectionId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.deleteAttachment(bucketId, collectionId, id, (error, data, response) => {
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
 **bucketId** | **String**|  | 
 **collectionId** | **String**|  | 
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

