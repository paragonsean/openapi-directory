# EditedPagesDataApi

All URIs are relative to *https://wikimedia.org/api/rest_v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**metricsEditedPagesAggregateProjectEditorTypePageTypeActivityLevelGranularityStartEndGet**](EditedPagesDataApi.md#metricsEditedPagesAggregateProjectEditorTypePageTypeActivityLevelGranularityStartEndGet) | **GET** /metrics/edited-pages/aggregate/{project}/{editor-type}/{page-type}/{activity-level}/{granularity}/{start}/{end} | Get edited-pages counts for a project. |
| [**metricsEditedPagesNewProjectEditorTypePageTypeGranularityStartEndGet**](EditedPagesDataApi.md#metricsEditedPagesNewProjectEditorTypePageTypeGranularityStartEndGet) | **GET** /metrics/edited-pages/new/{project}/{editor-type}/{page-type}/{granularity}/{start}/{end} | Get new pages counts for a project. |
| [**metricsEditedPagesTopByAbsoluteBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet**](EditedPagesDataApi.md#metricsEditedPagesTopByAbsoluteBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet) | **GET** /metrics/edited-pages/top-by-absolute-bytes-difference/{project}/{editor-type}/{page-type}/{year}/{month}/{day} | Get top 100 edited-pages by absolute bytes-difference. |
| [**metricsEditedPagesTopByEditsProjectEditorTypePageTypeYearMonthDayGet**](EditedPagesDataApi.md#metricsEditedPagesTopByEditsProjectEditorTypePageTypeYearMonthDayGet) | **GET** /metrics/edited-pages/top-by-edits/{project}/{editor-type}/{page-type}/{year}/{month}/{day} | Get top 100 edited-pages by edits count. |
| [**metricsEditedPagesTopByNetBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet**](EditedPagesDataApi.md#metricsEditedPagesTopByNetBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet) | **GET** /metrics/edited-pages/top-by-net-bytes-difference/{project}/{editor-type}/{page-type}/{year}/{month}/{day} | Get top 100 edited-pages by net bytes-difference. |


<a id="metricsEditedPagesAggregateProjectEditorTypePageTypeActivityLevelGranularityStartEndGet"></a>
# **metricsEditedPagesAggregateProjectEditorTypePageTypeActivityLevelGranularityStartEndGet**
> EditedPages metricsEditedPagesAggregateProjectEditorTypePageTypeActivityLevelGranularityStartEndGet(project, editorType, pageType, activityLevel, granularity, start, end)

Get edited-pages counts for a project.

Given a Mediawiki project and a date range, returns a timeseries of its edited-pages counts. You can filter by editor-type (all-editor-types, anonymous, group-bot, name-bot, user), page-type (all-page-types, content or non-content) or activity-level (1..4-edits, 5..24-edits, 25..99-edits, 100..-edits). You can choose between daily and monthly granularity as well.  - Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental) - Rate limit: 25 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditedPagesDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wikimedia.org/api/rest_v1");

    EditedPagesDataApi apiInstance = new EditedPagesDataApi(defaultClient);
    String project = "project_example"; // String | The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off.  For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org. 
    String editorType = "all-editor-types"; // String | If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types. 
    String pageType = "all-page-types"; // String | If you want to filter by page-type, use one of content (edited-pages in content namespaces) or non-content (edited-pages in non-content namespaces). If you are interested in edited-pages regardless of their page-type, use all-page-types. 
    String activityLevel = "all-activity-levels"; // String | If you want to filter by activity-level, use one of 1..4-edits, 5..24-edits, 25..99-edits or 100..-edits. If you are interested in edited-pages regardless of their activity level, use all-activity-levels. 
    String granularity = "daily"; // String | The time unit for the response data. As of today, supported values are daily and monthly. 
    String start = "start_example"; // String | The date of the first day to include, in YYYYMMDD format
    String end = "end_example"; // String | The date of the last day to include, in YYYYMMDD format
    try {
      EditedPages result = apiInstance.metricsEditedPagesAggregateProjectEditorTypePageTypeActivityLevelGranularityStartEndGet(project, editorType, pageType, activityLevel, granularity, start, end);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditedPagesDataApi#metricsEditedPagesAggregateProjectEditorTypePageTypeActivityLevelGranularityStartEndGet");
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
| **project** | **String**| The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off.  For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org.  | |
| **editorType** | **String**| If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types.  | [enum: all-editor-types, anonymous, group-bot, name-bot, user] |
| **pageType** | **String**| If you want to filter by page-type, use one of content (edited-pages in content namespaces) or non-content (edited-pages in non-content namespaces). If you are interested in edited-pages regardless of their page-type, use all-page-types.  | [enum: all-page-types, content, non-content] |
| **activityLevel** | **String**| If you want to filter by activity-level, use one of 1..4-edits, 5..24-edits, 25..99-edits or 100..-edits. If you are interested in edited-pages regardless of their activity level, use all-activity-levels.  | [enum: all-activity-levels, 1..4-edits, 5..24-edits, 25..99-edits, 100..-edits] |
| **granularity** | **String**| The time unit for the response data. As of today, supported values are daily and monthly.  | [enum: daily, monthly] |
| **start** | **String**| The date of the first day to include, in YYYYMMDD format | |
| **end** | **String**| The date of the last day to include, in YYYYMMDD format | |

### Return type

[**EditedPages**](EditedPages.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of values |  -  |
| **0** | Error |  -  |

<a id="metricsEditedPagesNewProjectEditorTypePageTypeGranularityStartEndGet"></a>
# **metricsEditedPagesNewProjectEditorTypePageTypeGranularityStartEndGet**
> NewPages metricsEditedPagesNewProjectEditorTypePageTypeGranularityStartEndGet(project, editorType, pageType, granularity, start, end)

Get new pages counts for a project.

Given a Mediawiki project and a date range, returns a timeseries of its new pages counts. You can filter by editor type (all-editor-types, anonymous, group-bot, name-bot, user) or page-type (all-page-types, content or non-content). You can choose between daily and monthly granularity as well.  - Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental) - Rate limit: 25 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditedPagesDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wikimedia.org/api/rest_v1");

    EditedPagesDataApi apiInstance = new EditedPagesDataApi(defaultClient);
    String project = "project_example"; // String | The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off.  For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org. If you're interested in the aggregation of all projects, use all-projects. 
    String editorType = "all-editor-types"; // String | If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types. 
    String pageType = "all-page-types"; // String | If you want to filter by page-type, use one of content (new pages in content namespaces) or non-content (new pages in non-content namespaces). If you are interested in new-articles regardless of their page-type, use all-page-types. 
    String granularity = "daily"; // String | The time unit for the response data. As of today, supported values are daily and monthly. 
    String start = "start_example"; // String | The date of the first day to include, in YYYYMMDD format
    String end = "end_example"; // String | The date of the last day to include, in YYYYMMDD format
    try {
      NewPages result = apiInstance.metricsEditedPagesNewProjectEditorTypePageTypeGranularityStartEndGet(project, editorType, pageType, granularity, start, end);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditedPagesDataApi#metricsEditedPagesNewProjectEditorTypePageTypeGranularityStartEndGet");
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
| **project** | **String**| The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off.  For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org. If you&#39;re interested in the aggregation of all projects, use all-projects.  | |
| **editorType** | **String**| If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types.  | [enum: all-editor-types, anonymous, group-bot, name-bot, user] |
| **pageType** | **String**| If you want to filter by page-type, use one of content (new pages in content namespaces) or non-content (new pages in non-content namespaces). If you are interested in new-articles regardless of their page-type, use all-page-types.  | [enum: all-page-types, content, non-content] |
| **granularity** | **String**| The time unit for the response data. As of today, supported values are daily and monthly.  | [enum: daily, monthly] |
| **start** | **String**| The date of the first day to include, in YYYYMMDD format | |
| **end** | **String**| The date of the last day to include, in YYYYMMDD format | |

### Return type

[**NewPages**](NewPages.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of values |  -  |
| **0** | Error |  -  |

<a id="metricsEditedPagesTopByAbsoluteBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet"></a>
# **metricsEditedPagesTopByAbsoluteBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet**
> TopEditedPagesByAbsBytesDiff metricsEditedPagesTopByAbsoluteBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet(project, editorType, pageType, year, month, day)

Get top 100 edited-pages by absolute bytes-difference.

Given a Mediawiki project and a date (day or month), returns a timeseries of the top 100 edited-pages by absolute bytes-difference. You can filter by editor-type (all-editor-types, anonymous, group-bot, name-bot, user) or page-type (all-page-types, content or non-content).  - Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental) - Rate limit: 25 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditedPagesDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wikimedia.org/api/rest_v1");

    EditedPagesDataApi apiInstance = new EditedPagesDataApi(defaultClient);
    String project = "project_example"; // String | The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off. For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org. 
    String editorType = "all-editor-types"; // String | If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types. 
    String pageType = "all-page-types"; // String | If you want to filter by page-type, use one of content (edits on pages in content namespaces) or non-content (edits on pages in non-content namespaces). If you are interested in edits regardless of their page-type, use all-page-types. 
    String year = "year_example"; // String | The year of the date for which to retrieve top edited-pages, in YYYY format.
    String month = "month_example"; // String | The month of the date for which to retrieve top edited-pages, in MM format. If you want to get the top edited-pages of a whole month, the day parameter should be all-days.
    String day = "day_example"; // String | The day of the date for which to retrieve top edited-pages, in DD format, or all-days for a monthly value.
    try {
      TopEditedPagesByAbsBytesDiff result = apiInstance.metricsEditedPagesTopByAbsoluteBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet(project, editorType, pageType, year, month, day);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditedPagesDataApi#metricsEditedPagesTopByAbsoluteBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet");
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
| **project** | **String**| The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off. For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org.  | |
| **editorType** | **String**| If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types.  | [enum: all-editor-types, anonymous, group-bot, name-bot, user] |
| **pageType** | **String**| If you want to filter by page-type, use one of content (edits on pages in content namespaces) or non-content (edits on pages in non-content namespaces). If you are interested in edits regardless of their page-type, use all-page-types.  | [enum: all-page-types, content, non-content] |
| **year** | **String**| The year of the date for which to retrieve top edited-pages, in YYYY format. | |
| **month** | **String**| The month of the date for which to retrieve top edited-pages, in MM format. If you want to get the top edited-pages of a whole month, the day parameter should be all-days. | |
| **day** | **String**| The day of the date for which to retrieve top edited-pages, in DD format, or all-days for a monthly value. | |

### Return type

[**TopEditedPagesByAbsBytesDiff**](TopEditedPagesByAbsBytesDiff.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of values |  -  |
| **0** | Error |  -  |

<a id="metricsEditedPagesTopByEditsProjectEditorTypePageTypeYearMonthDayGet"></a>
# **metricsEditedPagesTopByEditsProjectEditorTypePageTypeYearMonthDayGet**
> TopEditedPagesByEdits metricsEditedPagesTopByEditsProjectEditorTypePageTypeYearMonthDayGet(project, editorType, pageType, year, month, day)

Get top 100 edited-pages by edits count.

Given a Mediawiki project and a date (day or month), returns a timeseries of the top 100 edited-pages by edits count. You can filter by editor-type (all-editor-types, anonymous, group-bot, name-bot, user) or page-type (all-page-types, content or non-content).  - Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental) - Rate limit: 25 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditedPagesDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wikimedia.org/api/rest_v1");

    EditedPagesDataApi apiInstance = new EditedPagesDataApi(defaultClient);
    String project = "project_example"; // String | The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off. For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org. 
    String editorType = "all-editor-types"; // String | If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types. 
    String pageType = "all-page-types"; // String | If you want to filter by page-type, use one of content (edits on pages in content namespaces) or non-content (edits on pages in non-content namespaces). If you are interested in edits regardless of their page-type, use all-page-types. 
    String year = "year_example"; // String | The year of the date for which to retrieve top edited-pages, in YYYY format.
    String month = "month_example"; // String | The month of the date for which to retrieve top edited-pages, in MM format. If you want to get the top edited-pages of a whole month, the day parameter should be all-days.
    String day = "day_example"; // String | The day of the date for which to retrieve top edited-pages, in DD format, or all-days for a monthly value.
    try {
      TopEditedPagesByEdits result = apiInstance.metricsEditedPagesTopByEditsProjectEditorTypePageTypeYearMonthDayGet(project, editorType, pageType, year, month, day);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditedPagesDataApi#metricsEditedPagesTopByEditsProjectEditorTypePageTypeYearMonthDayGet");
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
| **project** | **String**| The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off. For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org.  | |
| **editorType** | **String**| If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types.  | [enum: all-editor-types, anonymous, group-bot, name-bot, user] |
| **pageType** | **String**| If you want to filter by page-type, use one of content (edits on pages in content namespaces) or non-content (edits on pages in non-content namespaces). If you are interested in edits regardless of their page-type, use all-page-types.  | [enum: all-page-types, content, non-content] |
| **year** | **String**| The year of the date for which to retrieve top edited-pages, in YYYY format. | |
| **month** | **String**| The month of the date for which to retrieve top edited-pages, in MM format. If you want to get the top edited-pages of a whole month, the day parameter should be all-days. | |
| **day** | **String**| The day of the date for which to retrieve top edited-pages, in DD format, or all-days for a monthly value. | |

### Return type

[**TopEditedPagesByEdits**](TopEditedPagesByEdits.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of values |  -  |
| **0** | Error |  -  |

<a id="metricsEditedPagesTopByNetBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet"></a>
# **metricsEditedPagesTopByNetBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet**
> TopEditedPagesByNetBytesDiff metricsEditedPagesTopByNetBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet(project, editorType, pageType, year, month, day)

Get top 100 edited-pages by net bytes-difference.

Given a Mediawiki project and a date (day or month), returns a timeseries of the top 100 edited-pages by net bytes-difference. You can filter by editor-type (all-editor-types, anonymous, group-bot, name-bot, user) or page-type (all-page-types, content or non-content).  - Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental) - Rate limit: 25 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditedPagesDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wikimedia.org/api/rest_v1");

    EditedPagesDataApi apiInstance = new EditedPagesDataApi(defaultClient);
    String project = "project_example"; // String | The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off. For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org. 
    String editorType = "all-editor-types"; // String | If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types. 
    String pageType = "all-page-types"; // String | If you want to filter by page-type, use one of content (edits on pages in content namespaces) or non-content (edits on pages in non-content namespaces). If you are interested in edits regardless of their page-type, use all-page-types. 
    String year = "year_example"; // String | The year of the date for which to retrieve top edited-pages, in YYYY format.
    String month = "month_example"; // String | The month of the date for which to retrieve top edited-pages, in MM format. If you want to get the top edited-pages of a whole month, the day parameter should be all-days.
    String day = "day_example"; // String | The day of the date for which to retrieve top edited-pages, in DD format, or all-days for a monthly value.
    try {
      TopEditedPagesByNetBytesDiff result = apiInstance.metricsEditedPagesTopByNetBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet(project, editorType, pageType, year, month, day);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditedPagesDataApi#metricsEditedPagesTopByNetBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet");
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
| **project** | **String**| The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off. For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org.  | |
| **editorType** | **String**| If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types.  | [enum: all-editor-types, anonymous, group-bot, name-bot, user] |
| **pageType** | **String**| If you want to filter by page-type, use one of content (edits on pages in content namespaces) or non-content (edits on pages in non-content namespaces). If you are interested in edits regardless of their page-type, use all-page-types.  | [enum: all-page-types, content, non-content] |
| **year** | **String**| The year of the date for which to retrieve top edited-pages, in YYYY format. | |
| **month** | **String**| The month of the date for which to retrieve top edited-pages, in MM format. If you want to get the top edited-pages of a whole month, the day parameter should be all-days. | |
| **day** | **String**| The day of the date for which to retrieve top edited-pages, in DD format, or all-days for a monthly value. | |

### Return type

[**TopEditedPagesByNetBytesDiff**](TopEditedPagesByNetBytesDiff.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of values |  -  |
| **0** | Error |  -  |

