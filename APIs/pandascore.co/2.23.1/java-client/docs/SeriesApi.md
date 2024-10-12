# SeriesApi

All URIs are relative to *https://api.pandascore.co*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSeries**](SeriesApi.md#getSeries) | **GET** /series | List series |
| [**getSeriesPast**](SeriesApi.md#getSeriesPast) | **GET** /series/past | Get past series |
| [**getSeriesRunning**](SeriesApi.md#getSeriesRunning) | **GET** /series/running | Get running series |
| [**getSeriesSerieIdOrSlug**](SeriesApi.md#getSeriesSerieIdOrSlug) | **GET** /series/{serie_id_or_slug} | Get a serie |
| [**getSeriesSerieIdOrSlugMatches**](SeriesApi.md#getSeriesSerieIdOrSlugMatches) | **GET** /series/{serie_id_or_slug}/matches | Get matches for a serie |
| [**getSeriesSerieIdOrSlugMatchesPast**](SeriesApi.md#getSeriesSerieIdOrSlugMatchesPast) | **GET** /series/{serie_id_or_slug}/matches/past | Get past matches for serie |
| [**getSeriesSerieIdOrSlugMatchesRunning**](SeriesApi.md#getSeriesSerieIdOrSlugMatchesRunning) | **GET** /series/{serie_id_or_slug}/matches/running | Get running matches for serie |
| [**getSeriesSerieIdOrSlugMatchesUpcoming**](SeriesApi.md#getSeriesSerieIdOrSlugMatchesUpcoming) | **GET** /series/{serie_id_or_slug}/matches/upcoming | Get upcoming matches for serie |
| [**getSeriesSerieIdOrSlugPlayers**](SeriesApi.md#getSeriesSerieIdOrSlugPlayers) | **GET** /series/{serie_id_or_slug}/players | Get players for a serie |
| [**getSeriesSerieIdOrSlugTournaments**](SeriesApi.md#getSeriesSerieIdOrSlugTournaments) | **GET** /series/{serie_id_or_slug}/tournaments | Get tournaments for a serie |
| [**getSeriesUpcoming**](SeriesApi.md#getSeriesUpcoming) | **GET** /series/upcoming | Get upcoming series |


<a id="getSeries"></a>
# **getSeries**
> List&lt;Serie&gt; getSeries(filter, search, sort, range, page, perPage)

List series

List series

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SeriesApi;

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

    SeriesApi apiInstance = new SeriesApi(defaultClient);
    FilterOverSeries filter = new FilterOverSeries(); // FilterOverSeries | Options to filter results. String fields are case sensitive
    SearchOverSeries search = new SearchOverSeries(); // SearchOverSeries | Options to search results
    List<String> sort = Arrays.asList(); // List<String> | Options to sort results
    RangeOverSeries range = new RangeOverSeries(); // RangeOverSeries | Options to select results within ranges
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    try {
      List<Serie> result = apiInstance.getSeries(filter, search, sort, range, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SeriesApi#getSeries");
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

<a id="getSeriesPast"></a>
# **getSeriesPast**
> List&lt;Serie&gt; getSeriesPast(filter, search, sort, range, page, perPage)

Get past series

List past series

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SeriesApi;

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

    SeriesApi apiInstance = new SeriesApi(defaultClient);
    FilterOverSeries filter = new FilterOverSeries(); // FilterOverSeries | Options to filter results. String fields are case sensitive
    SearchOverSeries search = new SearchOverSeries(); // SearchOverSeries | Options to search results
    List<String> sort = Arrays.asList(); // List<String> | Options to sort results
    RangeOverSeries range = new RangeOverSeries(); // RangeOverSeries | Options to select results within ranges
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    try {
      List<Serie> result = apiInstance.getSeriesPast(filter, search, sort, range, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SeriesApi#getSeriesPast");
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

<a id="getSeriesRunning"></a>
# **getSeriesRunning**
> List&lt;Serie&gt; getSeriesRunning(filter, search, sort, range, page, perPage)

Get running series

List currently running series

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SeriesApi;

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

    SeriesApi apiInstance = new SeriesApi(defaultClient);
    FilterOverSeries filter = new FilterOverSeries(); // FilterOverSeries | Options to filter results. String fields are case sensitive
    SearchOverSeries search = new SearchOverSeries(); // SearchOverSeries | Options to search results
    List<String> sort = Arrays.asList(); // List<String> | Options to sort results
    RangeOverSeries range = new RangeOverSeries(); // RangeOverSeries | Options to select results within ranges
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    try {
      List<Serie> result = apiInstance.getSeriesRunning(filter, search, sort, range, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SeriesApi#getSeriesRunning");
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

<a id="getSeriesSerieIdOrSlug"></a>
# **getSeriesSerieIdOrSlug**
> Serie getSeriesSerieIdOrSlug(serieIdOrSlug)

Get a serie

Get a single serie by ID or by slug

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SeriesApi;

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

    SeriesApi apiInstance = new SeriesApi(defaultClient);
    SerieIDOrSlug serieIdOrSlug = new SerieIDOrSlug(); // SerieIDOrSlug | A serie ID or slug
    try {
      Serie result = apiInstance.getSeriesSerieIdOrSlug(serieIdOrSlug);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SeriesApi#getSeriesSerieIdOrSlug");
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
| **serieIdOrSlug** | [**SerieIDOrSlug**](.md)| A serie ID or slug | |

### Return type

[**Serie**](Serie.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A serie |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="getSeriesSerieIdOrSlugMatches"></a>
# **getSeriesSerieIdOrSlugMatches**
> List&lt;Match&gt; getSeriesSerieIdOrSlugMatches(serieIdOrSlug, filter, search, sort, range, page, perPage)

Get matches for a serie

List matches of the given serie

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SeriesApi;

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

    SeriesApi apiInstance = new SeriesApi(defaultClient);
    SerieIDOrSlug serieIdOrSlug = new SerieIDOrSlug(); // SerieIDOrSlug | A serie ID or slug
    FilterOverMatches filter = new FilterOverMatches(); // FilterOverMatches | Options to filter results. String fields are case sensitive
    SearchOverMatches search = new SearchOverMatches(); // SearchOverMatches | Options to search results
    List<String> sort = Arrays.asList(); // List<String> | Options to sort results
    RangeOverMatches range = new RangeOverMatches(); // RangeOverMatches | Options to select results within ranges
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    try {
      List<Match> result = apiInstance.getSeriesSerieIdOrSlugMatches(serieIdOrSlug, filter, search, sort, range, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SeriesApi#getSeriesSerieIdOrSlugMatches");
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
| **serieIdOrSlug** | [**SerieIDOrSlug**](.md)| A serie ID or slug | |
| **filter** | [**FilterOverMatches**](.md)| Options to filter results. String fields are case sensitive | [optional] |
| **search** | [**SearchOverMatches**](.md)| Options to search results | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| Options to sort results | [optional] [enum: begin_at, -begin_at, detailed_stats, -detailed_stats, draw, -draw, end_at, -end_at, forfeit, -forfeit, id, -id, match_type, -match_type, modified_at, -modified_at, name, -name, number_of_games, -number_of_games, scheduled_at, -scheduled_at, slug, -slug, status, -status, tournament_id, -tournament_id, winner_id, -winner_id] |
| **range** | [**RangeOverMatches**](.md)| Options to select results within ranges | [optional] |
| **page** | [**GetAdditionsPageParameter**](.md)| Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; | [optional] |
| **perPage** | **Integer**| Equivalent to &#x60;page[size]&#x60; | [optional] [default to 50] |

### Return type

[**List&lt;Match&gt;**](Match.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of matches of any e-sport |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="getSeriesSerieIdOrSlugMatchesPast"></a>
# **getSeriesSerieIdOrSlugMatchesPast**
> List&lt;Match&gt; getSeriesSerieIdOrSlugMatchesPast(serieIdOrSlug, filter, search, sort, range, page, perPage)

Get past matches for serie

List past matches for the given serie

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SeriesApi;

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

    SeriesApi apiInstance = new SeriesApi(defaultClient);
    SerieIDOrSlug serieIdOrSlug = new SerieIDOrSlug(); // SerieIDOrSlug | A serie ID or slug
    FilterOverMatches filter = new FilterOverMatches(); // FilterOverMatches | Options to filter results. String fields are case sensitive
    SearchOverMatches search = new SearchOverMatches(); // SearchOverMatches | Options to search results
    List<String> sort = Arrays.asList(); // List<String> | Options to sort results
    RangeOverMatches range = new RangeOverMatches(); // RangeOverMatches | Options to select results within ranges
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    try {
      List<Match> result = apiInstance.getSeriesSerieIdOrSlugMatchesPast(serieIdOrSlug, filter, search, sort, range, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SeriesApi#getSeriesSerieIdOrSlugMatchesPast");
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
| **serieIdOrSlug** | [**SerieIDOrSlug**](.md)| A serie ID or slug | |
| **filter** | [**FilterOverMatches**](.md)| Options to filter results. String fields are case sensitive | [optional] |
| **search** | [**SearchOverMatches**](.md)| Options to search results | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| Options to sort results | [optional] [enum: begin_at, -begin_at, detailed_stats, -detailed_stats, draw, -draw, end_at, -end_at, forfeit, -forfeit, id, -id, match_type, -match_type, modified_at, -modified_at, name, -name, number_of_games, -number_of_games, scheduled_at, -scheduled_at, slug, -slug, status, -status, tournament_id, -tournament_id, winner_id, -winner_id] |
| **range** | [**RangeOverMatches**](.md)| Options to select results within ranges | [optional] |
| **page** | [**GetAdditionsPageParameter**](.md)| Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; | [optional] |
| **perPage** | **Integer**| Equivalent to &#x60;page[size]&#x60; | [optional] [default to 50] |

### Return type

[**List&lt;Match&gt;**](Match.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of matches of any e-sport |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="getSeriesSerieIdOrSlugMatchesRunning"></a>
# **getSeriesSerieIdOrSlugMatchesRunning**
> List&lt;Match&gt; getSeriesSerieIdOrSlugMatchesRunning(serieIdOrSlug, filter, search, sort, range, page, perPage)

Get running matches for serie

List currently running matches for the given serie

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SeriesApi;

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

    SeriesApi apiInstance = new SeriesApi(defaultClient);
    SerieIDOrSlug serieIdOrSlug = new SerieIDOrSlug(); // SerieIDOrSlug | A serie ID or slug
    FilterOverMatches filter = new FilterOverMatches(); // FilterOverMatches | Options to filter results. String fields are case sensitive
    SearchOverMatches search = new SearchOverMatches(); // SearchOverMatches | Options to search results
    List<String> sort = Arrays.asList(); // List<String> | Options to sort results
    RangeOverMatches range = new RangeOverMatches(); // RangeOverMatches | Options to select results within ranges
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    try {
      List<Match> result = apiInstance.getSeriesSerieIdOrSlugMatchesRunning(serieIdOrSlug, filter, search, sort, range, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SeriesApi#getSeriesSerieIdOrSlugMatchesRunning");
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
| **serieIdOrSlug** | [**SerieIDOrSlug**](.md)| A serie ID or slug | |
| **filter** | [**FilterOverMatches**](.md)| Options to filter results. String fields are case sensitive | [optional] |
| **search** | [**SearchOverMatches**](.md)| Options to search results | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| Options to sort results | [optional] [enum: begin_at, -begin_at, detailed_stats, -detailed_stats, draw, -draw, end_at, -end_at, forfeit, -forfeit, id, -id, match_type, -match_type, modified_at, -modified_at, name, -name, number_of_games, -number_of_games, scheduled_at, -scheduled_at, slug, -slug, status, -status, tournament_id, -tournament_id, winner_id, -winner_id] |
| **range** | [**RangeOverMatches**](.md)| Options to select results within ranges | [optional] |
| **page** | [**GetAdditionsPageParameter**](.md)| Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; | [optional] |
| **perPage** | **Integer**| Equivalent to &#x60;page[size]&#x60; | [optional] [default to 50] |

### Return type

[**List&lt;Match&gt;**](Match.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of matches of any e-sport |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="getSeriesSerieIdOrSlugMatchesUpcoming"></a>
# **getSeriesSerieIdOrSlugMatchesUpcoming**
> List&lt;Match&gt; getSeriesSerieIdOrSlugMatchesUpcoming(serieIdOrSlug, filter, search, sort, range, page, perPage)

Get upcoming matches for serie

List upcoming matches for the given serie

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SeriesApi;

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

    SeriesApi apiInstance = new SeriesApi(defaultClient);
    SerieIDOrSlug serieIdOrSlug = new SerieIDOrSlug(); // SerieIDOrSlug | A serie ID or slug
    FilterOverMatches filter = new FilterOverMatches(); // FilterOverMatches | Options to filter results. String fields are case sensitive
    SearchOverMatches search = new SearchOverMatches(); // SearchOverMatches | Options to search results
    List<String> sort = Arrays.asList(); // List<String> | Options to sort results
    RangeOverMatches range = new RangeOverMatches(); // RangeOverMatches | Options to select results within ranges
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    try {
      List<Match> result = apiInstance.getSeriesSerieIdOrSlugMatchesUpcoming(serieIdOrSlug, filter, search, sort, range, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SeriesApi#getSeriesSerieIdOrSlugMatchesUpcoming");
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
| **serieIdOrSlug** | [**SerieIDOrSlug**](.md)| A serie ID or slug | |
| **filter** | [**FilterOverMatches**](.md)| Options to filter results. String fields are case sensitive | [optional] |
| **search** | [**SearchOverMatches**](.md)| Options to search results | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| Options to sort results | [optional] [enum: begin_at, -begin_at, detailed_stats, -detailed_stats, draw, -draw, end_at, -end_at, forfeit, -forfeit, id, -id, match_type, -match_type, modified_at, -modified_at, name, -name, number_of_games, -number_of_games, scheduled_at, -scheduled_at, slug, -slug, status, -status, tournament_id, -tournament_id, winner_id, -winner_id] |
| **range** | [**RangeOverMatches**](.md)| Options to select results within ranges | [optional] |
| **page** | [**GetAdditionsPageParameter**](.md)| Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; | [optional] |
| **perPage** | **Integer**| Equivalent to &#x60;page[size]&#x60; | [optional] [default to 50] |

### Return type

[**List&lt;Match&gt;**](Match.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of matches of any e-sport |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="getSeriesSerieIdOrSlugPlayers"></a>
# **getSeriesSerieIdOrSlugPlayers**
> List&lt;Player&gt; getSeriesSerieIdOrSlugPlayers(serieIdOrSlug, filter, search, sort, range, page, perPage)

Get players for a serie

List players for the given serie

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SeriesApi;

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

    SeriesApi apiInstance = new SeriesApi(defaultClient);
    String serieIdOrSlug = "serieIdOrSlug_example"; // String | Automatically added
    FilterOverPlayers filter = new FilterOverPlayers(); // FilterOverPlayers | Options to filter results. String fields are case sensitive
    SearchOverPlayers search = new SearchOverPlayers(); // SearchOverPlayers | Options to search results
    List<String> sort = Arrays.asList(); // List<String> | Options to sort results
    RangeOverPlayers range = new RangeOverPlayers(); // RangeOverPlayers | Options to select results within ranges
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    try {
      List<Player> result = apiInstance.getSeriesSerieIdOrSlugPlayers(serieIdOrSlug, filter, search, sort, range, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SeriesApi#getSeriesSerieIdOrSlugPlayers");
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
| **serieIdOrSlug** | **String**| Automatically added | |
| **filter** | [**FilterOverPlayers**](.md)| Options to filter results. String fields are case sensitive | [optional] |
| **search** | [**SearchOverPlayers**](.md)| Options to search results | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| Options to sort results | [optional] [enum: birth_year, -birth_year, birthday, -birthday, first_name, -first_name, hometown, -hometown, id, -id, last_name, -last_name, name, -name, nationality, -nationality, role, -role, slug, -slug, videogame_id, -videogame_id, team_id, -team_id] |
| **range** | [**RangeOverPlayers**](.md)| Options to select results within ranges | [optional] |
| **page** | [**GetAdditionsPageParameter**](.md)| Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; | [optional] |
| **perPage** | **Integer**| Equivalent to &#x60;page[size]&#x60; | [optional] [default to 50] |

### Return type

[**List&lt;Player&gt;**](Player.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of players |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="getSeriesSerieIdOrSlugTournaments"></a>
# **getSeriesSerieIdOrSlugTournaments**
> List&lt;ShortTournament&gt; getSeriesSerieIdOrSlugTournaments(serieIdOrSlug, filter, search, sort, range, page, perPage)

Get tournaments for a serie

List tournaments of the given serie

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SeriesApi;

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

    SeriesApi apiInstance = new SeriesApi(defaultClient);
    SerieIDOrSlug serieIdOrSlug = new SerieIDOrSlug(); // SerieIDOrSlug | A serie ID or slug
    FilterOverShortTournaments filter = new FilterOverShortTournaments(); // FilterOverShortTournaments | Options to filter results. String fields are case sensitive
    SearchOverShortTournaments search = new SearchOverShortTournaments(); // SearchOverShortTournaments | Options to search results
    List<String> sort = Arrays.asList(); // List<String> | Options to sort results
    RangeOverShortTournaments range = new RangeOverShortTournaments(); // RangeOverShortTournaments | Options to select results within ranges
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    try {
      List<ShortTournament> result = apiInstance.getSeriesSerieIdOrSlugTournaments(serieIdOrSlug, filter, search, sort, range, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SeriesApi#getSeriesSerieIdOrSlugTournaments");
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
| **serieIdOrSlug** | [**SerieIDOrSlug**](.md)| A serie ID or slug | |
| **filter** | [**FilterOverShortTournaments**](.md)| Options to filter results. String fields are case sensitive | [optional] |
| **search** | [**SearchOverShortTournaments**](.md)| Options to search results | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| Options to sort results | [optional] [enum: begin_at, -begin_at, end_at, -end_at, id, -id, modified_at, -modified_at, name, -name, prizepool, -prizepool, serie_id, -serie_id, slug, -slug, winner_id, -winner_id, winner_type, -winner_type] |
| **range** | [**RangeOverShortTournaments**](.md)| Options to select results within ranges | [optional] |
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

<a id="getSeriesUpcoming"></a>
# **getSeriesUpcoming**
> List&lt;Serie&gt; getSeriesUpcoming(filter, search, sort, range, page, perPage)

Get upcoming series

List upcoming series

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SeriesApi;

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

    SeriesApi apiInstance = new SeriesApi(defaultClient);
    FilterOverSeries filter = new FilterOverSeries(); // FilterOverSeries | Options to filter results. String fields are case sensitive
    SearchOverSeries search = new SearchOverSeries(); // SearchOverSeries | Options to search results
    List<String> sort = Arrays.asList(); // List<String> | Options to sort results
    RangeOverSeries range = new RangeOverSeries(); // RangeOverSeries | Options to select results within ranges
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    try {
      List<Serie> result = apiInstance.getSeriesUpcoming(filter, search, sort, range, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SeriesApi#getSeriesUpcoming");
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

