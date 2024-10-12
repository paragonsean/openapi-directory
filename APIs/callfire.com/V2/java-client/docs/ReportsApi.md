# ReportsApi

All URIs are relative to *https://api.callfire.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDeliveryReports**](ReportsApi.md#getDeliveryReports) | **GET** /reports/delivery | Get delivery reports by ad hoc criteria |


<a id="getDeliveryReports"></a>
# **getDeliveryReports**
> PageDeliveryReport getDeliveryReports(startDate, endDate, limit, offset, campaignId, fromNumber, toNumber, deliveryCategory, deliveryState, carrier, messageText)

Get delivery reports by ad hoc criteria

Get delivery reports

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
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String startDate = "startDate_example"; // String | ~
    String endDate = "endDate_example"; // String | ~
    Integer limit = 100; // Integer | To set the maximum number of records to return in a paged list response. The default is 100
    Integer offset = 0; // Integer | Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
    Long campaignId = 56L; // Long | ~
    String fromNumber = "fromNumber_example"; // String | ~
    String toNumber = "toNumber_example"; // String | ~
    String deliveryCategory = "NO_DATA"; // String | ~
    String deliveryState = "DELIVERED"; // String | ~
    String carrier = "carrier_example"; // String | ~
    String messageText = "messageText_example"; // String | ~
    try {
      PageDeliveryReport result = apiInstance.getDeliveryReports(startDate, endDate, limit, offset, campaignId, fromNumber, toNumber, deliveryCategory, deliveryState, carrier, messageText);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#getDeliveryReports");
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
| **startDate** | **String**| ~ | [optional] |
| **endDate** | **String**| ~ | [optional] |
| **limit** | **Integer**| To set the maximum number of records to return in a paged list response. The default is 100 | [optional] [default to 100] |
| **offset** | **Integer**| Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API. | [optional] [default to 0] |
| **campaignId** | **Long**| ~ | [optional] |
| **fromNumber** | **String**| ~ | [optional] |
| **toNumber** | **String**| ~ | [optional] |
| **deliveryCategory** | **String**| ~ | [optional] [enum: NO_DATA, OPTED_OUT, BOUNCED, NO_CREDITS, DELIVERED] |
| **deliveryState** | **String**| ~ | [optional] [enum: DELIVERED, UNSENT_OPTED_OUT_GLOBAL, UNSENT_OPTED_OUT_LOCAL, UNSENT_NO_CREDITS, GATEWAY_REJECTED, CARRIER_REJECTED, NOT_DELIVERED, UNSENT_INVALID_NUMBER, UNSENT_BAD_DATA, UNSENT_FORCE_STOPPED, UNSENT_PERIOD_LIMIT, UNSENT_INTERNATIONAL, UNSENT_INVALID_TIMEZONE_OR_DNC, UNSENT_ALREADY_SCRUBBED, UNSENT_SYSTEM_ERROR, UNSENT_NO_WIRELESS_CARRIER, UNSENT_MESSAGE_TOO_LONG, UNSENT_MESSAGE_BLOCKED, UNSENT_QUEUE_LIMIT_REACHED, UNSENT_TOKEN_LIMIT_REACHED, UNSENT_TIME_LIMIT_REACHED, UNSENT_SCHEDULER_CAPACITY_EXCEEDED, SPAM_DETECTED, UNSENT_NO_GATEWAY, UNSENT_DAILY_LIMIT_REACHED, ORIGINATED, SUBMITTED, FORWARDED, NOT_GIVEN, UNKNOWN, RETRY_MMS_AS_SMS, QUEUED, QUEUED_TRANSCODE, ORIGINAL, DUPE, TRUNCATED, REQUEUED_RATE_LIMITED, BUFFERED, RATE_LIMIT_EXCEEDED, SERVICE_UNAVAILABLE, SEND_MMS_AS_SMS, REQUEUED_RECOVERABLE_ERROR, SEND_WITH_ADDITIONAL_SPID, UNSENT_FREE_TRIAL] |
| **carrier** | **String**| ~ | [optional] |
| **messageText** | **String**| ~ | [optional] |

### Return type

[**PageDeliveryReport**](PageDeliveryReport.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

