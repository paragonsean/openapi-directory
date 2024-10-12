# ProgrammesApi

All URIs are relative to *https://rms.api.bbc.co.uk*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getPopularEpisodesClips**](ProgrammesApi.md#getPopularEpisodesClips) | **GET** /radio/popular | Popular Episodes &amp; Clips |
| [**getRadioProgrammes**](ProgrammesApi.md#getRadioProgrammes) | **GET** /radio/programmes | Radio programmes |
| [**getRadioProgrammesByPid**](ProgrammesApi.md#getRadioProgrammesByPid) | **GET** /radio/programmes/{pid} | Available radio programme by Pid |
| [**getRecommendations**](ProgrammesApi.md#getRecommendations) | **GET** /my/programmes/recommendations | Recommended Programmes |


<a id="getPopularEpisodesClips"></a>
# **getPopularEpisodesClips**
> PopularResponse getPopularEpisodesClips(xAPIKey, type, distinct, network, networkUrlKey, category, format, group, mediaType, container, mediaSet, q)

Popular Episodes &amp; Clips

Retrieve Popular Episodes &amp; Clips 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProgrammesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    ProgrammesApi apiInstance = new ProgrammesApi(defaultClient);
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String type = "episode"; // String | Programme type required. Accepts comma separated values
    String distinct = "tleo"; // String | Filter by deduplication rule. E.g. 'tleo' returns programmes with distinct top level episode objects
    String network = "network_example"; // String | Filter by network master brand ID (mid). Accepts comma separated values
    String networkUrlKey = "networkUrlKey_example"; // String | Filter by network URL key. Accepts comma separated values
    String category = "category_example"; // String | Filter by category. Accepts comma separated values
    String format = "format_example"; // String | Filter by format. Accepts comma separated values
    String group = "tv"; // String | Filter by group. Accepts comma separated values
    String mediaType = "audio"; // String | Filter by programme media type. Accepts comma separated values
    String container = "container_example"; // String | Filter by container. Accepts any pid e.g. brand,series,episode
    List<Object> mediaSet = Arrays.asList(); // List<Object> | Filter by media set name. Accepts comma separated combinations of the following: pc,mobile-download,android-download-high,apple-ios-download-high,mobile-cellular-main,mobile-phone-main,iptv-all
    String q = "q_example"; // String | Search query String
    try {
      PopularResponse result = apiInstance.getPopularEpisodesClips(xAPIKey, type, distinct, network, networkUrlKey, category, format, group, mediaType, container, mediaSet, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProgrammesApi#getPopularEpisodesClips");
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
| **xAPIKey** | **String**| API_KEY | |
| **type** | **String**| Programme type required. Accepts comma separated values | [optional] [enum: episode, clip, episode,clip] |
| **distinct** | **String**| Filter by deduplication rule. E.g. &#39;tleo&#39; returns programmes with distinct top level episode objects | [optional] [enum: tleo] |
| **network** | **String**| Filter by network master brand ID (mid). Accepts comma separated values | [optional] |
| **networkUrlKey** | **String**| Filter by network URL key. Accepts comma separated values | [optional] |
| **category** | **String**| Filter by category. Accepts comma separated values | [optional] |
| **format** | **String**| Filter by format. Accepts comma separated values | [optional] |
| **group** | **String**| Filter by group. Accepts comma separated values | [optional] [enum: tv, radio, tv,radio] |
| **mediaType** | **String**| Filter by programme media type. Accepts comma separated values | [optional] [enum: audio, video, audio,video] |
| **container** | **String**| Filter by container. Accepts any pid e.g. brand,series,episode | [optional] |
| **mediaSet** | [**List&lt;Object&gt;**](Object.md)| Filter by media set name. Accepts comma separated combinations of the following: pc,mobile-download,android-download-high,apple-ios-download-high,mobile-cellular-main,mobile-phone-main,iptv-all | [optional] [enum: pc, mobile-download, android-download-high, apple-ios-download-high, mobile-cellular-main, mobile-phone-main, iptv-all] |
| **q** | **String**| Search query String | [optional] |

### Return type

[**PopularResponse**](PopularResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="getRadioProgrammes"></a>
# **getRadioProgrammes**
> ProgrammesResponse getRadioProgrammes(xAPIKey, kind, network, networkUrlKey, category, sort, container, type)

Radio programmes

Provides a paginated list of programmes by PID (brand, series, episode and clip). Accepts various filters and sorting methods.  N.B.  Swagger schemas cannot currently handle multiple combinations of object in an array i.e. a mix of Episode and Clip Summaries so we are defining results as an array of Programme Summary here.  This will be resolved in V3 with full support for  anyOf https://www.openapis.org/blog/2017/01/24/a-new-year-a-new-specification 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProgrammesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    ProgrammesApi apiInstance = new ProgrammesApi(defaultClient);
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String kind = "tleo"; // String | Filter by provided query. E.g. 'tleo' returns top level objects, ie. brands, orphaned series, and orphaned episodes
    String network = "network_example"; // String | Filter by network master brand ID (mid). Accepts comma separated values
    String networkUrlKey = "networkUrlKey_example"; // String | Filter by network URL key. Accepts comma separated values
    String category = "category_example"; // String | Filter by category id. Accepts comma separated values. See /category endpoint below for the type of response provided
    String sort = "available_from_date"; // String | Sort by provided query. E.g. 'title' sorts in ascending order, and -title sorts in descending order
    String container = "container_example"; // String | Filter by container. Accepts any brand or series pid
    String type = "brand"; // String | Filter by programme type. Accepts comma separated values
    try {
      ProgrammesResponse result = apiInstance.getRadioProgrammes(xAPIKey, kind, network, networkUrlKey, category, sort, container, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProgrammesApi#getRadioProgrammes");
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
| **xAPIKey** | **String**| API_KEY | |
| **kind** | **String**| Filter by provided query. E.g. &#39;tleo&#39; returns top level objects, ie. brands, orphaned series, and orphaned episodes | [optional] [enum: tleo] |
| **network** | **String**| Filter by network master brand ID (mid). Accepts comma separated values | [optional] |
| **networkUrlKey** | **String**| Filter by network URL key. Accepts comma separated values | [optional] |
| **category** | **String**| Filter by category id. Accepts comma separated values. See /category endpoint below for the type of response provided | [optional] |
| **sort** | **String**| Sort by provided query. E.g. &#39;title&#39; sorts in ascending order, and -title sorts in descending order | [optional] [enum: available_from_date, -available_from_date, title, -title] |
| **container** | **String**| Filter by container. Accepts any brand or series pid | [optional] |
| **type** | **String**| Filter by programme type. Accepts comma separated values | [optional] [enum: brand, series, episode, clip, episode,clip] |

### Return type

[**ProgrammesResponse**](ProgrammesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="getRadioProgrammesByPid"></a>
# **getRadioProgrammesByPid**
> ProgrammesResponse getRadioProgrammesByPid(xAPIKey, pid)

Available radio programme by Pid

Find programmes by PID (brand, series, episode and clip)  N.B.  Swagger schemas cannot currently handle multiple combinations of object in an array i.e. a mix of Episode and Clip Summaries so we are defining results as an array of Programme Summary here.  This will be resolved in V3 with full support for  anyOf https://www.openapis.org/blog/2017/01/24/a-new-year-a-new-specification 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProgrammesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    ProgrammesApi apiInstance = new ProgrammesApi(defaultClient);
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String pid = "pid_example"; // String | pid
    try {
      ProgrammesResponse result = apiInstance.getRadioProgrammesByPid(xAPIKey, pid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProgrammesApi#getRadioProgrammesByPid");
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
| **xAPIKey** | **String**| API_KEY | |
| **pid** | **String**| pid | |

### Return type

[**ProgrammesResponse**](ProgrammesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="getRecommendations"></a>
# **getRecommendations**
> ProgrammesResponse getRecommendations(authorization, xAPIKey, rights, offset, limit)

Recommended Programmes

Recommended Programmes from the Audience Platforms&#39; Recomendations Service 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProgrammesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    ProgrammesApi apiInstance = new ProgrammesApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String rights = "web"; // String | Only return available results for the web/mobile.
    Integer offset = 56; // Integer | Paginated results offset
    Integer limit = 56; // Integer | Paginated results limit
    try {
      ProgrammesResponse result = apiInstance.getRecommendations(authorization, xAPIKey, rights, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProgrammesApi#getRecommendations");
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
| **authorization** | **String**| Bearer OAUTH_TOKEN | [default to Bearer OAUTH_TOKEN] |
| **xAPIKey** | **String**| API_KEY | |
| **rights** | **String**| Only return available results for the web/mobile. | [enum: web, mobile] |
| **offset** | **Integer**| Paginated results offset | [optional] |
| **limit** | **Integer**| Paginated results limit | [optional] |

### Return type

[**ProgrammesResponse**](ProgrammesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | There was an error with the supplied &#x60;Authorization&#x60; header. |  -  |
| **0** | Unexpected error |  -  |

