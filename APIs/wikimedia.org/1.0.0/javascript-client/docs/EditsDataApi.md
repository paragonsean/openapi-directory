# Wikimedia.EditsDataApi

All URIs are relative to *https://wikimedia.org/api/rest_v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metricsEditsAggregateProjectEditorTypePageTypeGranularityStartEndGet**](EditsDataApi.md#metricsEditsAggregateProjectEditorTypePageTypeGranularityStartEndGet) | **GET** /metrics/edits/aggregate/{project}/{editor-type}/{page-type}/{granularity}/{start}/{end} | Get edits counts for a project.
[**metricsEditsPerPageProjectPageTitleEditorTypeGranularityStartEndGet**](EditsDataApi.md#metricsEditsPerPageProjectPageTitleEditorTypeGranularityStartEndGet) | **GET** /metrics/edits/per-page/{project}/{page-title}/{editor-type}/{granularity}/{start}/{end} | Get edit counts for a page in a project.



## metricsEditsAggregateProjectEditorTypePageTypeGranularityStartEndGet

> Edits metricsEditsAggregateProjectEditorTypePageTypeGranularityStartEndGet(project, editorType, pageType, granularity, start, end)

Get edits counts for a project.

Given a Mediawiki project and a date range, returns a timeseries of edits counts. You can filter by editors-type (all-editor-types, anonymous, bot, registered) and page-type (all-page-types, content or non-content). You can choose between daily and monthly granularity as well.  - Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental) - Rate limit: 25 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

### Example

```javascript
import Wikimedia from 'wikimedia';

let apiInstance = new Wikimedia.EditsDataApi();
let project = "project_example"; // String | The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off.  For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org. If you're interested in the aggregation of all projects, use all-projects. 
let editorType = "editorType_example"; // String | If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types. 
let pageType = "pageType_example"; // String | If you want to filter by page-type, use one of content (edits on pages in content namespaces) or non-content (edits on pages in non-content namespaces). If you are interested in edits regardless of their page-type, use all-page-types. 
let granularity = "granularity_example"; // String | The time unit for the response data. As of today, supported values are daily and monthly. 
let start = "start_example"; // String | The date of the first day to include, in YYYYMMDD format
let end = "end_example"; // String | The date of the last day to include, in YYYYMMDD format
apiInstance.metricsEditsAggregateProjectEditorTypePageTypeGranularityStartEndGet(project, editorType, pageType, granularity, start, end, (error, data, response) => {
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
 **pageType** | **String**| If you want to filter by page-type, use one of content (edits on pages in content namespaces) or non-content (edits on pages in non-content namespaces). If you are interested in edits regardless of their page-type, use all-page-types.  | 
 **granularity** | **String**| The time unit for the response data. As of today, supported values are daily and monthly.  | 
 **start** | **String**| The date of the first day to include, in YYYYMMDD format | 
 **end** | **String**| The date of the last day to include, in YYYYMMDD format | 

### Return type

[**Edits**](Edits.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## metricsEditsPerPageProjectPageTitleEditorTypeGranularityStartEndGet

> EditsPerPage metricsEditsPerPageProjectPageTitleEditorTypeGranularityStartEndGet(project, pageTitle, editorType, granularity, start, end)

Get edit counts for a page in a project.

Given a Mediawiki project, a page-title prefixed with its canonical namespace (for instance &#39;User:Jimbo_Wales&#39;) and a date range, returns a timeseries of edit counts. You can filter by editors-type (all-editor-types, anonymous, group-bot, name-bot, user). You can choose between daily and monthly granularity as well.  - Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental) - Rate limit: 25 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

### Example

```javascript
import Wikimedia from 'wikimedia';

let apiInstance = new Wikimedia.EditsDataApi();
let project = "project_example"; // String | The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off. For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org. 
let pageTitle = "pageTitle_example"; // String | The page-title to request edits for. It should be prefixed with canonical namespace. Spaces will be converted to underscores. 
let editorType = "editorType_example"; // String | If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types. 
let granularity = "granularity_example"; // String | Time unit for the response data. As of today, supported values are daily and monthly 
let start = "start_example"; // String | The date of the first day to include, in YYYYMMDD format
let end = "end_example"; // String | The date of the last day to include, in YYYYMMDD format
apiInstance.metricsEditsPerPageProjectPageTitleEditorTypeGranularityStartEndGet(project, pageTitle, editorType, granularity, start, end, (error, data, response) => {
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
 **pageTitle** | **String**| The page-title to request edits for. It should be prefixed with canonical namespace. Spaces will be converted to underscores.  | 
 **editorType** | **String**| If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types.  | 
 **granularity** | **String**| Time unit for the response data. As of today, supported values are daily and monthly  | 
 **start** | **String**| The date of the first day to include, in YYYYMMDD format | 
 **end** | **String**| The date of the last day to include, in YYYYMMDD format | 

### Return type

[**EditsPerPage**](EditsPerPage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json

