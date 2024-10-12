# EditorsDataApi

All URIs are relative to *https://wikimedia.org/api/rest_v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**metricsEditorsAggregateProjectEditorTypePageTypeActivityLevelGranularityStartEndGet**](EditorsDataApi.md#metricsEditorsAggregateProjectEditorTypePageTypeActivityLevelGranularityStartEndGet) | **GET** /metrics/editors/aggregate/{project}/{editor-type}/{page-type}/{activity-level}/{granularity}/{start}/{end} | Get editors counts for a project. |
| [**metricsEditorsTopByAbsoluteBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet**](EditorsDataApi.md#metricsEditorsTopByAbsoluteBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet) | **GET** /metrics/editors/top-by-absolute-bytes-difference/{project}/{editor-type}/{page-type}/{year}/{month}/{day} | Get top 100 editors by absolute bytes-difference. |
| [**metricsEditorsTopByEditsProjectEditorTypePageTypeYearMonthDayGet**](EditorsDataApi.md#metricsEditorsTopByEditsProjectEditorTypePageTypeYearMonthDayGet) | **GET** /metrics/editors/top-by-edits/{project}/{editor-type}/{page-type}/{year}/{month}/{day} | Get top 100 editors by edits count. |
| [**metricsEditorsTopByNetBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet**](EditorsDataApi.md#metricsEditorsTopByNetBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet) | **GET** /metrics/editors/top-by-net-bytes-difference/{project}/{editor-type}/{page-type}/{year}/{month}/{day} | Get top 100 editors by net bytes-difference. |


<a id="metricsEditorsAggregateProjectEditorTypePageTypeActivityLevelGranularityStartEndGet"></a>
# **metricsEditorsAggregateProjectEditorTypePageTypeActivityLevelGranularityStartEndGet**
> Editors metricsEditorsAggregateProjectEditorTypePageTypeActivityLevelGranularityStartEndGet(project, editorType, pageType, activityLevel, granularity, start, end)

Get editors counts for a project.

Given a Mediawiki project and a date range, returns a timeseries of its editors counts. You can filter by editory-type (all-editor-types, anonymous, group-bot, name-bot, user), page-type (all-page-types, content or non-content) or activity-level (1..4-edits, 5..24-edits, 25..99-edits or 100..-edits). You can choose between daily and monthly granularity as well.  - Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental) - Rate limit: 25 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditorsDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wikimedia.org/api/rest_v1");

    EditorsDataApi apiInstance = new EditorsDataApi(defaultClient);
    String project = "project_example"; // String | The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off.  For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org. 
    String editorType = "all-editor-types"; // String | If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types. 
    String pageType = "all-page-types"; // String | If you want to filter by page-type, use one of content (edits made in content namespaces) or non-content (edits made in non-content namespaces). If you are interested in editors regardless of their page-type, use all-page-types. 
    String activityLevel = "all-activity-levels"; // String | If you want to filter by activity-level, use one of 1..4-edits, 5..24-edits, 25..99-edits or 100..-edits. If you are interested in editors regardless of their activity-level, use all-activity-levels. 
    String granularity = "daily"; // String | The time unit for the response data. As of today, supported values are daily and monthly. 
    String start = "start_example"; // String | The date of the first day to include, in YYYYMMDD format
    String end = "end_example"; // String | The date of the last day to include, in YYYYMMDD format
    try {
      Editors result = apiInstance.metricsEditorsAggregateProjectEditorTypePageTypeActivityLevelGranularityStartEndGet(project, editorType, pageType, activityLevel, granularity, start, end);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditorsDataApi#metricsEditorsAggregateProjectEditorTypePageTypeActivityLevelGranularityStartEndGet");
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
| **pageType** | **String**| If you want to filter by page-type, use one of content (edits made in content namespaces) or non-content (edits made in non-content namespaces). If you are interested in editors regardless of their page-type, use all-page-types.  | [enum: all-page-types, content, non-content] |
| **activityLevel** | **String**| If you want to filter by activity-level, use one of 1..4-edits, 5..24-edits, 25..99-edits or 100..-edits. If you are interested in editors regardless of their activity-level, use all-activity-levels.  | [enum: all-activity-levels, 1..4-edits, 5..24-edits, 25..99-edits, 100..-edits] |
| **granularity** | **String**| The time unit for the response data. As of today, supported values are daily and monthly.  | [enum: daily, monthly] |
| **start** | **String**| The date of the first day to include, in YYYYMMDD format | |
| **end** | **String**| The date of the last day to include, in YYYYMMDD format | |

### Return type

[**Editors**](Editors.md)

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

<a id="metricsEditorsTopByAbsoluteBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet"></a>
# **metricsEditorsTopByAbsoluteBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet**
> TopEditorsByAbsBytesDiff metricsEditorsTopByAbsoluteBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet(project, editorType, pageType, year, month, day)

Get top 100 editors by absolute bytes-difference.

Given a Mediawiki project and a date (day or month), returns a timeseries of the top 100 editors by absolute bytes-difference. You can filter by editor-type (all-editor-types, anonymous, group-bot, name-bot, user) or page-type (all-page-types, content or non-content). The user_text returned is either the mediawiki user_text if the user is registered, or null if user is anonymous.  - Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental) - Rate limit: 25 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditorsDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wikimedia.org/api/rest_v1");

    EditorsDataApi apiInstance = new EditorsDataApi(defaultClient);
    String project = "project_example"; // String | The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off. For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org. 
    String editorType = "all-editor-types"; // String | If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types. 
    String pageType = "all-page-types"; // String | If you want to filter by page-type, use one of content (edits on pages in content namespaces) or non-content (edits on pages in non-content namespaces). If you are interested in edits regardless of their page-type, use all-page-types. 
    String year = "year_example"; // String | The year of the date for which to retrieve top editors, in YYYY format.
    String month = "month_example"; // String | The month of the date for which to retrieve top editors, in MM format. If you want to get the top editors of a whole month, the day parameter should be all-days.
    String day = "day_example"; // String | The day of the date for which to retrieve top editors, in DD format, or all-days for a monthly value.
    try {
      TopEditorsByAbsBytesDiff result = apiInstance.metricsEditorsTopByAbsoluteBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet(project, editorType, pageType, year, month, day);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditorsDataApi#metricsEditorsTopByAbsoluteBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet");
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
| **year** | **String**| The year of the date for which to retrieve top editors, in YYYY format. | |
| **month** | **String**| The month of the date for which to retrieve top editors, in MM format. If you want to get the top editors of a whole month, the day parameter should be all-days. | |
| **day** | **String**| The day of the date for which to retrieve top editors, in DD format, or all-days for a monthly value. | |

### Return type

[**TopEditorsByAbsBytesDiff**](TopEditorsByAbsBytesDiff.md)

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

<a id="metricsEditorsTopByEditsProjectEditorTypePageTypeYearMonthDayGet"></a>
# **metricsEditorsTopByEditsProjectEditorTypePageTypeYearMonthDayGet**
> TopEditorsByEdits metricsEditorsTopByEditsProjectEditorTypePageTypeYearMonthDayGet(project, editorType, pageType, year, month, day)

Get top 100 editors by edits count.

Given a Mediawiki project and a date (day or month), returns a timeseries of the top 100 editors by edits count. You can filter by editor-type (all-editor-types, anonymous, group-bot, name-bot, user) or page-type (all-page-types, content or non-content). The user_text returned is either the mediawiki user_text if the user is registered, or null if user is anonymous.  - Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental) - Rate limit: 25 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditorsDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wikimedia.org/api/rest_v1");

    EditorsDataApi apiInstance = new EditorsDataApi(defaultClient);
    String project = "project_example"; // String | The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off. For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org. 
    String editorType = "all-editor-types"; // String | If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types. 
    String pageType = "all-page-types"; // String | If you want to filter by page-type, use one of content (edits on pages in content namespaces) or non-content (edits on pages in non-content namespaces). If you are interested in edits regardless of their page-type, use all-page-types. 
    String year = "year_example"; // String | The year of the date for which to retrieve top editors, in YYYY format.
    String month = "month_example"; // String | The month of the date for which to retrieve top editors, in MM format. If you want to get the top editors of a whole month, the day parameter should be all-days.
    String day = "day_example"; // String | The day of the date for which to retrieve top editors, in DD format, or all-days for a monthly value.
    try {
      TopEditorsByEdits result = apiInstance.metricsEditorsTopByEditsProjectEditorTypePageTypeYearMonthDayGet(project, editorType, pageType, year, month, day);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditorsDataApi#metricsEditorsTopByEditsProjectEditorTypePageTypeYearMonthDayGet");
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
| **year** | **String**| The year of the date for which to retrieve top editors, in YYYY format. | |
| **month** | **String**| The month of the date for which to retrieve top editors, in MM format. If you want to get the top editors of a whole month, the day parameter should be all-days. | |
| **day** | **String**| The day of the date for which to retrieve top editors, in DD format, or all-days for a monthly value. | |

### Return type

[**TopEditorsByEdits**](TopEditorsByEdits.md)

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

<a id="metricsEditorsTopByNetBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet"></a>
# **metricsEditorsTopByNetBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet**
> TopEditorsByNetBytesDiff metricsEditorsTopByNetBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet(project, editorType, pageType, year, month, day)

Get top 100 editors by net bytes-difference.

Given a Mediawiki project and a date (day or month), returns a timeseries of the top 100 editors by net bytes-difference. You can filter by editor-type (all-editor-types, anonymous, group-bot, name-bot, user) or page-type (all-page-types, content or non-content). The user_text returned is either the mediawiki user_text if the user is registered, or \&quot;Anonymous Editor\&quot; if user is anonymous.  - Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental) - Rate limit: 25 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditorsDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wikimedia.org/api/rest_v1");

    EditorsDataApi apiInstance = new EditorsDataApi(defaultClient);
    String project = "project_example"; // String | The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off. For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org. 
    String editorType = "all-editor-types"; // String | If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types. 
    String pageType = "all-page-types"; // String | If you want to filter by page-type, use one of content (edits on pages in content namespaces) or non-content (edits on pages in non-content namespaces). If you are interested in edits regardless of their page-type, use all-page-types. 
    String year = "year_example"; // String | The year of the date for which to retrieve top editors, in YYYY format.
    String month = "month_example"; // String | The month of the date for which to retrieve top editors, in MM format. If you want to get the top editors of a whole month, the day parameter should be all-days.
    String day = "day_example"; // String | The day of the date for which to retrieve top editors, in DD format, or all-days for a monthly value.
    try {
      TopEditorsByNetBytesDiff result = apiInstance.metricsEditorsTopByNetBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet(project, editorType, pageType, year, month, day);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditorsDataApi#metricsEditorsTopByNetBytesDifferenceProjectEditorTypePageTypeYearMonthDayGet");
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
| **year** | **String**| The year of the date for which to retrieve top editors, in YYYY format. | |
| **month** | **String**| The month of the date for which to retrieve top editors, in MM format. If you want to get the top editors of a whole month, the day parameter should be all-days. | |
| **day** | **String**| The day of the date for which to retrieve top editors, in DD format, or all-days for a monthly value. | |

### Return type

[**TopEditorsByNetBytesDiff**](TopEditorsByNetBytesDiff.md)

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

