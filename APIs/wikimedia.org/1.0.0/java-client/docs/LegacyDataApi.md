# LegacyDataApi

All URIs are relative to *https://wikimedia.org/api/rest_v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**metricsLegacyPagecountsAggregateProjectAccessSiteGranularityStartEndGet**](LegacyDataApi.md#metricsLegacyPagecountsAggregateProjectAccessSiteGranularityStartEndGet) | **GET** /metrics/legacy/pagecounts/aggregate/{project}/{access-site}/{granularity}/{start}/{end} |  |


<a id="metricsLegacyPagecountsAggregateProjectAccessSiteGranularityStartEndGet"></a>
# **metricsLegacyPagecountsAggregateProjectAccessSiteGranularityStartEndGet**
> PagecountsProject metricsLegacyPagecountsAggregateProjectAccessSiteGranularityStartEndGet(project, accessSite, granularity, start, end)



Given a project and a date range, returns a timeseries of pagecounts. You can filter by access site (mobile or desktop) and you can choose between monthly, daily and hourly granularity as well.  - Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental) - Rate limit: 100 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LegacyDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wikimedia.org/api/rest_v1");

    LegacyDataApi apiInstance = new LegacyDataApi(defaultClient);
    String project = "project_example"; // String | The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off. For projects like commons without language codes, use commons.wikimedia. 
    String accessSite = "all-sites"; // String | If you want to filter by access site, use one of desktop-site or mobile-site. If you are interested in pagecounts regardless of access site use all-sites.
    String granularity = "hourly"; // String | The time unit for the response data. As of today, the supported granularities for this endpoint are hourly, daily and monthly. 
    String start = "start_example"; // String | The timestamp of the first hour/day/month to include, in YYYYMMDDHH format.
    String end = "end_example"; // String | The timestamp of the last hour/day/month to include, in YYYYMMDDHH format. In hourly and daily granularities this value is inclusive, in the monthly granularity this value is exclusive. 
    try {
      PagecountsProject result = apiInstance.metricsLegacyPagecountsAggregateProjectAccessSiteGranularityStartEndGet(project, accessSite, granularity, start, end);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LegacyDataApi#metricsLegacyPagecountsAggregateProjectAccessSiteGranularityStartEndGet");
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
| **project** | **String**| The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off. For projects like commons without language codes, use commons.wikimedia.  | |
| **accessSite** | **String**| If you want to filter by access site, use one of desktop-site or mobile-site. If you are interested in pagecounts regardless of access site use all-sites. | [enum: all-sites, desktop-site, mobile-site] |
| **granularity** | **String**| The time unit for the response data. As of today, the supported granularities for this endpoint are hourly, daily and monthly.  | [enum: hourly, daily, monthly] |
| **start** | **String**| The timestamp of the first hour/day/month to include, in YYYYMMDDHH format. | |
| **end** | **String**| The timestamp of the last hour/day/month to include, in YYYYMMDDHH format. In hourly and daily granularities this value is inclusive, in the monthly granularity this value is exclusive.  | |

### Return type

[**PagecountsProject**](PagecountsProject.md)

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

