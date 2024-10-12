# GroupsApi

All URIs are relative to *http://apiv2.clickmeter.com:80*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**groupsCount**](GroupsApi.md#groupsCount) | **GET** /groups/count | Count the groups associated to the user. |
| [**groupsDelete**](GroupsApi.md#groupsDelete) | **DELETE** /groups/{id} | Delete group specified by id |
| [**groupsGet**](GroupsApi.md#groupsGet) | **GET** /groups | List of all the groups associated to the user. |
| [**groupsGetDatapoints**](GroupsApi.md#groupsGetDatapoints) | **GET** /groups/{id}/datapoints | List of all the datapoints associated to the user in this group. |
| [**groupsGetDatapointsCount**](GroupsApi.md#groupsGetDatapointsCount) | **GET** /groups/{id}/datapoints/count | Count the datapoints associated to the user in this group. |
| [**groupsGetDatapointsSummary**](GroupsApi.md#groupsGetDatapointsSummary) | **GET** /groups/{id}/aggregated/summary | Retrieve statistics about a subset of datapoints for a timeframe with datapoints data |
| [**groupsGetHits**](GroupsApi.md#groupsGetHits) | **GET** /groups/{id}/hits | Retrieve the list of events related to this group. |
| [**groupsGetStatisticsAggregatedSingle**](GroupsApi.md#groupsGetStatisticsAggregatedSingle) | **GET** /groups/aggregated | Retrieve statistics about this customer for a timeframe by groups |
| [**groupsGetStatisticsAllList**](GroupsApi.md#groupsGetStatisticsAllList) | **GET** /groups/aggregated/list | Retrieve statistics about all groups of this customer for a timeframe grouped by some temporal entity (day/week/month) |
| [**groupsGetStatisticsList**](GroupsApi.md#groupsGetStatisticsList) | **GET** /groups/{id}/aggregated/list | Retrieve statistics about this group for a timeframe grouped by some temporal entity (day/week/month) |
| [**groupsGetStatisticsSingle**](GroupsApi.md#groupsGetStatisticsSingle) | **GET** /groups/{id}/aggregated | Retrieve statistics about this group for a timeframe |
| [**groupsIdGet**](GroupsApi.md#groupsIdGet) | **GET** /groups/{id} | Get a group |
| [**groupsPatchFavourite**](GroupsApi.md#groupsPatchFavourite) | **PUT** /groups/{id}/favourite | Fast switch the \&quot;favourite\&quot; field of a group |
| [**groupsPatchNotes**](GroupsApi.md#groupsPatchNotes) | **PUT** /groups/{id}/notes | Fast patch the \&quot;notes\&quot; field of a group |
| [**groupsPost**](GroupsApi.md#groupsPost) | **POST** /groups/{id} | Update a group |
| [**groupsPut**](GroupsApi.md#groupsPut) | **POST** /groups | Create a group |
| [**groupsPutDatapoint**](GroupsApi.md#groupsPutDatapoint) | **POST** /groups/{id}/datapoints | Create a datapoint in this group |


<a id="groupsCount"></a>
# **groupsCount**
> ApiCoreResponsesCountResponce groupsCount(status, tags, textSearch, createdAfter, createdBefore, write)

Count the groups associated to the user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String status = "deleted"; // String | Status of the datapoint
    String tags = "tags_example"; // String | A comma separated list of tags you want to filter with.
    String textSearch = "textSearch_example"; // String | Filter fields by this pattern
    String createdAfter = "createdAfter_example"; // String | Exclude groups created before this date (YYYYMMDD)
    String createdBefore = "createdBefore_example"; // String | Exclude groups created after this date (YYYYMMDD)
    Boolean write = true; // Boolean | Write permission
    try {
      ApiCoreResponsesCountResponce result = apiInstance.groupsCount(status, tags, textSearch, createdAfter, createdBefore, write);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsCount");
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
| **status** | **String**| Status of the datapoint | [optional] [enum: deleted, active] |
| **tags** | **String**| A comma separated list of tags you want to filter with. | [optional] |
| **textSearch** | **String**| Filter fields by this pattern | [optional] |
| **createdAfter** | **String**| Exclude groups created before this date (YYYYMMDD) | [optional] |
| **createdBefore** | **String**| Exclude groups created after this date (YYYYMMDD) | [optional] |
| **write** | **Boolean**| Write permission | [optional] |

### Return type

[**ApiCoreResponsesCountResponce**](ApiCoreResponsesCountResponce.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="groupsDelete"></a>
# **groupsDelete**
> ApiCoreResponsesEntityUriSystemInt64 groupsDelete(id)

Delete group specified by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    Long id = 56L; // Long | Id of the group
    try {
      ApiCoreResponsesEntityUriSystemInt64 result = apiInstance.groupsDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsDelete");
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
| **id** | **Long**| Id of the group | |

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="groupsGet"></a>
# **groupsGet**
> ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64 groupsGet(offset, limit, status, tags, textSearch, createdAfter, createdBefore, write)

List of all the groups associated to the user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    Integer offset = 0; // Integer | Where to start when retrieving elements. Default is 0 if not specified.
    Integer limit = 20; // Integer | Maximum elements to retrieve. Default to 20 if not specified.
    String status = "deleted"; // String | Status of the group
    String tags = "tags_example"; // String | A comma separated list of tags you want to filter with.
    String textSearch = "textSearch_example"; // String | Filter fields by this pattern
    String createdAfter = "createdAfter_example"; // String | Exclude groups created before this date (YYYYMMDD)
    String createdBefore = "createdBefore_example"; // String | Exclude groups created after this date (YYYYMMDD)
    Boolean write = true; // Boolean | Write permission
    try {
      ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64 result = apiInstance.groupsGet(offset, limit, status, tags, textSearch, createdAfter, createdBefore, write);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsGet");
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
| **offset** | **Integer**| Where to start when retrieving elements. Default is 0 if not specified. | [optional] [default to 0] |
| **limit** | **Integer**| Maximum elements to retrieve. Default to 20 if not specified. | [optional] [default to 20] |
| **status** | **String**| Status of the group | [optional] [enum: deleted, active] |
| **tags** | **String**| A comma separated list of tags you want to filter with. | [optional] |
| **textSearch** | **String**| Filter fields by this pattern | [optional] |
| **createdAfter** | **String**| Exclude groups created before this date (YYYYMMDD) | [optional] |
| **createdBefore** | **String**| Exclude groups created after this date (YYYYMMDD) | [optional] |
| **write** | **Boolean**| Write permission | [optional] |

### Return type

[**ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64.md)

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
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="groupsGetDatapoints"></a>
# **groupsGetDatapoints**
> ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64 groupsGetDatapoints(id, offset, limit, type, status, tags, textSearch, onlyFavorites, sortBy, sortDirection, createdAfter, createdBefore)

List of all the datapoints associated to the user in this group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    Long id = 56L; // Long | Id of the group
    Integer offset = 0; // Integer | Where to start when retrieving elements. Default is 0 if not specified.
    Integer limit = 20; // Integer | Maximum elements to retrieve. Default to 20 if not specified.
    String type = "tp"; // String | Type of the datapoint (\"tp\"/\"tl\")
    String status = "deleted"; // String | Status of the datapoint
    String tags = "tags_example"; // String | A comma separated list of tags you want to filter with.
    String textSearch = "textSearch_example"; // String | Filter fields by this pattern
    Boolean onlyFavorites = true; // Boolean | Filter fields by favourite status
    String sortBy = "sortBy_example"; // String | Field to sort by
    String sortDirection = "asc"; // String | Direction of sort \"asc\" or \"desc\"
    String createdAfter = "createdAfter_example"; // String | Exclude datapoints created before this date (YYYYMMDD)
    String createdBefore = "createdBefore_example"; // String | Exclude datapoints created after this date (YYYYMMDD)
    try {
      ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64 result = apiInstance.groupsGetDatapoints(id, offset, limit, type, status, tags, textSearch, onlyFavorites, sortBy, sortDirection, createdAfter, createdBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsGetDatapoints");
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
| **id** | **Long**| Id of the group | |
| **offset** | **Integer**| Where to start when retrieving elements. Default is 0 if not specified. | [optional] [default to 0] |
| **limit** | **Integer**| Maximum elements to retrieve. Default to 20 if not specified. | [optional] [default to 20] |
| **type** | **String**| Type of the datapoint (\&quot;tp\&quot;/\&quot;tl\&quot;) | [optional] [enum: tp, tl] |
| **status** | **String**| Status of the datapoint | [optional] [enum: deleted, active, paused, spam] |
| **tags** | **String**| A comma separated list of tags you want to filter with. | [optional] |
| **textSearch** | **String**| Filter fields by this pattern | [optional] |
| **onlyFavorites** | **Boolean**| Filter fields by favourite status | [optional] |
| **sortBy** | **String**| Field to sort by | [optional] |
| **sortDirection** | **String**| Direction of sort \&quot;asc\&quot; or \&quot;desc\&quot; | [optional] [enum: asc, desc] |
| **createdAfter** | **String**| Exclude datapoints created before this date (YYYYMMDD) | [optional] |
| **createdBefore** | **String**| Exclude datapoints created after this date (YYYYMMDD) | [optional] |

### Return type

[**ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64.md)

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
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="groupsGetDatapointsCount"></a>
# **groupsGetDatapointsCount**
> ApiCoreResponsesCountResponce groupsGetDatapointsCount(id, type, status, tags, textSearch, onlyFavorites, createdAfter, createdBefore)

Count the datapoints associated to the user in this group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    Long id = 56L; // Long | Id of the group
    String type = "tp"; // String | Type of the datapoint (\"tp\"/\"tl\")
    String status = "deleted"; // String | Status of the datapoint
    String tags = "tags_example"; // String | A comma separated list of tags you want to filter with.
    String textSearch = "textSearch_example"; // String | Filter fields by this pattern
    Boolean onlyFavorites = true; // Boolean | Filter fields by favourite status
    String createdAfter = "createdAfter_example"; // String | Exclude datapoints created before this date (YYYYMMDD)
    String createdBefore = "createdBefore_example"; // String | Exclude datapoints created after this date (YYYYMMDD)
    try {
      ApiCoreResponsesCountResponce result = apiInstance.groupsGetDatapointsCount(id, type, status, tags, textSearch, onlyFavorites, createdAfter, createdBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsGetDatapointsCount");
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
| **id** | **Long**| Id of the group | |
| **type** | **String**| Type of the datapoint (\&quot;tp\&quot;/\&quot;tl\&quot;) | [optional] [enum: tp, tl] |
| **status** | **String**| Status of the datapoint | [optional] [enum: deleted, active, paused, spam] |
| **tags** | **String**| A comma separated list of tags you want to filter with. | [optional] |
| **textSearch** | **String**| Filter fields by this pattern | [optional] |
| **onlyFavorites** | **Boolean**| Filter fields by favourite status | [optional] |
| **createdAfter** | **String**| Exclude datapoints created before this date (YYYYMMDD) | [optional] |
| **createdBefore** | **String**| Exclude datapoints created after this date (YYYYMMDD) | [optional] |

### Return type

[**ApiCoreResponsesCountResponce**](ApiCoreResponsesCountResponce.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="groupsGetDatapointsSummary"></a>
# **groupsGetDatapointsSummary**
> ApiCoreDtoAggregatedAggregatedSummaryResult groupsGetDatapointsSummary(id, timeFrame, type, fromDay, toDay, status, tag, favourite, sortBy, sortDirection, offset, limit, textSearch)

Retrieve statistics about a subset of datapoints for a timeframe with datapoints data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    Long id = 56L; // Long | Filter by this group id
    String timeFrame = "today"; // String | Timeframe of the request. See list at $timeframeList
    String type = "tp"; // String | Type of datapoint (\"tl\"/\"tp\")
    String fromDay = "fromDay_example"; // String | If using a \"custom\" timeFrame you can specify the starting day (YYYYMMDD)
    String toDay = "toDay_example"; // String | If using a \"custom\" timeFrame you can specify the ending day (YYYYMMDD)
    String status = "deleted"; // String | Status of datapoint (\"deleted\"/\"active\"/\"paused\"/\"spam\")
    String tag = "tag_example"; // String | A comma separated list of tags you want to filter with.
    Boolean favourite = true; // Boolean | Is the datapoint marked as favourite
    String sortBy = "sortBy_example"; // String | Field to sort by
    String sortDirection = "asc"; // String | Direction of sort \"asc\" or \"desc\"
    Integer offset = 0; // Integer | Offset where to start from
    Integer limit = 20; // Integer | Limit results to this number
    String textSearch = "textSearch_example"; // String | Filter fields by this pattern
    try {
      ApiCoreDtoAggregatedAggregatedSummaryResult result = apiInstance.groupsGetDatapointsSummary(id, timeFrame, type, fromDay, toDay, status, tag, favourite, sortBy, sortDirection, offset, limit, textSearch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsGetDatapointsSummary");
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
| **id** | **Long**| Filter by this group id | |
| **timeFrame** | **String**| Timeframe of the request. See list at $timeframeList | [enum: today, yesterday, last7, last30, lastmonth, currentmonth, previousmonth, last90, last120, last180, last12months, lastyear, currentyear, beginning, custom] |
| **type** | **String**| Type of datapoint (\&quot;tl\&quot;/\&quot;tp\&quot;) | [optional] [enum: tp, tl] |
| **fromDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the starting day (YYYYMMDD) | [optional] |
| **toDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the ending day (YYYYMMDD) | [optional] |
| **status** | **String**| Status of datapoint (\&quot;deleted\&quot;/\&quot;active\&quot;/\&quot;paused\&quot;/\&quot;spam\&quot;) | [optional] [enum: deleted, active] |
| **tag** | **String**| A comma separated list of tags you want to filter with. | [optional] |
| **favourite** | **Boolean**| Is the datapoint marked as favourite | [optional] |
| **sortBy** | **String**| Field to sort by | [optional] |
| **sortDirection** | **String**| Direction of sort \&quot;asc\&quot; or \&quot;desc\&quot; | [optional] [enum: asc, desc] |
| **offset** | **Integer**| Offset where to start from | [optional] [default to 0] |
| **limit** | **Integer**| Limit results to this number | [optional] [default to 20] |
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

<a id="groupsGetHits"></a>
# **groupsGetHits**
> ApiCoreDtoClickStreamHitListPage groupsGetHits(id, timeframe, limit, offset, fromDay, toDay, filter)

Retrieve the list of events related to this group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    Long id = 56L; // Long | Id of the group
    String timeframe = "yesterday"; // String | Timeframe of the request. See list at $timeframeList
    Integer limit = 56; // Integer | Limit results to this number
    String offset = "offset_example"; // String | Offset where to start from (it's the lastKey field in the response object)
    String fromDay = "fromDay_example"; // String | If using a \"custom\" timeFrame you can specify the starting day (YYYYMMDD)
    String toDay = "toDay_example"; // String | If using a \"custom\" timeFrame you can specify the ending day (YYYYMMDD)
    String filter = "spiders"; // String | Filter event type (\"spiders\"/\"uniques\"/\"nonuniques\"/\"conversions\")
    try {
      ApiCoreDtoClickStreamHitListPage result = apiInstance.groupsGetHits(id, timeframe, limit, offset, fromDay, toDay, filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsGetHits");
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
| **id** | **Long**| Id of the group | |
| **timeframe** | **String**| Timeframe of the request. See list at $timeframeList | [enum: yesterday, last7, last30, lastmonth, currentmonth, previousmonth, last90, last120, last180, custom] |
| **limit** | **Integer**| Limit results to this number | [optional] |
| **offset** | **String**| Offset where to start from (it&#39;s the lastKey field in the response object) | [optional] |
| **fromDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the starting day (YYYYMMDD) | [optional] |
| **toDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the ending day (YYYYMMDD) | [optional] |
| **filter** | **String**| Filter event type (\&quot;spiders\&quot;/\&quot;uniques\&quot;/\&quot;nonuniques\&quot;/\&quot;conversions\&quot;) | [optional] [enum: spiders, uniques, nonuniques, conversions] |

### Return type

[**ApiCoreDtoClickStreamHitListPage**](ApiCoreDtoClickStreamHitListPage.md)

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

<a id="groupsGetStatisticsAggregatedSingle"></a>
# **groupsGetStatisticsAggregatedSingle**
> ApiCoreDtoAggregatedAggregatedResult groupsGetStatisticsAggregatedSingle(timeFrame, fromDay, toDay, hourly, status, tag, favourite)

Retrieve statistics about this customer for a timeframe by groups

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String timeFrame = "today"; // String | Timeframe of the request. See list at $timeframeList
    String fromDay = "fromDay_example"; // String | If using a \"custom\" timeFrame you can specify the starting day (YYYYMMDD)
    String toDay = "toDay_example"; // String | If using a \"custom\" timeFrame you can specify the ending day (YYYYMMDD)
    Boolean hourly = true; // Boolean | If using \"yesterday\" or \"today\" timeframe you can ask for the hourly detail
    String status = "deleted"; // String | Status of group (\"deleted\"/\"active\")
    String tag = "tag_example"; // String | A comma separated list of tags you want to filter with.
    Boolean favourite = true; // Boolean | Is the group is marked as favourite
    try {
      ApiCoreDtoAggregatedAggregatedResult result = apiInstance.groupsGetStatisticsAggregatedSingle(timeFrame, fromDay, toDay, hourly, status, tag, favourite);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsGetStatisticsAggregatedSingle");
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
| **status** | **String**| Status of group (\&quot;deleted\&quot;/\&quot;active\&quot;) | [optional] [enum: deleted, active] |
| **tag** | **String**| A comma separated list of tags you want to filter with. | [optional] |
| **favourite** | **Boolean**| Is the group is marked as favourite | [optional] |

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

<a id="groupsGetStatisticsAllList"></a>
# **groupsGetStatisticsAllList**
> ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult groupsGetStatisticsAllList(timeFrame, fromDay, toDay, status, tag, favourite, groupBy)

Retrieve statistics about all groups of this customer for a timeframe grouped by some temporal entity (day/week/month)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String timeFrame = "today"; // String | Timeframe of the request. See list at $timeframeList
    String fromDay = "fromDay_example"; // String | If using a \"custom\" timeFrame you can specify the starting day (YYYYMMDD)
    String toDay = "toDay_example"; // String | If using a \"custom\" timeFrame you can specify the ending day (YYYYMMDD)
    String status = "status_example"; // String | Status of group (\"deleted\"/\"active\")
    String tag = "tag_example"; // String | A comma separated list of tags you want to filter with.
    Boolean favourite = true; // Boolean | Is the group is marked as favourite
    String groupBy = "deleted"; // String | The temporal entity you want to group by (\"week\"/\"month\"). If unspecified is \"day\".
    try {
      ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult result = apiInstance.groupsGetStatisticsAllList(timeFrame, fromDay, toDay, status, tag, favourite, groupBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsGetStatisticsAllList");
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
| **status** | **String**| Status of group (\&quot;deleted\&quot;/\&quot;active\&quot;) | [optional] |
| **tag** | **String**| A comma separated list of tags you want to filter with. | [optional] |
| **favourite** | **Boolean**| Is the group is marked as favourite | [optional] |
| **groupBy** | **String**| The temporal entity you want to group by (\&quot;week\&quot;/\&quot;month\&quot;). If unspecified is \&quot;day\&quot;. | [optional] [enum: deleted, active] |

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

<a id="groupsGetStatisticsList"></a>
# **groupsGetStatisticsList**
> ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult groupsGetStatisticsList(id, timeFrame, fromDay, toDay, groupBy)

Retrieve statistics about this group for a timeframe grouped by some temporal entity (day/week/month)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    Long id = 56L; // Long | Id of the group
    String timeFrame = "today"; // String | Timeframe of the request. See list at $timeframeList
    String fromDay = "fromDay_example"; // String | If using a \"custom\" timeFrame you can specify the starting day (YYYYMMDD)
    String toDay = "toDay_example"; // String | If using a \"custom\" timeFrame you can specify the ending day (YYYYMMDD)
    String groupBy = "week"; // String | The temporal entity you want to group by (\"week\"/\"month\"). If unspecified is \"day\".
    try {
      ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult result = apiInstance.groupsGetStatisticsList(id, timeFrame, fromDay, toDay, groupBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsGetStatisticsList");
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
| **id** | **Long**| Id of the group | |
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

<a id="groupsGetStatisticsSingle"></a>
# **groupsGetStatisticsSingle**
> ApiCoreDtoAggregatedAggregatedResult groupsGetStatisticsSingle(id, timeFrame, fromDay, toDay, hourly)

Retrieve statistics about this group for a timeframe

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    Long id = 56L; // Long | Id of the group
    String timeFrame = "today"; // String | Timeframe of the request. See list at $timeframeList
    String fromDay = "fromDay_example"; // String | If using a \"custom\" timeFrame you can specify the starting day (YYYYMMDD)
    String toDay = "toDay_example"; // String | If using a \"custom\" timeFrame you can specify the ending day (YYYYMMDD)
    Boolean hourly = true; // Boolean | If using \"yesterday\" or \"today\" timeframe you can ask for the hourly detail
    try {
      ApiCoreDtoAggregatedAggregatedResult result = apiInstance.groupsGetStatisticsSingle(id, timeFrame, fromDay, toDay, hourly);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsGetStatisticsSingle");
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
| **id** | **Long**| Id of the group | |
| **timeFrame** | **String**| Timeframe of the request. See list at $timeframeList | [enum: today, yesterday, last7, last30, lastmonth, currentmonth, previousmonth, last90, last120, last180, last12months, lastyear, currentyear, beginning, custom] |
| **fromDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the starting day (YYYYMMDD) | [optional] |
| **toDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the ending day (YYYYMMDD) | [optional] |
| **hourly** | **Boolean**| If using \&quot;yesterday\&quot; or \&quot;today\&quot; timeframe you can ask for the hourly detail | [optional] |

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

<a id="groupsIdGet"></a>
# **groupsIdGet**
> ApiCoreDtoGroupsGroup groupsIdGet(id)

Get a group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    Long id = 56L; // Long | The id of the group
    try {
      ApiCoreDtoGroupsGroup result = apiInstance.groupsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsIdGet");
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
| **id** | **Long**| The id of the group | |

### Return type

[**ApiCoreDtoGroupsGroup**](ApiCoreDtoGroupsGroup.md)

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
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="groupsPatchFavourite"></a>
# **groupsPatchFavourite**
> ApiCoreResponsesEntityUriSystemInt64 groupsPatchFavourite(id)

Fast switch the \&quot;favourite\&quot; field of a group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    Long id = 56L; // Long | Id of the group
    try {
      ApiCoreResponsesEntityUriSystemInt64 result = apiInstance.groupsPatchFavourite(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsPatchFavourite");
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
| **id** | **Long**| Id of the group | |

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="groupsPatchNotes"></a>
# **groupsPatchNotes**
> ApiCoreResponsesEntityUriSystemInt64 groupsPatchNotes(id, apiCoreRequestsGenericTextPatch)

Fast patch the \&quot;notes\&quot; field of a group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    Long id = 56L; // Long | Id of the group
    ApiCoreRequestsGenericTextPatch apiCoreRequestsGenericTextPatch = new ApiCoreRequestsGenericTextPatch(); // ApiCoreRequestsGenericTextPatch | Patch requests
    try {
      ApiCoreResponsesEntityUriSystemInt64 result = apiInstance.groupsPatchNotes(id, apiCoreRequestsGenericTextPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsPatchNotes");
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
| **id** | **Long**| Id of the group | |
| **apiCoreRequestsGenericTextPatch** | [**ApiCoreRequestsGenericTextPatch**](ApiCoreRequestsGenericTextPatch.md)| Patch requests | |

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="groupsPost"></a>
# **groupsPost**
> ApiCoreResponsesEntityUriSystemInt64 groupsPost(id, apiCoreDtoGroupsGroup)

Update a group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    Long id = 56L; // Long | The id of the group
    ApiCoreDtoGroupsGroup apiCoreDtoGroupsGroup = new ApiCoreDtoGroupsGroup(); // ApiCoreDtoGroupsGroup | The body of the group
    try {
      ApiCoreResponsesEntityUriSystemInt64 result = apiInstance.groupsPost(id, apiCoreDtoGroupsGroup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsPost");
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
| **id** | **Long**| The id of the group | |
| **apiCoreDtoGroupsGroup** | [**ApiCoreDtoGroupsGroup**](ApiCoreDtoGroupsGroup.md)| The body of the group | |

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, text/json
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="groupsPut"></a>
# **groupsPut**
> ApiCoreResponsesEntityUriSystemInt64 groupsPut(apiCoreDtoGroupsGroup)

Create a group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    ApiCoreDtoGroupsGroup apiCoreDtoGroupsGroup = new ApiCoreDtoGroupsGroup(); // ApiCoreDtoGroupsGroup | The body of the group
    try {
      ApiCoreResponsesEntityUriSystemInt64 result = apiInstance.groupsPut(apiCoreDtoGroupsGroup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsPut");
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
| **apiCoreDtoGroupsGroup** | [**ApiCoreDtoGroupsGroup**](ApiCoreDtoGroupsGroup.md)| The body of the group | |

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, text/json
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="groupsPutDatapoint"></a>
# **groupsPutDatapoint**
> ApiCoreResponsesEntityUriSystemInt64 groupsPutDatapoint(id, apiCoreDtoDatapointsDatapoint)

Create a datapoint in this group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    Long id = 56L; // Long | The id of the group
    ApiCoreDtoDatapointsDatapoint apiCoreDtoDatapointsDatapoint = new ApiCoreDtoDatapointsDatapoint(); // ApiCoreDtoDatapointsDatapoint | The body of the datapoint
    try {
      ApiCoreResponsesEntityUriSystemInt64 result = apiInstance.groupsPutDatapoint(id, apiCoreDtoDatapointsDatapoint);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsPutDatapoint");
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
| **id** | **Long**| The id of the group | |
| **apiCoreDtoDatapointsDatapoint** | [**ApiCoreDtoDatapointsDatapoint**](ApiCoreDtoDatapointsDatapoint.md)| The body of the datapoint | |

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, text/json
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

