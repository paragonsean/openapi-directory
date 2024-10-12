# CurrentApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkSensorAlertsCurrentOverviewByMetric_2**](CurrentApi.md#getNetworkSensorAlertsCurrentOverviewByMetric_2) | **GET** /networks/{networkId}/sensor/alerts/current/overview/byMetric | Return an overview of currently alerting sensors by metric |


<a id="getNetworkSensorAlertsCurrentOverviewByMetric_2"></a>
# **getNetworkSensorAlertsCurrentOverviewByMetric_2**
> GetNetworkSensorAlertsCurrentOverviewByMetric200Response getNetworkSensorAlertsCurrentOverviewByMetric_2(networkId)

Return an overview of currently alerting sensors by metric

Return an overview of currently alerting sensors by metric

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CurrentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CurrentApi apiInstance = new CurrentApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      GetNetworkSensorAlertsCurrentOverviewByMetric200Response result = apiInstance.getNetworkSensorAlertsCurrentOverviewByMetric_2(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CurrentApi#getNetworkSensorAlertsCurrentOverviewByMetric_2");
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
| **networkId** | **String**|  | |

### Return type

[**GetNetworkSensorAlertsCurrentOverviewByMetric200Response**](GetNetworkSensorAlertsCurrentOverviewByMetric200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

