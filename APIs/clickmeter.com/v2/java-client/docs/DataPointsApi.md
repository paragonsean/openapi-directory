# DataPointsApi

All URIs are relative to *http://apiv2.clickmeter.com:80*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dataPointsBatchDelete**](DataPointsApi.md#dataPointsBatchDelete) | **DELETE** /datapoints/batch | Delete multiple datapoints |
| [**dataPointsBatchPost**](DataPointsApi.md#dataPointsBatchPost) | **POST** /datapoints/batch | Update multiple datapoints |
| [**dataPointsBatchPut**](DataPointsApi.md#dataPointsBatchPut) | **PUT** /datapoints/batch | Create multiple datapoints |
| [**dataPointsCount**](DataPointsApi.md#dataPointsCount) | **GET** /datapoints/count | Count the datapoints associated to the user |
| [**dataPointsDelete**](DataPointsApi.md#dataPointsDelete) | **DELETE** /datapoints/{id} | Delete a datapoint |
| [**dataPointsGet**](DataPointsApi.md#dataPointsGet) | **GET** /datapoints | List of all the datapoints associated to the user |
| [**dataPointsGetHits**](DataPointsApi.md#dataPointsGetHits) | **GET** /datapoints/{id}/hits | Retrieve the list of events related to this datapoint. |
| [**dataPointsGetStatisticsAggregatedSingle**](DataPointsApi.md#dataPointsGetStatisticsAggregatedSingle) | **GET** /datapoints/aggregated | Retrieve statistics about this customer for a timeframe by groups |
| [**dataPointsGetStatisticsAllList**](DataPointsApi.md#dataPointsGetStatisticsAllList) | **GET** /datapoints/aggregated/list | Retrieve statistics about all datapoints of this customer for a timeframe grouped by some temporal entity (day/week/month) |
| [**dataPointsGetStatisticsList**](DataPointsApi.md#dataPointsGetStatisticsList) | **GET** /datapoints/{id}/aggregated/list | Retrieve statistics about this datapoint for a timeframe grouped by some temporal entity (day/week/month) |
| [**dataPointsGetStatisticsSingle**](DataPointsApi.md#dataPointsGetStatisticsSingle) | **GET** /datapoints/{id}/aggregated | Retrieve statistics about this datapoint for a timeframe |
| [**dataPointsPatchFavourite**](DataPointsApi.md#dataPointsPatchFavourite) | **PUT** /datapoints/{id}/favourite | Fast switch the \&quot;favourite\&quot; field of a datapoint |
| [**dataPointsPatchNotes**](DataPointsApi.md#dataPointsPatchNotes) | **PUT** /datapoints/{id}/notes | Fast patch the \&quot;notes\&quot; field of a datapoint |
| [**dataPointsPost**](DataPointsApi.md#dataPointsPost) | **POST** /datapoints/{id} | Update a datapoint |
| [**dataPointsPut**](DataPointsApi.md#dataPointsPut) | **POST** /datapoints | Create a datapoint |
| [**datapointsIdGet**](DataPointsApi.md#datapointsIdGet) | **GET** /datapoints/{id} | Get a datapoint |


<a id="dataPointsBatchDelete"></a>
# **dataPointsBatchDelete**
> ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64 dataPointsBatchDelete(apiCoreRequestsDeleteBatch)

Delete multiple datapoints

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataPointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DataPointsApi apiInstance = new DataPointsApi(defaultClient);
    ApiCoreRequestsDeleteBatch apiCoreRequestsDeleteBatch = new ApiCoreRequestsDeleteBatch(); // ApiCoreRequestsDeleteBatch | A json containing the datapoints to delete.
    try {
      ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64 result = apiInstance.dataPointsBatchDelete(apiCoreRequestsDeleteBatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataPointsApi#dataPointsBatchDelete");
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
| **apiCoreRequestsDeleteBatch** | [**ApiCoreRequestsDeleteBatch**](ApiCoreRequestsDeleteBatch.md)| A json containing the datapoints to delete. | |

### Return type

[**ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64**](ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="dataPointsBatchPost"></a>
# **dataPointsBatchPost**
> ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64 dataPointsBatchPost(apiCoreRequestsDatapointsBatch)

Update multiple datapoints

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataPointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DataPointsApi apiInstance = new DataPointsApi(defaultClient);
    ApiCoreRequestsDatapointsBatch apiCoreRequestsDatapointsBatch = new ApiCoreRequestsDatapointsBatch(); // ApiCoreRequestsDatapointsBatch | A json containing the datapoints to update.
    try {
      ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64 result = apiInstance.dataPointsBatchPost(apiCoreRequestsDatapointsBatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataPointsApi#dataPointsBatchPost");
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
| **apiCoreRequestsDatapointsBatch** | [**ApiCoreRequestsDatapointsBatch**](ApiCoreRequestsDatapointsBatch.md)| A json containing the datapoints to update. | |

### Return type

[**ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64**](ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="dataPointsBatchPut"></a>
# **dataPointsBatchPut**
> ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64 dataPointsBatchPut(apiCoreRequestsDatapointsBatch)

Create multiple datapoints

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataPointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DataPointsApi apiInstance = new DataPointsApi(defaultClient);
    ApiCoreRequestsDatapointsBatch apiCoreRequestsDatapointsBatch = new ApiCoreRequestsDatapointsBatch(); // ApiCoreRequestsDatapointsBatch | A json containing the datapoints to create.
    try {
      ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64 result = apiInstance.dataPointsBatchPut(apiCoreRequestsDatapointsBatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataPointsApi#dataPointsBatchPut");
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
| **apiCoreRequestsDatapointsBatch** | [**ApiCoreRequestsDatapointsBatch**](ApiCoreRequestsDatapointsBatch.md)| A json containing the datapoints to create. | |

### Return type

[**ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64**](ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="dataPointsCount"></a>
# **dataPointsCount**
> ApiCoreResponsesCountResponce dataPointsCount(type, status, tags, textSearch, onlyFavorites, createdAfter, createdBefore)

Count the datapoints associated to the user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataPointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DataPointsApi apiInstance = new DataPointsApi(defaultClient);
    String type = "tp"; // String | Type of the datapoint (\"tp\"/\"tl\")
    String status = "deleted"; // String | Status of the datapoint
    String tags = "tags_example"; // String | A comma separated list of tags you want to filter with.
    String textSearch = "textSearch_example"; // String | Filter fields by this pattern
    Boolean onlyFavorites = true; // Boolean | Filter fields by favourite status
    String createdAfter = "createdAfter_example"; // String | Exclude datapoints created before this date (YYYYMMDD)
    String createdBefore = "createdBefore_example"; // String | Exclude datapoints created after this date (YYYYMMDD)
    try {
      ApiCoreResponsesCountResponce result = apiInstance.dataPointsCount(type, status, tags, textSearch, onlyFavorites, createdAfter, createdBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataPointsApi#dataPointsCount");
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

<a id="dataPointsDelete"></a>
# **dataPointsDelete**
> ApiCoreResponsesEntityUriSystemInt64 dataPointsDelete(id)

Delete a datapoint

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataPointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DataPointsApi apiInstance = new DataPointsApi(defaultClient);
    Long id = 56L; // Long | The id of the datapoint
    try {
      ApiCoreResponsesEntityUriSystemInt64 result = apiInstance.dataPointsDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataPointsApi#dataPointsDelete");
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
| **id** | **Long**| The id of the datapoint | |

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

<a id="dataPointsGet"></a>
# **dataPointsGet**
> ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64 dataPointsGet(offset, limit, type, status, tags, textSearch, onlyFavorites, sortBy, sortDirection, createdAfter, createdBefore)

List of all the datapoints associated to the user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataPointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DataPointsApi apiInstance = new DataPointsApi(defaultClient);
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
      ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64 result = apiInstance.dataPointsGet(offset, limit, type, status, tags, textSearch, onlyFavorites, sortBy, sortDirection, createdAfter, createdBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataPointsApi#dataPointsGet");
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

<a id="dataPointsGetHits"></a>
# **dataPointsGetHits**
> ApiCoreDtoClickStreamHitListPage dataPointsGetHits(id, timeframe, limit, offset, fromDay, toDay, filter)

Retrieve the list of events related to this datapoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataPointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DataPointsApi apiInstance = new DataPointsApi(defaultClient);
    Long id = 56L; // Long | Id of the datapoint
    String timeframe = "yesterday"; // String | Timeframe of the request. See list at $timeframeList
    Integer limit = 56; // Integer | Limit results to this number
    String offset = "offset_example"; // String | Offset where to start from (it's the lastKey field in the response object)
    String fromDay = "fromDay_example"; // String | If using a \"custom\" timeFrame you can specify the starting day (YYYYMMDD)
    String toDay = "toDay_example"; // String | If using a \"custom\" timeFrame you can specify the ending day (YYYYMMDD)
    String filter = "spiders"; // String | Filter event type (\"spiders\"/\"uniques\"/\"nonuniques\"/\"conversions\")
    try {
      ApiCoreDtoClickStreamHitListPage result = apiInstance.dataPointsGetHits(id, timeframe, limit, offset, fromDay, toDay, filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataPointsApi#dataPointsGetHits");
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
| **id** | **Long**| Id of the datapoint | |
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

<a id="dataPointsGetStatisticsAggregatedSingle"></a>
# **dataPointsGetStatisticsAggregatedSingle**
> ApiCoreDtoAggregatedAggregatedResult dataPointsGetStatisticsAggregatedSingle(timeFrame, type, fromDay, toDay, hourly, status, tag, favourite)

Retrieve statistics about this customer for a timeframe by groups

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataPointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DataPointsApi apiInstance = new DataPointsApi(defaultClient);
    String timeFrame = "today"; // String | Timeframe of the request. See list at $timeframeList
    String type = "tp"; // String | Type of datapoint (\"tl\"/\"tp\")
    String fromDay = "fromDay_example"; // String | If using a \"custom\" timeFrame you can specify the starting day (YYYYMMDD)
    String toDay = "toDay_example"; // String | If using a \"custom\" timeFrame you can specify the ending day (YYYYMMDD)
    Boolean hourly = true; // Boolean | If using \"yesterday\" or \"today\" timeframe you can ask for the hourly detail
    String status = "deleted"; // String | Status of datapoint (\"deleted\"/\"active\"/\"paused\"/\"spam\")
    String tag = "tag_example"; // String | A comma separated list of tags you want to filter with.
    Boolean favourite = true; // Boolean | Is the datapoint is marked as favourite
    try {
      ApiCoreDtoAggregatedAggregatedResult result = apiInstance.dataPointsGetStatisticsAggregatedSingle(timeFrame, type, fromDay, toDay, hourly, status, tag, favourite);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataPointsApi#dataPointsGetStatisticsAggregatedSingle");
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
| **type** | **String**| Type of datapoint (\&quot;tl\&quot;/\&quot;tp\&quot;) | [optional] [enum: tp, tl] |
| **fromDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the starting day (YYYYMMDD) | [optional] |
| **toDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the ending day (YYYYMMDD) | [optional] |
| **hourly** | **Boolean**| If using \&quot;yesterday\&quot; or \&quot;today\&quot; timeframe you can ask for the hourly detail | [optional] |
| **status** | **String**| Status of datapoint (\&quot;deleted\&quot;/\&quot;active\&quot;/\&quot;paused\&quot;/\&quot;spam\&quot;) | [optional] [enum: deleted, active, paused, spam] |
| **tag** | **String**| A comma separated list of tags you want to filter with. | [optional] |
| **favourite** | **Boolean**| Is the datapoint is marked as favourite | [optional] |

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

<a id="dataPointsGetStatisticsAllList"></a>
# **dataPointsGetStatisticsAllList**
> ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult dataPointsGetStatisticsAllList(type, timeFrame, fromDay, toDay, status, tag, favourite, groupBy)

Retrieve statistics about all datapoints of this customer for a timeframe grouped by some temporal entity (day/week/month)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataPointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DataPointsApi apiInstance = new DataPointsApi(defaultClient);
    String type = "tp"; // String | Type of datapoint (\"tl\"/\"tp\")
    String timeFrame = "today"; // String | Timeframe of the request. See list at $timeframeList
    String fromDay = "fromDay_example"; // String | If using a \"custom\" timeFrame you can specify the starting day (YYYYMMDD)
    String toDay = "toDay_example"; // String | If using a \"custom\" timeFrame you can specify the ending day (YYYYMMDD)
    String status = "deleted"; // String | Status of datapoint (\"deleted\"/\"active\"/\"paused\"/\"spam\")
    String tag = "tag_example"; // String | A comma separated list of tags you want to filter with.
    Boolean favourite = true; // Boolean | Is the datapoint is marked as favourite
    String groupBy = "week"; // String | The temporal entity you want to group by (\"week\"/\"month\"). If unspecified is \"day\".
    try {
      ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult result = apiInstance.dataPointsGetStatisticsAllList(type, timeFrame, fromDay, toDay, status, tag, favourite, groupBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataPointsApi#dataPointsGetStatisticsAllList");
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
| **type** | **String**| Type of datapoint (\&quot;tl\&quot;/\&quot;tp\&quot;) | [enum: tp, tl] |
| **timeFrame** | **String**| Timeframe of the request. See list at $timeframeList | [enum: today, yesterday, last7, last30, lastmonth, currentmonth, previousmonth, last90, last120, last180, last12months, lastyear, currentyear, beginning, custom] |
| **fromDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the starting day (YYYYMMDD) | [optional] |
| **toDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the ending day (YYYYMMDD) | [optional] |
| **status** | **String**| Status of datapoint (\&quot;deleted\&quot;/\&quot;active\&quot;/\&quot;paused\&quot;/\&quot;spam\&quot;) | [optional] [enum: deleted, active, paused, spam] |
| **tag** | **String**| A comma separated list of tags you want to filter with. | [optional] |
| **favourite** | **Boolean**| Is the datapoint is marked as favourite | [optional] |
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

<a id="dataPointsGetStatisticsList"></a>
# **dataPointsGetStatisticsList**
> ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult dataPointsGetStatisticsList(id, timeFrame, fromDay, toDay, groupBy)

Retrieve statistics about this datapoint for a timeframe grouped by some temporal entity (day/week/month)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataPointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DataPointsApi apiInstance = new DataPointsApi(defaultClient);
    Long id = 56L; // Long | Id of the datapoint
    String timeFrame = "today"; // String | Timeframe of the request. See list at $timeframeList
    String fromDay = "fromDay_example"; // String | If using a \"custom\" timeFrame you can specify the starting day (YYYYMMDD)
    String toDay = "toDay_example"; // String | If using a \"custom\" timeFrame you can specify the ending day (YYYYMMDD)
    String groupBy = "week"; // String | The temporal entity you want to group by (\"week\"/\"month\"). If unspecified is \"day\".
    try {
      ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult result = apiInstance.dataPointsGetStatisticsList(id, timeFrame, fromDay, toDay, groupBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataPointsApi#dataPointsGetStatisticsList");
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
| **id** | **Long**| Id of the datapoint | |
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

<a id="dataPointsGetStatisticsSingle"></a>
# **dataPointsGetStatisticsSingle**
> ApiCoreDtoAggregatedAggregatedResult dataPointsGetStatisticsSingle(id, timeFrame, fromDay, toDay, hourly)

Retrieve statistics about this datapoint for a timeframe

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataPointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DataPointsApi apiInstance = new DataPointsApi(defaultClient);
    Long id = 56L; // Long | Id of the datapoint
    String timeFrame = "today"; // String | Timeframe of the request. See list at $timeframeList
    String fromDay = "fromDay_example"; // String | If using a \"custom\" timeFrame you can specify the starting day (YYYYMMDD)
    String toDay = "toDay_example"; // String | If using a \"custom\" timeFrame you can specify the ending day (YYYYMMDD)
    Boolean hourly = true; // Boolean | If using \"yesterday\" or \"today\" timeframe you can ask for the hourly detail
    try {
      ApiCoreDtoAggregatedAggregatedResult result = apiInstance.dataPointsGetStatisticsSingle(id, timeFrame, fromDay, toDay, hourly);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataPointsApi#dataPointsGetStatisticsSingle");
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
| **id** | **Long**| Id of the datapoint | |
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

<a id="dataPointsPatchFavourite"></a>
# **dataPointsPatchFavourite**
> ApiCoreResponsesEntityUriSystemInt64 dataPointsPatchFavourite(id)

Fast switch the \&quot;favourite\&quot; field of a datapoint

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataPointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DataPointsApi apiInstance = new DataPointsApi(defaultClient);
    Long id = 56L; // Long | Id of the datapoint
    try {
      ApiCoreResponsesEntityUriSystemInt64 result = apiInstance.dataPointsPatchFavourite(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataPointsApi#dataPointsPatchFavourite");
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
| **id** | **Long**| Id of the datapoint | |

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

<a id="dataPointsPatchNotes"></a>
# **dataPointsPatchNotes**
> ApiCoreResponsesEntityUriSystemInt64 dataPointsPatchNotes(id, apiCoreRequestsGenericTextPatch)

Fast patch the \&quot;notes\&quot; field of a datapoint

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataPointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DataPointsApi apiInstance = new DataPointsApi(defaultClient);
    Long id = 56L; // Long | Id of the datapoint
    ApiCoreRequestsGenericTextPatch apiCoreRequestsGenericTextPatch = new ApiCoreRequestsGenericTextPatch(); // ApiCoreRequestsGenericTextPatch | Patch requests
    try {
      ApiCoreResponsesEntityUriSystemInt64 result = apiInstance.dataPointsPatchNotes(id, apiCoreRequestsGenericTextPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataPointsApi#dataPointsPatchNotes");
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
| **id** | **Long**| Id of the datapoint | |
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

<a id="dataPointsPost"></a>
# **dataPointsPost**
> ApiCoreResponsesEntityUriSystemInt64 dataPointsPost(id, apiCoreDtoDatapointsDatapoint)

Update a datapoint

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataPointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DataPointsApi apiInstance = new DataPointsApi(defaultClient);
    Long id = 56L; // Long | The id of the datapoint
    ApiCoreDtoDatapointsDatapoint apiCoreDtoDatapointsDatapoint = new ApiCoreDtoDatapointsDatapoint(); // ApiCoreDtoDatapointsDatapoint | The body of the datapoint
    try {
      ApiCoreResponsesEntityUriSystemInt64 result = apiInstance.dataPointsPost(id, apiCoreDtoDatapointsDatapoint);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataPointsApi#dataPointsPost");
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
| **id** | **Long**| The id of the datapoint | |
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

<a id="dataPointsPut"></a>
# **dataPointsPut**
> ApiCoreResponsesEntityUriSystemInt64 dataPointsPut(apiCoreDtoDatapointsDatapoint)

Create a datapoint

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataPointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DataPointsApi apiInstance = new DataPointsApi(defaultClient);
    ApiCoreDtoDatapointsDatapoint apiCoreDtoDatapointsDatapoint = new ApiCoreDtoDatapointsDatapoint(); // ApiCoreDtoDatapointsDatapoint | The body of the datapoint
    try {
      ApiCoreResponsesEntityUriSystemInt64 result = apiInstance.dataPointsPut(apiCoreDtoDatapointsDatapoint);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataPointsApi#dataPointsPut");
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

<a id="datapointsIdGet"></a>
# **datapointsIdGet**
> ApiCoreDtoDatapointsDatapoint datapointsIdGet(id)

Get a datapoint

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataPointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DataPointsApi apiInstance = new DataPointsApi(defaultClient);
    Long id = 56L; // Long | The id of the datapoint
    try {
      ApiCoreDtoDatapointsDatapoint result = apiInstance.datapointsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataPointsApi#datapointsIdGet");
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
| **id** | **Long**| The id of the datapoint | |

### Return type

[**ApiCoreDtoDatapointsDatapoint**](ApiCoreDtoDatapointsDatapoint.md)

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

