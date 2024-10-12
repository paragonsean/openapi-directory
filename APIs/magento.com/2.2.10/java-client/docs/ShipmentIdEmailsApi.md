# ShipmentIdEmailsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesShipmentManagementV1NotifyPost**](ShipmentIdEmailsApi.md#salesShipmentManagementV1NotifyPost) | **POST** /V1/shipment/{id}/emails | shipment/{id}/emails |


<a id="salesShipmentManagementV1NotifyPost"></a>
# **salesShipmentManagementV1NotifyPost**
> Boolean salesShipmentManagementV1NotifyPost(id)

shipment/{id}/emails

Emails user a specified shipment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShipmentIdEmailsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ShipmentIdEmailsApi apiInstance = new ShipmentIdEmailsApi(defaultClient);
    Integer id = 56; // Integer | The shipment ID.
    try {
      Boolean result = apiInstance.salesShipmentManagementV1NotifyPost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShipmentIdEmailsApi#salesShipmentManagementV1NotifyPost");
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
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

