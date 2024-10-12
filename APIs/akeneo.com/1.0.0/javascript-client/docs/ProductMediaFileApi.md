# AkeneoPimRestApi.ProductMediaFileApi

All URIs are relative to *http://demo.akeneo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getMediaFiles**](ProductMediaFileApi.md#getMediaFiles) | **GET** /api/rest/v1/media-files | Get a list of product media files
[**getMediaFilesCode**](ProductMediaFileApi.md#getMediaFilesCode) | **GET** /api/rest/v1/media-files/{code} | Get a product media file
[**getMediaFilesCodeDownload**](ProductMediaFileApi.md#getMediaFilesCodeDownload) | **GET** /api/rest/v1/media-files/{code}/download | Download a product media file
[**postMediaFiles**](ProductMediaFileApi.md#postMediaFiles) | **POST** /api/rest/v1/media-files | Create a new product media file



## getMediaFiles

> MediaFiles getMediaFiles(opts)

Get a list of product media files

This endpoint allows you to get a list of media files that are used as attribute values in products or product models.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.ProductMediaFileApi();
let opts = {
  'page': 1, // Number | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section
  'limit': 10, // Number | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section
  'withCount': false // Boolean | Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
};
apiInstance.getMediaFiles(opts, (error, data, response) => {
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
 **page** | **Number**| Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 1]
 **limit** | **Number**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 10]
 **withCount** | **Boolean**| Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way | [optional] [default to false]

### Return type

[**MediaFiles**](MediaFiles.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, _embedded, _links, current_page, code, message


## getMediaFilesCode

> GetMediaFilesCode200Response getMediaFilesCode(code)

Get a product media file

This endpoint allows you to get the information about a given media file that is used as an attribute value of a product or a product model.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.ProductMediaFileApi();
let code = "code_example"; // String | Code of the resource
apiInstance.getMediaFilesCode(code, (error, data, response) => {
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
 **code** | **String**| Code of the resource | 

### Return type

[**GetMediaFilesCode200Response**](GetMediaFilesCode200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## getMediaFilesCodeDownload

> getMediaFilesCodeDownload(code)

Download a product media file

This endpoint allows you to download a given media file that is used as an attribute value of a product or a product model.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.ProductMediaFileApi();
let code = "code_example"; // String | Code of the resource
apiInstance.getMediaFilesCodeDownload(code, (error, data, response) => {
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


## postMediaFiles

> postMediaFiles(contentType, opts)

Create a new product media file

This endpoint allows you to create a new media file and associate it to an attribute value of a given product or product model.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.ProductMediaFileApi();
let contentType = "contentType_example"; // String | Equal to 'multipart/form-data', no other value allowed
let opts = {
  'body': new AkeneoPimRestApi.PostMediaFilesRequest() // PostMediaFilesRequest | 
};
apiInstance.postMediaFiles(contentType, opts, (error, data, response) => {
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
 **body** | [**PostMediaFilesRequest**](PostMediaFilesRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message, _links

