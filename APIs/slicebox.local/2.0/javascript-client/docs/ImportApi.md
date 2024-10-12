# SliceboxApi.ImportApi

All URIs are relative to *http://slicebox.local/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**importSessionsGet**](ImportApi.md#importSessionsGet) | **GET** /import/sessions | 
[**importSessionsIdDelete**](ImportApi.md#importSessionsIdDelete) | **DELETE** /import/sessions/{id} | 
[**importSessionsIdGet**](ImportApi.md#importSessionsIdGet) | **GET** /import/sessions/{id} | 
[**importSessionsIdImagesGet**](ImportApi.md#importSessionsIdImagesGet) | **GET** /import/sessions/{id}/images | 
[**importSessionsIdImagesPost**](ImportApi.md#importSessionsIdImagesPost) | **POST** /import/sessions/{id}/images | 
[**importSessionsPost**](ImportApi.md#importSessionsPost) | **POST** /import/sessions | 



## importSessionsGet

> [ImportSession] importSessionsGet(opts)



Returns a list of available import sessions.

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.ImportApi();
let opts = {
  'startindex': 0, // Number | start index of returned slice of import sessions
  'count': 20 // Number | size of returned slice of import sessions
};
apiInstance.importSessionsGet(opts, (error, data, response) => {
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
 **startindex** | **Number**| start index of returned slice of import sessions | [optional] [default to 0]
 **count** | **Number**| size of returned slice of import sessions | [optional] [default to 20]

### Return type

[**[ImportSession]**](ImportSession.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## importSessionsIdDelete

> importSessionsIdDelete(id)



deletes the import session with the supplied ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.ImportApi();
let id = 789; // Number | ID of import session to delete
apiInstance.importSessionsIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| ID of import session to delete | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## importSessionsIdGet

> ImportSession importSessionsIdGet(id)



Returns the import sessions with the supplied ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.ImportApi();
let id = 789; // Number | ID of session
apiInstance.importSessionsIdGet(id, (error, data, response) => {
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
 **id** | **Number**| ID of session | 

### Return type

[**ImportSession**](ImportSession.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## importSessionsIdImagesGet

> [Image] importSessionsIdImagesGet(id)



get the imported images corresponding to the import session with the supplied ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.ImportApi();
let id = 789; // Number | ID of import session
apiInstance.importSessionsIdImagesGet(id, (error, data, response) => {
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
 **id** | **Number**| ID of import session | 

### Return type

[**[Image]**](Image.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## importSessionsIdImagesPost

> Image importSessionsIdImagesPost(id, imagesPostRequest)



add a DICOM dataset to the import session with the supplied ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.ImportApi();
let id = 789; // Number | ID of session
let imagesPostRequest = new SliceboxApi.ImagesPostRequest(); // ImagesPostRequest | 
apiInstance.importSessionsIdImagesPost(id, imagesPostRequest, (error, data, response) => {
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
 **id** | **Number**| ID of session | 
 **imagesPostRequest** | [**ImagesPostRequest**](ImagesPostRequest.md)|  | 

### Return type

[**Image**](Image.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/octet-stream, multipart/form-data
- **Accept**: application/json, application/octet-stream


## importSessionsPost

> ImportSession importSessionsPost(importSession)



create a new import sessions

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.ImportApi();
let importSession = new SliceboxApi.ImportSession(); // ImportSession | The import session to create containing the user defined name of the session
apiInstance.importSessionsPost(importSession, (error, data, response) => {
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
 **importSession** | [**ImportSession**](ImportSession.md)| The import session to create containing the user defined name of the session | 

### Return type

[**ImportSession**](ImportSession.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/octet-stream, multipart/form-data
- **Accept**: application/json, application/octet-stream

