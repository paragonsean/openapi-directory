# EditsDataApi

All URIs are relative to *https://wikimedia.org/api/rest_v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**metricsEditsAggregateProjectEditorTypePageTypeGranularityStartEndGet**](EditsDataApi.md#metricsEditsAggregateProjectEditorTypePageTypeGranularityStartEndGet) | **GET** /metrics/edits/aggregate/{project}/{editor-type}/{page-type}/{granularity}/{start}/{end} | Get edits counts for a project. |
| [**metricsEditsPerPageProjectPageTitleEditorTypeGranularityStartEndGet**](EditsDataApi.md#metricsEditsPerPageProjectPageTitleEditorTypeGranularityStartEndGet) | **GET** /metrics/edits/per-page/{project}/{page-title}/{editor-type}/{granularity}/{start}/{end} | Get edit counts for a page in a project. |


<a id="metricsEditsAggregateProjectEditorTypePageTypeGranularityStartEndGet"></a>
# **metricsEditsAggregateProjectEditorTypePageTypeGranularityStartEndGet**
> Edits metricsEditsAggregateProjectEditorTypePageTypeGranularityStartEndGet(project, editorType, pageType, granularity, start, end)

Get edits counts for a project.

Given a Mediawiki project and a date range, returns a timeseries of edits counts. You can filter by editors-type (all-editor-types, anonymous, bot, registered) and page-type (all-page-types, content or non-content). You can choose between daily and monthly granularity as well.  - Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental) - Rate limit: 25 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wikimedia.org/api/rest_v1");

    EditsDataApi apiInstance = new EditsDataApi(defaultClient);
    String project = "project_example"; // String | The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off.  For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org. If you're interested in the aggregation of all projects, use all-projects. 
    String editorType = "all-editor-types"; // String | If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types. 
    String pageType = "all-page-types"; // String | If you want to filter by page-type, use one of content (edits on pages in content namespaces) or non-content (edits on pages in non-content namespaces). If you are interested in edits regardless of their page-type, use all-page-types. 
    String granularity = "daily"; // String | The time unit for the response data. As of today, supported values are daily and monthly. 
    String start = "start_example"; // String | The date of the first day to include, in YYYYMMDD format
    String end = "end_example"; // String | The date of the last day to include, in YYYYMMDD format
    try {
      Edits result = apiInstance.metricsEditsAggregateProjectEditorTypePageTypeGranularityStartEndGet(project, editorType, pageType, granularity, start, end);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsDataApi#metricsEditsAggregateProjectEditorTypePageTypeGranularityStartEndGet");
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
| **pageType** | **String**| If you want to filter by page-type, use one of content (edits on pages in content namespaces) or non-content (edits on pages in non-content namespaces). If you are interested in edits regardless of their page-type, use all-page-types.  | [enum: all-page-types, content, non-content] |
| **granularity** | **String**| The time unit for the response data. As of today, supported values are daily and monthly.  | [enum: daily, monthly] |
| **start** | **String**| The date of the first day to include, in YYYYMMDD format | |
| **end** | **String**| The date of the last day to include, in YYYYMMDD format | |

### Return type

[**Edits**](Edits.md)

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

<a id="metricsEditsPerPageProjectPageTitleEditorTypeGranularityStartEndGet"></a>
# **metricsEditsPerPageProjectPageTitleEditorTypeGranularityStartEndGet**
> EditsPerPage metricsEditsPerPageProjectPageTitleEditorTypeGranularityStartEndGet(project, pageTitle, editorType, granularity, start, end)

Get edit counts for a page in a project.

Given a Mediawiki project, a page-title prefixed with its canonical namespace (for instance &#39;User:Jimbo_Wales&#39;) and a date range, returns a timeseries of edit counts. You can filter by editors-type (all-editor-types, anonymous, group-bot, name-bot, user). You can choose between daily and monthly granularity as well.  - Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental) - Rate limit: 25 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditsDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wikimedia.org/api/rest_v1");

    EditsDataApi apiInstance = new EditsDataApi(defaultClient);
    String project = "project_example"; // String | The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off. For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org. 
    String pageTitle = "pageTitle_example"; // String | The page-title to request edits for. It should be prefixed with canonical namespace. Spaces will be converted to underscores. 
    String editorType = "all-editor-types"; // String | If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types. 
    String granularity = "daily"; // String | Time unit for the response data. As of today, supported values are daily and monthly 
    String start = "start_example"; // String | The date of the first day to include, in YYYYMMDD format
    String end = "end_example"; // String | The date of the last day to include, in YYYYMMDD format
    try {
      EditsPerPage result = apiInstance.metricsEditsPerPageProjectPageTitleEditorTypeGranularityStartEndGet(project, pageTitle, editorType, granularity, start, end);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditsDataApi#metricsEditsPerPageProjectPageTitleEditorTypeGranularityStartEndGet");
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
| **pageTitle** | **String**| The page-title to request edits for. It should be prefixed with canonical namespace. Spaces will be converted to underscores.  | |
| **editorType** | **String**| If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types.  | [enum: all-editor-types, anonymous, group-bot, name-bot, user] |
| **granularity** | **String**| Time unit for the response data. As of today, supported values are daily and monthly  | [enum: daily, monthly] |
| **start** | **String**| The date of the first day to include, in YYYYMMDD format | |
| **end** | **String**| The date of the last day to include, in YYYYMMDD format | |

### Return type

[**EditsPerPage**](EditsPerPage.md)

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

