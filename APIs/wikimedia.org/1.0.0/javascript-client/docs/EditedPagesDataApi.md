# Wikimedia.EditedPagesDataApi

All URIs are relative to *https://wikimedia.org/api/rest_v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metricsEditedPagesAggregateProjectEditorTypePageTypeActivityLevelGranularityStartEndGet**](EditedPagesDataApi.md#metricsEditedPagesAggregateProjectEditorTypePageTypeActivityLevelGranularityStartEndGet) | **GET** /metrics/edited-pages/aggregate/{project}/{editor-type}/{page-type}/{activity-level}/{granularity}/{start}/{end} | Get edited-pages counts for a project.
[**metricsEditedPagesNewProjectEditorTypePageTypeGranularityStartEndGet**](EditedPagesDataApi.md#metricsEditedPagesNewProjectEditorTypePageTypeGranularityStartEndGet) | **GET** /metrics/edited-pages/new/{project}/{editor-type}/{page-type}/{granularity}/{start}/{end} | Get new pages counts for a project.
[**metricsEditedPagesTopByAbsoluteBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet**](EditedPagesDataApi.md#metricsEditedPagesTopByAbsoluteBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet) | **GET** /metrics/edited-pages/top-by-absolute-bytes-difference/{project}/{editor-type}/{page-type}/{year}/{month}/{day} | Get top 100 edited-pages by absolute bytes-difference.
[**metricsEditedPagesTopByEditsProjectEditorTypePageTypeYearMonthDayGet**](EditedPagesDataApi.md#metricsEditedPagesTopByEditsProjectEditorTypePageTypeYearMonthDayGet) | **GET** /metrics/edited-pages/top-by-edits/{project}/{editor-type}/{page-type}/{year}/{month}/{day} | Get top 100 edited-pages by edits count.
[**metricsEditedPagesTopByNetBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet**](EditedPagesDataApi.md#metricsEditedPagesTopByNetBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet) | **GET** /metrics/edited-pages/top-by-net-bytes-difference/{project}/{editor-type}/{page-type}/{year}/{month}/{day} | Get top 100 edited-pages by net bytes-difference.



## metricsEditedPagesAggregateProjectEditorTypePageTypeActivityLevelGranularityStartEndGet

> EditedPages metricsEditedPagesAggregateProjectEditorTypePageTypeActivityLevelGranularityStartEndGet(project, editorType, pageType, activityLevel, granularity, start, end)

Get edited-pages counts for a project.

Given a Mediawiki project and a date range, returns a timeseries of its edited-pages counts. You can filter by editor-type (all-editor-types, anonymous, group-bot, name-bot, user), page-type (all-page-types, content or non-content) or activity-level (1..4-edits, 5..24-edits, 25..99-edits, 100..-edits). You can choose between daily and monthly granularity as well.  - Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental) - Rate limit: 25 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

### Example

```javascript
import Wikimedia from 'wikimedia';

let apiInstance = new Wikimedia.EditedPagesDataApi();
let project = "project_example"; // String | The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off.  For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org. 
let editorType = "editorType_example"; // String | If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types. 
let pageType = "pageType_example"; // String | If you want to filter by page-type, use one of content (edited-pages in content namespaces) or non-content (edited-pages in non-content namespaces). If you are interested in edited-pages regardless of their page-type, use all-page-types. 
let activityLevel = "activityLevel_example"; // String | If you want to filter by activity-level, use one of 1..4-edits, 5..24-edits, 25..99-edits or 100..-edits. If you are interested in edited-pages regardless of their activity level, use all-activity-levels. 
let granularity = "granularity_example"; // String | The time unit for the response data. As of today, supported values are daily and monthly. 
let start = "start_example"; // String | The date of the first day to include, in YYYYMMDD format
let end = "end_example"; // String | The date of the last day to include, in YYYYMMDD format
apiInstance.metricsEditedPagesAggregateProjectEditorTypePageTypeActivityLevelGranularityStartEndGet(project, editorType, pageType, activityLevel, granularity, start, end, (error, data, response) => {
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
 **project** | **String**| The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off.  For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org.  | 
 **editorType** | **String**| If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types.  | 
 **pageType** | **String**| If you want to filter by page-type, use one of content (edited-pages in content namespaces) or non-content (edited-pages in non-content namespaces). If you are interested in edited-pages regardless of their page-type, use all-page-types.  | 
 **activityLevel** | **String**| If you want to filter by activity-level, use one of 1..4-edits, 5..24-edits, 25..99-edits or 100..-edits. If you are interested in edited-pages regardless of their activity level, use all-activity-levels.  | 
 **granularity** | **String**| The time unit for the response data. As of today, supported values are daily and monthly.  | 
 **start** | **String**| The date of the first day to include, in YYYYMMDD format | 
 **end** | **String**| The date of the last day to include, in YYYYMMDD format | 

### Return type

[**EditedPages**](EditedPages.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## metricsEditedPagesNewProjectEditorTypePageTypeGranularityStartEndGet

> NewPages metricsEditedPagesNewProjectEditorTypePageTypeGranularityStartEndGet(project, editorType, pageType, granularity, start, end)

Get new pages counts for a project.

Given a Mediawiki project and a date range, returns a timeseries of its new pages counts. You can filter by editor type (all-editor-types, anonymous, group-bot, name-bot, user) or page-type (all-page-types, content or non-content). You can choose between daily and monthly granularity as well.  - Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental) - Rate limit: 25 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

### Example

```javascript
import Wikimedia from 'wikimedia';

let apiInstance = new Wikimedia.EditedPagesDataApi();
let project = "project_example"; // String | The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off.  For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org. If you're interested in the aggregation of all projects, use all-projects. 
let editorType = "editorType_example"; // String | If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types. 
let pageType = "pageType_example"; // String | If you want to filter by page-type, use one of content (new pages in content namespaces) or non-content (new pages in non-content namespaces). If you are interested in new-articles regardless of their page-type, use all-page-types. 
let granularity = "granularity_example"; // String | The time unit for the response data. As of today, supported values are daily and monthly. 
let start = "start_example"; // String | The date of the first day to include, in YYYYMMDD format
let end = "end_example"; // String | The date of the last day to include, in YYYYMMDD format
apiInstance.metricsEditedPagesNewProjectEditorTypePageTypeGranularityStartEndGet(project, editorType, pageType, granularity, start, end, (error, data, response) => {
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
 **project** | **String**| The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off.  For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org. If you&#39;re interested in the aggregation of all projects, use all-projects.  | 
 **editorType** | **String**| If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types.  | 
 **pageType** | **String**| If you want to filter by page-type, use one of content (new pages in content namespaces) or non-content (new pages in non-content namespaces). If you are interested in new-articles regardless of their page-type, use all-page-types.  | 
 **granularity** | **String**| The time unit for the response data. As of today, supported values are daily and monthly.  | 
 **start** | **String**| The date of the first day to include, in YYYYMMDD format | 
 **end** | **String**| The date of the last day to include, in YYYYMMDD format | 

### Return type

[**NewPages**](NewPages.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## metricsEditedPagesTopByAbsoluteBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet

> TopEditedPagesByAbsBytesDiff metricsEditedPagesTopByAbsoluteBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet(project, editorType, pageType, year, month, day)

Get top 100 edited-pages by absolute bytes-difference.

Given a Mediawiki project and a date (day or month), returns a timeseries of the top 100 edited-pages by absolute bytes-difference. You can filter by editor-type (all-editor-types, anonymous, group-bot, name-bot, user) or page-type (all-page-types, content or non-content).  - Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental) - Rate limit: 25 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

### Example

```javascript
import Wikimedia from 'wikimedia';

let apiInstance = new Wikimedia.EditedPagesDataApi();
let project = "project_example"; // String | The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off. For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org. 
let editorType = "editorType_example"; // String | If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types. 
let pageType = "pageType_example"; // String | If you want to filter by page-type, use one of content (edits on pages in content namespaces) or non-content (edits on pages in non-content namespaces). If you are interested in edits regardless of their page-type, use all-page-types. 
let year = "year_example"; // String | The year of the date for which to retrieve top edited-pages, in YYYY format.
let month = "month_example"; // String | The month of the date for which to retrieve top edited-pages, in MM format. If you want to get the top edited-pages of a whole month, the day parameter should be all-days.
let day = "day_example"; // String | The day of the date for which to retrieve top edited-pages, in DD format, or all-days for a monthly value.
apiInstance.metricsEditedPagesTopByAbsoluteBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet(project, editorType, pageType, year, month, day, (error, data, response) => {
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
 **editorType** | **String**| If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types.  | 
 **pageType** | **String**| If you want to filter by page-type, use one of content (edits on pages in content namespaces) or non-content (edits on pages in non-content namespaces). If you are interested in edits regardless of their page-type, use all-page-types.  | 
 **year** | **String**| The year of the date for which to retrieve top edited-pages, in YYYY format. | 
 **month** | **String**| The month of the date for which to retrieve top edited-pages, in MM format. If you want to get the top edited-pages of a whole month, the day parameter should be all-days. | 
 **day** | **String**| The day of the date for which to retrieve top edited-pages, in DD format, or all-days for a monthly value. | 

### Return type

[**TopEditedPagesByAbsBytesDiff**](TopEditedPagesByAbsBytesDiff.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## metricsEditedPagesTopByEditsProjectEditorTypePageTypeYearMonthDayGet

> TopEditedPagesByEdits metricsEditedPagesTopByEditsProjectEditorTypePageTypeYearMonthDayGet(project, editorType, pageType, year, month, day)

Get top 100 edited-pages by edits count.

Given a Mediawiki project and a date (day or month), returns a timeseries of the top 100 edited-pages by edits count. You can filter by editor-type (all-editor-types, anonymous, group-bot, name-bot, user) or page-type (all-page-types, content or non-content).  - Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental) - Rate limit: 25 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

### Example

```javascript
import Wikimedia from 'wikimedia';

let apiInstance = new Wikimedia.EditedPagesDataApi();
let project = "project_example"; // String | The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off. For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org. 
let editorType = "editorType_example"; // String | If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types. 
let pageType = "pageType_example"; // String | If you want to filter by page-type, use one of content (edits on pages in content namespaces) or non-content (edits on pages in non-content namespaces). If you are interested in edits regardless of their page-type, use all-page-types. 
let year = "year_example"; // String | The year of the date for which to retrieve top edited-pages, in YYYY format.
let month = "month_example"; // String | The month of the date for which to retrieve top edited-pages, in MM format. If you want to get the top edited-pages of a whole month, the day parameter should be all-days.
let day = "day_example"; // String | The day of the date for which to retrieve top edited-pages, in DD format, or all-days for a monthly value.
apiInstance.metricsEditedPagesTopByEditsProjectEditorTypePageTypeYearMonthDayGet(project, editorType, pageType, year, month, day, (error, data, response) => {
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
 **editorType** | **String**| If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types.  | 
 **pageType** | **String**| If you want to filter by page-type, use one of content (edits on pages in content namespaces) or non-content (edits on pages in non-content namespaces). If you are interested in edits regardless of their page-type, use all-page-types.  | 
 **year** | **String**| The year of the date for which to retrieve top edited-pages, in YYYY format. | 
 **month** | **String**| The month of the date for which to retrieve top edited-pages, in MM format. If you want to get the top edited-pages of a whole month, the day parameter should be all-days. | 
 **day** | **String**| The day of the date for which to retrieve top edited-pages, in DD format, or all-days for a monthly value. | 

### Return type

[**TopEditedPagesByEdits**](TopEditedPagesByEdits.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## metricsEditedPagesTopByNetBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet

> TopEditedPagesByNetBytesDiff metricsEditedPagesTopByNetBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet(project, editorType, pageType, year, month, day)

Get top 100 edited-pages by net bytes-difference.

Given a Mediawiki project and a date (day or month), returns a timeseries of the top 100 edited-pages by net bytes-difference. You can filter by editor-type (all-editor-types, anonymous, group-bot, name-bot, user) or page-type (all-page-types, content or non-content).  - Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental) - Rate limit: 25 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

### Example

```javascript
import Wikimedia from 'wikimedia';

let apiInstance = new Wikimedia.EditedPagesDataApi();
let project = "project_example"; // String | The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off. For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org. 
let editorType = "editorType_example"; // String | If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types. 
let pageType = "pageType_example"; // String | If you want to filter by page-type, use one of content (edits on pages in content namespaces) or non-content (edits on pages in non-content namespaces). If you are interested in edits regardless of their page-type, use all-page-types. 
let year = "year_example"; // String | The year of the date for which to retrieve top edited-pages, in YYYY format.
let month = "month_example"; // String | The month of the date for which to retrieve top edited-pages, in MM format. If you want to get the top edited-pages of a whole month, the day parameter should be all-days.
let day = "day_example"; // String | The day of the date for which to retrieve top edited-pages, in DD format, or all-days for a monthly value.
apiInstance.metricsEditedPagesTopByNetBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet(project, editorType, pageType, year, month, day, (error, data, response) => {
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
 **editorType** | **String**| If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types.  | 
 **pageType** | **String**| If you want to filter by page-type, use one of content (edits on pages in content namespaces) or non-content (edits on pages in non-content namespaces). If you are interested in edits regardless of their page-type, use all-page-types.  | 
 **year** | **String**| The year of the date for which to retrieve top edited-pages, in YYYY format. | 
 **month** | **String**| The month of the date for which to retrieve top edited-pages, in MM format. If you want to get the top edited-pages of a whole month, the day parameter should be all-days. | 
 **day** | **String**| The day of the date for which to retrieve top edited-pages, in DD format, or all-days for a monthly value. | 

### Return type

[**TopEditedPagesByNetBytesDiff**](TopEditedPagesByNetBytesDiff.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json

