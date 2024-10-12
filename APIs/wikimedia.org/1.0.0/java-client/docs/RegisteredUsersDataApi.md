# RegisteredUsersDataApi

All URIs are relative to *https://wikimedia.org/api/rest_v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**metricsRegisteredUsersNewProjectGranularityStartEndGet**](RegisteredUsersDataApi.md#metricsRegisteredUsersNewProjectGranularityStartEndGet) | **GET** /metrics/registered-users/new/{project}/{granularity}/{start}/{end} | Get newly registered users counts for a project. |


<a id="metricsRegisteredUsersNewProjectGranularityStartEndGet"></a>
# **metricsRegisteredUsersNewProjectGranularityStartEndGet**
> NewRegisteredUsers metricsRegisteredUsersNewProjectGranularityStartEndGet(project, granularity, start, end)

Get newly registered users counts for a project.

Given a Mediawiki project and a date range, returns a timeseries of its newly registered users counts. You can choose between daily and monthly granularity. The newly registered users value is computed with self-created users only, not auto-login created ones.  - Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental) - Rate limit: 25 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegisteredUsersDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wikimedia.org/api/rest_v1");

    RegisteredUsersDataApi apiInstance = new RegisteredUsersDataApi(defaultClient);
    String project = "project_example"; // String | The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off.  For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org. If you're interested in the aggregation of all projects, use all. 
    String granularity = "daily"; // String | The time unit for the response data. As of today, supported values are daily and monthly. 
    String start = "start_example"; // String | The date of the first day to include, in YYYYMMDD format
    String end = "end_example"; // String | The date of the last day to include, in YYYYMMDD format
    try {
      NewRegisteredUsers result = apiInstance.metricsRegisteredUsersNewProjectGranularityStartEndGet(project, granularity, start, end);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegisteredUsersDataApi#metricsRegisteredUsersNewProjectGranularityStartEndGet");
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
| **project** | **String**| The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off.  For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org. If you&#39;re interested in the aggregation of all projects, use all.  | |
| **granularity** | **String**| The time unit for the response data. As of today, supported values are daily and monthly.  | [enum: daily, monthly] |
| **start** | **String**| The date of the first day to include, in YYYYMMDD format | |
| **end** | **String**| The date of the last day to include, in YYYYMMDD format | |

### Return type

[**NewRegisteredUsers**](NewRegisteredUsers.md)

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

