# ConversionsApi

All URIs are relative to *http://apiv2.clickmeter.com:80*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**conversionsConversionIdDatapointsBatchPatchPut**](ConversionsApi.md#conversionsConversionIdDatapointsBatchPatchPut) | **PUT** /conversions/{conversionId}/datapoints/batch/patch | Modify the association between a conversion and multiple datapoints |
| [**conversionsConversionIdGet**](ConversionsApi.md#conversionsConversionIdGet) | **GET** /conversions/{conversionId} | Retrieve conversion specified by id |
| [**conversionsCount**](ConversionsApi.md#conversionsCount) | **GET** /conversions/count | Retrieve a count of conversions |
| [**conversionsDelete**](ConversionsApi.md#conversionsDelete) | **DELETE** /conversions/{conversionId} | Delete conversion specified by id |
| [**conversionsGet**](ConversionsApi.md#conversionsGet) | **GET** /conversions | Retrieve a list of conversions |
| [**conversionsGetDatapoints**](ConversionsApi.md#conversionsGetDatapoints) | **GET** /conversions/{conversionId}/datapoints | Retrieve a list of datapoints connected to this conversion |
| [**conversionsGetDatapointsCount**](ConversionsApi.md#conversionsGetDatapointsCount) | **GET** /conversions/{conversionId}/datapoints/count | Retrieve a count of datapoints connected to this conversion |
| [**conversionsGetHits**](ConversionsApi.md#conversionsGetHits) | **GET** /conversions/{conversionId}/hits | Retrieve the list of events related to this conversion. |
| [**conversionsGetStatisticsAllList**](ConversionsApi.md#conversionsGetStatisticsAllList) | **GET** /conversions/aggregated/list | Retrieve statistics about this customer for a timeframe related to a subset of conversions grouped by some temporal entity (day/week/month) |
| [**conversionsGetStatisticsList**](ConversionsApi.md#conversionsGetStatisticsList) | **GET** /conversions/{conversionId}/aggregated/list | Retrieve statistics about this conversion for a timeframe grouped by some temporal entity (day/week/month) |
| [**conversionsGetStatisticsSingle**](ConversionsApi.md#conversionsGetStatisticsSingle) | **GET** /conversions/{conversionId}/aggregated | Retrieve statistics about this conversion for a timeframe |
| [**conversionsPatch**](ConversionsApi.md#conversionsPatch) | **PUT** /conversions/{conversionId}/datapoints/patch | Modify the association between a conversion and a datapoint |
| [**conversionsPatchNotes**](ConversionsApi.md#conversionsPatchNotes) | **PUT** /conversions/{conversionId}/notes | Fast patch the \&quot;notes\&quot; field of a conversion |
| [**conversionsPost**](ConversionsApi.md#conversionsPost) | **POST** /conversions/{conversionId} | Update conversion specified by id |
| [**conversionsPut**](ConversionsApi.md#conversionsPut) | **POST** /conversions | Create a conversion |


<a id="conversionsConversionIdDatapointsBatchPatchPut"></a>
# **conversionsConversionIdDatapointsBatchPatchPut**
> ApiCoreResponsesEntityUriSystemInt64 conversionsConversionIdDatapointsBatchPatchPut(conversionId, apiCoreRequestsPatchBodyBatch)

Modify the association between a conversion and multiple datapoints

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ConversionsApi apiInstance = new ConversionsApi(defaultClient);
    Long conversionId = 56L; // Long | Id of the conversion
    ApiCoreRequestsPatchBodyBatch apiCoreRequestsPatchBodyBatch = new ApiCoreRequestsPatchBodyBatch(); // ApiCoreRequestsPatchBodyBatch | Patch requests
    try {
      ApiCoreResponsesEntityUriSystemInt64 result = apiInstance.conversionsConversionIdDatapointsBatchPatchPut(conversionId, apiCoreRequestsPatchBodyBatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversionsApi#conversionsConversionIdDatapointsBatchPatchPut");
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
| **conversionId** | **Long**| Id of the conversion | |
| **apiCoreRequestsPatchBodyBatch** | [**ApiCoreRequestsPatchBodyBatch**](ApiCoreRequestsPatchBodyBatch.md)| Patch requests | |

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

<a id="conversionsConversionIdGet"></a>
# **conversionsConversionIdGet**
> ApiCoreDtoConversionsConversion conversionsConversionIdGet(conversionId)

Retrieve conversion specified by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ConversionsApi apiInstance = new ConversionsApi(defaultClient);
    Long conversionId = 56L; // Long | Id of the conversion
    try {
      ApiCoreDtoConversionsConversion result = apiInstance.conversionsConversionIdGet(conversionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversionsApi#conversionsConversionIdGet");
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
| **conversionId** | **Long**| Id of the conversion | |

### Return type

[**ApiCoreDtoConversionsConversion**](ApiCoreDtoConversionsConversion.md)

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

<a id="conversionsCount"></a>
# **conversionsCount**
> ApiCoreResponsesCountResponce conversionsCount(status, textSearch, createdAfter, createdBefore)

Retrieve a count of conversions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ConversionsApi apiInstance = new ConversionsApi(defaultClient);
    String status = "deleted"; // String | Status of conversion (\"deleted\"/\"active\")
    String textSearch = "textSearch_example"; // String | Filter fields by this pattern
    String createdAfter = "createdAfter_example"; // String | Exclude conversions created before this date (YYYYMMDD)
    String createdBefore = "createdBefore_example"; // String | Exclude conversions created after this date (YYYYMMDD)
    try {
      ApiCoreResponsesCountResponce result = apiInstance.conversionsCount(status, textSearch, createdAfter, createdBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversionsApi#conversionsCount");
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
| **status** | **String**| Status of conversion (\&quot;deleted\&quot;/\&quot;active\&quot;) | [optional] [enum: deleted, active] |
| **textSearch** | **String**| Filter fields by this pattern | [optional] |
| **createdAfter** | **String**| Exclude conversions created before this date (YYYYMMDD) | [optional] |
| **createdBefore** | **String**| Exclude conversions created after this date (YYYYMMDD) | [optional] |

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
| **500** | Internal Server Error |  -  |

<a id="conversionsDelete"></a>
# **conversionsDelete**
> ApiCoreResponsesEntityUriSystemInt64 conversionsDelete(conversionId)

Delete conversion specified by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ConversionsApi apiInstance = new ConversionsApi(defaultClient);
    Long conversionId = 56L; // Long | Id of the conversion
    try {
      ApiCoreResponsesEntityUriSystemInt64 result = apiInstance.conversionsDelete(conversionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversionsApi#conversionsDelete");
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
| **conversionId** | **Long**| Id of the conversion | |

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

<a id="conversionsGet"></a>
# **conversionsGet**
> ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64 conversionsGet(offset, limit, status, textSearch, createdAfter, createdBefore)

Retrieve a list of conversions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ConversionsApi apiInstance = new ConversionsApi(defaultClient);
    Integer offset = 56; // Integer | Offset where to start from
    Integer limit = 56; // Integer | Limit results to this number
    String status = "deleted"; // String | Status of conversion (\"deleted\"/\"active\")
    String textSearch = "textSearch_example"; // String | Filter fields by this pattern
    String createdAfter = "createdAfter_example"; // String | Exclude conversions created before this date (YYYYMMDD)
    String createdBefore = "createdBefore_example"; // String | Exclude conversions created after this date (YYYYMMDD)
    try {
      ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64 result = apiInstance.conversionsGet(offset, limit, status, textSearch, createdAfter, createdBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversionsApi#conversionsGet");
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
| **offset** | **Integer**| Offset where to start from | [optional] |
| **limit** | **Integer**| Limit results to this number | [optional] |
| **status** | **String**| Status of conversion (\&quot;deleted\&quot;/\&quot;active\&quot;) | [optional] [enum: deleted, active] |
| **textSearch** | **String**| Filter fields by this pattern | [optional] |
| **createdAfter** | **String**| Exclude conversions created before this date (YYYYMMDD) | [optional] |
| **createdBefore** | **String**| Exclude conversions created after this date (YYYYMMDD) | [optional] |

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
| **500** | Internal Server Error |  -  |

<a id="conversionsGetDatapoints"></a>
# **conversionsGetDatapoints**
> ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64 conversionsGetDatapoints(conversionId, offset, limit, type, status, tags, textSearch, createdAfter, createdBefore)

Retrieve a list of datapoints connected to this conversion

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ConversionsApi apiInstance = new ConversionsApi(defaultClient);
    Long conversionId = 56L; // Long | Id of the conversion
    Integer offset = 56; // Integer | Offset where to start from
    Integer limit = 56; // Integer | Limit results to this number
    String type = "tp"; // String | Type of datapoint (\"tl\"/\"tp\")
    String status = "deleted"; // String | Status of datapoint (\"deleted\"/\"active\"/\"paused\"/\"spam\")
    String tags = "tags_example"; // String | Filter by this tag name
    String textSearch = "textSearch_example"; // String | Filter fields by this pattern
    String createdAfter = "createdAfter_example"; // String | Exclude datapoints created before this date (YYYYMMDD)
    String createdBefore = "createdBefore_example"; // String | Exclude datapoints created after this date (YYYYMMDD)
    try {
      ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64 result = apiInstance.conversionsGetDatapoints(conversionId, offset, limit, type, status, tags, textSearch, createdAfter, createdBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversionsApi#conversionsGetDatapoints");
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
| **conversionId** | **Long**| Id of the conversion | |
| **offset** | **Integer**| Offset where to start from | [optional] |
| **limit** | **Integer**| Limit results to this number | [optional] |
| **type** | **String**| Type of datapoint (\&quot;tl\&quot;/\&quot;tp\&quot;) | [optional] [enum: tp, tl] |
| **status** | **String**| Status of datapoint (\&quot;deleted\&quot;/\&quot;active\&quot;/\&quot;paused\&quot;/\&quot;spam\&quot;) | [optional] [enum: deleted, active, paused, spam] |
| **tags** | **String**| Filter by this tag name | [optional] |
| **textSearch** | **String**| Filter fields by this pattern | [optional] |
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
| **500** | Internal Server Error |  -  |

<a id="conversionsGetDatapointsCount"></a>
# **conversionsGetDatapointsCount**
> ApiCoreResponsesCountResponce conversionsGetDatapointsCount(conversionId, type, status, tags, textSearch, createdAfter, createdBefore)

Retrieve a count of datapoints connected to this conversion

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ConversionsApi apiInstance = new ConversionsApi(defaultClient);
    Long conversionId = 56L; // Long | Id of the conversion
    String type = "type_example"; // String | Type of datapoint (\"tl\"/\"tp\")
    String status = "status_example"; // String | Status of datapoint (\"deleted\"/\"active\"/\"paused\"/\"spam\")
    String tags = "tags_example"; // String | Filter by this tag name
    String textSearch = "textSearch_example"; // String | Filter fields by this pattern
    String createdAfter = "createdAfter_example"; // String | Exclude datapoints created before this date (YYYYMMDD)
    String createdBefore = "createdBefore_example"; // String | Exclude datapoints created after this date (YYYYMMDD)
    try {
      ApiCoreResponsesCountResponce result = apiInstance.conversionsGetDatapointsCount(conversionId, type, status, tags, textSearch, createdAfter, createdBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversionsApi#conversionsGetDatapointsCount");
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
| **conversionId** | **Long**| Id of the conversion | |
| **type** | **String**| Type of datapoint (\&quot;tl\&quot;/\&quot;tp\&quot;) | [optional] |
| **status** | **String**| Status of datapoint (\&quot;deleted\&quot;/\&quot;active\&quot;/\&quot;paused\&quot;/\&quot;spam\&quot;) | [optional] |
| **tags** | **String**| Filter by this tag name | [optional] |
| **textSearch** | **String**| Filter fields by this pattern | [optional] |
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
| **500** | Internal Server Error |  -  |

<a id="conversionsGetHits"></a>
# **conversionsGetHits**
> ApiCoreDtoClickStreamHitListPage conversionsGetHits(conversionId, timeframe, limit, offset, fromDay, toDay, filter)

Retrieve the list of events related to this conversion.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ConversionsApi apiInstance = new ConversionsApi(defaultClient);
    Long conversionId = 56L; // Long | Id of the conversion
    String timeframe = "yesterday"; // String | Timeframe of the request. See list at $timeframeList
    Integer limit = 56; // Integer | Limit results to this number
    String offset = "offset_example"; // String | Offset where to start from (it's the lastKey field in the response object)
    String fromDay = "fromDay_example"; // String | If using a \"custom\" timeFrame you can specify the starting day (YYYYMMDD)
    String toDay = "toDay_example"; // String | If using a \"custom\" timeFrame you can specify the ending day (YYYYMMDD)
    String filter = "spiders"; // String | Filter event type (\"spiders\"/\"uniques\"/\"nonuniques\"/\"conversions\")
    try {
      ApiCoreDtoClickStreamHitListPage result = apiInstance.conversionsGetHits(conversionId, timeframe, limit, offset, fromDay, toDay, filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversionsApi#conversionsGetHits");
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
| **conversionId** | **Long**| Id of the conversion | |
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

<a id="conversionsGetStatisticsAllList"></a>
# **conversionsGetStatisticsAllList**
> ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult conversionsGetStatisticsAllList(timeFrame, fromDay, toDay, status, groupBy)

Retrieve statistics about this customer for a timeframe related to a subset of conversions grouped by some temporal entity (day/week/month)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ConversionsApi apiInstance = new ConversionsApi(defaultClient);
    String timeFrame = "today"; // String | Timeframe of the request. See list at $timeframeList
    String fromDay = "fromDay_example"; // String | If using a \"custom\" timeFrame you can specify the starting day (YYYYMMDD)
    String toDay = "toDay_example"; // String | If using a \"custom\" timeFrame you can specify the ending day (YYYYMMDD)
    String status = "deleted"; // String | Status of conversion (\"deleted\"/\"active\")
    String groupBy = "week"; // String | The temporal entity you want to group by (\"week\"/\"month\"). If unspecified is \"day\".
    try {
      ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult result = apiInstance.conversionsGetStatisticsAllList(timeFrame, fromDay, toDay, status, groupBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversionsApi#conversionsGetStatisticsAllList");
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

<a id="conversionsGetStatisticsList"></a>
# **conversionsGetStatisticsList**
> ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult conversionsGetStatisticsList(conversionId, timeFrame, fromDay, toDay, groupBy)

Retrieve statistics about this conversion for a timeframe grouped by some temporal entity (day/week/month)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ConversionsApi apiInstance = new ConversionsApi(defaultClient);
    Long conversionId = 56L; // Long | Id of the conversion
    String timeFrame = "today"; // String | Timeframe of the request. See list at $timeframeList
    String fromDay = "fromDay_example"; // String | If using a \"custom\" timeFrame you can specify the starting day (YYYYMMDD)
    String toDay = "toDay_example"; // String | If using a \"custom\" timeFrame you can specify the ending day (YYYYMMDD)
    String groupBy = "week"; // String | The temporal entity you want to group by (\"week\"/\"month\"). If unspecified is \"day\".
    try {
      ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult result = apiInstance.conversionsGetStatisticsList(conversionId, timeFrame, fromDay, toDay, groupBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversionsApi#conversionsGetStatisticsList");
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
| **conversionId** | **Long**| Id of the conversion | |
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

<a id="conversionsGetStatisticsSingle"></a>
# **conversionsGetStatisticsSingle**
> ApiCoreDtoAggregatedAggregatedResult conversionsGetStatisticsSingle(conversionId, timeFrame, fromDay, toDay, tag, favourite, hourly)

Retrieve statistics about this conversion for a timeframe

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ConversionsApi apiInstance = new ConversionsApi(defaultClient);
    Long conversionId = 56L; // Long | Id of the conversion
    String timeFrame = "today"; // String | Timeframe of the request. See list at $timeframeList
    String fromDay = "fromDay_example"; // String | If using a \"custom\" timeFrame you can specify the starting day (YYYYMMDD)
    String toDay = "toDay_example"; // String | If using a \"custom\" timeFrame you can specify the ending day (YYYYMMDD)
    String tag = "tag_example"; // String | Filter by this tag name
    Boolean favourite = true; // Boolean | Is the datapoint marked as favourite
    Boolean hourly = true; // Boolean | If using \"yesterday\" or \"today\" timeframe you can ask for the hourly detail
    try {
      ApiCoreDtoAggregatedAggregatedResult result = apiInstance.conversionsGetStatisticsSingle(conversionId, timeFrame, fromDay, toDay, tag, favourite, hourly);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversionsApi#conversionsGetStatisticsSingle");
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
| **conversionId** | **Long**| Id of the conversion | |
| **timeFrame** | **String**| Timeframe of the request. See list at $timeframeList | [enum: today, yesterday, last7, last30, lastmonth, currentmonth, previousmonth, last90, last120, last180, last12months, lastyear, currentyear, beginning, custom] |
| **fromDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the starting day (YYYYMMDD) | [optional] |
| **toDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the ending day (YYYYMMDD) | [optional] |
| **tag** | **String**| Filter by this tag name | [optional] |
| **favourite** | **Boolean**| Is the datapoint marked as favourite | [optional] |
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

<a id="conversionsPatch"></a>
# **conversionsPatch**
> ApiCoreResponsesEntityUriSystemInt64 conversionsPatch(conversionId, apiCoreRequestsConversionPatchBody)

Modify the association between a conversion and a datapoint

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ConversionsApi apiInstance = new ConversionsApi(defaultClient);
    Long conversionId = 56L; // Long | Id of the conversion
    ApiCoreRequestsConversionPatchBody apiCoreRequestsConversionPatchBody = new ApiCoreRequestsConversionPatchBody(); // ApiCoreRequestsConversionPatchBody | Patch request
    try {
      ApiCoreResponsesEntityUriSystemInt64 result = apiInstance.conversionsPatch(conversionId, apiCoreRequestsConversionPatchBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversionsApi#conversionsPatch");
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
| **conversionId** | **Long**| Id of the conversion | |
| **apiCoreRequestsConversionPatchBody** | [**ApiCoreRequestsConversionPatchBody**](ApiCoreRequestsConversionPatchBody.md)| Patch request | |

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
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="conversionsPatchNotes"></a>
# **conversionsPatchNotes**
> ApiCoreResponsesEntityUriSystemInt64 conversionsPatchNotes(conversionId, apiCoreRequestsGenericTextPatch)

Fast patch the \&quot;notes\&quot; field of a conversion

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ConversionsApi apiInstance = new ConversionsApi(defaultClient);
    Long conversionId = 56L; // Long | Id of the conversion
    ApiCoreRequestsGenericTextPatch apiCoreRequestsGenericTextPatch = new ApiCoreRequestsGenericTextPatch(); // ApiCoreRequestsGenericTextPatch | Patch requests
    try {
      ApiCoreResponsesEntityUriSystemInt64 result = apiInstance.conversionsPatchNotes(conversionId, apiCoreRequestsGenericTextPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversionsApi#conversionsPatchNotes");
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
| **conversionId** | **Long**| Id of the conversion | |
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

<a id="conversionsPost"></a>
# **conversionsPost**
> ApiCoreResponsesEntityUriSystemInt64 conversionsPost(conversionId, apiCoreDtoConversionsConversion)

Update conversion specified by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ConversionsApi apiInstance = new ConversionsApi(defaultClient);
    Long conversionId = 56L; // Long | Id of the conversion
    ApiCoreDtoConversionsConversion apiCoreDtoConversionsConversion = new ApiCoreDtoConversionsConversion(); // ApiCoreDtoConversionsConversion | Updated body of the conversion
    try {
      ApiCoreResponsesEntityUriSystemInt64 result = apiInstance.conversionsPost(conversionId, apiCoreDtoConversionsConversion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversionsApi#conversionsPost");
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
| **conversionId** | **Long**| Id of the conversion | |
| **apiCoreDtoConversionsConversion** | [**ApiCoreDtoConversionsConversion**](ApiCoreDtoConversionsConversion.md)| Updated body of the conversion | |

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
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="conversionsPut"></a>
# **conversionsPut**
> ApiCoreResponsesEntityUriSystemInt64 conversionsPut(apiCoreDtoConversionsConversion)

Create a conversion

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ConversionsApi apiInstance = new ConversionsApi(defaultClient);
    ApiCoreDtoConversionsConversion apiCoreDtoConversionsConversion = new ApiCoreDtoConversionsConversion(); // ApiCoreDtoConversionsConversion | The body of the conversion
    try {
      ApiCoreResponsesEntityUriSystemInt64 result = apiInstance.conversionsPut(apiCoreDtoConversionsConversion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversionsApi#conversionsPut");
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
| **apiCoreDtoConversionsConversion** | [**ApiCoreDtoConversionsConversion**](ApiCoreDtoConversionsConversion.md)| The body of the conversion | |

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
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

