# CloudUtilizationApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**doCloudOutForecast**](CloudUtilizationApi.md#doCloudOutForecast) | **POST** /cloud_utilization/cloud_out_forecast | Forecast of the cloud utilization for CloudOut |


<a id="doCloudOutForecast"></a>
# **doCloudOutForecast**
> CloudOutForecastSummary doCloudOutForecast(cloudOutForecastRequest)

Forecast of the cloud utilization for CloudOut

Forecast of the cloud storage and compute utilization on cloud archival location according to the SLA Domain parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CloudUtilizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    CloudUtilizationApi apiInstance = new CloudUtilizationApi(defaultClient);
    CloudOutForecastRequest cloudOutForecastRequest = new CloudOutForecastRequest(); // CloudOutForecastRequest | Object that contains the CloudOut forecast request.
    try {
      CloudOutForecastSummary result = apiInstance.doCloudOutForecast(cloudOutForecastRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudUtilizationApi#doCloudOutForecast");
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
| **cloudOutForecastRequest** | [**CloudOutForecastRequest**](CloudOutForecastRequest.md)| Object that contains the CloudOut forecast request. | |

### Return type

[**CloudOutForecastSummary**](CloudOutForecastSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Object that contains the CloudOut forecast summary. |  -  |

