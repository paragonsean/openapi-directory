# ByMetricApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkSensorAlertsCurrentOverviewByMetric_4**](ByMetricApi.md#getNetworkSensorAlertsCurrentOverviewByMetric_4) | **GET** /networks/{networkId}/sensor/alerts/current/overview/byMetric | Return an overview of currently alerting sensors by metric |
| [**getNetworkSensorAlertsOverviewByMetric_3**](ByMetricApi.md#getNetworkSensorAlertsOverviewByMetric_3) | **GET** /networks/{networkId}/sensor/alerts/overview/byMetric | Return an overview of alert occurrences over a timespan, by metric |


<a id="getNetworkSensorAlertsCurrentOverviewByMetric_4"></a>
# **getNetworkSensorAlertsCurrentOverviewByMetric_4**
> GetNetworkSensorAlertsCurrentOverviewByMetric200Response getNetworkSensorAlertsCurrentOverviewByMetric_4(networkId)

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
import org.openapitools.client.api.ByMetricApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ByMetricApi apiInstance = new ByMetricApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      GetNetworkSensorAlertsCurrentOverviewByMetric200Response result = apiInstance.getNetworkSensorAlertsCurrentOverviewByMetric_4(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ByMetricApi#getNetworkSensorAlertsCurrentOverviewByMetric_4");
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

<a id="getNetworkSensorAlertsOverviewByMetric_3"></a>
# **getNetworkSensorAlertsOverviewByMetric_3**
> List&lt;GetNetworkSensorAlertsOverviewByMetric200ResponseInner&gt; getNetworkSensorAlertsOverviewByMetric_3(networkId, t0, t1, timespan, interval)

Return an overview of alert occurrences over a timespan, by metric

Return an overview of alert occurrences over a timespan, by metric

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ByMetricApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ByMetricApi apiInstance = new ByMetricApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
    Integer interval = 56; // Integer | The time interval in seconds for returned data. The valid intervals are: 86400, 604800. The default is 604800.
    try {
      List<GetNetworkSensorAlertsOverviewByMetric200ResponseInner> result = apiInstance.getNetworkSensorAlertsOverviewByMetric_3(networkId, t0, t1, timespan, interval);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ByMetricApi#getNetworkSensorAlertsOverviewByMetric_3");
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
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 365 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days. | [optional] |
| **interval** | **Integer**| The time interval in seconds for returned data. The valid intervals are: 86400, 604800. The default is 604800. | [optional] |

### Return type

[**List&lt;GetNetworkSensorAlertsOverviewByMetric200ResponseInner&gt;**](GetNetworkSensorAlertsOverviewByMetric200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

