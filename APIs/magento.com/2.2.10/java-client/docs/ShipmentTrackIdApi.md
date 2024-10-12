# ShipmentTrackIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesShipmentTrackRepositoryV1DeleteByIdDelete**](ShipmentTrackIdApi.md#salesShipmentTrackRepositoryV1DeleteByIdDelete) | **DELETE** /V1/shipment/track/{id} | shipment/track/{id} |


<a id="salesShipmentTrackRepositoryV1DeleteByIdDelete"></a>
# **salesShipmentTrackRepositoryV1DeleteByIdDelete**
> Boolean salesShipmentTrackRepositoryV1DeleteByIdDelete(id)

shipment/track/{id}

Deletes a specified shipment track by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShipmentTrackIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ShipmentTrackIdApi apiInstance = new ShipmentTrackIdApi(defaultClient);
    Integer id = 56; // Integer | The shipment track ID.
    try {
      Boolean result = apiInstance.salesShipmentTrackRepositoryV1DeleteByIdDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShipmentTrackIdApi#salesShipmentTrackRepositoryV1DeleteByIdDelete");
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
| **id** | **Integer**| The shipment track ID. | |

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
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

