# CanvasApi

All URIs are relative to *https://rest.iad-01.braze.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**canvasDataAnalyticsSummary_0**](CanvasApi.md#canvasDataAnalyticsSummary_0) | **GET** /canvas/data_summary | Canvas Data Analytics Summary |
| [**canvasDataSeriesAnalytics_0**](CanvasApi.md#canvasDataSeriesAnalytics_0) | **GET** /canvas/data_series | Canvas Data Series Analytics |
| [**canvasDetails_0**](CanvasApi.md#canvasDetails_0) | **GET** /canvas/details | Canvas Details |
| [**canvasList_0**](CanvasApi.md#canvasList_0) | **GET** /canvas/list | Canvas List |


<a id="canvasDataAnalyticsSummary_0"></a>
# **canvasDataAnalyticsSummary_0**
> canvasDataAnalyticsSummary_0(canvasId, endingAt, startingAt, length, includeVariantBreakdown, includeStepBreakdown, includeDeletedStepData)

Canvas Data Analytics Summary

This endpoint allows you to export rollups of time series data for a Canvas, providing a concise summary of a Canvas&#39; results.  ### Components Used - [Canvas Identifier](https://www.braze.com/docs/api/identifier_types/)  ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {   \&quot;data\&quot;: {     \&quot;name\&quot;: (string) Canvas name,     \&quot;total_stats\&quot;: {       \&quot;revenue\&quot;: (float),       \&quot;conversions\&quot;: (int),       \&quot;conversions_by_entry_time\&quot;: (int),       \&quot;entries\&quot;: (int)     },     \&quot;variant_stats\&quot;: (optional) {       \&quot;00000000-0000-0000-0000-0000000000000\&quot;: (API identifier for variant) {         \&quot;name\&quot;: (string) name of variant,         \&quot;revenue\&quot;: (float),         \&quot;conversions\&quot;: (int),         \&quot;entries\&quot;: (int)       },       ... (more variants)     },     \&quot;step_stats\&quot;: (optional) {       \&quot;00000000-0000-0000-0000-0000000000000\&quot;: (API identifier for step) {         \&quot;name\&quot;: (string) name of step,         \&quot;revenue\&quot;: (float),         \&quot;conversions\&quot;: (int),         \&quot;conversions_by_entry_time\&quot;: (int),         \&quot;messages\&quot;: {           \&quot;android_push\&quot;: (name of channel) [             {               \&quot;sent\&quot;: (int),               \&quot;opens\&quot;: (int),               \&quot;influenced_opens\&quot;: (int),               \&quot;bounces\&quot;: (int)               ... (more stats for channel)             }           ],           ... (more channels)         }       },       ... (more steps)     }   },   \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CanvasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.iad-01.braze.com");

    CanvasApi apiInstance = new CanvasApi(defaultClient);
    String canvasId = "{{canvas_id}}"; // String | (Required) String   Canvas API identifier
    String endingAt = "2018-05-30T23:59:59-5:00"; // String | (Required) DateTime (ISO 8601 string)  Date on which the data export should end - defaults to time of the request
    String startingAt = "2018-05-28T23:59:59-5:00"; // String | (Optional) DateTime (ISO 8601 string)  Date on which the data export should begin (either length or starting_at required)
    String length = "5"; // String | (Optional) Integer  Max number of days before ending_at to include in the returned series - must be between 1 and 14 inclusive (either length or starting_at required)
    String includeVariantBreakdown = "true"; // String | (Optional) Boolean  Whether or not to include variant stats (defaults to false)
    String includeStepBreakdown = "true"; // String | (Optional) Boolean  Whether or not to include step stats (defaults to false)
    String includeDeletedStepData = "true"; // String | (Optional) Boolean  Whether or not to include step stats for deleted steps (defaults to false)
    try {
      apiInstance.canvasDataAnalyticsSummary_0(canvasId, endingAt, startingAt, length, includeVariantBreakdown, includeStepBreakdown, includeDeletedStepData);
    } catch (ApiException e) {
      System.err.println("Exception when calling CanvasApi#canvasDataAnalyticsSummary_0");
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
| **canvasId** | **String**| (Required) String   Canvas API identifier | [optional] |
| **endingAt** | **String**| (Required) DateTime (ISO 8601 string)  Date on which the data export should end - defaults to time of the request | [optional] |
| **startingAt** | **String**| (Optional) DateTime (ISO 8601 string)  Date on which the data export should begin (either length or starting_at required) | [optional] |
| **length** | **String**| (Optional) Integer  Max number of days before ending_at to include in the returned series - must be between 1 and 14 inclusive (either length or starting_at required) | [optional] |
| **includeVariantBreakdown** | **String**| (Optional) Boolean  Whether or not to include variant stats (defaults to false) | [optional] |
| **includeStepBreakdown** | **String**| (Optional) Boolean  Whether or not to include step stats (defaults to false) | [optional] |
| **includeDeletedStepData** | **String**| (Optional) Boolean  Whether or not to include step stats for deleted steps (defaults to false) | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="canvasDataSeriesAnalytics_0"></a>
# **canvasDataSeriesAnalytics_0**
> canvasDataSeriesAnalytics_0(canvasId, endingAt, startingAt, length, includeVariantBreakdown, includeStepBreakdown, includeDeletedStepData)

Canvas Data Series Analytics

This endpoint allows you to export time series data for a Canvas.  ### Components Used - [Canvas Identifier](https://www.braze.com/docs/api/identifier_types/)  ## Response &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {   \&quot;data\&quot;: {     \&quot;name\&quot;: (string) Canvas name,     \&quot;stats\&quot;: [       {         \&quot;time\&quot;: (string) date as ISO 8601 date,         \&quot;total_stats\&quot;: {           \&quot;revenue\&quot;: (float),           \&quot;conversions\&quot;: (int),           \&quot;conversions_by_entry_time\&quot;: (int),           \&quot;entries\&quot;: (int)         },         \&quot;variant_stats\&quot;: (optional) {           \&quot;00000000-0000-0000-0000-0000000000000\&quot;: (API identifier for variant) {             \&quot;name\&quot;: (string) name of variant,             \&quot;revenue\&quot;: (int),             \&quot;conversions\&quot;: (int),             \&quot;conversions_by_entry_time\&quot;: (int),             \&quot;entries\&quot;: (int)           },           ... (more variants)         },         \&quot;step_stats\&quot;: (optional) {           \&quot;00000000-0000-0000-0000-0000000000000\&quot;: (API identifier for step) {             \&quot;name\&quot;: (string) name of step,             \&quot;revenue\&quot;: (float),             \&quot;conversions\&quot;: (int),             \&quot;conversions_by_entry_time\&quot;: (int),             \&quot;messages\&quot;: {               \&quot;email\&quot;: [                 {                   \&quot;sent\&quot;: (int),                   \&quot;opens\&quot;: (int),                   \&quot;unique_opens\&quot;: (int),                   \&quot;clicks\&quot;: (int),                   ... (more stats)                 }               ],               ... (more channels)             }           },           ... (more steps)         }       },       ... (more stats by time)     ]   },   \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CanvasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.iad-01.braze.com");

    CanvasApi apiInstance = new CanvasApi(defaultClient);
    String canvasId = "{{canvas_id}}"; // String | (Required) String  Canvas API Identifier
    String endingAt = "2018-05-30T23:59:59-5:00"; // String | (Required) DateTime (ISO 8601 string)  Date on which the data export should end - defaults to time of the request
    String startingAt = "2018-05-28T23:59:59-5:00"; // String | (Optional) DateTime (ISO 8601 string)   Date on which the data export should begin (either length or starting_at are required)
    String length = "10"; // String | (Optional) DateTime (ISO 8601 string)  Max number of days before ending_at to include in the returned series - must be between 1 and 14 inclusive (either length or starting_at required)
    String includeVariantBreakdown = "true"; // String | (Optional) Boolean  Whether or not to include variant stats (defaults to false)
    String includeStepBreakdown = "true"; // String | (Optional) Boolean  Whether or not to include step stats (defaults to false)
    String includeDeletedStepData = "true"; // String | (Optional) Boolean  Whether or not to include step stats for deleted steps (defaults to false)
    try {
      apiInstance.canvasDataSeriesAnalytics_0(canvasId, endingAt, startingAt, length, includeVariantBreakdown, includeStepBreakdown, includeDeletedStepData);
    } catch (ApiException e) {
      System.err.println("Exception when calling CanvasApi#canvasDataSeriesAnalytics_0");
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
| **canvasId** | **String**| (Required) String  Canvas API Identifier | [optional] |
| **endingAt** | **String**| (Required) DateTime (ISO 8601 string)  Date on which the data export should end - defaults to time of the request | [optional] |
| **startingAt** | **String**| (Optional) DateTime (ISO 8601 string)   Date on which the data export should begin (either length or starting_at are required) | [optional] |
| **length** | **String**| (Optional) DateTime (ISO 8601 string)  Max number of days before ending_at to include in the returned series - must be between 1 and 14 inclusive (either length or starting_at required) | [optional] |
| **includeVariantBreakdown** | **String**| (Optional) Boolean  Whether or not to include variant stats (defaults to false) | [optional] |
| **includeStepBreakdown** | **String**| (Optional) Boolean  Whether or not to include step stats (defaults to false) | [optional] |
| **includeDeletedStepData** | **String**| (Optional) Boolean  Whether or not to include step stats for deleted steps (defaults to false) | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="canvasDetails_0"></a>
# **canvasDetails_0**
> canvasDetails_0(canvasId)

Canvas Details

This endpoint allows you to export metadata about a Canvas, such as its name, when it was created, its current status, and more.  ### Components Used - [Canvas Identifier](https://www.braze.com/docs/api/identifier_types/)  ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {   \&quot;created_at\&quot;: (string) date created as ISO 8601 date,   \&quot;updated_at\&quot;: (string) date updated as ISO 8601 date,   \&quot;name\&quot;: (string) Canvas name,   \&quot;description\&quot;: (string) Canvas description,   \&quot;archived\&quot;: (boolean) whether this Canvas is archived,   \&quot;draft\&quot;: (boolean) whether this Canvas is a draft,   \&quot;schedule_type\&quot;: (string) type of scheduling action,   \&quot;first_entry\&quot;: (string) date of first entry as ISO 8601 date,   \&quot;last_entry\&quot;: (string) date of last entry as ISO 8601 date,   \&quot;channels\&quot;: (array of strings) step channels used with Canvas,   \&quot;variants\&quot;: [     {       \&quot;name\&quot;: (string) name of variant,       \&quot;id\&quot;: (string) API identifier of the variant,       \&quot;first_step_ids\&quot;: (array of strings) API identifiers for first steps in variant,       \&quot;first_step_id\&quot;: (string) API identifier of first step in variant (deprecated in November 2017, only included if the variant has only one first step)     },     ... (more variations)   ],   \&quot;tags\&quot;: (array of strings) tag names associated with the Canvas,   \&quot;steps\&quot;: [     {       \&quot;name\&quot;: (string) name of step,       \&quot;id\&quot;: (string) API identifier of the step,       \&quot;next_step_ids\&quot;: (array of strings) API identifiers of steps following step,       \&quot;channels\&quot;: (array of strings) channels used in step,       \&quot;messages\&quot;: {           \&quot;message_variation_id\&quot;: (string) {  // &lt;&#x3D;This is the actual id               \&quot;channel\&quot;: (string) channel type of the message (eg., \&quot;email\&quot;),               ... channel-specific fields for this message, see Campaign Details Endpoint API Response for example message responses ...           }       }     },     ... (more steps)   ],   \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CanvasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.iad-01.braze.com");

    CanvasApi apiInstance = new CanvasApi(defaultClient);
    String canvasId = "{{canvas_identifier}}"; // String | (Required) String  Canvas API Identifier 
    try {
      apiInstance.canvasDetails_0(canvasId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CanvasApi#canvasDetails_0");
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
| **canvasId** | **String**| (Required) String  Canvas API Identifier  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="canvasList_0"></a>
# **canvasList_0**
> canvasList_0(page, includeArchived, sortDirection, lastEditTimeGt)

Canvas List

This endpoint allows you to export a list of Canvases, including the name, Canvas API Identifier and associated Tags. The Canvases are returned in groups of 100 sorted by time of creation (oldest to newest by default).  &gt; Archived Canvases will not be included in the API response unless the &#x60;include_archived&#x60; field is specified. Canvases that are stopped but not archived, however, will be returned by default.   ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {   \&quot;canvases\&quot; : [    {     \&quot;id\&quot; : (string) Canvas API Identifier,     \&quot;last_edited\&quot;: (ISO 8601 string) the last edited time for the message,     \&quot;name\&quot; : (string) Canvas name,     \&quot;tags\&quot; : (array) tag names associated with the Canvas,    },     ... (more Canvases)   ],   \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CanvasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.iad-01.braze.com");

    CanvasApi apiInstance = new CanvasApi(defaultClient);
    String page = "1"; // String | (Optional) Integer  The page of Canvases to return, defaults to `0` (returns the first set of up to 100)
    String includeArchived = "false"; // String | (Optional) Boolean  Whether or not to include archived Canvases, defaults to `false`.
    String sortDirection = "desc"; // String | (Optional) String  Pass in the value `desc` to sort by creation time from newest to oldest. Pass in `asc` to sort from oldest to newest. If sort_direction is not included, the default order is oldest to newest.
    String lastEditTimeGt = "2020-06-28T23:59:59-5:00"; // String | (Optional) DateTime (ISO 8601 string)  Filters the results and only returns Canvases that were edited greater than the time provided till now.
    try {
      apiInstance.canvasList_0(page, includeArchived, sortDirection, lastEditTimeGt);
    } catch (ApiException e) {
      System.err.println("Exception when calling CanvasApi#canvasList_0");
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
| **page** | **String**| (Optional) Integer  The page of Canvases to return, defaults to &#x60;0&#x60; (returns the first set of up to 100) | [optional] |
| **includeArchived** | **String**| (Optional) Boolean  Whether or not to include archived Canvases, defaults to &#x60;false&#x60;. | [optional] |
| **sortDirection** | **String**| (Optional) String  Pass in the value &#x60;desc&#x60; to sort by creation time from newest to oldest. Pass in &#x60;asc&#x60; to sort from oldest to newest. If sort_direction is not included, the default order is oldest to newest. | [optional] |
| **lastEditTimeGt** | **String**| (Optional) DateTime (ISO 8601 string)  Filters the results and only returns Canvases that were edited greater than the time provided till now. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

