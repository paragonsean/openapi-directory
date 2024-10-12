# InvoicesIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesInvoiceRepositoryV1GetGet**](InvoicesIdApi.md#salesInvoiceRepositoryV1GetGet) | **GET** /V1/invoices/{id} | invoices/{id} |


<a id="salesInvoiceRepositoryV1GetGet"></a>
# **salesInvoiceRepositoryV1GetGet**
> SalesDataInvoiceInterface salesInvoiceRepositoryV1GetGet(id)

invoices/{id}

Loads a specified invoice.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    InvoicesIdApi apiInstance = new InvoicesIdApi(defaultClient);
    Integer id = 56; // Integer | The invoice ID.
    try {
      SalesDataInvoiceInterface result = apiInstance.salesInvoiceRepositoryV1GetGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesIdApi#salesInvoiceRepositoryV1GetGet");
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

[**SalesDataInvoiceInterface**](SalesDataInvoiceInterface.md)

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

