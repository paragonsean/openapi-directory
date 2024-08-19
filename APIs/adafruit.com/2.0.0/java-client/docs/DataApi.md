# DataApi

All URIs are relative to *https://io.adafruit.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**allData**](DataApi.md#allData) | **GET** /{username}/feeds/{feed_key}/data | Get all data for the given feed |
| [**allGroupFeedData**](DataApi.md#allGroupFeedData) | **GET** /{username}/groups/{group_key}/feeds/{feed_key}/data | All data for current feed in a specific group |
| [**batchCreateData**](DataApi.md#batchCreateData) | **POST** /{username}/feeds/{feed_key}/data/batch | Create multiple new Data records |
| [**batchCreateGroupFeedData**](DataApi.md#batchCreateGroupFeedData) | **POST** /{username}/groups/{group_key}/feeds/{feed_key}/data/batch | Create multiple new Data records in a feed belonging to a particular group |
| [**chartData**](DataApi.md#chartData) | **GET** /{username}/feeds/{feed_key}/data/chart | Chart data for current feed |
| [**createData**](DataApi.md#createData) | **POST** /{username}/feeds/{feed_key}/data | Create new Data |
| [**createGroupData**](DataApi.md#createGroupData) | **POST** /{username}/groups/{group_key}/data | Create new data for multiple feeds in a group |
| [**createGroupFeedData**](DataApi.md#createGroupFeedData) | **POST** /{username}/groups/{group_key}/feeds/{feed_key}/data | Create new Data in a feed belonging to a particular group |
| [**createRawWebhookFeedData_0**](DataApi.md#createRawWebhookFeedData_0) | **POST** /webhooks/feed/:token/raw | Send arbitrary data to a feed via webhook URL. |
| [**createWebhookFeedData_0**](DataApi.md#createWebhookFeedData_0) | **POST** /webhooks/feed/:token | Send data to a feed via webhook URL. |
| [**destroyData**](DataApi.md#destroyData) | **DELETE** /{username}/feeds/{feed_key}/data/{id} | Delete existing Data |
| [**firstData**](DataApi.md#firstData) | **GET** /{username}/feeds/{feed_key}/data/first | First Data in Queue |
| [**getData**](DataApi.md#getData) | **GET** /{username}/feeds/{feed_key}/data/{id} | Returns data based on feed key |
| [**lastData**](DataApi.md#lastData) | **GET** /{username}/feeds/{feed_key}/data/last | Last Data in Queue |
| [**nextData**](DataApi.md#nextData) | **GET** /{username}/feeds/{feed_key}/data/next | Next Data in Queue |
| [**previousData**](DataApi.md#previousData) | **GET** /{username}/feeds/{feed_key}/data/previous | Previous Data in Queue |
| [**replaceData**](DataApi.md#replaceData) | **PUT** /{username}/feeds/{feed_key}/data/{id} | Replace existing Data |
| [**retainData**](DataApi.md#retainData) | **GET** /{username}/feeds/{feed_key}/data/retain | Last Data in MQTT CSV format |
| [**updateData**](DataApi.md#updateData) | **PATCH** /{username}/feeds/{feed_key}/data/{id} | Update properties of existing Data |


<a id="allData"></a>
# **allData**
> List&lt;DataResponse&gt; allData(username, feedKey, startTime, endTime, limit, include)

Get all data for the given feed

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    DataApi apiInstance = new DataApi(defaultClient);
    String username = "username_example"; // String | a valid username string
    String feedKey = "feedKey_example"; // String | a valid feed key
    OffsetDateTime startTime = OffsetDateTime.now(); // OffsetDateTime | Start time for filtering, returns records created after given time.
    OffsetDateTime endTime = OffsetDateTime.now(); // OffsetDateTime | End time for filtering, returns records created before give time.
    Integer limit = 56; // Integer | Limit the number of records returned.
    String include = "include_example"; // String | List of Data record fields to include in response as comma separated list. Acceptable values are: `value`, `lat`, `lon`, `ele`, `id`, and `created_at`. 
    try {
      List<DataResponse> result = apiInstance.allData(username, feedKey, startTime, endTime, limit, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataApi#allData");
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
| **username** | **String**| a valid username string | |
| **feedKey** | **String**| a valid feed key | |
| **startTime** | **OffsetDateTime**| Start time for filtering, returns records created after given time. | [optional] |
| **endTime** | **OffsetDateTime**| End time for filtering, returns records created before give time. | [optional] |
| **limit** | **Integer**| Limit the number of records returned. | [optional] |
| **include** | **String**| List of Data record fields to include in response as comma separated list. Acceptable values are: &#x60;value&#x60;, &#x60;lat&#x60;, &#x60;lon&#x60;, &#x60;ele&#x60;, &#x60;id&#x60;, and &#x60;created_at&#x60;.  | [optional] |

### Return type

[**List&lt;DataResponse&gt;**](DataResponse.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of data |  * X-Pagination-Count - The number of records returned. <br>  * X-Pagination-Limit - The limit this request is using, either your given value or the default (1000). <br>  * X-Pagination-End - The created_at value for the newest record returned. <br>  * X-Pagination-Start - The created_at value for the oldest record returned. <br>  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="allGroupFeedData"></a>
# **allGroupFeedData**
> List&lt;DataResponse&gt; allGroupFeedData(username, groupKey, feedKey, startTime, endTime, limit)

All data for current feed in a specific group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    DataApi apiInstance = new DataApi(defaultClient);
    String username = "username_example"; // String | a valid username string
    String groupKey = "groupKey_example"; // String | 
    String feedKey = "feedKey_example"; // String | a valid feed key
    OffsetDateTime startTime = OffsetDateTime.now(); // OffsetDateTime | Start time for filtering data. Returns data created after given time.
    OffsetDateTime endTime = OffsetDateTime.now(); // OffsetDateTime | End time for filtering data. Returns data created before give time.
    Integer limit = 56; // Integer | Limit the number of records returned.
    try {
      List<DataResponse> result = apiInstance.allGroupFeedData(username, groupKey, feedKey, startTime, endTime, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataApi#allGroupFeedData");
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
| **username** | **String**| a valid username string | |
| **groupKey** | **String**|  | |
| **feedKey** | **String**| a valid feed key | |
| **startTime** | **OffsetDateTime**| Start time for filtering data. Returns data created after given time. | [optional] |
| **endTime** | **OffsetDateTime**| End time for filtering data. Returns data created before give time. | [optional] |
| **limit** | **Integer**| Limit the number of records returned. | [optional] |

### Return type

[**List&lt;DataResponse&gt;**](DataResponse.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of data |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="batchCreateData"></a>
# **batchCreateData**
> List&lt;DataResponse&gt; batchCreateData(username, feedKey, data)

Create multiple new Data records

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    DataApi apiInstance = new DataApi(defaultClient);
    String username = "username_example"; // String | a valid username string
    String feedKey = "feedKey_example"; // String | a valid feed key
    List<CreateDataRequest> data = Arrays.asList(); // List<CreateDataRequest> | A collection of data records including `value` (required) and optionally including: `lat`, `lon`, `ele` (latitude, longitude, and elevation values), and `created_at` (a date/time string).
    try {
      List<DataResponse> result = apiInstance.batchCreateData(username, feedKey, data);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataApi#batchCreateData");
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
| **username** | **String**| a valid username string | |
| **feedKey** | **String**| a valid feed key | |
| **data** | [**List&lt;CreateDataRequest&gt;**](CreateDataRequest.md)| A collection of data records including &#x60;value&#x60; (required) and optionally including: &#x60;lat&#x60;, &#x60;lon&#x60;, &#x60;ele&#x60; (latitude, longitude, and elevation values), and &#x60;created_at&#x60; (a date/time string). | |

### Return type

[**List&lt;DataResponse&gt;**](DataResponse.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | New data |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="batchCreateGroupFeedData"></a>
# **batchCreateGroupFeedData**
> List&lt;DataResponse&gt; batchCreateGroupFeedData(username, groupKey, feedKey, data)

Create multiple new Data records in a feed belonging to a particular group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    DataApi apiInstance = new DataApi(defaultClient);
    String username = "username_example"; // String | a valid username string
    String groupKey = "groupKey_example"; // String | 
    String feedKey = "feedKey_example"; // String | a valid feed key
    List<CreateDataRequest> data = Arrays.asList(); // List<CreateDataRequest> | A collection of data records including `value` (required) and optionally including: `lat`, `lon`, `ele` (latitude, longitude, and elevation values), and `created_at` (a date/time string).
    try {
      List<DataResponse> result = apiInstance.batchCreateGroupFeedData(username, groupKey, feedKey, data);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataApi#batchCreateGroupFeedData");
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
| **username** | **String**| a valid username string | |
| **groupKey** | **String**|  | |
| **feedKey** | **String**| a valid feed key | |
| **data** | [**List&lt;CreateDataRequest&gt;**](CreateDataRequest.md)| A collection of data records including &#x60;value&#x60; (required) and optionally including: &#x60;lat&#x60;, &#x60;lon&#x60;, &#x60;ele&#x60; (latitude, longitude, and elevation values), and &#x60;created_at&#x60; (a date/time string). | |

### Return type

[**List&lt;DataResponse&gt;**](DataResponse.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | New data |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="chartData"></a>
# **chartData**
> ChartData200Response chartData(username, feedKey, startTime, endTime, resolution, hours)

Chart data for current feed

The Chart API is what we use on io.adafruit.com to populate charts over varying timespans with a consistent number of data points. The maximum number of points returned is 480. This API works by aggregating slices of time into a single value by averaging.  All time-based parameters are optional, if none are given it will default to 1 hour at the finest-grained resolution possible.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    DataApi apiInstance = new DataApi(defaultClient);
    String username = "username_example"; // String | a valid username string
    String feedKey = "feedKey_example"; // String | a valid feed key
    OffsetDateTime startTime = OffsetDateTime.now(); // OffsetDateTime | Start time for filtering, returns records created after given time.
    OffsetDateTime endTime = OffsetDateTime.now(); // OffsetDateTime | End time for filtering, returns records created before give time.
    Integer resolution = 56; // Integer | A resolution size in minutes. By giving a resolution value you will get back grouped data points aggregated over resolution-sized intervals. NOTE: time span is preferred over resolution, so if you request a span of time that includes more than max limit points you may get a larger resolution than you requested. Valid resolutions are 1, 5, 10, 30, 60, and 120.
    Integer hours = 56; // Integer | The number of hours the chart should cover.
    try {
      ChartData200Response result = apiInstance.chartData(username, feedKey, startTime, endTime, resolution, hours);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataApi#chartData");
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
| **username** | **String**| a valid username string | |
| **feedKey** | **String**| a valid feed key | |
| **startTime** | **OffsetDateTime**| Start time for filtering, returns records created after given time. | [optional] |
| **endTime** | **OffsetDateTime**| End time for filtering, returns records created before give time. | [optional] |
| **resolution** | **Integer**| A resolution size in minutes. By giving a resolution value you will get back grouped data points aggregated over resolution-sized intervals. NOTE: time span is preferred over resolution, so if you request a span of time that includes more than max limit points you may get a larger resolution than you requested. Valid resolutions are 1, 5, 10, 30, 60, and 120. | [optional] |
| **hours** | **Integer**| The number of hours the chart should cover. | [optional] |

### Return type

[**ChartData200Response**](ChartData200Response.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A JSON record containing chart data and the parameters used to generate it. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="createData"></a>
# **createData**
> Data createData(username, feedKey, datum)

Create new Data

Create new data records on the given feed.  **NOTE:** when feed history is on, data &#x60;value&#x60; size is limited to 1KB, when feed history is turned off data value size is limited to 100KB.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    DataApi apiInstance = new DataApi(defaultClient);
    String username = "username_example"; // String | a valid username string
    String feedKey = "feedKey_example"; // String | a valid feed key
    CreateDataRequest datum = new CreateDataRequest(); // CreateDataRequest | Data record including a `value` field (required) and optionally including: `lat`, `lon`, `ele` (latitude, longitude, and elevation values), and `created_at` (a date/time string).
    try {
      Data result = apiInstance.createData(username, feedKey, datum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataApi#createData");
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
| **username** | **String**| a valid username string | |
| **feedKey** | **String**| a valid feed key | |
| **datum** | [**CreateDataRequest**](CreateDataRequest.md)| Data record including a &#x60;value&#x60; field (required) and optionally including: &#x60;lat&#x60;, &#x60;lon&#x60;, &#x60;ele&#x60; (latitude, longitude, and elevation values), and &#x60;created_at&#x60; (a date/time string). | |

### Return type

[**Data**](Data.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | New data |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="createGroupData"></a>
# **createGroupData**
> List&lt;DataResponse&gt; createGroupData(username, groupKey, groupFeedData)

Create new data for multiple feeds in a group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    DataApi apiInstance = new DataApi(defaultClient);
    String username = "username_example"; // String | a valid username string
    String groupKey = "groupKey_example"; // String | 
    CreateGroupDataRequest groupFeedData = new CreateGroupDataRequest(); // CreateGroupDataRequest | 
    try {
      List<DataResponse> result = apiInstance.createGroupData(username, groupKey, groupFeedData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataApi#createGroupData");
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
| **username** | **String**| a valid username string | |
| **groupKey** | **String**|  | |
| **groupFeedData** | [**CreateGroupDataRequest**](CreateGroupDataRequest.md)|  | |

### Return type

[**List&lt;DataResponse&gt;**](DataResponse.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | New data |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="createGroupFeedData"></a>
# **createGroupFeedData**
> DataResponse createGroupFeedData(username, groupKey, feedKey, datum)

Create new Data in a feed belonging to a particular group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    DataApi apiInstance = new DataApi(defaultClient);
    String username = "username_example"; // String | a valid username string
    String groupKey = "groupKey_example"; // String | 
    String feedKey = "feedKey_example"; // String | a valid feed key
    CreateDataRequest datum = new CreateDataRequest(); // CreateDataRequest | Data record including a `value` field (required) and optionally including: `lat`, `lon`, `ele` (latitude, longitude, and elevation values), and `created_at` (a date/time string).
    try {
      DataResponse result = apiInstance.createGroupFeedData(username, groupKey, feedKey, datum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataApi#createGroupFeedData");
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
| **username** | **String**| a valid username string | |
| **groupKey** | **String**|  | |
| **feedKey** | **String**| a valid feed key | |
| **datum** | [**CreateDataRequest**](CreateDataRequest.md)| Data record including a &#x60;value&#x60; field (required) and optionally including: &#x60;lat&#x60;, &#x60;lon&#x60;, &#x60;ele&#x60; (latitude, longitude, and elevation values), and &#x60;created_at&#x60; (a date/time string). | |

### Return type

[**DataResponse**](DataResponse.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | New data |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="createRawWebhookFeedData_0"></a>
# **createRawWebhookFeedData_0**
> Data createRawWebhookFeedData_0()

Send arbitrary data to a feed via webhook URL.

The raw data webhook receiver accepts POST requests and stores the raw request body on your feed. This is useful when you don&#39;t have control of the webhook sender. If feed history is turned on, payloads will be truncated at 1024 bytes. If feed history is turned off, payloads will be truncated at 100KB.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    DataApi apiInstance = new DataApi(defaultClient);
    try {
      Data result = apiInstance.createRawWebhookFeedData_0();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataApi#createRawWebhookFeedData_0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Data**](Data.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | New feed data record |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="createWebhookFeedData_0"></a>
# **createWebhookFeedData_0**
> Data createWebhookFeedData_0(payload)

Send data to a feed via webhook URL.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    DataApi apiInstance = new DataApi(defaultClient);
    CreateWebhookFeedDataRequest payload = new CreateWebhookFeedDataRequest(); // CreateWebhookFeedDataRequest | Webhook payload containing data `value` parameter.
    try {
      Data result = apiInstance.createWebhookFeedData_0(payload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataApi#createWebhookFeedData_0");
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
| **payload** | [**CreateWebhookFeedDataRequest**](CreateWebhookFeedDataRequest.md)| Webhook payload containing data &#x60;value&#x60; parameter. | |

### Return type

[**Data**](Data.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | New feed data record |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="destroyData"></a>
# **destroyData**
> String destroyData(username, feedKey, id)

Delete existing Data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    DataApi apiInstance = new DataApi(defaultClient);
    String username = "username_example"; // String | a valid username string
    String feedKey = "feedKey_example"; // String | a valid feed key
    String id = "id_example"; // String | 
    try {
      String result = apiInstance.destroyData(username, feedKey, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataApi#destroyData");
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
| **username** | **String**| a valid username string | |
| **feedKey** | **String**| a valid feed key | |
| **id** | **String**|  | |

### Return type

**String**

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted Group successfully |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="firstData"></a>
# **firstData**
> DataResponse firstData(username, feedKey, include)

First Data in Queue

Get the oldest data point in the feed. This request sets the queue pointer to the beginning of the feed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    DataApi apiInstance = new DataApi(defaultClient);
    String username = "username_example"; // String | a valid username string
    String feedKey = "feedKey_example"; // String | a valid feed key
    String include = "include_example"; // String | List of Data record fields to include in response as comma separated list. Acceptable values are: `value`, `lat`, `lon`, `ele`, `id`, and `created_at`. 
    try {
      DataResponse result = apiInstance.firstData(username, feedKey, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataApi#firstData");
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
| **username** | **String**| a valid username string | |
| **feedKey** | **String**| a valid feed key | |
| **include** | **String**| List of Data record fields to include in response as comma separated list. Acceptable values are: &#x60;value&#x60;, &#x60;lat&#x60;, &#x60;lon&#x60;, &#x60;ele&#x60;, &#x60;id&#x60;, and &#x60;created_at&#x60;.  | [optional] |

### Return type

[**DataResponse**](DataResponse.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Data response |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="getData"></a>
# **getData**
> DataResponse getData(username, feedKey, id, include)

Returns data based on feed key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    DataApi apiInstance = new DataApi(defaultClient);
    String username = "username_example"; // String | a valid username string
    String feedKey = "feedKey_example"; // String | a valid feed key
    String id = "id_example"; // String | 
    String include = "include_example"; // String | List of Data record fields to include in response as comma separated list. Acceptable values are: `value`, `lat`, `lon`, `ele`, `id`, and `created_at`. 
    try {
      DataResponse result = apiInstance.getData(username, feedKey, id, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataApi#getData");
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
| **username** | **String**| a valid username string | |
| **feedKey** | **String**| a valid feed key | |
| **id** | **String**|  | |
| **include** | **String**| List of Data record fields to include in response as comma separated list. Acceptable values are: &#x60;value&#x60;, &#x60;lat&#x60;, &#x60;lon&#x60;, &#x60;ele&#x60;, &#x60;id&#x60;, and &#x60;created_at&#x60;.  | [optional] |

### Return type

[**DataResponse**](DataResponse.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Data response |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="lastData"></a>
# **lastData**
> DataResponse lastData(username, feedKey, include)

Last Data in Queue

Get the most recent data point in the feed. This request sets the queue pointer to the end of the feed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    DataApi apiInstance = new DataApi(defaultClient);
    String username = "username_example"; // String | a valid username string
    String feedKey = "feedKey_example"; // String | a valid feed key
    String include = "include_example"; // String | List of Data record fields to include in response as comma separated list. Acceptable values are: `value`, `lat`, `lon`, `ele`, `id`, and `created_at`. 
    try {
      DataResponse result = apiInstance.lastData(username, feedKey, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataApi#lastData");
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
| **username** | **String**| a valid username string | |
| **feedKey** | **String**| a valid feed key | |
| **include** | **String**| List of Data record fields to include in response as comma separated list. Acceptable values are: &#x60;value&#x60;, &#x60;lat&#x60;, &#x60;lon&#x60;, &#x60;ele&#x60;, &#x60;id&#x60;, and &#x60;created_at&#x60;.  | [optional] |

### Return type

[**DataResponse**](DataResponse.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Data response |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="nextData"></a>
# **nextData**
> DataResponse nextData(username, feedKey, include)

Next Data in Queue

Get the next newest data point in the feed. If queue processing hasn&#39;t been started, the first data point in the feed will be returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    DataApi apiInstance = new DataApi(defaultClient);
    String username = "username_example"; // String | a valid username string
    String feedKey = "feedKey_example"; // String | a valid feed key
    String include = "include_example"; // String | List of Data record fields to include in response as comma separated list. Acceptable values are: `value`, `lat`, `lon`, `ele`, `id`, and `created_at`. 
    try {
      DataResponse result = apiInstance.nextData(username, feedKey, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataApi#nextData");
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
| **username** | **String**| a valid username string | |
| **feedKey** | **String**| a valid feed key | |
| **include** | **String**| List of Data record fields to include in response as comma separated list. Acceptable values are: &#x60;value&#x60;, &#x60;lat&#x60;, &#x60;lon&#x60;, &#x60;ele&#x60;, &#x60;id&#x60;, and &#x60;created_at&#x60;.  | [optional] |

### Return type

[**DataResponse**](DataResponse.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Data response |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="previousData"></a>
# **previousData**
> DataResponse previousData(username, feedKey, include)

Previous Data in Queue

Get the previously processed data point in the feed. NOTE: this method doesn&#39;t move the processing queue pointer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    DataApi apiInstance = new DataApi(defaultClient);
    String username = "username_example"; // String | a valid username string
    String feedKey = "feedKey_example"; // String | a valid feed key
    String include = "include_example"; // String | List of Data record fields to include in response as comma separated list. Acceptable values are: `value`, `lat`, `lon`, `ele`, `id`, and `created_at`. 
    try {
      DataResponse result = apiInstance.previousData(username, feedKey, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataApi#previousData");
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
| **username** | **String**| a valid username string | |
| **feedKey** | **String**| a valid feed key | |
| **include** | **String**| List of Data record fields to include in response as comma separated list. Acceptable values are: &#x60;value&#x60;, &#x60;lat&#x60;, &#x60;lon&#x60;, &#x60;ele&#x60;, &#x60;id&#x60;, and &#x60;created_at&#x60;.  | [optional] |

### Return type

[**DataResponse**](DataResponse.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Data response |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="replaceData"></a>
# **replaceData**
> DataResponse replaceData(username, feedKey, id, datum)

Replace existing Data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    DataApi apiInstance = new DataApi(defaultClient);
    String username = "username_example"; // String | a valid username string
    String feedKey = "feedKey_example"; // String | a valid feed key
    String id = "id_example"; // String | 
    CreateDataRequest datum = new CreateDataRequest(); // CreateDataRequest | Data record including a `value` field (required) and optionally including: `lat`, `lon`, `ele` (latitude, longitude, and elevation values), and `created_at` (a date/time string).
    try {
      DataResponse result = apiInstance.replaceData(username, feedKey, id, datum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataApi#replaceData");
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
| **username** | **String**| a valid username string | |
| **feedKey** | **String**| a valid feed key | |
| **id** | **String**|  | |
| **datum** | [**CreateDataRequest**](CreateDataRequest.md)| Data record including a &#x60;value&#x60; field (required) and optionally including: &#x60;lat&#x60;, &#x60;lon&#x60;, &#x60;ele&#x60; (latitude, longitude, and elevation values), and &#x60;created_at&#x60; (a date/time string). | |

### Return type

[**DataResponse**](DataResponse.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated Data |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="retainData"></a>
# **retainData**
> String retainData(username, feedKey)

Last Data in MQTT CSV format

Get the most recent data point in the feed in an MQTT compatible CSV format: &#x60;value,lat,lon,ele&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    DataApi apiInstance = new DataApi(defaultClient);
    String username = "username_example"; // String | a valid username string
    String feedKey = "feedKey_example"; // String | a valid feed key
    try {
      String result = apiInstance.retainData(username, feedKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataApi#retainData");
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
| **username** | **String**| a valid username string | |
| **feedKey** | **String**| a valid feed key | |

### Return type

**String**

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | CSV string in &#x60;value,lat,lon,ele&#x60; format. The lat, lon, and ele values are left blank if they are not set. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="updateData"></a>
# **updateData**
> DataResponse updateData(username, feedKey, id, datum)

Update properties of existing Data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    DataApi apiInstance = new DataApi(defaultClient);
    String username = "username_example"; // String | a valid username string
    String feedKey = "feedKey_example"; // String | a valid feed key
    String id = "id_example"; // String | 
    CreateDataRequest datum = new CreateDataRequest(); // CreateDataRequest | Data record including a `value` field (required) and optionally including: `lat`, `lon`, `ele` (latitude, longitude, and elevation values), and `created_at` (a date/time string).
    try {
      DataResponse result = apiInstance.updateData(username, feedKey, id, datum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataApi#updateData");
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
| **username** | **String**| a valid username string | |
| **feedKey** | **String**| a valid feed key | |
| **id** | **String**|  | |
| **datum** | [**CreateDataRequest**](CreateDataRequest.md)| Data record including a &#x60;value&#x60; field (required) and optionally including: &#x60;lat&#x60;, &#x60;lon&#x60;, &#x60;ele&#x60; (latitude, longitude, and elevation values), and &#x60;created_at&#x60; (a date/time string). | |

### Return type

[**DataResponse**](DataResponse.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated Data |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

