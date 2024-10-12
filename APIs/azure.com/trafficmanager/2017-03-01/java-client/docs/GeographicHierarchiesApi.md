# GeographicHierarchiesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**geographicHierarchiesGetDefault**](GeographicHierarchiesApi.md#geographicHierarchiesGetDefault) | **GET** /providers/Microsoft.Network/trafficManagerGeographicHierarchies/default |  |


<a id="geographicHierarchiesGetDefault"></a>
# **geographicHierarchiesGetDefault**
> TrafficManagerGeographicHierarchy geographicHierarchiesGetDefault(apiVersion)



Gets the default Geographic Hierarchy used by the Geographic traffic routing method.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeographicHierarchiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    GeographicHierarchiesApi apiInstance = new GeographicHierarchiesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      TrafficManagerGeographicHierarchy result = apiInstance.geographicHierarchiesGetDefault(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeographicHierarchiesApi#geographicHierarchiesGetDefault");
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
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**TrafficManagerGeographicHierarchy**](TrafficManagerGeographicHierarchy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The default Geographic Hierarchy. |  -  |
| **0** | Default response. It will be deserialized as per the Error definition. |  -  |

