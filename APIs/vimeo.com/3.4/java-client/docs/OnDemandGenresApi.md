# OnDemandGenresApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addVodGenre**](OnDemandGenresApi.md#addVodGenre) | **PUT** /ondemand/pages/{ondemand_id}/genres/{genre_id} | Add a genre to an On Demand page |
| [**deleteVodGenre**](OnDemandGenresApi.md#deleteVodGenre) | **DELETE** /ondemand/pages/{ondemand_id}/genres/{genre_id} | Remove a genre from an On Demand page |
| [**getGenreVod**](OnDemandGenresApi.md#getGenreVod) | **GET** /ondemand/genres/{genre_id}/pages/{ondemand_id} | Get a specific On Demand page in a genre |
| [**getGenreVods**](OnDemandGenresApi.md#getGenreVods) | **GET** /ondemand/genres/{genre_id}/pages | Get all the On Demand pages in a genre |
| [**getVodGenre**](OnDemandGenresApi.md#getVodGenre) | **GET** /ondemand/genres/{genre_id} | Get a specific On Demand genre |
| [**getVodGenreByOndemandId**](OnDemandGenresApi.md#getVodGenreByOndemandId) | **GET** /ondemand/pages/{ondemand_id}/genres/{genre_id} | Check whether an On Demand page belongs to a genre |
| [**getVodGenres**](OnDemandGenresApi.md#getVodGenres) | **GET** /ondemand/genres | Get all On Demand genres |
| [**getVodGenresByOndemandId**](OnDemandGenresApi.md#getVodGenresByOndemandId) | **GET** /ondemand/pages/{ondemand_id}/genres | Get all the genres of an On Demand page |


<a id="addVodGenre"></a>
# **addVodGenre**
> OnDemandGenre addVodGenre(genreId, ondemandId)

Add a genre to an On Demand page

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandGenresApi;

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

    OnDemandGenresApi apiInstance = new OnDemandGenresApi(defaultClient);
    String genreId = "animation"; // String | The ID of the genre.
    BigDecimal ondemandId = new BigDecimal("61326"); // BigDecimal | The ID of the On Demand.
    try {
      OnDemandGenre result = apiInstance.addVodGenre(genreId, ondemandId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandGenresApi#addVodGenre");
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
| **genreId** | **String**| The ID of the genre. | |
| **ondemandId** | **BigDecimal**| The ID of the On Demand. | |

### Return type

[**OnDemandGenre**](OnDemandGenre.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.ondemand.genre+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The genre was added. |  -  |
| **400** | You can&#39;t add more than two genres to an On Demand page. |  -  |
| **403** | You can&#39;t modify an On Demand page that you don&#39;t own. |  -  |
| **404** | No such On Demand page or genre exists. |  -  |

<a id="deleteVodGenre"></a>
# **deleteVodGenre**
> deleteVodGenre(genreId, ondemandId)

Remove a genre from an On Demand page

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandGenresApi;

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

    OnDemandGenresApi apiInstance = new OnDemandGenresApi(defaultClient);
    String genreId = "animation"; // String | The ID of the genre.
    BigDecimal ondemandId = new BigDecimal("61326"); // BigDecimal | The ID of the On Demand.
    try {
      apiInstance.deleteVodGenre(genreId, ondemandId);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandGenresApi#deleteVodGenre");
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
| **genreId** | **String**| The ID of the genre. | |
| **ondemandId** | **BigDecimal**| The ID of the On Demand. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.ondemand.genre+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The On Demand genre was deleted. |  -  |
| **400** | The On Demand page must belong to at least one genre. |  -  |
| **403** | You can&#39;t modify an On Demand page that you don&#39;t own. |  -  |
| **404** | No such On Demand page or genre exists. |  -  |

<a id="getGenreVod"></a>
# **getGenreVod**
> OnDemandPage getGenreVod(genreId, ondemandId)

Get a specific On Demand page in a genre

Check whether a genre contains an On Demand page.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandGenresApi;

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

    OnDemandGenresApi apiInstance = new OnDemandGenresApi(defaultClient);
    String genreId = "animation"; // String | The ID of the genre.
    BigDecimal ondemandId = new BigDecimal("61326"); // BigDecimal | The ID of the On Demand.
    try {
      OnDemandPage result = apiInstance.getGenreVod(genreId, ondemandId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandGenresApi#getGenreVod");
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
| **genreId** | **String**| The ID of the genre. | |
| **ondemandId** | **BigDecimal**| The ID of the On Demand. | |

### Return type

[**OnDemandPage**](OnDemandPage.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.ondemand.page+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The On Demand page belongs to the genre. |  -  |
| **404** | No such On Demand page or genre exists. |  -  |

<a id="getGenreVods"></a>
# **getGenreVods**
> List&lt;OnDemandPage&gt; getGenreVods(genreId, direction, filter, page, perPage, query, sort)

Get all the On Demand pages in a genre

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandGenresApi;

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

    OnDemandGenresApi apiInstance = new OnDemandGenresApi(defaultClient);
    String genreId = "animation"; // String | The ID of the genre.
    String direction = "asc"; // String | The sort direction of the results.
    String filter = "country"; // String | The attribute by which to filter the results.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    String query = "Stop motion"; // String | The search query to use to filter the results.
    String sort = "alphabetical"; // String | The way to sort the results.
    try {
      List<OnDemandPage> result = apiInstance.getGenreVods(genreId, direction, filter, page, perPage, query, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandGenresApi#getGenreVods");
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
| **genreId** | **String**| The ID of the genre. | |
| **direction** | **String**| The sort direction of the results. | [optional] [enum: asc, desc] |
| **filter** | **String**| The attribute by which to filter the results. | [optional] [enum: country, my_region] |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |
| **query** | **String**| The search query to use to filter the results. | [optional] |
| **sort** | **String**| The way to sort the results. | [optional] [enum: alphabetical, date, name, publish.time, videos] |

### Return type

[**List&lt;OnDemandPage&gt;**](OnDemandPage.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.ondemand.page+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The On Demand pages were returned. |  -  |

<a id="getVodGenre"></a>
# **getVodGenre**
> OnDemandGenre getVodGenre(genreId)

Get a specific On Demand genre

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandGenresApi;

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

    OnDemandGenresApi apiInstance = new OnDemandGenresApi(defaultClient);
    String genreId = "animation"; // String | The ID of the genre.
    try {
      OnDemandGenre result = apiInstance.getVodGenre(genreId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandGenresApi#getVodGenre");
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
| **genreId** | **String**| The ID of the genre. | |

### Return type

[**OnDemandGenre**](OnDemandGenre.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.ondemand.genre+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The On Demand genre was returned. |  -  |
| **404** | No such On Demand genre exists. |  -  |

<a id="getVodGenreByOndemandId"></a>
# **getVodGenreByOndemandId**
> OnDemandGenre getVodGenreByOndemandId(genreId, ondemandId)

Check whether an On Demand page belongs to a genre

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandGenresApi;

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

    OnDemandGenresApi apiInstance = new OnDemandGenresApi(defaultClient);
    String genreId = "animation"; // String | The ID of the genre.
    BigDecimal ondemandId = new BigDecimal("61326"); // BigDecimal | The ID of the On Demand.
    try {
      OnDemandGenre result = apiInstance.getVodGenreByOndemandId(genreId, ondemandId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandGenresApi#getVodGenreByOndemandId");
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
| **genreId** | **String**| The ID of the genre. | |
| **ondemandId** | **BigDecimal**| The ID of the On Demand. | |

### Return type

[**OnDemandGenre**](OnDemandGenre.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.ondemand.genre+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The On Demand page&#39;s genre was returned. |  -  |
| **404** | No such On Demand page or genre exists. |  -  |

<a id="getVodGenres"></a>
# **getVodGenres**
> List&lt;OnDemandGenre&gt; getVodGenres()

Get all On Demand genres

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandGenresApi;

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

    OnDemandGenresApi apiInstance = new OnDemandGenresApi(defaultClient);
    try {
      List<OnDemandGenre> result = apiInstance.getVodGenres();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandGenresApi#getVodGenres");
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

[**List&lt;OnDemandGenre&gt;**](OnDemandGenre.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.ondemand.genre+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The On Demand genres were returned. |  -  |

<a id="getVodGenresByOndemandId"></a>
# **getVodGenresByOndemandId**
> List&lt;OnDemandGenre&gt; getVodGenresByOndemandId(ondemandId)

Get all the genres of an On Demand page

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandGenresApi;

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

    OnDemandGenresApi apiInstance = new OnDemandGenresApi(defaultClient);
    BigDecimal ondemandId = new BigDecimal("61326"); // BigDecimal | The ID of the On Demand.
    try {
      List<OnDemandGenre> result = apiInstance.getVodGenresByOndemandId(ondemandId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandGenresApi#getVodGenresByOndemandId");
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

### Return type

[**List&lt;OnDemandGenre&gt;**](OnDemandGenre.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.ondemand.genre+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The genres were returned. |  -  |
| **404** | No such On Demand page exists. |  -  |

