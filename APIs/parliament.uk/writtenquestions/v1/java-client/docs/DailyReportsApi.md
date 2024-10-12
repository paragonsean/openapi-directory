# DailyReportsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiDailyreportsDailyreportsGet**](DailyReportsApi.md#apiDailyreportsDailyreportsGet) | **GET** /api/dailyreports/dailyreports | Returns a list of daily reports |


<a id="apiDailyreportsDailyreportsGet"></a>
# **apiDailyreportsDailyreportsGet**
> DailyReportViewModelSearchResult apiDailyreportsDailyreportsGet(dateFrom, dateTo, house, skip, take)

Returns a list of daily reports

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DailyReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DailyReportsApi apiInstance = new DailyReportsApi(defaultClient);
    OffsetDateTime dateFrom = OffsetDateTime.now(); // OffsetDateTime | Daily report with report date on or after the date specified. Date format yyyy-mm-dd
    OffsetDateTime dateTo = OffsetDateTime.now(); // OffsetDateTime | Daily report with report date on or before the date specified. Date format yyyy-mm-dd
    HouseEnum house = HouseEnum.fromValue("Bicameral"); // HouseEnum | Daily report relating to the House specified. Defaults to Bicameral
    Integer skip = 56; // Integer | Number of records to skip, default is 0
    Integer take = 56; // Integer | Number of records to take, default is 20
    try {
      DailyReportViewModelSearchResult result = apiInstance.apiDailyreportsDailyreportsGet(dateFrom, dateTo, house, skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DailyReportsApi#apiDailyreportsDailyreportsGet");
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
| **dateFrom** | **OffsetDateTime**| Daily report with report date on or after the date specified. Date format yyyy-mm-dd | [optional] |
| **dateTo** | **OffsetDateTime**| Daily report with report date on or before the date specified. Date format yyyy-mm-dd | [optional] |
| **house** | [**HouseEnum**](.md)| Daily report relating to the House specified. Defaults to Bicameral | [optional] [enum: Bicameral, Commons, Lords] |
| **skip** | **Integer**| Number of records to skip, default is 0 | [optional] |
| **take** | **Integer**| Number of records to take, default is 20 | [optional] |

### Return type

[**DailyReportViewModelSearchResult**](DailyReportViewModelSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

