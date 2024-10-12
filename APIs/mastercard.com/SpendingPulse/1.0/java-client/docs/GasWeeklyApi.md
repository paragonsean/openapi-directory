# GasWeeklyApi

All URIs are relative to *https://api.mastercard.com/spendingpulse/v1/spulse.svc*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**gasweeklyGet**](GasWeeklyApi.md#gasweeklyGet) | **GET** /gasweekly | Returns the weekly gasoline report. This resource pulls back the report with ProductLine &#x3D; \&quot;US Weekly Gasoline Demand Report\&quot;. Keep in mind that you must be subscribed to the gasoline weekly report to be able to receive data back from this resource. |


<a id="gasweeklyGet"></a>
# **gasweeklyGet**
> GasWeeklyListResponse gasweeklyGet(currentRow, offset)

Returns the weekly gasoline report. This resource pulls back the report with ProductLine &#x3D; \&quot;US Weekly Gasoline Demand Report\&quot;. Keep in mind that you must be subscribed to the gasoline weekly report to be able to receive data back from this resource.

Returns the weekly gasoline report. This resource pulls back the report with ProductLine &#x3D; \&quot;US Weekly Gasoline Demand Report\&quot;. Keep in mind that you must be subscribed to the gasoline weekly report to be able to receive data back from this resource. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GasWeeklyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com/spendingpulse/v1/spulse.svc");

    GasWeeklyApi apiInstance = new GasWeeklyApi(defaultClient);
    String currentRow = "1"; // String | Starting record number to return.
    String offset = "25"; // String | Used to restrict the number of records returned if needed to be less than max.
    try {
      GasWeeklyListResponse result = apiInstance.gasweeklyGet(currentRow, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GasWeeklyApi#gasweeklyGet");
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
| **currentRow** | **String**| Starting record number to return. | [optional] |
| **offset** | **String**| Used to restrict the number of records returned if needed to be less than max. | [optional] |

### Return type

[**GasWeeklyListResponse**](GasWeeklyListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of subscriptions. |  -  |
| **0** | Unexpected errors |  -  |

