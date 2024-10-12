# BucketsApi

All URIs are relative to *https://storage.googleapis.com/storage/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**storageBucketsDelete**](BucketsApi.md#storageBucketsDelete) | **DELETE** /b/{bucket} |  |
| [**storageBucketsGet**](BucketsApi.md#storageBucketsGet) | **GET** /b/{bucket} |  |
| [**storageBucketsGetIamPolicy**](BucketsApi.md#storageBucketsGetIamPolicy) | **GET** /b/{bucket}/iam |  |
| [**storageBucketsInsert**](BucketsApi.md#storageBucketsInsert) | **POST** /b |  |
| [**storageBucketsList**](BucketsApi.md#storageBucketsList) | **GET** /b |  |
| [**storageBucketsLockRetentionPolicy**](BucketsApi.md#storageBucketsLockRetentionPolicy) | **POST** /b/{bucket}/lockRetentionPolicy |  |
| [**storageBucketsPatch**](BucketsApi.md#storageBucketsPatch) | **PATCH** /b/{bucket} |  |
| [**storageBucketsSetIamPolicy**](BucketsApi.md#storageBucketsSetIamPolicy) | **PUT** /b/{bucket}/iam |  |
| [**storageBucketsTestIamPermissions**](BucketsApi.md#storageBucketsTestIamPermissions) | **GET** /b/{bucket}/iam/testPermissions |  |
| [**storageBucketsUpdate**](BucketsApi.md#storageBucketsUpdate) | **PUT** /b/{bucket} |  |


<a id="storageBucketsDelete"></a>
# **storageBucketsDelete**
> storageBucketsDelete(bucket, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, ifMetagenerationMatch, ifMetagenerationNotMatch, userProject)



Permanently deletes an empty bucket.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BucketsApi;

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

    BucketsApi apiInstance = new BucketsApi(defaultClient);
    String bucket = "bucket_example"; // String | Name of a bucket.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String uploadType = "uploadType_example"; // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String ifMetagenerationMatch = "ifMetagenerationMatch_example"; // String | If set, only deletes the bucket if its metageneration matches this value.
    String ifMetagenerationNotMatch = "ifMetagenerationNotMatch_example"; // String | If set, only deletes the bucket if its metageneration does not match this value.
    String userProject = "userProject_example"; // String | The project to be billed for this request. Required for Requester Pays buckets.
    try {
      apiInstance.storageBucketsDelete(bucket, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, ifMetagenerationMatch, ifMetagenerationNotMatch, userProject);
    } catch (ApiException e) {
      System.err.println("Exception when calling BucketsApi#storageBucketsDelete");
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
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **ifMetagenerationMatch** | **String**| If set, only deletes the bucket if its metageneration matches this value. | [optional] |
| **ifMetagenerationNotMatch** | **String**| If set, only deletes the bucket if its metageneration does not match this value. | [optional] |
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

<a id="storageBucketsGet"></a>
# **storageBucketsGet**
> Bucket storageBucketsGet(bucket, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, ifMetagenerationMatch, ifMetagenerationNotMatch, projection, userProject)



Returns metadata for the specified bucket.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BucketsApi;

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

    BucketsApi apiInstance = new BucketsApi(defaultClient);
    String bucket = "bucket_example"; // String | Name of a bucket.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String uploadType = "uploadType_example"; // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String ifMetagenerationMatch = "ifMetagenerationMatch_example"; // String | Makes the return of the bucket metadata conditional on whether the bucket's current metageneration matches the given value.
    String ifMetagenerationNotMatch = "ifMetagenerationNotMatch_example"; // String | Makes the return of the bucket metadata conditional on whether the bucket's current metageneration does not match the given value.
    String projection = "full"; // String | Set of properties to return. Defaults to noAcl.
    String userProject = "userProject_example"; // String | The project to be billed for this request. Required for Requester Pays buckets.
    try {
      Bucket result = apiInstance.storageBucketsGet(bucket, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, ifMetagenerationMatch, ifMetagenerationNotMatch, projection, userProject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BucketsApi#storageBucketsGet");
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
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **ifMetagenerationMatch** | **String**| Makes the return of the bucket metadata conditional on whether the bucket&#39;s current metageneration matches the given value. | [optional] |
| **ifMetagenerationNotMatch** | **String**| Makes the return of the bucket metadata conditional on whether the bucket&#39;s current metageneration does not match the given value. | [optional] |
| **projection** | **String**| Set of properties to return. Defaults to noAcl. | [optional] [enum: full, noAcl] |
| **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] |

### Return type

[**Bucket**](Bucket.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="storageBucketsGetIamPolicy"></a>
# **storageBucketsGetIamPolicy**
> Policy storageBucketsGetIamPolicy(bucket, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, optionsRequestedPolicyVersion, userProject)



Returns an IAM policy for the specified bucket.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BucketsApi;

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

    BucketsApi apiInstance = new BucketsApi(defaultClient);
    String bucket = "bucket_example"; // String | Name of a bucket.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String uploadType = "uploadType_example"; // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Integer optionsRequestedPolicyVersion = 56; // Integer | The IAM policy format version to be returned. If the optionsRequestedPolicyVersion is for an older version that doesn't support part of the requested IAM policy, the request fails.
    String userProject = "userProject_example"; // String | The project to be billed for this request. Required for Requester Pays buckets.
    try {
      Policy result = apiInstance.storageBucketsGetIamPolicy(bucket, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, optionsRequestedPolicyVersion, userProject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BucketsApi#storageBucketsGetIamPolicy");
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
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **optionsRequestedPolicyVersion** | **Integer**| The IAM policy format version to be returned. If the optionsRequestedPolicyVersion is for an older version that doesn&#39;t support part of the requested IAM policy, the request fails. | [optional] |
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

<a id="storageBucketsInsert"></a>
# **storageBucketsInsert**
> Bucket storageBucketsInsert(project, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, enableObjectRetention, predefinedAcl, predefinedDefaultObjectAcl, projection, userProject, bucket)



Creates a new bucket.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BucketsApi;

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

    BucketsApi apiInstance = new BucketsApi(defaultClient);
    String project = "project_example"; // String | A valid API project identifier.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String uploadType = "uploadType_example"; // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Boolean enableObjectRetention = true; // Boolean | When set to true, object retention is enabled for this bucket.
    String predefinedAcl = "authenticatedRead"; // String | Apply a predefined set of access controls to this bucket.
    String predefinedDefaultObjectAcl = "authenticatedRead"; // String | Apply a predefined set of default object access controls to this bucket.
    String projection = "full"; // String | Set of properties to return. Defaults to noAcl, unless the bucket resource specifies acl or defaultObjectAcl properties, when it defaults to full.
    String userProject = "userProject_example"; // String | The project to be billed for this request.
    Bucket bucket = new Bucket(); // Bucket | 
    try {
      Bucket result = apiInstance.storageBucketsInsert(project, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, enableObjectRetention, predefinedAcl, predefinedDefaultObjectAcl, projection, userProject, bucket);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BucketsApi#storageBucketsInsert");
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
| **project** | **String**| A valid API project identifier. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **enableObjectRetention** | **Boolean**| When set to true, object retention is enabled for this bucket. | [optional] |
| **predefinedAcl** | **String**| Apply a predefined set of access controls to this bucket. | [optional] [enum: authenticatedRead, private, projectPrivate, publicRead, publicReadWrite] |
| **predefinedDefaultObjectAcl** | **String**| Apply a predefined set of default object access controls to this bucket. | [optional] [enum: authenticatedRead, bucketOwnerFullControl, bucketOwnerRead, private, projectPrivate, publicRead] |
| **projection** | **String**| Set of properties to return. Defaults to noAcl, unless the bucket resource specifies acl or defaultObjectAcl properties, when it defaults to full. | [optional] [enum: full, noAcl] |
| **userProject** | **String**| The project to be billed for this request. | [optional] |
| **bucket** | [**Bucket**](Bucket.md)|  | [optional] |

### Return type

[**Bucket**](Bucket.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="storageBucketsList"></a>
# **storageBucketsList**
> Buckets storageBucketsList(project, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, maxResults, pageToken, prefix, projection, userProject)



Retrieves a list of buckets for a given project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BucketsApi;

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

    BucketsApi apiInstance = new BucketsApi(defaultClient);
    String project = "project_example"; // String | A valid API project identifier.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String uploadType = "uploadType_example"; // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Integer maxResults = 56; // Integer | Maximum number of buckets to return in a single response. The service will use this parameter or 1,000 items, whichever is smaller.
    String pageToken = "pageToken_example"; // String | A previously-returned page token representing part of the larger set of results to view.
    String prefix = "prefix_example"; // String | Filter results to buckets whose names begin with this prefix.
    String projection = "full"; // String | Set of properties to return. Defaults to noAcl.
    String userProject = "userProject_example"; // String | The project to be billed for this request.
    try {
      Buckets result = apiInstance.storageBucketsList(project, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, maxResults, pageToken, prefix, projection, userProject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BucketsApi#storageBucketsList");
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
| **project** | **String**| A valid API project identifier. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **maxResults** | **Integer**| Maximum number of buckets to return in a single response. The service will use this parameter or 1,000 items, whichever is smaller. | [optional] |
| **pageToken** | **String**| A previously-returned page token representing part of the larger set of results to view. | [optional] |
| **prefix** | **String**| Filter results to buckets whose names begin with this prefix. | [optional] |
| **projection** | **String**| Set of properties to return. Defaults to noAcl. | [optional] [enum: full, noAcl] |
| **userProject** | **String**| The project to be billed for this request. | [optional] |

### Return type

[**Buckets**](Buckets.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="storageBucketsLockRetentionPolicy"></a>
# **storageBucketsLockRetentionPolicy**
> Bucket storageBucketsLockRetentionPolicy(bucket, ifMetagenerationMatch, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, userProject)



Locks retention policy on a bucket.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BucketsApi;

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

    BucketsApi apiInstance = new BucketsApi(defaultClient);
    String bucket = "bucket_example"; // String | Name of a bucket.
    String ifMetagenerationMatch = "ifMetagenerationMatch_example"; // String | Makes the operation conditional on whether bucket's current metageneration matches the given value.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String uploadType = "uploadType_example"; // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String userProject = "userProject_example"; // String | The project to be billed for this request. Required for Requester Pays buckets.
    try {
      Bucket result = apiInstance.storageBucketsLockRetentionPolicy(bucket, ifMetagenerationMatch, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, userProject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BucketsApi#storageBucketsLockRetentionPolicy");
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
| **ifMetagenerationMatch** | **String**| Makes the operation conditional on whether bucket&#39;s current metageneration matches the given value. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] |

### Return type

[**Bucket**](Bucket.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="storageBucketsPatch"></a>
# **storageBucketsPatch**
> Bucket storageBucketsPatch(bucket, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, ifMetagenerationMatch, ifMetagenerationNotMatch, predefinedAcl, predefinedDefaultObjectAcl, projection, userProject, bucket2)



Patches a bucket. Changes to the bucket will be readable immediately after writing, but configuration changes may take time to propagate.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BucketsApi;

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

    BucketsApi apiInstance = new BucketsApi(defaultClient);
    String bucket = "bucket_example"; // String | Name of a bucket.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String uploadType = "uploadType_example"; // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String ifMetagenerationMatch = "ifMetagenerationMatch_example"; // String | Makes the return of the bucket metadata conditional on whether the bucket's current metageneration matches the given value.
    String ifMetagenerationNotMatch = "ifMetagenerationNotMatch_example"; // String | Makes the return of the bucket metadata conditional on whether the bucket's current metageneration does not match the given value.
    String predefinedAcl = "authenticatedRead"; // String | Apply a predefined set of access controls to this bucket.
    String predefinedDefaultObjectAcl = "authenticatedRead"; // String | Apply a predefined set of default object access controls to this bucket.
    String projection = "full"; // String | Set of properties to return. Defaults to full.
    String userProject = "userProject_example"; // String | The project to be billed for this request. Required for Requester Pays buckets.
    Bucket bucket2 = new Bucket(); // Bucket | 
    try {
      Bucket result = apiInstance.storageBucketsPatch(bucket, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, ifMetagenerationMatch, ifMetagenerationNotMatch, predefinedAcl, predefinedDefaultObjectAcl, projection, userProject, bucket2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BucketsApi#storageBucketsPatch");
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
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **ifMetagenerationMatch** | **String**| Makes the return of the bucket metadata conditional on whether the bucket&#39;s current metageneration matches the given value. | [optional] |
| **ifMetagenerationNotMatch** | **String**| Makes the return of the bucket metadata conditional on whether the bucket&#39;s current metageneration does not match the given value. | [optional] |
| **predefinedAcl** | **String**| Apply a predefined set of access controls to this bucket. | [optional] [enum: authenticatedRead, private, projectPrivate, publicRead, publicReadWrite] |
| **predefinedDefaultObjectAcl** | **String**| Apply a predefined set of default object access controls to this bucket. | [optional] [enum: authenticatedRead, bucketOwnerFullControl, bucketOwnerRead, private, projectPrivate, publicRead] |
| **projection** | **String**| Set of properties to return. Defaults to full. | [optional] [enum: full, noAcl] |
| **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] |
| **bucket2** | [**Bucket**](Bucket.md)|  | [optional] |

### Return type

[**Bucket**](Bucket.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="storageBucketsSetIamPolicy"></a>
# **storageBucketsSetIamPolicy**
> Policy storageBucketsSetIamPolicy(bucket, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, userProject, policy)



Updates an IAM policy for the specified bucket.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BucketsApi;

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

    BucketsApi apiInstance = new BucketsApi(defaultClient);
    String bucket = "bucket_example"; // String | Name of a bucket.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String uploadType = "uploadType_example"; // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String userProject = "userProject_example"; // String | The project to be billed for this request. Required for Requester Pays buckets.
    Policy policy = new Policy(); // Policy | 
    try {
      Policy result = apiInstance.storageBucketsSetIamPolicy(bucket, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, userProject, policy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BucketsApi#storageBucketsSetIamPolicy");
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
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
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

<a id="storageBucketsTestIamPermissions"></a>
# **storageBucketsTestIamPermissions**
> TestIamPermissionsResponse storageBucketsTestIamPermissions(bucket, permissions, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, userProject)



Tests a set of permissions on the given bucket to see which, if any, are held by the caller.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BucketsApi;

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

    BucketsApi apiInstance = new BucketsApi(defaultClient);
    String bucket = "bucket_example"; // String | Name of a bucket.
    List<String> permissions = Arrays.asList(); // List<String> | Permissions to test.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String uploadType = "uploadType_example"; // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String userProject = "userProject_example"; // String | The project to be billed for this request. Required for Requester Pays buckets.
    try {
      TestIamPermissionsResponse result = apiInstance.storageBucketsTestIamPermissions(bucket, permissions, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, userProject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BucketsApi#storageBucketsTestIamPermissions");
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
| **permissions** | [**List&lt;String&gt;**](String.md)| Permissions to test. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
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

<a id="storageBucketsUpdate"></a>
# **storageBucketsUpdate**
> Bucket storageBucketsUpdate(bucket, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, ifMetagenerationMatch, ifMetagenerationNotMatch, predefinedAcl, predefinedDefaultObjectAcl, projection, userProject, bucket2)



Updates a bucket. Changes to the bucket will be readable immediately after writing, but configuration changes may take time to propagate.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BucketsApi;

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

    BucketsApi apiInstance = new BucketsApi(defaultClient);
    String bucket = "bucket_example"; // String | Name of a bucket.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String uploadType = "uploadType_example"; // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String ifMetagenerationMatch = "ifMetagenerationMatch_example"; // String | Makes the return of the bucket metadata conditional on whether the bucket's current metageneration matches the given value.
    String ifMetagenerationNotMatch = "ifMetagenerationNotMatch_example"; // String | Makes the return of the bucket metadata conditional on whether the bucket's current metageneration does not match the given value.
    String predefinedAcl = "authenticatedRead"; // String | Apply a predefined set of access controls to this bucket.
    String predefinedDefaultObjectAcl = "authenticatedRead"; // String | Apply a predefined set of default object access controls to this bucket.
    String projection = "full"; // String | Set of properties to return. Defaults to full.
    String userProject = "userProject_example"; // String | The project to be billed for this request. Required for Requester Pays buckets.
    Bucket bucket2 = new Bucket(); // Bucket | 
    try {
      Bucket result = apiInstance.storageBucketsUpdate(bucket, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, ifMetagenerationMatch, ifMetagenerationNotMatch, predefinedAcl, predefinedDefaultObjectAcl, projection, userProject, bucket2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BucketsApi#storageBucketsUpdate");
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
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **ifMetagenerationMatch** | **String**| Makes the return of the bucket metadata conditional on whether the bucket&#39;s current metageneration matches the given value. | [optional] |
| **ifMetagenerationNotMatch** | **String**| Makes the return of the bucket metadata conditional on whether the bucket&#39;s current metageneration does not match the given value. | [optional] |
| **predefinedAcl** | **String**| Apply a predefined set of access controls to this bucket. | [optional] [enum: authenticatedRead, private, projectPrivate, publicRead, publicReadWrite] |
| **predefinedDefaultObjectAcl** | **String**| Apply a predefined set of default object access controls to this bucket. | [optional] [enum: authenticatedRead, bucketOwnerFullControl, bucketOwnerRead, private, projectPrivate, publicRead] |
| **projection** | **String**| Set of properties to return. Defaults to full. | [optional] [enum: full, noAcl] |
| **userProject** | **String**| The project to be billed for this request. Required for Requester Pays buckets. | [optional] |
| **bucket2** | [**Bucket**](Bucket.md)|  | [optional] |

### Return type

[**Bucket**](Bucket.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

