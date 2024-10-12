# AnalysisApi

All URIs are relative to *https://api.botify.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createUrlsExport**](AnalysisApi.md#createUrlsExport) | **POST** /analyses/{username}/{project_slug}/{analysis_slug}/urls/export | Creates a new UrlExport object and starts a task that will export the results into a csv |
| [**getAnalysisSummary**](AnalysisApi.md#getAnalysisSummary) | **GET** /analyses/{username}/{project_slug}/{analysis_slug} | Get an Analysis detail |
| [**getCrawlStatistics**](AnalysisApi.md#getCrawlStatistics) | **GET** /analyses/{username}/{project_slug}/{analysis_slug}/crawl_statistics | Return global statistics for an analysis |
| [**getCrawlStatisticsByFrequency**](AnalysisApi.md#getCrawlStatisticsByFrequency) | **GET** /analyses/{username}/{project_slug}/{analysis_slug}/crawl_statistics/time | Return crawl statistics grouped by time frequency (1 min, 5 mins or 60 min) |
| [**getCrawlStatisticsUrls**](AnalysisApi.md#getCrawlStatisticsUrls) | **GET** /analyses/{username}/{project_slug}/{analysis_slug}/crawl_statistics/urls/{list_type} | Return a list of 1000 latest URLs crawled (all crawled URLs or only URLS with HTTP errors) |
| [**getGanalyticsOrphanURLs**](AnalysisApi.md#getGanalyticsOrphanURLs) | **GET** /analyses/{username}/{project_slug}/{analysis_slug}/features/ganalytics/orphan_urls/{medium}/{source} | List of Orphan URLs |
| [**getLinksPercentiles**](AnalysisApi.md#getLinksPercentiles) | **GET** /analyses/{username}/{project_slug}/{analysis_slug}/features/links/percentiles | Get inlinks percentiles |
| [**getLinksTopDomains**](AnalysisApi.md#getLinksTopDomains) | **GET** /analyses/{username}/{project_slug}/{analysis_slug}/features/top_domains/domains | Top domains |
| [**getLinksTopSubdomains**](AnalysisApi.md#getLinksTopSubdomains) | **GET** /analyses/{username}/{project_slug}/{analysis_slug}/features/top_domains/subdomains | Top subddomains |
| [**getPageRankLost**](AnalysisApi.md#getPageRankLost) | **GET** /analyses/{username}/{project_slug}/{analysis_slug}/features/pagerank/lost | Lost pagerank |
| [**getSitemapsReport**](AnalysisApi.md#getSitemapsReport) | **GET** /analyses/{username}/{project_slug}/{analysis_slug}/features/sitemaps/report | Get global information of the sitemaps found (sitemaps indexes, invalid sitemaps urls, etc |
| [**getSitemapsSamplesOutOfConfig**](AnalysisApi.md#getSitemapsSamplesOutOfConfig) | **GET** /analyses/{username}/{project_slug}/{analysis_slug}/features/sitemaps/samples/out_of_config | Sample list of URLs which were found in your sitemaps but outside of the |
| [**getSitemapsSamplesSitemapsOnly**](AnalysisApi.md#getSitemapsSamplesSitemapsOnly) | **GET** /analyses/{username}/{project_slug}/{analysis_slug}/features/sitemaps/samples/sitemap_only | Sample list of URLs which were found in your sitemaps, within the project |
| [**getUrlDetail**](AnalysisApi.md#getUrlDetail) | **GET** /analyses/{username}/{project_slug}/{analysis_slug}/urls/{url} | Gets the detail of an URL for an analysis |
| [**getUrls**](AnalysisApi.md#getUrls) | **POST** /analyses/{username}/{project_slug}/{analysis_slug}/urls | Executes a query and returns a paginated response |
| [**getUrlsAggs**](AnalysisApi.md#getUrlsAggs) | **POST** /analyses/{username}/{project_slug}/{analysis_slug}/urls/aggs | Query aggregator |
| [**getUrlsDatamodel**](AnalysisApi.md#getUrlsDatamodel) | **GET** /analyses/{username}/{project_slug}/{analysis_slug}/urls/datamodel | Gets an Analysis datamodel |
| [**getUrlsExportStatus**](AnalysisApi.md#getUrlsExportStatus) | **GET** /analyses/{username}/{project_slug}/{analysis_slug}/urls/export/{url_export_id} | Checks the status of an CSVUrlExportJob object |
| [**getUrlsExports**](AnalysisApi.md#getUrlsExports) | **GET** /analyses/{username}/{project_slug}/{analysis_slug}/urls/export | A list of the CSV Exports requests and their current status |
| [**getUrlsSuggestedFilters**](AnalysisApi.md#getUrlsSuggestedFilters) | **POST** /analyses/{username}/{project_slug}/{analysis_slug}/urls/suggested_filters | Return most frequent segments (&#x3D; suggested patterns in the previous version) |


<a id="createUrlsExport"></a>
# **createUrlsExport**
> CsvExportStatus createUrlsExport(username, projectSlug, analysisSlug, area, urlsQuery)

Creates a new UrlExport object and starts a task that will export the results into a csv

Creates a new UrlExport object and starts a task that will export the results into a csv. Returns the model id that manages the task

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.botify.com/v1");
    
    // Configure API key authorization: DjangoRestToken
    ApiKeyAuth DjangoRestToken = (ApiKeyAuth) defaultClient.getAuthentication("DjangoRestToken");
    DjangoRestToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //DjangoRestToken.setApiKeyPrefix("Token");

    AnalysisApi apiInstance = new AnalysisApi(defaultClient);
    String username = "username_example"; // String | User's identifier
    String projectSlug = "projectSlug_example"; // String | Project's identifier
    String analysisSlug = "analysisSlug_example"; // String | Analysis' identifier
    String area = "current"; // String | 
    UrlsQuery urlsQuery = new UrlsQuery(); // UrlsQuery | 
    try {
      CsvExportStatus result = apiInstance.createUrlsExport(username, projectSlug, analysisSlug, area, urlsQuery);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysisApi#createUrlsExport");
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
| **username** | **String**| User&#39;s identifier | |
| **projectSlug** | **String**| Project&#39;s identifier | |
| **analysisSlug** | **String**| Analysis&#39; identifier | |
| **area** | **String**|  | [optional] [default to current] [enum: current, disappeared, new, search_engines_orphans] |
| **urlsQuery** | [**UrlsQuery**](UrlsQuery.md)|  | [optional] |

### Return type

[**CsvExportStatus**](CsvExportStatus.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |
| **0** | error payload |  -  |

<a id="getAnalysisSummary"></a>
# **getAnalysisSummary**
> AnalysisDetail getAnalysisSummary(username, projectSlug, analysisSlug)

Get an Analysis detail

Get an Analysis detail

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.botify.com/v1");
    
    // Configure API key authorization: DjangoRestToken
    ApiKeyAuth DjangoRestToken = (ApiKeyAuth) defaultClient.getAuthentication("DjangoRestToken");
    DjangoRestToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //DjangoRestToken.setApiKeyPrefix("Token");

    AnalysisApi apiInstance = new AnalysisApi(defaultClient);
    String username = "username_example"; // String | User's identifier
    String projectSlug = "projectSlug_example"; // String | Project's identifier
    String analysisSlug = "analysisSlug_example"; // String | Analysis' identifier
    try {
      AnalysisDetail result = apiInstance.getAnalysisSummary(username, projectSlug, analysisSlug);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysisApi#getAnalysisSummary");
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
| **username** | **String**| User&#39;s identifier | |
| **projectSlug** | **String**| Project&#39;s identifier | |
| **analysisSlug** | **String**| Analysis&#39; identifier | |

### Return type

[**AnalysisDetail**](AnalysisDetail.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **0** | error payload |  -  |

<a id="getCrawlStatistics"></a>
# **getCrawlStatistics**
> CrawlStatistics getCrawlStatistics(username, projectSlug, analysisSlug)

Return global statistics for an analysis

Return global statistics for an analysis

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.botify.com/v1");
    
    // Configure API key authorization: DjangoRestToken
    ApiKeyAuth DjangoRestToken = (ApiKeyAuth) defaultClient.getAuthentication("DjangoRestToken");
    DjangoRestToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //DjangoRestToken.setApiKeyPrefix("Token");

    AnalysisApi apiInstance = new AnalysisApi(defaultClient);
    String username = "username_example"; // String | User's identifier
    String projectSlug = "projectSlug_example"; // String | Project's identifier
    String analysisSlug = "analysisSlug_example"; // String | Analysis' identifier
    try {
      CrawlStatistics result = apiInstance.getCrawlStatistics(username, projectSlug, analysisSlug);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysisApi#getCrawlStatistics");
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
| **username** | **String**| User&#39;s identifier | |
| **projectSlug** | **String**| Project&#39;s identifier | |
| **analysisSlug** | **String**| Analysis&#39; identifier | |

### Return type

[**CrawlStatistics**](CrawlStatistics.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **0** | error payload |  -  |

<a id="getCrawlStatisticsByFrequency"></a>
# **getCrawlStatisticsByFrequency**
> CrawlStatisticsTime getCrawlStatisticsByFrequency(username, projectSlug, analysisSlug, frequency, limit)

Return crawl statistics grouped by time frequency (1 min, 5 mins or 60 min)

Return crawl statistics grouped by time frequency (1 min, 5 mins or 60 min) for an analysis

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.botify.com/v1");
    
    // Configure API key authorization: DjangoRestToken
    ApiKeyAuth DjangoRestToken = (ApiKeyAuth) defaultClient.getAuthentication("DjangoRestToken");
    DjangoRestToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //DjangoRestToken.setApiKeyPrefix("Token");

    AnalysisApi apiInstance = new AnalysisApi(defaultClient);
    String username = "username_example"; // String | User's identifier
    String projectSlug = "projectSlug_example"; // String | Project's identifier
    String analysisSlug = "analysisSlug_example"; // String | Analysis' identifier
    String frequency = "1mn"; // String | Aggregation frequency
    Integer limit = 56; // Integer | max number of elements to retrieve
    try {
      CrawlStatisticsTime result = apiInstance.getCrawlStatisticsByFrequency(username, projectSlug, analysisSlug, frequency, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysisApi#getCrawlStatisticsByFrequency");
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
| **username** | **String**| User&#39;s identifier | |
| **projectSlug** | **String**| Project&#39;s identifier | |
| **analysisSlug** | **String**| Analysis&#39; identifier | |
| **frequency** | **String**| Aggregation frequency | [enum: 1mn, 5mn, 60mn] |
| **limit** | **Integer**| max number of elements to retrieve | [optional] |

### Return type

[**CrawlStatisticsTime**](CrawlStatisticsTime.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **0** | error payload |  -  |

<a id="getCrawlStatisticsUrls"></a>
# **getCrawlStatisticsUrls**
> List&lt;Object&gt; getCrawlStatisticsUrls(username, projectSlug, analysisSlug, listType)

Return a list of 1000 latest URLs crawled (all crawled URLs or only URLS with HTTP errors)

Return a list of 1000 latest URLs crawled (all crawled URLs or only URLS with HTTP errors)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.botify.com/v1");
    
    // Configure API key authorization: DjangoRestToken
    ApiKeyAuth DjangoRestToken = (ApiKeyAuth) defaultClient.getAuthentication("DjangoRestToken");
    DjangoRestToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //DjangoRestToken.setApiKeyPrefix("Token");

    AnalysisApi apiInstance = new AnalysisApi(defaultClient);
    String username = "username_example"; // String | User's identifier
    String projectSlug = "projectSlug_example"; // String | Project's identifier
    String analysisSlug = "analysisSlug_example"; // String | Analysis' identifier
    String listType = "crawled"; // String | URLs list type (crawled URLs or error URLs)
    try {
      List<Object> result = apiInstance.getCrawlStatisticsUrls(username, projectSlug, analysisSlug, listType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysisApi#getCrawlStatisticsUrls");
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
| **username** | **String**| User&#39;s identifier | |
| **projectSlug** | **String**| Project&#39;s identifier | |
| **analysisSlug** | **String**| Analysis&#39; identifier | |
| **listType** | **String**| URLs list type (crawled URLs or error URLs) | [enum: crawled, errors] |

### Return type

**List&lt;Object&gt;**

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **0** | error payload |  -  |

<a id="getGanalyticsOrphanURLs"></a>
# **getGanalyticsOrphanURLs**
> GetGanalyticsOrphanURLs200Response getGanalyticsOrphanURLs(username, projectSlug, analysisSlug, medium, source, page, size)

List of Orphan URLs

List of Orphan URLs. URLs which generated visits from the selected source according to Google Analytics data, but were not crawled with by the Botify crawler (either because no links to them were found on the website, or because the crawler was not allowed to follow these links according to the project settings).   For a search engine (medium: origanic; sources: all, aol, ask, baidu, bing, google, naver, yahoo, yandex) or a social network (medium: social; sources: all, facebook, google+, linkedin, pinterest, reddit, tumblr, twitter)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.botify.com/v1");
    
    // Configure API key authorization: DjangoRestToken
    ApiKeyAuth DjangoRestToken = (ApiKeyAuth) defaultClient.getAuthentication("DjangoRestToken");
    DjangoRestToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //DjangoRestToken.setApiKeyPrefix("Token");

    AnalysisApi apiInstance = new AnalysisApi(defaultClient);
    String username = "username_example"; // String | User's identifier
    String projectSlug = "projectSlug_example"; // String | Project's identifier
    String analysisSlug = "analysisSlug_example"; // String | Analysis' identifier
    String medium = "organic"; // String | Type of traffic, value: 'organic' (from search engine)or 'social' (from a social network)
    String source = "all"; // String | Traffic source, value: name of the search engine or social network
    Integer page = 56; // Integer | Page Number
    Integer size = 56; // Integer | Page Size
    try {
      GetGanalyticsOrphanURLs200Response result = apiInstance.getGanalyticsOrphanURLs(username, projectSlug, analysisSlug, medium, source, page, size);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysisApi#getGanalyticsOrphanURLs");
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
| **username** | **String**| User&#39;s identifier | |
| **projectSlug** | **String**| Project&#39;s identifier | |
| **analysisSlug** | **String**| Analysis&#39; identifier | |
| **medium** | **String**| Type of traffic, value: &#39;organic&#39; (from search engine)or &#39;social&#39; (from a social network) | [enum: organic, social] |
| **source** | **String**| Traffic source, value: name of the search engine or social network | [enum: all, aol, ask, baidu, bing, facebook, google, google+, linkedin, naver, pinterest, reddit, tumblr, twitter, yahoo, yandex] |
| **page** | **Integer**| Page Number | [optional] |
| **size** | **Integer**| Page Size | [optional] |

### Return type

[**GetGanalyticsOrphanURLs200Response**](GetGanalyticsOrphanURLs200Response.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **0** | error payload |  -  |

<a id="getLinksPercentiles"></a>
# **getLinksPercentiles**
> LinksPercentiles getLinksPercentiles(username, projectSlug, analysisSlug)

Get inlinks percentiles

Get inlinks percentiles

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.botify.com/v1");
    
    // Configure API key authorization: DjangoRestToken
    ApiKeyAuth DjangoRestToken = (ApiKeyAuth) defaultClient.getAuthentication("DjangoRestToken");
    DjangoRestToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //DjangoRestToken.setApiKeyPrefix("Token");

    AnalysisApi apiInstance = new AnalysisApi(defaultClient);
    String username = "username_example"; // String | User's identifier
    String projectSlug = "projectSlug_example"; // String | Project's identifier
    String analysisSlug = "analysisSlug_example"; // String | Analysis' identifier
    try {
      LinksPercentiles result = apiInstance.getLinksPercentiles(username, projectSlug, analysisSlug);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysisApi#getLinksPercentiles");
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
| **username** | **String**| User&#39;s identifier | |
| **projectSlug** | **String**| Project&#39;s identifier | |
| **analysisSlug** | **String**| Analysis&#39; identifier | |

### Return type

[**LinksPercentiles**](LinksPercentiles.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **0** | error payload |  -  |

<a id="getLinksTopDomains"></a>
# **getLinksTopDomains**
> GetLinksTopDomains200Response getLinksTopDomains(username, projectSlug, analysisSlug, page, size)

Top domains

Top domains

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.botify.com/v1");
    
    // Configure API key authorization: DjangoRestToken
    ApiKeyAuth DjangoRestToken = (ApiKeyAuth) defaultClient.getAuthentication("DjangoRestToken");
    DjangoRestToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //DjangoRestToken.setApiKeyPrefix("Token");

    AnalysisApi apiInstance = new AnalysisApi(defaultClient);
    String username = "username_example"; // String | User's identifier
    String projectSlug = "projectSlug_example"; // String | Project's identifier
    String analysisSlug = "analysisSlug_example"; // String | Analysis' identifier
    Integer page = 56; // Integer | Page Number
    Integer size = 56; // Integer | Page Size
    try {
      GetLinksTopDomains200Response result = apiInstance.getLinksTopDomains(username, projectSlug, analysisSlug, page, size);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysisApi#getLinksTopDomains");
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
| **username** | **String**| User&#39;s identifier | |
| **projectSlug** | **String**| Project&#39;s identifier | |
| **analysisSlug** | **String**| Analysis&#39; identifier | |
| **page** | **Integer**| Page Number | [optional] |
| **size** | **Integer**| Page Size | [optional] |

### Return type

[**GetLinksTopDomains200Response**](GetLinksTopDomains200Response.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **0** | error payload |  -  |

<a id="getLinksTopSubdomains"></a>
# **getLinksTopSubdomains**
> GetLinksTopDomains200Response getLinksTopSubdomains(username, projectSlug, analysisSlug, page, size)

Top subddomains

Top subddomains

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.botify.com/v1");
    
    // Configure API key authorization: DjangoRestToken
    ApiKeyAuth DjangoRestToken = (ApiKeyAuth) defaultClient.getAuthentication("DjangoRestToken");
    DjangoRestToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //DjangoRestToken.setApiKeyPrefix("Token");

    AnalysisApi apiInstance = new AnalysisApi(defaultClient);
    String username = "username_example"; // String | User's identifier
    String projectSlug = "projectSlug_example"; // String | Project's identifier
    String analysisSlug = "analysisSlug_example"; // String | Analysis' identifier
    Integer page = 56; // Integer | Page Number
    Integer size = 56; // Integer | Page Size
    try {
      GetLinksTopDomains200Response result = apiInstance.getLinksTopSubdomains(username, projectSlug, analysisSlug, page, size);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysisApi#getLinksTopSubdomains");
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
| **username** | **String**| User&#39;s identifier | |
| **projectSlug** | **String**| Project&#39;s identifier | |
| **analysisSlug** | **String**| Analysis&#39; identifier | |
| **page** | **Integer**| Page Number | [optional] |
| **size** | **Integer**| Page Size | [optional] |

### Return type

[**GetLinksTopDomains200Response**](GetLinksTopDomains200Response.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **0** | error payload |  -  |

<a id="getPageRankLost"></a>
# **getPageRankLost**
> PageRankLost getPageRankLost(username, projectSlug, analysisSlug)

Lost pagerank

Lost pagerank

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.botify.com/v1");
    
    // Configure API key authorization: DjangoRestToken
    ApiKeyAuth DjangoRestToken = (ApiKeyAuth) defaultClient.getAuthentication("DjangoRestToken");
    DjangoRestToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //DjangoRestToken.setApiKeyPrefix("Token");

    AnalysisApi apiInstance = new AnalysisApi(defaultClient);
    String username = "username_example"; // String | User's identifier
    String projectSlug = "projectSlug_example"; // String | Project's identifier
    String analysisSlug = "analysisSlug_example"; // String | Analysis' identifier
    try {
      PageRankLost result = apiInstance.getPageRankLost(username, projectSlug, analysisSlug);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysisApi#getPageRankLost");
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
| **username** | **String**| User&#39;s identifier | |
| **projectSlug** | **String**| Project&#39;s identifier | |
| **analysisSlug** | **String**| Analysis&#39; identifier | |

### Return type

[**PageRankLost**](PageRankLost.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **0** | error payload |  -  |

<a id="getSitemapsReport"></a>
# **getSitemapsReport**
> SitemapsReport getSitemapsReport(username, projectSlug, analysisSlug)

Get global information of the sitemaps found (sitemaps indexes, invalid sitemaps urls, etc

Get global information of the sitemaps found (sitemaps indexes, invalid sitemaps urls, etc.)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.botify.com/v1");
    
    // Configure API key authorization: DjangoRestToken
    ApiKeyAuth DjangoRestToken = (ApiKeyAuth) defaultClient.getAuthentication("DjangoRestToken");
    DjangoRestToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //DjangoRestToken.setApiKeyPrefix("Token");

    AnalysisApi apiInstance = new AnalysisApi(defaultClient);
    String username = "username_example"; // String | User's identifier
    String projectSlug = "projectSlug_example"; // String | Project's identifier
    String analysisSlug = "analysisSlug_example"; // String | Analysis' identifier
    try {
      SitemapsReport result = apiInstance.getSitemapsReport(username, projectSlug, analysisSlug);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysisApi#getSitemapsReport");
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
| **username** | **String**| User&#39;s identifier | |
| **projectSlug** | **String**| Project&#39;s identifier | |
| **analysisSlug** | **String**| Analysis&#39; identifier | |

### Return type

[**SitemapsReport**](SitemapsReport.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **0** | error payload |  -  |

<a id="getSitemapsSamplesOutOfConfig"></a>
# **getSitemapsSamplesOutOfConfig**
> GetSitemapsSamplesOutOfConfig200Response getSitemapsSamplesOutOfConfig(username, projectSlug, analysisSlug, page, size)

Sample list of URLs which were found in your sitemaps but outside of the

Sample list of URLs which were found in your sitemaps but outside of the crawl perimeter defined for the project, for instance domain/subdomain or protocol (HTTP/HTTPS) not allowed in the crawl settings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.botify.com/v1");
    
    // Configure API key authorization: DjangoRestToken
    ApiKeyAuth DjangoRestToken = (ApiKeyAuth) defaultClient.getAuthentication("DjangoRestToken");
    DjangoRestToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //DjangoRestToken.setApiKeyPrefix("Token");

    AnalysisApi apiInstance = new AnalysisApi(defaultClient);
    String username = "username_example"; // String | User's identifier
    String projectSlug = "projectSlug_example"; // String | Project's identifier
    String analysisSlug = "analysisSlug_example"; // String | Analysis' identifier
    Integer page = 56; // Integer | Page Number
    Integer size = 56; // Integer | Page Size
    try {
      GetSitemapsSamplesOutOfConfig200Response result = apiInstance.getSitemapsSamplesOutOfConfig(username, projectSlug, analysisSlug, page, size);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysisApi#getSitemapsSamplesOutOfConfig");
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
| **username** | **String**| User&#39;s identifier | |
| **projectSlug** | **String**| Project&#39;s identifier | |
| **analysisSlug** | **String**| Analysis&#39; identifier | |
| **page** | **Integer**| Page Number | [optional] |
| **size** | **Integer**| Page Size | [optional] |

### Return type

[**GetSitemapsSamplesOutOfConfig200Response**](GetSitemapsSamplesOutOfConfig200Response.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **0** | error payload |  -  |

<a id="getSitemapsSamplesSitemapsOnly"></a>
# **getSitemapsSamplesSitemapsOnly**
> GetSitemapsSamplesOutOfConfig200Response getSitemapsSamplesSitemapsOnly(username, projectSlug, analysisSlug, page, size)

Sample list of URLs which were found in your sitemaps, within the project

Sample list of URLs which were found in your sitemaps, within the project allowed scope (allowed domains/subdomains/protocols), but not found by the Botify crawler.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.botify.com/v1");
    
    // Configure API key authorization: DjangoRestToken
    ApiKeyAuth DjangoRestToken = (ApiKeyAuth) defaultClient.getAuthentication("DjangoRestToken");
    DjangoRestToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //DjangoRestToken.setApiKeyPrefix("Token");

    AnalysisApi apiInstance = new AnalysisApi(defaultClient);
    String username = "username_example"; // String | User's identifier
    String projectSlug = "projectSlug_example"; // String | Project's identifier
    String analysisSlug = "analysisSlug_example"; // String | Analysis' identifier
    Integer page = 56; // Integer | Page Number
    Integer size = 56; // Integer | Page Size
    try {
      GetSitemapsSamplesOutOfConfig200Response result = apiInstance.getSitemapsSamplesSitemapsOnly(username, projectSlug, analysisSlug, page, size);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysisApi#getSitemapsSamplesSitemapsOnly");
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
| **username** | **String**| User&#39;s identifier | |
| **projectSlug** | **String**| Project&#39;s identifier | |
| **analysisSlug** | **String**| Analysis&#39; identifier | |
| **page** | **Integer**| Page Number | [optional] |
| **size** | **Integer**| Page Size | [optional] |

### Return type

[**GetSitemapsSamplesOutOfConfig200Response**](GetSitemapsSamplesOutOfConfig200Response.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **0** | error payload |  -  |

<a id="getUrlDetail"></a>
# **getUrlDetail**
> Object getUrlDetail(username, projectSlug, analysisSlug, url, fields)

Gets the detail of an URL for an analysis

Gets the detail of an URL for an analysis

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.botify.com/v1");
    
    // Configure API key authorization: DjangoRestToken
    ApiKeyAuth DjangoRestToken = (ApiKeyAuth) defaultClient.getAuthentication("DjangoRestToken");
    DjangoRestToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //DjangoRestToken.setApiKeyPrefix("Token");

    AnalysisApi apiInstance = new AnalysisApi(defaultClient);
    String username = "username_example"; // String | User's identifier
    String projectSlug = "projectSlug_example"; // String | Project's identifier
    String analysisSlug = "analysisSlug_example"; // String | Analysis' identifier
    String url = "url_example"; // String | (Urlencoded) Searched URL
    List<String> fields = Arrays.asList(); // List<String> | comma separated list of fields to return (c.f. URLs Datamodel)
    try {
      Object result = apiInstance.getUrlDetail(username, projectSlug, analysisSlug, url, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysisApi#getUrlDetail");
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
| **username** | **String**| User&#39;s identifier | |
| **projectSlug** | **String**| Project&#39;s identifier | |
| **analysisSlug** | **String**| Analysis&#39; identifier | |
| **url** | **String**| (Urlencoded) Searched URL | |
| **fields** | [**List&lt;String&gt;**](String.md)| comma separated list of fields to return (c.f. URLs Datamodel) | [optional] |

### Return type

**Object**

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **0** | error payload |  -  |

<a id="getUrls"></a>
# **getUrls**
> GetUrls200Response getUrls(username, projectSlug, analysisSlug, area, page, size, urlsQuery)

Executes a query and returns a paginated response

Executes a query and returns a paginated response

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.botify.com/v1");
    
    // Configure API key authorization: DjangoRestToken
    ApiKeyAuth DjangoRestToken = (ApiKeyAuth) defaultClient.getAuthentication("DjangoRestToken");
    DjangoRestToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //DjangoRestToken.setApiKeyPrefix("Token");

    AnalysisApi apiInstance = new AnalysisApi(defaultClient);
    String username = "username_example"; // String | User's identifier
    String projectSlug = "projectSlug_example"; // String | Project's identifier
    String analysisSlug = "analysisSlug_example"; // String | Analysis' identifier
    String area = "current"; // String | Analysis context to execute the query
    Integer page = 56; // Integer | Page Number
    Integer size = 56; // Integer | Page Size
    UrlsQuery urlsQuery = new UrlsQuery(); // UrlsQuery | 
    try {
      GetUrls200Response result = apiInstance.getUrls(username, projectSlug, analysisSlug, area, page, size, urlsQuery);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysisApi#getUrls");
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
| **username** | **String**| User&#39;s identifier | |
| **projectSlug** | **String**| Project&#39;s identifier | |
| **analysisSlug** | **String**| Analysis&#39; identifier | |
| **area** | **String**| Analysis context to execute the query | [optional] [default to current] [enum: current, disappeared, new, search_engines_orphans] |
| **page** | **Integer**| Page Number | [optional] |
| **size** | **Integer**| Page Size | [optional] |
| **urlsQuery** | [**UrlsQuery**](UrlsQuery.md)|  | [optional] |

### Return type

[**GetUrls200Response**](GetUrls200Response.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **0** | error payload |  -  |

<a id="getUrlsAggs"></a>
# **getUrlsAggs**
> List&lt;Object&gt; getUrlsAggs(username, projectSlug, analysisSlug, area, urlsAggsQuery)

Query aggregator

Query aggregator. It accepts multiple queries

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.botify.com/v1");
    
    // Configure API key authorization: DjangoRestToken
    ApiKeyAuth DjangoRestToken = (ApiKeyAuth) defaultClient.getAuthentication("DjangoRestToken");
    DjangoRestToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //DjangoRestToken.setApiKeyPrefix("Token");

    AnalysisApi apiInstance = new AnalysisApi(defaultClient);
    String username = "username_example"; // String | User's identifier
    String projectSlug = "projectSlug_example"; // String | Project's identifier
    String analysisSlug = "analysisSlug_example"; // String | Analysis' identifier
    String area = "current"; // String | 
    List<UrlsAggsQuery> urlsAggsQuery = Arrays.asList(); // List<UrlsAggsQuery> | 
    try {
      List<Object> result = apiInstance.getUrlsAggs(username, projectSlug, analysisSlug, area, urlsAggsQuery);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysisApi#getUrlsAggs");
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
| **username** | **String**| User&#39;s identifier | |
| **projectSlug** | **String**| Project&#39;s identifier | |
| **analysisSlug** | **String**| Analysis&#39; identifier | |
| **area** | **String**|  | [optional] [default to current] [enum: current, disappeared, new, search_engines_orphans] |
| **urlsAggsQuery** | [**List&lt;UrlsAggsQuery&gt;**](UrlsAggsQuery.md)|  | [optional] |

### Return type

**List&lt;Object&gt;**

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **0** | error payload |  -  |

<a id="getUrlsDatamodel"></a>
# **getUrlsDatamodel**
> CrawlDatamodel getUrlsDatamodel(username, projectSlug, analysisSlug, area)

Gets an Analysis datamodel

Gets an Analysis datamodel

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.botify.com/v1");
    
    // Configure API key authorization: DjangoRestToken
    ApiKeyAuth DjangoRestToken = (ApiKeyAuth) defaultClient.getAuthentication("DjangoRestToken");
    DjangoRestToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //DjangoRestToken.setApiKeyPrefix("Token");

    AnalysisApi apiInstance = new AnalysisApi(defaultClient);
    String username = "username_example"; // String | User's identifier
    String projectSlug = "projectSlug_example"; // String | Project's identifier
    String analysisSlug = "analysisSlug_example"; // String | Analysis' identifier
    String area = "current"; // String | 
    try {
      CrawlDatamodel result = apiInstance.getUrlsDatamodel(username, projectSlug, analysisSlug, area);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysisApi#getUrlsDatamodel");
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
| **username** | **String**| User&#39;s identifier | |
| **projectSlug** | **String**| Project&#39;s identifier | |
| **analysisSlug** | **String**| Analysis&#39; identifier | |
| **area** | **String**|  | [optional] [default to current] [enum: current, disappeared, new, search_engines_orphans] |

### Return type

[**CrawlDatamodel**](CrawlDatamodel.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **0** | error payload |  -  |

<a id="getUrlsExportStatus"></a>
# **getUrlsExportStatus**
> CsvExportStatus getUrlsExportStatus(username, projectSlug, analysisSlug, urlExportId)

Checks the status of an CSVUrlExportJob object

Checks the status of an CSVUrlExportJob object. Returns json object with the status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.botify.com/v1");
    
    // Configure API key authorization: DjangoRestToken
    ApiKeyAuth DjangoRestToken = (ApiKeyAuth) defaultClient.getAuthentication("DjangoRestToken");
    DjangoRestToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //DjangoRestToken.setApiKeyPrefix("Token");

    AnalysisApi apiInstance = new AnalysisApi(defaultClient);
    String username = "username_example"; // String | User's identifier
    String projectSlug = "projectSlug_example"; // String | Project's identifier
    String analysisSlug = "analysisSlug_example"; // String | Analysis' identifier
    String urlExportId = "urlExportId_example"; // String | Url Export ID
    try {
      CsvExportStatus result = apiInstance.getUrlsExportStatus(username, projectSlug, analysisSlug, urlExportId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysisApi#getUrlsExportStatus");
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
| **username** | **String**| User&#39;s identifier | |
| **projectSlug** | **String**| Project&#39;s identifier | |
| **analysisSlug** | **String**| Analysis&#39; identifier | |
| **urlExportId** | **String**| Url Export ID | |

### Return type

[**CsvExportStatus**](CsvExportStatus.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **0** | error payload |  -  |

<a id="getUrlsExports"></a>
# **getUrlsExports**
> GetUrlsExports200Response getUrlsExports(username, projectSlug, analysisSlug, page, size)

A list of the CSV Exports requests and their current status

A list of the CSV Exports requests and their current status

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.botify.com/v1");
    
    // Configure API key authorization: DjangoRestToken
    ApiKeyAuth DjangoRestToken = (ApiKeyAuth) defaultClient.getAuthentication("DjangoRestToken");
    DjangoRestToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //DjangoRestToken.setApiKeyPrefix("Token");

    AnalysisApi apiInstance = new AnalysisApi(defaultClient);
    String username = "username_example"; // String | User's identifier
    String projectSlug = "projectSlug_example"; // String | Project's identifier
    String analysisSlug = "analysisSlug_example"; // String | Analysis' identifier
    Integer page = 56; // Integer | Page Number
    Integer size = 56; // Integer | Page Size
    try {
      GetUrlsExports200Response result = apiInstance.getUrlsExports(username, projectSlug, analysisSlug, page, size);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysisApi#getUrlsExports");
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
| **username** | **String**| User&#39;s identifier | |
| **projectSlug** | **String**| Project&#39;s identifier | |
| **analysisSlug** | **String**| Analysis&#39; identifier | |
| **page** | **Integer**| Page Number | [optional] |
| **size** | **Integer**| Page Size | [optional] |

### Return type

[**GetUrlsExports200Response**](GetUrlsExports200Response.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **0** | error payload |  -  |

<a id="getUrlsSuggestedFilters"></a>
# **getUrlsSuggestedFilters**
> UrlsAggsQuery getUrlsSuggestedFilters(username, projectSlug, analysisSlug, area, urlsAggsQuery)

Return most frequent segments (&#x3D; suggested patterns in the previous version)

Return most frequent segments (&#x3D; suggested patterns in the previous version) for a Botify Query.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.botify.com/v1");
    
    // Configure API key authorization: DjangoRestToken
    ApiKeyAuth DjangoRestToken = (ApiKeyAuth) defaultClient.getAuthentication("DjangoRestToken");
    DjangoRestToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //DjangoRestToken.setApiKeyPrefix("Token");

    AnalysisApi apiInstance = new AnalysisApi(defaultClient);
    String username = "username_example"; // String | User's identifier
    String projectSlug = "projectSlug_example"; // String | Project's identifier
    String analysisSlug = "analysisSlug_example"; // String | Analysis' identifier
    String area = "current"; // String | 
    UrlsAggsQuery urlsAggsQuery = new UrlsAggsQuery(); // UrlsAggsQuery | 
    try {
      UrlsAggsQuery result = apiInstance.getUrlsSuggestedFilters(username, projectSlug, analysisSlug, area, urlsAggsQuery);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysisApi#getUrlsSuggestedFilters");
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
| **username** | **String**| User&#39;s identifier | |
| **projectSlug** | **String**| Project&#39;s identifier | |
| **analysisSlug** | **String**| Analysis&#39; identifier | |
| **area** | **String**|  | [optional] [default to current] [enum: current, new] |
| **urlsAggsQuery** | [**UrlsAggsQuery**](UrlsAggsQuery.md)|  | [optional] |

### Return type

[**UrlsAggsQuery**](UrlsAggsQuery.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |
| **0** | error payload |  -  |

