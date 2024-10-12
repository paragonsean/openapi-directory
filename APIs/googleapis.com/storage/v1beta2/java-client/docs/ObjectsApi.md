# ObjectsApi

All URIs are relative to *https://storage.googleapis.com/storage/v1beta2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**storageObjectsCompose**](ObjectsApi.md#storageObjectsCompose) | **POST** /b/{destinationBucket}/o/{destinationObject}/compose |  |
| [**storageObjectsCopy**](ObjectsApi.md#storageObjectsCopy) | **POST** /b/{sourceBucket}/o/{sourceObject}/copyTo/b/{destinationBucket}/o/{destinationObject} |  |
| [**storageObjectsDelete**](ObjectsApi.md#storageObjectsDelete) | **DELETE** /b/{bucket}/o/{object} |  |
| [**storageObjectsGet**](ObjectsApi.md#storageObjectsGet) | **GET** /b/{bucket}/o/{object} |  |
| [**storageObjectsInsert**](ObjectsApi.md#storageObjectsInsert) | **POST** /b/{bucket}/o |  |
| [**storageObjectsList**](ObjectsApi.md#storageObjectsList) | **GET** /b/{bucket}/o |  |
| [**storageObjectsPatch**](ObjectsApi.md#storageObjectsPatch) | **PATCH** /b/{bucket}/o/{object} |  |
| [**storageObjectsUpdate**](ObjectsApi.md#storageObjectsUpdate) | **PUT** /b/{bucket}/o/{object} |  |
| [**storageObjectsWatchAll**](ObjectsApi.md#storageObjectsWatchAll) | **POST** /b/{bucket}/o/watch |  |


<a id="storageObjectsCompose"></a>
# **storageObjectsCompose**
> ModelObject storageObjectsCompose(destinationBucket, destinationObject, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, ifGenerationMatch, ifMetagenerationMatch, composeRequest)



Concatenates a list of existing objects into a new object in the same bucket.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://storage.googleapis.com/storage/v1beta2");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ObjectsApi apiInstance = new ObjectsApi(defaultClient);
    String destinationBucket = "destinationBucket_example"; // String | Name of the bucket containing the source objects. The destination object is stored in this bucket.
    String destinationObject = "destinationObject_example"; // String | Name of the new object.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String ifGenerationMatch = "ifGenerationMatch_example"; // String | Makes the operation conditional on whether the object's current generation matches the given value.
    String ifMetagenerationMatch = "ifMetagenerationMatch_example"; // String | Makes the operation conditional on whether the object's current metageneration matches the given value.
    ComposeRequest composeRequest = new ComposeRequest(); // ComposeRequest | 
    try {
      ModelObject result = apiInstance.storageObjectsCompose(destinationBucket, destinationObject, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, ifGenerationMatch, ifMetagenerationMatch, composeRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectsApi#storageObjectsCompose");
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
| **destinationBucket** | **String**| Name of the bucket containing the source objects. The destination object is stored in this bucket. | |
| **destinationObject** | **String**| Name of the new object. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **ifGenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation matches the given value. | [optional] |
| **ifMetagenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration matches the given value. | [optional] |
| **composeRequest** | [**ComposeRequest**](ComposeRequest.md)|  | [optional] |

### Return type

[**ModelObject**](ModelObject.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="storageObjectsCopy"></a>
# **storageObjectsCopy**
> ModelObject storageObjectsCopy(sourceBucket, sourceObject, destinationBucket, destinationObject, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, ifGenerationMatch, ifGenerationNotMatch, ifMetagenerationMatch, ifMetagenerationNotMatch, ifSourceGenerationMatch, ifSourceGenerationNotMatch, ifSourceMetagenerationMatch, ifSourceMetagenerationNotMatch, projection, sourceGeneration, modelObject)



Copies an object to a destination in the same location. Optionally overrides metadata.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://storage.googleapis.com/storage/v1beta2");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ObjectsApi apiInstance = new ObjectsApi(defaultClient);
    String sourceBucket = "sourceBucket_example"; // String | Name of the bucket in which to find the source object.
    String sourceObject = "sourceObject_example"; // String | Name of the source object.
    String destinationBucket = "destinationBucket_example"; // String | Name of the bucket in which to store the new object. Overrides the provided object metadata's bucket value, if any.
    String destinationObject = "destinationObject_example"; // String | Name of the new object. Required when the object metadata is not otherwise provided. Overrides the object metadata's name value, if any.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String ifGenerationMatch = "ifGenerationMatch_example"; // String | Makes the operation conditional on whether the destination object's current generation matches the given value.
    String ifGenerationNotMatch = "ifGenerationNotMatch_example"; // String | Makes the operation conditional on whether the destination object's current generation does not match the given value.
    String ifMetagenerationMatch = "ifMetagenerationMatch_example"; // String | Makes the operation conditional on whether the destination object's current metageneration matches the given value.
    String ifMetagenerationNotMatch = "ifMetagenerationNotMatch_example"; // String | Makes the operation conditional on whether the destination object's current metageneration does not match the given value.
    String ifSourceGenerationMatch = "ifSourceGenerationMatch_example"; // String | Makes the operation conditional on whether the source object's generation matches the given value.
    String ifSourceGenerationNotMatch = "ifSourceGenerationNotMatch_example"; // String | Makes the operation conditional on whether the source object's generation does not match the given value.
    String ifSourceMetagenerationMatch = "ifSourceMetagenerationMatch_example"; // String | Makes the operation conditional on whether the source object's current metageneration matches the given value.
    String ifSourceMetagenerationNotMatch = "ifSourceMetagenerationNotMatch_example"; // String | Makes the operation conditional on whether the source object's current metageneration does not match the given value.
    String projection = "full"; // String | Set of properties to return. Defaults to noAcl, unless the object resource specifies the acl property, when it defaults to full.
    String sourceGeneration = "sourceGeneration_example"; // String | If present, selects a specific revision of the source object (as opposed to the latest version, the default).
    ModelObject modelObject = new ModelObject(); // ModelObject | 
    try {
      ModelObject result = apiInstance.storageObjectsCopy(sourceBucket, sourceObject, destinationBucket, destinationObject, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, ifGenerationMatch, ifGenerationNotMatch, ifMetagenerationMatch, ifMetagenerationNotMatch, ifSourceGenerationMatch, ifSourceGenerationNotMatch, ifSourceMetagenerationMatch, ifSourceMetagenerationNotMatch, projection, sourceGeneration, modelObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectsApi#storageObjectsCopy");
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
| **sourceBucket** | **String**| Name of the bucket in which to find the source object. | |
| **sourceObject** | **String**| Name of the source object. | |
| **destinationBucket** | **String**| Name of the bucket in which to store the new object. Overrides the provided object metadata&#39;s bucket value, if any. | |
| **destinationObject** | **String**| Name of the new object. Required when the object metadata is not otherwise provided. Overrides the object metadata&#39;s name value, if any. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **ifGenerationMatch** | **String**| Makes the operation conditional on whether the destination object&#39;s current generation matches the given value. | [optional] |
| **ifGenerationNotMatch** | **String**| Makes the operation conditional on whether the destination object&#39;s current generation does not match the given value. | [optional] |
| **ifMetagenerationMatch** | **String**| Makes the operation conditional on whether the destination object&#39;s current metageneration matches the given value. | [optional] |
| **ifMetagenerationNotMatch** | **String**| Makes the operation conditional on whether the destination object&#39;s current metageneration does not match the given value. | [optional] |
| **ifSourceGenerationMatch** | **String**| Makes the operation conditional on whether the source object&#39;s generation matches the given value. | [optional] |
| **ifSourceGenerationNotMatch** | **String**| Makes the operation conditional on whether the source object&#39;s generation does not match the given value. | [optional] |
| **ifSourceMetagenerationMatch** | **String**| Makes the operation conditional on whether the source object&#39;s current metageneration matches the given value. | [optional] |
| **ifSourceMetagenerationNotMatch** | **String**| Makes the operation conditional on whether the source object&#39;s current metageneration does not match the given value. | [optional] |
| **projection** | **String**| Set of properties to return. Defaults to noAcl, unless the object resource specifies the acl property, when it defaults to full. | [optional] [enum: full, noAcl] |
| **sourceGeneration** | **String**| If present, selects a specific revision of the source object (as opposed to the latest version, the default). | [optional] |
| **modelObject** | [**ModelObject**](ModelObject.md)|  | [optional] |

### Return type

[**ModelObject**](ModelObject.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="storageObjectsDelete"></a>
# **storageObjectsDelete**
> storageObjectsDelete(bucket, _object, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, generation, ifGenerationMatch, ifGenerationNotMatch, ifMetagenerationMatch, ifMetagenerationNotMatch)



Deletes data blobs and associated metadata. Deletions are permanent if versioning is not enabled for the bucket, or if the generation parameter is used.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://storage.googleapis.com/storage/v1beta2");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ObjectsApi apiInstance = new ObjectsApi(defaultClient);
    String bucket = "bucket_example"; // String | Name of the bucket in which the object resides.
    String _object = "_object_example"; // String | Name of the object.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String generation = "generation_example"; // String | If present, permanently deletes a specific revision of this object (as opposed to the latest version, the default).
    String ifGenerationMatch = "ifGenerationMatch_example"; // String | Makes the operation conditional on whether the object's current generation matches the given value.
    String ifGenerationNotMatch = "ifGenerationNotMatch_example"; // String | Makes the operation conditional on whether the object's current generation does not match the given value.
    String ifMetagenerationMatch = "ifMetagenerationMatch_example"; // String | Makes the operation conditional on whether the object's current metageneration matches the given value.
    String ifMetagenerationNotMatch = "ifMetagenerationNotMatch_example"; // String | Makes the operation conditional on whether the object's current metageneration does not match the given value.
    try {
      apiInstance.storageObjectsDelete(bucket, _object, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, generation, ifGenerationMatch, ifGenerationNotMatch, ifMetagenerationMatch, ifMetagenerationNotMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectsApi#storageObjectsDelete");
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
| **bucket** | **String**| Name of the bucket in which the object resides. | |
| **_object** | **String**| Name of the object. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **generation** | **String**| If present, permanently deletes a specific revision of this object (as opposed to the latest version, the default). | [optional] |
| **ifGenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation matches the given value. | [optional] |
| **ifGenerationNotMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation does not match the given value. | [optional] |
| **ifMetagenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration matches the given value. | [optional] |
| **ifMetagenerationNotMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration does not match the given value. | [optional] |

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

<a id="storageObjectsGet"></a>
# **storageObjectsGet**
> ModelObject storageObjectsGet(bucket, _object, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, generation, ifGenerationMatch, ifGenerationNotMatch, ifMetagenerationMatch, ifMetagenerationNotMatch, projection)



Retrieves objects or their associated metadata.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://storage.googleapis.com/storage/v1beta2");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ObjectsApi apiInstance = new ObjectsApi(defaultClient);
    String bucket = "bucket_example"; // String | Name of the bucket in which the object resides.
    String _object = "_object_example"; // String | Name of the object.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String generation = "generation_example"; // String | If present, selects a specific revision of this object (as opposed to the latest version, the default).
    String ifGenerationMatch = "ifGenerationMatch_example"; // String | Makes the operation conditional on whether the object's generation matches the given value.
    String ifGenerationNotMatch = "ifGenerationNotMatch_example"; // String | Makes the operation conditional on whether the object's generation does not match the given value.
    String ifMetagenerationMatch = "ifMetagenerationMatch_example"; // String | Makes the operation conditional on whether the object's current metageneration matches the given value.
    String ifMetagenerationNotMatch = "ifMetagenerationNotMatch_example"; // String | Makes the operation conditional on whether the object's current metageneration does not match the given value.
    String projection = "full"; // String | Set of properties to return. Defaults to noAcl.
    try {
      ModelObject result = apiInstance.storageObjectsGet(bucket, _object, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, generation, ifGenerationMatch, ifGenerationNotMatch, ifMetagenerationMatch, ifMetagenerationNotMatch, projection);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectsApi#storageObjectsGet");
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
| **bucket** | **String**| Name of the bucket in which the object resides. | |
| **_object** | **String**| Name of the object. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **generation** | **String**| If present, selects a specific revision of this object (as opposed to the latest version, the default). | [optional] |
| **ifGenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s generation matches the given value. | [optional] |
| **ifGenerationNotMatch** | **String**| Makes the operation conditional on whether the object&#39;s generation does not match the given value. | [optional] |
| **ifMetagenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration matches the given value. | [optional] |
| **ifMetagenerationNotMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration does not match the given value. | [optional] |
| **projection** | **String**| Set of properties to return. Defaults to noAcl. | [optional] [enum: full, noAcl] |

### Return type

[**ModelObject**](ModelObject.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="storageObjectsInsert"></a>
# **storageObjectsInsert**
> ModelObject storageObjectsInsert(bucket, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, ifGenerationMatch, ifGenerationNotMatch, ifMetagenerationMatch, ifMetagenerationNotMatch, name, projection, modelObject)



Stores new data blobs and associated metadata.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://storage.googleapis.com/storage/v1beta2");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ObjectsApi apiInstance = new ObjectsApi(defaultClient);
    String bucket = "bucket_example"; // String | Name of the bucket in which to store the new object. Overrides the provided object metadata's bucket value, if any.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String ifGenerationMatch = "ifGenerationMatch_example"; // String | Makes the operation conditional on whether the object's current generation matches the given value.
    String ifGenerationNotMatch = "ifGenerationNotMatch_example"; // String | Makes the operation conditional on whether the object's current generation does not match the given value.
    String ifMetagenerationMatch = "ifMetagenerationMatch_example"; // String | Makes the operation conditional on whether the object's current metageneration matches the given value.
    String ifMetagenerationNotMatch = "ifMetagenerationNotMatch_example"; // String | Makes the operation conditional on whether the object's current metageneration does not match the given value.
    String name = "name_example"; // String | Name of the object. Required when the object metadata is not otherwise provided. Overrides the object metadata's name value, if any.
    String projection = "full"; // String | Set of properties to return. Defaults to noAcl, unless the object resource specifies the acl property, when it defaults to full.
    ModelObject modelObject = new ModelObject(); // ModelObject | 
    try {
      ModelObject result = apiInstance.storageObjectsInsert(bucket, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, ifGenerationMatch, ifGenerationNotMatch, ifMetagenerationMatch, ifMetagenerationNotMatch, name, projection, modelObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectsApi#storageObjectsInsert");
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
| **bucket** | **String**| Name of the bucket in which to store the new object. Overrides the provided object metadata&#39;s bucket value, if any. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **ifGenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation matches the given value. | [optional] |
| **ifGenerationNotMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation does not match the given value. | [optional] |
| **ifMetagenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration matches the given value. | [optional] |
| **ifMetagenerationNotMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration does not match the given value. | [optional] |
| **name** | **String**| Name of the object. Required when the object metadata is not otherwise provided. Overrides the object metadata&#39;s name value, if any. | [optional] |
| **projection** | **String**| Set of properties to return. Defaults to noAcl, unless the object resource specifies the acl property, when it defaults to full. | [optional] [enum: full, noAcl] |
| **modelObject** | [**ModelObject**](ModelObject.md)|  | [optional] |

### Return type

[**ModelObject**](ModelObject.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="storageObjectsList"></a>
# **storageObjectsList**
> Objects storageObjectsList(bucket, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, delimiter, maxResults, pageToken, prefix, projection, versions)



Retrieves a list of objects matching the criteria.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://storage.googleapis.com/storage/v1beta2");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ObjectsApi apiInstance = new ObjectsApi(defaultClient);
    String bucket = "bucket_example"; // String | Name of the bucket in which to look for objects.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String delimiter = "delimiter_example"; // String | Returns results in a directory-like mode. items will contain only objects whose names, aside from the prefix, do not contain delimiter. Objects whose names, aside from the prefix, contain delimiter will have their name, truncated after the delimiter, returned in prefixes. Duplicate prefixes are omitted.
    Integer maxResults = 56; // Integer | Maximum number of items plus prefixes to return. As duplicate prefixes are omitted, fewer total results may be returned than requested.
    String pageToken = "pageToken_example"; // String | A previously-returned page token representing part of the larger set of results to view.
    String prefix = "prefix_example"; // String | Filter results to objects whose names begin with this prefix.
    String projection = "full"; // String | Set of properties to return. Defaults to noAcl.
    Boolean versions = true; // Boolean | If true, lists all versions of a file as distinct results.
    try {
      Objects result = apiInstance.storageObjectsList(bucket, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, delimiter, maxResults, pageToken, prefix, projection, versions);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectsApi#storageObjectsList");
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
| **bucket** | **String**| Name of the bucket in which to look for objects. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **delimiter** | **String**| Returns results in a directory-like mode. items will contain only objects whose names, aside from the prefix, do not contain delimiter. Objects whose names, aside from the prefix, contain delimiter will have their name, truncated after the delimiter, returned in prefixes. Duplicate prefixes are omitted. | [optional] |
| **maxResults** | **Integer**| Maximum number of items plus prefixes to return. As duplicate prefixes are omitted, fewer total results may be returned than requested. | [optional] |
| **pageToken** | **String**| A previously-returned page token representing part of the larger set of results to view. | [optional] |
| **prefix** | **String**| Filter results to objects whose names begin with this prefix. | [optional] |
| **projection** | **String**| Set of properties to return. Defaults to noAcl. | [optional] [enum: full, noAcl] |
| **versions** | **Boolean**| If true, lists all versions of a file as distinct results. | [optional] |

### Return type

[**Objects**](Objects.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="storageObjectsPatch"></a>
# **storageObjectsPatch**
> ModelObject storageObjectsPatch(bucket, _object, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, generation, ifGenerationMatch, ifGenerationNotMatch, ifMetagenerationMatch, ifMetagenerationNotMatch, projection, modelObject)



Updates a data blob&#39;s associated metadata. This method supports patch semantics.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://storage.googleapis.com/storage/v1beta2");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ObjectsApi apiInstance = new ObjectsApi(defaultClient);
    String bucket = "bucket_example"; // String | Name of the bucket in which the object resides.
    String _object = "_object_example"; // String | Name of the object.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String generation = "generation_example"; // String | If present, selects a specific revision of this object (as opposed to the latest version, the default).
    String ifGenerationMatch = "ifGenerationMatch_example"; // String | Makes the operation conditional on whether the object's current generation matches the given value.
    String ifGenerationNotMatch = "ifGenerationNotMatch_example"; // String | Makes the operation conditional on whether the object's current generation does not match the given value.
    String ifMetagenerationMatch = "ifMetagenerationMatch_example"; // String | Makes the operation conditional on whether the object's current metageneration matches the given value.
    String ifMetagenerationNotMatch = "ifMetagenerationNotMatch_example"; // String | Makes the operation conditional on whether the object's current metageneration does not match the given value.
    String projection = "full"; // String | Set of properties to return. Defaults to full.
    ModelObject modelObject = new ModelObject(); // ModelObject | 
    try {
      ModelObject result = apiInstance.storageObjectsPatch(bucket, _object, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, generation, ifGenerationMatch, ifGenerationNotMatch, ifMetagenerationMatch, ifMetagenerationNotMatch, projection, modelObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectsApi#storageObjectsPatch");
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
| **bucket** | **String**| Name of the bucket in which the object resides. | |
| **_object** | **String**| Name of the object. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **generation** | **String**| If present, selects a specific revision of this object (as opposed to the latest version, the default). | [optional] |
| **ifGenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation matches the given value. | [optional] |
| **ifGenerationNotMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation does not match the given value. | [optional] |
| **ifMetagenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration matches the given value. | [optional] |
| **ifMetagenerationNotMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration does not match the given value. | [optional] |
| **projection** | **String**| Set of properties to return. Defaults to full. | [optional] [enum: full, noAcl] |
| **modelObject** | [**ModelObject**](ModelObject.md)|  | [optional] |

### Return type

[**ModelObject**](ModelObject.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="storageObjectsUpdate"></a>
# **storageObjectsUpdate**
> ModelObject storageObjectsUpdate(bucket, _object, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, generation, ifGenerationMatch, ifGenerationNotMatch, ifMetagenerationMatch, ifMetagenerationNotMatch, projection, modelObject)



Updates a data blob&#39;s associated metadata.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://storage.googleapis.com/storage/v1beta2");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ObjectsApi apiInstance = new ObjectsApi(defaultClient);
    String bucket = "bucket_example"; // String | Name of the bucket in which the object resides.
    String _object = "_object_example"; // String | Name of the object.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String generation = "generation_example"; // String | If present, selects a specific revision of this object (as opposed to the latest version, the default).
    String ifGenerationMatch = "ifGenerationMatch_example"; // String | Makes the operation conditional on whether the object's current generation matches the given value.
    String ifGenerationNotMatch = "ifGenerationNotMatch_example"; // String | Makes the operation conditional on whether the object's current generation does not match the given value.
    String ifMetagenerationMatch = "ifMetagenerationMatch_example"; // String | Makes the operation conditional on whether the object's current metageneration matches the given value.
    String ifMetagenerationNotMatch = "ifMetagenerationNotMatch_example"; // String | Makes the operation conditional on whether the object's current metageneration does not match the given value.
    String projection = "full"; // String | Set of properties to return. Defaults to full.
    ModelObject modelObject = new ModelObject(); // ModelObject | 
    try {
      ModelObject result = apiInstance.storageObjectsUpdate(bucket, _object, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, generation, ifGenerationMatch, ifGenerationNotMatch, ifMetagenerationMatch, ifMetagenerationNotMatch, projection, modelObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectsApi#storageObjectsUpdate");
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
| **bucket** | **String**| Name of the bucket in which the object resides. | |
| **_object** | **String**| Name of the object. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **generation** | **String**| If present, selects a specific revision of this object (as opposed to the latest version, the default). | [optional] |
| **ifGenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation matches the given value. | [optional] |
| **ifGenerationNotMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation does not match the given value. | [optional] |
| **ifMetagenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration matches the given value. | [optional] |
| **ifMetagenerationNotMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration does not match the given value. | [optional] |
| **projection** | **String**| Set of properties to return. Defaults to full. | [optional] [enum: full, noAcl] |
| **modelObject** | [**ModelObject**](ModelObject.md)|  | [optional] |

### Return type

[**ModelObject**](ModelObject.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="storageObjectsWatchAll"></a>
# **storageObjectsWatchAll**
> Channel storageObjectsWatchAll(bucket, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, delimiter, maxResults, pageToken, prefix, projection, versions, channel)



Watch for changes on all objects in a bucket.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://storage.googleapis.com/storage/v1beta2");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ObjectsApi apiInstance = new ObjectsApi(defaultClient);
    String bucket = "bucket_example"; // String | Name of the bucket in which to look for objects.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String delimiter = "delimiter_example"; // String | Returns results in a directory-like mode. items will contain only objects whose names, aside from the prefix, do not contain delimiter. Objects whose names, aside from the prefix, contain delimiter will have their name, truncated after the delimiter, returned in prefixes. Duplicate prefixes are omitted.
    Integer maxResults = 56; // Integer | Maximum number of items plus prefixes to return. As duplicate prefixes are omitted, fewer total results may be returned than requested.
    String pageToken = "pageToken_example"; // String | A previously-returned page token representing part of the larger set of results to view.
    String prefix = "prefix_example"; // String | Filter results to objects whose names begin with this prefix.
    String projection = "full"; // String | Set of properties to return. Defaults to noAcl.
    Boolean versions = true; // Boolean | If true, lists all versions of a file as distinct results.
    Channel channel = new Channel(); // Channel | 
    try {
      Channel result = apiInstance.storageObjectsWatchAll(bucket, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, delimiter, maxResults, pageToken, prefix, projection, versions, channel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectsApi#storageObjectsWatchAll");
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
| **bucket** | **String**| Name of the bucket in which to look for objects. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **delimiter** | **String**| Returns results in a directory-like mode. items will contain only objects whose names, aside from the prefix, do not contain delimiter. Objects whose names, aside from the prefix, contain delimiter will have their name, truncated after the delimiter, returned in prefixes. Duplicate prefixes are omitted. | [optional] |
| **maxResults** | **Integer**| Maximum number of items plus prefixes to return. As duplicate prefixes are omitted, fewer total results may be returned than requested. | [optional] |
| **pageToken** | **String**| A previously-returned page token representing part of the larger set of results to view. | [optional] |
| **prefix** | **String**| Filter results to objects whose names begin with this prefix. | [optional] |
| **projection** | **String**| Set of properties to return. Defaults to noAcl. | [optional] [enum: full, noAcl] |
| **versions** | **Boolean**| If true, lists all versions of a file as distinct results. | [optional] |
| **channel** | [**Channel**](Channel.md)|  | [optional] |

### Return type

[**Channel**](Channel.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

