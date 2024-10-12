# CloudStorageJsonApi.BucketsApi

All URIs are relative to *https://storage.googleapis.com/storage/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storageBucketsDelete**](BucketsApi.md#storageBucketsDelete) | **DELETE** /b/{bucket} | 
[**storageBucketsGet**](BucketsApi.md#storageBucketsGet) | **GET** /b/{bucket} | 
[**storageBucketsGetIamPolicy**](BucketsApi.md#storageBucketsGetIamPolicy) | **GET** /b/{bucket}/iam | 
[**storageBucketsInsert**](BucketsApi.md#storageBucketsInsert) | **POST** /b | 
[**storageBucketsList**](BucketsApi.md#storageBucketsList) | **GET** /b | 
[**storageBucketsLockRetentionPolicy**](BucketsApi.md#storageBucketsLockRetentionPolicy) | **POST** /b/{bucket}/lockRetentionPolicy | 
[**storageBucketsPatch**](BucketsApi.md#storageBucketsPatch) | **PATCH** /b/{bucket} | 
[**storageBucketsSetIamPolicy**](BucketsApi.md#storageBucketsSetIamPolicy) | **PUT** /b/{bucket}/iam | 
[**storageBucketsTestIamPermissions**](BucketsApi.md#storageBucketsTestIamPermissions) | **GET** /b/{bucket}/iam/testPermissions | 
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
  'uploadType': "uploadType_example", // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'ifMetagenerationMatch': "ifMetagenerationMatch_example", // String | If set, only deletes the bucket if its metageneration matches this value.
  'ifMetagenerationNotMatch': "ifMetagenerationNotMatch_example", // String | If set, only deletes the bucket if its metageneration does not match this value.
  'userProject': "userProject_example" // String | The project to be billed for this request. Required for Requester Pays buckets.
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
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **ifMetagenerationMatch** | **String**| If set, only deletes the bucket if its metageneration matches this value. | [optional] 
 **ifMetagenerationNotMatch** | **String**| If set, only deletes the bucket if its metageneration does not match this value. | [optional] 
 **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] 

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
  'uploadType': "uploadType_example", // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'ifMetagenerationMatch': "ifMetagenerationMatch_example", // String | Makes the return of the bucket metadata conditional on whether the bucket's current metageneration matches the given value.
  'ifMetagenerationNotMatch': "ifMetagenerationNotMatch_example", // String | Makes the return of the bucket metadata conditional on whether the bucket's current metageneration does not match the given value.
  'projection': "projection_example", // String | Set of properties to return. Defaults to noAcl.
  'userProject': "userProject_example" // String | The project to be billed for this request. Required for Requester Pays buckets.
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
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **ifMetagenerationMatch** | **String**| Makes the return of the bucket metadata conditional on whether the bucket&#39;s current metageneration matches the given value. | [optional] 
 **ifMetagenerationNotMatch** | **String**| Makes the return of the bucket metadata conditional on whether the bucket&#39;s current metageneration does not match the given value. | [optional] 
 **projection** | **String**| Set of properties to return. Defaults to noAcl. | [optional] 
 **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] 

### Return type

[**Bucket**](Bucket.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storageBucketsGetIamPolicy

> Policy storageBucketsGetIamPolicy(bucket, opts)



Returns an IAM policy for the specified bucket.

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
  'uploadType': "uploadType_example", // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'optionsRequestedPolicyVersion': 56, // Number | The IAM policy format version to be returned. If the optionsRequestedPolicyVersion is for an older version that doesn't support part of the requested IAM policy, the request fails.
  'userProject': "userProject_example" // String | The project to be billed for this request. Required for Requester Pays buckets.
};
apiInstance.storageBucketsGetIamPolicy(bucket, opts, (error, data, response) => {
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
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **optionsRequestedPolicyVersion** | **Number**| The IAM policy format version to be returned. If the optionsRequestedPolicyVersion is for an older version that doesn&#39;t support part of the requested IAM policy, the request fails. | [optional] 
 **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] 

### Return type

[**Policy**](Policy.md)

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
  'uploadType': "uploadType_example", // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'enableObjectRetention': true, // Boolean | When set to true, object retention is enabled for this bucket.
  'predefinedAcl': "predefinedAcl_example", // String | Apply a predefined set of access controls to this bucket.
  'predefinedDefaultObjectAcl': "predefinedDefaultObjectAcl_example", // String | Apply a predefined set of default object access controls to this bucket.
  'projection': "projection_example", // String | Set of properties to return. Defaults to noAcl, unless the bucket resource specifies acl or defaultObjectAcl properties, when it defaults to full.
  'userProject': "userProject_example", // String | The project to be billed for this request.
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
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **enableObjectRetention** | **Boolean**| When set to true, object retention is enabled for this bucket. | [optional] 
 **predefinedAcl** | **String**| Apply a predefined set of access controls to this bucket. | [optional] 
 **predefinedDefaultObjectAcl** | **String**| Apply a predefined set of default object access controls to this bucket. | [optional] 
 **projection** | **String**| Set of properties to return. Defaults to noAcl, unless the bucket resource specifies acl or defaultObjectAcl properties, when it defaults to full. | [optional] 
 **userProject** | **String**| The project to be billed for this request. | [optional] 
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
  'uploadType': "uploadType_example", // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'maxResults': 56, // Number | Maximum number of buckets to return in a single response. The service will use this parameter or 1,000 items, whichever is smaller.
  'pageToken': "pageToken_example", // String | A previously-returned page token representing part of the larger set of results to view.
  'prefix': "prefix_example", // String | Filter results to buckets whose names begin with this prefix.
  'projection': "projection_example", // String | Set of properties to return. Defaults to noAcl.
  'userProject': "userProject_example" // String | The project to be billed for this request.
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
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **maxResults** | **Number**| Maximum number of buckets to return in a single response. The service will use this parameter or 1,000 items, whichever is smaller. | [optional] 
 **pageToken** | **String**| A previously-returned page token representing part of the larger set of results to view. | [optional] 
 **prefix** | **String**| Filter results to buckets whose names begin with this prefix. | [optional] 
 **projection** | **String**| Set of properties to return. Defaults to noAcl. | [optional] 
 **userProject** | **String**| The project to be billed for this request. | [optional] 

### Return type

[**Buckets**](Buckets.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storageBucketsLockRetentionPolicy

> Bucket storageBucketsLockRetentionPolicy(bucket, ifMetagenerationMatch, opts)



Locks retention policy on a bucket.

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
let ifMetagenerationMatch = "ifMetagenerationMatch_example"; // String | Makes the operation conditional on whether bucket's current metageneration matches the given value.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'uploadType': "uploadType_example", // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'userProject': "userProject_example" // String | The project to be billed for this request. Required for Requester Pays buckets.
};
apiInstance.storageBucketsLockRetentionPolicy(bucket, ifMetagenerationMatch, opts, (error, data, response) => {
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
 **ifMetagenerationMatch** | **String**| Makes the operation conditional on whether bucket&#39;s current metageneration matches the given value. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] 

### Return type

[**Bucket**](Bucket.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storageBucketsPatch

> Bucket storageBucketsPatch(bucket, opts)



Patches a bucket. Changes to the bucket will be readable immediately after writing, but configuration changes may take time to propagate.

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
  'uploadType': "uploadType_example", // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'ifMetagenerationMatch': "ifMetagenerationMatch_example", // String | Makes the return of the bucket metadata conditional on whether the bucket's current metageneration matches the given value.
  'ifMetagenerationNotMatch': "ifMetagenerationNotMatch_example", // String | Makes the return of the bucket metadata conditional on whether the bucket's current metageneration does not match the given value.
  'predefinedAcl': "predefinedAcl_example", // String | Apply a predefined set of access controls to this bucket.
  'predefinedDefaultObjectAcl': "predefinedDefaultObjectAcl_example", // String | Apply a predefined set of default object access controls to this bucket.
  'projection': "projection_example", // String | Set of properties to return. Defaults to full.
  'userProject': "userProject_example", // String | The project to be billed for this request. Required for Requester Pays buckets.
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
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **ifMetagenerationMatch** | **String**| Makes the return of the bucket metadata conditional on whether the bucket&#39;s current metageneration matches the given value. | [optional] 
 **ifMetagenerationNotMatch** | **String**| Makes the return of the bucket metadata conditional on whether the bucket&#39;s current metageneration does not match the given value. | [optional] 
 **predefinedAcl** | **String**| Apply a predefined set of access controls to this bucket. | [optional] 
 **predefinedDefaultObjectAcl** | **String**| Apply a predefined set of default object access controls to this bucket. | [optional] 
 **projection** | **String**| Set of properties to return. Defaults to full. | [optional] 
 **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] 
 **bucket2** | [**Bucket**](Bucket.md)|  | [optional] 

### Return type

[**Bucket**](Bucket.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## storageBucketsSetIamPolicy

> Policy storageBucketsSetIamPolicy(bucket, opts)



Updates an IAM policy for the specified bucket.

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
  'uploadType': "uploadType_example", // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'userProject': "userProject_example", // String | The project to be billed for this request. Required for Requester Pays buckets.
  'policy': new CloudStorageJsonApi.Policy() // Policy | 
};
apiInstance.storageBucketsSetIamPolicy(bucket, opts, (error, data, response) => {
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
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] 
 **policy** | [**Policy**](Policy.md)|  | [optional] 

### Return type

[**Policy**](Policy.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## storageBucketsTestIamPermissions

> TestIamPermissionsResponse storageBucketsTestIamPermissions(bucket, permissions, opts)



Tests a set of permissions on the given bucket to see which, if any, are held by the caller.

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
let permissions = ["null"]; // [String] | Permissions to test.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'uploadType': "uploadType_example", // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'userProject': "userProject_example" // String | The project to be billed for this request. Required for Requester Pays buckets.
};
apiInstance.storageBucketsTestIamPermissions(bucket, permissions, opts, (error, data, response) => {
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
 **permissions** | [**[String]**](String.md)| Permissions to test. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] 

### Return type

[**TestIamPermissionsResponse**](TestIamPermissionsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storageBucketsUpdate

> Bucket storageBucketsUpdate(bucket, opts)



Updates a bucket. Changes to the bucket will be readable immediately after writing, but configuration changes may take time to propagate.

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
  'uploadType': "uploadType_example", // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'ifMetagenerationMatch': "ifMetagenerationMatch_example", // String | Makes the return of the bucket metadata conditional on whether the bucket's current metageneration matches the given value.
  'ifMetagenerationNotMatch': "ifMetagenerationNotMatch_example", // String | Makes the return of the bucket metadata conditional on whether the bucket's current metageneration does not match the given value.
  'predefinedAcl': "predefinedAcl_example", // String | Apply a predefined set of access controls to this bucket.
  'predefinedDefaultObjectAcl': "predefinedDefaultObjectAcl_example", // String | Apply a predefined set of default object access controls to this bucket.
  'projection': "projection_example", // String | Set of properties to return. Defaults to full.
  'userProject': "userProject_example", // String | The project to be billed for this request. Required for Requester Pays buckets.
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
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **ifMetagenerationMatch** | **String**| Makes the return of the bucket metadata conditional on whether the bucket&#39;s current metageneration matches the given value. | [optional] 
 **ifMetagenerationNotMatch** | **String**| Makes the return of the bucket metadata conditional on whether the bucket&#39;s current metageneration does not match the given value. | [optional] 
 **predefinedAcl** | **String**| Apply a predefined set of access controls to this bucket. | [optional] 
 **predefinedDefaultObjectAcl** | **String**| Apply a predefined set of default object access controls to this bucket. | [optional] 
 **projection** | **String**| Set of properties to return. Defaults to full. | [optional] 
 **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] 
 **bucket2** | [**Bucket**](Bucket.md)|  | [optional] 

### Return type

[**Bucket**](Bucket.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

