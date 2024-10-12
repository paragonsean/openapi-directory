# DailyRatesApi

All URIs are relative to *https://api.hetras-certification.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dailyRatesGetDailyRates**](DailyRatesApi.md#dailyRatesGetDailyRates) | **GET** /api/booking/v0/daily_rates | Get a list of daily rates given a hotel Id, a channel code and a date range. |


<a id="dailyRatesGetDailyRates"></a>
# **dailyRatesGetDailyRates**
> DailyRatesResponse dailyRatesGetDailyRates(appId, appKey, hotelId, from, to, channelCode, expand, ratePlanCodes, skip, top, inlinecount)

Get a list of daily rates given a hotel Id, a channel code and a date range.

With the rates request you can get a list of different daily rates. You will have to at least               specify the hotel, the channel code, and a calendar range. The channel code will define which rates will be               returned based on the access control configuration for the rates. Additionally rate plan codes may be specified in              the request in order to limit only those rates of the given plans, if they are not specified, it will return all the public rate plans.              If requested the caller may specify whether he wants policies or not.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DailyRatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetras-certification.net");

    DailyRatesApi apiInstance = new DailyRatesApi(defaultClient);
    String appId = "appId_example"; // String | Application identifier
    String appKey = "appKey_example"; // String | Application key.
    Integer hotelId = 56; // Integer | Define the hotel id to request the availability for.
    OffsetDateTime from = OffsetDateTime.now(); // OffsetDateTime | Define the first business day you would like to get availability numbers for. The day should not be in the past.
    OffsetDateTime to = OffsetDateTime.now(); // OffsetDateTime | Define the last business day you would like to get rates for (inclusive). The maximum time span between <i>'From'</i> and <i>'To'</i>              is limited to 365 days. This can't be less than the 'From' date.
    String channelCode = "channelCode_example"; // String | Define the channel code in order to look up the rates for.
    List<String> expand = Arrays.asList(); // List<String> | Define the sections you want to expand and get informed about rates for.
    List<String> ratePlanCodes = Arrays.asList(); // List<String> | Define the codes of rate plans to show in the response. A list of comma ',' separated rate plan codes.
    Integer skip = 56; // Integer | Amount of items to skip.
    Integer top = 56; // Integer | Amount of items to select.
    String inlinecount = "None"; // String | Return total number of items for a given filter criteria.
    try {
      DailyRatesResponse result = apiInstance.dailyRatesGetDailyRates(appId, appKey, hotelId, from, to, channelCode, expand, ratePlanCodes, skip, top, inlinecount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DailyRatesApi#dailyRatesGetDailyRates");
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
| **appId** | **String**| Application identifier | |
| **appKey** | **String**| Application key. | |
| **hotelId** | **Integer**| Define the hotel id to request the availability for. | |
| **from** | **OffsetDateTime**| Define the first business day you would like to get availability numbers for. The day should not be in the past. | |
| **to** | **OffsetDateTime**| Define the last business day you would like to get rates for (inclusive). The maximum time span between &lt;i&gt;&#39;From&#39;&lt;/i&gt; and &lt;i&gt;&#39;To&#39;&lt;/i&gt;              is limited to 365 days. This can&#39;t be less than the &#39;From&#39; date. | |
| **channelCode** | **String**| Define the channel code in order to look up the rates for. | |
| **expand** | [**List&lt;String&gt;**](String.md)| Define the sections you want to expand and get informed about rates for. | [optional] [enum: None, Policies, RatePlans] |
| **ratePlanCodes** | [**List&lt;String&gt;**](String.md)| Define the codes of rate plans to show in the response. A list of comma &#39;,&#39; separated rate plan codes. | [optional] |
| **skip** | **Integer**| Amount of items to skip. | [optional] |
| **top** | **Integer**| Amount of items to select. | [optional] |
| **inlinecount** | **String**| Return total number of items for a given filter criteria. | [optional] [enum: None, AllPages] |

### Return type

[**DailyRatesResponse**](DailyRatesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Different rates for the requested stay details grouped by room type. |  -  |
| **204** | When there are no data to return. |  -  |
| **400** | The request failed to validate. One of the missing request parameters was missing or their value was wrong. |  -  |
| **401** | You provided wrong credentials, or you reached your API limit. |  -  |
| **403** | The application does not have access to the requested resource. |  -  |
| **404** | Not Found. The server has not found anything matching the Request-URI. This code will not be returned when there are no data to return for (please see 204). |  -  |
| **409** | When an error occurs which prevent the API to return a response and is normally cause by bad input. |  -  |
| **500** | We caught an unexpected error on our side. Please report with providing the Hetras-Tracking-Id from the response headers and we will check the logfiles. |  -  |
| **503** | The server is currently unavailable. Please try later. |  -  |

