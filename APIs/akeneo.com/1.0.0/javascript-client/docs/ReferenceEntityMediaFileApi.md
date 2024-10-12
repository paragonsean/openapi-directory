# AkeneoPimRestApi.ReferenceEntityMediaFileApi

All URIs are relative to *http://demo.akeneo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getReferenceEntityMediaFilesCode**](ReferenceEntityMediaFileApi.md#getReferenceEntityMediaFilesCode) | **GET** /api/rest/v1/reference-entities-media-files/{code} | Download the media file associated to a reference entity or a record
[**postReferenceEntityMediaFiles**](ReferenceEntityMediaFileApi.md#postReferenceEntityMediaFiles) | **POST** /api/rest/v1/reference-entities-media-files | Create a new media file for a reference entity or a record



## getReferenceEntityMediaFilesCode

> getReferenceEntityMediaFilesCode(code)

Download the media file associated to a reference entity or a record

This endpoint allows you to download a given media file that is associated with a reference entity or a record.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.ReferenceEntityMediaFileApi();
let code = "code_example"; // String | Code of the resource
apiInstance.getReferenceEntityMediaFilesCode(code, (error, data, response) => {
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
 **code** | **String**| Code of the resource | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## postReferenceEntityMediaFiles

> postReferenceEntityMediaFiles(contentType, opts)

Create a new media file for a reference entity or a record

This endpoint allows you to create a new media file and associate it to the image of a reference entity, or to the main image or to an attribute value of a record.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.ReferenceEntityMediaFileApi();
let contentType = "contentType_example"; // String | Equal to 'multipart/form-data', no other value allowed
let opts = {
  'body': new AkeneoPimRestApi.PostAssetMediaFilesRequest() // PostAssetMediaFilesRequest | 
};
apiInstance.postReferenceEntityMediaFiles(contentType, opts, (error, data, response) => {
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
 **contentType** | **String**| Equal to &#39;multipart/form-data&#39;, no other value allowed | 
 **body** | [**PostAssetMediaFilesRequest**](PostAssetMediaFilesRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message, _links

