# LeaguesApi

All URIs are relative to *https://api.pandascore.co*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getLeagues**](LeaguesApi.md#getLeagues) | **GET** /leagues | List leagues |
| [**getLeaguesLeagueIdOrSlug**](LeaguesApi.md#getLeaguesLeagueIdOrSlug) | **GET** /leagues/{league_id_or_slug} | Get a league |
| [**getLeaguesLeagueIdOrSlugMatches**](LeaguesApi.md#getLeaguesLeagueIdOrSlugMatches) | **GET** /leagues/{league_id_or_slug}/matches | Get matches for a league |
| [**getLeaguesLeagueIdOrSlugMatchesPast**](LeaguesApi.md#getLeaguesLeagueIdOrSlugMatchesPast) | **GET** /leagues/{league_id_or_slug}/matches/past | Get past matches for league |
| [**getLeaguesLeagueIdOrSlugMatchesRunning**](LeaguesApi.md#getLeaguesLeagueIdOrSlugMatchesRunning) | **GET** /leagues/{league_id_or_slug}/matches/running | Get running matches for league |
| [**getLeaguesLeagueIdOrSlugMatchesUpcoming**](LeaguesApi.md#getLeaguesLeagueIdOrSlugMatchesUpcoming) | **GET** /leagues/{league_id_or_slug}/matches/upcoming | Get upcoming matches for league |
| [**getLeaguesLeagueIdOrSlugSeries**](LeaguesApi.md#getLeaguesLeagueIdOrSlugSeries) | **GET** /leagues/{league_id_or_slug}/series | List series of a league |
| [**getLeaguesLeagueIdOrSlugTournaments**](LeaguesApi.md#getLeaguesLeagueIdOrSlugTournaments) | **GET** /leagues/{league_id_or_slug}/tournaments | Get tournaments for a league |


<a id="getLeagues"></a>
# **getLeagues**
> List&lt;League&gt; getLeagues(search, sort, range, filter, page, perPage)

List leagues

List leagues

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LeaguesApi;

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

    LeaguesApi apiInstance = new LeaguesApi(defaultClient);
    SearchOverLeagues search = new SearchOverLeagues(); // SearchOverLeagues | Options to search results
    List<String> sort = Arrays.asList(); // List<String> | Options to sort results
    RangeOverLeagues range = new RangeOverLeagues(); // RangeOverLeagues | Options to select results within ranges
    FilterOverLeagues filter = new FilterOverLeagues(); // FilterOverLeagues | Options to filter results. String fields are case sensitive
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    try {
      List<League> result = apiInstance.getLeagues(search, sort, range, filter, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LeaguesApi#getLeagues");
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

<a id="getLeaguesLeagueIdOrSlug"></a>
# **getLeaguesLeagueIdOrSlug**
> League getLeaguesLeagueIdOrSlug(leagueIdOrSlug)

Get a league

Get a single league by ID or by slug

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LeaguesApi;

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

    LeaguesApi apiInstance = new LeaguesApi(defaultClient);
    LeagueIDOrSlug leagueIdOrSlug = new LeagueIDOrSlug(); // LeagueIDOrSlug | A league ID or slug
    try {
      League result = apiInstance.getLeaguesLeagueIdOrSlug(leagueIdOrSlug);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LeaguesApi#getLeaguesLeagueIdOrSlug");
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
| **leagueIdOrSlug** | [**LeagueIDOrSlug**](.md)| A league ID or slug | |

### Return type

[**League**](League.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A league |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="getLeaguesLeagueIdOrSlugMatches"></a>
# **getLeaguesLeagueIdOrSlugMatches**
> List&lt;Match&gt; getLeaguesLeagueIdOrSlugMatches(leagueIdOrSlug, filter, search, sort, range, page, perPage)

Get matches for a league

List matches of the given league

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LeaguesApi;

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

    LeaguesApi apiInstance = new LeaguesApi(defaultClient);
    LeagueIDOrSlug leagueIdOrSlug = new LeagueIDOrSlug(); // LeagueIDOrSlug | A league ID or slug
    FilterOverMatches filter = new FilterOverMatches(); // FilterOverMatches | Options to filter results. String fields are case sensitive
    SearchOverMatches search = new SearchOverMatches(); // SearchOverMatches | Options to search results
    List<String> sort = Arrays.asList(); // List<String> | Options to sort results
    RangeOverMatches range = new RangeOverMatches(); // RangeOverMatches | Options to select results within ranges
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    try {
      List<Match> result = apiInstance.getLeaguesLeagueIdOrSlugMatches(leagueIdOrSlug, filter, search, sort, range, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LeaguesApi#getLeaguesLeagueIdOrSlugMatches");
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
| **leagueIdOrSlug** | [**LeagueIDOrSlug**](.md)| A league ID or slug | |
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

<a id="getLeaguesLeagueIdOrSlugMatchesPast"></a>
# **getLeaguesLeagueIdOrSlugMatchesPast**
> List&lt;Match&gt; getLeaguesLeagueIdOrSlugMatchesPast(leagueIdOrSlug, filter, search, sort, range, page, perPage)

Get past matches for league

List past matches for the given league

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LeaguesApi;

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

    LeaguesApi apiInstance = new LeaguesApi(defaultClient);
    LeagueIDOrSlug leagueIdOrSlug = new LeagueIDOrSlug(); // LeagueIDOrSlug | A league ID or slug
    FilterOverMatches filter = new FilterOverMatches(); // FilterOverMatches | Options to filter results. String fields are case sensitive
    SearchOverMatches search = new SearchOverMatches(); // SearchOverMatches | Options to search results
    List<String> sort = Arrays.asList(); // List<String> | Options to sort results
    RangeOverMatches range = new RangeOverMatches(); // RangeOverMatches | Options to select results within ranges
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    try {
      List<Match> result = apiInstance.getLeaguesLeagueIdOrSlugMatchesPast(leagueIdOrSlug, filter, search, sort, range, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LeaguesApi#getLeaguesLeagueIdOrSlugMatchesPast");
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
| **leagueIdOrSlug** | [**LeagueIDOrSlug**](.md)| A league ID or slug | |
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

<a id="getLeaguesLeagueIdOrSlugMatchesRunning"></a>
# **getLeaguesLeagueIdOrSlugMatchesRunning**
> List&lt;Match&gt; getLeaguesLeagueIdOrSlugMatchesRunning(leagueIdOrSlug, filter, search, sort, range, page, perPage)

Get running matches for league

List currently running matches for the given league

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LeaguesApi;

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

    LeaguesApi apiInstance = new LeaguesApi(defaultClient);
    LeagueIDOrSlug leagueIdOrSlug = new LeagueIDOrSlug(); // LeagueIDOrSlug | A league ID or slug
    FilterOverMatches filter = new FilterOverMatches(); // FilterOverMatches | Options to filter results. String fields are case sensitive
    SearchOverMatches search = new SearchOverMatches(); // SearchOverMatches | Options to search results
    List<String> sort = Arrays.asList(); // List<String> | Options to sort results
    RangeOverMatches range = new RangeOverMatches(); // RangeOverMatches | Options to select results within ranges
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    try {
      List<Match> result = apiInstance.getLeaguesLeagueIdOrSlugMatchesRunning(leagueIdOrSlug, filter, search, sort, range, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LeaguesApi#getLeaguesLeagueIdOrSlugMatchesRunning");
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
| **leagueIdOrSlug** | [**LeagueIDOrSlug**](.md)| A league ID or slug | |
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

<a id="getLeaguesLeagueIdOrSlugMatchesUpcoming"></a>
# **getLeaguesLeagueIdOrSlugMatchesUpcoming**
> List&lt;Match&gt; getLeaguesLeagueIdOrSlugMatchesUpcoming(leagueIdOrSlug, filter, search, sort, range, page, perPage)

Get upcoming matches for league

List upcoming matches for the given league

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LeaguesApi;

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

    LeaguesApi apiInstance = new LeaguesApi(defaultClient);
    LeagueIDOrSlug leagueIdOrSlug = new LeagueIDOrSlug(); // LeagueIDOrSlug | A league ID or slug
    FilterOverMatches filter = new FilterOverMatches(); // FilterOverMatches | Options to filter results. String fields are case sensitive
    SearchOverMatches search = new SearchOverMatches(); // SearchOverMatches | Options to search results
    List<String> sort = Arrays.asList(); // List<String> | Options to sort results
    RangeOverMatches range = new RangeOverMatches(); // RangeOverMatches | Options to select results within ranges
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    try {
      List<Match> result = apiInstance.getLeaguesLeagueIdOrSlugMatchesUpcoming(leagueIdOrSlug, filter, search, sort, range, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LeaguesApi#getLeaguesLeagueIdOrSlugMatchesUpcoming");
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
| **leagueIdOrSlug** | [**LeagueIDOrSlug**](.md)| A league ID or slug | |
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

<a id="getLeaguesLeagueIdOrSlugSeries"></a>
# **getLeaguesLeagueIdOrSlugSeries**
> List&lt;Serie&gt; getLeaguesLeagueIdOrSlugSeries(leagueIdOrSlug, filter, search, sort, range, page, perPage)

List series of a league

List series for the given league

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LeaguesApi;

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

    LeaguesApi apiInstance = new LeaguesApi(defaultClient);
    LeagueIDOrSlug leagueIdOrSlug = new LeagueIDOrSlug(); // LeagueIDOrSlug | A league ID or slug
    FilterOverSeries filter = new FilterOverSeries(); // FilterOverSeries | Options to filter results. String fields are case sensitive
    SearchOverSeries search = new SearchOverSeries(); // SearchOverSeries | Options to search results
    List<String> sort = Arrays.asList(); // List<String> | Options to sort results
    RangeOverSeries range = new RangeOverSeries(); // RangeOverSeries | Options to select results within ranges
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    try {
      List<Serie> result = apiInstance.getLeaguesLeagueIdOrSlugSeries(leagueIdOrSlug, filter, search, sort, range, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LeaguesApi#getLeaguesLeagueIdOrSlugSeries");
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
| **leagueIdOrSlug** | [**LeagueIDOrSlug**](.md)| A league ID or slug | |
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

<a id="getLeaguesLeagueIdOrSlugTournaments"></a>
# **getLeaguesLeagueIdOrSlugTournaments**
> List&lt;ShortTournament&gt; getLeaguesLeagueIdOrSlugTournaments(leagueIdOrSlug, filter, search, sort, range, page, perPage)

Get tournaments for a league

List tournaments of the given league

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LeaguesApi;

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

    LeaguesApi apiInstance = new LeaguesApi(defaultClient);
    LeagueIDOrSlug leagueIdOrSlug = new LeagueIDOrSlug(); // LeagueIDOrSlug | A league ID or slug
    FilterOverShortTournaments filter = new FilterOverShortTournaments(); // FilterOverShortTournaments | Options to filter results. String fields are case sensitive
    SearchOverShortTournaments search = new SearchOverShortTournaments(); // SearchOverShortTournaments | Options to search results
    List<String> sort = Arrays.asList(); // List<String> | Options to sort results
    RangeOverShortTournaments range = new RangeOverShortTournaments(); // RangeOverShortTournaments | Options to select results within ranges
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    try {
      List<ShortTournament> result = apiInstance.getLeaguesLeagueIdOrSlugTournaments(leagueIdOrSlug, filter, search, sort, range, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LeaguesApi#getLeaguesLeagueIdOrSlugTournaments");
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
| **leagueIdOrSlug** | [**LeagueIDOrSlug**](.md)| A league ID or slug | |
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

