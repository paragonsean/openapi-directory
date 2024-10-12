# ReportsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**reportsGetLatencyScorecards**](ReportsApi.md#reportsGetLatencyScorecards) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/NetworkExperimentProfiles/{profileName}/Experiments/{experimentName}/LatencyScorecard | Gets a Latency Scorecard for a given Experiment |
| [**reportsGetTimeseries**](ReportsApi.md#reportsGetTimeseries) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/NetworkExperimentProfiles/{profileName}/Experiments/{experimentName}/Timeseries | Gets a Timeseries for a given Experiment |


<a id="reportsGetLatencyScorecards"></a>
# **reportsGetLatencyScorecards**
> LatencyScorecard reportsGetLatencyScorecards(subscriptionId, apiVersion, resourceGroupName, profileName, experimentName, aggregationInterval, endDateTimeUTC, country)

Gets a Latency Scorecard for a given Experiment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String profileName = "profileName_example"; // String | The Profile identifier associated with the Tenant and Partner
    String experimentName = "experimentName_example"; // String | The Experiment identifier associated with the Experiment
    String aggregationInterval = "Daily"; // String | The aggregation interval of the Latency Scorecard
    String endDateTimeUTC = "endDateTimeUTC_example"; // String | The end DateTime of the Latency Scorecard in UTC
    String country = "country_example"; // String | The country associated with the Latency Scorecard. Values are country ISO codes as specified here- https://www.iso.org/iso-3166-country-codes.html
    try {
      LatencyScorecard result = apiInstance.reportsGetLatencyScorecards(subscriptionId, apiVersion, resourceGroupName, profileName, experimentName, aggregationInterval, endDateTimeUTC, country);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportsGetLatencyScorecards");
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
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API version. | |
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **profileName** | **String**| The Profile identifier associated with the Tenant and Partner | |
| **experimentName** | **String**| The Experiment identifier associated with the Experiment | |
| **aggregationInterval** | **String**| The aggregation interval of the Latency Scorecard | [enum: Daily, Weekly, Monthly] |
| **endDateTimeUTC** | **String**| The end DateTime of the Latency Scorecard in UTC | [optional] |
| **country** | **String**| The country associated with the Latency Scorecard. Values are country ISO codes as specified here- https://www.iso.org/iso-3166-country-codes.html | [optional] |

### Return type

[**LatencyScorecard**](LatencyScorecard.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="reportsGetTimeseries"></a>
# **reportsGetTimeseries**
> Timeseries reportsGetTimeseries(subscriptionId, apiVersion, resourceGroupName, profileName, experimentName, startDateTimeUTC, endDateTimeUTC, aggregationInterval, timeseriesType, endpoint, country)

Gets a Timeseries for a given Experiment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String profileName = "profileName_example"; // String | The Profile identifier associated with the Tenant and Partner
    String experimentName = "experimentName_example"; // String | The Experiment identifier associated with the Experiment
    OffsetDateTime startDateTimeUTC = OffsetDateTime.now(); // OffsetDateTime | The start DateTime of the Timeseries in UTC
    OffsetDateTime endDateTimeUTC = OffsetDateTime.now(); // OffsetDateTime | The end DateTime of the Timeseries in UTC
    String aggregationInterval = "Hourly"; // String | The aggregation interval of the Timeseries
    String timeseriesType = "MeasurementCounts"; // String | The type of Timeseries
    String endpoint = "endpoint_example"; // String | The specific endpoint
    String country = "country_example"; // String | The country associated with the Timeseries. Values are country ISO codes as specified here- https://www.iso.org/iso-3166-country-codes.html
    try {
      Timeseries result = apiInstance.reportsGetTimeseries(subscriptionId, apiVersion, resourceGroupName, profileName, experimentName, startDateTimeUTC, endDateTimeUTC, aggregationInterval, timeseriesType, endpoint, country);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportsGetTimeseries");
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
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API version. | |
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **profileName** | **String**| The Profile identifier associated with the Tenant and Partner | |
| **experimentName** | **String**| The Experiment identifier associated with the Experiment | |
| **startDateTimeUTC** | **OffsetDateTime**| The start DateTime of the Timeseries in UTC | |
| **endDateTimeUTC** | **OffsetDateTime**| The end DateTime of the Timeseries in UTC | |
| **aggregationInterval** | **String**| The aggregation interval of the Timeseries | [enum: Hourly, Daily] |
| **timeseriesType** | **String**| The type of Timeseries | [enum: MeasurementCounts, LatencyP50, LatencyP75, LatencyP95] |
| **endpoint** | **String**| The specific endpoint | [optional] |
| **country** | **String**| The country associated with the Timeseries. Values are country ISO codes as specified here- https://www.iso.org/iso-3166-country-codes.html | [optional] |

### Return type

[**Timeseries**](Timeseries.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | Error response describing why the operation failed. |  -  |

