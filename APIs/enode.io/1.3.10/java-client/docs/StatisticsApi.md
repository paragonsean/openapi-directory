# StatisticsApi

All URIs are relative to *https://api.test.enode.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getStatisticsCharging**](StatisticsApi.md#getStatisticsCharging) | **GET** /statistics/charging | Get User Charging Statistics |


<a id="getStatisticsCharging"></a>
# **getStatisticsCharging**
> List&lt;GetStatisticsCharging200ResponseInner&gt; getStatisticsCharging(startDate, resolution, endDate, vehicleId, chargingLocationId)

Get User Charging Statistics

Returns a normalized timeseries of statistics about power consumption and price for the User.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.enode.io");
    
    // Configure OAuth2 access token for authorization: UserAccessToken
    OAuth UserAccessToken = (OAuth) defaultClient.getAuthentication("UserAccessToken");
    UserAccessToken.setAccessToken("YOUR ACCESS TOKEN");

    StatisticsApi apiInstance = new StatisticsApi(defaultClient);
    LocalDate startDate = LocalDate.now(); // LocalDate | Earliest date to include in the response
    String resolution = "HOUR"; // String | The unit of time the data will be cut into before aggregate statistics are applied. For instance if you choose DAY, then each item in the returned array will cover 1 day.
    LocalDate endDate = LocalDate.now(); // LocalDate | Latest date to include in the response (defaults to current date/time)
    String vehicleId = "vehicleId_example"; // String | Filter statistics to only include this vehicle
    String chargingLocationId = "chargingLocationId_example"; // String | Filter statistics to only include this charging location
    try {
      List<GetStatisticsCharging200ResponseInner> result = apiInstance.getStatisticsCharging(startDate, resolution, endDate, vehicleId, chargingLocationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatisticsApi#getStatisticsCharging");
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
| **startDate** | **LocalDate**| Earliest date to include in the response | |
| **resolution** | **String**| The unit of time the data will be cut into before aggregate statistics are applied. For instance if you choose DAY, then each item in the returned array will cover 1 day. | [optional] [default to DAY] [enum: HOUR, DAY, WEEK, MONTH, YEAR] |
| **endDate** | **LocalDate**| Latest date to include in the response (defaults to current date/time) | [optional] |
| **vehicleId** | **String**| Filter statistics to only include this vehicle | [optional] |
| **chargingLocationId** | **String**| Filter statistics to only include this charging location | [optional] |

### Return type

[**List&lt;GetStatisticsCharging200ResponseInner&gt;**](GetStatisticsCharging200ResponseInner.md)

### Authorization

[UserAccessToken](../README.md#UserAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful |  -  |

