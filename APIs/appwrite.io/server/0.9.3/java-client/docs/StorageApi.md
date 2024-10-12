# StorageApi

All URIs are relative to *https://appwrite.io/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**storageCreateFile**](StorageApi.md#storageCreateFile) | **POST** /storage/files | Create File |
| [**storageDeleteFile**](StorageApi.md#storageDeleteFile) | **DELETE** /storage/files/{fileId} | Delete File |
| [**storageGetFile**](StorageApi.md#storageGetFile) | **GET** /storage/files/{fileId} | Get File |
| [**storageGetFileDownload**](StorageApi.md#storageGetFileDownload) | **GET** /storage/files/{fileId}/download | Get File for Download |
| [**storageGetFilePreview**](StorageApi.md#storageGetFilePreview) | **GET** /storage/files/{fileId}/preview | Get File Preview |
| [**storageGetFileView**](StorageApi.md#storageGetFileView) | **GET** /storage/files/{fileId}/view | Get File for View |
| [**storageListFiles**](StorageApi.md#storageListFiles) | **GET** /storage/files | List Files |
| [**storageUpdateFile**](StorageApi.md#storageUpdateFile) | **PUT** /storage/files/{fileId} | Update File |


<a id="storageCreateFile"></a>
# **storageCreateFile**
> File storageCreateFile(_file, read, write)

Create File

Create a new file. The user who creates the file will automatically be assigned to read and write access unless he has passed custom values for read and write arguments.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

    StorageApi apiInstance = new StorageApi(defaultClient);
    String _file = "_file_example"; // String | Binary file.
    List<String> read = Arrays.asList(); // List<String> | An array of strings with read permissions. By default only the current user is granted with read permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.
    List<String> write = Arrays.asList(); // List<String> | An array of strings with write permissions. By default only the current user is granted with write permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.
    try {
      File result = apiInstance.storageCreateFile(_file, read, write);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageApi#storageCreateFile");
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
| **_file** | **String**| Binary file. | |
| **read** | [**List&lt;String&gt;**](String.md)| An array of strings with read permissions. By default only the current user is granted with read permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions. | [optional] |
| **write** | [**List&lt;String&gt;**](String.md)| An array of strings with write permissions. By default only the current user is granted with write permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions. | [optional] |

### Return type

[**File**](File.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | File |  -  |

<a id="storageDeleteFile"></a>
# **storageDeleteFile**
> storageDeleteFile(fileId)

Delete File

Delete a file by its unique ID. Only users with write permissions have access to delete this resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

    StorageApi apiInstance = new StorageApi(defaultClient);
    String fileId = "fileId_example"; // String | File unique ID.
    try {
      apiInstance.storageDeleteFile(fileId);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageApi#storageDeleteFile");
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
| **fileId** | **String**| File unique ID. | |

### Return type

null (empty response body)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No content |  -  |

<a id="storageGetFile"></a>
# **storageGetFile**
> File storageGetFile(fileId)

Get File

Get a file by its unique ID. This endpoint response returns a JSON object with the file metadata.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

    StorageApi apiInstance = new StorageApi(defaultClient);
    String fileId = "fileId_example"; // String | File unique ID.
    try {
      File result = apiInstance.storageGetFile(fileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageApi#storageGetFile");
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
| **fileId** | **String**| File unique ID. | |

### Return type

[**File**](File.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | File |  -  |

<a id="storageGetFileDownload"></a>
# **storageGetFileDownload**
> storageGetFileDownload(fileId)

Get File for Download

Get a file content by its unique ID. The endpoint response return with a &#39;Content-Disposition: attachment&#39; header that tells the browser to start downloading the file to user downloads directory.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

    StorageApi apiInstance = new StorageApi(defaultClient);
    String fileId = "fileId_example"; // String | File unique ID.
    try {
      apiInstance.storageGetFileDownload(fileId);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageApi#storageGetFileDownload");
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
| **fileId** | **String**| File unique ID. | |

### Return type

null (empty response body)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | File |  -  |

<a id="storageGetFilePreview"></a>
# **storageGetFilePreview**
> storageGetFilePreview(fileId, width, height, gravity, quality, borderWidth, borderColor, borderRadius, opacity, rotation, background, output)

Get File Preview

Get a file preview image. Currently, this method supports preview for image files (jpg, png, and gif), other supported formats, like pdf, docs, slides, and spreadsheets, will return the file icon image. You can also pass query string arguments for cutting and resizing your preview image.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

    StorageApi apiInstance = new StorageApi(defaultClient);
    String fileId = "fileId_example"; // String | File unique ID
    Integer width = 0; // Integer | Resize preview image width, Pass an integer between 0 to 4000.
    Integer height = 0; // Integer | Resize preview image height, Pass an integer between 0 to 4000.
    String gravity = "center"; // String | Image crop gravity. Can be one of center,top-left,top,top-right,left,right,bottom-left,bottom,bottom-right
    Integer quality = 100; // Integer | Preview image quality. Pass an integer between 0 to 100. Defaults to 100.
    Integer borderWidth = 0; // Integer | Preview image border in pixels. Pass an integer between 0 to 100. Defaults to 0.
    String borderColor = ""; // String | Preview image border color. Use a valid HEX color, no # is needed for prefix.
    Integer borderRadius = 0; // Integer | Preview image border radius in pixels. Pass an integer between 0 to 4000.
    Float opacity = 1F; // Float | Preview image opacity. Only works with images having an alpha channel (like png). Pass a number between 0 to 1.
    Integer rotation = 0; // Integer | Preview image rotation in degrees. Pass an integer between 0 and 360.
    String background = ""; // String | Preview image background color. Only works with transparent images (png). Use a valid HEX color, no # is needed for prefix.
    String output = ""; // String | Output format type (jpeg, jpg, png, gif and webp).
    try {
      apiInstance.storageGetFilePreview(fileId, width, height, gravity, quality, borderWidth, borderColor, borderRadius, opacity, rotation, background, output);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageApi#storageGetFilePreview");
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
| **fileId** | **String**| File unique ID | |
| **width** | **Integer**| Resize preview image width, Pass an integer between 0 to 4000. | [optional] [default to 0] |
| **height** | **Integer**| Resize preview image height, Pass an integer between 0 to 4000. | [optional] [default to 0] |
| **gravity** | **String**| Image crop gravity. Can be one of center,top-left,top,top-right,left,right,bottom-left,bottom,bottom-right | [optional] [default to center] |
| **quality** | **Integer**| Preview image quality. Pass an integer between 0 to 100. Defaults to 100. | [optional] [default to 100] |
| **borderWidth** | **Integer**| Preview image border in pixels. Pass an integer between 0 to 100. Defaults to 0. | [optional] [default to 0] |
| **borderColor** | **String**| Preview image border color. Use a valid HEX color, no # is needed for prefix. | [optional] [default to ] |
| **borderRadius** | **Integer**| Preview image border radius in pixels. Pass an integer between 0 to 4000. | [optional] [default to 0] |
| **opacity** | **Float**| Preview image opacity. Only works with images having an alpha channel (like png). Pass a number between 0 to 1. | [optional] [default to 1] |
| **rotation** | **Integer**| Preview image rotation in degrees. Pass an integer between 0 and 360. | [optional] [default to 0] |
| **background** | **String**| Preview image background color. Only works with transparent images (png). Use a valid HEX color, no # is needed for prefix. | [optional] [default to ] |
| **output** | **String**| Output format type (jpeg, jpg, png, gif and webp). | [optional] [default to ] |

### Return type

null (empty response body)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Image |  -  |

<a id="storageGetFileView"></a>
# **storageGetFileView**
> storageGetFileView(fileId)

Get File for View

Get a file content by its unique ID. This endpoint is similar to the download method but returns with no  &#39;Content-Disposition: attachment&#39; header.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

    StorageApi apiInstance = new StorageApi(defaultClient);
    String fileId = "fileId_example"; // String | File unique ID.
    try {
      apiInstance.storageGetFileView(fileId);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageApi#storageGetFileView");
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
| **fileId** | **String**| File unique ID. | |

### Return type

null (empty response body)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | File |  -  |

<a id="storageListFiles"></a>
# **storageListFiles**
> FileList storageListFiles(search, limit, offset, orderType)

List Files

Get a list of all the user files. You can use the query params to filter your results. On admin mode, this endpoint will return a list of all of the project&#39;s files. [Learn more about different API modes](/docs/admin).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

    StorageApi apiInstance = new StorageApi(defaultClient);
    String search = ""; // String | Search term to filter your list results. Max length: 256 chars.
    Integer limit = 25; // Integer | Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.
    Integer offset = 0; // Integer | Results offset. The default value is 0. Use this param to manage pagination.
    String orderType = "ASC"; // String | Order result by ASC or DESC order.
    try {
      FileList result = apiInstance.storageListFiles(search, limit, offset, orderType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageApi#storageListFiles");
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
| **search** | **String**| Search term to filter your list results. Max length: 256 chars. | [optional] [default to ] |
| **limit** | **Integer**| Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request. | [optional] [default to 25] |
| **offset** | **Integer**| Results offset. The default value is 0. Use this param to manage pagination. | [optional] [default to 0] |
| **orderType** | **String**| Order result by ASC or DESC order. | [optional] [default to ASC] |

### Return type

[**FileList**](FileList.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Files List |  -  |

<a id="storageUpdateFile"></a>
# **storageUpdateFile**
> File storageUpdateFile(fileId, storageUpdateFileRequest)

Update File

Update a file by its unique ID. Only users with write permissions have access to update this resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

    StorageApi apiInstance = new StorageApi(defaultClient);
    String fileId = "fileId_example"; // String | File unique ID.
    StorageUpdateFileRequest storageUpdateFileRequest = new StorageUpdateFileRequest(); // StorageUpdateFileRequest | 
    try {
      File result = apiInstance.storageUpdateFile(fileId, storageUpdateFileRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageApi#storageUpdateFile");
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
| **fileId** | **String**| File unique ID. | |
| **storageUpdateFileRequest** | [**StorageUpdateFileRequest**](StorageUpdateFileRequest.md)|  | [optional] |

### Return type

[**File**](File.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | File |  -  |

