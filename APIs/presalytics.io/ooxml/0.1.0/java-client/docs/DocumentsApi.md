# DocumentsApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**documentsChildobjectsGetId**](DocumentsApi.md#documentsChildobjectsGetId) | **GET** /Documents/ChildObjects/{id} | DocumentsController: Get Dependent Objects Tree |
| [**documentsClonePostId**](DocumentsApi.md#documentsClonePostId) | **POST** /Documents/Clone/{id} | Documents: Clone an existing Ooxml Document to new Parent Story |
| [**documentsDeleteId**](DocumentsApi.md#documentsDeleteId) | **DELETE** /Documents/{id} | Documents: Delete by Id |
| [**documentsDownloadGetIdOrginal**](DocumentsApi.md#documentsDownloadGetIdOrginal) | **GET** /Documents/Download/{id} | Documents: Download |
| [**documentsGetId**](DocumentsApi.md#documentsGetId) | **GET** /Documents/{id} | Documents: Get by Id |
| [**documentsPost**](DocumentsApi.md#documentsPost) | **POST** /Documents | Documents: Upload |


<a id="documentsChildobjectsGetId"></a>
# **documentsChildobjectsGetId**
> List&lt;ChildObjects&gt; documentsChildobjectsGetId(id)

DocumentsController: Get Dependent Objects Tree

This endpoint is helpful for helping users and bots identify dependent objects to this DocumentsController and retreive their corresponding metadata in order to make modifications to those objects in downstream operations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      List<ChildObjects> result = apiInstance.documentsChildobjectsGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#documentsChildobjectsGetId");
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
| **id** | **UUID**|  | |

### Return type

[**List&lt;ChildObjects&gt;**](ChildObjects.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |

<a id="documentsClonePostId"></a>
# **documentsClonePostId**
> Document documentsClonePostId(id, documentCloneDTO)

Documents: Clone an existing Ooxml Document to new Parent Story

Clone A Document that has already been uploaded to a new Story

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | the Source document Id
    DocumentCloneDTO documentCloneDTO = new DocumentCloneDTO(); // DocumentCloneDTO | A DocumentCloneDto object with containing information required for cloning the document
    try {
      Document result = apiInstance.documentsClonePostId(id, documentCloneDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#documentsClonePostId");
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
| **id** | **UUID**| the Source document Id | |
| **documentCloneDTO** | [**DocumentCloneDTO**](DocumentCloneDTO.md)| A DocumentCloneDto object with containing information required for cloning the document | [optional] |

### Return type

[**Document**](Document.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="documentsDeleteId"></a>
# **documentsDeleteId**
> documentsDeleteId(id)

Documents: Delete by Id

Permantly delete a document from the Ooxml Automation API. Note that is does not make changes to the related Presalytics APIs.  Please use the delete endpoint in the story API to ensure that stories are not left with orphaned references to the Ooxml Automation API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      apiInstance.documentsDeleteId(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#documentsDeleteId");
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
| **id** | **UUID**|  | |

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
| **204** | Success |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |

<a id="documentsDownloadGetIdOrginal"></a>
# **documentsDownloadGetIdOrginal**
> File documentsDownloadGetIdOrginal(id, orginal)

Documents: Download

Download the into a bytestream for client-side processing.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    Boolean orginal = false; // Boolean | 
    try {
      File result = apiInstance.documentsDownloadGetIdOrginal(id, orginal);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#documentsDownloadGetIdOrginal");
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
| **id** | **UUID**|  | |
| **orginal** | **Boolean**|  | [optional] [default to false] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an updated version of the OpenOffice Xml file |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |

<a id="documentsGetId"></a>
# **documentsGetId**
> Document documentsGetId(id)

Documents: Get by Id

Get by Id: Use this method to retrieve a Documents object by its primary key (id)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      Document result = apiInstance.documentsGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#documentsGetId");
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
| **id** | **UUID**|  | |

### Return type

[**Document**](Document.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="documentsPost"></a>
# **documentsPost**
> List&lt;Document&gt; documentsPost(_file, storyId)

Documents: Upload

Upload an OpenOfficeXml document (e.g., .xlsx, .pptx) for processing by the API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    File _file = new File("/path/to/file"); // File | The file to upload.  Must be of type .pptx, ppt
    UUID storyId = UUID.randomUUID(); // UUID | The story_id of the document being uploaded.
    try {
      List<Document> result = apiInstance.documentsPost(_file, storyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#documentsPost");
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
| **_file** | **File**| The file to upload.  Must be of type .pptx, ppt | |
| **storyId** | **UUID**| The story_id of the document being uploaded. | |

### Return type

[**List&lt;Document&gt;**](Document.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

