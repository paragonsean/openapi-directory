# DocumentsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteDocument**](DocumentsApi.md#deleteDocument) | **DELETE** /documents/{documentId} | Delete Document |
| [**downloadDocument**](DocumentsApi.md#downloadDocument) | **GET** /documents/{documentId} | Download a Document |
| [**getDocuments**](DocumentsApi.md#getDocuments) | **GET** /documents | Get Documents |


<a id="deleteDocument"></a>
# **deleteDocument**
> deleteDocument(documentId)

Delete Document

The delete document service allows the consumer to delete a document. The deleted document will not be returned in the get documents API. The HTTP response code is 204 (success without content).&lt;br&gt;Documents can be deleted only if the document related dataset attributes are subscribed.&lt;br&gt;

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
    defaultClient.setBasePath("http://localhost");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    String documentId = "documentId_example"; // String | documentId
    try {
      apiInstance.deleteDocument(documentId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#deleteDocument");
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
| **documentId** | **String**| documentId | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | OK |  -  |
| **400** | Y800 : Invalid value for documentId&lt;br&gt;Y868 : No action is allowed, as the data is being migrated to the Open Banking provider&lt;br&gt; |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="downloadDocument"></a>
# **downloadDocument**
> DocumentDownloadResponse downloadDocument(documentId)

Download a Document

The get document details service allows consumers to download a document. The document is provided in base64.&lt;br&gt;This API is a premium service which requires subscription in advance to use.  Please contact Yodlee Client Services for more information. &lt;br&gt;

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
    defaultClient.setBasePath("http://localhost");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    String documentId = "documentId_example"; // String | documentId
    try {
      DocumentDownloadResponse result = apiInstance.downloadDocument(documentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#downloadDocument");
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
| **documentId** | **String**| documentId | |

### Return type

[**DocumentDownloadResponse**](DocumentDownloadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Y800 : Invalid value for documentId |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="getDocuments"></a>
# **getDocuments**
> DocumentResponse getDocuments(keyword, accountId, docType, fromDate, toDate)

Get Documents

The get documents service allows customers to search or retrieve metadata related to documents. &lt;br&gt;The API returns the document as per the input parameters passed. If no date range is provided then all downloaded documents will be retrieved. Details of deleted documents or documents associated to closed providerAccount will not be returned. &lt;br&gt;This API is a premium service which requires subscription in advance to use.  Please contact Yodlee Client Services for more information. &lt;br&gt;

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
    defaultClient.setBasePath("http://localhost");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    String keyword = "keyword_example"; // String | The string used to search a document by its name.
    String accountId = "accountId_example"; // String | The unique identifier of an account. Retrieve documents for a given accountId.
    String docType = "docType_example"; // String | Accepts only one of the following valid document types: STMT, TAX, and EBILL.
    String fromDate = "fromDate_example"; // String | The date from which documents have to be retrieved.
    String toDate = "toDate_example"; // String | The date to which documents have to be retrieved.
    try {
      DocumentResponse result = apiInstance.getDocuments(keyword, accountId, docType, fromDate, toDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#getDocuments");
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
| **keyword** | **String**| The string used to search a document by its name. | [optional] |
| **accountId** | **String**| The unique identifier of an account. Retrieve documents for a given accountId. | [optional] |
| **docType** | **String**| Accepts only one of the following valid document types: STMT, TAX, and EBILL. | [optional] |
| **fromDate** | **String**| The date from which documents have to be retrieved. | [optional] |
| **toDate** | **String**| The date to which documents have to be retrieved. | [optional] |

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Y800 : Invalid value for accountId&lt;br&gt;Y800 : Invalid value for fromDate&lt;br&gt;Y800 : Invalid value for toDate&lt;br&gt;Y800 : Invalid value for docType |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

