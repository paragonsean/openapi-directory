# ObjectAccessControlsApi

All URIs are relative to *https://storage.googleapis.com/storage/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**storageObjectAccessControlsDelete**](ObjectAccessControlsApi.md#storageObjectAccessControlsDelete) | **DELETE** /b/{bucket}/o/{object}/acl/{entity} |  |
| [**storageObjectAccessControlsGet**](ObjectAccessControlsApi.md#storageObjectAccessControlsGet) | **GET** /b/{bucket}/o/{object}/acl/{entity} |  |
| [**storageObjectAccessControlsInsert**](ObjectAccessControlsApi.md#storageObjectAccessControlsInsert) | **POST** /b/{bucket}/o/{object}/acl |  |
| [**storageObjectAccessControlsList**](ObjectAccessControlsApi.md#storageObjectAccessControlsList) | **GET** /b/{bucket}/o/{object}/acl |  |
| [**storageObjectAccessControlsPatch**](ObjectAccessControlsApi.md#storageObjectAccessControlsPatch) | **PATCH** /b/{bucket}/o/{object}/acl/{entity} |  |
| [**storageObjectAccessControlsUpdate**](ObjectAccessControlsApi.md#storageObjectAccessControlsUpdate) | **PUT** /b/{bucket}/o/{object}/acl/{entity} |  |


<a id="storageObjectAccessControlsDelete"></a>
# **storageObjectAccessControlsDelete**
> storageObjectAccessControlsDelete(bucket, _object, entity, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, generation, userProject)



Permanently deletes the ACL entry for the specified entity on the specified object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectAccessControlsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://storage.googleapis.com/storage/v1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ObjectAccessControlsApi apiInstance = new ObjectAccessControlsApi(defaultClient);
    String bucket = "bucket_example"; // String | Name of a bucket.
    String _object = "_object_example"; // String | Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding).
    String entity = "entity_example"; // String | The entity holding the permission. Can be user-userId, user-emailAddress, group-groupId, group-emailAddress, allUsers, or allAuthenticatedUsers.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String uploadType = "uploadType_example"; // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String generation = "generation_example"; // String | If present, selects a specific revision of this object (as opposed to the latest version, the default).
    String userProject = "userProject_example"; // String | The project to be billed for this request. Required for Requester Pays buckets.
    try {
      apiInstance.storageObjectAccessControlsDelete(bucket, _object, entity, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, generation, userProject);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectAccessControlsApi#storageObjectAccessControlsDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **bucket** | **String**| Name of a bucket. | |
| **_object** | **String**| Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding). | |
| **entity** | **String**| The entity holding the permission. Can be user-userId, user-emailAddress, group-groupId, group-emailAddress, allUsers, or allAuthenticatedUsers. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **generation** | **String**| If present, selects a specific revision of this object (as opposed to the latest version, the default). | [optional] |
| **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] |

### Return type

null (empty response body)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="storageObjectAccessControlsGet"></a>
# **storageObjectAccessControlsGet**
> ObjectAccessControl storageObjectAccessControlsGet(bucket, _object, entity, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, generation, userProject)



Returns the ACL entry for the specified entity on the specified object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectAccessControlsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://storage.googleapis.com/storage/v1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ObjectAccessControlsApi apiInstance = new ObjectAccessControlsApi(defaultClient);
    String bucket = "bucket_example"; // String | Name of a bucket.
    String _object = "_object_example"; // String | Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding).
    String entity = "entity_example"; // String | The entity holding the permission. Can be user-userId, user-emailAddress, group-groupId, group-emailAddress, allUsers, or allAuthenticatedUsers.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String uploadType = "uploadType_example"; // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String generation = "generation_example"; // String | If present, selects a specific revision of this object (as opposed to the latest version, the default).
    String userProject = "userProject_example"; // String | The project to be billed for this request. Required for Requester Pays buckets.
    try {
      ObjectAccessControl result = apiInstance.storageObjectAccessControlsGet(bucket, _object, entity, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, generation, userProject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectAccessControlsApi#storageObjectAccessControlsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **bucket** | **String**| Name of a bucket. | |
| **_object** | **String**| Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding). | |
| **entity** | **String**| The entity holding the permission. Can be user-userId, user-emailAddress, group-groupId, group-emailAddress, allUsers, or allAuthenticatedUsers. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **generation** | **String**| If present, selects a specific revision of this object (as opposed to the latest version, the default). | [optional] |
| **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] |

### Return type

[**ObjectAccessControl**](ObjectAccessControl.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="storageObjectAccessControlsInsert"></a>
# **storageObjectAccessControlsInsert**
> ObjectAccessControl storageObjectAccessControlsInsert(bucket, _object, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, generation, userProject, objectAccessControl)



Creates a new ACL entry on the specified object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectAccessControlsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://storage.googleapis.com/storage/v1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ObjectAccessControlsApi apiInstance = new ObjectAccessControlsApi(defaultClient);
    String bucket = "bucket_example"; // String | Name of a bucket.
    String _object = "_object_example"; // String | Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding).
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String uploadType = "uploadType_example"; // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String generation = "generation_example"; // String | If present, selects a specific revision of this object (as opposed to the latest version, the default).
    String userProject = "userProject_example"; // String | The project to be billed for this request. Required for Requester Pays buckets.
    ObjectAccessControl objectAccessControl = new ObjectAccessControl(); // ObjectAccessControl | 
    try {
      ObjectAccessControl result = apiInstance.storageObjectAccessControlsInsert(bucket, _object, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, generation, userProject, objectAccessControl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectAccessControlsApi#storageObjectAccessControlsInsert");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **bucket** | **String**| Name of a bucket. | |
| **_object** | **String**| Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding). | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **generation** | **String**| If present, selects a specific revision of this object (as opposed to the latest version, the default). | [optional] |
| **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] |
| **objectAccessControl** | [**ObjectAccessControl**](ObjectAccessControl.md)|  | [optional] |

### Return type

[**ObjectAccessControl**](ObjectAccessControl.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="storageObjectAccessControlsList"></a>
# **storageObjectAccessControlsList**
> ObjectAccessControls storageObjectAccessControlsList(bucket, _object, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, generation, userProject)



Retrieves ACL entries on the specified object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectAccessControlsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://storage.googleapis.com/storage/v1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ObjectAccessControlsApi apiInstance = new ObjectAccessControlsApi(defaultClient);
    String bucket = "bucket_example"; // String | Name of a bucket.
    String _object = "_object_example"; // String | Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding).
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String uploadType = "uploadType_example"; // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String generation = "generation_example"; // String | If present, selects a specific revision of this object (as opposed to the latest version, the default).
    String userProject = "userProject_example"; // String | The project to be billed for this request. Required for Requester Pays buckets.
    try {
      ObjectAccessControls result = apiInstance.storageObjectAccessControlsList(bucket, _object, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, generation, userProject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectAccessControlsApi#storageObjectAccessControlsList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **bucket** | **String**| Name of a bucket. | |
| **_object** | **String**| Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding). | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **generation** | **String**| If present, selects a specific revision of this object (as opposed to the latest version, the default). | [optional] |
| **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] |

### Return type

[**ObjectAccessControls**](ObjectAccessControls.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="storageObjectAccessControlsPatch"></a>
# **storageObjectAccessControlsPatch**
> ObjectAccessControl storageObjectAccessControlsPatch(bucket, _object, entity, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, generation, userProject, objectAccessControl)



Patches an ACL entry on the specified object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectAccessControlsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://storage.googleapis.com/storage/v1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ObjectAccessControlsApi apiInstance = new ObjectAccessControlsApi(defaultClient);
    String bucket = "bucket_example"; // String | Name of a bucket.
    String _object = "_object_example"; // String | Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding).
    String entity = "entity_example"; // String | The entity holding the permission. Can be user-userId, user-emailAddress, group-groupId, group-emailAddress, allUsers, or allAuthenticatedUsers.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String uploadType = "uploadType_example"; // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String generation = "generation_example"; // String | If present, selects a specific revision of this object (as opposed to the latest version, the default).
    String userProject = "userProject_example"; // String | The project to be billed for this request. Required for Requester Pays buckets.
    ObjectAccessControl objectAccessControl = new ObjectAccessControl(); // ObjectAccessControl | 
    try {
      ObjectAccessControl result = apiInstance.storageObjectAccessControlsPatch(bucket, _object, entity, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, generation, userProject, objectAccessControl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectAccessControlsApi#storageObjectAccessControlsPatch");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **bucket** | **String**| Name of a bucket. | |
| **_object** | **String**| Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding). | |
| **entity** | **String**| The entity holding the permission. Can be user-userId, user-emailAddress, group-groupId, group-emailAddress, allUsers, or allAuthenticatedUsers. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **generation** | **String**| If present, selects a specific revision of this object (as opposed to the latest version, the default). | [optional] |
| **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] |
| **objectAccessControl** | [**ObjectAccessControl**](ObjectAccessControl.md)|  | [optional] |

### Return type

[**ObjectAccessControl**](ObjectAccessControl.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="storageObjectAccessControlsUpdate"></a>
# **storageObjectAccessControlsUpdate**
> ObjectAccessControl storageObjectAccessControlsUpdate(bucket, _object, entity, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, generation, userProject, objectAccessControl)



Updates an ACL entry on the specified object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectAccessControlsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://storage.googleapis.com/storage/v1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ObjectAccessControlsApi apiInstance = new ObjectAccessControlsApi(defaultClient);
    String bucket = "bucket_example"; // String | Name of a bucket.
    String _object = "_object_example"; // String | Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding).
    String entity = "entity_example"; // String | The entity holding the permission. Can be user-userId, user-emailAddress, group-groupId, group-emailAddress, allUsers, or allAuthenticatedUsers.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String uploadType = "uploadType_example"; // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String generation = "generation_example"; // String | If present, selects a specific revision of this object (as opposed to the latest version, the default).
    String userProject = "userProject_example"; // String | The project to be billed for this request. Required for Requester Pays buckets.
    ObjectAccessControl objectAccessControl = new ObjectAccessControl(); // ObjectAccessControl | 
    try {
      ObjectAccessControl result = apiInstance.storageObjectAccessControlsUpdate(bucket, _object, entity, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, generation, userProject, objectAccessControl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectAccessControlsApi#storageObjectAccessControlsUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **bucket** | **String**| Name of a bucket. | |
| **_object** | **String**| Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding). | |
| **entity** | **String**| The entity holding the permission. Can be user-userId, user-emailAddress, group-groupId, group-emailAddress, allUsers, or allAuthenticatedUsers. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **generation** | **String**| If present, selects a specific revision of this object (as opposed to the latest version, the default). | [optional] |
| **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] |
| **objectAccessControl** | [**ObjectAccessControl**](ObjectAccessControl.md)|  | [optional] |

### Return type

[**ObjectAccessControl**](ObjectAccessControl.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

