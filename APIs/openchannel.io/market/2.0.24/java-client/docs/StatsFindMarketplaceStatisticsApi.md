# StatsFindMarketplaceStatisticsApi

All URIs are relative to *https://market.openchannel.io/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**statsIncrementFieldPost**](StatsFindMarketplaceStatisticsApi.md#statsIncrementFieldPost) | **POST** /stats/increment/{field} | Increments a statistics field |
| [**statsSeriesPeriodFieldsGet**](StatsFindMarketplaceStatisticsApi.md#statsSeriesPeriodFieldsGet) | **GET** /stats/series/{period}/{fields} | Return a timeseries for a particular field |
| [**statsTotalGet**](StatsFindMarketplaceStatisticsApi.md#statsTotalGet) | **GET** /stats/total | Returns the total number of events for a particular field. |


<a id="statsIncrementFieldPost"></a>
# **statsIncrementFieldPost**
> statsIncrementFieldPost(field, appId, userId, value, date)

Increments a statistics field

increment a statistics field

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatsFindMarketplaceStatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    StatsFindMarketplaceStatisticsApi apiInstance = new StatsFindMarketplaceStatisticsApi(defaultClient);
    String field = "field_example"; // String | The field to be incremented
    String appId = "appId_example"; // String | The id of the app associated with this statistic value
    String userId = "userId_example"; // String | The id of the user that is performing the action
    Integer value = 56; // Integer | The increment amount. Default is 1 if no value is provided.
    Long date = 56L; // Long | The date (in millis) for when this increment occurred. The default is the current date if no value is provided.
    try {
      apiInstance.statsIncrementFieldPost(field, appId, userId, value, date);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatsFindMarketplaceStatisticsApi#statsIncrementFieldPost");
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
| **field** | **String**| The field to be incremented | |
| **appId** | **String**| The id of the app associated with this statistic value | |
| **userId** | **String**| The id of the user that is performing the action | [optional] |
| **value** | **Integer**| The increment amount. Default is 1 if no value is provided. | [optional] |
| **date** | **Long**| The date (in millis) for when this increment occurred. The default is the current date if no value is provided. | [optional] |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | OK |  -  |

<a id="statsSeriesPeriodFieldsGet"></a>
# **statsSeriesPeriodFieldsGet**
> List&lt;List&lt;Object&gt;&gt; statsSeriesPeriodFieldsGet(period, fields, start, end, query)

Return a timeseries for a particular field

Return a timeseries nested array containing date and value. Example: [[1406520000000,2],[1406606400000,34],[1406692800000,245],...]

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatsFindMarketplaceStatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    StatsFindMarketplaceStatisticsApi apiInstance = new StatsFindMarketplaceStatisticsApi(defaultClient);
    String period = "day"; // String | The period for the series (day or month)
    String fields = "fields_example"; // String | The field to be graphed. This also be a comma separated list of fields and the result will be a single timeseries containing the sum of all fields.
    Long start = 56L; // Long | The start date for this series (in millis)
    Long end = 56L; // Long | The end date for this series (in millis)
    String query = "query_example"; // String | A query document. Example: {'developerId': '112'} matches all the apps that have the developer with id 112
    try {
      List<List<Object>> result = apiInstance.statsSeriesPeriodFieldsGet(period, fields, start, end, query);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatsFindMarketplaceStatisticsApi#statsSeriesPeriodFieldsGet");
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
| **period** | **String**| The period for the series (day or month) | [enum: day, month] |
| **fields** | **String**| The field to be graphed. This also be a comma separated list of fields and the result will be a single timeseries containing the sum of all fields. | |
| **start** | **Long**| The start date for this series (in millis) | [optional] |
| **end** | **Long**| The end date for this series (in millis) | [optional] |
| **query** | **String**| A query document. Example: {&#39;developerId&#39;: &#39;112&#39;} matches all the apps that have the developer with id 112 | [optional] |

### Return type

[**List&lt;List&lt;Object&gt;&gt;**](List.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | OK |  -  |

<a id="statsTotalGet"></a>
# **statsTotalGet**
> Total statsTotalGet(fields, query, start, end)

Returns the total number of events for a particular field.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatsFindMarketplaceStatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    StatsFindMarketplaceStatisticsApi apiInstance = new StatsFindMarketplaceStatisticsApi(defaultClient);
    String fields = "fields_example"; // String | A comma seperated list of all the fields to be returned in the total (available by default: dislikes, likes, reviews, totalSales, developerSales, marketplaceSales, downloads, ownerships, views)
    String query = "query_example"; // String | A query document. Example: {'developerId': '112'} matches all the apps that have the developer with id 112
    Long start = 56L; // Long | The start date for this total (in millis)
    Long end = 56L; // Long | The end date for this total (in millis)
    try {
      Total result = apiInstance.statsTotalGet(fields, query, start, end);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatsFindMarketplaceStatisticsApi#statsTotalGet");
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
| **fields** | **String**| A comma seperated list of all the fields to be returned in the total (available by default: dislikes, likes, reviews, totalSales, developerSales, marketplaceSales, downloads, ownerships, views) | |
| **query** | **String**| A query document. Example: {&#39;developerId&#39;: &#39;112&#39;} matches all the apps that have the developer with id 112 | [optional] |
| **start** | **Long**| The start date for this total (in millis) | [optional] |
| **end** | **Long**| The end date for this total (in millis) | [optional] |

### Return type

[**Total**](Total.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | OK |  -  |

