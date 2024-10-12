# ReceivedDocumentsApi

All URIs are relative to *https://api.storecove.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getReceivedDocument**](ReceivedDocumentsApi.md#getReceivedDocument) | **GET** /received_documents/{guid}/{format} | Get a new ReceivedDocument |
| [**receiveDocument**](ReceivedDocumentsApi.md#receiveDocument) | **POST** /legal_entities/{legal_entity_id}/received_documents | Receive a new Document |


<a id="getReceivedDocument"></a>
# **getReceivedDocument**
> ReceivedDocument getReceivedDocument(guid, syntax, format)

Get a new ReceivedDocument

EXPERIMENTAL: use only for orders. Get a new ReceivedDocument.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReceivedDocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.storecove.com/api/v2");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ReceivedDocumentsApi apiInstance = new ReceivedDocumentsApi(defaultClient);
    UUID guid = UUID.randomUUID(); // UUID | The guid of the document that was received. This is the \"document_guid\" property of the \"received_document\" webhook.
    String syntax = "json"; // String | The syntax in which to receive the received document.
    String format = "format_example"; // String | Automatically added
    try {
      ReceivedDocument result = apiInstance.getReceivedDocument(guid, syntax, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReceivedDocumentsApi#getReceivedDocument");
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
| **guid** | **UUID**| The guid of the document that was received. This is the \&quot;document_guid\&quot; property of the \&quot;received_document\&quot; webhook. | |
| **syntax** | **String**| The syntax in which to receive the received document. | [default to json] [enum: json, original] |
| **format** | **String**| Automatically added | |

### Return type

[**ReceivedDocument**](ReceivedDocument.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="receiveDocument"></a>
# **receiveDocument**
> ReceivedDocument receiveDocument(legalEntityId, receivedDocumentCreate)

Receive a new Document

Receive a new Document.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReceivedDocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.storecove.com/api/v2");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ReceivedDocumentsApi apiInstance = new ReceivedDocumentsApi(defaultClient);
    Long legalEntityId = 56L; // Long | The id of the LegalEntity for which the document was received.
    ReceivedDocumentCreate receivedDocumentCreate = new ReceivedDocumentCreate(); // ReceivedDocumentCreate | Received document to process.
    try {
      ReceivedDocument result = apiInstance.receiveDocument(legalEntityId, receivedDocumentCreate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReceivedDocumentsApi#receiveDocument");
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
| **legalEntityId** | **Long**| The id of the LegalEntity for which the document was received. | |
| **receivedDocumentCreate** | [**ReceivedDocumentCreate**](ReceivedDocumentCreate.md)| Received document to process. | |

### Return type

[**ReceivedDocument**](ReceivedDocument.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **422** | Unprocessable Entity |  -  |

