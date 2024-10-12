# AnalyticsApi

All URIs are relative to *http://config2.gamesparks.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAnalyticsDataUsingGET**](AnalyticsApi.md#getAnalyticsDataUsingGET) | **GET** /restv2/game/{apiKey}/admin/analytics | Returns the results of executed query defined by the parameters passed in |
| [**getDataCountUsingGET**](AnalyticsApi.md#getDataCountUsingGET) | **GET** /restv2/game/{apiKey}/admin/analytics/count | Returns the count of executed query |
| [**getRetentionUsingGET**](AnalyticsApi.md#getRetentionUsingGET) | **GET** /restv2/game/{apiKey}/admin/analytics/rollingRetention | Returns the percentage of user retention over the last 30 days |


<a id="getAnalyticsDataUsingGET"></a>
# **getAnalyticsDataUsingGET**
> List&lt;AnalyticsDataSwaggerModel&gt; getAnalyticsDataUsingGET(apiKey, stage, dataType, precision, startDate, endDate, keys)

Returns the results of executed query defined by the parameters passed in

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    String stage = "LIVE"; // String | stage
    String dataType = "activeDevices"; // String | dataType
    String precision = "HOURLY"; // String | precision
    LocalDate startDate = LocalDate.now(); // LocalDate | yyyy-MM-dd
    LocalDate endDate = LocalDate.now(); // LocalDate | yyyy-MM-dd
    String keys = "keys_example"; // String | the keys to select. For example \"ReturningUsers\", \"NewUsers\", etc
    try {
      List<AnalyticsDataSwaggerModel> result = apiInstance.getAnalyticsDataUsingGET(apiKey, stage, dataType, precision, startDate, endDate, keys);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#getAnalyticsDataUsingGET");
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
| **apiKey** | **String**| apiKey | |
| **stage** | **String**| stage | [enum: LIVE, PREVIEW] |
| **dataType** | **String**| dataType | [enum: activeDevices, activeLocations, activeUsers, averageBandwidthPerUser, averageDauOverMau, averageJsExecutionTime, averageRequestsPerUser, averageResponseTime, averageResponseTimePerType, scriptLogLevelsCount, sessionAnalytic, storagePerUser, customAnalyticTotal, customAnalyticUser, timedAnalyticTotal, sessionAnalyticTotal, connectedUsers] |
| **precision** | **String**| precision | [enum: HOURLY, DAILY, MONTHLY] |
| **startDate** | **LocalDate**| yyyy-MM-dd | |
| **endDate** | **LocalDate**| yyyy-MM-dd | |
| **keys** | **String**| the keys to select. For example \&quot;ReturningUsers\&quot;, \&quot;NewUsers\&quot;, etc | [optional] |

### Return type

[**List&lt;AnalyticsDataSwaggerModel&gt;**](AnalyticsDataSwaggerModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="getDataCountUsingGET"></a>
# **getDataCountUsingGET**
> AnalyticsDataCountSwaggerModel getDataCountUsingGET(apiKey, stage, queryName)

Returns the count of executed query

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    String stage = "LIVE"; // String | stage
    String queryName = "activeUsersNow"; // String | queryName
    try {
      AnalyticsDataCountSwaggerModel result = apiInstance.getDataCountUsingGET(apiKey, stage, queryName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#getDataCountUsingGET");
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
| **apiKey** | **String**| apiKey | |
| **stage** | **String**| stage | [enum: LIVE, PREVIEW] |
| **queryName** | **String**| queryName | [enum: activeUsersNow, dailyActiveUsers, averageDailyActiveUsers, lastMonthlyActiveUsers, monthlyActiveUsers, averageSessionDuration] |

### Return type

[**AnalyticsDataCountSwaggerModel**](AnalyticsDataCountSwaggerModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="getRetentionUsingGET"></a>
# **getRetentionUsingGET**
> AnalyticsDataCountSwaggerModel getRetentionUsingGET(apiKey, stage)

Returns the percentage of user retention over the last 30 days

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    String stage = "LIVE"; // String | stage
    try {
      AnalyticsDataCountSwaggerModel result = apiInstance.getRetentionUsingGET(apiKey, stage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#getRetentionUsingGET");
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
| **apiKey** | **String**| apiKey | |
| **stage** | **String**| stage | [enum: LIVE, PREVIEW] |

### Return type

[**AnalyticsDataCountSwaggerModel**](AnalyticsDataCountSwaggerModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

