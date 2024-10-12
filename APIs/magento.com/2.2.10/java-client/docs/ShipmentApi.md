# ShipmentApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesShipmentRepositoryV1SavePost**](ShipmentApi.md#salesShipmentRepositoryV1SavePost) | **POST** /V1/shipment/ | shipment/ |


<a id="salesShipmentRepositoryV1SavePost"></a>
# **salesShipmentRepositoryV1SavePost**
> SalesDataShipmentInterface salesShipmentRepositoryV1SavePost(salesShipmentRepositoryV1SavePostRequest)

shipment/

Performs persist operations for a specified shipment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShipmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ShipmentApi apiInstance = new ShipmentApi(defaultClient);
    SalesShipmentRepositoryV1SavePostRequest salesShipmentRepositoryV1SavePostRequest = new SalesShipmentRepositoryV1SavePostRequest(); // SalesShipmentRepositoryV1SavePostRequest | 
    try {
      SalesDataShipmentInterface result = apiInstance.salesShipmentRepositoryV1SavePost(salesShipmentRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShipmentApi#salesShipmentRepositoryV1SavePost");
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
| **salesShipmentRepositoryV1SavePostRequest** | [**SalesShipmentRepositoryV1SavePostRequest**](SalesShipmentRepositoryV1SavePostRequest.md)|  | [optional] |

### Return type

[**SalesDataShipmentInterface**](SalesDataShipmentInterface.md)

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

