# ProjectsApi

All URIs are relative to *https://storage.googleapis.com/storage/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**storageProjectsHmacKeysCreate**](ProjectsApi.md#storageProjectsHmacKeysCreate) | **POST** /projects/{projectId}/hmacKeys |  |
| [**storageProjectsHmacKeysDelete**](ProjectsApi.md#storageProjectsHmacKeysDelete) | **DELETE** /projects/{projectId}/hmacKeys/{accessId} |  |
| [**storageProjectsHmacKeysGet**](ProjectsApi.md#storageProjectsHmacKeysGet) | **GET** /projects/{projectId}/hmacKeys/{accessId} |  |
| [**storageProjectsHmacKeysList**](ProjectsApi.md#storageProjectsHmacKeysList) | **GET** /projects/{projectId}/hmacKeys |  |
| [**storageProjectsHmacKeysUpdate**](ProjectsApi.md#storageProjectsHmacKeysUpdate) | **PUT** /projects/{projectId}/hmacKeys/{accessId} |  |
| [**storageProjectsServiceAccountGet**](ProjectsApi.md#storageProjectsServiceAccountGet) | **GET** /projects/{projectId}/serviceAccount |  |


<a id="storageProjectsHmacKeysCreate"></a>
# **storageProjectsHmacKeysCreate**
> HmacKey storageProjectsHmacKeysCreate(projectId, serviceAccountEmail, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, userProject)



Creates a new HMAC key for the specified service account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String projectId = "projectId_example"; // String | Project ID owning the service account.
    String serviceAccountEmail = "serviceAccountEmail_example"; // String | Email address of the service account.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String uploadType = "uploadType_example"; // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String userProject = "userProject_example"; // String | The project to be billed for this request.
    try {
      HmacKey result = apiInstance.storageProjectsHmacKeysCreate(projectId, serviceAccountEmail, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, userProject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#storageProjectsHmacKeysCreate");
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
| **projectId** | **String**| Project ID owning the service account. | |
| **serviceAccountEmail** | **String**| Email address of the service account. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **userProject** | **String**| The project to be billed for this request. | [optional] |

### Return type

[**HmacKey**](HmacKey.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="storageProjectsHmacKeysDelete"></a>
# **storageProjectsHmacKeysDelete**
> storageProjectsHmacKeysDelete(projectId, accessId, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, userProject)



Deletes an HMAC key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String projectId = "projectId_example"; // String | Project ID owning the requested key
    String accessId = "accessId_example"; // String | Name of the HMAC key to be deleted.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String uploadType = "uploadType_example"; // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String userProject = "userProject_example"; // String | The project to be billed for this request.
    try {
      apiInstance.storageProjectsHmacKeysDelete(projectId, accessId, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, userProject);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#storageProjectsHmacKeysDelete");
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
| **projectId** | **String**| Project ID owning the requested key | |
| **accessId** | **String**| Name of the HMAC key to be deleted. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **userProject** | **String**| The project to be billed for this request. | [optional] |

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

<a id="storageProjectsHmacKeysGet"></a>
# **storageProjectsHmacKeysGet**
> HmacKeyMetadata storageProjectsHmacKeysGet(projectId, accessId, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, userProject)



Retrieves an HMAC key&#39;s metadata

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String projectId = "projectId_example"; // String | Project ID owning the service account of the requested key.
    String accessId = "accessId_example"; // String | Name of the HMAC key.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String uploadType = "uploadType_example"; // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String userProject = "userProject_example"; // String | The project to be billed for this request.
    try {
      HmacKeyMetadata result = apiInstance.storageProjectsHmacKeysGet(projectId, accessId, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, userProject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#storageProjectsHmacKeysGet");
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
| **projectId** | **String**| Project ID owning the service account of the requested key. | |
| **accessId** | **String**| Name of the HMAC key. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **userProject** | **String**| The project to be billed for this request. | [optional] |

### Return type

[**HmacKeyMetadata**](HmacKeyMetadata.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="storageProjectsHmacKeysList"></a>
# **storageProjectsHmacKeysList**
> HmacKeysMetadata storageProjectsHmacKeysList(projectId, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, maxResults, pageToken, serviceAccountEmail, showDeletedKeys, userProject)



Retrieves a list of HMAC keys matching the criteria.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String projectId = "projectId_example"; // String | Name of the project in which to look for HMAC keys.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String uploadType = "uploadType_example"; // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Integer maxResults = 56; // Integer | Maximum number of items to return in a single page of responses. The service uses this parameter or 250 items, whichever is smaller. The max number of items per page will also be limited by the number of distinct service accounts in the response. If the number of service accounts in a single response is too high, the page will truncated and a next page token will be returned.
    String pageToken = "pageToken_example"; // String | A previously-returned page token representing part of the larger set of results to view.
    String serviceAccountEmail = "serviceAccountEmail_example"; // String | If present, only keys for the given service account are returned.
    Boolean showDeletedKeys = true; // Boolean | Whether or not to show keys in the DELETED state.
    String userProject = "userProject_example"; // String | The project to be billed for this request.
    try {
      HmacKeysMetadata result = apiInstance.storageProjectsHmacKeysList(projectId, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, maxResults, pageToken, serviceAccountEmail, showDeletedKeys, userProject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#storageProjectsHmacKeysList");
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
| **projectId** | **String**| Name of the project in which to look for HMAC keys. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **maxResults** | **Integer**| Maximum number of items to return in a single page of responses. The service uses this parameter or 250 items, whichever is smaller. The max number of items per page will also be limited by the number of distinct service accounts in the response. If the number of service accounts in a single response is too high, the page will truncated and a next page token will be returned. | [optional] |
| **pageToken** | **String**| A previously-returned page token representing part of the larger set of results to view. | [optional] |
| **serviceAccountEmail** | **String**| If present, only keys for the given service account are returned. | [optional] |
| **showDeletedKeys** | **Boolean**| Whether or not to show keys in the DELETED state. | [optional] |
| **userProject** | **String**| The project to be billed for this request. | [optional] |

### Return type

[**HmacKeysMetadata**](HmacKeysMetadata.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="storageProjectsHmacKeysUpdate"></a>
# **storageProjectsHmacKeysUpdate**
> HmacKeyMetadata storageProjectsHmacKeysUpdate(projectId, accessId, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, userProject, hmacKeyMetadata)



Updates the state of an HMAC key. See the HMAC Key resource descriptor for valid states.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String projectId = "projectId_example"; // String | Project ID owning the service account of the updated key.
    String accessId = "accessId_example"; // String | Name of the HMAC key being updated.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String uploadType = "uploadType_example"; // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String userProject = "userProject_example"; // String | The project to be billed for this request.
    HmacKeyMetadata hmacKeyMetadata = new HmacKeyMetadata(); // HmacKeyMetadata | 
    try {
      HmacKeyMetadata result = apiInstance.storageProjectsHmacKeysUpdate(projectId, accessId, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, userProject, hmacKeyMetadata);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#storageProjectsHmacKeysUpdate");
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
| **projectId** | **String**| Project ID owning the service account of the updated key. | |
| **accessId** | **String**| Name of the HMAC key being updated. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **userProject** | **String**| The project to be billed for this request. | [optional] |
| **hmacKeyMetadata** | [**HmacKeyMetadata**](HmacKeyMetadata.md)|  | [optional] |

### Return type

[**HmacKeyMetadata**](HmacKeyMetadata.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="storageProjectsServiceAccountGet"></a>
# **storageProjectsServiceAccountGet**
> ServiceAccount storageProjectsServiceAccountGet(projectId, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, userProject)



Get the email address of this project&#39;s Google Cloud Storage service account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String projectId = "projectId_example"; // String | Project ID
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String uploadType = "uploadType_example"; // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String userProject = "userProject_example"; // String | The project to be billed for this request.
    try {
      ServiceAccount result = apiInstance.storageProjectsServiceAccountGet(projectId, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, userProject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#storageProjectsServiceAccountGet");
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
| **projectId** | **String**| Project ID | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **userProject** | **String**| The project to be billed for this request. | [optional] |

### Return type

[**ServiceAccount**](ServiceAccount.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

