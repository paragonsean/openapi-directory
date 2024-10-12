# InvoiceEmailsApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getOneInvoiceEmails**](InvoiceEmailsApi.md#getOneInvoiceEmails) | **GET** /invoices/{invoice_id}/emails/{email_id} | Get an invoice emails |


<a id="getOneInvoiceEmails"></a>
# **getOneInvoiceEmails**
> GetOneInvoiceEmails200Response getOneInvoiceEmails(invoiceId, emailId)

Get an invoice emails

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceEmailsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");

    InvoiceEmailsApi apiInstance = new InvoiceEmailsApi(defaultClient);
    UUID invoiceId = UUID.randomUUID(); // UUID | 
    UUID emailId = UUID.randomUUID(); // UUID | 
    try {
      GetOneInvoiceEmails200Response result = apiInstance.getOneInvoiceEmails(invoiceId, emailId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceEmailsApi#getOneInvoiceEmails");
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
| **invoiceId** | **UUID**|  | |
| **emailId** | **UUID**|  | |

### Return type

[**GetOneInvoiceEmails200Response**](GetOneInvoiceEmails200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not found |  -  |

