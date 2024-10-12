# Class21UserStatisticsOptionalApi

All URIs are relative to *https://api.telematicssdk.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**userStatisticeDailyValueV1StatisticsIndividualDaily_0**](Class21UserStatisticsOptionalApi.md#userStatisticeDailyValueV1StatisticsIndividualDaily_0) | **GET** /statistics/v1/Statistics/individual/daily/ | User statistice - Daily value - v1/Statistics/individual/daily |
| [**userStatisticsAccumulatedValueV1StatisticsIndividual_0**](Class21UserStatisticsOptionalApi.md#userStatisticsAccumulatedValueV1StatisticsIndividual_0) | **GET** /statistics/v1/Statistics/individual/ | User statistics - Accumulated value - /v1/Statistics/individual |


<a id="userStatisticeDailyValueV1StatisticsIndividualDaily_0"></a>
# **userStatisticeDailyValueV1StatisticsIndividualDaily_0**
> UserStatisticeDailyValueV1StatisticsIndividualDaily200Response userStatisticeDailyValueV1StatisticsIndividualDaily_0(startDate, endDate)

User statistice - Daily value - v1/Statistics/individual/daily

User statistice - Daily value - v1/Statistics/individual/daily

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class21UserStatisticsOptionalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.telematicssdk.com");

    Class21UserStatisticsOptionalApi apiInstance = new Class21UserStatisticsOptionalApi(defaultClient);
    String startDate = "2021-03-30"; // String | 
    String endDate = "2021-03-30"; // String | 
    try {
      UserStatisticeDailyValueV1StatisticsIndividualDaily200Response result = apiInstance.userStatisticeDailyValueV1StatisticsIndividualDaily_0(startDate, endDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class21UserStatisticsOptionalApi#userStatisticeDailyValueV1StatisticsIndividualDaily_0");
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
| **startDate** | **String**|  | [optional] |
| **endDate** | **String**|  | [optional] |

### Return type

[**UserStatisticeDailyValueV1StatisticsIndividualDaily200Response**](UserStatisticeDailyValueV1StatisticsIndividualDaily200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  * Content-Length -  <br>  * Date -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * X-Powered-By -  <br>  * X-StackifyID -  <br>  |

<a id="userStatisticsAccumulatedValueV1StatisticsIndividual_0"></a>
# **userStatisticsAccumulatedValueV1StatisticsIndividual_0**
> UserStatisticsAccumulatedValueV1StatisticsIndividual200Response userStatisticsAccumulatedValueV1StatisticsIndividual_0(startDate, endDate)

User statistics - Accumulated value - /v1/Statistics/individual

User statistics - Accumulated value - /v1/Statistics/individual

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class21UserStatisticsOptionalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.telematicssdk.com");

    Class21UserStatisticsOptionalApi apiInstance = new Class21UserStatisticsOptionalApi(defaultClient);
    String startDate = "2021-01-01"; // String | 
    String endDate = "2021-01-30"; // String | 
    try {
      UserStatisticsAccumulatedValueV1StatisticsIndividual200Response result = apiInstance.userStatisticsAccumulatedValueV1StatisticsIndividual_0(startDate, endDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class21UserStatisticsOptionalApi#userStatisticsAccumulatedValueV1StatisticsIndividual_0");
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
| **startDate** | **String**|  | [optional] |
| **endDate** | **String**|  | [optional] |

### Return type

[**UserStatisticsAccumulatedValueV1StatisticsIndividual200Response**](UserStatisticsAccumulatedValueV1StatisticsIndividual200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  * Content-Length -  <br>  * Date -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * X-Powered-By -  <br>  * X-StackifyID -  <br>  |

