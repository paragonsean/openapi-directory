# Wikimedia.PageviewsDataApi

All URIs are relative to *https://wikimedia.org/api/rest_v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metricsPageviewsAggregateProjectAccessAgentGranularityStartEndGet**](PageviewsDataApi.md#metricsPageviewsAggregateProjectAccessAgentGranularityStartEndGet) | **GET** /metrics/pageviews/aggregate/{project}/{access}/{agent}/{granularity}/{start}/{end} | Get pageview counts for a project.
[**metricsPageviewsPerArticleProjectAccessAgentArticleGranularityStartEndGet**](PageviewsDataApi.md#metricsPageviewsPerArticleProjectAccessAgentArticleGranularityStartEndGet) | **GET** /metrics/pageviews/per-article/{project}/{access}/{agent}/{article}/{granularity}/{start}/{end} | Get pageview counts for a page.
[**metricsPageviewsTopByCountryProjectAccessYearMonthGet**](PageviewsDataApi.md#metricsPageviewsTopByCountryProjectAccessYearMonthGet) | **GET** /metrics/pageviews/top-by-country/{project}/{access}/{year}/{month} | Get pageviews by country and access method.
[**metricsPageviewsTopProjectAccessYearMonthDayGet**](PageviewsDataApi.md#metricsPageviewsTopProjectAccessYearMonthDayGet) | **GET** /metrics/pageviews/top/{project}/{access}/{year}/{month}/{day} | Get the most viewed articles for a project.



## metricsPageviewsAggregateProjectAccessAgentGranularityStartEndGet

> PageviewProject metricsPageviewsAggregateProjectAccessAgentGranularityStartEndGet(project, access, agent, granularity, start, end)

Get pageview counts for a project.

Given a date range, returns a timeseries of pageview counts. You can filter by project, access method and/or agent type. You can choose between daily and hourly granularity as well.  - Stability: [stable](https://www.mediawiki.org/wiki/API_versioning#Stable) - Rate limit: 100 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

### Example

```javascript
import Wikimedia from 'wikimedia';

let apiInstance = new Wikimedia.PageviewsDataApi();
let project = "project_example"; // String | If you want to filter by project, use the domain of any Wikimedia project, for example 'en.wikipedia.org', 'www.mediawiki.org' or 'commons.wikimedia.org'. If you are interested in all pageviews regardless of project, use all-projects. 
let access = "access_example"; // String | If you want to filter by access method, use one of desktop, mobile-app or mobile-web. If you are interested in pageviews regardless of access method, use all-access. 
let agent = "agent_example"; // String | If you want to filter by agent type, use one of user or spider. If you are interested in pageviews regardless of agent type, use all-agents. 
let granularity = "granularity_example"; // String | The time unit for the response data. As of today, the supported granularities for this endpoint are hourly, daily, and monthly. 
let start = "start_example"; // String | The timestamp of the first hour/day/month to include, in YYYYMMDDHH format
let end = "end_example"; // String | The timestamp of the last hour/day/month to include, in YYYYMMDDHH format
apiInstance.metricsPageviewsAggregateProjectAccessAgentGranularityStartEndGet(project, access, agent, granularity, start, end, (error, data, response) => {
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
 **project** | **String**| If you want to filter by project, use the domain of any Wikimedia project, for example &#39;en.wikipedia.org&#39;, &#39;www.mediawiki.org&#39; or &#39;commons.wikimedia.org&#39;. If you are interested in all pageviews regardless of project, use all-projects.  | 
 **access** | **String**| If you want to filter by access method, use one of desktop, mobile-app or mobile-web. If you are interested in pageviews regardless of access method, use all-access.  | 
 **agent** | **String**| If you want to filter by agent type, use one of user or spider. If you are interested in pageviews regardless of agent type, use all-agents.  | 
 **granularity** | **String**| The time unit for the response data. As of today, the supported granularities for this endpoint are hourly, daily, and monthly.  | 
 **start** | **String**| The timestamp of the first hour/day/month to include, in YYYYMMDDHH format | 
 **end** | **String**| The timestamp of the last hour/day/month to include, in YYYYMMDDHH format | 

### Return type

[**PageviewProject**](PageviewProject.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## metricsPageviewsPerArticleProjectAccessAgentArticleGranularityStartEndGet

> PageviewArticle metricsPageviewsPerArticleProjectAccessAgentArticleGranularityStartEndGet(project, access, agent, article, granularity, start, end)

Get pageview counts for a page.

Given a Mediawiki article and a date range, returns a daily timeseries of its pageview counts. You can also filter by access method and/or agent type.  - Stability: [stable](https://www.mediawiki.org/wiki/API_versioning#Stable) - Rate limit: 100 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

### Example

```javascript
import Wikimedia from 'wikimedia';

let apiInstance = new Wikimedia.PageviewsDataApi();
let project = "project_example"; // String | If you want to filter by project, use the domain of any Wikimedia project, for example 'en.wikipedia.org', 'www.mediawiki.org' or 'commons.wikimedia.org'. 
let access = "access_example"; // String | If you want to filter by access method, use one of desktop, mobile-app or mobile-web. If you are interested in pageviews regardless of access method, use all-access. 
let agent = "agent_example"; // String | If you want to filter by agent type, use one of user, bot or spider. If you are interested in pageviews regardless of agent type, use all-agents. 
let article = "article_example"; // String | 'The title of any article in the specified project. Any spaces should be replaced with underscores. It also should be URI-encoded, so that non-URI-safe characters like %, / or ? are accepted. Example: Are_You_the_One%3F'. 
let granularity = "granularity_example"; // String | The time unit for the response data. As of today, the only supported granularity for this endpoint is daily and monthly. 
let start = "start_example"; // String | The date of the first day to include, in YYYYMMDD or YYYYMMDDHH format
let end = "end_example"; // String | The date of the last day to include, in YYYYMMDD or YYYYMMDDHH format
apiInstance.metricsPageviewsPerArticleProjectAccessAgentArticleGranularityStartEndGet(project, access, agent, article, granularity, start, end, (error, data, response) => {
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
 **project** | **String**| If you want to filter by project, use the domain of any Wikimedia project, for example &#39;en.wikipedia.org&#39;, &#39;www.mediawiki.org&#39; or &#39;commons.wikimedia.org&#39;.  | 
 **access** | **String**| If you want to filter by access method, use one of desktop, mobile-app or mobile-web. If you are interested in pageviews regardless of access method, use all-access.  | 
 **agent** | **String**| If you want to filter by agent type, use one of user, bot or spider. If you are interested in pageviews regardless of agent type, use all-agents.  | 
 **article** | **String**| &#39;The title of any article in the specified project. Any spaces should be replaced with underscores. It also should be URI-encoded, so that non-URI-safe characters like %, / or ? are accepted. Example: Are_You_the_One%3F&#39;.  | 
 **granularity** | **String**| The time unit for the response data. As of today, the only supported granularity for this endpoint is daily and monthly.  | 
 **start** | **String**| The date of the first day to include, in YYYYMMDD or YYYYMMDDHH format | 
 **end** | **String**| The date of the last day to include, in YYYYMMDD or YYYYMMDDHH format | 

### Return type

[**PageviewArticle**](PageviewArticle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## metricsPageviewsTopByCountryProjectAccessYearMonthGet

> ByCountry metricsPageviewsTopByCountryProjectAccessYearMonthGet(project, access, year, month)

Get pageviews by country and access method.

Lists the pageviews to this project, split by country of origin for a given month. Because of privacy reasons, pageviews are given in a bucketed format, and countries with less than 100 views do not get reported. Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental) - Rate limit: 100 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

### Example

```javascript
import Wikimedia from 'wikimedia';

let apiInstance = new Wikimedia.PageviewsDataApi();
let project = "project_example"; // String | If you want to filter by project, use the domain of any Wikimedia project, for example 'en.wikipedia.org', 'www.mediawiki.org' or 'commons.wikimedia.org'. 
let access = "access_example"; // String | If you want to filter by access method, use one of desktop, mobile-app or mobile-web. If you are interested in pageviews regardless of access method, use all-access. 
let year = "year_example"; // String | The year of the date for which to retrieve top countries, in YYYY format.
let month = "month_example"; // String | The month of the date for which to retrieve top countries, in MM format. 
apiInstance.metricsPageviewsTopByCountryProjectAccessYearMonthGet(project, access, year, month, (error, data, response) => {
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
 **project** | **String**| If you want to filter by project, use the domain of any Wikimedia project, for example &#39;en.wikipedia.org&#39;, &#39;www.mediawiki.org&#39; or &#39;commons.wikimedia.org&#39;.  | 
 **access** | **String**| If you want to filter by access method, use one of desktop, mobile-app or mobile-web. If you are interested in pageviews regardless of access method, use all-access.  | 
 **year** | **String**| The year of the date for which to retrieve top countries, in YYYY format. | 
 **month** | **String**| The month of the date for which to retrieve top countries, in MM format.  | 

### Return type

[**ByCountry**](ByCountry.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## metricsPageviewsTopProjectAccessYearMonthDayGet

> PageviewTops metricsPageviewsTopProjectAccessYearMonthDayGet(project, access, year, month, day)

Get the most viewed articles for a project.

Lists the 1000 most viewed articles for a given project and timespan (month or day). You can filter by access method.  - Stability: [stable](https://www.mediawiki.org/wiki/API_versioning#Stable) - Rate limit: 100 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

### Example

```javascript
import Wikimedia from 'wikimedia';

let apiInstance = new Wikimedia.PageviewsDataApi();
let project = "project_example"; // String | If you want to filter by project, use the domain of any Wikimedia project, for example 'en.wikipedia.org', 'www.mediawiki.org' or 'commons.wikimedia.org'. 
let access = "access_example"; // String | If you want to filter by access method, use one of desktop, mobile-app or mobile-web. If you are interested in pageviews regardless of access method, use all-access. 
let year = "year_example"; // String | The year of the date for which to retrieve top articles, in YYYY format.
let month = "month_example"; // String | The month of the date for which to retrieve top articles, in MM format. If you want to get the top articles of a whole month, the day parameter should be all-days. 
let day = "day_example"; // String | The day of the date for which to retrieve top articles, in DD format.
apiInstance.metricsPageviewsTopProjectAccessYearMonthDayGet(project, access, year, month, day, (error, data, response) => {
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
 **project** | **String**| If you want to filter by project, use the domain of any Wikimedia project, for example &#39;en.wikipedia.org&#39;, &#39;www.mediawiki.org&#39; or &#39;commons.wikimedia.org&#39;.  | 
 **access** | **String**| If you want to filter by access method, use one of desktop, mobile-app or mobile-web. If you are interested in pageviews regardless of access method, use all-access.  | 
 **year** | **String**| The year of the date for which to retrieve top articles, in YYYY format. | 
 **month** | **String**| The month of the date for which to retrieve top articles, in MM format. If you want to get the top articles of a whole month, the day parameter should be all-days.  | 
 **day** | **String**| The day of the date for which to retrieve top articles, in DD format. | 

### Return type

[**PageviewTops**](PageviewTops.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json

