# FoldersApi

All URIs are relative to *https://storage.googleapis.com/storage/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**storageFoldersDelete**](FoldersApi.md#storageFoldersDelete) | **DELETE** /b/{bucket}/folders/{folder} |  |
| [**storageFoldersGet**](FoldersApi.md#storageFoldersGet) | **GET** /b/{bucket}/folders/{folder} |  |
| [**storageFoldersInsert**](FoldersApi.md#storageFoldersInsert) | **POST** /b/{bucket}/folders |  |
| [**storageFoldersList**](FoldersApi.md#storageFoldersList) | **GET** /b/{bucket}/folders |  |
| [**storageFoldersRename**](FoldersApi.md#storageFoldersRename) | **POST** /b/{bucket}/folders/{sourceFolder}/renameTo/folders/{destinationFolder} |  |


<a id="storageFoldersDelete"></a>
# **storageFoldersDelete**
> storageFoldersDelete(bucket, folder, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, ifMetagenerationMatch, ifMetagenerationNotMatch)



Permanently deletes a folder. Only applicable to buckets with hierarchical namespace enabled.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FoldersApi;

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

    FoldersApi apiInstance = new FoldersApi(defaultClient);
    String bucket = "bucket_example"; // String | Name of the bucket in which the folder resides.
    String folder = "folder_example"; // String | Name of a folder.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String uploadType = "uploadType_example"; // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String ifMetagenerationMatch = "ifMetagenerationMatch_example"; // String | If set, only deletes the folder if its metageneration matches this value.
    String ifMetagenerationNotMatch = "ifMetagenerationNotMatch_example"; // String | If set, only deletes the folder if its metageneration does not match this value.
    try {
      apiInstance.storageFoldersDelete(bucket, folder, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, ifMetagenerationMatch, ifMetagenerationNotMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling FoldersApi#storageFoldersDelete");
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
| **bucket** | **String**| Name of the bucket in which the folder resides. | |
| **folder** | **String**| Name of a folder. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **ifMetagenerationMatch** | **String**| If set, only deletes the folder if its metageneration matches this value. | [optional] |
| **ifMetagenerationNotMatch** | **String**| If set, only deletes the folder if its metageneration does not match this value. | [optional] |

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

<a id="storageFoldersGet"></a>
# **storageFoldersGet**
> Folder storageFoldersGet(bucket, folder, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, ifMetagenerationMatch, ifMetagenerationNotMatch)



Returns metadata for the specified folder. Only applicable to buckets with hierarchical namespace enabled.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FoldersApi;

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

    FoldersApi apiInstance = new FoldersApi(defaultClient);
    String bucket = "bucket_example"; // String | Name of the bucket in which the folder resides.
    String folder = "folder_example"; // String | Name of a folder.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String uploadType = "uploadType_example"; // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String ifMetagenerationMatch = "ifMetagenerationMatch_example"; // String | Makes the return of the folder metadata conditional on whether the folder's current metageneration matches the given value.
    String ifMetagenerationNotMatch = "ifMetagenerationNotMatch_example"; // String | Makes the return of the folder metadata conditional on whether the folder's current metageneration does not match the given value.
    try {
      Folder result = apiInstance.storageFoldersGet(bucket, folder, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, ifMetagenerationMatch, ifMetagenerationNotMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FoldersApi#storageFoldersGet");
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
| **bucket** | **String**| Name of the bucket in which the folder resides. | |
| **folder** | **String**| Name of a folder. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **ifMetagenerationMatch** | **String**| Makes the return of the folder metadata conditional on whether the folder&#39;s current metageneration matches the given value. | [optional] |
| **ifMetagenerationNotMatch** | **String**| Makes the return of the folder metadata conditional on whether the folder&#39;s current metageneration does not match the given value. | [optional] |

### Return type

[**Folder**](Folder.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="storageFoldersInsert"></a>
# **storageFoldersInsert**
> Folder storageFoldersInsert(bucket, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, recursive, folder)



Creates a new folder. Only applicable to buckets with hierarchical namespace enabled.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FoldersApi;

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

    FoldersApi apiInstance = new FoldersApi(defaultClient);
    String bucket = "bucket_example"; // String | Name of the bucket in which the folder resides.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String uploadType = "uploadType_example"; // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Boolean recursive = true; // Boolean | If true, any parent folder which doesn’t exist will be created automatically.
    Folder folder = new Folder(); // Folder | 
    try {
      Folder result = apiInstance.storageFoldersInsert(bucket, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, recursive, folder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FoldersApi#storageFoldersInsert");
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
| **bucket** | **String**| Name of the bucket in which the folder resides. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **recursive** | **Boolean**| If true, any parent folder which doesn’t exist will be created automatically. | [optional] |
| **folder** | [**Folder**](Folder.md)|  | [optional] |

### Return type

[**Folder**](Folder.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="storageFoldersList"></a>
# **storageFoldersList**
> Folders storageFoldersList(bucket, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, delimiter, endOffset, pageSize, pageToken, prefix, startOffset)



Retrieves a list of folders matching the criteria. Only applicable to buckets with hierarchical namespace enabled.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FoldersApi;

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

    FoldersApi apiInstance = new FoldersApi(defaultClient);
    String bucket = "bucket_example"; // String | Name of the bucket in which to look for folders.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String uploadType = "uploadType_example"; // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String delimiter = "delimiter_example"; // String | Returns results in a directory-like mode. The only supported value is '/'. If set, items will only contain folders that either exactly match the prefix, or are one level below the prefix.
    String endOffset = "endOffset_example"; // String | Filter results to folders whose names are lexicographically before endOffset. If startOffset is also set, the folders listed will have names between startOffset (inclusive) and endOffset (exclusive).
    Integer pageSize = 56; // Integer | Maximum number of items to return in a single page of responses.
    String pageToken = "pageToken_example"; // String | A previously-returned page token representing part of the larger set of results to view.
    String prefix = "prefix_example"; // String | Filter results to folders whose paths begin with this prefix. If set, the value must either be an empty string or end with a '/'.
    String startOffset = "startOffset_example"; // String | Filter results to folders whose names are lexicographically equal to or after startOffset. If endOffset is also set, the folders listed will have names between startOffset (inclusive) and endOffset (exclusive).
    try {
      Folders result = apiInstance.storageFoldersList(bucket, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, delimiter, endOffset, pageSize, pageToken, prefix, startOffset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FoldersApi#storageFoldersList");
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
| **bucket** | **String**| Name of the bucket in which to look for folders. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **delimiter** | **String**| Returns results in a directory-like mode. The only supported value is &#39;/&#39;. If set, items will only contain folders that either exactly match the prefix, or are one level below the prefix. | [optional] |
| **endOffset** | **String**| Filter results to folders whose names are lexicographically before endOffset. If startOffset is also set, the folders listed will have names between startOffset (inclusive) and endOffset (exclusive). | [optional] |
| **pageSize** | **Integer**| Maximum number of items to return in a single page of responses. | [optional] |
| **pageToken** | **String**| A previously-returned page token representing part of the larger set of results to view. | [optional] |
| **prefix** | **String**| Filter results to folders whose paths begin with this prefix. If set, the value must either be an empty string or end with a &#39;/&#39;. | [optional] |
| **startOffset** | **String**| Filter results to folders whose names are lexicographically equal to or after startOffset. If endOffset is also set, the folders listed will have names between startOffset (inclusive) and endOffset (exclusive). | [optional] |

### Return type

[**Folders**](Folders.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="storageFoldersRename"></a>
# **storageFoldersRename**
> GoogleLongrunningOperation storageFoldersRename(bucket, sourceFolder, destinationFolder, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, ifSourceMetagenerationMatch, ifSourceMetagenerationNotMatch)



Renames a source folder to a destination folder. Only applicable to buckets with hierarchical namespace enabled.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FoldersApi;

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

    FoldersApi apiInstance = new FoldersApi(defaultClient);
    String bucket = "bucket_example"; // String | Name of the bucket in which the folders are in.
    String sourceFolder = "sourceFolder_example"; // String | Name of the source folder.
    String destinationFolder = "destinationFolder_example"; // String | Name of the destination folder.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String uploadType = "uploadType_example"; // String | Upload protocol for media (e.g. \"media\", \"multipart\", \"resumable\").
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String ifSourceMetagenerationMatch = "ifSourceMetagenerationMatch_example"; // String | Makes the operation conditional on whether the source object's current metageneration matches the given value.
    String ifSourceMetagenerationNotMatch = "ifSourceMetagenerationNotMatch_example"; // String | Makes the operation conditional on whether the source object's current metageneration does not match the given value.
    try {
      GoogleLongrunningOperation result = apiInstance.storageFoldersRename(bucket, sourceFolder, destinationFolder, alt, fields, key, oauthToken, prettyPrint, quotaUser, uploadType, userIp, ifSourceMetagenerationMatch, ifSourceMetagenerationNotMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FoldersApi#storageFoldersRename");
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
| **bucket** | **String**| Name of the bucket in which the folders are in. | |
| **sourceFolder** | **String**| Name of the source folder. | |
| **destinationFolder** | **String**| Name of the destination folder. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **uploadType** | **String**| Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;). | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **ifSourceMetagenerationMatch** | **String**| Makes the operation conditional on whether the source object&#39;s current metageneration matches the given value. | [optional] |
| **ifSourceMetagenerationNotMatch** | **String**| Makes the operation conditional on whether the source object&#39;s current metageneration does not match the given value. | [optional] |

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

