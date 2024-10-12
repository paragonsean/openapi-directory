# InvoiceInvoiceIdRefundApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesRefundInvoiceV1ExecutePost**](InvoiceInvoiceIdRefundApi.md#salesRefundInvoiceV1ExecutePost) | **POST** /V1/invoice/{invoiceId}/refund | invoice/{invoiceId}/refund |


<a id="salesRefundInvoiceV1ExecutePost"></a>
# **salesRefundInvoiceV1ExecutePost**
> Integer salesRefundInvoiceV1ExecutePost(invoiceId, salesRefundInvoiceV1ExecutePostRequest)

invoice/{invoiceId}/refund

Create refund for invoice

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceInvoiceIdRefundApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    InvoiceInvoiceIdRefundApi apiInstance = new InvoiceInvoiceIdRefundApi(defaultClient);
    Integer invoiceId = 56; // Integer | 
    SalesRefundInvoiceV1ExecutePostRequest salesRefundInvoiceV1ExecutePostRequest = new SalesRefundInvoiceV1ExecutePostRequest(); // SalesRefundInvoiceV1ExecutePostRequest | 
    try {
      Integer result = apiInstance.salesRefundInvoiceV1ExecutePost(invoiceId, salesRefundInvoiceV1ExecutePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceInvoiceIdRefundApi#salesRefundInvoiceV1ExecutePost");
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
| **invoiceId** | **Integer**|  | |
| **salesRefundInvoiceV1ExecutePostRequest** | [**SalesRefundInvoiceV1ExecutePostRequest**](SalesRefundInvoiceV1ExecutePostRequest.md)|  | [optional] |

### Return type

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

