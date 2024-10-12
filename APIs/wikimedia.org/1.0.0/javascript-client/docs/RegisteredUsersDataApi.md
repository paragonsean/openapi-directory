# Wikimedia.RegisteredUsersDataApi

All URIs are relative to *https://wikimedia.org/api/rest_v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metricsRegisteredUsersNewProjectGranularityStartEndGet**](RegisteredUsersDataApi.md#metricsRegisteredUsersNewProjectGranularityStartEndGet) | **GET** /metrics/registered-users/new/{project}/{granularity}/{start}/{end} | Get newly registered users counts for a project.



## metricsRegisteredUsersNewProjectGranularityStartEndGet

> NewRegisteredUsers metricsRegisteredUsersNewProjectGranularityStartEndGet(project, granularity, start, end)

Get newly registered users counts for a project.

Given a Mediawiki project and a date range, returns a timeseries of its newly registered users counts. You can choose between daily and monthly granularity. The newly registered users value is computed with self-created users only, not auto-login created ones.  - Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental) - Rate limit: 25 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

### Example

```javascript
import Wikimedia from 'wikimedia';

let apiInstance = new Wikimedia.RegisteredUsersDataApi();
let project = "project_example"; // String | The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off.  For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org. If you're interested in the aggregation of all projects, use all. 
let granularity = "granularity_example"; // String | The time unit for the response data. As of today, supported values are daily and monthly. 
let start = "start_example"; // String | The date of the first day to include, in YYYYMMDD format
let end = "end_example"; // String | The date of the last day to include, in YYYYMMDD format
apiInstance.metricsRegisteredUsersNewProjectGranularityStartEndGet(project, granularity, start, end, (error, data, response) => {
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
 **project** | **String**| The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off.  For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org. If you&#39;re interested in the aggregation of all projects, use all.  | 
 **granularity** | **String**| The time unit for the response data. As of today, supported values are daily and monthly.  | 
 **start** | **String**| The date of the first day to include, in YYYYMMDD format | 
 **end** | **String**| The date of the last day to include, in YYYYMMDD format | 

### Return type

[**NewRegisteredUsers**](NewRegisteredUsers.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json

