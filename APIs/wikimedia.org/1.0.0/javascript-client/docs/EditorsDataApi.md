# Wikimedia.EditorsDataApi

All URIs are relative to *https://wikimedia.org/api/rest_v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metricsEditorsAggregateProjectEditorTypePageTypeActivityLevelGranularityStartEndGet**](EditorsDataApi.md#metricsEditorsAggregateProjectEditorTypePageTypeActivityLevelGranularityStartEndGet) | **GET** /metrics/editors/aggregate/{project}/{editor-type}/{page-type}/{activity-level}/{granularity}/{start}/{end} | Get editors counts for a project.
[**metricsEditorsTopByAbsoluteBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet**](EditorsDataApi.md#metricsEditorsTopByAbsoluteBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet) | **GET** /metrics/editors/top-by-absolute-bytes-difference/{project}/{editor-type}/{page-type}/{year}/{month}/{day} | Get top 100 editors by absolute bytes-difference.
[**metricsEditorsTopByEditsProjectEditorTypePageTypeYearMonthDayGet**](EditorsDataApi.md#metricsEditorsTopByEditsProjectEditorTypePageTypeYearMonthDayGet) | **GET** /metrics/editors/top-by-edits/{project}/{editor-type}/{page-type}/{year}/{month}/{day} | Get top 100 editors by edits count.
[**metricsEditorsTopByNetBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet**](EditorsDataApi.md#metricsEditorsTopByNetBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet) | **GET** /metrics/editors/top-by-net-bytes-difference/{project}/{editor-type}/{page-type}/{year}/{month}/{day} | Get top 100 editors by net bytes-difference.



## metricsEditorsAggregateProjectEditorTypePageTypeActivityLevelGranularityStartEndGet

> Editors metricsEditorsAggregateProjectEditorTypePageTypeActivityLevelGranularityStartEndGet(project, editorType, pageType, activityLevel, granularity, start, end)

Get editors counts for a project.

Given a Mediawiki project and a date range, returns a timeseries of its editors counts. You can filter by editory-type (all-editor-types, anonymous, group-bot, name-bot, user), page-type (all-page-types, content or non-content) or activity-level (1..4-edits, 5..24-edits, 25..99-edits or 100..-edits). You can choose between daily and monthly granularity as well.  - Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental) - Rate limit: 25 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

### Example

```javascript
import Wikimedia from 'wikimedia';

let apiInstance = new Wikimedia.EditorsDataApi();
let project = "project_example"; // String | The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off.  For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org. 
let editorType = "editorType_example"; // String | If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types. 
let pageType = "pageType_example"; // String | If you want to filter by page-type, use one of content (edits made in content namespaces) or non-content (edits made in non-content namespaces). If you are interested in editors regardless of their page-type, use all-page-types. 
let activityLevel = "activityLevel_example"; // String | If you want to filter by activity-level, use one of 1..4-edits, 5..24-edits, 25..99-edits or 100..-edits. If you are interested in editors regardless of their activity-level, use all-activity-levels. 
let granularity = "granularity_example"; // String | The time unit for the response data. As of today, supported values are daily and monthly. 
let start = "start_example"; // String | The date of the first day to include, in YYYYMMDD format
let end = "end_example"; // String | The date of the last day to include, in YYYYMMDD format
apiInstance.metricsEditorsAggregateProjectEditorTypePageTypeActivityLevelGranularityStartEndGet(project, editorType, pageType, activityLevel, granularity, start, end, (error, data, response) => {
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
 **pageType** | **String**| If you want to filter by page-type, use one of content (edits made in content namespaces) or non-content (edits made in non-content namespaces). If you are interested in editors regardless of their page-type, use all-page-types.  | 
 **activityLevel** | **String**| If you want to filter by activity-level, use one of 1..4-edits, 5..24-edits, 25..99-edits or 100..-edits. If you are interested in editors regardless of their activity-level, use all-activity-levels.  | 
 **granularity** | **String**| The time unit for the response data. As of today, supported values are daily and monthly.  | 
 **start** | **String**| The date of the first day to include, in YYYYMMDD format | 
 **end** | **String**| The date of the last day to include, in YYYYMMDD format | 

### Return type

[**Editors**](Editors.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## metricsEditorsTopByAbsoluteBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet

> TopEditorsByAbsBytesDiff metricsEditorsTopByAbsoluteBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet(project, editorType, pageType, year, month, day)

Get top 100 editors by absolute bytes-difference.

Given a Mediawiki project and a date (day or month), returns a timeseries of the top 100 editors by absolute bytes-difference. You can filter by editor-type (all-editor-types, anonymous, group-bot, name-bot, user) or page-type (all-page-types, content or non-content). The user_text returned is either the mediawiki user_text if the user is registered, or null if user is anonymous.  - Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental) - Rate limit: 25 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

### Example

```javascript
import Wikimedia from 'wikimedia';

let apiInstance = new Wikimedia.EditorsDataApi();
let project = "project_example"; // String | The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off. For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org. 
let editorType = "editorType_example"; // String | If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types. 
let pageType = "pageType_example"; // String | If you want to filter by page-type, use one of content (edits on pages in content namespaces) or non-content (edits on pages in non-content namespaces). If you are interested in edits regardless of their page-type, use all-page-types. 
let year = "year_example"; // String | The year of the date for which to retrieve top editors, in YYYY format.
let month = "month_example"; // String | The month of the date for which to retrieve top editors, in MM format. If you want to get the top editors of a whole month, the day parameter should be all-days.
let day = "day_example"; // String | The day of the date for which to retrieve top editors, in DD format, or all-days for a monthly value.
apiInstance.metricsEditorsTopByAbsoluteBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet(project, editorType, pageType, year, month, day, (error, data, response) => {
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
 **year** | **String**| The year of the date for which to retrieve top editors, in YYYY format. | 
 **month** | **String**| The month of the date for which to retrieve top editors, in MM format. If you want to get the top editors of a whole month, the day parameter should be all-days. | 
 **day** | **String**| The day of the date for which to retrieve top editors, in DD format, or all-days for a monthly value. | 

### Return type

[**TopEditorsByAbsBytesDiff**](TopEditorsByAbsBytesDiff.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## metricsEditorsTopByEditsProjectEditorTypePageTypeYearMonthDayGet

> TopEditorsByEdits metricsEditorsTopByEditsProjectEditorTypePageTypeYearMonthDayGet(project, editorType, pageType, year, month, day)

Get top 100 editors by edits count.

Given a Mediawiki project and a date (day or month), returns a timeseries of the top 100 editors by edits count. You can filter by editor-type (all-editor-types, anonymous, group-bot, name-bot, user) or page-type (all-page-types, content or non-content). The user_text returned is either the mediawiki user_text if the user is registered, or null if user is anonymous.  - Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental) - Rate limit: 25 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

### Example

```javascript
import Wikimedia from 'wikimedia';

let apiInstance = new Wikimedia.EditorsDataApi();
let project = "project_example"; // String | The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off. For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org. 
let editorType = "editorType_example"; // String | If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types. 
let pageType = "pageType_example"; // String | If you want to filter by page-type, use one of content (edits on pages in content namespaces) or non-content (edits on pages in non-content namespaces). If you are interested in edits regardless of their page-type, use all-page-types. 
let year = "year_example"; // String | The year of the date for which to retrieve top editors, in YYYY format.
let month = "month_example"; // String | The month of the date for which to retrieve top editors, in MM format. If you want to get the top editors of a whole month, the day parameter should be all-days.
let day = "day_example"; // String | The day of the date for which to retrieve top editors, in DD format, or all-days for a monthly value.
apiInstance.metricsEditorsTopByEditsProjectEditorTypePageTypeYearMonthDayGet(project, editorType, pageType, year, month, day, (error, data, response) => {
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
 **year** | **String**| The year of the date for which to retrieve top editors, in YYYY format. | 
 **month** | **String**| The month of the date for which to retrieve top editors, in MM format. If you want to get the top editors of a whole month, the day parameter should be all-days. | 
 **day** | **String**| The day of the date for which to retrieve top editors, in DD format, or all-days for a monthly value. | 

### Return type

[**TopEditorsByEdits**](TopEditorsByEdits.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## metricsEditorsTopByNetBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet

> TopEditorsByNetBytesDiff metricsEditorsTopByNetBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet(project, editorType, pageType, year, month, day)

Get top 100 editors by net bytes-difference.

Given a Mediawiki project and a date (day or month), returns a timeseries of the top 100 editors by net bytes-difference. You can filter by editor-type (all-editor-types, anonymous, group-bot, name-bot, user) or page-type (all-page-types, content or non-content). The user_text returned is either the mediawiki user_text if the user is registered, or \&quot;Anonymous Editor\&quot; if user is anonymous.  - Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental) - Rate limit: 25 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

### Example

```javascript
import Wikimedia from 'wikimedia';

let apiInstance = new Wikimedia.EditorsDataApi();
let project = "project_example"; // String | The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off. For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org. 
let editorType = "editorType_example"; // String | If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types. 
let pageType = "pageType_example"; // String | If you want to filter by page-type, use one of content (edits on pages in content namespaces) or non-content (edits on pages in non-content namespaces). If you are interested in edits regardless of their page-type, use all-page-types. 
let year = "year_example"; // String | The year of the date for which to retrieve top editors, in YYYY format.
let month = "month_example"; // String | The month of the date for which to retrieve top editors, in MM format. If you want to get the top editors of a whole month, the day parameter should be all-days.
let day = "day_example"; // String | The day of the date for which to retrieve top editors, in DD format, or all-days for a monthly value.
apiInstance.metricsEditorsTopByNetBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet(project, editorType, pageType, year, month, day, (error, data, response) => {
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
 **year** | **String**| The year of the date for which to retrieve top editors, in YYYY format. | 
 **month** | **String**| The month of the date for which to retrieve top editors, in MM format. If you want to get the top editors of a whole month, the day parameter should be all-days. | 
 **day** | **String**| The day of the date for which to retrieve top editors, in DD format, or all-days for a monthly value. | 

### Return type

[**TopEditorsByNetBytesDiff**](TopEditorsByNetBytesDiff.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json

