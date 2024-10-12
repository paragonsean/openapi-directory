# DocumentsApi

All URIs are relative to *https://bills-api.parliament.uk*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV1PublicationsPublicationIdDocumentsDocumentIdDownloadGet**](DocumentsApi.md#apiV1PublicationsPublicationIdDocumentsDocumentIdDownloadGet) | **GET** /api/v1/Publications/{publicationId}/Documents/{documentId}/Download | Return a document. |
| [**apiV1PublicationsPublicationIdDocumentsDocumentIdGet**](DocumentsApi.md#apiV1PublicationsPublicationIdDocumentsDocumentIdGet) | **GET** /api/v1/Publications/{publicationId}/Documents/{documentId} | Return information on a document. |


<a id="apiV1PublicationsPublicationIdDocumentsDocumentIdDownloadGet"></a>
# **apiV1PublicationsPublicationIdDocumentsDocumentIdDownloadGet**
> apiV1PublicationsPublicationIdDocumentsDocumentIdDownloadGet(publicationId, documentId)

Return a document.

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
    defaultClient.setBasePath("https://bills-api.parliament.uk");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    Integer publicationId = 56; // Integer | Document with publication Id specified
    Integer documentId = 56; // Integer | Document with Id specified
    try {
      apiInstance.apiV1PublicationsPublicationIdDocumentsDocumentIdDownloadGet(publicationId, documentId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#apiV1PublicationsPublicationIdDocumentsDocumentIdDownloadGet");
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
| **publicationId** | **Integer**| Document with publication Id specified | |
| **documentId** | **Integer**| Document with Id specified | |

### Return type

null (empty response body)

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
| **404** | Not Found |  -  |

<a id="apiV1PublicationsPublicationIdDocumentsDocumentIdGet"></a>
# **apiV1PublicationsPublicationIdDocumentsDocumentIdGet**
> PublicationDocument apiV1PublicationsPublicationIdDocumentsDocumentIdGet(publicationId, documentId)

Return information on a document.

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
    defaultClient.setBasePath("https://bills-api.parliament.uk");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    Integer publicationId = 56; // Integer | Document with publication Id specified
    Integer documentId = 56; // Integer | Document with Id specified
    try {
      PublicationDocument result = apiInstance.apiV1PublicationsPublicationIdDocumentsDocumentIdGet(publicationId, documentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#apiV1PublicationsPublicationIdDocumentsDocumentIdGet");
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
| **publicationId** | **Integer**| Document with publication Id specified | |
| **documentId** | **Integer**| Document with Id specified | |

### Return type

[**PublicationDocument**](PublicationDocument.md)

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
| **404** | Not Found |  -  |

