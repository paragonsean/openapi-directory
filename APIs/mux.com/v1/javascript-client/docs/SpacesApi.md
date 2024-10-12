# MuxApi.SpacesApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSpace**](SpacesApi.md#createSpace) | **POST** /video/v1/spaces | Create a space
[**createSpaceBroadcast**](SpacesApi.md#createSpaceBroadcast) | **POST** /video/v1/spaces/{SPACE_ID}/broadcasts | Create a space broadcast
[**deleteSpace**](SpacesApi.md#deleteSpace) | **DELETE** /video/v1/spaces/{SPACE_ID} | Delete a space
[**deleteSpaceBroadcast**](SpacesApi.md#deleteSpaceBroadcast) | **DELETE** /video/v1/spaces/{SPACE_ID}/broadcasts/{BROADCAST_ID} | Delete a space broadcast
[**getSpace**](SpacesApi.md#getSpace) | **GET** /video/v1/spaces/{SPACE_ID} | Retrieve a space
[**getSpaceBroadcast**](SpacesApi.md#getSpaceBroadcast) | **GET** /video/v1/spaces/{SPACE_ID}/broadcasts/{BROADCAST_ID} | Retrieve space broadcast
[**listSpaces**](SpacesApi.md#listSpaces) | **GET** /video/v1/spaces | List spaces
[**startSpaceBroadcast**](SpacesApi.md#startSpaceBroadcast) | **POST** /video/v1/spaces/{SPACE_ID}/broadcasts/{BROADCAST_ID}/start | Start a space broadcast
[**stopSpaceBroadcast**](SpacesApi.md#stopSpaceBroadcast) | **POST** /video/v1/spaces/{SPACE_ID}/broadcasts/{BROADCAST_ID}/stop | Stop a space broadcast



## createSpace

> SpaceResponse createSpace(createSpaceRequest)

Create a space

Create a new space. Spaces are used to build [real-time video applications.](https://mux.com/real-time-video)

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.SpacesApi();
let createSpaceRequest = {"type":"server"}; // CreateSpaceRequest | 
apiInstance.createSpace(createSpaceRequest, (error, data, response) => {
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
 **createSpaceRequest** | [**CreateSpaceRequest**](CreateSpaceRequest.md)|  | 

### Return type

[**SpaceResponse**](SpaceResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createSpaceBroadcast

> BroadcastResponse createSpaceBroadcast(SPACE_ID, createBroadcastRequest)

Create a space broadcast

Creates a new broadcast. Broadcasts are used to create composited versions of your space, which can be broadcast to live streams. **Note:** By default only a single broadcast destination can be specified. Contact Mux support if you need more.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.SpacesApi();
let SPACE_ID = "SPACE_ID_example"; // String | The space ID.
let createBroadcastRequest = {"live_stream_id":"GQ9025mPqzyjOy3kKQW006qKTqmULW9vFO"}; // CreateBroadcastRequest | 
apiInstance.createSpaceBroadcast(SPACE_ID, createBroadcastRequest, (error, data, response) => {
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
 **SPACE_ID** | **String**| The space ID. | 
 **createBroadcastRequest** | [**CreateBroadcastRequest**](CreateBroadcastRequest.md)|  | 

### Return type

[**BroadcastResponse**](BroadcastResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteSpace

> deleteSpace(SPACE_ID)

Delete a space

Deletes a space. Spaces can only be deleted when &#x60;idle&#x60;.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.SpacesApi();
let SPACE_ID = "SPACE_ID_example"; // String | The space ID.
apiInstance.deleteSpace(SPACE_ID, (error, data, response) => {
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
 **SPACE_ID** | **String**| The space ID. | 

### Return type

null (empty response body)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteSpaceBroadcast

> deleteSpaceBroadcast(SPACE_ID, BROADCAST_ID)

Delete a space broadcast

Deletes a single broadcast of a specific space. Broadcasts can only be deleted when &#x60;idle&#x60;.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.SpacesApi();
let SPACE_ID = "SPACE_ID_example"; // String | The space ID.
let BROADCAST_ID = "BROADCAST_ID_example"; // String | The broadcast ID.
apiInstance.deleteSpaceBroadcast(SPACE_ID, BROADCAST_ID, (error, data, response) => {
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
 **SPACE_ID** | **String**| The space ID. | 
 **BROADCAST_ID** | **String**| The broadcast ID. | 

### Return type

null (empty response body)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getSpace

> SpaceResponse getSpace(SPACE_ID)

Retrieve a space

Retrieves the details of a space that has previously been created. Supply the unique space ID that was returned from your create space request, and Mux will return the information about the corresponding space. The same information is returned when creating a space.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.SpacesApi();
let SPACE_ID = "SPACE_ID_example"; // String | The space ID.
apiInstance.getSpace(SPACE_ID, (error, data, response) => {
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
 **SPACE_ID** | **String**| The space ID. | 

### Return type

[**SpaceResponse**](SpaceResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSpaceBroadcast

> BroadcastResponse getSpaceBroadcast(SPACE_ID, BROADCAST_ID)

Retrieve space broadcast

Retrieves the details of a broadcast of a specific space.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.SpacesApi();
let SPACE_ID = "SPACE_ID_example"; // String | The space ID.
let BROADCAST_ID = "BROADCAST_ID_example"; // String | The broadcast ID.
apiInstance.getSpaceBroadcast(SPACE_ID, BROADCAST_ID, (error, data, response) => {
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
 **SPACE_ID** | **String**| The space ID. | 
 **BROADCAST_ID** | **String**| The broadcast ID. | 

### Return type

[**BroadcastResponse**](BroadcastResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSpaces

> ListSpacesResponse listSpaces(opts)

List spaces

List all spaces in the current enviroment.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.SpacesApi();
let opts = {
  'limit': 25, // Number | Number of items to include in the response
  'page': 1 // Number | Offset by this many pages, of the size of `limit`
};
apiInstance.listSpaces(opts, (error, data, response) => {
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
 **limit** | **Number**| Number of items to include in the response | [optional] [default to 25]
 **page** | **Number**| Offset by this many pages, of the size of &#x60;limit&#x60; | [optional] [default to 1]

### Return type

[**ListSpacesResponse**](ListSpacesResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## startSpaceBroadcast

> StartSpaceBroadcastResponse startSpaceBroadcast(SPACE_ID, BROADCAST_ID)

Start a space broadcast

Starts broadcasting a space to the associated destination. Broadcasts can only be started when the space is &#x60;active&#x60; (when there are participants connected).

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.SpacesApi();
let SPACE_ID = "SPACE_ID_example"; // String | The space ID.
let BROADCAST_ID = "BROADCAST_ID_example"; // String | The broadcast ID.
apiInstance.startSpaceBroadcast(SPACE_ID, BROADCAST_ID, (error, data, response) => {
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
 **SPACE_ID** | **String**| The space ID. | 
 **BROADCAST_ID** | **String**| The broadcast ID. | 

### Return type

[**StartSpaceBroadcastResponse**](StartSpaceBroadcastResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## stopSpaceBroadcast

> StopSpaceBroadcastResponse stopSpaceBroadcast(SPACE_ID, BROADCAST_ID)

Stop a space broadcast

Stops broadcasting a space, causing the destination live stream to become idle. This API also automatically calls &#x60;complete&#x60; on the destination live stream. Broadcasts are also automatically stopped when a space becomes idle.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.SpacesApi();
let SPACE_ID = "SPACE_ID_example"; // String | The space ID.
let BROADCAST_ID = "BROADCAST_ID_example"; // String | The broadcast ID.
apiInstance.stopSpaceBroadcast(SPACE_ID, BROADCAST_ID, (error, data, response) => {
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
 **SPACE_ID** | **String**| The space ID. | 
 **BROADCAST_ID** | **String**| The broadcast ID. | 

### Return type

[**StopSpaceBroadcastResponse**](StopSpaceBroadcastResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

