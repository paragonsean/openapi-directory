# RunscopeApi.BucketsApi

All URIs are relative to *https://api.runscope.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bucketsBucketKeyDelete**](BucketsApi.md#bucketsBucketKeyDelete) | **DELETE** /buckets/{bucketKey} | Delete a single bucket resource.
[**bucketsBucketKeyGet**](BucketsApi.md#bucketsBucketKeyGet) | **GET** /buckets/{bucketKey} | Returns a single bucket resource.
[**bucketsGet**](BucketsApi.md#bucketsGet) | **GET** /buckets | Returns a list of buckets.
[**bucketsPost**](BucketsApi.md#bucketsPost) | **POST** /buckets | Create a new bucket



## bucketsBucketKeyDelete

> bucketsBucketKeyDelete(bucketKey)

Delete a single bucket resource.

### Example

```javascript
import RunscopeApi from 'runscope_api';
let defaultClient = RunscopeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: runscope_auth
let runscope_auth = defaultClient.authentications['runscope_auth'];
runscope_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RunscopeApi.BucketsApi();
let bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
apiInstance.bucketsBucketKeyDelete(bucketKey, (error, data, response) => {
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


## bucketsBucketKeyGet

> Bucket bucketsBucketKeyGet(bucketKey)

Returns a single bucket resource.

### Example

```javascript
import RunscopeApi from 'runscope_api';
let defaultClient = RunscopeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: runscope_auth
let runscope_auth = defaultClient.authentications['runscope_auth'];
runscope_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RunscopeApi.BucketsApi();
let bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
apiInstance.bucketsBucketKeyGet(bucketKey, (error, data, response) => {
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

### Return type

[**Bucket**](Bucket.md)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## bucketsGet

> BucketsGet200Response bucketsGet()

Returns a list of buckets.

### Example

```javascript
import RunscopeApi from 'runscope_api';
let defaultClient = RunscopeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: runscope_auth
let runscope_auth = defaultClient.authentications['runscope_auth'];
runscope_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RunscopeApi.BucketsApi();
apiInstance.bucketsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**BucketsGet200Response**](BucketsGet200Response.md)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## bucketsPost

> Bucket bucketsPost(newBucket)

Create a new bucket

### Example

```javascript
import RunscopeApi from 'runscope_api';
let defaultClient = RunscopeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: runscope_auth
let runscope_auth = defaultClient.authentications['runscope_auth'];
runscope_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RunscopeApi.BucketsApi();
let newBucket = new RunscopeApi.NewBucket(); // NewBucket | 
apiInstance.bucketsPost(newBucket, (error, data, response) => {
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
 **newBucket** | [**NewBucket**](NewBucket.md)|  | 

### Return type

[**Bucket**](Bucket.md)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

