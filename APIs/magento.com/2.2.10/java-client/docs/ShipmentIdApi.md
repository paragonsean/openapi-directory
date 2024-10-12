# ShipmentIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesShipmentRepositoryV1GetGet**](ShipmentIdApi.md#salesShipmentRepositoryV1GetGet) | **GET** /V1/shipment/{id} | shipment/{id} |


<a id="salesShipmentRepositoryV1GetGet"></a>
# **salesShipmentRepositoryV1GetGet**
> SalesDataShipmentInterface salesShipmentRepositoryV1GetGet(id)

shipment/{id}

Loads a specified shipment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShipmentIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ShipmentIdApi apiInstance = new ShipmentIdApi(defaultClient);
    Integer id = 56; // Integer | The shipment ID.
    try {
      SalesDataShipmentInterface result = apiInstance.salesShipmentRepositoryV1GetGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShipmentIdApi#salesShipmentRepositoryV1GetGet");
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
| **id** | **Integer**| The shipment ID. | |

### Return type

[**SalesDataShipmentInterface**](SalesDataShipmentInterface.md)

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

