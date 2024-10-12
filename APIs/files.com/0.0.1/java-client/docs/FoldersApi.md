# FoldersApi

All URIs are relative to *http://app.files.com/api/rest/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**folderListForPath**](FoldersApi.md#folderListForPath) | **GET** /folders/{path} | List Folders by path |
| [**postFoldersPath**](FoldersApi.md#postFoldersPath) | **POST** /folders/{path} | Create folder |


<a id="folderListForPath"></a>
# **folderListForPath**
> List&lt;FileEntity&gt; folderListForPath(path, cursor, perPage, filter, previewSize, sortBy, search, searchAll, withPreviews, withPriorityColor)

List Folders by path

List Folders by path

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FoldersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    FoldersApi apiInstance = new FoldersApi(defaultClient);
    String path = "path_example"; // String | Path to operate on.
    String cursor = "cursor_example"; // String | Send cursor to resume an existing list from the point at which you left off.  Get a cursor from an existing list via the X-Files-Cursor-Next header or the X-Files-Cursor-Prev header.
    Integer perPage = 56; // Integer | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    String filter = "filter_example"; // String | If specified, will filter folders/files list by this string.  Wildcards of `*` and `?` are acceptable here.
    String previewSize = "previewSize_example"; // String | Request a preview size.  Can be `small` (default), `large`, `xlarge`, or `pdf`.
    Object sortBy = null; // Object | Search by field and direction. Valid fields are `path`, `size`, `modified_at_datetime`, `provided_modified_at`.  Valid directions are `asc` and `desc`.  Defaults to `{\"path\":\"asc\"}`.
    String search = "search_example"; // String | If `search_all` is `true`, provide the search string here.  Otherwise, this parameter acts like an alias of `filter`.
    Boolean searchAll = true; // Boolean | Search entire site?  If set, we will ignore the folder path provided and search the entire site.  This is the same API used by the search bar in the UI.  Search results are a best effort, not real time, and not guaranteed to match every file.  This field should only be used for ad-hoc (human) searching, and not as part of an automated process.
    Boolean withPreviews = true; // Boolean | Include file previews?
    Boolean withPriorityColor = true; // Boolean | Include file priority color information?
    try {
      List<FileEntity> result = apiInstance.folderListForPath(path, cursor, perPage, filter, previewSize, sortBy, search, searchAll, withPreviews, withPriorityColor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FoldersApi#folderListForPath");
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
| **cursor** | **String**| Send cursor to resume an existing list from the point at which you left off.  Get a cursor from an existing list via the X-Files-Cursor-Next header or the X-Files-Cursor-Prev header. | [optional] |
| **perPage** | **Integer**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] |
| **filter** | **String**| If specified, will filter folders/files list by this string.  Wildcards of &#x60;*&#x60; and &#x60;?&#x60; are acceptable here. | [optional] |
| **previewSize** | **String**| Request a preview size.  Can be &#x60;small&#x60; (default), &#x60;large&#x60;, &#x60;xlarge&#x60;, or &#x60;pdf&#x60;. | [optional] |
| **sortBy** | [**Object**](.md)| Search by field and direction. Valid fields are &#x60;path&#x60;, &#x60;size&#x60;, &#x60;modified_at_datetime&#x60;, &#x60;provided_modified_at&#x60;.  Valid directions are &#x60;asc&#x60; and &#x60;desc&#x60;.  Defaults to &#x60;{\&quot;path\&quot;:\&quot;asc\&quot;}&#x60;. | [optional] |
| **search** | **String**| If &#x60;search_all&#x60; is &#x60;true&#x60;, provide the search string here.  Otherwise, this parameter acts like an alias of &#x60;filter&#x60;. | [optional] |
| **searchAll** | **Boolean**| Search entire site?  If set, we will ignore the folder path provided and search the entire site.  This is the same API used by the search bar in the UI.  Search results are a best effort, not real time, and not guaranteed to match every file.  This field should only be used for ad-hoc (human) searching, and not as part of an automated process. | [optional] |
| **withPreviews** | **Boolean**| Include file previews? | [optional] |
| **withPriorityColor** | **Boolean**| Include file priority color information? | [optional] |

### Return type

[**List&lt;FileEntity&gt;**](FileEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of Folders objects. |  -  |
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

<a id="postFoldersPath"></a>
# **postFoldersPath**
> FileEntity postFoldersPath(path, mkdirParents, providedMtime)

Create folder

Create folder

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FoldersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    FoldersApi apiInstance = new FoldersApi(defaultClient);
    String path = "path_example"; // String | Path to operate on.
    Boolean mkdirParents = true; // Boolean | Create parent directories if they do not exist?
    OffsetDateTime providedMtime = OffsetDateTime.now(); // OffsetDateTime | User provided modification time.
    try {
      FileEntity result = apiInstance.postFoldersPath(path, mkdirParents, providedMtime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FoldersApi#postFoldersPath");
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
| **mkdirParents** | **Boolean**| Create parent directories if they do not exist? | [optional] |
| **providedMtime** | **OffsetDateTime**| User provided modification time. | [optional] |

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
| **201** | The Folders object. |  -  |
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

