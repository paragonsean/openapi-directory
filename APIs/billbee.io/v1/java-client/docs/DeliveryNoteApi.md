# DeliveryNoteApi

All URIs are relative to *https://app.billbee.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**orderApiCreateDeliveryNote_0**](DeliveryNoteApi.md#orderApiCreateDeliveryNote_0) | **POST** /api/v1/orders/CreateDeliveryNote/{id} | Create an delivery note for an existing order. This request is extra throttled by order and api key to a maximum of 1 per 5 minutes. |


<a id="orderApiCreateDeliveryNote_0"></a>
# **orderApiCreateDeliveryNote_0**
> Object orderApiCreateDeliveryNote_0(id, includePdf, sendToCloudId)

Create an delivery note for an existing order. This request is extra throttled by order and api key to a maximum of 1 per 5 minutes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeliveryNoteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    DeliveryNoteApi apiInstance = new DeliveryNoteApi(defaultClient);
    Long id = 56L; // Long | The internal billbee id of the order
    Boolean includePdf = true; // Boolean | If true, the PDF is included in the response as base64 encoded string
    Long sendToCloudId = 56L; // Long | Optionally specify the id of a billbee connected cloud device to send the pdf to
    try {
      Object result = apiInstance.orderApiCreateDeliveryNote_0(id, includePdf, sendToCloudId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeliveryNoteApi#orderApiCreateDeliveryNote_0");
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
| **id** | **Long**| The internal billbee id of the order | |
| **includePdf** | **Boolean**| If true, the PDF is included in the response as base64 encoded string | [optional] |
| **sendToCloudId** | **Long**| Optionally specify the id of a billbee connected cloud device to send the pdf to | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

