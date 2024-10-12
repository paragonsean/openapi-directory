# TemandoRmaRmaIdShipmentsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**temandoShippingRmaRmaShipmentManagementV1AssignShipmentIdsPut**](TemandoRmaRmaIdShipmentsApi.md#temandoShippingRmaRmaShipmentManagementV1AssignShipmentIdsPut) | **PUT** /V1/temando/rma/{rmaId}/shipments | temando/rma/{rmaId}/shipments |


<a id="temandoShippingRmaRmaShipmentManagementV1AssignShipmentIdsPut"></a>
# **temandoShippingRmaRmaShipmentManagementV1AssignShipmentIdsPut**
> Integer temandoShippingRmaRmaShipmentManagementV1AssignShipmentIdsPut(rmaId, temandoShippingRmaRmaShipmentManagementV1AssignShipmentIdsPutRequest)

temando/rma/{rmaId}/shipments

Assign platform shipment IDs to a core RMA entity.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TemandoRmaRmaIdShipmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    TemandoRmaRmaIdShipmentsApi apiInstance = new TemandoRmaRmaIdShipmentsApi(defaultClient);
    Integer rmaId = 56; // Integer | 
    TemandoShippingRmaRmaShipmentManagementV1AssignShipmentIdsPutRequest temandoShippingRmaRmaShipmentManagementV1AssignShipmentIdsPutRequest = new TemandoShippingRmaRmaShipmentManagementV1AssignShipmentIdsPutRequest(); // TemandoShippingRmaRmaShipmentManagementV1AssignShipmentIdsPutRequest | 
    try {
      Integer result = apiInstance.temandoShippingRmaRmaShipmentManagementV1AssignShipmentIdsPut(rmaId, temandoShippingRmaRmaShipmentManagementV1AssignShipmentIdsPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TemandoRmaRmaIdShipmentsApi#temandoShippingRmaRmaShipmentManagementV1AssignShipmentIdsPut");
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
| **rmaId** | **Integer**|  | |
| **temandoShippingRmaRmaShipmentManagementV1AssignShipmentIdsPutRequest** | [**TemandoShippingRmaRmaShipmentManagementV1AssignShipmentIdsPutRequest**](TemandoShippingRmaRmaShipmentManagementV1AssignShipmentIdsPutRequest.md)|  | [optional] |

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
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

