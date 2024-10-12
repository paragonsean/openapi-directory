# AggregatedApi

All URIs are relative to *http://apiv2.clickmeter.com:80*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**aggregatedGetConversionsSummary**](AggregatedApi.md#aggregatedGetConversionsSummary) | **GET** /aggregated/summary/conversions | Retrieve statistics about a subset of conversions for a timeframe with conversions data |
| [**aggregatedGetDatapointsSummary**](AggregatedApi.md#aggregatedGetDatapointsSummary) | **GET** /aggregated/summary/datapoints | Retrieve statistics about a subset of datapoints for a timeframe with datapoints data |
| [**aggregatedGetGroupsSummary**](AggregatedApi.md#aggregatedGetGroupsSummary) | **GET** /aggregated/summary/groups | Retrieve statistics about a subset of groups for a timeframe with groups data |
| [**aggregatedGetStatisticsList**](AggregatedApi.md#aggregatedGetStatisticsList) | **GET** /aggregated/list | Retrieve statistics about this customer for a timeframe grouped by some temporal entity (day/week/month) |
| [**aggregatedGetStatisticsSingle**](AggregatedApi.md#aggregatedGetStatisticsSingle) | **GET** /aggregated | Retrieve statistics about this customer for a timeframe |


<a id="aggregatedGetConversionsSummary"></a>
# **aggregatedGetConversionsSummary**
> ApiCoreDtoAggregatedAggregatedSummaryResult aggregatedGetConversionsSummary(timeFrame, fromDay, toDay, status, sortBy, sortDirection, offset, limit, textSearch)

Retrieve statistics about a subset of conversions for a timeframe with conversions data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AggregatedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    AggregatedApi apiInstance = new AggregatedApi(defaultClient);
    String timeFrame = "today"; // String | Timeframe of the request. See list at $timeframeList
    String fromDay = "fromDay_example"; // String | If using a \"custom\" timeFrame you can specify the starting day (YYYYMMDD)
    String toDay = "toDay_example"; // String | If using a \"custom\" timeFrame you can specify the ending day (YYYYMMDD)
    String status = "deleted"; // String | Status of conversion (\"deleted\"/\"active\")
    String sortBy = "sortBy_example"; // String | Field to sort by
    String sortDirection = "asc"; // String | Direction of sort \"asc\" or \"desc\"
    Integer offset = 56; // Integer | Offset where to start from
    Integer limit = 56; // Integer | Limit results to this number
    String textSearch = "textSearch_example"; // String | Filter fields by this pattern
    try {
      ApiCoreDtoAggregatedAggregatedSummaryResult result = apiInstance.aggregatedGetConversionsSummary(timeFrame, fromDay, toDay, status, sortBy, sortDirection, offset, limit, textSearch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AggregatedApi#aggregatedGetConversionsSummary");
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
| **timeFrame** | **String**| Timeframe of the request. See list at $timeframeList | [enum: today, yesterday, last7, last30, lastmonth, currentmonth, previousmonth, last90, last120, last180, last12months, lastyear, currentyear, beginning, custom] |
| **fromDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the starting day (YYYYMMDD) | [optional] |
| **toDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the ending day (YYYYMMDD) | [optional] |
| **status** | **String**| Status of conversion (\&quot;deleted\&quot;/\&quot;active\&quot;) | [optional] [enum: deleted, active] |
| **sortBy** | **String**| Field to sort by | [optional] |
| **sortDirection** | **String**| Direction of sort \&quot;asc\&quot; or \&quot;desc\&quot; | [optional] [enum: asc, desc] |
| **offset** | **Integer**| Offset where to start from | [optional] |
| **limit** | **Integer**| Limit results to this number | [optional] |
| **textSearch** | **String**| Filter fields by this pattern | [optional] |

### Return type

[**ApiCoreDtoAggregatedAggregatedSummaryResult**](ApiCoreDtoAggregatedAggregatedSummaryResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |

<a id="aggregatedGetDatapointsSummary"></a>
# **aggregatedGetDatapointsSummary**
> ApiCoreDtoAggregatedAggregatedSummaryResult aggregatedGetDatapointsSummary(timeFrame, type, fromDay, toDay, status, tag, favourite, sortBy, sortDirection, offset, limit, groupId, textSearch)

Retrieve statistics about a subset of datapoints for a timeframe with datapoints data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AggregatedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    AggregatedApi apiInstance = new AggregatedApi(defaultClient);
    String timeFrame = "today"; // String | Timeframe of the request. See list at $timeframeList
    String type = "tp"; // String | Type of datapoint (\"tl\"/\"tp\")
    String fromDay = "fromDay_example"; // String | If using a \"custom\" timeFrame you can specify the starting day (YYYYMMDD)
    String toDay = "toDay_example"; // String | If using a \"custom\" timeFrame you can specify the ending day (YYYYMMDD)
    String status = "deleted"; // String | Status of datapoint (\"deleted\"/\"active\"/\"paused\"/\"spam\")
    String tag = "tag_example"; // String | A comma separated list of tags you want to filter with.
    Boolean favourite = true; // Boolean | Is the datapoint marked as favourite
    String sortBy = "sortBy_example"; // String | Field to sort by
    String sortDirection = "asc"; // String | Direction of sort \"asc\" or \"desc\"
    Integer offset = 56; // Integer | Offset where to start from
    Integer limit = 56; // Integer | Limit results to this number
    Long groupId = 56L; // Long | Filter by this group id
    String textSearch = "textSearch_example"; // String | Filter fields by this pattern
    try {
      ApiCoreDtoAggregatedAggregatedSummaryResult result = apiInstance.aggregatedGetDatapointsSummary(timeFrame, type, fromDay, toDay, status, tag, favourite, sortBy, sortDirection, offset, limit, groupId, textSearch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AggregatedApi#aggregatedGetDatapointsSummary");
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
| **timeFrame** | **String**| Timeframe of the request. See list at $timeframeList | [enum: today, yesterday, last7, last30, lastmonth, currentmonth, previousmonth, last90, last120, last180, last12months, lastyear, currentyear, beginning, custom] |
| **type** | **String**| Type of datapoint (\&quot;tl\&quot;/\&quot;tp\&quot;) | [enum: tp, tl] |
| **fromDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the starting day (YYYYMMDD) | [optional] |
| **toDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the ending day (YYYYMMDD) | [optional] |
| **status** | **String**| Status of datapoint (\&quot;deleted\&quot;/\&quot;active\&quot;/\&quot;paused\&quot;/\&quot;spam\&quot;) | [optional] [enum: deleted, active, paused, spam] |
| **tag** | **String**| A comma separated list of tags you want to filter with. | [optional] |
| **favourite** | **Boolean**| Is the datapoint marked as favourite | [optional] |
| **sortBy** | **String**| Field to sort by | [optional] |
| **sortDirection** | **String**| Direction of sort \&quot;asc\&quot; or \&quot;desc\&quot; | [optional] [enum: asc, desc] |
| **offset** | **Integer**| Offset where to start from | [optional] |
| **limit** | **Integer**| Limit results to this number | [optional] |
| **groupId** | **Long**| Filter by this group id | [optional] |
| **textSearch** | **String**| Filter fields by this pattern | [optional] |

### Return type

[**ApiCoreDtoAggregatedAggregatedSummaryResult**](ApiCoreDtoAggregatedAggregatedSummaryResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |

<a id="aggregatedGetGroupsSummary"></a>
# **aggregatedGetGroupsSummary**
> ApiCoreDtoAggregatedAggregatedSummaryResult aggregatedGetGroupsSummary(timeFrame, fromDay, toDay, status, tag, favourite, sortBy, sortDirection, offset, limit, textSearch)

Retrieve statistics about a subset of groups for a timeframe with groups data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AggregatedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    AggregatedApi apiInstance = new AggregatedApi(defaultClient);
    String timeFrame = "today"; // String | Timeframe of the request. See list at $timeframeList
    String fromDay = "fromDay_example"; // String | If using a \"custom\" timeFrame you can specify the starting day (YYYYMMDD)
    String toDay = "toDay_example"; // String | If using a \"custom\" timeFrame you can specify the ending day (YYYYMMDD)
    String status = "deleted"; // String | Status of group (\"deleted\"/\"active\")
    String tag = "tag_example"; // String | A comma separated list of tags you want to filter with.
    Boolean favourite = true; // Boolean | Is the group marked as favourite
    String sortBy = "sortBy_example"; // String | Field to sort by
    String sortDirection = "asc"; // String | Direction of sort \"asc\" or \"desc\"
    Integer offset = 56; // Integer | Offset where to start from
    Integer limit = 56; // Integer | Limit results to this number
    String textSearch = "textSearch_example"; // String | Filter fields by this pattern
    try {
      ApiCoreDtoAggregatedAggregatedSummaryResult result = apiInstance.aggregatedGetGroupsSummary(timeFrame, fromDay, toDay, status, tag, favourite, sortBy, sortDirection, offset, limit, textSearch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AggregatedApi#aggregatedGetGroupsSummary");
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
| **timeFrame** | **String**| Timeframe of the request. See list at $timeframeList | [enum: today, yesterday, last7, last30, lastmonth, currentmonth, previousmonth, last90, last120, last180, last12months, lastyear, currentyear, beginning, custom] |
| **fromDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the starting day (YYYYMMDD) | [optional] |
| **toDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the ending day (YYYYMMDD) | [optional] |
| **status** | **String**| Status of group (\&quot;deleted\&quot;/\&quot;active\&quot;) | [optional] [enum: deleted, active] |
| **tag** | **String**| A comma separated list of tags you want to filter with. | [optional] |
| **favourite** | **Boolean**| Is the group marked as favourite | [optional] |
| **sortBy** | **String**| Field to sort by | [optional] |
| **sortDirection** | **String**| Direction of sort \&quot;asc\&quot; or \&quot;desc\&quot; | [optional] [enum: asc, desc] |
| **offset** | **Integer**| Offset where to start from | [optional] |
| **limit** | **Integer**| Limit results to this number | [optional] |
| **textSearch** | **String**| Filter fields by this pattern | [optional] |

### Return type

[**ApiCoreDtoAggregatedAggregatedSummaryResult**](ApiCoreDtoAggregatedAggregatedSummaryResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |

<a id="aggregatedGetStatisticsList"></a>
# **aggregatedGetStatisticsList**
> ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult aggregatedGetStatisticsList(timeFrame, fromDay, toDay, groupBy)

Retrieve statistics about this customer for a timeframe grouped by some temporal entity (day/week/month)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AggregatedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    AggregatedApi apiInstance = new AggregatedApi(defaultClient);
    String timeFrame = "today"; // String | Timeframe of the request. See list at $timeframeList
    String fromDay = "fromDay_example"; // String | If using a \"custom\" timeFrame you can specify the starting day (YYYYMMDD)
    String toDay = "toDay_example"; // String | If using a \"custom\" timeFrame you can specify the ending day (YYYYMMDD)
    String groupBy = "week"; // String | The temporal entity you want to group by (\"week\"/\"month\"). If unspecified is \"day\".
    try {
      ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult result = apiInstance.aggregatedGetStatisticsList(timeFrame, fromDay, toDay, groupBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AggregatedApi#aggregatedGetStatisticsList");
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
| **timeFrame** | **String**| Timeframe of the request. See list at $timeframeList | [enum: today, yesterday, last7, last30, lastmonth, currentmonth, previousmonth, last90, last120, last180, last12months, lastyear, currentyear, beginning, custom] |
| **fromDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the starting day (YYYYMMDD) | [optional] |
| **toDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the ending day (YYYYMMDD) | [optional] |
| **groupBy** | **String**| The temporal entity you want to group by (\&quot;week\&quot;/\&quot;month\&quot;). If unspecified is \&quot;day\&quot;. | [optional] [enum: week, month] |

### Return type

[**ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult**](ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |

<a id="aggregatedGetStatisticsSingle"></a>
# **aggregatedGetStatisticsSingle**
> ApiCoreDtoAggregatedAggregatedResult aggregatedGetStatisticsSingle(timeFrame, fromDay, toDay, hourly, onlyFavorites)

Retrieve statistics about this customer for a timeframe

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AggregatedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    AggregatedApi apiInstance = new AggregatedApi(defaultClient);
    String timeFrame = "today"; // String | Timeframe of the request. See list at $timeframeList
    String fromDay = "fromDay_example"; // String | If using a \"custom\" timeFrame you can specify the starting day (YYYYMMDD)
    String toDay = "toDay_example"; // String | If using a \"custom\" timeFrame you can specify the ending day (YYYYMMDD)
    Boolean hourly = true; // Boolean | If using \"yesterday\" or \"today\" timeframe you can ask for the hourly detail
    String onlyFavorites = "onlyFavorites_example"; // String | 
    try {
      ApiCoreDtoAggregatedAggregatedResult result = apiInstance.aggregatedGetStatisticsSingle(timeFrame, fromDay, toDay, hourly, onlyFavorites);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AggregatedApi#aggregatedGetStatisticsSingle");
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
| **timeFrame** | **String**| Timeframe of the request. See list at $timeframeList | [enum: today, yesterday, last7, last30, lastmonth, currentmonth, previousmonth, last90, last120, last180, last12months, lastyear, currentyear, beginning, custom] |
| **fromDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the starting day (YYYYMMDD) | [optional] |
| **toDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the ending day (YYYYMMDD) | [optional] |
| **hourly** | **Boolean**| If using \&quot;yesterday\&quot; or \&quot;today\&quot; timeframe you can ask for the hourly detail | [optional] |
| **onlyFavorites** | **String**|  | [optional] |

### Return type

[**ApiCoreDtoAggregatedAggregatedResult**](ApiCoreDtoAggregatedAggregatedResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |

