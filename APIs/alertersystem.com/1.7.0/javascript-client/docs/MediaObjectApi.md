# AlerterSystemApi.MediaObjectApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiMediaObjectGetCollection**](MediaObjectApi.md#apiMediaObjectGetCollection) | **GET** /api/media-object | Retrieves the collection of MediaObject resources.
[**apiMediaObjectIdDelete**](MediaObjectApi.md#apiMediaObjectIdDelete) | **DELETE** /api/media-object/{id} | Removes the MediaObject resource.
[**apiMediaObjectIdGet**](MediaObjectApi.md#apiMediaObjectIdGet) | **GET** /api/media-object/{id} | Retrieves a MediaObject resource.
[**apiMediaObjectPost**](MediaObjectApi.md#apiMediaObjectPost) | **POST** /api/media-object | Creates a MediaObject resource.



## apiMediaObjectGetCollection

> [MediaObjectGet] apiMediaObjectGetCollection(opts)

Retrieves the collection of MediaObject resources.

Retrieves the collection of MediaObject resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.MediaObjectApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiMediaObjectGetCollection(opts, (error, data, response) => {
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
 **page** | **Number**| The collection page number | [optional] [default to 1]
 **dataSegmentCode** | **String**|  | [optional] 
 **dataSegmentCode2** | [**[String]**](String.md)|  | [optional] 
 **partition** | **String**|  | [optional] 
 **partition2** | [**[String]**](String.md)|  | [optional] 
 **properties** | [**[String]**](String.md)| Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]&#x3D;{propertyName}&amp;properties[]&#x3D;{anotherPropertyName}&amp;properties[{nestedPropertyParent}][]&#x3D;{nestedProperty} | [optional] 

### Return type

[**[MediaObjectGet]**](MediaObjectGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiMediaObjectIdDelete

> apiMediaObjectIdDelete(id)

Removes the MediaObject resource.

Removes the MediaObject resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.MediaObjectApi();
let id = "id_example"; // String | MediaObject identifier
apiInstance.apiMediaObjectIdDelete(id, (error, data, response) => {
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
 **id** | **String**| MediaObject identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiMediaObjectIdGet

> MediaObjectGet apiMediaObjectIdGet(id)

Retrieves a MediaObject resource.

Retrieves a MediaObject resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.MediaObjectApi();
let id = "id_example"; // String | MediaObject identifier
apiInstance.apiMediaObjectIdGet(id, (error, data, response) => {
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
 **id** | **String**| MediaObject identifier | 

### Return type

[**MediaObjectGet**](MediaObjectGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiMediaObjectPost

> MediaObjectGet apiMediaObjectPost(opts)

Creates a MediaObject resource.

Creates a MediaObject resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.MediaObjectApi();
let opts = {
  'dataSegmentCode': "dataSegmentCode_example", // String | User-provided string on which to segment and filter data. Max 50 characters.
  'file': "/path/to/file", // File | 
  'keywords': "keywords_example", // String | A string of keywords that can be used to search for a resource. Max 100 characters.
  'partition': "partition_example" // String | The unique id of the partition. Can be just the id or an IRI.
};
apiInstance.apiMediaObjectPost(opts, (error, data, response) => {
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
 **dataSegmentCode** | **String**| User-provided string on which to segment and filter data. Max 50 characters. | [optional] 
 **file** | **File**|  | [optional] 
 **keywords** | **String**| A string of keywords that can be used to search for a resource. Max 100 characters. | [optional] 
 **partition** | **String**| The unique id of the partition. Can be just the id or an IRI. | [optional] 

### Return type

[**MediaObjectGet**](MediaObjectGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json, application/ld+json, text/html

