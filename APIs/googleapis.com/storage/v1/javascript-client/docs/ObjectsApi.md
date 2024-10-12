# CloudStorageJsonApi.ObjectsApi

All URIs are relative to *https://storage.googleapis.com/storage/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storageObjectsBulkRestore**](ObjectsApi.md#storageObjectsBulkRestore) | **POST** /b/{bucket}/o/bulkRestore | 
[**storageObjectsCompose**](ObjectsApi.md#storageObjectsCompose) | **POST** /b/{destinationBucket}/o/{destinationObject}/compose | 
[**storageObjectsCopy**](ObjectsApi.md#storageObjectsCopy) | **POST** /b/{sourceBucket}/o/{sourceObject}/copyTo/b/{destinationBucket}/o/{destinationObject} | 
[**storageObjectsDelete**](ObjectsApi.md#storageObjectsDelete) | **DELETE** /b/{bucket}/o/{object} | 
[**storageObjectsGet**](ObjectsApi.md#storageObjectsGet) | **GET** /b/{bucket}/o/{object} | 
[**storageObjectsGetIamPolicy**](ObjectsApi.md#storageObjectsGetIamPolicy) | **GET** /b/{bucket}/o/{object}/iam | 
[**storageObjectsInsert**](ObjectsApi.md#storageObjectsInsert) | **POST** /b/{bucket}/o | 
[**storageObjectsList**](ObjectsApi.md#storageObjectsList) | **GET** /b/{bucket}/o | 
[**storageObjectsPatch**](ObjectsApi.md#storageObjectsPatch) | **PATCH** /b/{bucket}/o/{object} | 
[**storageObjectsRestore**](ObjectsApi.md#storageObjectsRestore) | **POST** /b/{bucket}/o/{object}/restore | 
[**storageObjectsRewrite**](ObjectsApi.md#storageObjectsRewrite) | **POST** /b/{sourceBucket}/o/{sourceObject}/rewriteTo/b/{destinationBucket}/o/{destinationObject} | 
[**storageObjectsSetIamPolicy**](ObjectsApi.md#storageObjectsSetIamPolicy) | **PUT** /b/{bucket}/o/{object}/iam | 
[**storageObjectsTestIamPermissions**](ObjectsApi.md#storageObjectsTestIamPermissions) | **GET** /b/{bucket}/o/{object}/iam/testPermissions | 
[**storageObjectsUpdate**](ObjectsApi.md#storageObjectsUpdate) | **PUT** /b/{bucket}/o/{object} | 
[**storageObjectsWatchAll**](ObjectsApi.md#storageObjectsWatchAll) | **POST** /b/{bucket}/o/watch | 



## storageObjectsBulkRestore

> GoogleLongrunningOperation storageObjectsBulkRestore(bucket, opts)



Initiates a long-running bulk restore operation on the specified bucket.

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

let apiInstance = new CloudStorageJsonApi.ObjectsApi();
let bucket = "bucket_example"; // String | Name of the bucket in which the object resides.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'uploadType': "uploadType_example", // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'bulkRestoreObjectsRequest': new CloudStorageJsonApi.BulkRestoreObjectsRequest() // BulkRestoreObjectsRequest | 
};
apiInstance.storageObjectsBulkRestore(bucket, opts, (error, data, response) => {
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
 **bucket** | **String**| Name of the bucket in which the object resides. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **bulkRestoreObjectsRequest** | [**BulkRestoreObjectsRequest**](BulkRestoreObjectsRequest.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## storageObjectsCompose

> ModelObject storageObjectsCompose(destinationBucket, destinationObject, opts)



Concatenates a list of existing objects into a new object in the same bucket.

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

let apiInstance = new CloudStorageJsonApi.ObjectsApi();
let destinationBucket = "destinationBucket_example"; // String | Name of the bucket containing the source objects. The destination object is stored in this bucket.
let destinationObject = "destinationObject_example"; // String | Name of the new object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding).
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'uploadType': "uploadType_example", // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'destinationPredefinedAcl': "destinationPredefinedAcl_example", // String | Apply a predefined set of access controls to the destination object.
  'ifGenerationMatch': "ifGenerationMatch_example", // String | Makes the operation conditional on whether the object's current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object.
  'ifMetagenerationMatch': "ifMetagenerationMatch_example", // String | Makes the operation conditional on whether the object's current metageneration matches the given value.
  'kmsKeyName': "kmsKeyName_example", // String | Resource name of the Cloud KMS key, of the form projects/my-project/locations/global/keyRings/my-kr/cryptoKeys/my-key, that will be used to encrypt the object. Overrides the object metadata's kms_key_name value, if any.
  'userProject': "userProject_example", // String | The project to be billed for this request. Required for Requester Pays buckets.
  'composeRequest': new CloudStorageJsonApi.ComposeRequest() // ComposeRequest | 
};
apiInstance.storageObjectsCompose(destinationBucket, destinationObject, opts, (error, data, response) => {
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
 **destinationBucket** | **String**| Name of the bucket containing the source objects. The destination object is stored in this bucket. | 
 **destinationObject** | **String**| Name of the new object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding). | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **destinationPredefinedAcl** | **String**| Apply a predefined set of access controls to the destination object. | [optional] 
 **ifGenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object. | [optional] 
 **ifMetagenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration matches the given value. | [optional] 
 **kmsKeyName** | **String**| Resource name of the Cloud KMS key, of the form projects/my-project/locations/global/keyRings/my-kr/cryptoKeys/my-key, that will be used to encrypt the object. Overrides the object metadata&#39;s kms_key_name value, if any. | [optional] 
 **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] 
 **composeRequest** | [**ComposeRequest**](ComposeRequest.md)|  | [optional] 

### Return type

[**ModelObject**](ModelObject.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## storageObjectsCopy

> ModelObject storageObjectsCopy(sourceBucket, sourceObject, destinationBucket, destinationObject, opts)



Copies a source object to a destination object. Optionally overrides metadata.

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

let apiInstance = new CloudStorageJsonApi.ObjectsApi();
let sourceBucket = "sourceBucket_example"; // String | Name of the bucket in which to find the source object.
let sourceObject = "sourceObject_example"; // String | Name of the source object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding).
let destinationBucket = "destinationBucket_example"; // String | Name of the bucket in which to store the new object. Overrides the provided object metadata's bucket value, if any.For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding).
let destinationObject = "destinationObject_example"; // String | Name of the new object. Required when the object metadata is not otherwise provided. Overrides the object metadata's name value, if any.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'uploadType': "uploadType_example", // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'destinationKmsKeyName': "destinationKmsKeyName_example", // String | Resource name of the Cloud KMS key, of the form projects/my-project/locations/global/keyRings/my-kr/cryptoKeys/my-key, that will be used to encrypt the object. Overrides the object metadata's kms_key_name value, if any.
  'destinationPredefinedAcl': "destinationPredefinedAcl_example", // String | Apply a predefined set of access controls to the destination object.
  'ifGenerationMatch': "ifGenerationMatch_example", // String | Makes the operation conditional on whether the destination object's current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object.
  'ifGenerationNotMatch': "ifGenerationNotMatch_example", // String | Makes the operation conditional on whether the destination object's current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object.
  'ifMetagenerationMatch': "ifMetagenerationMatch_example", // String | Makes the operation conditional on whether the destination object's current metageneration matches the given value.
  'ifMetagenerationNotMatch': "ifMetagenerationNotMatch_example", // String | Makes the operation conditional on whether the destination object's current metageneration does not match the given value.
  'ifSourceGenerationMatch': "ifSourceGenerationMatch_example", // String | Makes the operation conditional on whether the source object's current generation matches the given value.
  'ifSourceGenerationNotMatch': "ifSourceGenerationNotMatch_example", // String | Makes the operation conditional on whether the source object's current generation does not match the given value.
  'ifSourceMetagenerationMatch': "ifSourceMetagenerationMatch_example", // String | Makes the operation conditional on whether the source object's current metageneration matches the given value.
  'ifSourceMetagenerationNotMatch': "ifSourceMetagenerationNotMatch_example", // String | Makes the operation conditional on whether the source object's current metageneration does not match the given value.
  'projection': "projection_example", // String | Set of properties to return. Defaults to noAcl, unless the object resource specifies the acl property, when it defaults to full.
  'sourceGeneration': "sourceGeneration_example", // String | If present, selects a specific revision of the source object (as opposed to the latest version, the default).
  'userProject': "userProject_example", // String | The project to be billed for this request. Required for Requester Pays buckets.
  'modelObject': new CloudStorageJsonApi.ModelObject() // ModelObject | 
};
apiInstance.storageObjectsCopy(sourceBucket, sourceObject, destinationBucket, destinationObject, opts, (error, data, response) => {
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
 **sourceBucket** | **String**| Name of the bucket in which to find the source object. | 
 **sourceObject** | **String**| Name of the source object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding). | 
 **destinationBucket** | **String**| Name of the bucket in which to store the new object. Overrides the provided object metadata&#39;s bucket value, if any.For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding). | 
 **destinationObject** | **String**| Name of the new object. Required when the object metadata is not otherwise provided. Overrides the object metadata&#39;s name value, if any. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **destinationKmsKeyName** | **String**| Resource name of the Cloud KMS key, of the form projects/my-project/locations/global/keyRings/my-kr/cryptoKeys/my-key, that will be used to encrypt the object. Overrides the object metadata&#39;s kms_key_name value, if any. | [optional] 
 **destinationPredefinedAcl** | **String**| Apply a predefined set of access controls to the destination object. | [optional] 
 **ifGenerationMatch** | **String**| Makes the operation conditional on whether the destination object&#39;s current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object. | [optional] 
 **ifGenerationNotMatch** | **String**| Makes the operation conditional on whether the destination object&#39;s current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object. | [optional] 
 **ifMetagenerationMatch** | **String**| Makes the operation conditional on whether the destination object&#39;s current metageneration matches the given value. | [optional] 
 **ifMetagenerationNotMatch** | **String**| Makes the operation conditional on whether the destination object&#39;s current metageneration does not match the given value. | [optional] 
 **ifSourceGenerationMatch** | **String**| Makes the operation conditional on whether the source object&#39;s current generation matches the given value. | [optional] 
 **ifSourceGenerationNotMatch** | **String**| Makes the operation conditional on whether the source object&#39;s current generation does not match the given value. | [optional] 
 **ifSourceMetagenerationMatch** | **String**| Makes the operation conditional on whether the source object&#39;s current metageneration matches the given value. | [optional] 
 **ifSourceMetagenerationNotMatch** | **String**| Makes the operation conditional on whether the source object&#39;s current metageneration does not match the given value. | [optional] 
 **projection** | **String**| Set of properties to return. Defaults to noAcl, unless the object resource specifies the acl property, when it defaults to full. | [optional] 
 **sourceGeneration** | **String**| If present, selects a specific revision of the source object (as opposed to the latest version, the default). | [optional] 
 **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] 
 **modelObject** | [**ModelObject**](ModelObject.md)|  | [optional] 

### Return type

[**ModelObject**](ModelObject.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## storageObjectsDelete

> storageObjectsDelete(bucket, object, opts)



Deletes an object and its metadata. Deletions are permanent if versioning is not enabled for the bucket, or if the generation parameter is used.

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

let apiInstance = new CloudStorageJsonApi.ObjectsApi();
let bucket = "bucket_example"; // String | Name of the bucket in which the object resides.
let object = "object_example"; // String | Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding).
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'uploadType': "uploadType_example", // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'generation': "generation_example", // String | If present, permanently deletes a specific revision of this object (as opposed to the latest version, the default).
  'ifGenerationMatch': "ifGenerationMatch_example", // String | Makes the operation conditional on whether the object's current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object.
  'ifGenerationNotMatch': "ifGenerationNotMatch_example", // String | Makes the operation conditional on whether the object's current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object.
  'ifMetagenerationMatch': "ifMetagenerationMatch_example", // String | Makes the operation conditional on whether the object's current metageneration matches the given value.
  'ifMetagenerationNotMatch': "ifMetagenerationNotMatch_example", // String | Makes the operation conditional on whether the object's current metageneration does not match the given value.
  'userProject': "userProject_example" // String | The project to be billed for this request. Required for Requester Pays buckets.
};
apiInstance.storageObjectsDelete(bucket, object, opts, (error, data, response) => {
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
 **bucket** | **String**| Name of the bucket in which the object resides. | 
 **object** | **String**| Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding). | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **generation** | **String**| If present, permanently deletes a specific revision of this object (as opposed to the latest version, the default). | [optional] 
 **ifGenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object. | [optional] 
 **ifGenerationNotMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object. | [optional] 
 **ifMetagenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration matches the given value. | [optional] 
 **ifMetagenerationNotMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration does not match the given value. | [optional] 
 **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] 

### Return type

null (empty response body)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## storageObjectsGet

> ModelObject storageObjectsGet(bucket, object, opts)



Retrieves an object or its metadata.

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

let apiInstance = new CloudStorageJsonApi.ObjectsApi();
let bucket = "bucket_example"; // String | Name of the bucket in which the object resides.
let object = "object_example"; // String | Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding).
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'uploadType': "uploadType_example", // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'generation': "generation_example", // String | If present, selects a specific revision of this object (as opposed to the latest version, the default).
  'ifGenerationMatch': "ifGenerationMatch_example", // String | Makes the operation conditional on whether the object's current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object.
  'ifGenerationNotMatch': "ifGenerationNotMatch_example", // String | Makes the operation conditional on whether the object's current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object.
  'ifMetagenerationMatch': "ifMetagenerationMatch_example", // String | Makes the operation conditional on whether the object's current metageneration matches the given value.
  'ifMetagenerationNotMatch': "ifMetagenerationNotMatch_example", // String | Makes the operation conditional on whether the object's current metageneration does not match the given value.
  'projection': "projection_example", // String | Set of properties to return. Defaults to noAcl.
  'softDeleted': true, // Boolean | If true, only soft-deleted object versions will be listed. The default is false. For more information, see Soft Delete.
  'userProject': "userProject_example" // String | The project to be billed for this request. Required for Requester Pays buckets.
};
apiInstance.storageObjectsGet(bucket, object, opts, (error, data, response) => {
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
 **bucket** | **String**| Name of the bucket in which the object resides. | 
 **object** | **String**| Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding). | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **generation** | **String**| If present, selects a specific revision of this object (as opposed to the latest version, the default). | [optional] 
 **ifGenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object. | [optional] 
 **ifGenerationNotMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object. | [optional] 
 **ifMetagenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration matches the given value. | [optional] 
 **ifMetagenerationNotMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration does not match the given value. | [optional] 
 **projection** | **String**| Set of properties to return. Defaults to noAcl. | [optional] 
 **softDeleted** | **Boolean**| If true, only soft-deleted object versions will be listed. The default is false. For more information, see Soft Delete. | [optional] 
 **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] 

### Return type

[**ModelObject**](ModelObject.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storageObjectsGetIamPolicy

> Policy storageObjectsGetIamPolicy(bucket, object, opts)



Returns an IAM policy for the specified object.

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

let apiInstance = new CloudStorageJsonApi.ObjectsApi();
let bucket = "bucket_example"; // String | Name of the bucket in which the object resides.
let object = "object_example"; // String | Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding).
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'uploadType': "uploadType_example", // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'generation': "generation_example", // String | If present, selects a specific revision of this object (as opposed to the latest version, the default).
  'userProject': "userProject_example" // String | The project to be billed for this request. Required for Requester Pays buckets.
};
apiInstance.storageObjectsGetIamPolicy(bucket, object, opts, (error, data, response) => {
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
 **bucket** | **String**| Name of the bucket in which the object resides. | 
 **object** | **String**| Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding). | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **generation** | **String**| If present, selects a specific revision of this object (as opposed to the latest version, the default). | [optional] 
 **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] 

### Return type

[**Policy**](Policy.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storageObjectsInsert

> ModelObject storageObjectsInsert(bucket, opts)



Stores a new object and metadata.

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

let apiInstance = new CloudStorageJsonApi.ObjectsApi();
let bucket = "bucket_example"; // String | Name of the bucket in which to store the new object. Overrides the provided object metadata's bucket value, if any.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'uploadType': "uploadType_example", // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'contentEncoding': "contentEncoding_example", // String | If set, sets the contentEncoding property of the final object to this value. Setting this parameter is equivalent to setting the contentEncoding metadata property. This can be useful when uploading an object with uploadType=media to indicate the encoding of the content being uploaded.
  'ifGenerationMatch': "ifGenerationMatch_example", // String | Makes the operation conditional on whether the object's current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object.
  'ifGenerationNotMatch': "ifGenerationNotMatch_example", // String | Makes the operation conditional on whether the object's current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object.
  'ifMetagenerationMatch': "ifMetagenerationMatch_example", // String | Makes the operation conditional on whether the object's current metageneration matches the given value.
  'ifMetagenerationNotMatch': "ifMetagenerationNotMatch_example", // String | Makes the operation conditional on whether the object's current metageneration does not match the given value.
  'kmsKeyName': "kmsKeyName_example", // String | Resource name of the Cloud KMS key, of the form projects/my-project/locations/global/keyRings/my-kr/cryptoKeys/my-key, that will be used to encrypt the object. Overrides the object metadata's kms_key_name value, if any.
  'name': "name_example", // String | Name of the object. Required when the object metadata is not otherwise provided. Overrides the object metadata's name value, if any. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding).
  'predefinedAcl': "predefinedAcl_example", // String | Apply a predefined set of access controls to this object.
  'projection': "projection_example", // String | Set of properties to return. Defaults to noAcl, unless the object resource specifies the acl property, when it defaults to full.
  'userProject': "userProject_example", // String | The project to be billed for this request. Required for Requester Pays buckets.
  'modelObject': new CloudStorageJsonApi.ModelObject() // ModelObject | 
};
apiInstance.storageObjectsInsert(bucket, opts, (error, data, response) => {
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
 **bucket** | **String**| Name of the bucket in which to store the new object. Overrides the provided object metadata&#39;s bucket value, if any. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **contentEncoding** | **String**| If set, sets the contentEncoding property of the final object to this value. Setting this parameter is equivalent to setting the contentEncoding metadata property. This can be useful when uploading an object with uploadType&#x3D;media to indicate the encoding of the content being uploaded. | [optional] 
 **ifGenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object. | [optional] 
 **ifGenerationNotMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object. | [optional] 
 **ifMetagenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration matches the given value. | [optional] 
 **ifMetagenerationNotMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration does not match the given value. | [optional] 
 **kmsKeyName** | **String**| Resource name of the Cloud KMS key, of the form projects/my-project/locations/global/keyRings/my-kr/cryptoKeys/my-key, that will be used to encrypt the object. Overrides the object metadata&#39;s kms_key_name value, if any. | [optional] 
 **name** | **String**| Name of the object. Required when the object metadata is not otherwise provided. Overrides the object metadata&#39;s name value, if any. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding). | [optional] 
 **predefinedAcl** | **String**| Apply a predefined set of access controls to this object. | [optional] 
 **projection** | **String**| Set of properties to return. Defaults to noAcl, unless the object resource specifies the acl property, when it defaults to full. | [optional] 
 **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] 
 **modelObject** | [**ModelObject**](ModelObject.md)|  | [optional] 

### Return type

[**ModelObject**](ModelObject.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json


## storageObjectsList

> Objects storageObjectsList(bucket, opts)



Retrieves a list of objects matching the criteria.

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

let apiInstance = new CloudStorageJsonApi.ObjectsApi();
let bucket = "bucket_example"; // String | Name of the bucket in which to look for objects.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'uploadType': "uploadType_example", // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'delimiter': "delimiter_example", // String | Returns results in a directory-like mode. items will contain only objects whose names, aside from the prefix, do not contain delimiter. Objects whose names, aside from the prefix, contain delimiter will have their name, truncated after the delimiter, returned in prefixes. Duplicate prefixes are omitted.
  'endOffset': "endOffset_example", // String | Filter results to objects whose names are lexicographically before endOffset. If startOffset is also set, the objects listed will have names between startOffset (inclusive) and endOffset (exclusive).
  'includeFoldersAsPrefixes': true, // Boolean | Only applicable if delimiter is set to '/'. If true, will also include folders and managed folders (besides objects) in the returned prefixes.
  'includeTrailingDelimiter': true, // Boolean | If true, objects that end in exactly one instance of delimiter will have their metadata included in items in addition to prefixes.
  'matchGlob': "matchGlob_example", // String | Filter results to objects and prefixes that match this glob pattern.
  'maxResults': 56, // Number | Maximum number of items plus prefixes to return in a single page of responses. As duplicate prefixes are omitted, fewer total results may be returned than requested. The service will use this parameter or 1,000 items, whichever is smaller.
  'pageToken': "pageToken_example", // String | A previously-returned page token representing part of the larger set of results to view.
  'prefix': "prefix_example", // String | Filter results to objects whose names begin with this prefix.
  'projection': "projection_example", // String | Set of properties to return. Defaults to noAcl.
  'softDeleted': true, // Boolean | If true, only soft-deleted object versions will be listed. The default is false. For more information, see Soft Delete.
  'startOffset': "startOffset_example", // String | Filter results to objects whose names are lexicographically equal to or after startOffset. If endOffset is also set, the objects listed will have names between startOffset (inclusive) and endOffset (exclusive).
  'userProject': "userProject_example", // String | The project to be billed for this request. Required for Requester Pays buckets.
  'versions': true // Boolean | If true, lists all versions of an object as distinct results. The default is false. For more information, see Object Versioning.
};
apiInstance.storageObjectsList(bucket, opts, (error, data, response) => {
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
 **bucket** | **String**| Name of the bucket in which to look for objects. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **delimiter** | **String**| Returns results in a directory-like mode. items will contain only objects whose names, aside from the prefix, do not contain delimiter. Objects whose names, aside from the prefix, contain delimiter will have their name, truncated after the delimiter, returned in prefixes. Duplicate prefixes are omitted. | [optional] 
 **endOffset** | **String**| Filter results to objects whose names are lexicographically before endOffset. If startOffset is also set, the objects listed will have names between startOffset (inclusive) and endOffset (exclusive). | [optional] 
 **includeFoldersAsPrefixes** | **Boolean**| Only applicable if delimiter is set to &#39;/&#39;. If true, will also include folders and managed folders (besides objects) in the returned prefixes. | [optional] 
 **includeTrailingDelimiter** | **Boolean**| If true, objects that end in exactly one instance of delimiter will have their metadata included in items in addition to prefixes. | [optional] 
 **matchGlob** | **String**| Filter results to objects and prefixes that match this glob pattern. | [optional] 
 **maxResults** | **Number**| Maximum number of items plus prefixes to return in a single page of responses. As duplicate prefixes are omitted, fewer total results may be returned than requested. The service will use this parameter or 1,000 items, whichever is smaller. | [optional] 
 **pageToken** | **String**| A previously-returned page token representing part of the larger set of results to view. | [optional] 
 **prefix** | **String**| Filter results to objects whose names begin with this prefix. | [optional] 
 **projection** | **String**| Set of properties to return. Defaults to noAcl. | [optional] 
 **softDeleted** | **Boolean**| If true, only soft-deleted object versions will be listed. The default is false. For more information, see Soft Delete. | [optional] 
 **startOffset** | **String**| Filter results to objects whose names are lexicographically equal to or after startOffset. If endOffset is also set, the objects listed will have names between startOffset (inclusive) and endOffset (exclusive). | [optional] 
 **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] 
 **versions** | **Boolean**| If true, lists all versions of an object as distinct results. The default is false. For more information, see Object Versioning. | [optional] 

### Return type

[**Objects**](Objects.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storageObjectsPatch

> ModelObject storageObjectsPatch(bucket, object, opts)



Patches an object&#39;s metadata.

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

let apiInstance = new CloudStorageJsonApi.ObjectsApi();
let bucket = "bucket_example"; // String | Name of the bucket in which the object resides.
let object = "object_example"; // String | Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding).
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'uploadType': "uploadType_example", // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'generation': "generation_example", // String | If present, selects a specific revision of this object (as opposed to the latest version, the default).
  'ifGenerationMatch': "ifGenerationMatch_example", // String | Makes the operation conditional on whether the object's current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object.
  'ifGenerationNotMatch': "ifGenerationNotMatch_example", // String | Makes the operation conditional on whether the object's current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object.
  'ifMetagenerationMatch': "ifMetagenerationMatch_example", // String | Makes the operation conditional on whether the object's current metageneration matches the given value.
  'ifMetagenerationNotMatch': "ifMetagenerationNotMatch_example", // String | Makes the operation conditional on whether the object's current metageneration does not match the given value.
  'overrideUnlockedRetention': true, // Boolean | Must be true to remove the retention configuration, reduce its unlocked retention period, or change its mode from unlocked to locked.
  'predefinedAcl': "predefinedAcl_example", // String | Apply a predefined set of access controls to this object.
  'projection': "projection_example", // String | Set of properties to return. Defaults to full.
  'userProject': "userProject_example", // String | The project to be billed for this request, for Requester Pays buckets.
  'modelObject': new CloudStorageJsonApi.ModelObject() // ModelObject | 
};
apiInstance.storageObjectsPatch(bucket, object, opts, (error, data, response) => {
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
 **bucket** | **String**| Name of the bucket in which the object resides. | 
 **object** | **String**| Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding). | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **generation** | **String**| If present, selects a specific revision of this object (as opposed to the latest version, the default). | [optional] 
 **ifGenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object. | [optional] 
 **ifGenerationNotMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object. | [optional] 
 **ifMetagenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration matches the given value. | [optional] 
 **ifMetagenerationNotMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration does not match the given value. | [optional] 
 **overrideUnlockedRetention** | **Boolean**| Must be true to remove the retention configuration, reduce its unlocked retention period, or change its mode from unlocked to locked. | [optional] 
 **predefinedAcl** | **String**| Apply a predefined set of access controls to this object. | [optional] 
 **projection** | **String**| Set of properties to return. Defaults to full. | [optional] 
 **userProject** | **String**| The project to be billed for this request, for Requester Pays buckets. | [optional] 
 **modelObject** | [**ModelObject**](ModelObject.md)|  | [optional] 

### Return type

[**ModelObject**](ModelObject.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## storageObjectsRestore

> ModelObject storageObjectsRestore(bucket, object, generation, opts)



Restores a soft-deleted object.

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

let apiInstance = new CloudStorageJsonApi.ObjectsApi();
let bucket = "bucket_example"; // String | Name of the bucket in which the object resides.
let object = "object_example"; // String | Name of the object. For information about how to URL encode object names to be path safe, see Encoding URI Path Parts.
let generation = "generation_example"; // String | Selects a specific revision of this object.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'uploadType': "uploadType_example", // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'copySourceAcl': true, // Boolean | If true, copies the source object's ACL; otherwise, uses the bucket's default object ACL. The default is false.
  'ifGenerationMatch': "ifGenerationMatch_example", // String | Makes the operation conditional on whether the object's one live generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object.
  'ifGenerationNotMatch': "ifGenerationNotMatch_example", // String | Makes the operation conditional on whether none of the object's live generations match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object.
  'ifMetagenerationMatch': "ifMetagenerationMatch_example", // String | Makes the operation conditional on whether the object's one live metageneration matches the given value.
  'ifMetagenerationNotMatch': "ifMetagenerationNotMatch_example", // String | Makes the operation conditional on whether none of the object's live metagenerations match the given value.
  'projection': "projection_example", // String | Set of properties to return. Defaults to full.
  'userProject': "userProject_example", // String | The project to be billed for this request. Required for Requester Pays buckets.
  'modelObject': new CloudStorageJsonApi.ModelObject() // ModelObject | 
};
apiInstance.storageObjectsRestore(bucket, object, generation, opts, (error, data, response) => {
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
 **bucket** | **String**| Name of the bucket in which the object resides. | 
 **object** | **String**| Name of the object. For information about how to URL encode object names to be path safe, see Encoding URI Path Parts. | 
 **generation** | **String**| Selects a specific revision of this object. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **copySourceAcl** | **Boolean**| If true, copies the source object&#39;s ACL; otherwise, uses the bucket&#39;s default object ACL. The default is false. | [optional] 
 **ifGenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s one live generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object. | [optional] 
 **ifGenerationNotMatch** | **String**| Makes the operation conditional on whether none of the object&#39;s live generations match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object. | [optional] 
 **ifMetagenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s one live metageneration matches the given value. | [optional] 
 **ifMetagenerationNotMatch** | **String**| Makes the operation conditional on whether none of the object&#39;s live metagenerations match the given value. | [optional] 
 **projection** | **String**| Set of properties to return. Defaults to full. | [optional] 
 **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] 
 **modelObject** | [**ModelObject**](ModelObject.md)|  | [optional] 

### Return type

[**ModelObject**](ModelObject.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## storageObjectsRewrite

> RewriteResponse storageObjectsRewrite(sourceBucket, sourceObject, destinationBucket, destinationObject, opts)



Rewrites a source object to a destination object. Optionally overrides metadata.

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

let apiInstance = new CloudStorageJsonApi.ObjectsApi();
let sourceBucket = "sourceBucket_example"; // String | Name of the bucket in which to find the source object.
let sourceObject = "sourceObject_example"; // String | Name of the source object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding).
let destinationBucket = "destinationBucket_example"; // String | Name of the bucket in which to store the new object. Overrides the provided object metadata's bucket value, if any.
let destinationObject = "destinationObject_example"; // String | Name of the new object. Required when the object metadata is not otherwise provided. Overrides the object metadata's name value, if any. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding).
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'uploadType': "uploadType_example", // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'destinationKmsKeyName': "destinationKmsKeyName_example", // String | Resource name of the Cloud KMS key, of the form projects/my-project/locations/global/keyRings/my-kr/cryptoKeys/my-key, that will be used to encrypt the object. Overrides the object metadata's kms_key_name value, if any.
  'destinationPredefinedAcl': "destinationPredefinedAcl_example", // String | Apply a predefined set of access controls to the destination object.
  'ifGenerationMatch': "ifGenerationMatch_example", // String | Makes the operation conditional on whether the object's current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object.
  'ifGenerationNotMatch': "ifGenerationNotMatch_example", // String | Makes the operation conditional on whether the object's current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object.
  'ifMetagenerationMatch': "ifMetagenerationMatch_example", // String | Makes the operation conditional on whether the destination object's current metageneration matches the given value.
  'ifMetagenerationNotMatch': "ifMetagenerationNotMatch_example", // String | Makes the operation conditional on whether the destination object's current metageneration does not match the given value.
  'ifSourceGenerationMatch': "ifSourceGenerationMatch_example", // String | Makes the operation conditional on whether the source object's current generation matches the given value.
  'ifSourceGenerationNotMatch': "ifSourceGenerationNotMatch_example", // String | Makes the operation conditional on whether the source object's current generation does not match the given value.
  'ifSourceMetagenerationMatch': "ifSourceMetagenerationMatch_example", // String | Makes the operation conditional on whether the source object's current metageneration matches the given value.
  'ifSourceMetagenerationNotMatch': "ifSourceMetagenerationNotMatch_example", // String | Makes the operation conditional on whether the source object's current metageneration does not match the given value.
  'maxBytesRewrittenPerCall': "maxBytesRewrittenPerCall_example", // String | The maximum number of bytes that will be rewritten per rewrite request. Most callers shouldn't need to specify this parameter - it is primarily in place to support testing. If specified the value must be an integral multiple of 1 MiB (1048576). Also, this only applies to requests where the source and destination span locations and/or storage classes. Finally, this value must not change across rewrite calls else you'll get an error that the rewriteToken is invalid.
  'projection': "projection_example", // String | Set of properties to return. Defaults to noAcl, unless the object resource specifies the acl property, when it defaults to full.
  'rewriteToken': "rewriteToken_example", // String | Include this field (from the previous rewrite response) on each rewrite request after the first one, until the rewrite response 'done' flag is true. Calls that provide a rewriteToken can omit all other request fields, but if included those fields must match the values provided in the first rewrite request.
  'sourceGeneration': "sourceGeneration_example", // String | If present, selects a specific revision of the source object (as opposed to the latest version, the default).
  'userProject': "userProject_example", // String | The project to be billed for this request. Required for Requester Pays buckets.
  'modelObject': new CloudStorageJsonApi.ModelObject() // ModelObject | 
};
apiInstance.storageObjectsRewrite(sourceBucket, sourceObject, destinationBucket, destinationObject, opts, (error, data, response) => {
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
 **sourceBucket** | **String**| Name of the bucket in which to find the source object. | 
 **sourceObject** | **String**| Name of the source object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding). | 
 **destinationBucket** | **String**| Name of the bucket in which to store the new object. Overrides the provided object metadata&#39;s bucket value, if any. | 
 **destinationObject** | **String**| Name of the new object. Required when the object metadata is not otherwise provided. Overrides the object metadata&#39;s name value, if any. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding). | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **destinationKmsKeyName** | **String**| Resource name of the Cloud KMS key, of the form projects/my-project/locations/global/keyRings/my-kr/cryptoKeys/my-key, that will be used to encrypt the object. Overrides the object metadata&#39;s kms_key_name value, if any. | [optional] 
 **destinationPredefinedAcl** | **String**| Apply a predefined set of access controls to the destination object. | [optional] 
 **ifGenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object. | [optional] 
 **ifGenerationNotMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object. | [optional] 
 **ifMetagenerationMatch** | **String**| Makes the operation conditional on whether the destination object&#39;s current metageneration matches the given value. | [optional] 
 **ifMetagenerationNotMatch** | **String**| Makes the operation conditional on whether the destination object&#39;s current metageneration does not match the given value. | [optional] 
 **ifSourceGenerationMatch** | **String**| Makes the operation conditional on whether the source object&#39;s current generation matches the given value. | [optional] 
 **ifSourceGenerationNotMatch** | **String**| Makes the operation conditional on whether the source object&#39;s current generation does not match the given value. | [optional] 
 **ifSourceMetagenerationMatch** | **String**| Makes the operation conditional on whether the source object&#39;s current metageneration matches the given value. | [optional] 
 **ifSourceMetagenerationNotMatch** | **String**| Makes the operation conditional on whether the source object&#39;s current metageneration does not match the given value. | [optional] 
 **maxBytesRewrittenPerCall** | **String**| The maximum number of bytes that will be rewritten per rewrite request. Most callers shouldn&#39;t need to specify this parameter - it is primarily in place to support testing. If specified the value must be an integral multiple of 1 MiB (1048576). Also, this only applies to requests where the source and destination span locations and/or storage classes. Finally, this value must not change across rewrite calls else you&#39;ll get an error that the rewriteToken is invalid. | [optional] 
 **projection** | **String**| Set of properties to return. Defaults to noAcl, unless the object resource specifies the acl property, when it defaults to full. | [optional] 
 **rewriteToken** | **String**| Include this field (from the previous rewrite response) on each rewrite request after the first one, until the rewrite response &#39;done&#39; flag is true. Calls that provide a rewriteToken can omit all other request fields, but if included those fields must match the values provided in the first rewrite request. | [optional] 
 **sourceGeneration** | **String**| If present, selects a specific revision of the source object (as opposed to the latest version, the default). | [optional] 
 **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] 
 **modelObject** | [**ModelObject**](ModelObject.md)|  | [optional] 

### Return type

[**RewriteResponse**](RewriteResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## storageObjectsSetIamPolicy

> Policy storageObjectsSetIamPolicy(bucket, object, opts)



Updates an IAM policy for the specified object.

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

let apiInstance = new CloudStorageJsonApi.ObjectsApi();
let bucket = "bucket_example"; // String | Name of the bucket in which the object resides.
let object = "object_example"; // String | Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding).
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'uploadType': "uploadType_example", // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'generation': "generation_example", // String | If present, selects a specific revision of this object (as opposed to the latest version, the default).
  'userProject': "userProject_example", // String | The project to be billed for this request. Required for Requester Pays buckets.
  'policy': new CloudStorageJsonApi.Policy() // Policy | 
};
apiInstance.storageObjectsSetIamPolicy(bucket, object, opts, (error, data, response) => {
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
 **bucket** | **String**| Name of the bucket in which the object resides. | 
 **object** | **String**| Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding). | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **generation** | **String**| If present, selects a specific revision of this object (as opposed to the latest version, the default). | [optional] 
 **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] 
 **policy** | [**Policy**](Policy.md)|  | [optional] 

### Return type

[**Policy**](Policy.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## storageObjectsTestIamPermissions

> TestIamPermissionsResponse storageObjectsTestIamPermissions(bucket, object, permissions, opts)



Tests a set of permissions on the given object to see which, if any, are held by the caller.

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

let apiInstance = new CloudStorageJsonApi.ObjectsApi();
let bucket = "bucket_example"; // String | Name of the bucket in which the object resides.
let object = "object_example"; // String | Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding).
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
  'generation': "generation_example", // String | If present, selects a specific revision of this object (as opposed to the latest version, the default).
  'userProject': "userProject_example" // String | The project to be billed for this request. Required for Requester Pays buckets.
};
apiInstance.storageObjectsTestIamPermissions(bucket, object, permissions, opts, (error, data, response) => {
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
 **bucket** | **String**| Name of the bucket in which the object resides. | 
 **object** | **String**| Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding). | 
 **permissions** | [**[String]**](String.md)| Permissions to test. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **generation** | **String**| If present, selects a specific revision of this object (as opposed to the latest version, the default). | [optional] 
 **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] 

### Return type

[**TestIamPermissionsResponse**](TestIamPermissionsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storageObjectsUpdate

> ModelObject storageObjectsUpdate(bucket, object, opts)



Updates an object&#39;s metadata.

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

let apiInstance = new CloudStorageJsonApi.ObjectsApi();
let bucket = "bucket_example"; // String | Name of the bucket in which the object resides.
let object = "object_example"; // String | Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding).
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'uploadType': "uploadType_example", // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'generation': "generation_example", // String | If present, selects a specific revision of this object (as opposed to the latest version, the default).
  'ifGenerationMatch': "ifGenerationMatch_example", // String | Makes the operation conditional on whether the object's current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object.
  'ifGenerationNotMatch': "ifGenerationNotMatch_example", // String | Makes the operation conditional on whether the object's current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object.
  'ifMetagenerationMatch': "ifMetagenerationMatch_example", // String | Makes the operation conditional on whether the object's current metageneration matches the given value.
  'ifMetagenerationNotMatch': "ifMetagenerationNotMatch_example", // String | Makes the operation conditional on whether the object's current metageneration does not match the given value.
  'overrideUnlockedRetention': true, // Boolean | Must be true to remove the retention configuration, reduce its unlocked retention period, or change its mode from unlocked to locked.
  'predefinedAcl': "predefinedAcl_example", // String | Apply a predefined set of access controls to this object.
  'projection': "projection_example", // String | Set of properties to return. Defaults to full.
  'userProject': "userProject_example", // String | The project to be billed for this request. Required for Requester Pays buckets.
  'modelObject': new CloudStorageJsonApi.ModelObject() // ModelObject | 
};
apiInstance.storageObjectsUpdate(bucket, object, opts, (error, data, response) => {
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
 **bucket** | **String**| Name of the bucket in which the object resides. | 
 **object** | **String**| Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding). | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **generation** | **String**| If present, selects a specific revision of this object (as opposed to the latest version, the default). | [optional] 
 **ifGenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object. | [optional] 
 **ifGenerationNotMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object. | [optional] 
 **ifMetagenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration matches the given value. | [optional] 
 **ifMetagenerationNotMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration does not match the given value. | [optional] 
 **overrideUnlockedRetention** | **Boolean**| Must be true to remove the retention configuration, reduce its unlocked retention period, or change its mode from unlocked to locked. | [optional] 
 **predefinedAcl** | **String**| Apply a predefined set of access controls to this object. | [optional] 
 **projection** | **String**| Set of properties to return. Defaults to full. | [optional] 
 **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] 
 **modelObject** | [**ModelObject**](ModelObject.md)|  | [optional] 

### Return type

[**ModelObject**](ModelObject.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## storageObjectsWatchAll

> Channel storageObjectsWatchAll(bucket, opts)



Watch for changes on all objects in a bucket.

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

let apiInstance = new CloudStorageJsonApi.ObjectsApi();
let bucket = "bucket_example"; // String | Name of the bucket in which to look for objects.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'uploadType': "uploadType_example", // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'delimiter': "delimiter_example", // String | Returns results in a directory-like mode. items will contain only objects whose names, aside from the prefix, do not contain delimiter. Objects whose names, aside from the prefix, contain delimiter will have their name, truncated after the delimiter, returned in prefixes. Duplicate prefixes are omitted.
  'endOffset': "endOffset_example", // String | Filter results to objects whose names are lexicographically before endOffset. If startOffset is also set, the objects listed will have names between startOffset (inclusive) and endOffset (exclusive).
  'includeTrailingDelimiter': true, // Boolean | If true, objects that end in exactly one instance of delimiter will have their metadata included in items in addition to prefixes.
  'maxResults': 56, // Number | Maximum number of items plus prefixes to return in a single page of responses. As duplicate prefixes are omitted, fewer total results may be returned than requested. The service will use this parameter or 1,000 items, whichever is smaller.
  'pageToken': "pageToken_example", // String | A previously-returned page token representing part of the larger set of results to view.
  'prefix': "prefix_example", // String | Filter results to objects whose names begin with this prefix.
  'projection': "projection_example", // String | Set of properties to return. Defaults to noAcl.
  'startOffset': "startOffset_example", // String | Filter results to objects whose names are lexicographically equal to or after startOffset. If endOffset is also set, the objects listed will have names between startOffset (inclusive) and endOffset (exclusive).
  'userProject': "userProject_example", // String | The project to be billed for this request. Required for Requester Pays buckets.
  'versions': true, // Boolean | If true, lists all versions of an object as distinct results. The default is false. For more information, see Object Versioning.
  'channel': new CloudStorageJsonApi.Channel() // Channel | 
};
apiInstance.storageObjectsWatchAll(bucket, opts, (error, data, response) => {
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
 **bucket** | **String**| Name of the bucket in which to look for objects. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **delimiter** | **String**| Returns results in a directory-like mode. items will contain only objects whose names, aside from the prefix, do not contain delimiter. Objects whose names, aside from the prefix, contain delimiter will have their name, truncated after the delimiter, returned in prefixes. Duplicate prefixes are omitted. | [optional] 
 **endOffset** | **String**| Filter results to objects whose names are lexicographically before endOffset. If startOffset is also set, the objects listed will have names between startOffset (inclusive) and endOffset (exclusive). | [optional] 
 **includeTrailingDelimiter** | **Boolean**| If true, objects that end in exactly one instance of delimiter will have their metadata included in items in addition to prefixes. | [optional] 
 **maxResults** | **Number**| Maximum number of items plus prefixes to return in a single page of responses. As duplicate prefixes are omitted, fewer total results may be returned than requested. The service will use this parameter or 1,000 items, whichever is smaller. | [optional] 
 **pageToken** | **String**| A previously-returned page token representing part of the larger set of results to view. | [optional] 
 **prefix** | **String**| Filter results to objects whose names begin with this prefix. | [optional] 
 **projection** | **String**| Set of properties to return. Defaults to noAcl. | [optional] 
 **startOffset** | **String**| Filter results to objects whose names are lexicographically equal to or after startOffset. If endOffset is also set, the objects listed will have names between startOffset (inclusive) and endOffset (exclusive). | [optional] 
 **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] 
 **versions** | **Boolean**| If true, lists all versions of an object as distinct results. The default is false. For more information, see Object Versioning. | [optional] 
 **channel** | [**Channel**](Channel.md)|  | [optional] 

### Return type

[**Channel**](Channel.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

