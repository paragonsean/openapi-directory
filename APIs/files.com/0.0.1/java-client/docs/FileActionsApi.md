# FileActionsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fileActionBeginUpload**](FileActionsApi.md#fileActionBeginUpload) | **POST** /file_actions/begin_upload/{path} | Begin file upload |
| [**fileActionCopy**](FileActionsApi.md#fileActionCopy) | **POST** /file_actions/copy/{path} | Copy file/folder |
| [**fileActionFind**](FileActionsApi.md#fileActionFind) | **GET** /file_actions/metadata/{path} | Find file/folder by path |
| [**fileActionMove**](FileActionsApi.md#fileActionMove) | **POST** /file_actions/move/{path} | Move file/folder |


<a id="fileActionBeginUpload"></a>
# **fileActionBeginUpload**
> List&lt;FileUploadPartEntity&gt; fileActionBeginUpload(path, mkdirParents, part, parts, ref, restart, size, withRename)

Begin file upload

Begin file upload

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    FileActionsApi apiInstance = new FileActionsApi(defaultClient);
    String path = "path_example"; // String | Path to operate on.
    Boolean mkdirParents = true; // Boolean | Create parent directories if they do not exist?
    Integer part = 56; // Integer | Part if uploading a part.
    Integer parts = 56; // Integer | How many parts to fetch?
    String ref = "ref_example"; // String | 
    Integer restart = 56; // Integer | File byte offset to restart from.
    Integer size = 56; // Integer | Total bytes of file being uploaded (include bytes being retained if appending/restarting).
    Boolean withRename = true; // Boolean | Allow file rename instead of overwrite?
    try {
      List<FileUploadPartEntity> result = apiInstance.fileActionBeginUpload(path, mkdirParents, part, parts, ref, restart, size, withRename);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileActionsApi#fileActionBeginUpload");
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
| **part** | **Integer**| Part if uploading a part. | [optional] |
| **parts** | **Integer**| How many parts to fetch? | [optional] |
| **ref** | **String**|  | [optional] |
| **restart** | **Integer**| File byte offset to restart from. | [optional] |
| **size** | **Integer**| Total bytes of file being uploaded (include bytes being retained if appending/restarting). | [optional] |
| **withRename** | **Boolean**| Allow file rename instead of overwrite? | [optional] |

### Return type

[**List&lt;FileUploadPartEntity&gt;**](FileUploadPartEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The FileActions object. |  -  |
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

<a id="fileActionCopy"></a>
# **fileActionCopy**
> FileActionEntity fileActionCopy(path, destination, structure)

Copy file/folder

Copy file/folder

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    FileActionsApi apiInstance = new FileActionsApi(defaultClient);
    String path = "path_example"; // String | Path to operate on.
    String destination = "destination_example"; // String | Copy destination path.
    Boolean structure = true; // Boolean | Copy structure only?
    try {
      FileActionEntity result = apiInstance.fileActionCopy(path, destination, structure);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileActionsApi#fileActionCopy");
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
| **destination** | **String**| Copy destination path. | |
| **structure** | **Boolean**| Copy structure only? | [optional] |

### Return type

[**FileActionEntity**](FileActionEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The FileActions object. |  -  |
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

<a id="fileActionFind"></a>
# **fileActionFind**
> FileEntity fileActionFind(path, previewSize, withPreviews, withPriorityColor)

Find file/folder by path

Find file/folder by path

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    FileActionsApi apiInstance = new FileActionsApi(defaultClient);
    String path = "path_example"; // String | Path to operate on.
    String previewSize = "previewSize_example"; // String | Request a preview size.  Can be `small` (default), `large`, `xlarge`, or `pdf`.
    Boolean withPreviews = true; // Boolean | Include file preview information?
    Boolean withPriorityColor = true; // Boolean | Include file priority color information?
    try {
      FileEntity result = apiInstance.fileActionFind(path, previewSize, withPreviews, withPriorityColor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileActionsApi#fileActionFind");
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
| **200** | The FileActions object. |  -  |
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

<a id="fileActionMove"></a>
# **fileActionMove**
> FileActionEntity fileActionMove(path, destination)

Move file/folder

Move file/folder

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    FileActionsApi apiInstance = new FileActionsApi(defaultClient);
    String path = "path_example"; // String | Path to operate on.
    String destination = "destination_example"; // String | Move destination path.
    try {
      FileActionEntity result = apiInstance.fileActionMove(path, destination);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileActionsApi#fileActionMove");
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
| **destination** | **String**| Move destination path. | |

### Return type

[**FileActionEntity**](FileActionEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The FileActions object. |  -  |
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

