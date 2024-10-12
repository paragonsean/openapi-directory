# InvoicesIdVoidApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesInvoiceManagementV1SetVoidPost**](InvoicesIdVoidApi.md#salesInvoiceManagementV1SetVoidPost) | **POST** /V1/invoices/{id}/void | invoices/{id}/void |


<a id="salesInvoiceManagementV1SetVoidPost"></a>
# **salesInvoiceManagementV1SetVoidPost**
> Boolean salesInvoiceManagementV1SetVoidPost(id)

invoices/{id}/void

Voids a specified invoice.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesIdVoidApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    InvoicesIdVoidApi apiInstance = new InvoicesIdVoidApi(defaultClient);
    Integer id = 56; // Integer | The invoice ID.
    try {
      Boolean result = apiInstance.salesInvoiceManagementV1SetVoidPost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesIdVoidApi#salesInvoiceManagementV1SetVoidPost");
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
| **id** | **Integer**| The invoice ID. | |

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

