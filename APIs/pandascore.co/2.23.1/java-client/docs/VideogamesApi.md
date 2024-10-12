# VideogamesApi

All URIs are relative to *https://api.pandascore.co*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getVideogames**](VideogamesApi.md#getVideogames) | **GET** /videogames | List videogames |
| [**getVideogamesVideogameIdOrSlug**](VideogamesApi.md#getVideogamesVideogameIdOrSlug) | **GET** /videogames/{videogame_id_or_slug} | Get a videogame |
| [**getVideogamesVideogameIdOrSlugLeagues**](VideogamesApi.md#getVideogamesVideogameIdOrSlugLeagues) | **GET** /videogames/{videogame_id_or_slug}/leagues |  |
| [**getVideogamesVideogameIdOrSlugSeries**](VideogamesApi.md#getVideogamesVideogameIdOrSlugSeries) | **GET** /videogames/{videogame_id_or_slug}/series | List series for a videogame |
| [**getVideogamesVideogameIdOrSlugTournaments**](VideogamesApi.md#getVideogamesVideogameIdOrSlugTournaments) | **GET** /videogames/{videogame_id_or_slug}/tournaments | Get tournaments for a videogame |
| [**getVideogamesVideogameIdOrSlugVersions**](VideogamesApi.md#getVideogamesVideogameIdOrSlugVersions) | **GET** /videogames/{videogame_id_or_slug}/versions | List videogame versions |


<a id="getVideogames"></a>
# **getVideogames**
> List&lt;Videogame&gt; getVideogames(page, perPage)

List videogames

List videogames

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideogamesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pandascore.co");
    
    // Configure HTTP bearer authorization: BearerToken
    HttpBearerAuth BearerToken = (HttpBearerAuth) defaultClient.getAuthentication("BearerToken");
    BearerToken.setBearerToken("BEARER TOKEN");

    // Configure API key authorization: QueryToken
    ApiKeyAuth QueryToken = (ApiKeyAuth) defaultClient.getAuthentication("QueryToken");
    QueryToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryToken.setApiKeyPrefix("Token");

    VideogamesApi apiInstance = new VideogamesApi(defaultClient);
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    try {
      List<Videogame> result = apiInstance.getVideogames(page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideogamesApi#getVideogames");
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
| **page** | [**GetAdditionsPageParameter**](.md)| Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; | [optional] |
| **perPage** | **Integer**| Equivalent to &#x60;page[size]&#x60; | [optional] [default to 50] |

### Return type

[**List&lt;Videogame&gt;**](Videogame.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of videogames |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="getVideogamesVideogameIdOrSlug"></a>
# **getVideogamesVideogameIdOrSlug**
> Videogame getVideogamesVideogameIdOrSlug(videogameIdOrSlug)

Get a videogame

Get a single videogame by ID or by slug

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideogamesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pandascore.co");
    
    // Configure HTTP bearer authorization: BearerToken
    HttpBearerAuth BearerToken = (HttpBearerAuth) defaultClient.getAuthentication("BearerToken");
    BearerToken.setBearerToken("BEARER TOKEN");

    // Configure API key authorization: QueryToken
    ApiKeyAuth QueryToken = (ApiKeyAuth) defaultClient.getAuthentication("QueryToken");
    QueryToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryToken.setApiKeyPrefix("Token");

    VideogamesApi apiInstance = new VideogamesApi(defaultClient);
    VideogameIDOrSlug videogameIdOrSlug = new VideogameIDOrSlug(); // VideogameIDOrSlug | A videogame ID or slug
    try {
      Videogame result = apiInstance.getVideogamesVideogameIdOrSlug(videogameIdOrSlug);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideogamesApi#getVideogamesVideogameIdOrSlug");
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
| **videogameIdOrSlug** | [**VideogameIDOrSlug**](.md)| A videogame ID or slug | |

### Return type

[**Videogame**](Videogame.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A videogame |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="getVideogamesVideogameIdOrSlugLeagues"></a>
# **getVideogamesVideogameIdOrSlugLeagues**
> List&lt;League&gt; getVideogamesVideogameIdOrSlugLeagues(videogameIdOrSlug, search, sort, range, filter, page, perPage)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideogamesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pandascore.co");
    
    // Configure HTTP bearer authorization: BearerToken
    HttpBearerAuth BearerToken = (HttpBearerAuth) defaultClient.getAuthentication("BearerToken");
    BearerToken.setBearerToken("BEARER TOKEN");

    // Configure API key authorization: QueryToken
    ApiKeyAuth QueryToken = (ApiKeyAuth) defaultClient.getAuthentication("QueryToken");
    QueryToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryToken.setApiKeyPrefix("Token");

    VideogamesApi apiInstance = new VideogamesApi(defaultClient);
    VideogameIDOrSlug videogameIdOrSlug = new VideogameIDOrSlug(); // VideogameIDOrSlug | A videogame ID or slug
    SearchOverLeagues search = new SearchOverLeagues(); // SearchOverLeagues | Options to search results
    List<String> sort = Arrays.asList(); // List<String> | Options to sort results
    RangeOverLeagues range = new RangeOverLeagues(); // RangeOverLeagues | Options to select results within ranges
    FilterOverLeagues filter = new FilterOverLeagues(); // FilterOverLeagues | Options to filter results. String fields are case sensitive
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    try {
      List<League> result = apiInstance.getVideogamesVideogameIdOrSlugLeagues(videogameIdOrSlug, search, sort, range, filter, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideogamesApi#getVideogamesVideogameIdOrSlugLeagues");
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
| **videogameIdOrSlug** | [**VideogameIDOrSlug**](.md)| A videogame ID or slug | |
| **search** | [**SearchOverLeagues**](.md)| Options to search results | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| Options to sort results | [optional] [enum: id, -id, modified_at, -modified_at, name, -name, slug, -slug, url, -url] |
| **range** | [**RangeOverLeagues**](.md)| Options to select results within ranges | [optional] |
| **filter** | [**FilterOverLeagues**](.md)| Options to filter results. String fields are case sensitive | [optional] |
| **page** | [**GetAdditionsPageParameter**](.md)| Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; | [optional] |
| **perPage** | **Integer**| Equivalent to &#x60;page[size]&#x60; | [optional] [default to 50] |

### Return type

[**List&lt;League&gt;**](League.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of leagues |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="getVideogamesVideogameIdOrSlugSeries"></a>
# **getVideogamesVideogameIdOrSlugSeries**
> List&lt;Serie&gt; getVideogamesVideogameIdOrSlugSeries(videogameIdOrSlug, filter, search, sort, range, page, perPage)

List series for a videogame

List series for the given videogame

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideogamesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pandascore.co");
    
    // Configure HTTP bearer authorization: BearerToken
    HttpBearerAuth BearerToken = (HttpBearerAuth) defaultClient.getAuthentication("BearerToken");
    BearerToken.setBearerToken("BEARER TOKEN");

    // Configure API key authorization: QueryToken
    ApiKeyAuth QueryToken = (ApiKeyAuth) defaultClient.getAuthentication("QueryToken");
    QueryToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryToken.setApiKeyPrefix("Token");

    VideogamesApi apiInstance = new VideogamesApi(defaultClient);
    VideogameIDOrSlug videogameIdOrSlug = new VideogameIDOrSlug(); // VideogameIDOrSlug | A videogame ID or slug
    FilterOverSeries filter = new FilterOverSeries(); // FilterOverSeries | Options to filter results. String fields are case sensitive
    SearchOverSeries search = new SearchOverSeries(); // SearchOverSeries | Options to search results
    List<String> sort = Arrays.asList(); // List<String> | Options to sort results
    RangeOverSeries range = new RangeOverSeries(); // RangeOverSeries | Options to select results within ranges
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    try {
      List<Serie> result = apiInstance.getVideogamesVideogameIdOrSlugSeries(videogameIdOrSlug, filter, search, sort, range, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideogamesApi#getVideogamesVideogameIdOrSlugSeries");
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
| **videogameIdOrSlug** | [**VideogameIDOrSlug**](.md)| A videogame ID or slug | |
| **filter** | [**FilterOverSeries**](.md)| Options to filter results. String fields are case sensitive | [optional] |
| **search** | [**SearchOverSeries**](.md)| Options to search results | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| Options to sort results | [optional] [enum: begin_at, -begin_at, description, -description, end_at, -end_at, id, -id, league_id, -league_id, modified_at, -modified_at, name, -name, season, -season, slug, -slug, tier, -tier, winner_id, -winner_id, winner_type, -winner_type, year, -year] |
| **range** | [**RangeOverSeries**](.md)| Options to select results within ranges | [optional] |
| **page** | [**GetAdditionsPageParameter**](.md)| Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; | [optional] |
| **perPage** | **Integer**| Equivalent to &#x60;page[size]&#x60; | [optional] [default to 50] |

### Return type

[**List&lt;Serie&gt;**](Serie.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of series |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="getVideogamesVideogameIdOrSlugTournaments"></a>
# **getVideogamesVideogameIdOrSlugTournaments**
> List&lt;ShortTournament&gt; getVideogamesVideogameIdOrSlugTournaments(videogameIdOrSlug, filter, range, sort, search, page, perPage)

Get tournaments for a videogame

List tournaments of the given videogame

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideogamesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pandascore.co");
    
    // Configure HTTP bearer authorization: BearerToken
    HttpBearerAuth BearerToken = (HttpBearerAuth) defaultClient.getAuthentication("BearerToken");
    BearerToken.setBearerToken("BEARER TOKEN");

    // Configure API key authorization: QueryToken
    ApiKeyAuth QueryToken = (ApiKeyAuth) defaultClient.getAuthentication("QueryToken");
    QueryToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryToken.setApiKeyPrefix("Token");

    VideogamesApi apiInstance = new VideogamesApi(defaultClient);
    VideogameIDOrSlug videogameIdOrSlug = new VideogameIDOrSlug(); // VideogameIDOrSlug | A videogame ID or slug
    FilterOverShortTournaments filter = new FilterOverShortTournaments(); // FilterOverShortTournaments | Options to filter results. String fields are case sensitive
    RangeOverShortTournaments range = new RangeOverShortTournaments(); // RangeOverShortTournaments | Options to select results within ranges
    List<String> sort = Arrays.asList(); // List<String> | Options to sort results
    SearchOverShortTournaments search = new SearchOverShortTournaments(); // SearchOverShortTournaments | Options to search results
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    try {
      List<ShortTournament> result = apiInstance.getVideogamesVideogameIdOrSlugTournaments(videogameIdOrSlug, filter, range, sort, search, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideogamesApi#getVideogamesVideogameIdOrSlugTournaments");
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
| **videogameIdOrSlug** | [**VideogameIDOrSlug**](.md)| A videogame ID or slug | |
| **filter** | [**FilterOverShortTournaments**](.md)| Options to filter results. String fields are case sensitive | [optional] |
| **range** | [**RangeOverShortTournaments**](.md)| Options to select results within ranges | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| Options to sort results | [optional] [enum: begin_at, -begin_at, end_at, -end_at, id, -id, modified_at, -modified_at, name, -name, prizepool, -prizepool, serie_id, -serie_id, slug, -slug, winner_id, -winner_id, winner_type, -winner_type] |
| **search** | [**SearchOverShortTournaments**](.md)| Options to search results | [optional] |
| **page** | [**GetAdditionsPageParameter**](.md)| Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; | [optional] |
| **perPage** | **Integer**| Equivalent to &#x60;page[size]&#x60; | [optional] [default to 50] |

### Return type

[**List&lt;ShortTournament&gt;**](ShortTournament.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of tournaments |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="getVideogamesVideogameIdOrSlugVersions"></a>
# **getVideogamesVideogameIdOrSlugVersions**
> List&lt;ShortVideogameVersion&gt; getVideogamesVideogameIdOrSlugVersions(videogameIdOrSlug, filter, range, sort, search, page, perPage)

List videogame versions

List available versions for a given videogame

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideogamesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pandascore.co");
    
    // Configure HTTP bearer authorization: BearerToken
    HttpBearerAuth BearerToken = (HttpBearerAuth) defaultClient.getAuthentication("BearerToken");
    BearerToken.setBearerToken("BEARER TOKEN");

    // Configure API key authorization: QueryToken
    ApiKeyAuth QueryToken = (ApiKeyAuth) defaultClient.getAuthentication("QueryToken");
    QueryToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryToken.setApiKeyPrefix("Token");

    VideogamesApi apiInstance = new VideogamesApi(defaultClient);
    VideogameIDOrSlug videogameIdOrSlug = new VideogameIDOrSlug(); // VideogameIDOrSlug | A videogame ID or slug
    FilterOverShortVideogameVersions filter = new FilterOverShortVideogameVersions(); // FilterOverShortVideogameVersions | Options to filter results. String fields are case sensitive
    RangeOverShortVideogameVersions range = new RangeOverShortVideogameVersions(); // RangeOverShortVideogameVersions | Options to select results within ranges
    List<String> sort = Arrays.asList(); // List<String> | Options to sort results
    SearchOverShortVideogameVersions search = new SearchOverShortVideogameVersions(); // SearchOverShortVideogameVersions | Options to search results
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    try {
      List<ShortVideogameVersion> result = apiInstance.getVideogamesVideogameIdOrSlugVersions(videogameIdOrSlug, filter, range, sort, search, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideogamesApi#getVideogamesVideogameIdOrSlugVersions");
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
| **videogameIdOrSlug** | [**VideogameIDOrSlug**](.md)| A videogame ID or slug | |
| **filter** | [**FilterOverShortVideogameVersions**](.md)| Options to filter results. String fields are case sensitive | [optional] |
| **range** | [**RangeOverShortVideogameVersions**](.md)| Options to select results within ranges | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| Options to sort results | [optional] [enum: current, -current, name, -name] |
| **search** | [**SearchOverShortVideogameVersions**](.md)| Options to search results | [optional] |
| **page** | [**GetAdditionsPageParameter**](.md)| Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; | [optional] |
| **perPage** | **Integer**| Equivalent to &#x60;page[size]&#x60; | [optional] [default to 50] |

### Return type

[**List&lt;ShortVideogameVersion&gt;**](ShortVideogameVersion.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of a videogame&#39;s versions |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **422** | Unprocessable Entity |  -  |

