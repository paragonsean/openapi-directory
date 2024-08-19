# HeatMapsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**heatMapGet**](HeatMapsApi.md#heatMapGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficmanagerprofiles/{profileName}/heatMaps/{heatMapType} |  |


<a id="heatMapGet"></a>
# **heatMapGet**
> HeatMapModel heatMapGet(subscriptionId, resourceGroupName, profileName, heatMapType, apiVersion, topLeft, botRight)



Gets latest heatmap for Traffic Manager profile.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HeatMapsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HeatMapsApi apiInstance = new HeatMapsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Traffic Manager endpoint.
    String profileName = "profileName_example"; // String | The name of the Traffic Manager profile.
    String heatMapType = "default"; // String | The type of HeatMap for the Traffic Manager profile.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    List<Double> topLeft = Arrays.asList(); // List<Double> | The top left latitude,longitude pair of the rectangular viewport to query for.
    List<Double> botRight = Arrays.asList(); // List<Double> | The bottom right latitude,longitude pair of the rectangular viewport to query for.
    try {
      HeatMapModel result = apiInstance.heatMapGet(subscriptionId, resourceGroupName, profileName, heatMapType, apiVersion, topLeft, botRight);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HeatMapsApi#heatMapGet");
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group containing the Traffic Manager endpoint. | |
| **profileName** | **String**| The name of the Traffic Manager profile. | |
| **heatMapType** | **String**| The type of HeatMap for the Traffic Manager profile. | [enum: default] |
| **apiVersion** | **String**| Client Api Version. | |
| **topLeft** | [**List&lt;Double&gt;**](Double.md)| The top left latitude,longitude pair of the rectangular viewport to query for. | [optional] |
| **botRight** | [**List&lt;Double&gt;**](Double.md)| The bottom right latitude,longitude pair of the rectangular viewport to query for. | [optional] |

### Return type

[**HeatMapModel**](HeatMapModel.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Traffic Manager heatmap. |  -  |
| **0** | Default response. It will be deserialized as per the Error definition. |  -  |

