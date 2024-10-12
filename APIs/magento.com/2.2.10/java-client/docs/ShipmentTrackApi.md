# ShipmentTrackApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesShipmentTrackRepositoryV1SavePost**](ShipmentTrackApi.md#salesShipmentTrackRepositoryV1SavePost) | **POST** /V1/shipment/track | shipment/track |


<a id="salesShipmentTrackRepositoryV1SavePost"></a>
# **salesShipmentTrackRepositoryV1SavePost**
> SalesDataShipmentTrackInterface salesShipmentTrackRepositoryV1SavePost(salesShipmentTrackRepositoryV1SavePostRequest)

shipment/track

Performs persist operations for a specified shipment track.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShipmentTrackApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ShipmentTrackApi apiInstance = new ShipmentTrackApi(defaultClient);
    SalesShipmentTrackRepositoryV1SavePostRequest salesShipmentTrackRepositoryV1SavePostRequest = new SalesShipmentTrackRepositoryV1SavePostRequest(); // SalesShipmentTrackRepositoryV1SavePostRequest | 
    try {
      SalesDataShipmentTrackInterface result = apiInstance.salesShipmentTrackRepositoryV1SavePost(salesShipmentTrackRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShipmentTrackApi#salesShipmentTrackRepositoryV1SavePost");
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
| **salesShipmentTrackRepositoryV1SavePostRequest** | [**SalesShipmentTrackRepositoryV1SavePostRequest**](SalesShipmentTrackRepositoryV1SavePostRequest.md)|  | [optional] |

### Return type

[**SalesDataShipmentTrackInterface**](SalesDataShipmentTrackInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

