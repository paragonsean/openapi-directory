# NotificationsApi

All URIs are relative to *http://config2.gamesparks.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getGameSummaryUsingGET**](NotificationsApi.md#getGameSummaryUsingGET) | **GET** /restv2/game/{apiKey}/admin/notifications/summary | getGameSummary |


<a id="getGameSummaryUsingGET"></a>
# **getGameSummaryUsingGET**
> GameSummaryModel getGameSummaryUsingGET(apiKey, stage, startDate, endDate)

getGameSummary

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    NotificationsApi apiInstance = new NotificationsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    String stage = "LIVE"; // String | stage
    LocalDate startDate = LocalDate.now(); // LocalDate | yyyy-MM-dd
    LocalDate endDate = LocalDate.now(); // LocalDate | yyyy-MM-dd
    try {
      GameSummaryModel result = apiInstance.getGameSummaryUsingGET(apiKey, stage, startDate, endDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationsApi#getGameSummaryUsingGET");
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
| **startDate** | **LocalDate**| yyyy-MM-dd | |
| **endDate** | **LocalDate**| yyyy-MM-dd | |

### Return type

[**GameSummaryModel**](GameSummaryModel.md)

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

