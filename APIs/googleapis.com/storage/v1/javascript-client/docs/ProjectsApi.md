# CloudStorageJsonApi.ProjectsApi

All URIs are relative to *https://storage.googleapis.com/storage/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storageProjectsHmacKeysCreate**](ProjectsApi.md#storageProjectsHmacKeysCreate) | **POST** /projects/{projectId}/hmacKeys | 
[**storageProjectsHmacKeysDelete**](ProjectsApi.md#storageProjectsHmacKeysDelete) | **DELETE** /projects/{projectId}/hmacKeys/{accessId} | 
[**storageProjectsHmacKeysGet**](ProjectsApi.md#storageProjectsHmacKeysGet) | **GET** /projects/{projectId}/hmacKeys/{accessId} | 
[**storageProjectsHmacKeysList**](ProjectsApi.md#storageProjectsHmacKeysList) | **GET** /projects/{projectId}/hmacKeys | 
[**storageProjectsHmacKeysUpdate**](ProjectsApi.md#storageProjectsHmacKeysUpdate) | **PUT** /projects/{projectId}/hmacKeys/{accessId} | 
[**storageProjectsServiceAccountGet**](ProjectsApi.md#storageProjectsServiceAccountGet) | **GET** /projects/{projectId}/serviceAccount | 



## storageProjectsHmacKeysCreate

> HmacKey storageProjectsHmacKeysCreate(projectId, serviceAccountEmail, opts)



Creates a new HMAC key for the specified service account.

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

let apiInstance = new CloudStorageJsonApi.ProjectsApi();
let projectId = "projectId_example"; // String | Project ID owning the service account.
let serviceAccountEmail = "serviceAccountEmail_example"; // String | Email address of the service account.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'uploadType': "uploadType_example", // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'userProject': "userProject_example" // String | The project to be billed for this request.
};
apiInstance.storageProjectsHmacKeysCreate(projectId, serviceAccountEmail, opts, (error, data, response) => {
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
 **projectId** | **String**| Project ID owning the service account. | 
 **serviceAccountEmail** | **String**| Email address of the service account. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **userProject** | **String**| The project to be billed for this request. | [optional] 

### Return type

[**HmacKey**](HmacKey.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storageProjectsHmacKeysDelete

> storageProjectsHmacKeysDelete(projectId, accessId, opts)



Deletes an HMAC key.

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

let apiInstance = new CloudStorageJsonApi.ProjectsApi();
let projectId = "projectId_example"; // String | Project ID owning the requested key
let accessId = "accessId_example"; // String | Name of the HMAC key to be deleted.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'uploadType': "uploadType_example", // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'userProject': "userProject_example" // String | The project to be billed for this request.
};
apiInstance.storageProjectsHmacKeysDelete(projectId, accessId, opts, (error, data, response) => {
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
 **projectId** | **String**| Project ID owning the requested key | 
 **accessId** | **String**| Name of the HMAC key to be deleted. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **userProject** | **String**| The project to be billed for this request. | [optional] 

### Return type

null (empty response body)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## storageProjectsHmacKeysGet

> HmacKeyMetadata storageProjectsHmacKeysGet(projectId, accessId, opts)



Retrieves an HMAC key&#39;s metadata

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

let apiInstance = new CloudStorageJsonApi.ProjectsApi();
let projectId = "projectId_example"; // String | Project ID owning the service account of the requested key.
let accessId = "accessId_example"; // String | Name of the HMAC key.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'uploadType': "uploadType_example", // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'userProject': "userProject_example" // String | The project to be billed for this request.
};
apiInstance.storageProjectsHmacKeysGet(projectId, accessId, opts, (error, data, response) => {
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
 **projectId** | **String**| Project ID owning the service account of the requested key. | 
 **accessId** | **String**| Name of the HMAC key. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **userProject** | **String**| The project to be billed for this request. | [optional] 

### Return type

[**HmacKeyMetadata**](HmacKeyMetadata.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storageProjectsHmacKeysList

> HmacKeysMetadata storageProjectsHmacKeysList(projectId, opts)



Retrieves a list of HMAC keys matching the criteria.

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

let apiInstance = new CloudStorageJsonApi.ProjectsApi();
let projectId = "projectId_example"; // String | Name of the project in which to look for HMAC keys.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'uploadType': "uploadType_example", // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'maxResults': 56, // Number | Maximum number of items to return in a single page of responses. The service uses this parameter or 250 items, whichever is smaller. The max number of items per page will also be limited by the number of distinct service accounts in the response. If the number of service accounts in a single response is too high, the page will truncated and a next page token will be returned.
  'pageToken': "pageToken_example", // String | A previously-returned page token representing part of the larger set of results to view.
  'serviceAccountEmail': "serviceAccountEmail_example", // String | If present, only keys for the given service account are returned.
  'showDeletedKeys': true, // Boolean | Whether or not to show keys in the DELETED state.
  'userProject': "userProject_example" // String | The project to be billed for this request.
};
apiInstance.storageProjectsHmacKeysList(projectId, opts, (error, data, response) => {
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
 **projectId** | **String**| Name of the project in which to look for HMAC keys. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **maxResults** | **Number**| Maximum number of items to return in a single page of responses. The service uses this parameter or 250 items, whichever is smaller. The max number of items per page will also be limited by the number of distinct service accounts in the response. If the number of service accounts in a single response is too high, the page will truncated and a next page token will be returned. | [optional] 
 **pageToken** | **String**| A previously-returned page token representing part of the larger set of results to view. | [optional] 
 **serviceAccountEmail** | **String**| If present, only keys for the given service account are returned. | [optional] 
 **showDeletedKeys** | **Boolean**| Whether or not to show keys in the DELETED state. | [optional] 
 **userProject** | **String**| The project to be billed for this request. | [optional] 

### Return type

[**HmacKeysMetadata**](HmacKeysMetadata.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storageProjectsHmacKeysUpdate

> HmacKeyMetadata storageProjectsHmacKeysUpdate(projectId, accessId, opts)



Updates the state of an HMAC key. See the HMAC Key resource descriptor for valid states.

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

let apiInstance = new CloudStorageJsonApi.ProjectsApi();
let projectId = "projectId_example"; // String | Project ID owning the service account of the updated key.
let accessId = "accessId_example"; // String | Name of the HMAC key being updated.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'uploadType': "uploadType_example", // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'userProject': "userProject_example", // String | The project to be billed for this request.
  'hmacKeyMetadata': new CloudStorageJsonApi.HmacKeyMetadata() // HmacKeyMetadata | 
};
apiInstance.storageProjectsHmacKeysUpdate(projectId, accessId, opts, (error, data, response) => {
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
 **projectId** | **String**| Project ID owning the service account of the updated key. | 
 **accessId** | **String**| Name of the HMAC key being updated. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **userProject** | **String**| The project to be billed for this request. | [optional] 
 **hmacKeyMetadata** | [**HmacKeyMetadata**](HmacKeyMetadata.md)|  | [optional] 

### Return type

[**HmacKeyMetadata**](HmacKeyMetadata.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## storageProjectsServiceAccountGet

> ServiceAccount storageProjectsServiceAccountGet(projectId, opts)



Get the email address of this project&#39;s Google Cloud Storage service account.

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

let apiInstance = new CloudStorageJsonApi.ProjectsApi();
let projectId = "projectId_example"; // String | Project ID
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'uploadType': "uploadType_example", // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'userProject': "userProject_example" // String | The project to be billed for this request.
};
apiInstance.storageProjectsServiceAccountGet(projectId, opts, (error, data, response) => {
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
 **projectId** | **String**| Project ID | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **userProject** | **String**| The project to be billed for this request. | [optional] 

### Return type

[**ServiceAccount**](ServiceAccount.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

