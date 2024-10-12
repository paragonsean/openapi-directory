# ProcessingDocumentsApi

All URIs are relative to *https://api.semantria.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelDocument**](ProcessingDocumentsApi.md#cancelDocument) | **DELETE** /document/{document_id}.{content_type} | Cancel document analysis |
| [**queueBatchOfDocuments**](ProcessingDocumentsApi.md#queueBatchOfDocuments) | **POST** /document/batch.{content_type} | Queue batch of documents for analysis |
| [**queueDocument**](ProcessingDocumentsApi.md#queueDocument) | **POST** /document.{content_type} | Queue document for analysis |
| [**receiveDocumentAnalyticData**](ProcessingDocumentsApi.md#receiveDocumentAnalyticData) | **GET** /document/{document_id}.{content_type} | Retrieve document analysis or its status in queue |
| [**retrieveProcessedDocuments**](ProcessingDocumentsApi.md#retrieveProcessedDocuments) | **GET** /document/processed.{content_type} | Retrieve documents analysis |


<a id="cancelDocument"></a>
# **cancelDocument**
> cancelDocument(documentId, contentType, configId)

Cancel document analysis

This method cancels document analysis by unique ID on Semantria side if it is waiting for analysis in queue.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProcessingDocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.semantria.com");

    ProcessingDocumentsApi apiInstance = new ProcessingDocumentsApi(defaultClient);
    String documentId = "documentId_example"; // String | Document ID
    String contentType = "contentType_example"; // String | 
    String configId = "configId_example"; // String | Identifier of configuration used for analysis.
    try {
      apiInstance.cancelDocument(documentId, contentType, configId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProcessingDocumentsApi#cancelDocument");
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
| **documentId** | **String**| Document ID | |
| **contentType** | **String**|  | |
| **configId** | **String**| Identifier of configuration used for analysis. | [optional] |

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
| **200** | Client request accepted. Document canceled from processing on the server. |  -  |
| **401** | Authentication failed. |  -  |
| **402** | Unauthorized. Limit of system calls is reached or subscription is expired. |  -  |
| **404** | No documents with provided ID found on server. |  -  |
| **500** | Server side issue. Server may respond with the details in response body. |  -  |

<a id="queueBatchOfDocuments"></a>
# **queueBatchOfDocuments**
> Document queueBatchOfDocuments(contentType, batchOfDocuments, configId)

Queue batch of documents for analysis

This method queues batch of documents for analysis. The rules are the same as for single document mode but here the documents ordered into the batch.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProcessingDocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.semantria.com");

    ProcessingDocumentsApi apiInstance = new ProcessingDocumentsApi(defaultClient);
    String contentType = "contentType_example"; // String | 
    Object batchOfDocuments = null; // Object | List of parametrized JSON or XML objects.
    String configId = "configId_example"; // String | Identifier of configuration used for analysis.
    try {
      Document result = apiInstance.queueBatchOfDocuments(contentType, batchOfDocuments, configId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProcessingDocumentsApi#queueBatchOfDocuments");
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
| **contentType** | **String**|  | |
| **batchOfDocuments** | **Object**| List of parametrized JSON or XML objects. | |
| **configId** | **String**| Identifier of configuration used for analysis. | [optional] |

### Return type

[**Document**](Document.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Client request accepted and queued. Server responds with the sentiment-bearing phrases list. |  -  |
| **202** | Client request accepted and queued for processing. |  -  |
| **401** | Authentication failed. |  -  |
| **402** | Unauthorized. Limit of system calls is reached or subscription is expired. |  -  |
| **403** | Request is forbidden for selected processing mode. |  -  |
| **406** | Documents limit per batch is achieved. |  -  |
| **413** | Characters limit for the document exceeded. |  -  |
| **500** | Server side issue. Server may respond with the details in response body. |  -  |

<a id="queueDocument"></a>
# **queueDocument**
> Document queueDocument(contentType, document, configId)

Queue document for analysis

This method queues document onto the server for analysis. Queued document analyzes individually and will have its own set of results. If unique configuration ID provided, Semantria uses settings of that configuration during analysis, in opposite the primary configuration uses. Document IDs are unique in scope of configuration. If the same ID appears twice, Semantria overrides existing document with the new Data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProcessingDocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.semantria.com");

    ProcessingDocumentsApi apiInstance = new ProcessingDocumentsApi(defaultClient);
    String contentType = "contentType_example"; // String | 
    Object document = null; // Object | Parametrized JSON or XML object.
    String configId = "configId_example"; // String | Identifier of configuration used for analysis.
    try {
      Document result = apiInstance.queueDocument(contentType, document, configId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProcessingDocumentsApi#queueDocument");
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
| **contentType** | **String**|  | |
| **document** | **Object**| Parametrized JSON or XML object. | |
| **configId** | **String**| Identifier of configuration used for analysis. | [optional] |

### Return type

[**Document**](Document.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Client request accepted and queued. Server responds with the sentiment-bearing phrases list. |  -  |
| **202** | Client request accepted and queued for processing. |  -  |
| **401** | Authentication failed. |  -  |
| **402** | Unauthorized. Limit of system calls is reached or subscription is expired. |  -  |
| **413** | Characters limit for the document exceeded. |  -  |
| **500** | Server side issue. Server may respond with the details in response body. |  -  |

<a id="receiveDocumentAnalyticData"></a>
# **receiveDocumentAnalyticData**
> DocumentAnalyticData receiveDocumentAnalyticData(documentId, contentType, configId)

Retrieve document analysis or its status in queue

This method retrieves analysis results for the single document by its unique ID or the document’s status in queue if it did not analyzed yet. Semantria guarantees delivering of all documents back to the client even if they FAILED on Semantria side due to some reason.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProcessingDocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.semantria.com");

    ProcessingDocumentsApi apiInstance = new ProcessingDocumentsApi(defaultClient);
    String documentId = "documentId_example"; // String | Document ID
    String contentType = "contentType_example"; // String | 
    String configId = "configId_example"; // String | Identifier of configuration used for analysis.
    try {
      DocumentAnalyticData result = apiInstance.receiveDocumentAnalyticData(documentId, contentType, configId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProcessingDocumentsApi#receiveDocumentAnalyticData");
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
| **documentId** | **String**| Document ID | |
| **contentType** | **String**|  | |
| **configId** | **String**| Identifier of configuration used for analysis. | [optional] |

### Return type

[**DocumentAnalyticData**](DocumentAnalyticData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Client request accepted. Server responds with processed document or its status. |  -  |
| **401** | Authentication failed. |  -  |
| **402** | Unauthorized. Limit of system calls is reached or subscription is expired. |  -  |
| **404** | No documents with provided ID found on server. |  -  |
| **500** | Server side issue. Server may respond with the details in response body. |  -  |

<a id="retrieveProcessedDocuments"></a>
# **retrieveProcessedDocuments**
> DocumentAnalyticData retrieveProcessedDocuments(contentType, configId)

Retrieve documents analysis

This method retrieves analysis results for processed documents from Semantria. FAILED documents will have FAILED status in response. Semantria responds with limited amount of results per API call. If configuration ID provided, Semantria responds with the document, which were queued using the same configuration ID, in opposite Primary.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProcessingDocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.semantria.com");

    ProcessingDocumentsApi apiInstance = new ProcessingDocumentsApi(defaultClient);
    String contentType = "contentType_example"; // String | 
    String configId = "configId_example"; // String | Identifier of configuration used for analysis.
    try {
      DocumentAnalyticData result = apiInstance.retrieveProcessedDocuments(contentType, configId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProcessingDocumentsApi#retrieveProcessedDocuments");
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
| **contentType** | **String**|  | |
| **configId** | **String**| Identifier of configuration used for analysis. | [optional] |

### Return type

[**DocumentAnalyticData**](DocumentAnalyticData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Client request accepted and queued. Server responds with processed documents. |  -  |
| **202** | Client request accepted, no processed documents found on the server. |  -  |
| **401** | Authentication failed. |  -  |
| **402** | Unauthorized. Limit of system calls is reached or subscription is expired. |  -  |
| **500** | Server side issue. Server may respond with the details in response body. |  -  |

