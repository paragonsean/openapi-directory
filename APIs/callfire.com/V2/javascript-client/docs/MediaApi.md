# CallFireApiDocumentation.MediaApi

All URIs are relative to *https://api.callfire.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createMedia**](MediaApi.md#createMedia) | **POST** /media | Create media
[**findMedia**](MediaApi.md#findMedia) | **GET** /media | Find media
[**getMedia**](MediaApi.md#getMedia) | **GET** /media/{id} | Get a specific media
[**getMediaData**](MediaApi.md#getMediaData) | **GET** /media/{id}.{extension} | Download media by extension
[**getMediaDataBinary**](MediaApi.md#getMediaDataBinary) | **GET** /media/{id}/file | Download a MP3 media
[**getMediaDataByKey**](MediaApi.md#getMediaDataByKey) | **GET** /media/public/{key}.{extension} | Download media by extension



## createMedia

> ResourceId createMedia(file, opts)

Create media

Uploads media file to account, acceptable media formats: bmp, gif, jpg, m4a, mp3, mp4, png, wav

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.MediaApi();
let file = "/path/to/file"; // File | Binary media file
let opts = {
  'name': "name_example" // String | A name of a media file
};
apiInstance.createMedia(file, opts, (error, data, response) => {
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
 **file** | **File**| Binary media file | 
 **name** | **String**| A name of a media file | [optional] 

### Return type

[**ResourceId**](ResourceId.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## findMedia

> MediaPage findMedia(opts)

Find media

Find media files created by user

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.MediaApi();
let opts = {
  'limit': 100, // Number | To set the maximum number of records to return in a paged list response. The default is 100
  'offset': 0, // Number | Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
  'filter': "filter_example", // String | value to filter file names again; this value is used to check if the filename contains the filter value.
  'fields': "fields_example" // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
};
apiInstance.findMedia(opts, (error, data, response) => {
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
 **limit** | **Number**| To set the maximum number of records to return in a paged list response. The default is 100 | [optional] [default to 100]
 **offset** | **Number**| Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API. | [optional] [default to 0]
 **filter** | **String**| value to filter file names again; this value is used to check if the filename contains the filter value. | [optional] 
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 

### Return type

[**MediaPage**](MediaPage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMedia

> Media getMedia(id, opts)

Get a specific media

Get media resource by id

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.MediaApi();
let id = 789; // Number | An id of a media resource
let opts = {
  'fields': "fields_example" // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
};
apiInstance.getMedia(id, opts, (error, data, response) => {
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
 **id** | **Number**| An id of a media resource | 
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 

### Return type

[**Media**](Media.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMediaData

> Object getMediaData(id, extension)

Download media by extension

Download a media file. Available types of files: bmp, gif, jpg, m4a, mp3, mp4, png, wav. Content type in response depends on &#39;extension&#39; parameter, e.g. image/jpeg, image/png, audio/mp3, etc

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.MediaApi();
let id = 789; // Number | An id of a media resource
let extension = "extension_example"; // String | Media file type. Available types: bmp, gif, jpg, m4a, mp3, mp4, png, wav
apiInstance.getMediaData(id, extension, (error, data, response) => {
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
 **id** | **Number**| An id of a media resource | 
 **extension** | **String**| Media file type. Available types: bmp, gif, jpg, m4a, mp3, mp4, png, wav | 

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: audio/m4a, audio/mp3, audio/wav, image/gif, image/jpeg, image/png, image/x-bmp, video/3gpp, video/mp4


## getMediaDataBinary

> Object getMediaDataBinary(id)

Download a MP3 media

Download a MP3 media, endpoint returns application/binary content-type

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.MediaApi();
let id = 789; // Number | An id of a media resource
apiInstance.getMediaDataBinary(id, (error, data, response) => {
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
 **id** | **Number**| An id of a media resource | 

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/binary


## getMediaDataByKey

> Object getMediaDataByKey(key, extension)

Download media by extension

Download a media file. Available types of files: bmp, gif, jpg, m4a, mp3, mp4, png, wav. Content type in response depends on &#39;extension&#39; parameter, e.g. image/jpeg, image/png, audio/mp3, etc

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.MediaApi();
let key = "key_example"; // String | A hash-key of a media resource
let extension = "extension_example"; // String | Media file type, available types: bmp, gif, jpg, m4a, mp3, mp4, png, wav
apiInstance.getMediaDataByKey(key, extension, (error, data, response) => {
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
 **key** | **String**| A hash-key of a media resource | 
 **extension** | **String**| Media file type, available types: bmp, gif, jpg, m4a, mp3, mp4, png, wav | 

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: audio/m4a, audio/mp3, audio/wav, image/gif, image/jpeg, image/png, image/x-bmp, video/3gpp, video/mp4

