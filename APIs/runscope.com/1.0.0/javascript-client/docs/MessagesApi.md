# RunscopeApi.MessagesApi

All URIs are relative to *https://api.runscope.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bucketsBucketKeyErrorsGet**](MessagesApi.md#bucketsBucketKeyErrorsGet) | **GET** /buckets/{bucketKey}/errors | Retrieve a list of error messages in a bucket
[**bucketsBucketKeyMessagesDelete**](MessagesApi.md#bucketsBucketKeyMessagesDelete) | **DELETE** /buckets/{bucketKey}/messages | Clear a bucket (remove all messages).
[**bucketsBucketKeyMessagesGet**](MessagesApi.md#bucketsBucketKeyMessagesGet) | **GET** /buckets/{bucketKey}/messages | Retrieve a list of messages in a bucket
[**bucketsBucketKeyMessagesMessageIdGet**](MessagesApi.md#bucketsBucketKeyMessagesMessageIdGet) | **GET** /buckets/{bucketKey}/messages/{messageId} | Retrieve the details for a single message.
[**bucketsBucketKeyMessagesPost**](MessagesApi.md#bucketsBucketKeyMessagesPost) | **POST** /buckets/{bucketKey}/messages | Create a message



## bucketsBucketKeyErrorsGet

> bucketsBucketKeyErrorsGet(bucketKey, opts)

Retrieve a list of error messages in a bucket

### Example

```javascript
import RunscopeApi from 'runscope_api';
let defaultClient = RunscopeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: runscope_auth
let runscope_auth = defaultClient.authentications['runscope_auth'];
runscope_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RunscopeApi.MessagesApi();
let bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
let opts = {
  'count': 56, // Number | Maxiumum number of messages to return. Default 50, max 1000.
  'since': 56, // Number | Only return messages after the given Unix timestamp
  'before': 56 // Number | Only return messages before the given Unix timestamp
};
apiInstance.bucketsBucketKeyErrorsGet(bucketKey, opts, (error, data, response) => {
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
 **bucketKey** | **String**| Unique identifier for a bucket | 
 **count** | **Number**| Maxiumum number of messages to return. Default 50, max 1000. | [optional] 
 **since** | **Number**| Only return messages after the given Unix timestamp | [optional] 
 **before** | **Number**| Only return messages before the given Unix timestamp | [optional] 

### Return type

null (empty response body)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## bucketsBucketKeyMessagesDelete

> bucketsBucketKeyMessagesDelete(bucketKey)

Clear a bucket (remove all messages).

### Example

```javascript
import RunscopeApi from 'runscope_api';
let defaultClient = RunscopeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: runscope_auth
let runscope_auth = defaultClient.authentications['runscope_auth'];
runscope_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RunscopeApi.MessagesApi();
let bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
apiInstance.bucketsBucketKeyMessagesDelete(bucketKey, (error, data, response) => {
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
 **bucketKey** | **String**| Unique identifier for a bucket | 

### Return type

null (empty response body)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## bucketsBucketKeyMessagesGet

> bucketsBucketKeyMessagesGet(bucketKey, opts)

Retrieve a list of messages in a bucket

### Example

```javascript
import RunscopeApi from 'runscope_api';
let defaultClient = RunscopeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: runscope_auth
let runscope_auth = defaultClient.authentications['runscope_auth'];
runscope_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RunscopeApi.MessagesApi();
let bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
let opts = {
  'count': 56, // Number | Maxiumum number of messages to return. Default 50, max 1000.
  'since': 56, // Number | Only return messages after the given Unix timestamp
  'before': 56 // Number | Only return messages before the given Unix timestamp
};
apiInstance.bucketsBucketKeyMessagesGet(bucketKey, opts, (error, data, response) => {
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
 **bucketKey** | **String**| Unique identifier for a bucket | 
 **count** | **Number**| Maxiumum number of messages to return. Default 50, max 1000. | [optional] 
 **since** | **Number**| Only return messages after the given Unix timestamp | [optional] 
 **before** | **Number**| Only return messages before the given Unix timestamp | [optional] 

### Return type

null (empty response body)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## bucketsBucketKeyMessagesMessageIdGet

> bucketsBucketKeyMessagesMessageIdGet(bucketKey, messageId)

Retrieve the details for a single message.

### Example

```javascript
import RunscopeApi from 'runscope_api';
let defaultClient = RunscopeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: runscope_auth
let runscope_auth = defaultClient.authentications['runscope_auth'];
runscope_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RunscopeApi.MessagesApi();
let bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
let messageId = "messageId_example"; // String | The unique identifier for this message
apiInstance.bucketsBucketKeyMessagesMessageIdGet(bucketKey, messageId, (error, data, response) => {
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
 **bucketKey** | **String**| Unique identifier for a bucket | 
 **messageId** | **String**| The unique identifier for this message | 

### Return type

null (empty response body)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## bucketsBucketKeyMessagesPost

> BucketsBucketKeyMessagesPost200Response bucketsBucketKeyMessagesPost(bucketKey, newMessage)

Create a message

### Example

```javascript
import RunscopeApi from 'runscope_api';
let defaultClient = RunscopeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: runscope_auth
let runscope_auth = defaultClient.authentications['runscope_auth'];
runscope_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RunscopeApi.MessagesApi();
let bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
let newMessage = new RunscopeApi.NewMessage(); // NewMessage | 
apiInstance.bucketsBucketKeyMessagesPost(bucketKey, newMessage, (error, data, response) => {
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
 **bucketKey** | **String**| Unique identifier for a bucket | 
 **newMessage** | [**NewMessage**](NewMessage.md)|  | 

### Return type

[**BucketsBucketKeyMessagesPost200Response**](BucketsBucketKeyMessagesPost200Response.md)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

