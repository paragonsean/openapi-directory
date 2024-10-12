# BucketsApi

All URIs are relative to *https://storage.googleapis.com/storage/v1beta2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**storageBucketsDelete**](BucketsApi.md#storageBucketsDelete) | **DELETE** /b/{bucket} |  |
| [**storageBucketsGet**](BucketsApi.md#storageBucketsGet) | **GET** /b/{bucket} |  |
| [**storageBucketsInsert**](BucketsApi.md#storageBucketsInsert) | **POST** /b |  |
| [**storageBucketsList**](BucketsApi.md#storageBucketsList) | **GET** /b |  |
| [**storageBucketsPatch**](BucketsApi.md#storageBucketsPatch) | **PATCH** /b/{bucket} |  |
| [**storageBucketsUpdate**](BucketsApi.md#storageBucketsUpdate) | **PUT** /b/{bucket} |  |


<a id="storageBucketsDelete"></a>
# **storageBucketsDelete**
> storageBucketsDelete(bucket, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, ifMetagenerationMatch, ifMetagenerationNotMatch)



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
    defaultClient.setBasePath("https://storage.googleapis.com/storage/v1beta2");
    
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
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String ifMetagenerationMatch = "ifMetagenerationMatch_example"; // String | Makes the return of the bucket metadata conditional on whether the bucket's current metageneration matches the given value.
    String ifMetagenerationNotMatch = "ifMetagenerationNotMatch_example"; // String | Makes the return of the bucket metadata conditional on whether the bucket's current metageneration does not match the given value.
    try {
      apiInstance.storageBucketsDelete(bucket, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, ifMetagenerationMatch, ifMetagenerationNotMatch);
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
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **ifMetagenerationMatch** | **String**| Makes the return of the bucket metadata conditional on whether the bucket&#39;s current metageneration matches the given value. | [optional] |
| **ifMetagenerationNotMatch** | **String**| Makes the return of the bucket metadata conditional on whether the bucket&#39;s current metageneration does not match the given value. | [optional] |

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
> Bucket storageBucketsGet(bucket, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, ifMetagenerationMatch, ifMetagenerationNotMatch, projection)



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
    defaultClient.setBasePath("https://storage.googleapis.com/storage/v1beta2");
    
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
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String ifMetagenerationMatch = "ifMetagenerationMatch_example"; // String | Makes the return of the bucket metadata conditional on whether the bucket's current metageneration matches the given value.
    String ifMetagenerationNotMatch = "ifMetagenerationNotMatch_example"; // String | Makes the return of the bucket metadata conditional on whether the bucket's current metageneration does not match the given value.
    String projection = "full"; // String | Set of properties to return. Defaults to noAcl.
    try {
      Bucket result = apiInstance.storageBucketsGet(bucket, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, ifMetagenerationMatch, ifMetagenerationNotMatch, projection);
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
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **ifMetagenerationMatch** | **String**| Makes the return of the bucket metadata conditional on whether the bucket&#39;s current metageneration matches the given value. | [optional] |
| **ifMetagenerationNotMatch** | **String**| Makes the return of the bucket metadata conditional on whether the bucket&#39;s current metageneration does not match the given value. | [optional] |
| **projection** | **String**| Set of properties to return. Defaults to noAcl. | [optional] [enum: full, noAcl] |

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

<a id="storageBucketsInsert"></a>
# **storageBucketsInsert**
> Bucket storageBucketsInsert(project, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, projection, bucket)



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
    defaultClient.setBasePath("https://storage.googleapis.com/storage/v1beta2");
    
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
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String projection = "full"; // String | Set of properties to return. Defaults to noAcl, unless the bucket resource specifies acl or defaultObjectAcl properties, when it defaults to full.
    Bucket bucket = new Bucket(); // Bucket | 
    try {
      Bucket result = apiInstance.storageBucketsInsert(project, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, projection, bucket);
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
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **projection** | **String**| Set of properties to return. Defaults to noAcl, unless the bucket resource specifies acl or defaultObjectAcl properties, when it defaults to full. | [optional] [enum: full, noAcl] |
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
> Buckets storageBucketsList(project, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, maxResults, pageToken, projection)



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
    defaultClient.setBasePath("https://storage.googleapis.com/storage/v1beta2");
    
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
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Integer maxResults = 56; // Integer | Maximum number of buckets to return.
    String pageToken = "pageToken_example"; // String | A previously-returned page token representing part of the larger set of results to view.
    String projection = "full"; // String | Set of properties to return. Defaults to noAcl.
    try {
      Buckets result = apiInstance.storageBucketsList(project, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, maxResults, pageToken, projection);
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
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **maxResults** | **Integer**| Maximum number of buckets to return. | [optional] |
| **pageToken** | **String**| A previously-returned page token representing part of the larger set of results to view. | [optional] |
| **projection** | **String**| Set of properties to return. Defaults to noAcl. | [optional] [enum: full, noAcl] |

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

<a id="storageBucketsPatch"></a>
# **storageBucketsPatch**
> Bucket storageBucketsPatch(bucket, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, ifMetagenerationMatch, ifMetagenerationNotMatch, projection, bucket2)



Updates a bucket. This method supports patch semantics.

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
    defaultClient.setBasePath("https://storage.googleapis.com/storage/v1beta2");
    
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
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String ifMetagenerationMatch = "ifMetagenerationMatch_example"; // String | Makes the return of the bucket metadata conditional on whether the bucket's current metageneration matches the given value.
    String ifMetagenerationNotMatch = "ifMetagenerationNotMatch_example"; // String | Makes the return of the bucket metadata conditional on whether the bucket's current metageneration does not match the given value.
    String projection = "full"; // String | Set of properties to return. Defaults to full.
    Bucket bucket2 = new Bucket(); // Bucket | 
    try {
      Bucket result = apiInstance.storageBucketsPatch(bucket, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, ifMetagenerationMatch, ifMetagenerationNotMatch, projection, bucket2);
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
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **ifMetagenerationMatch** | **String**| Makes the return of the bucket metadata conditional on whether the bucket&#39;s current metageneration matches the given value. | [optional] |
| **ifMetagenerationNotMatch** | **String**| Makes the return of the bucket metadata conditional on whether the bucket&#39;s current metageneration does not match the given value. | [optional] |
| **projection** | **String**| Set of properties to return. Defaults to full. | [optional] [enum: full, noAcl] |
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

<a id="storageBucketsUpdate"></a>
# **storageBucketsUpdate**
> Bucket storageBucketsUpdate(bucket, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, ifMetagenerationMatch, ifMetagenerationNotMatch, projection, bucket2)



Updates a bucket.

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
    defaultClient.setBasePath("https://storage.googleapis.com/storage/v1beta2");
    
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
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String ifMetagenerationMatch = "ifMetagenerationMatch_example"; // String | Makes the return of the bucket metadata conditional on whether the bucket's current metageneration matches the given value.
    String ifMetagenerationNotMatch = "ifMetagenerationNotMatch_example"; // String | Makes the return of the bucket metadata conditional on whether the bucket's current metageneration does not match the given value.
    String projection = "full"; // String | Set of properties to return. Defaults to full.
    Bucket bucket2 = new Bucket(); // Bucket | 
    try {
      Bucket result = apiInstance.storageBucketsUpdate(bucket, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, ifMetagenerationMatch, ifMetagenerationNotMatch, projection, bucket2);
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
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **ifMetagenerationMatch** | **String**| Makes the return of the bucket metadata conditional on whether the bucket&#39;s current metageneration matches the given value. | [optional] |
| **ifMetagenerationNotMatch** | **String**| Makes the return of the bucket metadata conditional on whether the bucket&#39;s current metageneration does not match the given value. | [optional] |
| **projection** | **String**| Set of properties to return. Defaults to full. | [optional] [enum: full, noAcl] |
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

