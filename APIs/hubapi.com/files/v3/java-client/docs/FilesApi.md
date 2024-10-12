# FilesApi

All URIs are relative to *https://api.hubapi.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteFilesV3FilesFileIdArchive**](FilesApi.md#deleteFilesV3FilesFileIdArchive) | **DELETE** /files/v3/files/{fileId} | Delete file |
| [**deleteFilesV3FilesFileIdGdprDeleteArchiveGDPR**](FilesApi.md#deleteFilesV3FilesFileIdGdprDeleteArchiveGDPR) | **DELETE** /files/v3/files/{fileId}/gdpr-delete | GDPR delete |
| [**getFilesV3FilesFileIdGetById**](FilesApi.md#getFilesV3FilesFileIdGetById) | **GET** /files/v3/files/{fileId} | Get file. |
| [**getFilesV3FilesFileIdSignedUrlGetSignedUrl**](FilesApi.md#getFilesV3FilesFileIdSignedUrlGetSignedUrl) | **GET** /files/v3/files/{fileId}/signed-url | Get signed URL to access private file. |
| [**getFilesV3FilesImportFromUrlAsyncTasksTaskIdStatusCheckImport**](FilesApi.md#getFilesV3FilesImportFromUrlAsyncTasksTaskIdStatusCheckImport) | **GET** /files/v3/files/import-from-url/async/tasks/{taskId}/status | Check import status. |
| [**getFilesV3FilesSearchDoSearch**](FilesApi.md#getFilesV3FilesSearchDoSearch) | **GET** /files/v3/files/search | Search files |
| [**getFilesV3FilesStatPathGetMetadata**](FilesApi.md#getFilesV3FilesStatPathGetMetadata) | **GET** /files/v3/files/stat/{path} |  |
| [**patchFilesV3FilesFileIdUpdateProperties**](FilesApi.md#patchFilesV3FilesFileIdUpdateProperties) | **PATCH** /files/v3/files/{fileId} | update file properties |
| [**postFilesV3FilesImportFromUrlAsyncImportFromUrl**](FilesApi.md#postFilesV3FilesImportFromUrlAsyncImportFromUrl) | **POST** /files/v3/files/import-from-url/async | Import a file from a URL into the file manager. |
| [**postFilesV3FilesUpload**](FilesApi.md#postFilesV3FilesUpload) | **POST** /files/v3/files | Upload file |
| [**putFilesV3FilesFileIdReplace**](FilesApi.md#putFilesV3FilesFileIdReplace) | **PUT** /files/v3/files/{fileId} | Replace file. |


<a id="deleteFilesV3FilesFileIdArchive"></a>
# **deleteFilesV3FilesFileIdArchive**
> deleteFilesV3FilesFileIdArchive(fileId)

Delete file

Delete file by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure OAuth2 access token for authorization: oauth2_legacy
    OAuth oauth2_legacy = (OAuth) defaultClient.getAuthentication("oauth2_legacy");
    oauth2_legacy.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: private_apps_legacy
    ApiKeyAuth private_apps_legacy = (ApiKeyAuth) defaultClient.getAuthentication("private_apps_legacy");
    private_apps_legacy.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_apps_legacy.setApiKeyPrefix("Token");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String fileId = "fileId_example"; // String | FileId to delete
    try {
      apiInstance.deleteFilesV3FilesFileIdArchive(fileId);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#deleteFilesV3FilesFileIdArchive");
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
| **fileId** | **String**| FileId to delete | |

### Return type

null (empty response body)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No content |  -  |
| **0** | An error occurred. |  -  |

<a id="deleteFilesV3FilesFileIdGdprDeleteArchiveGDPR"></a>
# **deleteFilesV3FilesFileIdGdprDeleteArchiveGDPR**
> deleteFilesV3FilesFileIdGdprDeleteArchiveGDPR(fileId)

GDPR delete

GDRP delete file

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure OAuth2 access token for authorization: oauth2_legacy
    OAuth oauth2_legacy = (OAuth) defaultClient.getAuthentication("oauth2_legacy");
    oauth2_legacy.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: private_apps_legacy
    ApiKeyAuth private_apps_legacy = (ApiKeyAuth) defaultClient.getAuthentication("private_apps_legacy");
    private_apps_legacy.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_apps_legacy.setApiKeyPrefix("Token");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String fileId = "fileId_example"; // String | ID of file to GDPR delete
    try {
      apiInstance.deleteFilesV3FilesFileIdGdprDeleteArchiveGDPR(fileId);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#deleteFilesV3FilesFileIdGdprDeleteArchiveGDPR");
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
| **fileId** | **String**| ID of file to GDPR delete | |

### Return type

null (empty response body)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No content |  -  |
| **0** | An error occurred. |  -  |

<a id="getFilesV3FilesFileIdGetById"></a>
# **getFilesV3FilesFileIdGetById**
> ModelFile getFilesV3FilesFileIdGetById(fileId, properties)

Get file.

Get file by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure OAuth2 access token for authorization: oauth2_legacy
    OAuth oauth2_legacy = (OAuth) defaultClient.getAuthentication("oauth2_legacy");
    oauth2_legacy.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: private_apps_legacy
    ApiKeyAuth private_apps_legacy = (ApiKeyAuth) defaultClient.getAuthentication("private_apps_legacy");
    private_apps_legacy.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_apps_legacy.setApiKeyPrefix("Token");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String fileId = "fileId_example"; // String | ID of the desired file.
    List<String> properties = Arrays.asList(); // List<String> | 
    try {
      ModelFile result = apiInstance.getFilesV3FilesFileIdGetById(fileId, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#getFilesV3FilesFileIdGetById");
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
| **fileId** | **String**| ID of the desired file. | |
| **properties** | [**List&lt;String&gt;**](String.md)|  | [optional] |

### Return type

[**ModelFile**](ModelFile.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | An error occurred. |  -  |

<a id="getFilesV3FilesFileIdSignedUrlGetSignedUrl"></a>
# **getFilesV3FilesFileIdSignedUrlGetSignedUrl**
> SignedUrl getFilesV3FilesFileIdSignedUrlGetSignedUrl(fileId, size, expirationSeconds, upscale)

Get signed URL to access private file.

Generates signed URL that allows temporary access to a private file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure OAuth2 access token for authorization: oauth2_legacy
    OAuth oauth2_legacy = (OAuth) defaultClient.getAuthentication("oauth2_legacy");
    oauth2_legacy.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: private_apps_legacy
    ApiKeyAuth private_apps_legacy = (ApiKeyAuth) defaultClient.getAuthentication("private_apps_legacy");
    private_apps_legacy.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_apps_legacy.setApiKeyPrefix("Token");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String fileId = "fileId_example"; // String | ID of file.
    String size = "thumb"; // String | For image files. This will resize the image to the desired size before sharing. Does not affect the original file, just the file served by this signed URL.
    Long expirationSeconds = 56L; // Long | How long in seconds the link will provide access to the file.
    Boolean upscale = true; // Boolean | If size is provided, this will upscale the image to fit the size dimensions.
    try {
      SignedUrl result = apiInstance.getFilesV3FilesFileIdSignedUrlGetSignedUrl(fileId, size, expirationSeconds, upscale);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#getFilesV3FilesFileIdSignedUrlGetSignedUrl");
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
| **fileId** | **String**| ID of file. | |
| **size** | **String**| For image files. This will resize the image to the desired size before sharing. Does not affect the original file, just the file served by this signed URL. | [optional] [enum: thumb, icon, medium, preview] |
| **expirationSeconds** | **Long**| How long in seconds the link will provide access to the file. | [optional] |
| **upscale** | **Boolean**| If size is provided, this will upscale the image to fit the size dimensions. | [optional] |

### Return type

[**SignedUrl**](SignedUrl.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | An error occurred. |  -  |

<a id="getFilesV3FilesImportFromUrlAsyncTasksTaskIdStatusCheckImport"></a>
# **getFilesV3FilesImportFromUrlAsyncTasksTaskIdStatusCheckImport**
> FileActionResponse getFilesV3FilesImportFromUrlAsyncTasksTaskIdStatusCheckImport(taskId)

Check import status.

Check the status of requested import.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure OAuth2 access token for authorization: oauth2_legacy
    OAuth oauth2_legacy = (OAuth) defaultClient.getAuthentication("oauth2_legacy");
    oauth2_legacy.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: private_apps_legacy
    ApiKeyAuth private_apps_legacy = (ApiKeyAuth) defaultClient.getAuthentication("private_apps_legacy");
    private_apps_legacy.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_apps_legacy.setApiKeyPrefix("Token");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String taskId = "taskId_example"; // String | Import by URL task ID
    try {
      FileActionResponse result = apiInstance.getFilesV3FilesImportFromUrlAsyncTasksTaskIdStatusCheckImport(taskId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#getFilesV3FilesImportFromUrlAsyncTasksTaskIdStatusCheckImport");
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
| **taskId** | **String**| Import by URL task ID | |

### Return type

[**FileActionResponse**](FileActionResponse.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | An error occurred. |  -  |

<a id="getFilesV3FilesSearchDoSearch"></a>
# **getFilesV3FilesSearchDoSearch**
> CollectionResponseFile getFilesV3FilesSearchDoSearch(properties, after, before, limit, sort, id, createdAt, createdAtLte, createdAtGte, updatedAt, updatedAtLte, updatedAtGte, name, path, parentFolderId, size, height, width, encoding, type, extension, url, isUsableInContent, allowsAnonymousAccess)

Search files

Search through files in the file manager. Does not display hidden or archived files.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure OAuth2 access token for authorization: oauth2_legacy
    OAuth oauth2_legacy = (OAuth) defaultClient.getAuthentication("oauth2_legacy");
    oauth2_legacy.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: private_apps_legacy
    ApiKeyAuth private_apps_legacy = (ApiKeyAuth) defaultClient.getAuthentication("private_apps_legacy");
    private_apps_legacy.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_apps_legacy.setApiKeyPrefix("Token");

    FilesApi apiInstance = new FilesApi(defaultClient);
    List<String> properties = Arrays.asList(); // List<String> | Desired file properties in the return object.
    String after = "after_example"; // String | The maximum offset of items for a given search is 10000. Narrow your search down if you are reaching this limit.
    String before = "before_example"; // String | 
    Integer limit = 56; // Integer | Number of items to return. Maximum limit is 100.
    List<String> sort = Arrays.asList(); // List<String> | Sort files by a given field.
    String id = "id_example"; // String | Search files by given ID.
    OffsetDateTime createdAt = OffsetDateTime.now(); // OffsetDateTime | Search files by time of creation.
    OffsetDateTime createdAtLte = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtGte = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime updatedAt = OffsetDateTime.now(); // OffsetDateTime | Search files by time of latest updated.
    OffsetDateTime updatedAtLte = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime updatedAtGte = OffsetDateTime.now(); // OffsetDateTime | 
    String name = "name_example"; // String | Search for files containing the given name.
    String path = "path_example"; // String | Search files by path.
    Long parentFolderId = 56L; // Long | Search files within given folderId.
    Long size = 56L; // Long | Query by file size.
    Integer height = 56; // Integer | Search files by height of image or video.
    Integer width = 56; // Integer | Search files by width of image or video.
    String encoding = "encoding_example"; // String | Search files with specified encoding.
    String type = "type_example"; // String | Filter by provided file type.
    String extension = "extension_example"; // String | Search files by given extension.
    String url = "url_example"; // String | Search for given URL
    Boolean isUsableInContent = true; // Boolean | If true shows files that have been marked to be used in new content. It false shows files that should not be used in new content.
    Boolean allowsAnonymousAccess = true; // Boolean | If 'true' will show private files; if 'false' will show public files
    try {
      CollectionResponseFile result = apiInstance.getFilesV3FilesSearchDoSearch(properties, after, before, limit, sort, id, createdAt, createdAtLte, createdAtGte, updatedAt, updatedAtLte, updatedAtGte, name, path, parentFolderId, size, height, width, encoding, type, extension, url, isUsableInContent, allowsAnonymousAccess);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#getFilesV3FilesSearchDoSearch");
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
| **properties** | [**List&lt;String&gt;**](String.md)| Desired file properties in the return object. | [optional] |
| **after** | **String**| The maximum offset of items for a given search is 10000. Narrow your search down if you are reaching this limit. | [optional] |
| **before** | **String**|  | [optional] |
| **limit** | **Integer**| Number of items to return. Maximum limit is 100. | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| Sort files by a given field. | [optional] |
| **id** | **String**| Search files by given ID. | [optional] |
| **createdAt** | **OffsetDateTime**| Search files by time of creation. | [optional] |
| **createdAtLte** | **OffsetDateTime**|  | [optional] |
| **createdAtGte** | **OffsetDateTime**|  | [optional] |
| **updatedAt** | **OffsetDateTime**| Search files by time of latest updated. | [optional] |
| **updatedAtLte** | **OffsetDateTime**|  | [optional] |
| **updatedAtGte** | **OffsetDateTime**|  | [optional] |
| **name** | **String**| Search for files containing the given name. | [optional] |
| **path** | **String**| Search files by path. | [optional] |
| **parentFolderId** | **Long**| Search files within given folderId. | [optional] |
| **size** | **Long**| Query by file size. | [optional] |
| **height** | **Integer**| Search files by height of image or video. | [optional] |
| **width** | **Integer**| Search files by width of image or video. | [optional] |
| **encoding** | **String**| Search files with specified encoding. | [optional] |
| **type** | **String**| Filter by provided file type. | [optional] |
| **extension** | **String**| Search files by given extension. | [optional] |
| **url** | **String**| Search for given URL | [optional] |
| **isUsableInContent** | **Boolean**| If true shows files that have been marked to be used in new content. It false shows files that should not be used in new content. | [optional] |
| **allowsAnonymousAccess** | **Boolean**| If &#39;true&#39; will show private files; if &#39;false&#39; will show public files | [optional] |

### Return type

[**CollectionResponseFile**](CollectionResponseFile.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | An error occurred. |  -  |

<a id="getFilesV3FilesStatPathGetMetadata"></a>
# **getFilesV3FilesStatPathGetMetadata**
> FileStat getFilesV3FilesStatPathGetMetadata(path, properties)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure OAuth2 access token for authorization: oauth2_legacy
    OAuth oauth2_legacy = (OAuth) defaultClient.getAuthentication("oauth2_legacy");
    oauth2_legacy.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: private_apps_legacy
    ApiKeyAuth private_apps_legacy = (ApiKeyAuth) defaultClient.getAuthentication("private_apps_legacy");
    private_apps_legacy.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_apps_legacy.setApiKeyPrefix("Token");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String path = "path_example"; // String | 
    List<String> properties = Arrays.asList(); // List<String> | 
    try {
      FileStat result = apiInstance.getFilesV3FilesStatPathGetMetadata(path, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#getFilesV3FilesStatPathGetMetadata");
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
| **path** | **String**|  | |
| **properties** | [**List&lt;String&gt;**](String.md)|  | [optional] |

### Return type

[**FileStat**](FileStat.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | An error occurred. |  -  |

<a id="patchFilesV3FilesFileIdUpdateProperties"></a>
# **patchFilesV3FilesFileIdUpdateProperties**
> ModelFile patchFilesV3FilesFileIdUpdateProperties(fileId, fileUpdateInput)

update file properties

Update properties of file by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure OAuth2 access token for authorization: oauth2_legacy
    OAuth oauth2_legacy = (OAuth) defaultClient.getAuthentication("oauth2_legacy");
    oauth2_legacy.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: private_apps_legacy
    ApiKeyAuth private_apps_legacy = (ApiKeyAuth) defaultClient.getAuthentication("private_apps_legacy");
    private_apps_legacy.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_apps_legacy.setApiKeyPrefix("Token");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String fileId = "fileId_example"; // String | ID of file to update
    FileUpdateInput fileUpdateInput = new FileUpdateInput(); // FileUpdateInput | Options to update.
    try {
      ModelFile result = apiInstance.patchFilesV3FilesFileIdUpdateProperties(fileId, fileUpdateInput);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#patchFilesV3FilesFileIdUpdateProperties");
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
| **fileId** | **String**| ID of file to update | |
| **fileUpdateInput** | [**FileUpdateInput**](FileUpdateInput.md)| Options to update. | |

### Return type

[**ModelFile**](ModelFile.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | An error occurred. |  -  |

<a id="postFilesV3FilesImportFromUrlAsyncImportFromUrl"></a>
# **postFilesV3FilesImportFromUrlAsyncImportFromUrl**
> ImportFromUrlTaskLocator postFilesV3FilesImportFromUrlAsyncImportFromUrl(importFromUrlInput)

Import a file from a URL into the file manager.

Asynchronously imports the file at the given URL into the file manager.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure OAuth2 access token for authorization: oauth2_legacy
    OAuth oauth2_legacy = (OAuth) defaultClient.getAuthentication("oauth2_legacy");
    oauth2_legacy.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: private_apps_legacy
    ApiKeyAuth private_apps_legacy = (ApiKeyAuth) defaultClient.getAuthentication("private_apps_legacy");
    private_apps_legacy.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_apps_legacy.setApiKeyPrefix("Token");

    FilesApi apiInstance = new FilesApi(defaultClient);
    ImportFromUrlInput importFromUrlInput = new ImportFromUrlInput(); // ImportFromUrlInput | 
    try {
      ImportFromUrlTaskLocator result = apiInstance.postFilesV3FilesImportFromUrlAsyncImportFromUrl(importFromUrlInput);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#postFilesV3FilesImportFromUrlAsyncImportFromUrl");
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
| **importFromUrlInput** | [**ImportFromUrlInput**](ImportFromUrlInput.md)|  | |

### Return type

[**ImportFromUrlTaskLocator**](ImportFromUrlTaskLocator.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | accepted |  -  |
| **0** | An error occurred. |  -  |

<a id="postFilesV3FilesUpload"></a>
# **postFilesV3FilesUpload**
> ModelFile postFilesV3FilesUpload(charsetHunch, _file, fileName, folderId, folderPath, options)

Upload file

Upload a single file with content specified in request body.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure OAuth2 access token for authorization: oauth2_legacy
    OAuth oauth2_legacy = (OAuth) defaultClient.getAuthentication("oauth2_legacy");
    oauth2_legacy.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: private_apps_legacy
    ApiKeyAuth private_apps_legacy = (ApiKeyAuth) defaultClient.getAuthentication("private_apps_legacy");
    private_apps_legacy.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_apps_legacy.setApiKeyPrefix("Token");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String charsetHunch = "charsetHunch_example"; // String | Character set of the uploaded file.
    File _file = new File("/path/to/file"); // File | File to be uploaded.
    String fileName = "fileName_example"; // String | Desired name for the uploaded file.
    String folderId = "folderId_example"; // String | Either 'folderId' or 'folderPath' is required. folderId is the ID of the folder the file will be uploaded to.
    String folderPath = "folderPath_example"; // String | Either 'folderPath' or 'folderId' is required. This field represents the destination folder path for the uploaded file. If a path doesn't exist, the system will try to create one.
    String options = "options_example"; // String | JSON string representing FileUploadOptions.
    try {
      ModelFile result = apiInstance.postFilesV3FilesUpload(charsetHunch, _file, fileName, folderId, folderPath, options);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#postFilesV3FilesUpload");
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
| **charsetHunch** | **String**| Character set of the uploaded file. | [optional] |
| **_file** | **File**| File to be uploaded. | [optional] |
| **fileName** | **String**| Desired name for the uploaded file. | [optional] |
| **folderId** | **String**| Either &#39;folderId&#39; or &#39;folderPath&#39; is required. folderId is the ID of the folder the file will be uploaded to. | [optional] |
| **folderPath** | **String**| Either &#39;folderPath&#39; or &#39;folderId&#39; is required. This field represents the destination folder path for the uploaded file. If a path doesn&#39;t exist, the system will try to create one. | [optional] |
| **options** | **String**| JSON string representing FileUploadOptions. | [optional] |

### Return type

[**ModelFile**](ModelFile.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | successful operation |  -  |
| **0** | An error occurred. |  -  |

<a id="putFilesV3FilesFileIdReplace"></a>
# **putFilesV3FilesFileIdReplace**
> ModelFile putFilesV3FilesFileIdReplace(fileId, charsetHunch, _file, options)

Replace file.

Replace existing file data with new file data. Can be used to change image content without having to upload a new file and update all references.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure OAuth2 access token for authorization: oauth2_legacy
    OAuth oauth2_legacy = (OAuth) defaultClient.getAuthentication("oauth2_legacy");
    oauth2_legacy.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: private_apps_legacy
    ApiKeyAuth private_apps_legacy = (ApiKeyAuth) defaultClient.getAuthentication("private_apps_legacy");
    private_apps_legacy.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_apps_legacy.setApiKeyPrefix("Token");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String fileId = "fileId_example"; // String | ID of the desired file.
    String charsetHunch = "charsetHunch_example"; // String | Character set of given file data.
    File _file = new File("/path/to/file"); // File | File data that will replace existing file in the file manager.
    String options = "options_example"; // String | JSON String representing FileReplaceOptions
    try {
      ModelFile result = apiInstance.putFilesV3FilesFileIdReplace(fileId, charsetHunch, _file, options);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#putFilesV3FilesFileIdReplace");
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
| **fileId** | **String**| ID of the desired file. | |
| **charsetHunch** | **String**| Character set of given file data. | [optional] |
| **_file** | **File**| File data that will replace existing file in the file manager. | [optional] |
| **options** | **String**| JSON String representing FileReplaceOptions | [optional] |

### Return type

[**ModelFile**](ModelFile.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | An error occurred. |  -  |

