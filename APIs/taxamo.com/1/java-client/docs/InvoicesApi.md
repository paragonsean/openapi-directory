# InvoicesApi

All URIs are relative to *https://api.taxamo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**emailInvoice**](InvoicesApi.md#emailInvoice) | **POST** /api/v1/transactions/{key}/invoice/send_email | Email invoice |
| [**emailRefund**](InvoicesApi.md#emailRefund) | **POST** /api/v1/transactions/{key}/invoice/refunds/{refund_note_number}/send_email | Email credit note |


<a id="emailInvoice"></a>
# **emailInvoice**
> EmailInvoiceOut emailInvoice(key, input)

Email invoice

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taxamo.com");

    InvoicesApi apiInstance = new InvoicesApi(defaultClient);
    String key = "key_example"; // String | Transaction key.
    EmailInvoiceIn input = new EmailInvoiceIn(); // EmailInvoiceIn | Input
    try {
      EmailInvoiceOut result = apiInstance.emailInvoice(key, input);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesApi#emailInvoice");
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
| **key** | **String**| Transaction key. | |
| **input** | [**EmailInvoiceIn**](EmailInvoiceIn.md)| Input | |

### Return type

[**EmailInvoiceOut**](EmailInvoiceOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Validation failed, see JSON body response for details. |  -  |
| **401** | Incorrect token |  -  |

<a id="emailRefund"></a>
# **emailRefund**
> EmailRefundOut emailRefund(key, refundNoteNumber, input)

Email credit note

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taxamo.com");

    InvoicesApi apiInstance = new InvoicesApi(defaultClient);
    String key = "key_example"; // String | Transaction key.
    String refundNoteNumber = "refundNoteNumber_example"; // String | Refund note id.
    EmailRefundIn input = new EmailRefundIn(); // EmailRefundIn | Input
    try {
      EmailRefundOut result = apiInstance.emailRefund(key, refundNoteNumber, input);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesApi#emailRefund");
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
| **key** | **String**| Transaction key. | |
| **refundNoteNumber** | **String**| Refund note id. | |
| **input** | [**EmailRefundIn**](EmailRefundIn.md)| Input | |

### Return type

[**EmailRefundOut**](EmailRefundOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Validation failed, see JSON body response for details. |  -  |
| **401** | Incorrect token |  -  |

