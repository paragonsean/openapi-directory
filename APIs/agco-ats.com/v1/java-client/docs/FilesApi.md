# FilesApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**filesDeleteFile**](FilesApi.md#filesDeleteFile) | **DELETE** /api/v2/Files/{ID} | Mark a file as &#39;Removed&#39;. Disables download of the file and hides metadata from GET all method |
| [**filesGetFile**](FilesApi.md#filesGetFile) | **GET** /api/v2/Files/{ID} | Gets a file&#39;s metadata. |
| [**filesGetFileContents**](FilesApi.md#filesGetFileContents) | **GET** /api/v2/Files/{ID}/FileContents | Download the contents of a file. The current State of the File should be &#39;Available&#39;. |
| [**filesGetFiles**](FilesApi.md#filesGetFiles) | **GET** /api/v2/Files | Get a paged response of file metadata. |
| [**filesPostFile**](FilesApi.md#filesPostFile) | **POST** /api/v2/Files | Create the metadata for a file before uploading. The State of the File should be &#39;Created&#39;. |
| [**filesPutFile**](FilesApi.md#filesPutFile) | **PUT** /api/v2/Files/{ID} | Update the metadata for a file. Size may not be modified by the client. |
| [**filesPutFileContents**](FilesApi.md#filesPutFileContents) | **PUT** /api/v2/Files/{ID}/FileContents | Upload the contents of a file. The current State of the File should be &#39;Created&#39;. |


<a id="filesDeleteFile"></a>
# **filesDeleteFile**
> filesDeleteFile(ID)

Mark a file as &#39;Removed&#39;. Disables download of the file and hides metadata from GET all method

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String ID = "ID_example"; // String | The file's id.
    try {
      apiInstance.filesDeleteFile(ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#filesDeleteFile");
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
| **ID** | **String**| The file&#39;s id. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

<a id="filesGetFile"></a>
# **filesGetFile**
> GlobalResourcesSharedModelsFileDownload filesGetFile(ID)

Gets a file&#39;s metadata.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String ID = "ID_example"; // String | 
    try {
      GlobalResourcesSharedModelsFileDownload result = apiInstance.filesGetFile(ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#filesGetFile");
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
| **ID** | **String**|  | |

### Return type

[**GlobalResourcesSharedModelsFileDownload**](GlobalResourcesSharedModelsFileDownload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="filesGetFileContents"></a>
# **filesGetFileContents**
> Object filesGetFileContents(ID)

Download the contents of a file. The current State of the File should be &#39;Available&#39;.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String ID = "ID_example"; // String | The file's metadata.
    try {
      Object result = apiInstance.filesGetFileContents(ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#filesGetFileContents");
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
| **ID** | **String**| The file&#39;s metadata. | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="filesGetFiles"></a>
# **filesGetFiles**
> APIIPagedResponseGlobalResourcesSharedModelsFileDownload filesGetFiles(includeDeleted, limit, offset)

Get a paged response of file metadata.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    FilesApi apiInstance = new FilesApi(defaultClient);
    Boolean includeDeleted = true; // Boolean | Indicates whether to include files marked as removed.
    Integer limit = 56; // Integer | Optional. The page limit. The default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset. The default page offset is 0.
    try {
      APIIPagedResponseGlobalResourcesSharedModelsFileDownload result = apiInstance.filesGetFiles(includeDeleted, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#filesGetFiles");
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
| **includeDeleted** | **Boolean**| Indicates whether to include files marked as removed. | [optional] |
| **limit** | **Integer**| Optional. The page limit. The default page limit is 10. | [optional] |
| **offset** | **Integer**| Optional. The page offset. The default page offset is 0. | [optional] |

### Return type

[**APIIPagedResponseGlobalResourcesSharedModelsFileDownload**](APIIPagedResponseGlobalResourcesSharedModelsFileDownload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="filesPostFile"></a>
# **filesPostFile**
> String filesPostFile(globalResourcesSharedModelsFileDownload)

Create the metadata for a file before uploading. The State of the File should be &#39;Created&#39;.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    FilesApi apiInstance = new FilesApi(defaultClient);
    GlobalResourcesSharedModelsFileDownload globalResourcesSharedModelsFileDownload = new GlobalResourcesSharedModelsFileDownload(); // GlobalResourcesSharedModelsFileDownload | The file's metadata.
    try {
      String result = apiInstance.filesPostFile(globalResourcesSharedModelsFileDownload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#filesPostFile");
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
| **globalResourcesSharedModelsFileDownload** | [**GlobalResourcesSharedModelsFileDownload**](GlobalResourcesSharedModelsFileDownload.md)| The file&#39;s metadata. | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="filesPutFile"></a>
# **filesPutFile**
> filesPutFile(ID, globalResourcesSharedModelsFileDownload)

Update the metadata for a file. Size may not be modified by the client.

Update the metadata for a file. Size may not be modified by the client.                   Set status to &#39;Available&#39; to publish a file. The file must be uploaded.                  Set status to &#39;Created&#39; to reset a file&#39;s contents and re-upload.                   A file may only be &#39;Removed&#39; by the DELETE method.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String ID = "ID_example"; // String | The file's id
    GlobalResourcesSharedModelsFileDownload globalResourcesSharedModelsFileDownload = new GlobalResourcesSharedModelsFileDownload(); // GlobalResourcesSharedModelsFileDownload | The file's metadata
    try {
      apiInstance.filesPutFile(ID, globalResourcesSharedModelsFileDownload);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#filesPutFile");
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
| **ID** | **String**| The file&#39;s id | |
| **globalResourcesSharedModelsFileDownload** | [**GlobalResourcesSharedModelsFileDownload**](GlobalResourcesSharedModelsFileDownload.md)| The file&#39;s metadata | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

<a id="filesPutFileContents"></a>
# **filesPutFileContents**
> Object filesPutFileContents(ID)

Upload the contents of a file. The current State of the File should be &#39;Created&#39;.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String ID = "ID_example"; // String | The file's metadata.
    try {
      Object result = apiInstance.filesPutFileContents(ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#filesPutFileContents");
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
| **ID** | **String**| The file&#39;s metadata. | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

