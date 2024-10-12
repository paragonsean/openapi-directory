# UniqueDevicesDataApi

All URIs are relative to *https://wikimedia.org/api/rest_v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**metricsUniqueDevicesProjectAccessSiteGranularityStartEndGet**](UniqueDevicesDataApi.md#metricsUniqueDevicesProjectAccessSiteGranularityStartEndGet) | **GET** /metrics/unique-devices/{project}/{access-site}/{granularity}/{start}/{end} | Get unique devices count per project |


<a id="metricsUniqueDevicesProjectAccessSiteGranularityStartEndGet"></a>
# **metricsUniqueDevicesProjectAccessSiteGranularityStartEndGet**
> UniqueDevices metricsUniqueDevicesProjectAccessSiteGranularityStartEndGet(project, accessSite, granularity, start, end)

Get unique devices count per project

Given a project and a date range, returns a timeseries of unique devices counts. You need to specify a project, and can filter by accessed site (mobile or desktop). You can choose between daily and hourly granularity as well.  - Stability: [stable](https://www.mediawiki.org/wiki/API_versioning#Stable) - Rate limit: 100 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UniqueDevicesDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wikimedia.org/api/rest_v1");

    UniqueDevicesDataApi apiInstance = new UniqueDevicesDataApi(defaultClient);
    String project = "project_example"; // String | If you want to filter by project, use the domain of any Wikimedia project, for example 'en.wikipedia.org', 'www.mediawiki.org' or 'commons.wikimedia.org'. 
    String accessSite = "all-sites"; // String | If you want to filter by accessed site, use one of desktop-site or mobile-site. If you are interested in unique devices regardless of accessed site, use or all-sites. 
    String granularity = "daily"; // String | The time unit for the response data. As of today, the supported granularities for this endpoint are daily and monthly. 
    String start = "start_example"; // String | The timestamp of the first day/month to include, in YYYYMMDD format
    String end = "end_example"; // String | The timestamp of the last day/month to include, in YYYYMMDD format
    try {
      UniqueDevices result = apiInstance.metricsUniqueDevicesProjectAccessSiteGranularityStartEndGet(project, accessSite, granularity, start, end);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UniqueDevicesDataApi#metricsUniqueDevicesProjectAccessSiteGranularityStartEndGet");
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
| **project** | **String**| If you want to filter by project, use the domain of any Wikimedia project, for example &#39;en.wikipedia.org&#39;, &#39;www.mediawiki.org&#39; or &#39;commons.wikimedia.org&#39;.  | |
| **accessSite** | **String**| If you want to filter by accessed site, use one of desktop-site or mobile-site. If you are interested in unique devices regardless of accessed site, use or all-sites.  | [enum: all-sites, desktop-site, mobile-site] |
| **granularity** | **String**| The time unit for the response data. As of today, the supported granularities for this endpoint are daily and monthly.  | [enum: daily, monthly] |
| **start** | **String**| The timestamp of the first day/month to include, in YYYYMMDD format | |
| **end** | **String**| The timestamp of the last day/month to include, in YYYYMMDD format | |

### Return type

[**UniqueDevices**](UniqueDevices.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of values |  -  |
| **0** | Error |  -  |

