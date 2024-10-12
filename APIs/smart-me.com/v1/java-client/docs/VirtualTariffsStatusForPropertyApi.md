# VirtualTariffsStatusForPropertyApi

All URIs are relative to *https://smart-me.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**virtualTariffsStatusForPropertyGet**](VirtualTariffsStatusForPropertyApi.md#virtualTariffsStatusForPropertyGet) | **GET** /api/VirtualTariffsStatusForProperty/{id} | Gets the calculation status for a virtual tariff property |


<a id="virtualTariffsStatusForPropertyGet"></a>
# **virtualTariffsStatusForPropertyGet**
> String virtualTariffsStatusForPropertyGet(id)

Gets the calculation status for a virtual tariff property

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualTariffsStatusForPropertyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    VirtualTariffsStatusForPropertyApi apiInstance = new VirtualTariffsStatusForPropertyApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      String result = apiInstance.virtualTariffsStatusForPropertyGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualTariffsStatusForPropertyApi#virtualTariffsStatusForPropertyGet");
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
| **id** | **String**|  | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

