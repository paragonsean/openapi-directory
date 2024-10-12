# VisageCloud.StreamApi

All URIs are relative to *https://visagecloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addStreamUsingPOST**](StreamApi.md#addStreamUsingPOST) | **POST** /rest/v1.1/stream/stream | Create new stream with given name
[**cleanupStreamUsingPATCH**](StreamApi.md#cleanupStreamUsingPATCH) | **PATCH** /rest/v1.1/stream/cleanup | Cleanup frames older than specified timeframe
[**getFrameImageUsingGET**](StreamApi.md#getFrameImageUsingGET) | **GET** /rest/v1.1/stream/frameImage | Get individual frame image
[**getLastNAttedanceUsingGET**](StreamApi.md#getLastNAttedanceUsingGET) | **GET** /rest/v1.1/stream/attendance | Get last N recognized individuals from stream
[**getLastNFramesUsingGET**](StreamApi.md#getLastNFramesUsingGET) | **GET** /rest/v1.1/stream/frames | Get last processed N frames from stream
[**getStreamUsingGET**](StreamApi.md#getStreamUsingGET) | **GET** /rest/v1.1/stream/{streamId} | Get an existing stream with a given ID
[**removeStreamUsingDELETE**](StreamApi.md#removeStreamUsingDELETE) | **DELETE** /rest/v1.1/stream/{id} | Delete existing stream
[**startStreamUsingPATCH**](StreamApi.md#startStreamUsingPATCH) | **PATCH** /rest/v1.1/stream/start | Start existing stream
[**stopStreamUsingPATCH**](StreamApi.md#stopStreamUsingPATCH) | **PATCH** /rest/v1.1/stream/stop | Stop existing stream
[**streamsByAccountUsingGET**](StreamApi.md#streamsByAccountUsingGET) | **GET** /rest/v1.1/stream/all | Show status of all streams from account
[**updateStreamUsingPATCH**](StreamApi.md#updateStreamUsingPATCH) | **PATCH** /rest/v1.1/stream/{streamId} | Update an existing stream with a given ID



## addStreamUsingPOST

> RestResponse addStreamUsingPOST(accessKey, secretKey, name, url, opts)

Create new stream with given name

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.StreamApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey provided by VisageCloud
let name = "name_example"; // String | The name of the stream that will be created
let url = "url_example"; // String | The url of the stream
let opts = {
  'method': "'WEBRTC_PUSH'", // String | Streaming method
  'username': "username_example", // String | Username
  'password': "password_example", // String | Password
  'skipFramesWithNoFaces': true, // Boolean | Boolean value indicating whether you want the original picture to be stored for later retrieval
  'retentionTime': 605000, // Number | Number of seconds for frames to be kept. Default is 605000s (7 days)
  'storeOriginalFrames': false, // Boolean | Boolean value indicating whether you want the original picture to be stored for later retrieval
  'storeAttendanceFaces': false, // Boolean | Boolean value indicating whether you want to store permanently store faces clippings of the recognized faces
  'storeAttendanceFrames': false, // Boolean | Boolean value indicating whether you want to store permanently store frames with a recognized face in them
  'isActive': false, // Boolean | Boolean value indicating whether the stream is currently active or not
  'associatedCollections': ["null"], // [String] | List of collection ids which will be used to measure attendance
  'attributes': "attributes_example" // String | Attributes of the stream
};
apiInstance.addStreamUsingPOST(accessKey, secretKey, name, url, opts, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey provided by VisageCloud | 
 **name** | **String**| The name of the stream that will be created | 
 **url** | **String**| The url of the stream | 
 **method** | **String**| Streaming method | [optional] [default to &#39;WEBRTC_PUSH&#39;]
 **username** | **String**| Username | [optional] 
 **password** | **String**| Password | [optional] 
 **skipFramesWithNoFaces** | **Boolean**| Boolean value indicating whether you want the original picture to be stored for later retrieval | [optional] [default to true]
 **retentionTime** | **Number**| Number of seconds for frames to be kept. Default is 605000s (7 days) | [optional] [default to 605000]
 **storeOriginalFrames** | **Boolean**| Boolean value indicating whether you want the original picture to be stored for later retrieval | [optional] [default to false]
 **storeAttendanceFaces** | **Boolean**| Boolean value indicating whether you want to store permanently store faces clippings of the recognized faces | [optional] [default to false]
 **storeAttendanceFrames** | **Boolean**| Boolean value indicating whether you want to store permanently store frames with a recognized face in them | [optional] [default to false]
 **isActive** | **Boolean**| Boolean value indicating whether the stream is currently active or not | [optional] [default to false]
 **associatedCollections** | [**[String]**](String.md)| List of collection ids which will be used to measure attendance | [optional] 
 **attributes** | **String**| Attributes of the stream | [optional] 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cleanupStreamUsingPATCH

> RestResponse cleanupStreamUsingPATCH(accessKey, secretKey, streamId, interval)

Cleanup frames older than specified timeframe

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.StreamApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey provided by VisageCloud
let streamId = "streamId_example"; // String | The id of the stream that will be stopped
let interval = 56; // Number | Frames older than interval (seconds) will be cleaned up
apiInstance.cleanupStreamUsingPATCH(accessKey, secretKey, streamId, interval, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey provided by VisageCloud | 
 **streamId** | **String**| The id of the stream that will be stopped | 
 **interval** | **Number**| Frames older than interval (seconds) will be cleaned up | 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFrameImageUsingGET

> [Blob] getFrameImageUsingGET(accessKey, secretKey, streamId, timestamp)

Get individual frame image

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.StreamApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
let streamId = "streamId_example"; // String | The id of the stream for which the frames will be retrieved
let timestamp = 789; // Number | Timestamp of frame to retrieve
apiInstance.getFrameImageUsingGET(accessKey, secretKey, streamId, timestamp, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | 
 **streamId** | **String**| The id of the stream for which the frames will be retrieved | 
 **timestamp** | **Number**| Timestamp of frame to retrieve | 

### Return type

**[Blob]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/jpeg


## getLastNAttedanceUsingGET

> RestResponse getLastNAttedanceUsingGET(accessKey, secretKey, opts)

Get last N recognized individuals from stream

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.StreamApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
let opts = {
  'streamIds': ["null"], // [String] | The id of the stream for which the frames will be retrieved
  'count': 10 // Number | How many frames to retrieve at a time
};
apiInstance.getLastNAttedanceUsingGET(accessKey, secretKey, opts, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | 
 **streamIds** | [**[String]**](String.md)| The id of the stream for which the frames will be retrieved | [optional] 
 **count** | **Number**| How many frames to retrieve at a time | [optional] [default to 10]

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLastNFramesUsingGET

> RestResponse getLastNFramesUsingGET(accessKey, secretKey, streamId, opts)

Get last processed N frames from stream

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.StreamApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
let streamId = "streamId_example"; // String | The id of the stream for which the frames will be retrieved
let opts = {
  'count': 10, // Number | How many frames to retrieve at a time
  'collectionId': "collectionId_example", // String | The collection id you want to run recognition against
  'labels': ["null"], // [String] | Labels associated with the given picture or picture URL
  'attributeFilters': ["null"] // [String] | Filters that will be applied on the recognition operation
};
apiInstance.getLastNFramesUsingGET(accessKey, secretKey, streamId, opts, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | 
 **streamId** | **String**| The id of the stream for which the frames will be retrieved | 
 **count** | **Number**| How many frames to retrieve at a time | [optional] [default to 10]
 **collectionId** | **String**| The collection id you want to run recognition against | [optional] 
 **labels** | [**[String]**](String.md)| Labels associated with the given picture or picture URL | [optional] 
 **attributeFilters** | [**[String]**](String.md)| Filters that will be applied on the recognition operation | [optional] 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStreamUsingGET

> RestResponse getStreamUsingGET(accessKey, secretKey, streamId)

Get an existing stream with a given ID

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.StreamApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey provided by VisageCloud
let streamId = "streamId_example"; // String | The id of the stream for which the data will be retrieved
apiInstance.getStreamUsingGET(accessKey, secretKey, streamId, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey provided by VisageCloud | 
 **streamId** | **String**| The id of the stream for which the data will be retrieved | 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeStreamUsingDELETE

> RestResponse removeStreamUsingDELETE(accessKey, secretKey, id)

Delete existing stream

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.StreamApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey provided by VisageCloud
let id = "id_example"; // String | The id of the stream that will be removed
apiInstance.removeStreamUsingDELETE(accessKey, secretKey, id, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey provided by VisageCloud | 
 **id** | **String**| The id of the stream that will be removed | 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## startStreamUsingPATCH

> RestResponse startStreamUsingPATCH(accessKey, secretKey, streamId)

Start existing stream

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.StreamApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey provided by VisageCloud
let streamId = "streamId_example"; // String | The id of the stream that will be started
apiInstance.startStreamUsingPATCH(accessKey, secretKey, streamId, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey provided by VisageCloud | 
 **streamId** | **String**| The id of the stream that will be started | 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## stopStreamUsingPATCH

> RestResponse stopStreamUsingPATCH(accessKey, secretKey, streamId)

Stop existing stream

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.StreamApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey provided by VisageCloud
let streamId = "streamId_example"; // String | The id of the stream that will be stopped
apiInstance.stopStreamUsingPATCH(accessKey, secretKey, streamId, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey provided by VisageCloud | 
 **streamId** | **String**| The id of the stream that will be stopped | 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## streamsByAccountUsingGET

> RestResponse streamsByAccountUsingGET(accessKey, secretKey)

Show status of all streams from account

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.StreamApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
apiInstance.streamsByAccountUsingGET(accessKey, secretKey, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateStreamUsingPATCH

> RestResponse updateStreamUsingPATCH(accessKey, secretKey, streamId, opts)

Update an existing stream with a given ID

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.StreamApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey provided by VisageCloud
let streamId = "streamId_example"; // String | The id of the stream that will be updated
let opts = {
  'name': "name_example", // String | The name of the stream that will be updated
  'url': "url_example", // String | The url of the stream
  'method': "method_example", // String | Streaming method
  'username': "username_example", // String | Username
  'password': "password_example", // String | Password
  'skipFramesWithNoFaces': true, // Boolean | Boolean value indicating whether you want the original picture to be stored for later retrieval
  'retentionTime': 56, // Number | Number of seconds for frames to be kept
  'storeOriginalFrames': true, // Boolean | Boolean value indicating whether you want the original picture to be stored for later retrieval
  'storeAttendanceFaces': true, // Boolean | Boolean value indicating whether you want to store permanently store faces clippings of the recognized faces
  'storeAttendanceFrames': true, // Boolean | Boolean value indicating whether you want to store permanently store frames with a recognized face in them
  'isActive': true, // Boolean | Boolean value indicating whether the stream is currently active or not
  'associatedCollections': ["null"], // [String] | List of collection ids which will be used to measure attendance
  'attributes': "attributes_example" // String | Attributes of the stream
};
apiInstance.updateStreamUsingPATCH(accessKey, secretKey, streamId, opts, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey provided by VisageCloud | 
 **streamId** | **String**| The id of the stream that will be updated | 
 **name** | **String**| The name of the stream that will be updated | [optional] 
 **url** | **String**| The url of the stream | [optional] 
 **method** | **String**| Streaming method | [optional] 
 **username** | **String**| Username | [optional] 
 **password** | **String**| Password | [optional] 
 **skipFramesWithNoFaces** | **Boolean**| Boolean value indicating whether you want the original picture to be stored for later retrieval | [optional] 
 **retentionTime** | **Number**| Number of seconds for frames to be kept | [optional] 
 **storeOriginalFrames** | **Boolean**| Boolean value indicating whether you want the original picture to be stored for later retrieval | [optional] 
 **storeAttendanceFaces** | **Boolean**| Boolean value indicating whether you want to store permanently store faces clippings of the recognized faces | [optional] 
 **storeAttendanceFrames** | **Boolean**| Boolean value indicating whether you want to store permanently store frames with a recognized face in them | [optional] 
 **isActive** | **Boolean**| Boolean value indicating whether the stream is currently active or not | [optional] 
 **associatedCollections** | [**[String]**](String.md)| List of collection ids which will be used to measure attendance | [optional] 
 **attributes** | **String**| Attributes of the stream | [optional] 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

