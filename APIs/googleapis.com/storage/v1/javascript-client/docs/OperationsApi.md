# CloudStorageJsonApi.OperationsApi

All URIs are relative to *https://storage.googleapis.com/storage/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storageBucketsOperationsCancel**](OperationsApi.md#storageBucketsOperationsCancel) | **POST** /b/{bucket}/operations/{operationId}/cancel | 
[**storageBucketsOperationsGet**](OperationsApi.md#storageBucketsOperationsGet) | **GET** /b/{bucket}/operations/{operationId} | 
[**storageBucketsOperationsList**](OperationsApi.md#storageBucketsOperationsList) | **GET** /b/{bucket}/operations | 



## storageBucketsOperationsCancel

> storageBucketsOperationsCancel(bucket, operationId, opts)



Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed.

### Example

```javascript
import CloudStorageJsonApi from 'cloud_storage_json_api';
let defaultClient = CloudStorageJsonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudStorageJsonApi.OperationsApi();
let bucket = "bucket_example"; // String | The parent bucket of the operation resource.
let operationId = "operationId_example"; // String | The ID of the operation resource.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'uploadType': "uploadType_example", // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.storageBucketsOperationsCancel(bucket, operationId, opts, (error, data, response) => {
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
 **bucket** | **String**| The parent bucket of the operation resource. | 
 **operationId** | **String**| The ID of the operation resource. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

null (empty response body)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## storageBucketsOperationsGet

> GoogleLongrunningOperation storageBucketsOperationsGet(bucket, operationId, opts)



Gets the latest state of a long-running operation.

### Example

```javascript
import CloudStorageJsonApi from 'cloud_storage_json_api';
let defaultClient = CloudStorageJsonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudStorageJsonApi.OperationsApi();
let bucket = "bucket_example"; // String | The parent bucket of the operation resource.
let operationId = "operationId_example"; // String | The ID of the operation resource.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'uploadType': "uploadType_example", // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.storageBucketsOperationsGet(bucket, operationId, opts, (error, data, response) => {
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
 **bucket** | **String**| The parent bucket of the operation resource. | 
 **operationId** | **String**| The ID of the operation resource. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storageBucketsOperationsList

> GoogleLongrunningListOperationsResponse storageBucketsOperationsList(bucket, opts)



Lists operations that match the specified filter in the request.

### Example

```javascript
import CloudStorageJsonApi from 'cloud_storage_json_api';
let defaultClient = CloudStorageJsonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudStorageJsonApi.OperationsApi();
let bucket = "bucket_example"; // String | Name of the bucket in which to look for operations.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'uploadType': "uploadType_example", // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'filter': "filter_example", // String | A filter to narrow down results to a preferred subset. The filtering language is documented in more detail in [AIP-160](https://google.aip.dev/160).
  'pageSize': 56, // Number | Maximum number of items to return in a single page of responses. Fewer total results may be returned than requested. The service uses this parameter or 100 items, whichever is smaller.
  'pageToken': "pageToken_example" // String | A previously-returned page token representing part of the larger set of results to view.
};
apiInstance.storageBucketsOperationsList(bucket, opts, (error, data, response) => {
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
 **bucket** | **String**| Name of the bucket in which to look for operations. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **filter** | **String**| A filter to narrow down results to a preferred subset. The filtering language is documented in more detail in [AIP-160](https://google.aip.dev/160). | [optional] 
 **pageSize** | **Number**| Maximum number of items to return in a single page of responses. Fewer total results may be returned than requested. The service uses this parameter or 100 items, whichever is smaller. | [optional] 
 **pageToken** | **String**| A previously-returned page token representing part of the larger set of results to view. | [optional] 

### Return type

[**GoogleLongrunningListOperationsResponse**](GoogleLongrunningListOperationsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

