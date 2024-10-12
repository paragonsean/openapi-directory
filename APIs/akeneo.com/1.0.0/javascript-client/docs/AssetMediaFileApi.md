# AkeneoPimRestApi.AssetMediaFileApi

All URIs are relative to *http://demo.akeneo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAssetMediaFilesCode**](AssetMediaFileApi.md#getAssetMediaFilesCode) | **GET** /api/rest/v1/asset-media-files/{code} | Download the media file associated to an asset
[**postAssetMediaFiles**](AssetMediaFileApi.md#postAssetMediaFiles) | **POST** /api/rest/v1/asset-media-files | Create a new media file for an asset



## getAssetMediaFilesCode

> getAssetMediaFilesCode(code)

Download the media file associated to an asset

This endpoint allows you to download a given media file that is associated with an asset.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.AssetMediaFileApi();
let code = "code_example"; // String | Code of the resource
apiInstance.getAssetMediaFilesCode(code, (error, data, response) => {
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


## postAssetMediaFiles

> postAssetMediaFiles(contentType, opts)

Create a new media file for an asset

This endpoint allows you to create a new media file and associate it to a media file attribute value of an asset.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.AssetMediaFileApi();
let contentType = "contentType_example"; // String | Equal to 'multipart/form-data', no other value allowed
let opts = {
  'body': new AkeneoPimRestApi.PostAssetMediaFilesRequest() // PostAssetMediaFilesRequest | 
};
apiInstance.postAssetMediaFiles(contentType, opts, (error, data, response) => {
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

