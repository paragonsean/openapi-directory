# InvoicesIdEmailsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesInvoiceManagementV1NotifyPost**](InvoicesIdEmailsApi.md#salesInvoiceManagementV1NotifyPost) | **POST** /V1/invoices/{id}/emails | invoices/{id}/emails |


<a id="salesInvoiceManagementV1NotifyPost"></a>
# **salesInvoiceManagementV1NotifyPost**
> Boolean salesInvoiceManagementV1NotifyPost(id)

invoices/{id}/emails

Emails a user a specified invoice.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesIdEmailsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    InvoicesIdEmailsApi apiInstance = new InvoicesIdEmailsApi(defaultClient);
    Integer id = 56; // Integer | The invoice ID.
    try {
      Boolean result = apiInstance.salesInvoiceManagementV1NotifyPost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesIdEmailsApi#salesInvoiceManagementV1NotifyPost");
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

