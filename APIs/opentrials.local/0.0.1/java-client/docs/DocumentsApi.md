# DocumentsApi

All URIs are relative to *http://opentrials.local/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDocument**](DocumentsApi.md#getDocument) | **GET** /documents/{id} |  |
| [**listDocuments**](DocumentsApi.md#listDocuments) | **GET** /documents |  |


<a id="getDocument"></a>
# **getDocument**
> Document getDocument(id)



Returns details of a document

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
    defaultClient.setBasePath("http://opentrials.local/v1");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    String id = "id_example"; // String | ID of the document
    try {
      Document result = apiInstance.getDocument(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#getDocument");
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
| **id** | **String**| ID of the document | |

### Return type

[**Document**](Document.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Document not found |  -  |
| **0** | Error |  -  |

<a id="listDocuments"></a>
# **listDocuments**
> DocumentList listDocuments(page, perPage)



Returns documents

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
    defaultClient.setBasePath("http://opentrials.local/v1");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    Integer page = 1; // Integer | The page number
    Integer perPage = 20; // Integer | Number of items per page
    try {
      DocumentList result = apiInstance.listDocuments(page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#listDocuments");
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
| **page** | **Integer**| The page number | [optional] [default to 1] |
| **perPage** | **Integer**| Number of items per page | [optional] [default to 20] |

### Return type

[**DocumentList**](DocumentList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

