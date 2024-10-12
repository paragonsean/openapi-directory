# Wikimedia.UniqueDevicesDataApi

All URIs are relative to *https://wikimedia.org/api/rest_v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metricsUniqueDevicesProjectAccessSiteGranularityStartEndGet**](UniqueDevicesDataApi.md#metricsUniqueDevicesProjectAccessSiteGranularityStartEndGet) | **GET** /metrics/unique-devices/{project}/{access-site}/{granularity}/{start}/{end} | Get unique devices count per project



## metricsUniqueDevicesProjectAccessSiteGranularityStartEndGet

> UniqueDevices metricsUniqueDevicesProjectAccessSiteGranularityStartEndGet(project, accessSite, granularity, start, end)

Get unique devices count per project

Given a project and a date range, returns a timeseries of unique devices counts. You need to specify a project, and can filter by accessed site (mobile or desktop). You can choose between daily and hourly granularity as well.  - Stability: [stable](https://www.mediawiki.org/wiki/API_versioning#Stable) - Rate limit: 100 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

### Example

```javascript
import Wikimedia from 'wikimedia';

let apiInstance = new Wikimedia.UniqueDevicesDataApi();
let project = "project_example"; // String | If you want to filter by project, use the domain of any Wikimedia project, for example 'en.wikipedia.org', 'www.mediawiki.org' or 'commons.wikimedia.org'. 
let accessSite = "accessSite_example"; // String | If you want to filter by accessed site, use one of desktop-site or mobile-site. If you are interested in unique devices regardless of accessed site, use or all-sites. 
let granularity = "granularity_example"; // String | The time unit for the response data. As of today, the supported granularities for this endpoint are daily and monthly. 
let start = "start_example"; // String | The timestamp of the first day/month to include, in YYYYMMDD format
let end = "end_example"; // String | The timestamp of the last day/month to include, in YYYYMMDD format
apiInstance.metricsUniqueDevicesProjectAccessSiteGranularityStartEndGet(project, accessSite, granularity, start, end, (error, data, response) => {
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
 **accessSite** | **String**| If you want to filter by accessed site, use one of desktop-site or mobile-site. If you are interested in unique devices regardless of accessed site, use or all-sites.  | 
 **granularity** | **String**| The time unit for the response data. As of today, the supported granularities for this endpoint are daily and monthly.  | 
 **start** | **String**| The timestamp of the first day/month to include, in YYYYMMDD format | 
 **end** | **String**| The timestamp of the last day/month to include, in YYYYMMDD format | 

### Return type

[**UniqueDevices**](UniqueDevices.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json

