# FilesApi

All URIs are relative to *http://app.files.com/api/rest/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteFilesPath**](FilesApi.md#deleteFilesPath) | **DELETE** /files/{path} | Delete file/folder |
| [**fileDownload**](FilesApi.md#fileDownload) | **GET** /files/{path} | Download file |
| [**patchFilesPath**](FilesApi.md#patchFilesPath) | **PATCH** /files/{path} | Update file/folder metadata |
| [**postFilesPath**](FilesApi.md#postFilesPath) | **POST** /files/{path} | Upload file |


<a id="deleteFilesPath"></a>
# **deleteFilesPath**
> deleteFilesPath(path, recursive)

Delete file/folder

Delete file/folder

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
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String path = "path_example"; // String | Path to operate on.
    Boolean recursive = true; // Boolean | If true, will recursively delete folers.  Otherwise, will error on non-empty folders.
    try {
      apiInstance.deleteFilesPath(path, recursive);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#deleteFilesPath");
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
| **path** | **String**| Path to operate on. | |
| **recursive** | **Boolean**| If true, will recursively delete folers.  Otherwise, will error on non-empty folders. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No body. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

<a id="fileDownload"></a>
# **fileDownload**
> FileEntity fileDownload(path, action, previewSize, withPreviews, withPriorityColor)

Download file

Download file

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
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String path = "path_example"; // String | Path to operate on.
    String action = "action_example"; // String | Can be blank, `redirect` or `stat`.  If set to `stat`, we will return file information but without a download URL, and without logging a download.  If set to `redirect` we will serve a 302 redirect directly to the file.  This is used for integrations with Zapier, and is not recommended for most integrations.
    String previewSize = "previewSize_example"; // String | Request a preview size.  Can be `small` (default), `large`, `xlarge`, or `pdf`.
    Boolean withPreviews = true; // Boolean | Include file preview information?
    Boolean withPriorityColor = true; // Boolean | Include file priority color information?
    try {
      FileEntity result = apiInstance.fileDownload(path, action, previewSize, withPreviews, withPriorityColor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#fileDownload");
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
| **path** | **String**| Path to operate on. | |
| **action** | **String**| Can be blank, &#x60;redirect&#x60; or &#x60;stat&#x60;.  If set to &#x60;stat&#x60;, we will return file information but without a download URL, and without logging a download.  If set to &#x60;redirect&#x60; we will serve a 302 redirect directly to the file.  This is used for integrations with Zapier, and is not recommended for most integrations. | [optional] |
| **previewSize** | **String**| Request a preview size.  Can be &#x60;small&#x60; (default), &#x60;large&#x60;, &#x60;xlarge&#x60;, or &#x60;pdf&#x60;. | [optional] |
| **withPreviews** | **Boolean**| Include file preview information? | [optional] |
| **withPriorityColor** | **Boolean**| Include file priority color information? | [optional] |

### Return type

[**FileEntity**](FileEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Files object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

<a id="patchFilesPath"></a>
# **patchFilesPath**
> FileEntity patchFilesPath(path, priorityColor, providedMtime)

Update file/folder metadata

Update file/folder metadata

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
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String path = "path_example"; // String | Path to operate on.
    String priorityColor = "priorityColor_example"; // String | Priority/Bookmark color of file.
    OffsetDateTime providedMtime = OffsetDateTime.now(); // OffsetDateTime | Modified time of file.
    try {
      FileEntity result = apiInstance.patchFilesPath(path, priorityColor, providedMtime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#patchFilesPath");
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
| **path** | **String**| Path to operate on. | |
| **priorityColor** | **String**| Priority/Bookmark color of file. | [optional] |
| **providedMtime** | **OffsetDateTime**| Modified time of file. | [optional] |

### Return type

[**FileEntity**](FileEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Files object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

<a id="postFilesPath"></a>
# **postFilesPath**
> FileEntity postFilesPath(path, etagsEtag, etagsPart, action, length, mkdirParents, part, parts, providedMtime, ref, restart, size, structure, withRename)

Upload file

Upload file

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
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String path = "path_example"; // String | Path to operate on.
    List<String> etagsEtag = Arrays.asList(); // List<String> | etag identifier.
    List<Integer> etagsPart = Arrays.asList(); // List<Integer> | Part number.
    String action = "action_example"; // String | The action to perform.  Can be `append`, `attachment`, `end`, `upload`, `put`, or may not exist
    Integer length = 56; // Integer | Length of file.
    Boolean mkdirParents = true; // Boolean | Create parent directories if they do not exist?
    Integer part = 56; // Integer | Part if uploading a part.
    Integer parts = 56; // Integer | How many parts to fetch?
    OffsetDateTime providedMtime = OffsetDateTime.now(); // OffsetDateTime | User provided modification time.
    String ref = "ref_example"; // String | 
    Integer restart = 56; // Integer | File byte offset to restart from.
    Integer size = 56; // Integer | Size of file.
    String structure = "structure_example"; // String | If copying folder, copy just the structure?
    Boolean withRename = true; // Boolean | Allow file rename instead of overwrite?
    try {
      FileEntity result = apiInstance.postFilesPath(path, etagsEtag, etagsPart, action, length, mkdirParents, part, parts, providedMtime, ref, restart, size, structure, withRename);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#postFilesPath");
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
| **path** | **String**| Path to operate on. | |
| **etagsEtag** | [**List&lt;String&gt;**](String.md)| etag identifier. | |
| **etagsPart** | [**List&lt;Integer&gt;**](Integer.md)| Part number. | |
| **action** | **String**| The action to perform.  Can be &#x60;append&#x60;, &#x60;attachment&#x60;, &#x60;end&#x60;, &#x60;upload&#x60;, &#x60;put&#x60;, or may not exist | [optional] |
| **length** | **Integer**| Length of file. | [optional] |
| **mkdirParents** | **Boolean**| Create parent directories if they do not exist? | [optional] |
| **part** | **Integer**| Part if uploading a part. | [optional] |
| **parts** | **Integer**| How many parts to fetch? | [optional] |
| **providedMtime** | **OffsetDateTime**| User provided modification time. | [optional] |
| **ref** | **String**|  | [optional] |
| **restart** | **Integer**| File byte offset to restart from. | [optional] |
| **size** | **Integer**| Size of file. | [optional] |
| **structure** | **String**| If copying folder, copy just the structure? | [optional] |
| **withRename** | **Boolean**| Allow file rename instead of overwrite? | [optional] |

### Return type

[**FileEntity**](FileEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The Files object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

