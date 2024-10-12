# InvoicesIdCaptureApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesInvoiceManagementV1SetCapturePost**](InvoicesIdCaptureApi.md#salesInvoiceManagementV1SetCapturePost) | **POST** /V1/invoices/{id}/capture | invoices/{id}/capture |


<a id="salesInvoiceManagementV1SetCapturePost"></a>
# **salesInvoiceManagementV1SetCapturePost**
> String salesInvoiceManagementV1SetCapturePost(id)

invoices/{id}/capture

Sets invoice capture.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesIdCaptureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    InvoicesIdCaptureApi apiInstance = new InvoicesIdCaptureApi(defaultClient);
    Integer id = 56; // Integer | 
    try {
      String result = apiInstance.salesInvoiceManagementV1SetCapturePost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesIdCaptureApi#salesInvoiceManagementV1SetCapturePost");
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
| **id** | **Integer**|  | |

### Return type

**String**

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

