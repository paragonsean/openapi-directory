# ObjectsApi

All URIs are relative to *https://storage.googleapis.com/storage/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**storageObjectsBulkRestore**](ObjectsApi.md#storageObjectsBulkRestore) | **POST** /b/{bucket}/o/bulkRestore |  |
| [**storageObjectsCompose**](ObjectsApi.md#storageObjectsCompose) | **POST** /b/{destinationBucket}/o/{destinationObject}/compose |  |
| [**storageObjectsCopy**](ObjectsApi.md#storageObjectsCopy) | **POST** /b/{sourceBucket}/o/{sourceObject}/copyTo/b/{destinationBucket}/o/{destinationObject} |  |
| [**storageObjectsDelete**](ObjectsApi.md#storageObjectsDelete) | **DELETE** /b/{bucket}/o/{object} |  |
| [**storageObjectsGet**](ObjectsApi.md#storageObjectsGet) | **GET** /b/{bucket}/o/{object} |  |
| [**storageObjectsGetIamPolicy**](ObjectsApi.md#storageObjectsGetIamPolicy) | **GET** /b/{bucket}/o/{object}/iam |  |
| [**storageObjectsInsert**](ObjectsApi.md#storageObjectsInsert) | **POST** /b/{bucket}/o |  |
| [**storageObjectsList**](ObjectsApi.md#storageObjectsList) | **GET** /b/{bucket}/o |  |
| [**storageObjectsPatch**](ObjectsApi.md#storageObjectsPatch) | **PATCH** /b/{bucket}/o/{object} |  |
| [**storageObjectsRestore**](ObjectsApi.md#storageObjectsRestore) | **POST** /b/{bucket}/o/{object}/restore |  |
| [**storageObjectsRewrite**](ObjectsApi.md#storageObjectsRewrite) | **POST** /b/{sourceBucket}/o/{sourceObject}/rewriteTo/b/{destinationBucket}/o/{destinationObject} |  |
| [**storageObjectsSetIamPolicy**](ObjectsApi.md#storageObjectsSetIamPolicy) | **PUT** /b/{bucket}/o/{object}/iam |  |
| [**storageObjectsTestIamPermissions**](ObjectsApi.md#storageObjectsTestIamPermissions) | **GET** /b/{bucket}/o/{object}/iam/testPermissions |  |
| [**storageObjectsUpdate**](ObjectsApi.md#storageObjectsUpdate) | **PUT** /b/{bucket}/o/{object} |  |
| [**storageObjectsWatchAll**](ObjectsApi.md#storageObjectsWatchAll) | **POST** /b/{bucket}/o/watch |  |


<a id="storageObjectsBulkRestore"></a>
# **storageObjectsBulkRestore**
> GoogleLongrunningOperation storageObjectsBulkRestore(bucket, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, bulkRestoreObjectsRequest)



Initiates a long-running bulk restore operation on the specified bucket.

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
    defaultClient.setBasePath("https://storage.googleapis.com/storage/v1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ObjectsApi apiInstance = new ObjectsApi(defaultClient);
    String bucket = "bucket_example"; // String | Name of the bucket in which the object resides.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String uploadType = "uploadType_example"; // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    BulkRestoreObjectsRequest bulkRestoreObjectsRequest = new BulkRestoreObjectsRequest(); // BulkRestoreObjectsRequest | 
    try {
      GoogleLongrunningOperation result = apiInstance.storageObjectsBulkRestore(bucket, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, bulkRestoreObjectsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectsApi#storageObjectsBulkRestore");
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
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **bulkRestoreObjectsRequest** | [**BulkRestoreObjectsRequest**](BulkRestoreObjectsRequest.md)|  | [optional] |

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="storageObjectsCompose"></a>
# **storageObjectsCompose**
> ModelObject storageObjectsCompose(destinationBucket, destinationObject, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, destinationPredefinedAcl, ifGenerationMatch, ifMetagenerationMatch, kmsKeyName, userProject, composeRequest)



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
    defaultClient.setBasePath("https://storage.googleapis.com/storage/v1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ObjectsApi apiInstance = new ObjectsApi(defaultClient);
    String destinationBucket = "destinationBucket_example"; // String | Name of the bucket containing the source objects. The destination object is stored in this bucket.
    String destinationObject = "destinationObject_example"; // String | Name of the new object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding).
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String uploadType = "uploadType_example"; // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String destinationPredefinedAcl = "authenticatedRead"; // String | Apply a predefined set of access controls to the destination object.
    String ifGenerationMatch = "ifGenerationMatch_example"; // String | Makes the operation conditional on whether the object's current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object.
    String ifMetagenerationMatch = "ifMetagenerationMatch_example"; // String | Makes the operation conditional on whether the object's current metageneration matches the given value.
    String kmsKeyName = "kmsKeyName_example"; // String | Resource name of the Cloud KMS key, of the form projects/my-project/locations/global/keyRings/my-kr/cryptoKeys/my-key, that will be used to encrypt the object. Overrides the object metadata's kms_key_name value, if any.
    String userProject = "userProject_example"; // String | The project to be billed for this request. Required for Requester Pays buckets.
    ComposeRequest composeRequest = new ComposeRequest(); // ComposeRequest | 
    try {
      ModelObject result = apiInstance.storageObjectsCompose(destinationBucket, destinationObject, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, destinationPredefinedAcl, ifGenerationMatch, ifMetagenerationMatch, kmsKeyName, userProject, composeRequest);
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
| **destinationObject** | **String**| Name of the new object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding). | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **destinationPredefinedAcl** | **String**| Apply a predefined set of access controls to the destination object. | [optional] [enum: authenticatedRead, bucketOwnerFullControl, bucketOwnerRead, private, projectPrivate, publicRead] |
| **ifGenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object. | [optional] |
| **ifMetagenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration matches the given value. | [optional] |
| **kmsKeyName** | **String**| Resource name of the Cloud KMS key, of the form projects/my-project/locations/global/keyRings/my-kr/cryptoKeys/my-key, that will be used to encrypt the object. Overrides the object metadata&#39;s kms_key_name value, if any. | [optional] |
| **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] |
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
> ModelObject storageObjectsCopy(sourceBucket, sourceObject, destinationBucket, destinationObject, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, destinationKmsKeyName, destinationPredefinedAcl, ifGenerationMatch, ifGenerationNotMatch, ifMetagenerationMatch, ifMetagenerationNotMatch, ifSourceGenerationMatch, ifSourceGenerationNotMatch, ifSourceMetagenerationMatch, ifSourceMetagenerationNotMatch, projection, sourceGeneration, userProject, modelObject)



Copies a source object to a destination object. Optionally overrides metadata.

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
    defaultClient.setBasePath("https://storage.googleapis.com/storage/v1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ObjectsApi apiInstance = new ObjectsApi(defaultClient);
    String sourceBucket = "sourceBucket_example"; // String | Name of the bucket in which to find the source object.
    String sourceObject = "sourceObject_example"; // String | Name of the source object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding).
    String destinationBucket = "destinationBucket_example"; // String | Name of the bucket in which to store the new object. Overrides the provided object metadata's bucket value, if any.For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding).
    String destinationObject = "destinationObject_example"; // String | Name of the new object. Required when the object metadata is not otherwise provided. Overrides the object metadata's name value, if any.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String uploadType = "uploadType_example"; // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String destinationKmsKeyName = "destinationKmsKeyName_example"; // String | Resource name of the Cloud KMS key, of the form projects/my-project/locations/global/keyRings/my-kr/cryptoKeys/my-key, that will be used to encrypt the object. Overrides the object metadata's kms_key_name value, if any.
    String destinationPredefinedAcl = "authenticatedRead"; // String | Apply a predefined set of access controls to the destination object.
    String ifGenerationMatch = "ifGenerationMatch_example"; // String | Makes the operation conditional on whether the destination object's current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object.
    String ifGenerationNotMatch = "ifGenerationNotMatch_example"; // String | Makes the operation conditional on whether the destination object's current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object.
    String ifMetagenerationMatch = "ifMetagenerationMatch_example"; // String | Makes the operation conditional on whether the destination object's current metageneration matches the given value.
    String ifMetagenerationNotMatch = "ifMetagenerationNotMatch_example"; // String | Makes the operation conditional on whether the destination object's current metageneration does not match the given value.
    String ifSourceGenerationMatch = "ifSourceGenerationMatch_example"; // String | Makes the operation conditional on whether the source object's current generation matches the given value.
    String ifSourceGenerationNotMatch = "ifSourceGenerationNotMatch_example"; // String | Makes the operation conditional on whether the source object's current generation does not match the given value.
    String ifSourceMetagenerationMatch = "ifSourceMetagenerationMatch_example"; // String | Makes the operation conditional on whether the source object's current metageneration matches the given value.
    String ifSourceMetagenerationNotMatch = "ifSourceMetagenerationNotMatch_example"; // String | Makes the operation conditional on whether the source object's current metageneration does not match the given value.
    String projection = "full"; // String | Set of properties to return. Defaults to noAcl, unless the object resource specifies the acl property, when it defaults to full.
    String sourceGeneration = "sourceGeneration_example"; // String | If present, selects a specific revision of the source object (as opposed to the latest version, the default).
    String userProject = "userProject_example"; // String | The project to be billed for this request. Required for Requester Pays buckets.
    ModelObject modelObject = new ModelObject(); // ModelObject | 
    try {
      ModelObject result = apiInstance.storageObjectsCopy(sourceBucket, sourceObject, destinationBucket, destinationObject, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, destinationKmsKeyName, destinationPredefinedAcl, ifGenerationMatch, ifGenerationNotMatch, ifMetagenerationMatch, ifMetagenerationNotMatch, ifSourceGenerationMatch, ifSourceGenerationNotMatch, ifSourceMetagenerationMatch, ifSourceMetagenerationNotMatch, projection, sourceGeneration, userProject, modelObject);
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
| **sourceObject** | **String**| Name of the source object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding). | |
| **destinationBucket** | **String**| Name of the bucket in which to store the new object. Overrides the provided object metadata&#39;s bucket value, if any.For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding). | |
| **destinationObject** | **String**| Name of the new object. Required when the object metadata is not otherwise provided. Overrides the object metadata&#39;s name value, if any. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **destinationKmsKeyName** | **String**| Resource name of the Cloud KMS key, of the form projects/my-project/locations/global/keyRings/my-kr/cryptoKeys/my-key, that will be used to encrypt the object. Overrides the object metadata&#39;s kms_key_name value, if any. | [optional] |
| **destinationPredefinedAcl** | **String**| Apply a predefined set of access controls to the destination object. | [optional] [enum: authenticatedRead, bucketOwnerFullControl, bucketOwnerRead, private, projectPrivate, publicRead] |
| **ifGenerationMatch** | **String**| Makes the operation conditional on whether the destination object&#39;s current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object. | [optional] |
| **ifGenerationNotMatch** | **String**| Makes the operation conditional on whether the destination object&#39;s current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object. | [optional] |
| **ifMetagenerationMatch** | **String**| Makes the operation conditional on whether the destination object&#39;s current metageneration matches the given value. | [optional] |
| **ifMetagenerationNotMatch** | **String**| Makes the operation conditional on whether the destination object&#39;s current metageneration does not match the given value. | [optional] |
| **ifSourceGenerationMatch** | **String**| Makes the operation conditional on whether the source object&#39;s current generation matches the given value. | [optional] |
| **ifSourceGenerationNotMatch** | **String**| Makes the operation conditional on whether the source object&#39;s current generation does not match the given value. | [optional] |
| **ifSourceMetagenerationMatch** | **String**| Makes the operation conditional on whether the source object&#39;s current metageneration matches the given value. | [optional] |
| **ifSourceMetagenerationNotMatch** | **String**| Makes the operation conditional on whether the source object&#39;s current metageneration does not match the given value. | [optional] |
| **projection** | **String**| Set of properties to return. Defaults to noAcl, unless the object resource specifies the acl property, when it defaults to full. | [optional] [enum: full, noAcl] |
| **sourceGeneration** | **String**| If present, selects a specific revision of the source object (as opposed to the latest version, the default). | [optional] |
| **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] |
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
> storageObjectsDelete(bucket, _object, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, generation, ifGenerationMatch, ifGenerationNotMatch, ifMetagenerationMatch, ifMetagenerationNotMatch, userProject)



Deletes an object and its metadata. Deletions are permanent if versioning is not enabled for the bucket, or if the generation parameter is used.

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
    defaultClient.setBasePath("https://storage.googleapis.com/storage/v1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ObjectsApi apiInstance = new ObjectsApi(defaultClient);
    String bucket = "bucket_example"; // String | Name of the bucket in which the object resides.
    String _object = "_object_example"; // String | Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding).
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String uploadType = "uploadType_example"; // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String generation = "generation_example"; // String | If present, permanently deletes a specific revision of this object (as opposed to the latest version, the default).
    String ifGenerationMatch = "ifGenerationMatch_example"; // String | Makes the operation conditional on whether the object's current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object.
    String ifGenerationNotMatch = "ifGenerationNotMatch_example"; // String | Makes the operation conditional on whether the object's current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object.
    String ifMetagenerationMatch = "ifMetagenerationMatch_example"; // String | Makes the operation conditional on whether the object's current metageneration matches the given value.
    String ifMetagenerationNotMatch = "ifMetagenerationNotMatch_example"; // String | Makes the operation conditional on whether the object's current metageneration does not match the given value.
    String userProject = "userProject_example"; // String | The project to be billed for this request. Required for Requester Pays buckets.
    try {
      apiInstance.storageObjectsDelete(bucket, _object, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, generation, ifGenerationMatch, ifGenerationNotMatch, ifMetagenerationMatch, ifMetagenerationNotMatch, userProject);
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
| **_object** | **String**| Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding). | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **generation** | **String**| If present, permanently deletes a specific revision of this object (as opposed to the latest version, the default). | [optional] |
| **ifGenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object. | [optional] |
| **ifGenerationNotMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object. | [optional] |
| **ifMetagenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration matches the given value. | [optional] |
| **ifMetagenerationNotMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration does not match the given value. | [optional] |
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

<a id="storageObjectsGet"></a>
# **storageObjectsGet**
> ModelObject storageObjectsGet(bucket, _object, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, generation, ifGenerationMatch, ifGenerationNotMatch, ifMetagenerationMatch, ifMetagenerationNotMatch, projection, softDeleted, userProject)



Retrieves an object or its metadata.

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
    defaultClient.setBasePath("https://storage.googleapis.com/storage/v1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ObjectsApi apiInstance = new ObjectsApi(defaultClient);
    String bucket = "bucket_example"; // String | Name of the bucket in which the object resides.
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
    String ifGenerationMatch = "ifGenerationMatch_example"; // String | Makes the operation conditional on whether the object's current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object.
    String ifGenerationNotMatch = "ifGenerationNotMatch_example"; // String | Makes the operation conditional on whether the object's current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object.
    String ifMetagenerationMatch = "ifMetagenerationMatch_example"; // String | Makes the operation conditional on whether the object's current metageneration matches the given value.
    String ifMetagenerationNotMatch = "ifMetagenerationNotMatch_example"; // String | Makes the operation conditional on whether the object's current metageneration does not match the given value.
    String projection = "full"; // String | Set of properties to return. Defaults to noAcl.
    Boolean softDeleted = true; // Boolean | If true, only soft-deleted object versions will be listed. The default is false. For more information, see Soft Delete.
    String userProject = "userProject_example"; // String | The project to be billed for this request. Required for Requester Pays buckets.
    try {
      ModelObject result = apiInstance.storageObjectsGet(bucket, _object, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, generation, ifGenerationMatch, ifGenerationNotMatch, ifMetagenerationMatch, ifMetagenerationNotMatch, projection, softDeleted, userProject);
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
| **ifGenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object. | [optional] |
| **ifGenerationNotMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object. | [optional] |
| **ifMetagenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration matches the given value. | [optional] |
| **ifMetagenerationNotMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration does not match the given value. | [optional] |
| **projection** | **String**| Set of properties to return. Defaults to noAcl. | [optional] [enum: full, noAcl] |
| **softDeleted** | **Boolean**| If true, only soft-deleted object versions will be listed. The default is false. For more information, see Soft Delete. | [optional] |
| **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] |

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

<a id="storageObjectsGetIamPolicy"></a>
# **storageObjectsGetIamPolicy**
> Policy storageObjectsGetIamPolicy(bucket, _object, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, generation, userProject)



Returns an IAM policy for the specified object.

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
    defaultClient.setBasePath("https://storage.googleapis.com/storage/v1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ObjectsApi apiInstance = new ObjectsApi(defaultClient);
    String bucket = "bucket_example"; // String | Name of the bucket in which the object resides.
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
      Policy result = apiInstance.storageObjectsGetIamPolicy(bucket, _object, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, generation, userProject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectsApi#storageObjectsGetIamPolicy");
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

[**Policy**](Policy.md)

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
> ModelObject storageObjectsInsert(bucket, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, contentEncoding, ifGenerationMatch, ifGenerationNotMatch, ifMetagenerationMatch, ifMetagenerationNotMatch, kmsKeyName, name, predefinedAcl, projection, userProject, modelObject)



Stores a new object and metadata.

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
    defaultClient.setBasePath("https://storage.googleapis.com/storage/v1");
    
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
    String uploadType = "uploadType_example"; // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String contentEncoding = "contentEncoding_example"; // String | If set, sets the contentEncoding property of the final object to this value. Setting this parameter is equivalent to setting the contentEncoding metadata property. This can be useful when uploading an object with uploadType=media to indicate the encoding of the content being uploaded.
    String ifGenerationMatch = "ifGenerationMatch_example"; // String | Makes the operation conditional on whether the object's current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object.
    String ifGenerationNotMatch = "ifGenerationNotMatch_example"; // String | Makes the operation conditional on whether the object's current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object.
    String ifMetagenerationMatch = "ifMetagenerationMatch_example"; // String | Makes the operation conditional on whether the object's current metageneration matches the given value.
    String ifMetagenerationNotMatch = "ifMetagenerationNotMatch_example"; // String | Makes the operation conditional on whether the object's current metageneration does not match the given value.
    String kmsKeyName = "kmsKeyName_example"; // String | Resource name of the Cloud KMS key, of the form projects/my-project/locations/global/keyRings/my-kr/cryptoKeys/my-key, that will be used to encrypt the object. Overrides the object metadata's kms_key_name value, if any.
    String name = "name_example"; // String | Name of the object. Required when the object metadata is not otherwise provided. Overrides the object metadata's name value, if any. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding).
    String predefinedAcl = "authenticatedRead"; // String | Apply a predefined set of access controls to this object.
    String projection = "full"; // String | Set of properties to return. Defaults to noAcl, unless the object resource specifies the acl property, when it defaults to full.
    String userProject = "userProject_example"; // String | The project to be billed for this request. Required for Requester Pays buckets.
    ModelObject modelObject = new ModelObject(); // ModelObject | 
    try {
      ModelObject result = apiInstance.storageObjectsInsert(bucket, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, contentEncoding, ifGenerationMatch, ifGenerationNotMatch, ifMetagenerationMatch, ifMetagenerationNotMatch, kmsKeyName, name, predefinedAcl, projection, userProject, modelObject);
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
| **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **contentEncoding** | **String**| If set, sets the contentEncoding property of the final object to this value. Setting this parameter is equivalent to setting the contentEncoding metadata property. This can be useful when uploading an object with uploadType&#x3D;media to indicate the encoding of the content being uploaded. | [optional] |
| **ifGenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object. | [optional] |
| **ifGenerationNotMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object. | [optional] |
| **ifMetagenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration matches the given value. | [optional] |
| **ifMetagenerationNotMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration does not match the given value. | [optional] |
| **kmsKeyName** | **String**| Resource name of the Cloud KMS key, of the form projects/my-project/locations/global/keyRings/my-kr/cryptoKeys/my-key, that will be used to encrypt the object. Overrides the object metadata&#39;s kms_key_name value, if any. | [optional] |
| **name** | **String**| Name of the object. Required when the object metadata is not otherwise provided. Overrides the object metadata&#39;s name value, if any. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding). | [optional] |
| **predefinedAcl** | **String**| Apply a predefined set of access controls to this object. | [optional] [enum: authenticatedRead, bucketOwnerFullControl, bucketOwnerRead, private, projectPrivate, publicRead] |
| **projection** | **String**| Set of properties to return. Defaults to noAcl, unless the object resource specifies the acl property, when it defaults to full. | [optional] [enum: full, noAcl] |
| **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] |
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
> Objects storageObjectsList(bucket, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, delimiter, endOffset, includeFoldersAsPrefixes, includeTrailingDelimiter, matchGlob, maxResults, pageToken, prefix, projection, softDeleted, startOffset, userProject, versions)



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
    defaultClient.setBasePath("https://storage.googleapis.com/storage/v1");
    
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
    String uploadType = "uploadType_example"; // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String delimiter = "delimiter_example"; // String | Returns results in a directory-like mode. items will contain only objects whose names, aside from the prefix, do not contain delimiter. Objects whose names, aside from the prefix, contain delimiter will have their name, truncated after the delimiter, returned in prefixes. Duplicate prefixes are omitted.
    String endOffset = "endOffset_example"; // String | Filter results to objects whose names are lexicographically before endOffset. If startOffset is also set, the objects listed will have names between startOffset (inclusive) and endOffset (exclusive).
    Boolean includeFoldersAsPrefixes = true; // Boolean | Only applicable if delimiter is set to '/'. If true, will also include folders and managed folders (besides objects) in the returned prefixes.
    Boolean includeTrailingDelimiter = true; // Boolean | If true, objects that end in exactly one instance of delimiter will have their metadata included in items in addition to prefixes.
    String matchGlob = "matchGlob_example"; // String | Filter results to objects and prefixes that match this glob pattern.
    Integer maxResults = 56; // Integer | Maximum number of items plus prefixes to return in a single page of responses. As duplicate prefixes are omitted, fewer total results may be returned than requested. The service will use this parameter or 1,000 items, whichever is smaller.
    String pageToken = "pageToken_example"; // String | A previously-returned page token representing part of the larger set of results to view.
    String prefix = "prefix_example"; // String | Filter results to objects whose names begin with this prefix.
    String projection = "full"; // String | Set of properties to return. Defaults to noAcl.
    Boolean softDeleted = true; // Boolean | If true, only soft-deleted object versions will be listed. The default is false. For more information, see Soft Delete.
    String startOffset = "startOffset_example"; // String | Filter results to objects whose names are lexicographically equal to or after startOffset. If endOffset is also set, the objects listed will have names between startOffset (inclusive) and endOffset (exclusive).
    String userProject = "userProject_example"; // String | The project to be billed for this request. Required for Requester Pays buckets.
    Boolean versions = true; // Boolean | If true, lists all versions of an object as distinct results. The default is false. For more information, see Object Versioning.
    try {
      Objects result = apiInstance.storageObjectsList(bucket, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, delimiter, endOffset, includeFoldersAsPrefixes, includeTrailingDelimiter, matchGlob, maxResults, pageToken, prefix, projection, softDeleted, startOffset, userProject, versions);
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
| **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **delimiter** | **String**| Returns results in a directory-like mode. items will contain only objects whose names, aside from the prefix, do not contain delimiter. Objects whose names, aside from the prefix, contain delimiter will have their name, truncated after the delimiter, returned in prefixes. Duplicate prefixes are omitted. | [optional] |
| **endOffset** | **String**| Filter results to objects whose names are lexicographically before endOffset. If startOffset is also set, the objects listed will have names between startOffset (inclusive) and endOffset (exclusive). | [optional] |
| **includeFoldersAsPrefixes** | **Boolean**| Only applicable if delimiter is set to &#39;/&#39;. If true, will also include folders and managed folders (besides objects) in the returned prefixes. | [optional] |
| **includeTrailingDelimiter** | **Boolean**| If true, objects that end in exactly one instance of delimiter will have their metadata included in items in addition to prefixes. | [optional] |
| **matchGlob** | **String**| Filter results to objects and prefixes that match this glob pattern. | [optional] |
| **maxResults** | **Integer**| Maximum number of items plus prefixes to return in a single page of responses. As duplicate prefixes are omitted, fewer total results may be returned than requested. The service will use this parameter or 1,000 items, whichever is smaller. | [optional] |
| **pageToken** | **String**| A previously-returned page token representing part of the larger set of results to view. | [optional] |
| **prefix** | **String**| Filter results to objects whose names begin with this prefix. | [optional] |
| **projection** | **String**| Set of properties to return. Defaults to noAcl. | [optional] [enum: full, noAcl] |
| **softDeleted** | **Boolean**| If true, only soft-deleted object versions will be listed. The default is false. For more information, see Soft Delete. | [optional] |
| **startOffset** | **String**| Filter results to objects whose names are lexicographically equal to or after startOffset. If endOffset is also set, the objects listed will have names between startOffset (inclusive) and endOffset (exclusive). | [optional] |
| **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] |
| **versions** | **Boolean**| If true, lists all versions of an object as distinct results. The default is false. For more information, see Object Versioning. | [optional] |

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
> ModelObject storageObjectsPatch(bucket, _object, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, generation, ifGenerationMatch, ifGenerationNotMatch, ifMetagenerationMatch, ifMetagenerationNotMatch, overrideUnlockedRetention, predefinedAcl, projection, userProject, modelObject)



Patches an object&#39;s metadata.

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
    defaultClient.setBasePath("https://storage.googleapis.com/storage/v1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ObjectsApi apiInstance = new ObjectsApi(defaultClient);
    String bucket = "bucket_example"; // String | Name of the bucket in which the object resides.
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
    String ifGenerationMatch = "ifGenerationMatch_example"; // String | Makes the operation conditional on whether the object's current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object.
    String ifGenerationNotMatch = "ifGenerationNotMatch_example"; // String | Makes the operation conditional on whether the object's current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object.
    String ifMetagenerationMatch = "ifMetagenerationMatch_example"; // String | Makes the operation conditional on whether the object's current metageneration matches the given value.
    String ifMetagenerationNotMatch = "ifMetagenerationNotMatch_example"; // String | Makes the operation conditional on whether the object's current metageneration does not match the given value.
    Boolean overrideUnlockedRetention = true; // Boolean | Must be true to remove the retention configuration, reduce its unlocked retention period, or change its mode from unlocked to locked.
    String predefinedAcl = "authenticatedRead"; // String | Apply a predefined set of access controls to this object.
    String projection = "full"; // String | Set of properties to return. Defaults to full.
    String userProject = "userProject_example"; // String | The project to be billed for this request, for Requester Pays buckets.
    ModelObject modelObject = new ModelObject(); // ModelObject | 
    try {
      ModelObject result = apiInstance.storageObjectsPatch(bucket, _object, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, generation, ifGenerationMatch, ifGenerationNotMatch, ifMetagenerationMatch, ifMetagenerationNotMatch, overrideUnlockedRetention, predefinedAcl, projection, userProject, modelObject);
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
| **ifGenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object. | [optional] |
| **ifGenerationNotMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object. | [optional] |
| **ifMetagenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration matches the given value. | [optional] |
| **ifMetagenerationNotMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration does not match the given value. | [optional] |
| **overrideUnlockedRetention** | **Boolean**| Must be true to remove the retention configuration, reduce its unlocked retention period, or change its mode from unlocked to locked. | [optional] |
| **predefinedAcl** | **String**| Apply a predefined set of access controls to this object. | [optional] [enum: authenticatedRead, bucketOwnerFullControl, bucketOwnerRead, private, projectPrivate, publicRead] |
| **projection** | **String**| Set of properties to return. Defaults to full. | [optional] [enum: full, noAcl] |
| **userProject** | **String**| The project to be billed for this request, for Requester Pays buckets. | [optional] |
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

<a id="storageObjectsRestore"></a>
# **storageObjectsRestore**
> ModelObject storageObjectsRestore(bucket, _object, generation, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, copySourceAcl, ifGenerationMatch, ifGenerationNotMatch, ifMetagenerationMatch, ifMetagenerationNotMatch, projection, userProject, modelObject)



Restores a soft-deleted object.

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
    defaultClient.setBasePath("https://storage.googleapis.com/storage/v1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ObjectsApi apiInstance = new ObjectsApi(defaultClient);
    String bucket = "bucket_example"; // String | Name of the bucket in which the object resides.
    String _object = "_object_example"; // String | Name of the object. For information about how to URL encode object names to be path safe, see Encoding URI Path Parts.
    String generation = "generation_example"; // String | Selects a specific revision of this object.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String uploadType = "uploadType_example"; // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Boolean copySourceAcl = true; // Boolean | If true, copies the source object's ACL; otherwise, uses the bucket's default object ACL. The default is false.
    String ifGenerationMatch = "ifGenerationMatch_example"; // String | Makes the operation conditional on whether the object's one live generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object.
    String ifGenerationNotMatch = "ifGenerationNotMatch_example"; // String | Makes the operation conditional on whether none of the object's live generations match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object.
    String ifMetagenerationMatch = "ifMetagenerationMatch_example"; // String | Makes the operation conditional on whether the object's one live metageneration matches the given value.
    String ifMetagenerationNotMatch = "ifMetagenerationNotMatch_example"; // String | Makes the operation conditional on whether none of the object's live metagenerations match the given value.
    String projection = "full"; // String | Set of properties to return. Defaults to full.
    String userProject = "userProject_example"; // String | The project to be billed for this request. Required for Requester Pays buckets.
    ModelObject modelObject = new ModelObject(); // ModelObject | 
    try {
      ModelObject result = apiInstance.storageObjectsRestore(bucket, _object, generation, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, copySourceAcl, ifGenerationMatch, ifGenerationNotMatch, ifMetagenerationMatch, ifMetagenerationNotMatch, projection, userProject, modelObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectsApi#storageObjectsRestore");
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
| **_object** | **String**| Name of the object. For information about how to URL encode object names to be path safe, see Encoding URI Path Parts. | |
| **generation** | **String**| Selects a specific revision of this object. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **copySourceAcl** | **Boolean**| If true, copies the source object&#39;s ACL; otherwise, uses the bucket&#39;s default object ACL. The default is false. | [optional] |
| **ifGenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s one live generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object. | [optional] |
| **ifGenerationNotMatch** | **String**| Makes the operation conditional on whether none of the object&#39;s live generations match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object. | [optional] |
| **ifMetagenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s one live metageneration matches the given value. | [optional] |
| **ifMetagenerationNotMatch** | **String**| Makes the operation conditional on whether none of the object&#39;s live metagenerations match the given value. | [optional] |
| **projection** | **String**| Set of properties to return. Defaults to full. | [optional] [enum: full, noAcl] |
| **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] |
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

<a id="storageObjectsRewrite"></a>
# **storageObjectsRewrite**
> RewriteResponse storageObjectsRewrite(sourceBucket, sourceObject, destinationBucket, destinationObject, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, destinationKmsKeyName, destinationPredefinedAcl, ifGenerationMatch, ifGenerationNotMatch, ifMetagenerationMatch, ifMetagenerationNotMatch, ifSourceGenerationMatch, ifSourceGenerationNotMatch, ifSourceMetagenerationMatch, ifSourceMetagenerationNotMatch, maxBytesRewrittenPerCall, projection, rewriteToken, sourceGeneration, userProject, modelObject)



Rewrites a source object to a destination object. Optionally overrides metadata.

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
    defaultClient.setBasePath("https://storage.googleapis.com/storage/v1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ObjectsApi apiInstance = new ObjectsApi(defaultClient);
    String sourceBucket = "sourceBucket_example"; // String | Name of the bucket in which to find the source object.
    String sourceObject = "sourceObject_example"; // String | Name of the source object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding).
    String destinationBucket = "destinationBucket_example"; // String | Name of the bucket in which to store the new object. Overrides the provided object metadata's bucket value, if any.
    String destinationObject = "destinationObject_example"; // String | Name of the new object. Required when the object metadata is not otherwise provided. Overrides the object metadata's name value, if any. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding).
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String uploadType = "uploadType_example"; // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String destinationKmsKeyName = "destinationKmsKeyName_example"; // String | Resource name of the Cloud KMS key, of the form projects/my-project/locations/global/keyRings/my-kr/cryptoKeys/my-key, that will be used to encrypt the object. Overrides the object metadata's kms_key_name value, if any.
    String destinationPredefinedAcl = "authenticatedRead"; // String | Apply a predefined set of access controls to the destination object.
    String ifGenerationMatch = "ifGenerationMatch_example"; // String | Makes the operation conditional on whether the object's current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object.
    String ifGenerationNotMatch = "ifGenerationNotMatch_example"; // String | Makes the operation conditional on whether the object's current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object.
    String ifMetagenerationMatch = "ifMetagenerationMatch_example"; // String | Makes the operation conditional on whether the destination object's current metageneration matches the given value.
    String ifMetagenerationNotMatch = "ifMetagenerationNotMatch_example"; // String | Makes the operation conditional on whether the destination object's current metageneration does not match the given value.
    String ifSourceGenerationMatch = "ifSourceGenerationMatch_example"; // String | Makes the operation conditional on whether the source object's current generation matches the given value.
    String ifSourceGenerationNotMatch = "ifSourceGenerationNotMatch_example"; // String | Makes the operation conditional on whether the source object's current generation does not match the given value.
    String ifSourceMetagenerationMatch = "ifSourceMetagenerationMatch_example"; // String | Makes the operation conditional on whether the source object's current metageneration matches the given value.
    String ifSourceMetagenerationNotMatch = "ifSourceMetagenerationNotMatch_example"; // String | Makes the operation conditional on whether the source object's current metageneration does not match the given value.
    String maxBytesRewrittenPerCall = "maxBytesRewrittenPerCall_example"; // String | The maximum number of bytes that will be rewritten per rewrite request. Most callers shouldn't need to specify this parameter - it is primarily in place to support testing. If specified the value must be an integral multiple of 1 MiB (1048576). Also, this only applies to requests where the source and destination span locations and/or storage classes. Finally, this value must not change across rewrite calls else you'll get an error that the rewriteToken is invalid.
    String projection = "full"; // String | Set of properties to return. Defaults to noAcl, unless the object resource specifies the acl property, when it defaults to full.
    String rewriteToken = "rewriteToken_example"; // String | Include this field (from the previous rewrite response) on each rewrite request after the first one, until the rewrite response 'done' flag is true. Calls that provide a rewriteToken can omit all other request fields, but if included those fields must match the values provided in the first rewrite request.
    String sourceGeneration = "sourceGeneration_example"; // String | If present, selects a specific revision of the source object (as opposed to the latest version, the default).
    String userProject = "userProject_example"; // String | The project to be billed for this request. Required for Requester Pays buckets.
    ModelObject modelObject = new ModelObject(); // ModelObject | 
    try {
      RewriteResponse result = apiInstance.storageObjectsRewrite(sourceBucket, sourceObject, destinationBucket, destinationObject, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, destinationKmsKeyName, destinationPredefinedAcl, ifGenerationMatch, ifGenerationNotMatch, ifMetagenerationMatch, ifMetagenerationNotMatch, ifSourceGenerationMatch, ifSourceGenerationNotMatch, ifSourceMetagenerationMatch, ifSourceMetagenerationNotMatch, maxBytesRewrittenPerCall, projection, rewriteToken, sourceGeneration, userProject, modelObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectsApi#storageObjectsRewrite");
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
| **sourceObject** | **String**| Name of the source object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding). | |
| **destinationBucket** | **String**| Name of the bucket in which to store the new object. Overrides the provided object metadata&#39;s bucket value, if any. | |
| **destinationObject** | **String**| Name of the new object. Required when the object metadata is not otherwise provided. Overrides the object metadata&#39;s name value, if any. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding). | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **destinationKmsKeyName** | **String**| Resource name of the Cloud KMS key, of the form projects/my-project/locations/global/keyRings/my-kr/cryptoKeys/my-key, that will be used to encrypt the object. Overrides the object metadata&#39;s kms_key_name value, if any. | [optional] |
| **destinationPredefinedAcl** | **String**| Apply a predefined set of access controls to the destination object. | [optional] [enum: authenticatedRead, bucketOwnerFullControl, bucketOwnerRead, private, projectPrivate, publicRead] |
| **ifGenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object. | [optional] |
| **ifGenerationNotMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object. | [optional] |
| **ifMetagenerationMatch** | **String**| Makes the operation conditional on whether the destination object&#39;s current metageneration matches the given value. | [optional] |
| **ifMetagenerationNotMatch** | **String**| Makes the operation conditional on whether the destination object&#39;s current metageneration does not match the given value. | [optional] |
| **ifSourceGenerationMatch** | **String**| Makes the operation conditional on whether the source object&#39;s current generation matches the given value. | [optional] |
| **ifSourceGenerationNotMatch** | **String**| Makes the operation conditional on whether the source object&#39;s current generation does not match the given value. | [optional] |
| **ifSourceMetagenerationMatch** | **String**| Makes the operation conditional on whether the source object&#39;s current metageneration matches the given value. | [optional] |
| **ifSourceMetagenerationNotMatch** | **String**| Makes the operation conditional on whether the source object&#39;s current metageneration does not match the given value. | [optional] |
| **maxBytesRewrittenPerCall** | **String**| The maximum number of bytes that will be rewritten per rewrite request. Most callers shouldn&#39;t need to specify this parameter - it is primarily in place to support testing. If specified the value must be an integral multiple of 1 MiB (1048576). Also, this only applies to requests where the source and destination span locations and/or storage classes. Finally, this value must not change across rewrite calls else you&#39;ll get an error that the rewriteToken is invalid. | [optional] |
| **projection** | **String**| Set of properties to return. Defaults to noAcl, unless the object resource specifies the acl property, when it defaults to full. | [optional] [enum: full, noAcl] |
| **rewriteToken** | **String**| Include this field (from the previous rewrite response) on each rewrite request after the first one, until the rewrite response &#39;done&#39; flag is true. Calls that provide a rewriteToken can omit all other request fields, but if included those fields must match the values provided in the first rewrite request. | [optional] |
| **sourceGeneration** | **String**| If present, selects a specific revision of the source object (as opposed to the latest version, the default). | [optional] |
| **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] |
| **modelObject** | [**ModelObject**](ModelObject.md)|  | [optional] |

### Return type

[**RewriteResponse**](RewriteResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="storageObjectsSetIamPolicy"></a>
# **storageObjectsSetIamPolicy**
> Policy storageObjectsSetIamPolicy(bucket, _object, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, generation, userProject, policy)



Updates an IAM policy for the specified object.

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
    defaultClient.setBasePath("https://storage.googleapis.com/storage/v1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ObjectsApi apiInstance = new ObjectsApi(defaultClient);
    String bucket = "bucket_example"; // String | Name of the bucket in which the object resides.
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
    Policy policy = new Policy(); // Policy | 
    try {
      Policy result = apiInstance.storageObjectsSetIamPolicy(bucket, _object, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, generation, userProject, policy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectsApi#storageObjectsSetIamPolicy");
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
| **policy** | [**Policy**](Policy.md)|  | [optional] |

### Return type

[**Policy**](Policy.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="storageObjectsTestIamPermissions"></a>
# **storageObjectsTestIamPermissions**
> TestIamPermissionsResponse storageObjectsTestIamPermissions(bucket, _object, permissions, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, generation, userProject)



Tests a set of permissions on the given object to see which, if any, are held by the caller.

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
    defaultClient.setBasePath("https://storage.googleapis.com/storage/v1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ObjectsApi apiInstance = new ObjectsApi(defaultClient);
    String bucket = "bucket_example"; // String | Name of the bucket in which the object resides.
    String _object = "_object_example"; // String | Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding).
    List<String> permissions = Arrays.asList(); // List<String> | Permissions to test.
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
      TestIamPermissionsResponse result = apiInstance.storageObjectsTestIamPermissions(bucket, _object, permissions, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, generation, userProject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObjectsApi#storageObjectsTestIamPermissions");
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
| **_object** | **String**| Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI Path Parts](https://cloud.google.com/storage/docs/request-endpoints#encoding). | |
| **permissions** | [**List&lt;String&gt;**](String.md)| Permissions to test. | |
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

[**TestIamPermissionsResponse**](TestIamPermissionsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="storageObjectsUpdate"></a>
# **storageObjectsUpdate**
> ModelObject storageObjectsUpdate(bucket, _object, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, generation, ifGenerationMatch, ifGenerationNotMatch, ifMetagenerationMatch, ifMetagenerationNotMatch, overrideUnlockedRetention, predefinedAcl, projection, userProject, modelObject)



Updates an object&#39;s metadata.

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
    defaultClient.setBasePath("https://storage.googleapis.com/storage/v1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ObjectsApi apiInstance = new ObjectsApi(defaultClient);
    String bucket = "bucket_example"; // String | Name of the bucket in which the object resides.
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
    String ifGenerationMatch = "ifGenerationMatch_example"; // String | Makes the operation conditional on whether the object's current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object.
    String ifGenerationNotMatch = "ifGenerationNotMatch_example"; // String | Makes the operation conditional on whether the object's current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object.
    String ifMetagenerationMatch = "ifMetagenerationMatch_example"; // String | Makes the operation conditional on whether the object's current metageneration matches the given value.
    String ifMetagenerationNotMatch = "ifMetagenerationNotMatch_example"; // String | Makes the operation conditional on whether the object's current metageneration does not match the given value.
    Boolean overrideUnlockedRetention = true; // Boolean | Must be true to remove the retention configuration, reduce its unlocked retention period, or change its mode from unlocked to locked.
    String predefinedAcl = "authenticatedRead"; // String | Apply a predefined set of access controls to this object.
    String projection = "full"; // String | Set of properties to return. Defaults to full.
    String userProject = "userProject_example"; // String | The project to be billed for this request. Required for Requester Pays buckets.
    ModelObject modelObject = new ModelObject(); // ModelObject | 
    try {
      ModelObject result = apiInstance.storageObjectsUpdate(bucket, _object, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, generation, ifGenerationMatch, ifGenerationNotMatch, ifMetagenerationMatch, ifMetagenerationNotMatch, overrideUnlockedRetention, predefinedAcl, projection, userProject, modelObject);
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
| **ifGenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object. | [optional] |
| **ifGenerationNotMatch** | **String**| Makes the operation conditional on whether the object&#39;s current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object. | [optional] |
| **ifMetagenerationMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration matches the given value. | [optional] |
| **ifMetagenerationNotMatch** | **String**| Makes the operation conditional on whether the object&#39;s current metageneration does not match the given value. | [optional] |
| **overrideUnlockedRetention** | **Boolean**| Must be true to remove the retention configuration, reduce its unlocked retention period, or change its mode from unlocked to locked. | [optional] |
| **predefinedAcl** | **String**| Apply a predefined set of access controls to this object. | [optional] [enum: authenticatedRead, bucketOwnerFullControl, bucketOwnerRead, private, projectPrivate, publicRead] |
| **projection** | **String**| Set of properties to return. Defaults to full. | [optional] [enum: full, noAcl] |
| **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] |
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
> Channel storageObjectsWatchAll(bucket, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, delimiter, endOffset, includeTrailingDelimiter, maxResults, pageToken, prefix, projection, startOffset, userProject, versions, channel)



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
    defaultClient.setBasePath("https://storage.googleapis.com/storage/v1");
    
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
    String uploadType = "uploadType_example"; // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String delimiter = "delimiter_example"; // String | Returns results in a directory-like mode. items will contain only objects whose names, aside from the prefix, do not contain delimiter. Objects whose names, aside from the prefix, contain delimiter will have their name, truncated after the delimiter, returned in prefixes. Duplicate prefixes are omitted.
    String endOffset = "endOffset_example"; // String | Filter results to objects whose names are lexicographically before endOffset. If startOffset is also set, the objects listed will have names between startOffset (inclusive) and endOffset (exclusive).
    Boolean includeTrailingDelimiter = true; // Boolean | If true, objects that end in exactly one instance of delimiter will have their metadata included in items in addition to prefixes.
    Integer maxResults = 56; // Integer | Maximum number of items plus prefixes to return in a single page of responses. As duplicate prefixes are omitted, fewer total results may be returned than requested. The service will use this parameter or 1,000 items, whichever is smaller.
    String pageToken = "pageToken_example"; // String | A previously-returned page token representing part of the larger set of results to view.
    String prefix = "prefix_example"; // String | Filter results to objects whose names begin with this prefix.
    String projection = "full"; // String | Set of properties to return. Defaults to noAcl.
    String startOffset = "startOffset_example"; // String | Filter results to objects whose names are lexicographically equal to or after startOffset. If endOffset is also set, the objects listed will have names between startOffset (inclusive) and endOffset (exclusive).
    String userProject = "userProject_example"; // String | The project to be billed for this request. Required for Requester Pays buckets.
    Boolean versions = true; // Boolean | If true, lists all versions of an object as distinct results. The default is false. For more information, see Object Versioning.
    Channel channel = new Channel(); // Channel | 
    try {
      Channel result = apiInstance.storageObjectsWatchAll(bucket, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, delimiter, endOffset, includeTrailingDelimiter, maxResults, pageToken, prefix, projection, startOffset, userProject, versions, channel);
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
| **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **delimiter** | **String**| Returns results in a directory-like mode. items will contain only objects whose names, aside from the prefix, do not contain delimiter. Objects whose names, aside from the prefix, contain delimiter will have their name, truncated after the delimiter, returned in prefixes. Duplicate prefixes are omitted. | [optional] |
| **endOffset** | **String**| Filter results to objects whose names are lexicographically before endOffset. If startOffset is also set, the objects listed will have names between startOffset (inclusive) and endOffset (exclusive). | [optional] |
| **includeTrailingDelimiter** | **Boolean**| If true, objects that end in exactly one instance of delimiter will have their metadata included in items in addition to prefixes. | [optional] |
| **maxResults** | **Integer**| Maximum number of items plus prefixes to return in a single page of responses. As duplicate prefixes are omitted, fewer total results may be returned than requested. The service will use this parameter or 1,000 items, whichever is smaller. | [optional] |
| **pageToken** | **String**| A previously-returned page token representing part of the larger set of results to view. | [optional] |
| **prefix** | **String**| Filter results to objects whose names begin with this prefix. | [optional] |
| **projection** | **String**| Set of properties to return. Defaults to noAcl. | [optional] [enum: full, noAcl] |
| **startOffset** | **String**| Filter results to objects whose names are lexicographically equal to or after startOffset. If endOffset is also set, the objects listed will have names between startOffset (inclusive) and endOffset (exclusive). | [optional] |
| **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] |
| **versions** | **Boolean**| If true, lists all versions of an object as distinct results. The default is false. For more information, see Object Versioning. | [optional] |
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

