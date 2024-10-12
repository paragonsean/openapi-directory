# Wikimedia.LegacyDataApi

All URIs are relative to *https://wikimedia.org/api/rest_v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metricsLegacyPagecountsAggregateProjectAccessSiteGranularityStartEndGet**](LegacyDataApi.md#metricsLegacyPagecountsAggregateProjectAccessSiteGranularityStartEndGet) | **GET** /metrics/legacy/pagecounts/aggregate/{project}/{access-site}/{granularity}/{start}/{end} | 



## metricsLegacyPagecountsAggregateProjectAccessSiteGranularityStartEndGet

> PagecountsProject metricsLegacyPagecountsAggregateProjectAccessSiteGranularityStartEndGet(project, accessSite, granularity, start, end)



Given a project and a date range, returns a timeseries of pagecounts. You can filter by access site (mobile or desktop) and you can choose between monthly, daily and hourly granularity as well.  - Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental) - Rate limit: 100 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

### Example

```javascript
import Wikimedia from 'wikimedia';

let apiInstance = new Wikimedia.LegacyDataApi();
let project = "project_example"; // String | The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off. For projects like commons without language codes, use commons.wikimedia. 
let accessSite = "accessSite_example"; // String | If you want to filter by access site, use one of desktop-site or mobile-site. If you are interested in pagecounts regardless of access site use all-sites.
let granularity = "granularity_example"; // String | The time unit for the response data. As of today, the supported granularities for this endpoint are hourly, daily and monthly. 
let start = "start_example"; // String | The timestamp of the first hour/day/month to include, in YYYYMMDDHH format.
let end = "end_example"; // String | The timestamp of the last hour/day/month to include, in YYYYMMDDHH format. In hourly and daily granularities this value is inclusive, in the monthly granularity this value is exclusive. 
apiInstance.metricsLegacyPagecountsAggregateProjectAccessSiteGranularityStartEndGet(project, accessSite, granularity, start, end, (error, data, response) => {
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
 **project** | **String**| The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off. For projects like commons without language codes, use commons.wikimedia.  | 
 **accessSite** | **String**| If you want to filter by access site, use one of desktop-site or mobile-site. If you are interested in pagecounts regardless of access site use all-sites. | 
 **granularity** | **String**| The time unit for the response data. As of today, the supported granularities for this endpoint are hourly, daily and monthly.  | 
 **start** | **String**| The timestamp of the first hour/day/month to include, in YYYYMMDDHH format. | 
 **end** | **String**| The timestamp of the last hour/day/month to include, in YYYYMMDDHH format. In hourly and daily granularities this value is inclusive, in the monthly granularity this value is exclusive.  | 

### Return type

[**PagecountsProject**](PagecountsProject.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json

