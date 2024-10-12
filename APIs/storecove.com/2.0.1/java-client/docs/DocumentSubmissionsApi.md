# DocumentSubmissionsApi

All URIs are relative to *https://api.storecove.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createDocumentSubmission**](DocumentSubmissionsApi.md#createDocumentSubmission) | **POST** /document_submissions | Submit a new document. |
| [**showDocumentSubmissionEvidence**](DocumentSubmissionsApi.md#showDocumentSubmissionEvidence) | **GET** /document_submissions/{guid}/evidence/{evidence_type} | Get DocumentSubmission Evidence |


<a id="createDocumentSubmission"></a>
# **createDocumentSubmission**
> DocumentSubmissionResult createDocumentSubmission(documentSubmission)

Submit a new document.

Submit a document for delivery. This endpoint will replaces the /invoice_submissions endpoint which will soon be deprecated.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentSubmissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.storecove.com/api/v2");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DocumentSubmissionsApi apiInstance = new DocumentSubmissionsApi(defaultClient);
    DocumentSubmission documentSubmission = new DocumentSubmission(); // DocumentSubmission | Document to submit
    try {
      DocumentSubmissionResult result = apiInstance.createDocumentSubmission(documentSubmission);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentSubmissionsApi#createDocumentSubmission");
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
| **documentSubmission** | [**DocumentSubmission**](DocumentSubmission.md)| Document to submit | |

### Return type

[**DocumentSubmissionResult**](DocumentSubmissionResult.md)

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
| **422** | Unprocessable Entity |  -  |

<a id="showDocumentSubmissionEvidence"></a>
# **showDocumentSubmissionEvidence**
> DocumentSubmissionEvidence showDocumentSubmissionEvidence(guid, evidenceType)

Get DocumentSubmission Evidence

Get evidence for a DocumentSubmission by GUID with corresponding status

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentSubmissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.storecove.com/api/v2");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DocumentSubmissionsApi apiInstance = new DocumentSubmissionsApi(defaultClient);
    UUID guid = UUID.randomUUID(); // UUID | DocumentSubmission GUID
    String evidenceType = "sending"; // String | Type of evidence requested
    try {
      DocumentSubmissionEvidence result = apiInstance.showDocumentSubmissionEvidence(guid, evidenceType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentSubmissionsApi#showDocumentSubmissionEvidence");
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
| **guid** | **UUID**| DocumentSubmission GUID | |
| **evidenceType** | **String**| Type of evidence requested | [default to sending] [enum: sending, clearing] |

### Return type

[**DocumentSubmissionEvidence**](DocumentSubmissionEvidence.md)

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

