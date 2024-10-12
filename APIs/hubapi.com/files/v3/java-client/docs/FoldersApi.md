# FoldersApi

All URIs are relative to *https://api.hubapi.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteFilesV3FoldersFolderIdArchive**](FoldersApi.md#deleteFilesV3FoldersFolderIdArchive) | **DELETE** /files/v3/folders/{folderId} | Delete folder. |
| [**deleteFilesV3FoldersFolderPathArchiveByPath**](FoldersApi.md#deleteFilesV3FoldersFolderPathArchiveByPath) | **DELETE** /files/v3/folders/{folderPath} | Delete folder. |
| [**getFilesV3FoldersFolderIdGetById**](FoldersApi.md#getFilesV3FoldersFolderIdGetById) | **GET** /files/v3/folders/{folderId} | Get folder |
| [**getFilesV3FoldersFolderPathGetByPath**](FoldersApi.md#getFilesV3FoldersFolderPathGetByPath) | **GET** /files/v3/folders/{folderPath} | Get folder. |
| [**getFilesV3FoldersSearchDoSearch**](FoldersApi.md#getFilesV3FoldersSearchDoSearch) | **GET** /files/v3/folders/search | Search folders |
| [**getFilesV3FoldersUpdateAsyncTasksTaskIdStatusCheckUpdateStatus**](FoldersApi.md#getFilesV3FoldersUpdateAsyncTasksTaskIdStatusCheckUpdateStatus) | **GET** /files/v3/folders/update/async/tasks/{taskId}/status | Check folder update status. |
| [**postFilesV3FoldersCreate**](FoldersApi.md#postFilesV3FoldersCreate) | **POST** /files/v3/folders | Create folder. |
| [**postFilesV3FoldersUpdateAsyncUpdateProperties**](FoldersApi.md#postFilesV3FoldersUpdateAsyncUpdateProperties) | **POST** /files/v3/folders/update/async | Update folder properties |


<a id="deleteFilesV3FoldersFolderIdArchive"></a>
# **deleteFilesV3FoldersFolderIdArchive**
> deleteFilesV3FoldersFolderIdArchive(folderId)

Delete folder.

Delete folder by ID.

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
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure OAuth2 access token for authorization: oauth2_legacy
    OAuth oauth2_legacy = (OAuth) defaultClient.getAuthentication("oauth2_legacy");
    oauth2_legacy.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: private_apps_legacy
    ApiKeyAuth private_apps_legacy = (ApiKeyAuth) defaultClient.getAuthentication("private_apps_legacy");
    private_apps_legacy.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_apps_legacy.setApiKeyPrefix("Token");

    FoldersApi apiInstance = new FoldersApi(defaultClient);
    String folderId = "folderId_example"; // String | ID of folder to delete.
    try {
      apiInstance.deleteFilesV3FoldersFolderIdArchive(folderId);
    } catch (ApiException e) {
      System.err.println("Exception when calling FoldersApi#deleteFilesV3FoldersFolderIdArchive");
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
| **folderId** | **String**| ID of folder to delete. | |

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

<a id="deleteFilesV3FoldersFolderPathArchiveByPath"></a>
# **deleteFilesV3FoldersFolderPathArchiveByPath**
> deleteFilesV3FoldersFolderPathArchiveByPath(folderPath)

Delete folder.

Delete folder by path.

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
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure OAuth2 access token for authorization: oauth2_legacy
    OAuth oauth2_legacy = (OAuth) defaultClient.getAuthentication("oauth2_legacy");
    oauth2_legacy.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: private_apps_legacy
    ApiKeyAuth private_apps_legacy = (ApiKeyAuth) defaultClient.getAuthentication("private_apps_legacy");
    private_apps_legacy.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_apps_legacy.setApiKeyPrefix("Token");

    FoldersApi apiInstance = new FoldersApi(defaultClient);
    String folderPath = "folderPath_example"; // String | Path of folder to delete
    try {
      apiInstance.deleteFilesV3FoldersFolderPathArchiveByPath(folderPath);
    } catch (ApiException e) {
      System.err.println("Exception when calling FoldersApi#deleteFilesV3FoldersFolderPathArchiveByPath");
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
| **folderPath** | **String**| Path of folder to delete | |

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

<a id="getFilesV3FoldersFolderIdGetById"></a>
# **getFilesV3FoldersFolderIdGetById**
> Folder getFilesV3FoldersFolderIdGetById(folderId, properties)

Get folder

Get folder by ID

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
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure OAuth2 access token for authorization: oauth2_legacy
    OAuth oauth2_legacy = (OAuth) defaultClient.getAuthentication("oauth2_legacy");
    oauth2_legacy.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: private_apps_legacy
    ApiKeyAuth private_apps_legacy = (ApiKeyAuth) defaultClient.getAuthentication("private_apps_legacy");
    private_apps_legacy.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_apps_legacy.setApiKeyPrefix("Token");

    FoldersApi apiInstance = new FoldersApi(defaultClient);
    String folderId = "folderId_example"; // String | ID of desired folder
    List<String> properties = Arrays.asList(); // List<String> | Properties to set on returned folder.
    try {
      Folder result = apiInstance.getFilesV3FoldersFolderIdGetById(folderId, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FoldersApi#getFilesV3FoldersFolderIdGetById");
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
| **folderId** | **String**| ID of desired folder | |
| **properties** | [**List&lt;String&gt;**](String.md)| Properties to set on returned folder. | [optional] |

### Return type

[**Folder**](Folder.md)

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

<a id="getFilesV3FoldersFolderPathGetByPath"></a>
# **getFilesV3FoldersFolderPathGetByPath**
> Folder getFilesV3FoldersFolderPathGetByPath(folderPath, properties)

Get folder.

Get folder by path.

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
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure OAuth2 access token for authorization: oauth2_legacy
    OAuth oauth2_legacy = (OAuth) defaultClient.getAuthentication("oauth2_legacy");
    oauth2_legacy.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: private_apps_legacy
    ApiKeyAuth private_apps_legacy = (ApiKeyAuth) defaultClient.getAuthentication("private_apps_legacy");
    private_apps_legacy.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_apps_legacy.setApiKeyPrefix("Token");

    FoldersApi apiInstance = new FoldersApi(defaultClient);
    String folderPath = "folderPath_example"; // String | Path of desired folder.
    List<String> properties = Arrays.asList(); // List<String> | Properties to set on returned folder.
    try {
      Folder result = apiInstance.getFilesV3FoldersFolderPathGetByPath(folderPath, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FoldersApi#getFilesV3FoldersFolderPathGetByPath");
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
| **folderPath** | **String**| Path of desired folder. | |
| **properties** | [**List&lt;String&gt;**](String.md)| Properties to set on returned folder. | [optional] |

### Return type

[**Folder**](Folder.md)

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

<a id="getFilesV3FoldersSearchDoSearch"></a>
# **getFilesV3FoldersSearchDoSearch**
> CollectionResponseFolder getFilesV3FoldersSearchDoSearch(properties, after, before, limit, sort, id, createdAt, createdAtLte, createdAtGte, updatedAt, updatedAtLte, updatedAtGte, name, path, parentFolderId)

Search folders

Search for folders. Does not contain hidden or archived folders.

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
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure OAuth2 access token for authorization: oauth2_legacy
    OAuth oauth2_legacy = (OAuth) defaultClient.getAuthentication("oauth2_legacy");
    oauth2_legacy.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: private_apps_legacy
    ApiKeyAuth private_apps_legacy = (ApiKeyAuth) defaultClient.getAuthentication("private_apps_legacy");
    private_apps_legacy.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_apps_legacy.setApiKeyPrefix("Token");

    FoldersApi apiInstance = new FoldersApi(defaultClient);
    List<String> properties = Arrays.asList(); // List<String> | Properties that should be included in the returned folders.
    String after = "after_example"; // String | The maximum offset of items for a given search is 10000. Narrow your search down if you are reaching this limit.
    String before = "before_example"; // String | 
    Integer limit = 56; // Integer | Limit of results to return. Max limit is 100.
    List<String> sort = Arrays.asList(); // List<String> | Sort results by given property. For example -name sorts by name field descending, name sorts by name field ascending.
    String id = "id_example"; // String | Search folder by given ID.
    OffsetDateTime createdAt = OffsetDateTime.now(); // OffsetDateTime | Search for folders with the given creation timestamp.
    OffsetDateTime createdAtLte = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtGte = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime updatedAt = OffsetDateTime.now(); // OffsetDateTime | Search for folder at given update timestamp.
    OffsetDateTime updatedAtLte = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime updatedAtGte = OffsetDateTime.now(); // OffsetDateTime | 
    String name = "name_example"; // String | Search for folders containing the specified name.
    String path = "path_example"; // String | Search for folders by path.
    Long parentFolderId = 56L; // Long | Search for folders with the given parent folderId.
    try {
      CollectionResponseFolder result = apiInstance.getFilesV3FoldersSearchDoSearch(properties, after, before, limit, sort, id, createdAt, createdAtLte, createdAtGte, updatedAt, updatedAtLte, updatedAtGte, name, path, parentFolderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FoldersApi#getFilesV3FoldersSearchDoSearch");
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
| **properties** | [**List&lt;String&gt;**](String.md)| Properties that should be included in the returned folders. | [optional] |
| **after** | **String**| The maximum offset of items for a given search is 10000. Narrow your search down if you are reaching this limit. | [optional] |
| **before** | **String**|  | [optional] |
| **limit** | **Integer**| Limit of results to return. Max limit is 100. | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| Sort results by given property. For example -name sorts by name field descending, name sorts by name field ascending. | [optional] |
| **id** | **String**| Search folder by given ID. | [optional] |
| **createdAt** | **OffsetDateTime**| Search for folders with the given creation timestamp. | [optional] |
| **createdAtLte** | **OffsetDateTime**|  | [optional] |
| **createdAtGte** | **OffsetDateTime**|  | [optional] |
| **updatedAt** | **OffsetDateTime**| Search for folder at given update timestamp. | [optional] |
| **updatedAtLte** | **OffsetDateTime**|  | [optional] |
| **updatedAtGte** | **OffsetDateTime**|  | [optional] |
| **name** | **String**| Search for folders containing the specified name. | [optional] |
| **path** | **String**| Search for folders by path. | [optional] |
| **parentFolderId** | **Long**| Search for folders with the given parent folderId. | [optional] |

### Return type

[**CollectionResponseFolder**](CollectionResponseFolder.md)

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

<a id="getFilesV3FoldersUpdateAsyncTasksTaskIdStatusCheckUpdateStatus"></a>
# **getFilesV3FoldersUpdateAsyncTasksTaskIdStatusCheckUpdateStatus**
> FolderActionResponse getFilesV3FoldersUpdateAsyncTasksTaskIdStatusCheckUpdateStatus(taskId)

Check folder update status.

Check status of folder update. Folder updates happen asynchronously.

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
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure OAuth2 access token for authorization: oauth2_legacy
    OAuth oauth2_legacy = (OAuth) defaultClient.getAuthentication("oauth2_legacy");
    oauth2_legacy.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: private_apps_legacy
    ApiKeyAuth private_apps_legacy = (ApiKeyAuth) defaultClient.getAuthentication("private_apps_legacy");
    private_apps_legacy.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_apps_legacy.setApiKeyPrefix("Token");

    FoldersApi apiInstance = new FoldersApi(defaultClient);
    String taskId = "taskId_example"; // String | TaskId of folder update
    try {
      FolderActionResponse result = apiInstance.getFilesV3FoldersUpdateAsyncTasksTaskIdStatusCheckUpdateStatus(taskId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FoldersApi#getFilesV3FoldersUpdateAsyncTasksTaskIdStatusCheckUpdateStatus");
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
| **taskId** | **String**| TaskId of folder update | |

### Return type

[**FolderActionResponse**](FolderActionResponse.md)

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

<a id="postFilesV3FoldersCreate"></a>
# **postFilesV3FoldersCreate**
> Folder postFilesV3FoldersCreate(folderInput)

Create folder.

Creates a folder.

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
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure OAuth2 access token for authorization: oauth2_legacy
    OAuth oauth2_legacy = (OAuth) defaultClient.getAuthentication("oauth2_legacy");
    oauth2_legacy.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: private_apps_legacy
    ApiKeyAuth private_apps_legacy = (ApiKeyAuth) defaultClient.getAuthentication("private_apps_legacy");
    private_apps_legacy.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_apps_legacy.setApiKeyPrefix("Token");

    FoldersApi apiInstance = new FoldersApi(defaultClient);
    FolderInput folderInput = new FolderInput(); // FolderInput | Folder creation options
    try {
      Folder result = apiInstance.postFilesV3FoldersCreate(folderInput);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FoldersApi#postFilesV3FoldersCreate");
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
| **folderInput** | [**FolderInput**](FolderInput.md)| Folder creation options | |

### Return type

[**Folder**](Folder.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | successful operation |  -  |
| **0** | An error occurred. |  -  |

<a id="postFilesV3FoldersUpdateAsyncUpdateProperties"></a>
# **postFilesV3FoldersUpdateAsyncUpdateProperties**
> FolderUpdateTaskLocator postFilesV3FoldersUpdateAsyncUpdateProperties(folderUpdateInput)

Update folder properties

Update properties of folder by given ID. This action happens asynchronously and will update all of the folder&#39;s children as well.

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
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure OAuth2 access token for authorization: oauth2_legacy
    OAuth oauth2_legacy = (OAuth) defaultClient.getAuthentication("oauth2_legacy");
    oauth2_legacy.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: private_apps_legacy
    ApiKeyAuth private_apps_legacy = (ApiKeyAuth) defaultClient.getAuthentication("private_apps_legacy");
    private_apps_legacy.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_apps_legacy.setApiKeyPrefix("Token");

    FoldersApi apiInstance = new FoldersApi(defaultClient);
    FolderUpdateInput folderUpdateInput = new FolderUpdateInput(); // FolderUpdateInput | Properties to change in the folder
    try {
      FolderUpdateTaskLocator result = apiInstance.postFilesV3FoldersUpdateAsyncUpdateProperties(folderUpdateInput);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FoldersApi#postFilesV3FoldersUpdateAsyncUpdateProperties");
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
| **folderUpdateInput** | [**FolderUpdateInput**](FolderUpdateInput.md)| Properties to change in the folder | |

### Return type

[**FolderUpdateTaskLocator**](FolderUpdateTaskLocator.md)

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

