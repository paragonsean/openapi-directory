# InvoicesIdCommentsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesInvoiceManagementV1GetCommentsListGet**](InvoicesIdCommentsApi.md#salesInvoiceManagementV1GetCommentsListGet) | **GET** /V1/invoices/{id}/comments | invoices/{id}/comments |


<a id="salesInvoiceManagementV1GetCommentsListGet"></a>
# **salesInvoiceManagementV1GetCommentsListGet**
> SalesDataInvoiceCommentSearchResultInterface salesInvoiceManagementV1GetCommentsListGet(id)

invoices/{id}/comments

Lists comments for a specified invoice.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesIdCommentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    InvoicesIdCommentsApi apiInstance = new InvoicesIdCommentsApi(defaultClient);
    Integer id = 56; // Integer | The invoice ID.
    try {
      SalesDataInvoiceCommentSearchResultInterface result = apiInstance.salesInvoiceManagementV1GetCommentsListGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesIdCommentsApi#salesInvoiceManagementV1GetCommentsListGet");
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

[**SalesDataInvoiceCommentSearchResultInterface**](SalesDataInvoiceCommentSearchResultInterface.md)

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

