# ShipmentIdLabelApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesShipmentManagementV1GetLabelGet**](ShipmentIdLabelApi.md#salesShipmentManagementV1GetLabelGet) | **GET** /V1/shipment/{id}/label | shipment/{id}/label |


<a id="salesShipmentManagementV1GetLabelGet"></a>
# **salesShipmentManagementV1GetLabelGet**
> String salesShipmentManagementV1GetLabelGet(id)

shipment/{id}/label

Gets a specified shipment label.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShipmentIdLabelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ShipmentIdLabelApi apiInstance = new ShipmentIdLabelApi(defaultClient);
    Integer id = 56; // Integer | The shipment label ID.
    try {
      String result = apiInstance.salesShipmentManagementV1GetLabelGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShipmentIdLabelApi#salesShipmentManagementV1GetLabelGet");
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
| **id** | **Integer**| The shipment label ID. | |

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

