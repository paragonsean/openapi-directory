# CloudStorageJsonApi.BucketsApi

All URIs are relative to *https://storage.googleapis.com/storage/v1beta2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storageBucketsDelete**](BucketsApi.md#storageBucketsDelete) | **DELETE** /b/{bucket} | 
[**storageBucketsGet**](BucketsApi.md#storageBucketsGet) | **GET** /b/{bucket} | 
[**storageBucketsInsert**](BucketsApi.md#storageBucketsInsert) | **POST** /b | 
[**storageBucketsList**](BucketsApi.md#storageBucketsList) | **GET** /b | 
[**storageBucketsPatch**](BucketsApi.md#storageBucketsPatch) | **PATCH** /b/{bucket} | 
[**storageBucketsUpdate**](BucketsApi.md#storageBucketsUpdate) | **PUT** /b/{bucket} | 



## storageBucketsDelete

> storageBucketsDelete(bucket, opts)



Permanently deletes an empty bucket.

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

let apiInstance = new CloudStorageJsonApi.BucketsApi();
let bucket = "bucket_example"; // String | Name of a bucket.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'ifMetagenerationMatch': "ifMetagenerationMatch_example", // String | Makes the return of the bucket metadata conditional on whether the bucket's current metageneration matches the given value.
  'ifMetagenerationNotMatch': "ifMetagenerationNotMatch_example" // String | Makes the return of the bucket metadata conditional on whether the bucket's current metageneration does not match the given value.
};
apiInstance.storageBucketsDelete(bucket, opts, (error, data, response) => {
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
 **bucket** | **String**| Name of a bucket. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **ifMetagenerationMatch** | **String**| Makes the return of the bucket metadata conditional on whether the bucket&#39;s current metageneration matches the given value. | [optional] 
 **ifMetagenerationNotMatch** | **String**| Makes the return of the bucket metadata conditional on whether the bucket&#39;s current metageneration does not match the given value. | [optional] 

### Return type

null (empty response body)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## storageBucketsGet

> Bucket storageBucketsGet(bucket, opts)



Returns metadata for the specified bucket.

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

let apiInstance = new CloudStorageJsonApi.BucketsApi();
let bucket = "bucket_example"; // String | Name of a bucket.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'ifMetagenerationMatch': "ifMetagenerationMatch_example", // String | Makes the return of the bucket metadata conditional on whether the bucket's current metageneration matches the given value.
  'ifMetagenerationNotMatch': "ifMetagenerationNotMatch_example", // String | Makes the return of the bucket metadata conditional on whether the bucket's current metageneration does not match the given value.
  'projection': "projection_example" // String | Set of properties to return. Defaults to noAcl.
};
apiInstance.storageBucketsGet(bucket, opts, (error, data, response) => {
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
 **bucket** | **String**| Name of a bucket. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **ifMetagenerationMatch** | **String**| Makes the return of the bucket metadata conditional on whether the bucket&#39;s current metageneration matches the given value. | [optional] 
 **ifMetagenerationNotMatch** | **String**| Makes the return of the bucket metadata conditional on whether the bucket&#39;s current metageneration does not match the given value. | [optional] 
 **projection** | **String**| Set of properties to return. Defaults to noAcl. | [optional] 

### Return type

[**Bucket**](Bucket.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storageBucketsInsert

> Bucket storageBucketsInsert(project, opts)



Creates a new bucket.

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

let apiInstance = new CloudStorageJsonApi.BucketsApi();
let project = "project_example"; // String | A valid API project identifier.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'projection': "projection_example", // String | Set of properties to return. Defaults to noAcl, unless the bucket resource specifies acl or defaultObjectAcl properties, when it defaults to full.
  'bucket': new CloudStorageJsonApi.Bucket() // Bucket | 
};
apiInstance.storageBucketsInsert(project, opts, (error, data, response) => {
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
 **project** | **String**| A valid API project identifier. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **projection** | **String**| Set of properties to return. Defaults to noAcl, unless the bucket resource specifies acl or defaultObjectAcl properties, when it defaults to full. | [optional] 
 **bucket** | [**Bucket**](Bucket.md)|  | [optional] 

### Return type

[**Bucket**](Bucket.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## storageBucketsList

> Buckets storageBucketsList(project, opts)



Retrieves a list of buckets for a given project.

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

let apiInstance = new CloudStorageJsonApi.BucketsApi();
let project = "project_example"; // String | A valid API project identifier.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'maxResults': 56, // Number | Maximum number of buckets to return.
  'pageToken': "pageToken_example", // String | A previously-returned page token representing part of the larger set of results to view.
  'projection': "projection_example" // String | Set of properties to return. Defaults to noAcl.
};
apiInstance.storageBucketsList(project, opts, (error, data, response) => {
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
 **project** | **String**| A valid API project identifier. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **maxResults** | **Number**| Maximum number of buckets to return. | [optional] 
 **pageToken** | **String**| A previously-returned page token representing part of the larger set of results to view. | [optional] 
 **projection** | **String**| Set of properties to return. Defaults to noAcl. | [optional] 

### Return type

[**Buckets**](Buckets.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storageBucketsPatch

> Bucket storageBucketsPatch(bucket, opts)



Updates a bucket. This method supports patch semantics.

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

let apiInstance = new CloudStorageJsonApi.BucketsApi();
let bucket = "bucket_example"; // String | Name of a bucket.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'ifMetagenerationMatch': "ifMetagenerationMatch_example", // String | Makes the return of the bucket metadata conditional on whether the bucket's current metageneration matches the given value.
  'ifMetagenerationNotMatch': "ifMetagenerationNotMatch_example", // String | Makes the return of the bucket metadata conditional on whether the bucket's current metageneration does not match the given value.
  'projection': "projection_example", // String | Set of properties to return. Defaults to full.
  'bucket2': new CloudStorageJsonApi.Bucket() // Bucket | 
};
apiInstance.storageBucketsPatch(bucket, opts, (error, data, response) => {
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
 **bucket** | **String**| Name of a bucket. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **ifMetagenerationMatch** | **String**| Makes the return of the bucket metadata conditional on whether the bucket&#39;s current metageneration matches the given value. | [optional] 
 **ifMetagenerationNotMatch** | **String**| Makes the return of the bucket metadata conditional on whether the bucket&#39;s current metageneration does not match the given value. | [optional] 
 **projection** | **String**| Set of properties to return. Defaults to full. | [optional] 
 **bucket2** | [**Bucket**](Bucket.md)|  | [optional] 

### Return type

[**Bucket**](Bucket.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## storageBucketsUpdate

> Bucket storageBucketsUpdate(bucket, opts)



Updates a bucket.

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

let apiInstance = new CloudStorageJsonApi.BucketsApi();
let bucket = "bucket_example"; // String | Name of a bucket.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'ifMetagenerationMatch': "ifMetagenerationMatch_example", // String | Makes the return of the bucket metadata conditional on whether the bucket's current metageneration matches the given value.
  'ifMetagenerationNotMatch': "ifMetagenerationNotMatch_example", // String | Makes the return of the bucket metadata conditional on whether the bucket's current metageneration does not match the given value.
  'projection': "projection_example", // String | Set of properties to return. Defaults to full.
  'bucket2': new CloudStorageJsonApi.Bucket() // Bucket | 
};
apiInstance.storageBucketsUpdate(bucket, opts, (error, data, response) => {
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
 **bucket** | **String**| Name of a bucket. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **ifMetagenerationMatch** | **String**| Makes the return of the bucket metadata conditional on whether the bucket&#39;s current metageneration matches the given value. | [optional] 
 **ifMetagenerationNotMatch** | **String**| Makes the return of the bucket metadata conditional on whether the bucket&#39;s current metageneration does not match the given value. | [optional] 
 **projection** | **String**| Set of properties to return. Defaults to full. | [optional] 
 **bucket2** | [**Bucket**](Bucket.md)|  | [optional] 

### Return type

[**Bucket**](Bucket.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

