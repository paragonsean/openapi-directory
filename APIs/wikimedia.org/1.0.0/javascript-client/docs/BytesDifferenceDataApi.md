# Wikimedia.BytesDifferenceDataApi

All URIs are relative to *https://wikimedia.org/api/rest_v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metricsBytesDifferenceAbsoluteAggregateProjectEditorTypePageTypeGranularityStartEndGet**](BytesDifferenceDataApi.md#metricsBytesDifferenceAbsoluteAggregateProjectEditorTypePageTypeGranularityStartEndGet) | **GET** /metrics/bytes-difference/absolute/aggregate/{project}/{editor-type}/{page-type}/{granularity}/{start}/{end} | Get the sum of absolute value of text bytes difference between current edit and previous one. 
[**metricsBytesDifferenceAbsolutePerPageProjectPageTitleEditorTypeGranularityStartEndGet**](BytesDifferenceDataApi.md#metricsBytesDifferenceAbsolutePerPageProjectPageTitleEditorTypeGranularityStartEndGet) | **GET** /metrics/bytes-difference/absolute/per-page/{project}/{page-title}/{editor-type}/{granularity}/{start}/{end} | Get the sum of absolute text bytes difference per page.
[**metricsBytesDifferenceNetAggregateProjectEditorTypePageTypeGranularityStartEndGet**](BytesDifferenceDataApi.md#metricsBytesDifferenceNetAggregateProjectEditorTypePageTypeGranularityStartEndGet) | **GET** /metrics/bytes-difference/net/aggregate/{project}/{editor-type}/{page-type}/{granularity}/{start}/{end} | Get the sum of net text bytes difference between current edit and previous one.
[**metricsBytesDifferenceNetPerPageProjectPageTitleEditorTypeGranularityStartEndGet**](BytesDifferenceDataApi.md#metricsBytesDifferenceNetPerPageProjectPageTitleEditorTypeGranularityStartEndGet) | **GET** /metrics/bytes-difference/net/per-page/{project}/{page-title}/{editor-type}/{granularity}/{start}/{end} | Get the sum of net text bytes difference per page.



## metricsBytesDifferenceAbsoluteAggregateProjectEditorTypePageTypeGranularityStartEndGet

> AbsoluteBytesDifference metricsBytesDifferenceAbsoluteAggregateProjectEditorTypePageTypeGranularityStartEndGet(project, editorType, pageType, granularity, start, end)

Get the sum of absolute value of text bytes difference between current edit and previous one. 

Given a Mediawiki project and a date range, returns a timeseries of absolute bytes difference sums. You can filter by editors-type (all-editor-types, anonymous, group-bot, name-bot, user) and page-type (all-page-types, content, non-content). You can choose between daily and monthly granularity as well.  - Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental) - Rate limit: 25 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

### Example

```javascript
import Wikimedia from 'wikimedia';

let apiInstance = new Wikimedia.BytesDifferenceDataApi();
let project = "project_example"; // String | The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off. For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org. If you're interested in the aggregation of all projects, use all-projects. 
let editorType = "editorType_example"; // String | If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types. 
let pageType = "pageType_example"; // String | If you want to filter by page-type, use one of content (edits on pages in content namespaces) or non-content (edits on pages in non-content namespaces). If you are interested in edits regardless of their page-type, use all-page-types. 
let granularity = "granularity_example"; // String | Time unit for the response data. As of today, supported values are daily and monthly 
let start = "start_example"; // String | The date of the first day to include, in YYYYMMDD format
let end = "end_example"; // String | The date of the last day to include, in YYYYMMDD format
apiInstance.metricsBytesDifferenceAbsoluteAggregateProjectEditorTypePageTypeGranularityStartEndGet(project, editorType, pageType, granularity, start, end, (error, data, response) => {
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
 **project** | **String**| The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off. For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org. If you&#39;re interested in the aggregation of all projects, use all-projects.  | 
 **editorType** | **String**| If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types.  | 
 **pageType** | **String**| If you want to filter by page-type, use one of content (edits on pages in content namespaces) or non-content (edits on pages in non-content namespaces). If you are interested in edits regardless of their page-type, use all-page-types.  | 
 **granularity** | **String**| Time unit for the response data. As of today, supported values are daily and monthly  | 
 **start** | **String**| The date of the first day to include, in YYYYMMDD format | 
 **end** | **String**| The date of the last day to include, in YYYYMMDD format | 

### Return type

[**AbsoluteBytesDifference**](AbsoluteBytesDifference.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## metricsBytesDifferenceAbsolutePerPageProjectPageTitleEditorTypeGranularityStartEndGet

> AbsoluteBytesDifferencePerPage metricsBytesDifferenceAbsolutePerPageProjectPageTitleEditorTypeGranularityStartEndGet(project, pageTitle, editorType, granularity, start, end)

Get the sum of absolute text bytes difference per page.

Given a Mediawiki project, a page-title prefixed with canonical namespace (for instance &#39;User:Jimbo_Wales&#39;) and a date range, returns a timeseries of bytes difference absolute sums. You can filter by editors-type (all-editor-types, anonymous, group-bot, name-bot, user). You can choose between daily and monthly granularity as well.  - Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental) - Rate limit: 25 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

### Example

```javascript
import Wikimedia from 'wikimedia';

let apiInstance = new Wikimedia.BytesDifferenceDataApi();
let project = "project_example"; // String | The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off. For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org. 
let pageTitle = "pageTitle_example"; // String | The page-title to request absolute bytes-difference for. Should be prefixed with the page canonical namespace. 
let editorType = "editorType_example"; // String | If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types. 
let granularity = "granularity_example"; // String | Time unit for the response data. As of today, supported values are daily and monthly 
let start = "start_example"; // String | The date of the first day to include, in YYYYMMDD format
let end = "end_example"; // String | The date of the last day to include, in YYYYMMDD format
apiInstance.metricsBytesDifferenceAbsolutePerPageProjectPageTitleEditorTypeGranularityStartEndGet(project, pageTitle, editorType, granularity, start, end, (error, data, response) => {
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
 **project** | **String**| The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off. For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org.  | 
 **pageTitle** | **String**| The page-title to request absolute bytes-difference for. Should be prefixed with the page canonical namespace.  | 
 **editorType** | **String**| If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types.  | 
 **granularity** | **String**| Time unit for the response data. As of today, supported values are daily and monthly  | 
 **start** | **String**| The date of the first day to include, in YYYYMMDD format | 
 **end** | **String**| The date of the last day to include, in YYYYMMDD format | 

### Return type

[**AbsoluteBytesDifferencePerPage**](AbsoluteBytesDifferencePerPage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## metricsBytesDifferenceNetAggregateProjectEditorTypePageTypeGranularityStartEndGet

> NetBytesDifference metricsBytesDifferenceNetAggregateProjectEditorTypePageTypeGranularityStartEndGet(project, editorType, pageType, granularity, start, end)

Get the sum of net text bytes difference between current edit and previous one.

Given a Mediawiki project and a date range, returns a timeseries of bytes difference net sums. You can filter by editors-type (all-editor-types, anonymous, group-bot, name-bot, user) and page-type (all-page-types, content or non-content). You can choose between daily and monthly granularity as well.  - Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental) - Rate limit: 25 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

### Example

```javascript
import Wikimedia from 'wikimedia';

let apiInstance = new Wikimedia.BytesDifferenceDataApi();
let project = "project_example"; // String | The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off. For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org. If you're interested in the aggregation of all projects, use all-projects. 
let editorType = "editorType_example"; // String | If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types. 
let pageType = "pageType_example"; // String | If you want to filter by page-type, use one of content (edits on pages in content namespaces) or non-content (edits on pages in non-content namespaces). If you are interested in edits regardless of their page-type, use all-page-types. 
let granularity = "granularity_example"; // String | Time unit for the response data. As of today, supported values are daily and monthly 
let start = "start_example"; // String | The date of the first day to include, in YYYYMMDD format
let end = "end_example"; // String | The date of the last day to include, in YYYYMMDD format
apiInstance.metricsBytesDifferenceNetAggregateProjectEditorTypePageTypeGranularityStartEndGet(project, editorType, pageType, granularity, start, end, (error, data, response) => {
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
 **project** | **String**| The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off. For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org. If you&#39;re interested in the aggregation of all projects, use all-projects.  | 
 **editorType** | **String**| If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types.  | 
 **pageType** | **String**| If you want to filter by page-type, use one of content (edits on pages in content namespaces) or non-content (edits on pages in non-content namespaces). If you are interested in edits regardless of their page-type, use all-page-types.  | 
 **granularity** | **String**| Time unit for the response data. As of today, supported values are daily and monthly  | 
 **start** | **String**| The date of the first day to include, in YYYYMMDD format | 
 **end** | **String**| The date of the last day to include, in YYYYMMDD format | 

### Return type

[**NetBytesDifference**](NetBytesDifference.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## metricsBytesDifferenceNetPerPageProjectPageTitleEditorTypeGranularityStartEndGet

> NetBytesDifferencePerPage metricsBytesDifferenceNetPerPageProjectPageTitleEditorTypeGranularityStartEndGet(project, pageTitle, editorType, granularity, start, end)

Get the sum of net text bytes difference per page.

Given a Mediawiki project, a page-title prefixed with canonical namespace (for instance &#39;User:Jimbo_Wales&#39;) and a date range, returns a timeseries of bytes difference net sums. You can filter by editors-type (all-editor-types, anonymous, group-bot, name-bot, user). You can choose between daily and monthly granularity as well.  - Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental) - Rate limit: 25 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

### Example

```javascript
import Wikimedia from 'wikimedia';

let apiInstance = new Wikimedia.BytesDifferenceDataApi();
let project = "project_example"; // String | The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off. For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org. 
let pageTitle = "pageTitle_example"; // String | The page-title to request net bytes-difference for. Should be prefixed with the page canonical namespace. 
let editorType = "editorType_example"; // String | If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types. 
let granularity = "granularity_example"; // String | Time unit for the response data. As of today, supported values are daily and monthly 
let start = "start_example"; // String | The date of the first day to include, in YYYYMMDD format
let end = "end_example"; // String | The date of the last day to include, in YYYYMMDD format
apiInstance.metricsBytesDifferenceNetPerPageProjectPageTitleEditorTypeGranularityStartEndGet(project, pageTitle, editorType, granularity, start, end, (error, data, response) => {
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
 **project** | **String**| The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off. For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org.  | 
 **pageTitle** | **String**| The page-title to request net bytes-difference for. Should be prefixed with the page canonical namespace.  | 
 **editorType** | **String**| If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types.  | 
 **granularity** | **String**| Time unit for the response data. As of today, supported values are daily and monthly  | 
 **start** | **String**| The date of the first day to include, in YYYYMMDD format | 
 **end** | **String**| The date of the last day to include, in YYYYMMDD format | 

### Return type

[**NetBytesDifferencePerPage**](NetBytesDifferencePerPage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json

