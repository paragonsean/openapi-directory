# SessionAnalyticsApi

All URIs are relative to *https://rest.iad-01.braze.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appSessionsByTime_0**](SessionAnalyticsApi.md#appSessionsByTime_0) | **GET** /sessions/data_series | App Sessions by Time |


<a id="appSessionsByTime_0"></a>
# **appSessionsByTime_0**
> appSessionsByTime_0(length, unit, endingAt, appId, segmentId)

App Sessions by Time

This endpoint allows you to retrieve a series of the number of sessions for your app over a designated time period.  ### Components Used - [Segment Identifier](https://www.braze.com/docs/api/identifier_types/)  ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;data\&quot; : [         {             \&quot;time\&quot; : (string) point in time - as ISO 8601 extended when unit is \&quot;hour\&quot; and as ISO 8601 date when unit is \&quot;day\&quot;,             \&quot;sessions\&quot; : (int)         },         ...     ] } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SessionAnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.iad-01.braze.com");

    SessionAnalyticsApi apiInstance = new SessionAnalyticsApi(defaultClient);
    String length = "14"; // String | (Required) Integer  Max number of units (days or hours) before ending_at to include in the returned series - must be between 1 and 100 inclusive.
    String unit = "day"; // String | (Optional) String  Unit of time between data points - can be \"day\" or \"hour\" (defaults to \"day\"). 
    String endingAt = "2018-06-28T23:59:59-5:00"; // String | (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request.
    String appId = "{{app_identifier}}"; // String | (Optional) String  App API identifier retrieved from the Developer Console to limit analytics to a specific app.
    String segmentId = "{{segment_identifier}}"; // String | (Optional) String  Segment API identifier indicating the analytics enabled segment for which sessions should be returned.
    try {
      apiInstance.appSessionsByTime_0(length, unit, endingAt, appId, segmentId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionAnalyticsApi#appSessionsByTime_0");
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
| **length** | **String**| (Required) Integer  Max number of units (days or hours) before ending_at to include in the returned series - must be between 1 and 100 inclusive. | [optional] |
| **unit** | **String**| (Optional) String  Unit of time between data points - can be \&quot;day\&quot; or \&quot;hour\&quot; (defaults to \&quot;day\&quot;).  | [optional] |
| **endingAt** | **String**| (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request. | [optional] |
| **appId** | **String**| (Optional) String  App API identifier retrieved from the Developer Console to limit analytics to a specific app. | [optional] |
| **segmentId** | **String**| (Optional) String  Segment API identifier indicating the analytics enabled segment for which sessions should be returned. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

