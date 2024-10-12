# ManagedFoldersApi

All URIs are relative to *https://storage.googleapis.com/storage/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**storageManagedFoldersDelete**](ManagedFoldersApi.md#storageManagedFoldersDelete) | **DELETE** /b/{bucket}/managedFolders/{managedFolder} |  |
| [**storageManagedFoldersGet**](ManagedFoldersApi.md#storageManagedFoldersGet) | **GET** /b/{bucket}/managedFolders/{managedFolder} |  |
| [**storageManagedFoldersGetIamPolicy**](ManagedFoldersApi.md#storageManagedFoldersGetIamPolicy) | **GET** /b/{bucket}/managedFolders/{managedFolder}/iam |  |
| [**storageManagedFoldersInsert**](ManagedFoldersApi.md#storageManagedFoldersInsert) | **POST** /b/{bucket}/managedFolders |  |
| [**storageManagedFoldersList**](ManagedFoldersApi.md#storageManagedFoldersList) | **GET** /b/{bucket}/managedFolders |  |
| [**storageManagedFoldersSetIamPolicy**](ManagedFoldersApi.md#storageManagedFoldersSetIamPolicy) | **PUT** /b/{bucket}/managedFolders/{managedFolder}/iam |  |
| [**storageManagedFoldersTestIamPermissions**](ManagedFoldersApi.md#storageManagedFoldersTestIamPermissions) | **GET** /b/{bucket}/managedFolders/{managedFolder}/iam/testPermissions |  |


<a id="storageManagedFoldersDelete"></a>
# **storageManagedFoldersDelete**
> storageManagedFoldersDelete(bucket, managedFolder, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, ifMetagenerationMatch, ifMetagenerationNotMatch)



Permanently deletes a managed folder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedFoldersApi;

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

    ManagedFoldersApi apiInstance = new ManagedFoldersApi(defaultClient);
    String bucket = "bucket_example"; // String | Name of the bucket containing the managed folder.
    String managedFolder = "managedFolder_example"; // String | The managed folder name/path.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String uploadType = "uploadType_example"; // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String ifMetagenerationMatch = "ifMetagenerationMatch_example"; // String | If set, only deletes the managed folder if its metageneration matches this value.
    String ifMetagenerationNotMatch = "ifMetagenerationNotMatch_example"; // String | If set, only deletes the managed folder if its metageneration does not match this value.
    try {
      apiInstance.storageManagedFoldersDelete(bucket, managedFolder, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, ifMetagenerationMatch, ifMetagenerationNotMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedFoldersApi#storageManagedFoldersDelete");
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
| **bucket** | **String**| Name of the bucket containing the managed folder. | |
| **managedFolder** | **String**| The managed folder name/path. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **ifMetagenerationMatch** | **String**| If set, only deletes the managed folder if its metageneration matches this value. | [optional] |
| **ifMetagenerationNotMatch** | **String**| If set, only deletes the managed folder if its metageneration does not match this value. | [optional] |

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

<a id="storageManagedFoldersGet"></a>
# **storageManagedFoldersGet**
> ManagedFolder storageManagedFoldersGet(bucket, managedFolder, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, ifMetagenerationMatch, ifMetagenerationNotMatch)



Returns metadata of the specified managed folder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedFoldersApi;

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

    ManagedFoldersApi apiInstance = new ManagedFoldersApi(defaultClient);
    String bucket = "bucket_example"; // String | Name of the bucket containing the managed folder.
    String managedFolder = "managedFolder_example"; // String | The managed folder name/path.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String uploadType = "uploadType_example"; // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String ifMetagenerationMatch = "ifMetagenerationMatch_example"; // String | Makes the return of the managed folder metadata conditional on whether the managed folder's current metageneration matches the given value.
    String ifMetagenerationNotMatch = "ifMetagenerationNotMatch_example"; // String | Makes the return of the managed folder metadata conditional on whether the managed folder's current metageneration does not match the given value.
    try {
      ManagedFolder result = apiInstance.storageManagedFoldersGet(bucket, managedFolder, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, ifMetagenerationMatch, ifMetagenerationNotMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedFoldersApi#storageManagedFoldersGet");
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
| **bucket** | **String**| Name of the bucket containing the managed folder. | |
| **managedFolder** | **String**| The managed folder name/path. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **ifMetagenerationMatch** | **String**| Makes the return of the managed folder metadata conditional on whether the managed folder&#39;s current metageneration matches the given value. | [optional] |
| **ifMetagenerationNotMatch** | **String**| Makes the return of the managed folder metadata conditional on whether the managed folder&#39;s current metageneration does not match the given value. | [optional] |

### Return type

[**ManagedFolder**](ManagedFolder.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="storageManagedFoldersGetIamPolicy"></a>
# **storageManagedFoldersGetIamPolicy**
> Policy storageManagedFoldersGetIamPolicy(bucket, managedFolder, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, optionsRequestedPolicyVersion, userProject)



Returns an IAM policy for the specified managed folder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedFoldersApi;

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

    ManagedFoldersApi apiInstance = new ManagedFoldersApi(defaultClient);
    String bucket = "bucket_example"; // String | Name of the bucket containing the managed folder.
    String managedFolder = "managedFolder_example"; // String | The managed folder name/path.
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
      Policy result = apiInstance.storageManagedFoldersGetIamPolicy(bucket, managedFolder, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, optionsRequestedPolicyVersion, userProject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedFoldersApi#storageManagedFoldersGetIamPolicy");
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
| **bucket** | **String**| Name of the bucket containing the managed folder. | |
| **managedFolder** | **String**| The managed folder name/path. | |
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

<a id="storageManagedFoldersInsert"></a>
# **storageManagedFoldersInsert**
> ManagedFolder storageManagedFoldersInsert(bucket, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, managedFolder)



Creates a new managed folder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedFoldersApi;

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

    ManagedFoldersApi apiInstance = new ManagedFoldersApi(defaultClient);
    String bucket = "bucket_example"; // String | Name of the bucket containing the managed folder.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String uploadType = "uploadType_example"; // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    ManagedFolder managedFolder = new ManagedFolder(); // ManagedFolder | 
    try {
      ManagedFolder result = apiInstance.storageManagedFoldersInsert(bucket, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, managedFolder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedFoldersApi#storageManagedFoldersInsert");
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
| **bucket** | **String**| Name of the bucket containing the managed folder. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **managedFolder** | [**ManagedFolder**](ManagedFolder.md)|  | [optional] |

### Return type

[**ManagedFolder**](ManagedFolder.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="storageManagedFoldersList"></a>
# **storageManagedFoldersList**
> ManagedFolders storageManagedFoldersList(bucket, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, pageSize, pageToken, prefix)



Lists managed folders in the given bucket.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedFoldersApi;

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

    ManagedFoldersApi apiInstance = new ManagedFoldersApi(defaultClient);
    String bucket = "bucket_example"; // String | Name of the bucket containing the managed folder.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String uploadType = "uploadType_example"; // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Integer pageSize = 56; // Integer | Maximum number of items to return in a single page of responses.
    String pageToken = "pageToken_example"; // String | A previously-returned page token representing part of the larger set of results to view.
    String prefix = "prefix_example"; // String | The managed folder name/path prefix to filter the output list of results.
    try {
      ManagedFolders result = apiInstance.storageManagedFoldersList(bucket, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, pageSize, pageToken, prefix);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedFoldersApi#storageManagedFoldersList");
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
| **bucket** | **String**| Name of the bucket containing the managed folder. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **pageSize** | **Integer**| Maximum number of items to return in a single page of responses. | [optional] |
| **pageToken** | **String**| A previously-returned page token representing part of the larger set of results to view. | [optional] |
| **prefix** | **String**| The managed folder name/path prefix to filter the output list of results. | [optional] |

### Return type

[**ManagedFolders**](ManagedFolders.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="storageManagedFoldersSetIamPolicy"></a>
# **storageManagedFoldersSetIamPolicy**
> Policy storageManagedFoldersSetIamPolicy(bucket, managedFolder, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, userProject, policy)



Updates an IAM policy for the specified managed folder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedFoldersApi;

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

    ManagedFoldersApi apiInstance = new ManagedFoldersApi(defaultClient);
    String bucket = "bucket_example"; // String | Name of the bucket containing the managed folder.
    String managedFolder = "managedFolder_example"; // String | The managed folder name/path.
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
      Policy result = apiInstance.storageManagedFoldersSetIamPolicy(bucket, managedFolder, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, userProject, policy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedFoldersApi#storageManagedFoldersSetIamPolicy");
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
| **bucket** | **String**| Name of the bucket containing the managed folder. | |
| **managedFolder** | **String**| The managed folder name/path. | |
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

<a id="storageManagedFoldersTestIamPermissions"></a>
# **storageManagedFoldersTestIamPermissions**
> TestIamPermissionsResponse storageManagedFoldersTestIamPermissions(bucket, managedFolder, permissions, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, userProject)



Tests a set of permissions on the given managed folder to see which, if any, are held by the caller.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedFoldersApi;

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

    ManagedFoldersApi apiInstance = new ManagedFoldersApi(defaultClient);
    String bucket = "bucket_example"; // String | Name of the bucket containing the managed folder.
    String managedFolder = "managedFolder_example"; // String | The managed folder name/path.
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
      TestIamPermissionsResponse result = apiInstance.storageManagedFoldersTestIamPermissions(bucket, managedFolder, permissions, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, userProject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedFoldersApi#storageManagedFoldersTestIamPermissions");
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
| **bucket** | **String**| Name of the bucket containing the managed folder. | |
| **managedFolder** | **String**| The managed folder name/path. | |
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

