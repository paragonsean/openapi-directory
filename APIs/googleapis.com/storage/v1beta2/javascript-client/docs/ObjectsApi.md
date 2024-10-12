# CloudStorageJsonApi.ObjectsApi

All URIs are relative to *https://storage.googleapis.com/storage/v1beta2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storageObjectsCompose**](ObjectsApi.md#storageObjectsCompose) | **POST** /b/{destinationBucket}/o/{destinationObject}/compose | 
[**storageObjectsCopy**](ObjectsApi.md#storageObjectsCopy) | **POST** /b/{sourceBucket}/o/{sourceObject}/copyTo/b/{destinationBucket}/o/{destinationObject} | 
[**storageObjectsDelete**](ObjectsApi.md#storageObjectsDelete) | **DELETE** /b/{bucket}/o/{object} | 
[**storageObjectsGet**](ObjectsApi.md#storageObjectsGet) | **GET** /b/{bucket}/o/{object} | 
[**storageObjectsInsert**](ObjectsApi.md#storageObjectsInsert) | **POST** /b/{bucket}/o | 
[**storageObjectsList**](ObjectsApi.md#storageObjectsList) | **GET** /b/{bucket}/o | 
[**storageObjectsPatch**](ObjectsApi.md#storageObjectsPatch) | **PATCH** /b/{bucket}/o/{object} | 
[**storageObjectsUpdate**](ObjectsApi.md#storageObjectsUpdate) | **PUT** /b/{bucket}/o/{object} | 
[**storageObjectsWatchAll**](ObjectsApi.md#storageObjectsWatchAll) | **POST** /b/{bucket}/o/watch | 



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
let destinationObject = "destinationObject_example"; // String | Name of the new object.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'ifGenerationMatch': "ifGenerationMatch_example", // String | Makes the operation conditional on whether the object's current generation matches the given value.
  'ifMetagenerationMatch': "ifMetagenerationMatch_example", // String | Makes the operation conditional on whether the object's current metageneration matches the given value.
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
 **destinationObject** | **String**| Name of the new object. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **ifGenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation matches the given value. | [optional] 
 **ifMetagenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration matches the given value. | [optional] 
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



Copies an object to a destination in the same location. Optionally overrides metadata.

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
let sourceObject = "sourceObject_example"; // String | Name of the source object.
let destinationBucket = "destinationBucket_example"; // String | Name of the bucket in which to store the new object. Overrides the provided object metadata's bucket value, if any.
let destinationObject = "destinationObject_example"; // String | Name of the new object. Required when the object metadata is not otherwise provided. Overrides the object metadata's name value, if any.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'ifGenerationMatch': "ifGenerationMatch_example", // String | Makes the operation conditional on whether the destination object's current generation matches the given value.
  'ifGenerationNotMatch': "ifGenerationNotMatch_example", // String | Makes the operation conditional on whether the destination object's current generation does not match the given value.
  'ifMetagenerationMatch': "ifMetagenerationMatch_example", // String | Makes the operation conditional on whether the destination object's current metageneration matches the given value.
  'ifMetagenerationNotMatch': "ifMetagenerationNotMatch_example", // String | Makes the operation conditional on whether the destination object's current metageneration does not match the given value.
  'ifSourceGenerationMatch': "ifSourceGenerationMatch_example", // String | Makes the operation conditional on whether the source object's generation matches the given value.
  'ifSourceGenerationNotMatch': "ifSourceGenerationNotMatch_example", // String | Makes the operation conditional on whether the source object's generation does not match the given value.
  'ifSourceMetagenerationMatch': "ifSourceMetagenerationMatch_example", // String | Makes the operation conditional on whether the source object's current metageneration matches the given value.
  'ifSourceMetagenerationNotMatch': "ifSourceMetagenerationNotMatch_example", // String | Makes the operation conditional on whether the source object's current metageneration does not match the given value.
  'projection': "projection_example", // String | Set of properties to return. Defaults to noAcl, unless the object resource specifies the acl property, when it defaults to full.
  'sourceGeneration': "sourceGeneration_example", // String | If present, selects a specific revision of the source object (as opposed to the latest version, the default).
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
 **sourceObject** | **String**| Name of the source object. | 
 **destinationBucket** | **String**| Name of the bucket in which to store the new object. Overrides the provided object metadata&#39;s bucket value, if any. | 
 **destinationObject** | **String**| Name of the new object. Required when the object metadata is not otherwise provided. Overrides the object metadata&#39;s name value, if any. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **ifGenerationMatch** | **String**| Makes the operation conditional on whether the destination object&#39;s current generation matches the given value. | [optional] 
 **ifGenerationNotMatch** | **String**| Makes the operation conditional on whether the destination object&#39;s current generation does not match the given value. | [optional] 
 **ifMetagenerationMatch** | **String**| Makes the operation conditional on whether the destination object&#39;s current metageneration matches the given value. | [optional] 
 **ifMetagenerationNotMatch** | **String**| Makes the operation conditional on whether the destination object&#39;s current metageneration does not match the given value. | [optional] 
 **ifSourceGenerationMatch** | **String**| Makes the operation conditional on whether the source object&#39;s generation matches the given value. | [optional] 
 **ifSourceGenerationNotMatch** | **String**| Makes the operation conditional on whether the source object&#39;s generation does not match the given value. | [optional] 
 **ifSourceMetagenerationMatch** | **String**| Makes the operation conditional on whether the source object&#39;s current metageneration matches the given value. | [optional] 
 **ifSourceMetagenerationNotMatch** | **String**| Makes the operation conditional on whether the source object&#39;s current metageneration does not match the given value. | [optional] 
 **projection** | **String**| Set of properties to return. Defaults to noAcl, unless the object resource specifies the acl property, when it defaults to full. | [optional] 
 **sourceGeneration** | **String**| If present, selects a specific revision of the source object (as opposed to the latest version, the default). | [optional] 
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



Deletes data blobs and associated metadata. Deletions are permanent if versioning is not enabled for the bucket, or if the generation parameter is used.

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
let object = "object_example"; // String | Name of the object.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'generation': "generation_example", // String | If present, permanently deletes a specific revision of this object (as opposed to the latest version, the default).
  'ifGenerationMatch': "ifGenerationMatch_example", // String | Makes the operation conditional on whether the object's current generation matches the given value.
  'ifGenerationNotMatch': "ifGenerationNotMatch_example", // String | Makes the operation conditional on whether the object's current generation does not match the given value.
  'ifMetagenerationMatch': "ifMetagenerationMatch_example", // String | Makes the operation conditional on whether the object's current metageneration matches the given value.
  'ifMetagenerationNotMatch': "ifMetagenerationNotMatch_example" // String | Makes the operation conditional on whether the object's current metageneration does not match the given value.
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
 **object** | **String**| Name of the object. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **generation** | **String**| If present, permanently deletes a specific revision of this object (as opposed to the latest version, the default). | [optional] 
 **ifGenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation matches the given value. | [optional] 
 **ifGenerationNotMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation does not match the given value. | [optional] 
 **ifMetagenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration matches the given value. | [optional] 
 **ifMetagenerationNotMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration does not match the given value. | [optional] 

### Return type

null (empty response body)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## storageObjectsGet

> ModelObject storageObjectsGet(bucket, object, opts)



Retrieves objects or their associated metadata.

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
let object = "object_example"; // String | Name of the object.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'generation': "generation_example", // String | If present, selects a specific revision of this object (as opposed to the latest version, the default).
  'ifGenerationMatch': "ifGenerationMatch_example", // String | Makes the operation conditional on whether the object's generation matches the given value.
  'ifGenerationNotMatch': "ifGenerationNotMatch_example", // String | Makes the operation conditional on whether the object's generation does not match the given value.
  'ifMetagenerationMatch': "ifMetagenerationMatch_example", // String | Makes the operation conditional on whether the object's current metageneration matches the given value.
  'ifMetagenerationNotMatch': "ifMetagenerationNotMatch_example", // String | Makes the operation conditional on whether the object's current metageneration does not match the given value.
  'projection': "projection_example" // String | Set of properties to return. Defaults to noAcl.
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
 **object** | **String**| Name of the object. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **generation** | **String**| If present, selects a specific revision of this object (as opposed to the latest version, the default). | [optional] 
 **ifGenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s generation matches the given value. | [optional] 
 **ifGenerationNotMatch** | **String**| Makes the operation conditional on whether the object&#39;s generation does not match the given value. | [optional] 
 **ifMetagenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration matches the given value. | [optional] 
 **ifMetagenerationNotMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration does not match the given value. | [optional] 
 **projection** | **String**| Set of properties to return. Defaults to noAcl. | [optional] 

### Return type

[**ModelObject**](ModelObject.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storageObjectsInsert

> ModelObject storageObjectsInsert(bucket, opts)



Stores new data blobs and associated metadata.

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
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'ifGenerationMatch': "ifGenerationMatch_example", // String | Makes the operation conditional on whether the object's current generation matches the given value.
  'ifGenerationNotMatch': "ifGenerationNotMatch_example", // String | Makes the operation conditional on whether the object's current generation does not match the given value.
  'ifMetagenerationMatch': "ifMetagenerationMatch_example", // String | Makes the operation conditional on whether the object's current metageneration matches the given value.
  'ifMetagenerationNotMatch': "ifMetagenerationNotMatch_example", // String | Makes the operation conditional on whether the object's current metageneration does not match the given value.
  'name': "name_example", // String | Name of the object. Required when the object metadata is not otherwise provided. Overrides the object metadata's name value, if any.
  'projection': "projection_example", // String | Set of properties to return. Defaults to noAcl, unless the object resource specifies the acl property, when it defaults to full.
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
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **ifGenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation matches the given value. | [optional] 
 **ifGenerationNotMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation does not match the given value. | [optional] 
 **ifMetagenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration matches the given value. | [optional] 
 **ifMetagenerationNotMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration does not match the given value. | [optional] 
 **name** | **String**| Name of the object. Required when the object metadata is not otherwise provided. Overrides the object metadata&#39;s name value, if any. | [optional] 
 **projection** | **String**| Set of properties to return. Defaults to noAcl, unless the object resource specifies the acl property, when it defaults to full. | [optional] 
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
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'delimiter': "delimiter_example", // String | Returns results in a directory-like mode. items will contain only objects whose names, aside from the prefix, do not contain delimiter. Objects whose names, aside from the prefix, contain delimiter will have their name, truncated after the delimiter, returned in prefixes. Duplicate prefixes are omitted.
  'maxResults': 56, // Number | Maximum number of items plus prefixes to return. As duplicate prefixes are omitted, fewer total results may be returned than requested.
  'pageToken': "pageToken_example", // String | A previously-returned page token representing part of the larger set of results to view.
  'prefix': "prefix_example", // String | Filter results to objects whose names begin with this prefix.
  'projection': "projection_example", // String | Set of properties to return. Defaults to noAcl.
  'versions': true // Boolean | If true, lists all versions of a file as distinct results.
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
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **delimiter** | **String**| Returns results in a directory-like mode. items will contain only objects whose names, aside from the prefix, do not contain delimiter. Objects whose names, aside from the prefix, contain delimiter will have their name, truncated after the delimiter, returned in prefixes. Duplicate prefixes are omitted. | [optional] 
 **maxResults** | **Number**| Maximum number of items plus prefixes to return. As duplicate prefixes are omitted, fewer total results may be returned than requested. | [optional] 
 **pageToken** | **String**| A previously-returned page token representing part of the larger set of results to view. | [optional] 
 **prefix** | **String**| Filter results to objects whose names begin with this prefix. | [optional] 
 **projection** | **String**| Set of properties to return. Defaults to noAcl. | [optional] 
 **versions** | **Boolean**| If true, lists all versions of a file as distinct results. | [optional] 

### Return type

[**Objects**](Objects.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storageObjectsPatch

> ModelObject storageObjectsPatch(bucket, object, opts)



Updates a data blob&#39;s associated metadata. This method supports patch semantics.

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
let object = "object_example"; // String | Name of the object.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'generation': "generation_example", // String | If present, selects a specific revision of this object (as opposed to the latest version, the default).
  'ifGenerationMatch': "ifGenerationMatch_example", // String | Makes the operation conditional on whether the object's current generation matches the given value.
  'ifGenerationNotMatch': "ifGenerationNotMatch_example", // String | Makes the operation conditional on whether the object's current generation does not match the given value.
  'ifMetagenerationMatch': "ifMetagenerationMatch_example", // String | Makes the operation conditional on whether the object's current metageneration matches the given value.
  'ifMetagenerationNotMatch': "ifMetagenerationNotMatch_example", // String | Makes the operation conditional on whether the object's current metageneration does not match the given value.
  'projection': "projection_example", // String | Set of properties to return. Defaults to full.
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
 **object** | **String**| Name of the object. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **generation** | **String**| If present, selects a specific revision of this object (as opposed to the latest version, the default). | [optional] 
 **ifGenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation matches the given value. | [optional] 
 **ifGenerationNotMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation does not match the given value. | [optional] 
 **ifMetagenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration matches the given value. | [optional] 
 **ifMetagenerationNotMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration does not match the given value. | [optional] 
 **projection** | **String**| Set of properties to return. Defaults to full. | [optional] 
 **modelObject** | [**ModelObject**](ModelObject.md)|  | [optional] 

### Return type

[**ModelObject**](ModelObject.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## storageObjectsUpdate

> ModelObject storageObjectsUpdate(bucket, object, opts)



Updates a data blob&#39;s associated metadata.

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
let object = "object_example"; // String | Name of the object.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'generation': "generation_example", // String | If present, selects a specific revision of this object (as opposed to the latest version, the default).
  'ifGenerationMatch': "ifGenerationMatch_example", // String | Makes the operation conditional on whether the object's current generation matches the given value.
  'ifGenerationNotMatch': "ifGenerationNotMatch_example", // String | Makes the operation conditional on whether the object's current generation does not match the given value.
  'ifMetagenerationMatch': "ifMetagenerationMatch_example", // String | Makes the operation conditional on whether the object's current metageneration matches the given value.
  'ifMetagenerationNotMatch': "ifMetagenerationNotMatch_example", // String | Makes the operation conditional on whether the object's current metageneration does not match the given value.
  'projection': "projection_example", // String | Set of properties to return. Defaults to full.
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
 **object** | **String**| Name of the object. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **generation** | **String**| If present, selects a specific revision of this object (as opposed to the latest version, the default). | [optional] 
 **ifGenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation matches the given value. | [optional] 
 **ifGenerationNotMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation does not match the given value. | [optional] 
 **ifMetagenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration matches the given value. | [optional] 
 **ifMetagenerationNotMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration does not match the given value. | [optional] 
 **projection** | **String**| Set of properties to return. Defaults to full. | [optional] 
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
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'delimiter': "delimiter_example", // String | Returns results in a directory-like mode. items will contain only objects whose names, aside from the prefix, do not contain delimiter. Objects whose names, aside from the prefix, contain delimiter will have their name, truncated after the delimiter, returned in prefixes. Duplicate prefixes are omitted.
  'maxResults': 56, // Number | Maximum number of items plus prefixes to return. As duplicate prefixes are omitted, fewer total results may be returned than requested.
  'pageToken': "pageToken_example", // String | A previously-returned page token representing part of the larger set of results to view.
  'prefix': "prefix_example", // String | Filter results to objects whose names begin with this prefix.
  'projection': "projection_example", // String | Set of properties to return. Defaults to noAcl.
  'versions': true, // Boolean | If true, lists all versions of a file as distinct results.
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
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **delimiter** | **String**| Returns results in a directory-like mode. items will contain only objects whose names, aside from the prefix, do not contain delimiter. Objects whose names, aside from the prefix, contain delimiter will have their name, truncated after the delimiter, returned in prefixes. Duplicate prefixes are omitted. | [optional] 
 **maxResults** | **Number**| Maximum number of items plus prefixes to return. As duplicate prefixes are omitted, fewer total results may be returned than requested. | [optional] 
 **pageToken** | **String**| A previously-returned page token representing part of the larger set of results to view. | [optional] 
 **prefix** | **String**| Filter results to objects whose names begin with this prefix. | [optional] 
 **projection** | **String**| Set of properties to return. Defaults to noAcl. | [optional] 
 **versions** | **Boolean**| If true, lists all versions of a file as distinct results. | [optional] 
 **channel** | [**Channel**](Channel.md)|  | [optional] 

### Return type

[**Channel**](Channel.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

