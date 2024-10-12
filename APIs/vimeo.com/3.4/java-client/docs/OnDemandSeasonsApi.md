# OnDemandSeasonsApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getVodSeason**](OnDemandSeasonsApi.md#getVodSeason) | **GET** /ondemand/pages/{ondemand_id}/seasons/{season_id} | Get a specific season on an On Demand page |
| [**getVodSeasonVideos**](OnDemandSeasonsApi.md#getVodSeasonVideos) | **GET** /ondemand/pages/{ondemand_id}/seasons/{season_id}/videos | Get all the videos in a season on an On Demand page |
| [**getVodSeasons**](OnDemandSeasonsApi.md#getVodSeasons) | **GET** /ondemand/pages/{ondemand_id}/seasons | Get all the seasons on an On Demand page |


<a id="getVodSeason"></a>
# **getVodSeason**
> OnDemandSeason getVodSeason(ondemandId, seasonId)

Get a specific season on an On Demand page

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandSeasonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OnDemandSeasonsApi apiInstance = new OnDemandSeasonsApi(defaultClient);
    BigDecimal ondemandId = new BigDecimal("61326"); // BigDecimal | The ID of the On Demand.
    BigDecimal seasonId = new BigDecimal("12345"); // BigDecimal | The ID of the season.
    try {
      OnDemandSeason result = apiInstance.getVodSeason(ondemandId, seasonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandSeasonsApi#getVodSeason");
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
| **ondemandId** | **BigDecimal**| The ID of the On Demand. | |
| **seasonId** | **BigDecimal**| The ID of the season. | |

### Return type

[**OnDemandSeason**](OnDemandSeason.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.ondemand.season+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The season was returned. |  -  |
| **404** | No such On Demand page or season exists. |  -  |

<a id="getVodSeasonVideos"></a>
# **getVodSeasonVideos**
> List&lt;Video&gt; getVodSeasonVideos(ondemandId, seasonId, filter, page, perPage, sort)

Get all the videos in a season on an On Demand page

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandSeasonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OnDemandSeasonsApi apiInstance = new OnDemandSeasonsApi(defaultClient);
    BigDecimal ondemandId = new BigDecimal("61326"); // BigDecimal | The ID of the On Demand.
    BigDecimal seasonId = new BigDecimal("12345"); // BigDecimal | The ID of the season.
    String filter = "viewable"; // String | The attribute by which to filter the results.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    String sort = "date"; // String | The way to sort the results.
    try {
      List<Video> result = apiInstance.getVodSeasonVideos(ondemandId, seasonId, filter, page, perPage, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandSeasonsApi#getVodSeasonVideos");
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
| **ondemandId** | **BigDecimal**| The ID of the On Demand. | |
| **seasonId** | **BigDecimal**| The ID of the season. | |
| **filter** | **String**| The attribute by which to filter the results. | [optional] [enum: viewable] |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |
| **sort** | **String**| The way to sort the results. | [optional] [enum: date, default, manual, name, purchase_time, release_date] |

### Return type

[**List&lt;Video&gt;**](Video.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.video+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The videos were returned. |  -  |

<a id="getVodSeasons"></a>
# **getVodSeasons**
> List&lt;OnDemandSeason&gt; getVodSeasons(ondemandId, direction, filter, page, perPage, sort)

Get all the seasons on an On Demand page

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandSeasonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OnDemandSeasonsApi apiInstance = new OnDemandSeasonsApi(defaultClient);
    BigDecimal ondemandId = new BigDecimal("61326"); // BigDecimal | The ID of the On Demand.
    String direction = "asc"; // String | The sort direction of the results.
    String filter = "viewable"; // String | The attribute by which to filter the results.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    String sort = "date"; // String | The way to sort the results.
    try {
      List<OnDemandSeason> result = apiInstance.getVodSeasons(ondemandId, direction, filter, page, perPage, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandSeasonsApi#getVodSeasons");
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
| **ondemandId** | **BigDecimal**| The ID of the On Demand. | |
| **direction** | **String**| The sort direction of the results. | [optional] [enum: asc, desc] |
| **filter** | **String**| The attribute by which to filter the results. | [optional] [enum: viewable] |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |
| **sort** | **String**| The way to sort the results. | [optional] [enum: date, manual] |

### Return type

[**List&lt;OnDemandSeason&gt;**](OnDemandSeason.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.ondemand.season+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The seasons were returned. |  -  |
| **404** | No such On Demand page exists. |  -  |

