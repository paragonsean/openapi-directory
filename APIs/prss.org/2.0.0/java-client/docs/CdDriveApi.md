# CdDriveApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV2CddriveFilesContentPost**](CdDriveApi.md#apiV2CddriveFilesContentPost) | **POST** /api/v2/cddrive/files/content | Upload a file. |
| [**apiV2CddriveFilesFileIdContentGet**](CdDriveApi.md#apiV2CddriveFilesFileIdContentGet) | **GET** /api/v2/cddrive/files/{file-id}/content | UNDER DEVELOPMENT - Download a file. |
| [**apiV2CddriveFilesFileIdDelete**](CdDriveApi.md#apiV2CddriveFilesFileIdDelete) | **DELETE** /api/v2/cddrive/files/{file-id} | Delete a file. |
| [**apiV2CddriveFilesFileIdGet**](CdDriveApi.md#apiV2CddriveFilesFileIdGet) | **GET** /api/v2/cddrive/files/{file-id} | Get file information. |
| [**apiV2CddriveFoldersFolderIdDelete**](CdDriveApi.md#apiV2CddriveFoldersFolderIdDelete) | **DELETE** /api/v2/cddrive/folders/{folder-id} | UNDER DEVELOPMENT - Delete a folder. |
| [**apiV2CddriveFoldersFolderIdGet**](CdDriveApi.md#apiV2CddriveFoldersFolderIdGet) | **GET** /api/v2/cddrive/folders/{folder-id} | UNDER DEVELOPMENT - Get folder information. |
| [**apiV2CddriveFoldersFolderIdItemsGet**](CdDriveApi.md#apiV2CddriveFoldersFolderIdItemsGet) | **GET** /api/v2/cddrive/folders/{folder-id}/items | Get the items in the folder. |
| [**apiV2CddriveFoldersPost**](CdDriveApi.md#apiV2CddriveFoldersPost) | **POST** /api/v2/cddrive/folders | Create a folder. |


<a id="apiV2CddriveFilesContentPost"></a>
# **apiV2CddriveFilesContentPost**
> CDDriveFile apiV2CddriveFilesContentPost(contentMD5, _file, name, parentId)

Upload a file.

Upload a file to the customer&#39;s private CD Drive.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CdDriveApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: cd_oauth2
    OAuth cd_oauth2 = (OAuth) defaultClient.getAuthentication("cd_oauth2");
    cd_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CdDriveApi apiInstance = new CdDriveApi(defaultClient);
    String contentMD5 = "contentMD5_example"; // String | If present, the MD5 will be compared against the file received as a message integrity check.
    File _file = new File("/path/to/file"); // File | The file content being uploaded.
    String name = "name_example"; // String | The name of the file, including extension.
    Long parentId = 56L; // Long | The ID of the parent folder or 0 for the root folder.
    try {
      CDDriveFile result = apiInstance.apiV2CddriveFilesContentPost(contentMD5, _file, name, parentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CdDriveApi#apiV2CddriveFilesContentPost");
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
| **contentMD5** | **String**| If present, the MD5 will be compared against the file received as a message integrity check. | [optional] |
| **_file** | **File**| The file content being uploaded. | [optional] |
| **name** | **String**| The name of the file, including extension. | [optional] |
| **parentId** | **Long**| The ID of the parent folder or 0 for the root folder. | [optional] |

### Return type

[**CDDriveFile**](CDDriveFile.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The file was created successfully. The response contains the file metadata. |  -  |
| **400** | The provided Content-MD5 header doesn&#39;t match the provided content |  -  |
| **403** | Authorization failed, Username or password not found or incorrect. |  -  |
| **404** | A parent id cannot be found. |  -  |
| **409** | A name conflict because the file already exists. |  -  |
| **413** | File is bigger than maximum size of 500 MB. |  -  |

<a id="apiV2CddriveFilesFileIdContentGet"></a>
# **apiV2CddriveFilesFileIdContentGet**
> File apiV2CddriveFilesFileIdContentGet(fileId, range)

UNDER DEVELOPMENT - Download a file.

Download a file from the customer&#39;s private CD Drive.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CdDriveApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: cd_oauth2
    OAuth cd_oauth2 = (OAuth) defaultClient.getAuthentication("cd_oauth2");
    cd_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CdDriveApi apiInstance = new CdDriveApi(defaultClient);
    Long fileId = 56L; // Long | The ID of the file to download.
    String range = "range_example"; // String | Can be used to limit the range of bytes retrieved. Only a single byte range in the format ```bytes={start-range}-{end-range}``` is supported.
    try {
      File result = apiInstance.apiV2CddriveFilesFileIdContentGet(fileId, range);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CdDriveApi#apiV2CddriveFilesFileIdContentGet");
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
| **fileId** | **Long**| The ID of the file to download. | |
| **range** | **String**| Can be used to limit the range of bytes retrieved. Only a single byte range in the format &#x60;&#x60;&#x60;bytes&#x3D;{start-range}-{end-range}&#x60;&#x60;&#x60; is supported. | [optional] |

### Return type

[**File**](File.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The file was found and will be returned in the body of the response. |  -  |
| **302** | The file was found but should be downloaded at the URL presented in the Location header. This return code may be used when the file is available via a CDN or other optimized path. |  * Location - The location the file can be downloaded from <br>  |
| **404** | The file cannot be found. |  -  |

<a id="apiV2CddriveFilesFileIdDelete"></a>
# **apiV2CddriveFilesFileIdDelete**
> apiV2CddriveFilesFileIdDelete(fileId)

Delete a file.

Delete a file from the customer&#39;s private CD Drive.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CdDriveApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: cd_oauth2
    OAuth cd_oauth2 = (OAuth) defaultClient.getAuthentication("cd_oauth2");
    cd_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CdDriveApi apiInstance = new CdDriveApi(defaultClient);
    Long fileId = 56L; // Long | The ID of the file to access.
    try {
      apiInstance.apiV2CddriveFilesFileIdDelete(fileId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CdDriveApi#apiV2CddriveFilesFileIdDelete");
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
| **fileId** | **Long**| The ID of the file to access. | |

### Return type

null (empty response body)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The file was successfully deleted. |  -  |
| **404** | The file cannot be found. |  -  |

<a id="apiV2CddriveFilesFileIdGet"></a>
# **apiV2CddriveFilesFileIdGet**
> CDDriveFile apiV2CddriveFilesFileIdGet(fileId)

Get file information.

Get the information about a file in the customer&#39;s private CD Drive.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CdDriveApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: cd_oauth2
    OAuth cd_oauth2 = (OAuth) defaultClient.getAuthentication("cd_oauth2");
    cd_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CdDriveApi apiInstance = new CdDriveApi(defaultClient);
    Long fileId = 56L; // Long | The ID of the file to access.
    try {
      CDDriveFile result = apiInstance.apiV2CddriveFilesFileIdGet(fileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CdDriveApi#apiV2CddriveFilesFileIdGet");
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
| **fileId** | **Long**| The ID of the file to access. | |

### Return type

[**CDDriveFile**](CDDriveFile.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The file information. |  -  |
| **404** | The file cannot be found. |  -  |

<a id="apiV2CddriveFoldersFolderIdDelete"></a>
# **apiV2CddriveFoldersFolderIdDelete**
> apiV2CddriveFoldersFolderIdDelete(folderId, recursive)

UNDER DEVELOPMENT - Delete a folder.

Delete a file from the customer&#39;s private CD Drive.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CdDriveApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: cd_oauth2
    OAuth cd_oauth2 = (OAuth) defaultClient.getAuthentication("cd_oauth2");
    cd_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CdDriveApi apiInstance = new CdDriveApi(defaultClient);
    Long folderId = 56L; // Long | The ID of the folder to get.
    Boolean recursive = true; // Boolean | Flag to indicate if the folder should be deleted if it has items inside of it.
    try {
      apiInstance.apiV2CddriveFoldersFolderIdDelete(folderId, recursive);
    } catch (ApiException e) {
      System.err.println("Exception when calling CdDriveApi#apiV2CddriveFoldersFolderIdDelete");
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
| **folderId** | **Long**| The ID of the folder to get. | |
| **recursive** | **Boolean**| Flag to indicate if the folder should be deleted if it has items inside of it. | [optional] [default to true] |

### Return type

null (empty response body)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The file was successfully deleted. |  -  |
| **404** | The file cannot be found. |  -  |

<a id="apiV2CddriveFoldersFolderIdGet"></a>
# **apiV2CddriveFoldersFolderIdGet**
> CDDriveFolder apiV2CddriveFoldersFolderIdGet(folderId)

UNDER DEVELOPMENT - Get folder information.

Get the information about a folder in the customer&#39;s private CD Drive.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CdDriveApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: cd_oauth2
    OAuth cd_oauth2 = (OAuth) defaultClient.getAuthentication("cd_oauth2");
    cd_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CdDriveApi apiInstance = new CdDriveApi(defaultClient);
    Long folderId = 56L; // Long | The ID of the folder to get.
    try {
      CDDriveFolder result = apiInstance.apiV2CddriveFoldersFolderIdGet(folderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CdDriveApi#apiV2CddriveFoldersFolderIdGet");
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
| **folderId** | **Long**| The ID of the folder to get. | |

### Return type

[**CDDriveFolder**](CDDriveFolder.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The folder information. |  -  |
| **404** | The folder cannot be found. |  -  |

<a id="apiV2CddriveFoldersFolderIdItemsGet"></a>
# **apiV2CddriveFoldersFolderIdItemsGet**
> ApiV2CddriveFoldersFolderIdItemsGet200Response apiV2CddriveFoldersFolderIdItemsGet(folderId, offset, limit)

Get the items in the folder.

Get the information about a folder in the customer&#39;s private CD Drive.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CdDriveApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: cd_oauth2
    OAuth cd_oauth2 = (OAuth) defaultClient.getAuthentication("cd_oauth2");
    cd_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CdDriveApi apiInstance = new CdDriveApi(defaultClient);
    Long folderId = 56L; // Long | The ID of the folder to get. Folder ID 0 represents the uppermost CD drive folder.
    Integer offset = 0; // Integer | The offset into the items to begin the response.
    Integer limit = 20; // Integer | The maximum number of items to return in the response.
    try {
      ApiV2CddriveFoldersFolderIdItemsGet200Response result = apiInstance.apiV2CddriveFoldersFolderIdItemsGet(folderId, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CdDriveApi#apiV2CddriveFoldersFolderIdItemsGet");
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
| **folderId** | **Long**| The ID of the folder to get. Folder ID 0 represents the uppermost CD drive folder. | |
| **offset** | **Integer**| The offset into the items to begin the response. | [optional] [default to 0] |
| **limit** | **Integer**| The maximum number of items to return in the response. | [optional] [default to 20] |

### Return type

[**ApiV2CddriveFoldersFolderIdItemsGet200Response**](ApiV2CddriveFoldersFolderIdItemsGet200Response.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The folder information. |  -  |
| **404** | The folder cannot be found. |  -  |

<a id="apiV2CddriveFoldersPost"></a>
# **apiV2CddriveFoldersPost**
> CDDriveFolder apiV2CddriveFoldersPost(name, parentId)

Create a folder.

Create a new folder in the customer&#39;s private CD Drive.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CdDriveApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: cd_oauth2
    OAuth cd_oauth2 = (OAuth) defaultClient.getAuthentication("cd_oauth2");
    cd_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CdDriveApi apiInstance = new CdDriveApi(defaultClient);
    String name = "name_example"; // String | the name of the folder
    Long parentId = 56L; // Long | The ID of the parent folder or 0 for the root folder.
    try {
      CDDriveFolder result = apiInstance.apiV2CddriveFoldersPost(name, parentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CdDriveApi#apiV2CddriveFoldersPost");
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
| **name** | **String**| the name of the folder | [optional] |
| **parentId** | **Long**| The ID of the parent folder or 0 for the root folder. | [optional] |

### Return type

[**CDDriveFolder**](CDDriveFolder.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The folder information. |  -  |
| **403** | Authorization failed, username or password not found or incorrect. |  -  |
| **404** | A parent id cannot be found. |  -  |
| **409** | The folder already exists. |  -  |

