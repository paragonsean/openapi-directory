# InvoiceSubmissionsApi

All URIs are relative to *https://api.storecove.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createInvoiceSubmission**](InvoiceSubmissionsApi.md#createInvoiceSubmission) | **POST** /invoice_submissions | Submit a new invoice |
| [**preflightInvoiceRecipient**](InvoiceSubmissionsApi.md#preflightInvoiceRecipient) | **POST** /invoice_submissions/preflight | DEPRECATED. Preflight an invoice recipient |
| [**showInvoiceSubmissionEvidence**](InvoiceSubmissionsApi.md#showInvoiceSubmissionEvidence) | **GET** /invoice_submissions/{guid}/evidence | DEPRECATED. Get InvoiceSubmission Evidence |


<a id="createInvoiceSubmission"></a>
# **createInvoiceSubmission**
> InvoiceSubmissionResult createInvoiceSubmission(invoiceSubmission)

Submit a new invoice

DEPRECATED. Use the new /document_submissions endpoint. Submit an invoice for delivery.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceSubmissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.storecove.com/api/v2");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    InvoiceSubmissionsApi apiInstance = new InvoiceSubmissionsApi(defaultClient);
    InvoiceSubmission invoiceSubmission = new InvoiceSubmission(); // InvoiceSubmission | Invoice to submit
    try {
      InvoiceSubmissionResult result = apiInstance.createInvoiceSubmission(invoiceSubmission);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceSubmissionsApi#createInvoiceSubmission");
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
| **invoiceSubmission** | [**InvoiceSubmission**](InvoiceSubmission.md)| Invoice to submit | |

### Return type

[**InvoiceSubmissionResult**](InvoiceSubmissionResult.md)

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

<a id="preflightInvoiceRecipient"></a>
# **preflightInvoiceRecipient**
> PreflightInvoiceRecipientResult preflightInvoiceRecipient(invoiceRecipientPreflight)

DEPRECATED. Preflight an invoice recipient

Deprecated. Use the new /discovery endpoint. Check whether Storecove can deliver an invoice for a list of ids.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceSubmissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.storecove.com/api/v2");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    InvoiceSubmissionsApi apiInstance = new InvoiceSubmissionsApi(defaultClient);
    InvoiceRecipientPreflight invoiceRecipientPreflight = new InvoiceRecipientPreflight(); // InvoiceRecipientPreflight | The invoice recipient to preflight
    try {
      PreflightInvoiceRecipientResult result = apiInstance.preflightInvoiceRecipient(invoiceRecipientPreflight);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceSubmissionsApi#preflightInvoiceRecipient");
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
| **invoiceRecipientPreflight** | [**InvoiceRecipientPreflight**](InvoiceRecipientPreflight.md)| The invoice recipient to preflight | |

### Return type

[**PreflightInvoiceRecipientResult**](PreflightInvoiceRecipientResult.md)

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

<a id="showInvoiceSubmissionEvidence"></a>
# **showInvoiceSubmissionEvidence**
> InvoiceSubmissionEvidence showInvoiceSubmissionEvidence(guid)

DEPRECATED. Get InvoiceSubmission Evidence

Deprecated. Use the new /document_submissions/{guid}/evidence endpoint. Get evidence for an InvoiceSubmission by GUID with corresponding status

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceSubmissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.storecove.com/api/v2");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    InvoiceSubmissionsApi apiInstance = new InvoiceSubmissionsApi(defaultClient);
    UUID guid = UUID.randomUUID(); // UUID | InvoiceSubmission GUID
    try {
      InvoiceSubmissionEvidence result = apiInstance.showInvoiceSubmissionEvidence(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceSubmissionsApi#showInvoiceSubmissionEvidence");
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
| **guid** | **UUID**| InvoiceSubmission GUID | |

### Return type

[**InvoiceSubmissionEvidence**](InvoiceSubmissionEvidence.md)

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

