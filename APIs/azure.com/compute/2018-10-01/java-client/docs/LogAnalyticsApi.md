# LogAnalyticsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**logAnalyticsExportRequestRateByInterval**](LogAnalyticsApi.md#logAnalyticsExportRequestRateByInterval) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/logAnalytics/apiAccess/getRequestRateByInterval |  |
| [**logAnalyticsExportThrottledRequests**](LogAnalyticsApi.md#logAnalyticsExportThrottledRequests) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/logAnalytics/apiAccess/getThrottledRequests |  |


<a id="logAnalyticsExportRequestRateByInterval"></a>
# **logAnalyticsExportRequestRateByInterval**
> LogAnalyticsOperationResult logAnalyticsExportRequestRateByInterval(location, apiVersion, subscriptionId, parameters)



Export logs that show Api requests made by this subscription in the given time window to show throttling activities.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LogAnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LogAnalyticsApi apiInstance = new LogAnalyticsApi(defaultClient);
    String location = "location_example"; // String | The location upon which virtual-machine-sizes is queried.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    RequestRateByIntervalInput parameters = new RequestRateByIntervalInput(); // RequestRateByIntervalInput | Parameters supplied to the LogAnalytics getRequestRateByInterval Api.
    try {
      LogAnalyticsOperationResult result = apiInstance.logAnalyticsExportRequestRateByInterval(location, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogAnalyticsApi#logAnalyticsExportRequestRateByInterval");
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
| **location** | **String**| The location upon which virtual-machine-sizes is queried. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**RequestRateByIntervalInput**](RequestRateByIntervalInput.md)| Parameters supplied to the LogAnalytics getRequestRateByInterval Api. | |

### Return type

[**LogAnalyticsOperationResult**](LogAnalyticsOperationResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |

<a id="logAnalyticsExportThrottledRequests"></a>
# **logAnalyticsExportThrottledRequests**
> LogAnalyticsOperationResult logAnalyticsExportThrottledRequests(location, apiVersion, subscriptionId, parameters)



Export logs that show total throttled Api requests for this subscription in the given time window.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LogAnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LogAnalyticsApi apiInstance = new LogAnalyticsApi(defaultClient);
    String location = "location_example"; // String | The location upon which virtual-machine-sizes is queried.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    ThrottledRequestsInput parameters = new ThrottledRequestsInput(); // ThrottledRequestsInput | Parameters supplied to the LogAnalytics getThrottledRequests Api.
    try {
      LogAnalyticsOperationResult result = apiInstance.logAnalyticsExportThrottledRequests(location, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogAnalyticsApi#logAnalyticsExportThrottledRequests");
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
| **location** | **String**| The location upon which virtual-machine-sizes is queried. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**ThrottledRequestsInput**](ThrottledRequestsInput.md)| Parameters supplied to the LogAnalytics getThrottledRequests Api. | |

### Return type

[**LogAnalyticsOperationResult**](LogAnalyticsOperationResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |

