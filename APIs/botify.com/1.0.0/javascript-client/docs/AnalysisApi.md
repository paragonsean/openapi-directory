# BotifyApi.AnalysisApi

All URIs are relative to *https://api.botify.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createUrlsExport**](AnalysisApi.md#createUrlsExport) | **POST** /analyses/{username}/{project_slug}/{analysis_slug}/urls/export | Creates a new UrlExport object and starts a task that will export the results into a csv
[**getAnalysisSummary**](AnalysisApi.md#getAnalysisSummary) | **GET** /analyses/{username}/{project_slug}/{analysis_slug} | Get an Analysis detail
[**getCrawlStatistics**](AnalysisApi.md#getCrawlStatistics) | **GET** /analyses/{username}/{project_slug}/{analysis_slug}/crawl_statistics | Return global statistics for an analysis
[**getCrawlStatisticsByFrequency**](AnalysisApi.md#getCrawlStatisticsByFrequency) | **GET** /analyses/{username}/{project_slug}/{analysis_slug}/crawl_statistics/time | Return crawl statistics grouped by time frequency (1 min, 5 mins or 60 min)
[**getCrawlStatisticsUrls**](AnalysisApi.md#getCrawlStatisticsUrls) | **GET** /analyses/{username}/{project_slug}/{analysis_slug}/crawl_statistics/urls/{list_type} | Return a list of 1000 latest URLs crawled (all crawled URLs or only URLS with HTTP errors)
[**getGanalyticsOrphanURLs**](AnalysisApi.md#getGanalyticsOrphanURLs) | **GET** /analyses/{username}/{project_slug}/{analysis_slug}/features/ganalytics/orphan_urls/{medium}/{source} | List of Orphan URLs
[**getLinksPercentiles**](AnalysisApi.md#getLinksPercentiles) | **GET** /analyses/{username}/{project_slug}/{analysis_slug}/features/links/percentiles | Get inlinks percentiles
[**getLinksTopDomains**](AnalysisApi.md#getLinksTopDomains) | **GET** /analyses/{username}/{project_slug}/{analysis_slug}/features/top_domains/domains | Top domains
[**getLinksTopSubdomains**](AnalysisApi.md#getLinksTopSubdomains) | **GET** /analyses/{username}/{project_slug}/{analysis_slug}/features/top_domains/subdomains | Top subddomains
[**getPageRankLost**](AnalysisApi.md#getPageRankLost) | **GET** /analyses/{username}/{project_slug}/{analysis_slug}/features/pagerank/lost | Lost pagerank
[**getSitemapsReport**](AnalysisApi.md#getSitemapsReport) | **GET** /analyses/{username}/{project_slug}/{analysis_slug}/features/sitemaps/report | Get global information of the sitemaps found (sitemaps indexes, invalid sitemaps urls, etc
[**getSitemapsSamplesOutOfConfig**](AnalysisApi.md#getSitemapsSamplesOutOfConfig) | **GET** /analyses/{username}/{project_slug}/{analysis_slug}/features/sitemaps/samples/out_of_config | Sample list of URLs which were found in your sitemaps but outside of the
[**getSitemapsSamplesSitemapsOnly**](AnalysisApi.md#getSitemapsSamplesSitemapsOnly) | **GET** /analyses/{username}/{project_slug}/{analysis_slug}/features/sitemaps/samples/sitemap_only | Sample list of URLs which were found in your sitemaps, within the project
[**getUrlDetail**](AnalysisApi.md#getUrlDetail) | **GET** /analyses/{username}/{project_slug}/{analysis_slug}/urls/{url} | Gets the detail of an URL for an analysis
[**getUrls**](AnalysisApi.md#getUrls) | **POST** /analyses/{username}/{project_slug}/{analysis_slug}/urls | Executes a query and returns a paginated response
[**getUrlsAggs**](AnalysisApi.md#getUrlsAggs) | **POST** /analyses/{username}/{project_slug}/{analysis_slug}/urls/aggs | Query aggregator
[**getUrlsDatamodel**](AnalysisApi.md#getUrlsDatamodel) | **GET** /analyses/{username}/{project_slug}/{analysis_slug}/urls/datamodel | Gets an Analysis datamodel
[**getUrlsExportStatus**](AnalysisApi.md#getUrlsExportStatus) | **GET** /analyses/{username}/{project_slug}/{analysis_slug}/urls/export/{url_export_id} | Checks the status of an CSVUrlExportJob object
[**getUrlsExports**](AnalysisApi.md#getUrlsExports) | **GET** /analyses/{username}/{project_slug}/{analysis_slug}/urls/export | A list of the CSV Exports requests and their current status
[**getUrlsSuggestedFilters**](AnalysisApi.md#getUrlsSuggestedFilters) | **POST** /analyses/{username}/{project_slug}/{analysis_slug}/urls/suggested_filters | Return most frequent segments (&#x3D; suggested patterns in the previous version)



## createUrlsExport

> CsvExportStatus createUrlsExport(username, projectSlug, analysisSlug, opts)

Creates a new UrlExport object and starts a task that will export the results into a csv

Creates a new UrlExport object and starts a task that will export the results into a csv. Returns the model id that manages the task

### Example

```javascript
import BotifyApi from 'botify_api';
let defaultClient = BotifyApi.ApiClient.instance;
// Configure API key authorization: DjangoRestToken
let DjangoRestToken = defaultClient.authentications['DjangoRestToken'];
DjangoRestToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//DjangoRestToken.apiKeyPrefix = 'Token';

let apiInstance = new BotifyApi.AnalysisApi();
let username = "username_example"; // String | User's identifier
let projectSlug = "projectSlug_example"; // String | Project's identifier
let analysisSlug = "analysisSlug_example"; // String | Analysis' identifier
let opts = {
  'area': "'current'", // String | 
  'urlsQuery': new BotifyApi.UrlsQuery() // UrlsQuery | 
};
apiInstance.createUrlsExport(username, projectSlug, analysisSlug, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| User&#39;s identifier | 
 **projectSlug** | **String**| Project&#39;s identifier | 
 **analysisSlug** | **String**| Analysis&#39; identifier | 
 **area** | **String**|  | [optional] [default to &#39;current&#39;]
 **urlsQuery** | [**UrlsQuery**](UrlsQuery.md)|  | [optional] 

### Return type

[**CsvExportStatus**](CsvExportStatus.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getAnalysisSummary

> AnalysisDetail getAnalysisSummary(username, projectSlug, analysisSlug)

Get an Analysis detail

Get an Analysis detail

### Example

```javascript
import BotifyApi from 'botify_api';
let defaultClient = BotifyApi.ApiClient.instance;
// Configure API key authorization: DjangoRestToken
let DjangoRestToken = defaultClient.authentications['DjangoRestToken'];
DjangoRestToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//DjangoRestToken.apiKeyPrefix = 'Token';

let apiInstance = new BotifyApi.AnalysisApi();
let username = "username_example"; // String | User's identifier
let projectSlug = "projectSlug_example"; // String | Project's identifier
let analysisSlug = "analysisSlug_example"; // String | Analysis' identifier
apiInstance.getAnalysisSummary(username, projectSlug, analysisSlug, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| User&#39;s identifier | 
 **projectSlug** | **String**| Project&#39;s identifier | 
 **analysisSlug** | **String**| Analysis&#39; identifier | 

### Return type

[**AnalysisDetail**](AnalysisDetail.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCrawlStatistics

> CrawlStatistics getCrawlStatistics(username, projectSlug, analysisSlug)

Return global statistics for an analysis

Return global statistics for an analysis

### Example

```javascript
import BotifyApi from 'botify_api';
let defaultClient = BotifyApi.ApiClient.instance;
// Configure API key authorization: DjangoRestToken
let DjangoRestToken = defaultClient.authentications['DjangoRestToken'];
DjangoRestToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//DjangoRestToken.apiKeyPrefix = 'Token';

let apiInstance = new BotifyApi.AnalysisApi();
let username = "username_example"; // String | User's identifier
let projectSlug = "projectSlug_example"; // String | Project's identifier
let analysisSlug = "analysisSlug_example"; // String | Analysis' identifier
apiInstance.getCrawlStatistics(username, projectSlug, analysisSlug, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| User&#39;s identifier | 
 **projectSlug** | **String**| Project&#39;s identifier | 
 **analysisSlug** | **String**| Analysis&#39; identifier | 

### Return type

[**CrawlStatistics**](CrawlStatistics.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCrawlStatisticsByFrequency

> CrawlStatisticsTime getCrawlStatisticsByFrequency(username, projectSlug, analysisSlug, frequency, opts)

Return crawl statistics grouped by time frequency (1 min, 5 mins or 60 min)

Return crawl statistics grouped by time frequency (1 min, 5 mins or 60 min) for an analysis

### Example

```javascript
import BotifyApi from 'botify_api';
let defaultClient = BotifyApi.ApiClient.instance;
// Configure API key authorization: DjangoRestToken
let DjangoRestToken = defaultClient.authentications['DjangoRestToken'];
DjangoRestToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//DjangoRestToken.apiKeyPrefix = 'Token';

let apiInstance = new BotifyApi.AnalysisApi();
let username = "username_example"; // String | User's identifier
let projectSlug = "projectSlug_example"; // String | Project's identifier
let analysisSlug = "analysisSlug_example"; // String | Analysis' identifier
let frequency = "frequency_example"; // String | Aggregation frequency
let opts = {
  'limit': 56 // Number | max number of elements to retrieve
};
apiInstance.getCrawlStatisticsByFrequency(username, projectSlug, analysisSlug, frequency, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| User&#39;s identifier | 
 **projectSlug** | **String**| Project&#39;s identifier | 
 **analysisSlug** | **String**| Analysis&#39; identifier | 
 **frequency** | **String**| Aggregation frequency | 
 **limit** | **Number**| max number of elements to retrieve | [optional] 

### Return type

[**CrawlStatisticsTime**](CrawlStatisticsTime.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCrawlStatisticsUrls

> [Object] getCrawlStatisticsUrls(username, projectSlug, analysisSlug, listType)

Return a list of 1000 latest URLs crawled (all crawled URLs or only URLS with HTTP errors)

Return a list of 1000 latest URLs crawled (all crawled URLs or only URLS with HTTP errors)

### Example

```javascript
import BotifyApi from 'botify_api';
let defaultClient = BotifyApi.ApiClient.instance;
// Configure API key authorization: DjangoRestToken
let DjangoRestToken = defaultClient.authentications['DjangoRestToken'];
DjangoRestToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//DjangoRestToken.apiKeyPrefix = 'Token';

let apiInstance = new BotifyApi.AnalysisApi();
let username = "username_example"; // String | User's identifier
let projectSlug = "projectSlug_example"; // String | Project's identifier
let analysisSlug = "analysisSlug_example"; // String | Analysis' identifier
let listType = "listType_example"; // String | URLs list type (crawled URLs or error URLs)
apiInstance.getCrawlStatisticsUrls(username, projectSlug, analysisSlug, listType, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| User&#39;s identifier | 
 **projectSlug** | **String**| Project&#39;s identifier | 
 **analysisSlug** | **String**| Analysis&#39; identifier | 
 **listType** | **String**| URLs list type (crawled URLs or error URLs) | 

### Return type

**[Object]**

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGanalyticsOrphanURLs

> GetGanalyticsOrphanURLs200Response getGanalyticsOrphanURLs(username, projectSlug, analysisSlug, medium, source, opts)

List of Orphan URLs

List of Orphan URLs. URLs which generated visits from the selected source according to Google Analytics data, but were not crawled with by the Botify crawler (either because no links to them were found on the website, or because the crawler was not allowed to follow these links according to the project settings).   For a search engine (medium: origanic; sources: all, aol, ask, baidu, bing, google, naver, yahoo, yandex) or a social network (medium: social; sources: all, facebook, google+, linkedin, pinterest, reddit, tumblr, twitter)

### Example

```javascript
import BotifyApi from 'botify_api';
let defaultClient = BotifyApi.ApiClient.instance;
// Configure API key authorization: DjangoRestToken
let DjangoRestToken = defaultClient.authentications['DjangoRestToken'];
DjangoRestToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//DjangoRestToken.apiKeyPrefix = 'Token';

let apiInstance = new BotifyApi.AnalysisApi();
let username = "username_example"; // String | User's identifier
let projectSlug = "projectSlug_example"; // String | Project's identifier
let analysisSlug = "analysisSlug_example"; // String | Analysis' identifier
let medium = "medium_example"; // String | Type of traffic, value: 'organic' (from search engine)or 'social' (from a social network)
let source = "source_example"; // String | Traffic source, value: name of the search engine or social network
let opts = {
  'page': 56, // Number | Page Number
  'size': 56 // Number | Page Size
};
apiInstance.getGanalyticsOrphanURLs(username, projectSlug, analysisSlug, medium, source, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| User&#39;s identifier | 
 **projectSlug** | **String**| Project&#39;s identifier | 
 **analysisSlug** | **String**| Analysis&#39; identifier | 
 **medium** | **String**| Type of traffic, value: &#39;organic&#39; (from search engine)or &#39;social&#39; (from a social network) | 
 **source** | **String**| Traffic source, value: name of the search engine or social network | 
 **page** | **Number**| Page Number | [optional] 
 **size** | **Number**| Page Size | [optional] 

### Return type

[**GetGanalyticsOrphanURLs200Response**](GetGanalyticsOrphanURLs200Response.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLinksPercentiles

> LinksPercentiles getLinksPercentiles(username, projectSlug, analysisSlug)

Get inlinks percentiles

Get inlinks percentiles

### Example

```javascript
import BotifyApi from 'botify_api';
let defaultClient = BotifyApi.ApiClient.instance;
// Configure API key authorization: DjangoRestToken
let DjangoRestToken = defaultClient.authentications['DjangoRestToken'];
DjangoRestToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//DjangoRestToken.apiKeyPrefix = 'Token';

let apiInstance = new BotifyApi.AnalysisApi();
let username = "username_example"; // String | User's identifier
let projectSlug = "projectSlug_example"; // String | Project's identifier
let analysisSlug = "analysisSlug_example"; // String | Analysis' identifier
apiInstance.getLinksPercentiles(username, projectSlug, analysisSlug, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| User&#39;s identifier | 
 **projectSlug** | **String**| Project&#39;s identifier | 
 **analysisSlug** | **String**| Analysis&#39; identifier | 

### Return type

[**LinksPercentiles**](LinksPercentiles.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLinksTopDomains

> GetLinksTopDomains200Response getLinksTopDomains(username, projectSlug, analysisSlug, opts)

Top domains

Top domains

### Example

```javascript
import BotifyApi from 'botify_api';
let defaultClient = BotifyApi.ApiClient.instance;
// Configure API key authorization: DjangoRestToken
let DjangoRestToken = defaultClient.authentications['DjangoRestToken'];
DjangoRestToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//DjangoRestToken.apiKeyPrefix = 'Token';

let apiInstance = new BotifyApi.AnalysisApi();
let username = "username_example"; // String | User's identifier
let projectSlug = "projectSlug_example"; // String | Project's identifier
let analysisSlug = "analysisSlug_example"; // String | Analysis' identifier
let opts = {
  'page': 56, // Number | Page Number
  'size': 56 // Number | Page Size
};
apiInstance.getLinksTopDomains(username, projectSlug, analysisSlug, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| User&#39;s identifier | 
 **projectSlug** | **String**| Project&#39;s identifier | 
 **analysisSlug** | **String**| Analysis&#39; identifier | 
 **page** | **Number**| Page Number | [optional] 
 **size** | **Number**| Page Size | [optional] 

### Return type

[**GetLinksTopDomains200Response**](GetLinksTopDomains200Response.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLinksTopSubdomains

> GetLinksTopDomains200Response getLinksTopSubdomains(username, projectSlug, analysisSlug, opts)

Top subddomains

Top subddomains

### Example

```javascript
import BotifyApi from 'botify_api';
let defaultClient = BotifyApi.ApiClient.instance;
// Configure API key authorization: DjangoRestToken
let DjangoRestToken = defaultClient.authentications['DjangoRestToken'];
DjangoRestToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//DjangoRestToken.apiKeyPrefix = 'Token';

let apiInstance = new BotifyApi.AnalysisApi();
let username = "username_example"; // String | User's identifier
let projectSlug = "projectSlug_example"; // String | Project's identifier
let analysisSlug = "analysisSlug_example"; // String | Analysis' identifier
let opts = {
  'page': 56, // Number | Page Number
  'size': 56 // Number | Page Size
};
apiInstance.getLinksTopSubdomains(username, projectSlug, analysisSlug, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| User&#39;s identifier | 
 **projectSlug** | **String**| Project&#39;s identifier | 
 **analysisSlug** | **String**| Analysis&#39; identifier | 
 **page** | **Number**| Page Number | [optional] 
 **size** | **Number**| Page Size | [optional] 

### Return type

[**GetLinksTopDomains200Response**](GetLinksTopDomains200Response.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPageRankLost

> PageRankLost getPageRankLost(username, projectSlug, analysisSlug)

Lost pagerank

Lost pagerank

### Example

```javascript
import BotifyApi from 'botify_api';
let defaultClient = BotifyApi.ApiClient.instance;
// Configure API key authorization: DjangoRestToken
let DjangoRestToken = defaultClient.authentications['DjangoRestToken'];
DjangoRestToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//DjangoRestToken.apiKeyPrefix = 'Token';

let apiInstance = new BotifyApi.AnalysisApi();
let username = "username_example"; // String | User's identifier
let projectSlug = "projectSlug_example"; // String | Project's identifier
let analysisSlug = "analysisSlug_example"; // String | Analysis' identifier
apiInstance.getPageRankLost(username, projectSlug, analysisSlug, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| User&#39;s identifier | 
 **projectSlug** | **String**| Project&#39;s identifier | 
 **analysisSlug** | **String**| Analysis&#39; identifier | 

### Return type

[**PageRankLost**](PageRankLost.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSitemapsReport

> SitemapsReport getSitemapsReport(username, projectSlug, analysisSlug)

Get global information of the sitemaps found (sitemaps indexes, invalid sitemaps urls, etc

Get global information of the sitemaps found (sitemaps indexes, invalid sitemaps urls, etc.)

### Example

```javascript
import BotifyApi from 'botify_api';
let defaultClient = BotifyApi.ApiClient.instance;
// Configure API key authorization: DjangoRestToken
let DjangoRestToken = defaultClient.authentications['DjangoRestToken'];
DjangoRestToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//DjangoRestToken.apiKeyPrefix = 'Token';

let apiInstance = new BotifyApi.AnalysisApi();
let username = "username_example"; // String | User's identifier
let projectSlug = "projectSlug_example"; // String | Project's identifier
let analysisSlug = "analysisSlug_example"; // String | Analysis' identifier
apiInstance.getSitemapsReport(username, projectSlug, analysisSlug, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| User&#39;s identifier | 
 **projectSlug** | **String**| Project&#39;s identifier | 
 **analysisSlug** | **String**| Analysis&#39; identifier | 

### Return type

[**SitemapsReport**](SitemapsReport.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSitemapsSamplesOutOfConfig

> GetSitemapsSamplesOutOfConfig200Response getSitemapsSamplesOutOfConfig(username, projectSlug, analysisSlug, opts)

Sample list of URLs which were found in your sitemaps but outside of the

Sample list of URLs which were found in your sitemaps but outside of the crawl perimeter defined for the project, for instance domain/subdomain or protocol (HTTP/HTTPS) not allowed in the crawl settings.

### Example

```javascript
import BotifyApi from 'botify_api';
let defaultClient = BotifyApi.ApiClient.instance;
// Configure API key authorization: DjangoRestToken
let DjangoRestToken = defaultClient.authentications['DjangoRestToken'];
DjangoRestToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//DjangoRestToken.apiKeyPrefix = 'Token';

let apiInstance = new BotifyApi.AnalysisApi();
let username = "username_example"; // String | User's identifier
let projectSlug = "projectSlug_example"; // String | Project's identifier
let analysisSlug = "analysisSlug_example"; // String | Analysis' identifier
let opts = {
  'page': 56, // Number | Page Number
  'size': 56 // Number | Page Size
};
apiInstance.getSitemapsSamplesOutOfConfig(username, projectSlug, analysisSlug, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| User&#39;s identifier | 
 **projectSlug** | **String**| Project&#39;s identifier | 
 **analysisSlug** | **String**| Analysis&#39; identifier | 
 **page** | **Number**| Page Number | [optional] 
 **size** | **Number**| Page Size | [optional] 

### Return type

[**GetSitemapsSamplesOutOfConfig200Response**](GetSitemapsSamplesOutOfConfig200Response.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSitemapsSamplesSitemapsOnly

> GetSitemapsSamplesOutOfConfig200Response getSitemapsSamplesSitemapsOnly(username, projectSlug, analysisSlug, opts)

Sample list of URLs which were found in your sitemaps, within the project

Sample list of URLs which were found in your sitemaps, within the project allowed scope (allowed domains/subdomains/protocols), but not found by the Botify crawler.

### Example

```javascript
import BotifyApi from 'botify_api';
let defaultClient = BotifyApi.ApiClient.instance;
// Configure API key authorization: DjangoRestToken
let DjangoRestToken = defaultClient.authentications['DjangoRestToken'];
DjangoRestToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//DjangoRestToken.apiKeyPrefix = 'Token';

let apiInstance = new BotifyApi.AnalysisApi();
let username = "username_example"; // String | User's identifier
let projectSlug = "projectSlug_example"; // String | Project's identifier
let analysisSlug = "analysisSlug_example"; // String | Analysis' identifier
let opts = {
  'page': 56, // Number | Page Number
  'size': 56 // Number | Page Size
};
apiInstance.getSitemapsSamplesSitemapsOnly(username, projectSlug, analysisSlug, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| User&#39;s identifier | 
 **projectSlug** | **String**| Project&#39;s identifier | 
 **analysisSlug** | **String**| Analysis&#39; identifier | 
 **page** | **Number**| Page Number | [optional] 
 **size** | **Number**| Page Size | [optional] 

### Return type

[**GetSitemapsSamplesOutOfConfig200Response**](GetSitemapsSamplesOutOfConfig200Response.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUrlDetail

> Object getUrlDetail(username, projectSlug, analysisSlug, url, opts)

Gets the detail of an URL for an analysis

Gets the detail of an URL for an analysis

### Example

```javascript
import BotifyApi from 'botify_api';
let defaultClient = BotifyApi.ApiClient.instance;
// Configure API key authorization: DjangoRestToken
let DjangoRestToken = defaultClient.authentications['DjangoRestToken'];
DjangoRestToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//DjangoRestToken.apiKeyPrefix = 'Token';

let apiInstance = new BotifyApi.AnalysisApi();
let username = "username_example"; // String | User's identifier
let projectSlug = "projectSlug_example"; // String | Project's identifier
let analysisSlug = "analysisSlug_example"; // String | Analysis' identifier
let url = "url_example"; // String | (Urlencoded) Searched URL
let opts = {
  'fields': ["null"] // [String] | comma separated list of fields to return (c.f. URLs Datamodel)
};
apiInstance.getUrlDetail(username, projectSlug, analysisSlug, url, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| User&#39;s identifier | 
 **projectSlug** | **String**| Project&#39;s identifier | 
 **analysisSlug** | **String**| Analysis&#39; identifier | 
 **url** | **String**| (Urlencoded) Searched URL | 
 **fields** | [**[String]**](String.md)| comma separated list of fields to return (c.f. URLs Datamodel) | [optional] 

### Return type

**Object**

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUrls

> GetUrls200Response getUrls(username, projectSlug, analysisSlug, opts)

Executes a query and returns a paginated response

Executes a query and returns a paginated response

### Example

```javascript
import BotifyApi from 'botify_api';
let defaultClient = BotifyApi.ApiClient.instance;
// Configure API key authorization: DjangoRestToken
let DjangoRestToken = defaultClient.authentications['DjangoRestToken'];
DjangoRestToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//DjangoRestToken.apiKeyPrefix = 'Token';

let apiInstance = new BotifyApi.AnalysisApi();
let username = "username_example"; // String | User's identifier
let projectSlug = "projectSlug_example"; // String | Project's identifier
let analysisSlug = "analysisSlug_example"; // String | Analysis' identifier
let opts = {
  'area': "'current'", // String | Analysis context to execute the query
  'page': 56, // Number | Page Number
  'size': 56, // Number | Page Size
  'urlsQuery': new BotifyApi.UrlsQuery() // UrlsQuery | 
};
apiInstance.getUrls(username, projectSlug, analysisSlug, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| User&#39;s identifier | 
 **projectSlug** | **String**| Project&#39;s identifier | 
 **analysisSlug** | **String**| Analysis&#39; identifier | 
 **area** | **String**| Analysis context to execute the query | [optional] [default to &#39;current&#39;]
 **page** | **Number**| Page Number | [optional] 
 **size** | **Number**| Page Size | [optional] 
 **urlsQuery** | [**UrlsQuery**](UrlsQuery.md)|  | [optional] 

### Return type

[**GetUrls200Response**](GetUrls200Response.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getUrlsAggs

> [Object] getUrlsAggs(username, projectSlug, analysisSlug, opts)

Query aggregator

Query aggregator. It accepts multiple queries

### Example

```javascript
import BotifyApi from 'botify_api';
let defaultClient = BotifyApi.ApiClient.instance;
// Configure API key authorization: DjangoRestToken
let DjangoRestToken = defaultClient.authentications['DjangoRestToken'];
DjangoRestToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//DjangoRestToken.apiKeyPrefix = 'Token';

let apiInstance = new BotifyApi.AnalysisApi();
let username = "username_example"; // String | User's identifier
let projectSlug = "projectSlug_example"; // String | Project's identifier
let analysisSlug = "analysisSlug_example"; // String | Analysis' identifier
let opts = {
  'area': "'current'", // String | 
  'urlsAggsQuery': [new BotifyApi.UrlsAggsQuery()] // [UrlsAggsQuery] | 
};
apiInstance.getUrlsAggs(username, projectSlug, analysisSlug, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| User&#39;s identifier | 
 **projectSlug** | **String**| Project&#39;s identifier | 
 **analysisSlug** | **String**| Analysis&#39; identifier | 
 **area** | **String**|  | [optional] [default to &#39;current&#39;]
 **urlsAggsQuery** | [**[UrlsAggsQuery]**](UrlsAggsQuery.md)|  | [optional] 

### Return type

**[Object]**

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getUrlsDatamodel

> CrawlDatamodel getUrlsDatamodel(username, projectSlug, analysisSlug, opts)

Gets an Analysis datamodel

Gets an Analysis datamodel

### Example

```javascript
import BotifyApi from 'botify_api';
let defaultClient = BotifyApi.ApiClient.instance;
// Configure API key authorization: DjangoRestToken
let DjangoRestToken = defaultClient.authentications['DjangoRestToken'];
DjangoRestToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//DjangoRestToken.apiKeyPrefix = 'Token';

let apiInstance = new BotifyApi.AnalysisApi();
let username = "username_example"; // String | User's identifier
let projectSlug = "projectSlug_example"; // String | Project's identifier
let analysisSlug = "analysisSlug_example"; // String | Analysis' identifier
let opts = {
  'area': "'current'" // String | 
};
apiInstance.getUrlsDatamodel(username, projectSlug, analysisSlug, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| User&#39;s identifier | 
 **projectSlug** | **String**| Project&#39;s identifier | 
 **analysisSlug** | **String**| Analysis&#39; identifier | 
 **area** | **String**|  | [optional] [default to &#39;current&#39;]

### Return type

[**CrawlDatamodel**](CrawlDatamodel.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUrlsExportStatus

> CsvExportStatus getUrlsExportStatus(username, projectSlug, analysisSlug, urlExportId)

Checks the status of an CSVUrlExportJob object

Checks the status of an CSVUrlExportJob object. Returns json object with the status.

### Example

```javascript
import BotifyApi from 'botify_api';
let defaultClient = BotifyApi.ApiClient.instance;
// Configure API key authorization: DjangoRestToken
let DjangoRestToken = defaultClient.authentications['DjangoRestToken'];
DjangoRestToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//DjangoRestToken.apiKeyPrefix = 'Token';

let apiInstance = new BotifyApi.AnalysisApi();
let username = "username_example"; // String | User's identifier
let projectSlug = "projectSlug_example"; // String | Project's identifier
let analysisSlug = "analysisSlug_example"; // String | Analysis' identifier
let urlExportId = "urlExportId_example"; // String | Url Export ID
apiInstance.getUrlsExportStatus(username, projectSlug, analysisSlug, urlExportId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| User&#39;s identifier | 
 **projectSlug** | **String**| Project&#39;s identifier | 
 **analysisSlug** | **String**| Analysis&#39; identifier | 
 **urlExportId** | **String**| Url Export ID | 

### Return type

[**CsvExportStatus**](CsvExportStatus.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUrlsExports

> GetUrlsExports200Response getUrlsExports(username, projectSlug, analysisSlug, opts)

A list of the CSV Exports requests and their current status

A list of the CSV Exports requests and their current status

### Example

```javascript
import BotifyApi from 'botify_api';
let defaultClient = BotifyApi.ApiClient.instance;
// Configure API key authorization: DjangoRestToken
let DjangoRestToken = defaultClient.authentications['DjangoRestToken'];
DjangoRestToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//DjangoRestToken.apiKeyPrefix = 'Token';

let apiInstance = new BotifyApi.AnalysisApi();
let username = "username_example"; // String | User's identifier
let projectSlug = "projectSlug_example"; // String | Project's identifier
let analysisSlug = "analysisSlug_example"; // String | Analysis' identifier
let opts = {
  'page': 56, // Number | Page Number
  'size': 56 // Number | Page Size
};
apiInstance.getUrlsExports(username, projectSlug, analysisSlug, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| User&#39;s identifier | 
 **projectSlug** | **String**| Project&#39;s identifier | 
 **analysisSlug** | **String**| Analysis&#39; identifier | 
 **page** | **Number**| Page Number | [optional] 
 **size** | **Number**| Page Size | [optional] 

### Return type

[**GetUrlsExports200Response**](GetUrlsExports200Response.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUrlsSuggestedFilters

> UrlsAggsQuery getUrlsSuggestedFilters(username, projectSlug, analysisSlug, opts)

Return most frequent segments (&#x3D; suggested patterns in the previous version)

Return most frequent segments (&#x3D; suggested patterns in the previous version) for a Botify Query.

### Example

```javascript
import BotifyApi from 'botify_api';
let defaultClient = BotifyApi.ApiClient.instance;
// Configure API key authorization: DjangoRestToken
let DjangoRestToken = defaultClient.authentications['DjangoRestToken'];
DjangoRestToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//DjangoRestToken.apiKeyPrefix = 'Token';

let apiInstance = new BotifyApi.AnalysisApi();
let username = "username_example"; // String | User's identifier
let projectSlug = "projectSlug_example"; // String | Project's identifier
let analysisSlug = "analysisSlug_example"; // String | Analysis' identifier
let opts = {
  'area': "'current'", // String | 
  'urlsAggsQuery': new BotifyApi.UrlsAggsQuery() // UrlsAggsQuery | 
};
apiInstance.getUrlsSuggestedFilters(username, projectSlug, analysisSlug, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| User&#39;s identifier | 
 **projectSlug** | **String**| Project&#39;s identifier | 
 **analysisSlug** | **String**| Analysis&#39; identifier | 
 **area** | **String**|  | [optional] [default to &#39;current&#39;]
 **urlsAggsQuery** | [**UrlsAggsQuery**](UrlsAggsQuery.md)|  | [optional] 

### Return type

[**UrlsAggsQuery**](UrlsAggsQuery.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

