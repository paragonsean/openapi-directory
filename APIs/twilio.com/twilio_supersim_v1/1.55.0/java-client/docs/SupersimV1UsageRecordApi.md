# SupersimV1UsageRecordApi

All URIs are relative to *https://supersim.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listUsageRecord**](SupersimV1UsageRecordApi.md#listUsageRecord) | **GET** /v1/UsageRecords |  |


<a id="listUsageRecord"></a>
# **listUsageRecord**
> ListUsageRecordResponse listUsageRecord(sim, fleet, network, isoCountry, group, granularity, startTime, endTime, pageSize, page, pageToken)



List UsageRecords

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupersimV1UsageRecordApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://supersim.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SupersimV1UsageRecordApi apiInstance = new SupersimV1UsageRecordApi(defaultClient);
    String sim = "sim_example"; // String | SID or unique name of a Sim resource. Only show UsageRecords representing usage incurred by this Super SIM.
    String fleet = "fleet_example"; // String | SID or unique name of a Fleet resource. Only show UsageRecords representing usage for Super SIMs belonging to this Fleet resource at the time the usage occurred.
    String network = "network_example"; // String | SID of a Network resource. Only show UsageRecords representing usage on this network.
    String isoCountry = "isoCountry_example"; // String | Alpha-2 ISO Country Code. Only show UsageRecords representing usage in this country.
    UsageRecordEnumGroup group = UsageRecordEnumGroup.fromValue("sim"); // UsageRecordEnumGroup | Dimension over which to aggregate usage records. Can be: `sim`, `fleet`, `network`, `isoCountry`. Default is to not aggregate across any of these dimensions, UsageRecords will be aggregated into the time buckets described by the `Granularity` parameter.
    UsageRecordEnumGranularity granularity = UsageRecordEnumGranularity.fromValue("hour"); // UsageRecordEnumGranularity | Time-based grouping that UsageRecords should be aggregated by. Can be: `hour`, `day`, or `all`. Default is `all`. `all` returns one UsageRecord that describes the usage for the entire period.
    OffsetDateTime startTime = OffsetDateTime.now(); // OffsetDateTime | Only include usage that occurred at or after this time, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Default is one month before the `end_time`.
    OffsetDateTime endTime = OffsetDateTime.now(); // OffsetDateTime | Only include usage that occurred before this time (exclusive), specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Default is the current time.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListUsageRecordResponse result = apiInstance.listUsageRecord(sim, fleet, network, isoCountry, group, granularity, startTime, endTime, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupersimV1UsageRecordApi#listUsageRecord");
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
| **sim** | **String**| SID or unique name of a Sim resource. Only show UsageRecords representing usage incurred by this Super SIM. | [optional] |
| **fleet** | **String**| SID or unique name of a Fleet resource. Only show UsageRecords representing usage for Super SIMs belonging to this Fleet resource at the time the usage occurred. | [optional] |
| **network** | **String**| SID of a Network resource. Only show UsageRecords representing usage on this network. | [optional] |
| **isoCountry** | **String**| Alpha-2 ISO Country Code. Only show UsageRecords representing usage in this country. | [optional] |
| **group** | **UsageRecordEnumGroup**| Dimension over which to aggregate usage records. Can be: &#x60;sim&#x60;, &#x60;fleet&#x60;, &#x60;network&#x60;, &#x60;isoCountry&#x60;. Default is to not aggregate across any of these dimensions, UsageRecords will be aggregated into the time buckets described by the &#x60;Granularity&#x60; parameter. | [optional] [enum: sim, fleet, network, isoCountry] |
| **granularity** | **UsageRecordEnumGranularity**| Time-based grouping that UsageRecords should be aggregated by. Can be: &#x60;hour&#x60;, &#x60;day&#x60;, or &#x60;all&#x60;. Default is &#x60;all&#x60;. &#x60;all&#x60; returns one UsageRecord that describes the usage for the entire period. | [optional] [enum: hour, day, all] |
| **startTime** | **OffsetDateTime**| Only include usage that occurred at or after this time, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Default is one month before the &#x60;end_time&#x60;. | [optional] |
| **endTime** | **OffsetDateTime**| Only include usage that occurred before this time (exclusive), specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Default is the current time. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListUsageRecordResponse**](ListUsageRecordResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

