# TournamentsApi

All URIs are relative to *https://api.pandascore.co*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getTournaments**](TournamentsApi.md#getTournaments) | **GET** /tournaments | List tournaments |
| [**getTournamentsPast**](TournamentsApi.md#getTournamentsPast) | **GET** /tournaments/past | Get past tournaments |
| [**getTournamentsRunning**](TournamentsApi.md#getTournamentsRunning) | **GET** /tournaments/running | Get running tournaments |
| [**getTournamentsTournamentIdOrSlug**](TournamentsApi.md#getTournamentsTournamentIdOrSlug) | **GET** /tournaments/{tournament_id_or_slug} | Get a tournament |
| [**getTournamentsTournamentIdOrSlugBrackets**](TournamentsApi.md#getTournamentsTournamentIdOrSlugBrackets) | **GET** /tournaments/{tournament_id_or_slug}/brackets | Get a tournament&#39;s brackets |
| [**getTournamentsTournamentIdOrSlugMatches**](TournamentsApi.md#getTournamentsTournamentIdOrSlugMatches) | **GET** /tournaments/{tournament_id_or_slug}/matches | Get matches for tournament |
| [**getTournamentsTournamentIdOrSlugPlayers**](TournamentsApi.md#getTournamentsTournamentIdOrSlugPlayers) | **GET** /tournaments/{tournament_id_or_slug}/players | Get players for a tournament |
| [**getTournamentsTournamentIdOrSlugRosters**](TournamentsApi.md#getTournamentsTournamentIdOrSlugRosters) | **GET** /tournaments/{tournament_id_or_slug}/rosters | Get rosters for a tournament |
| [**getTournamentsTournamentIdOrSlugStandings**](TournamentsApi.md#getTournamentsTournamentIdOrSlugStandings) | **GET** /tournaments/{tournament_id_or_slug}/standings | Get tournament standings |
| [**getTournamentsTournamentIdOrSlugTeams**](TournamentsApi.md#getTournamentsTournamentIdOrSlugTeams) | **GET** /tournaments/{tournament_id_or_slug}/teams | Get teams for a tournament |
| [**getTournamentsUpcoming**](TournamentsApi.md#getTournamentsUpcoming) | **GET** /tournaments/upcoming | Get upcoming tournaments |


<a id="getTournaments"></a>
# **getTournaments**
> List&lt;ShortTournament&gt; getTournaments(filter, search, sort, range, page, perPage)

List tournaments

List tournaments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TournamentsApi;

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

    TournamentsApi apiInstance = new TournamentsApi(defaultClient);
    FilterOverShortTournaments filter = new FilterOverShortTournaments(); // FilterOverShortTournaments | Options to filter results. String fields are case sensitive
    SearchOverShortTournaments search = new SearchOverShortTournaments(); // SearchOverShortTournaments | Options to search results
    List<String> sort = Arrays.asList(); // List<String> | Options to sort results
    RangeOverShortTournaments range = new RangeOverShortTournaments(); // RangeOverShortTournaments | Options to select results within ranges
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    try {
      List<ShortTournament> result = apiInstance.getTournaments(filter, search, sort, range, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TournamentsApi#getTournaments");
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

<a id="getTournamentsPast"></a>
# **getTournamentsPast**
> List&lt;ShortTournament&gt; getTournamentsPast(filter, search, sort, range, page, perPage)

Get past tournaments

List past tournaments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TournamentsApi;

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

    TournamentsApi apiInstance = new TournamentsApi(defaultClient);
    FilterOverShortTournaments filter = new FilterOverShortTournaments(); // FilterOverShortTournaments | Options to filter results. String fields are case sensitive
    SearchOverShortTournaments search = new SearchOverShortTournaments(); // SearchOverShortTournaments | Options to search results
    List<String> sort = Arrays.asList(); // List<String> | Options to sort results
    RangeOverShortTournaments range = new RangeOverShortTournaments(); // RangeOverShortTournaments | Options to select results within ranges
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    try {
      List<ShortTournament> result = apiInstance.getTournamentsPast(filter, search, sort, range, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TournamentsApi#getTournamentsPast");
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

<a id="getTournamentsRunning"></a>
# **getTournamentsRunning**
> List&lt;ShortTournament&gt; getTournamentsRunning(filter, search, sort, range, page, perPage)

Get running tournaments

List currently running tournaments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TournamentsApi;

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

    TournamentsApi apiInstance = new TournamentsApi(defaultClient);
    FilterOverShortTournaments filter = new FilterOverShortTournaments(); // FilterOverShortTournaments | Options to filter results. String fields are case sensitive
    SearchOverShortTournaments search = new SearchOverShortTournaments(); // SearchOverShortTournaments | Options to search results
    List<String> sort = Arrays.asList(); // List<String> | Options to sort results
    RangeOverShortTournaments range = new RangeOverShortTournaments(); // RangeOverShortTournaments | Options to select results within ranges
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    try {
      List<ShortTournament> result = apiInstance.getTournamentsRunning(filter, search, sort, range, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TournamentsApi#getTournamentsRunning");
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

<a id="getTournamentsTournamentIdOrSlug"></a>
# **getTournamentsTournamentIdOrSlug**
> Tournament getTournamentsTournamentIdOrSlug(tournamentIdOrSlug)

Get a tournament

Get a single tournament by ID or by slug

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TournamentsApi;

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

    TournamentsApi apiInstance = new TournamentsApi(defaultClient);
    TournamentIDOrSlug tournamentIdOrSlug = new TournamentIDOrSlug(); // TournamentIDOrSlug | A tournament ID or slug
    try {
      Tournament result = apiInstance.getTournamentsTournamentIdOrSlug(tournamentIdOrSlug);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TournamentsApi#getTournamentsTournamentIdOrSlug");
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
| **tournamentIdOrSlug** | [**TournamentIDOrSlug**](.md)| A tournament ID or slug | |

### Return type

[**Tournament**](Tournament.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A detailed tournament |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="getTournamentsTournamentIdOrSlugBrackets"></a>
# **getTournamentsTournamentIdOrSlugBrackets**
> List&lt;Bracket&gt; getTournamentsTournamentIdOrSlugBrackets(tournamentIdOrSlug, filter, range, sort, search, page, perPage)

Get a tournament&#39;s brackets

Get the brackets of the given tournament

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TournamentsApi;

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

    TournamentsApi apiInstance = new TournamentsApi(defaultClient);
    TournamentIDOrSlug tournamentIdOrSlug = new TournamentIDOrSlug(); // TournamentIDOrSlug | A tournament ID or slug
    FilterOverBrackets filter = new FilterOverBrackets(); // FilterOverBrackets | Options to filter results. String fields are case sensitive
    RangeOverBrackets range = new RangeOverBrackets(); // RangeOverBrackets | Options to select results within ranges
    List<String> sort = Arrays.asList(); // List<String> | Options to sort results
    SearchOverBrackets search = new SearchOverBrackets(); // SearchOverBrackets | Options to search results
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    try {
      List<Bracket> result = apiInstance.getTournamentsTournamentIdOrSlugBrackets(tournamentIdOrSlug, filter, range, sort, search, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TournamentsApi#getTournamentsTournamentIdOrSlugBrackets");
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
| **tournamentIdOrSlug** | [**TournamentIDOrSlug**](.md)| A tournament ID or slug | |
| **filter** | [**FilterOverBrackets**](.md)| Options to filter results. String fields are case sensitive | [optional] |
| **range** | [**RangeOverBrackets**](.md)| Options to select results within ranges | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| Options to sort results | [optional] [enum: begin_at, -begin_at, detailed_stats, -detailed_stats, draw, -draw, end_at, -end_at, forfeit, -forfeit, game_advantage, -game_advantage, id, -id, live_embed_url, -live_embed_url, match_type, -match_type, modified_at, -modified_at, name, -name, number_of_games, -number_of_games, official_stream_url, -official_stream_url, original_scheduled_at, -original_scheduled_at, scheduled_at, -scheduled_at, slug, -slug, status, -status, tournament_id, -tournament_id, winner_id, -winner_id] |
| **search** | [**SearchOverBrackets**](.md)| Options to search results | [optional] |
| **page** | [**GetAdditionsPageParameter**](.md)| Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; | [optional] |
| **perPage** | **Integer**| Equivalent to &#x60;page[size]&#x60; | [optional] [default to 50] |

### Return type

[**List&lt;Bracket&gt;**](Bracket.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A tree of games played during a tournament |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="getTournamentsTournamentIdOrSlugMatches"></a>
# **getTournamentsTournamentIdOrSlugMatches**
> List&lt;Match&gt; getTournamentsTournamentIdOrSlugMatches(tournamentIdOrSlug, filter, search, sort, range, page, perPage)

Get matches for tournament

List matches for the given tournament

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TournamentsApi;

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

    TournamentsApi apiInstance = new TournamentsApi(defaultClient);
    TournamentIDOrSlug tournamentIdOrSlug = new TournamentIDOrSlug(); // TournamentIDOrSlug | A tournament ID or slug
    FilterOverMatches filter = new FilterOverMatches(); // FilterOverMatches | Options to filter results. String fields are case sensitive
    SearchOverMatches search = new SearchOverMatches(); // SearchOverMatches | Options to search results
    List<String> sort = Arrays.asList(); // List<String> | Options to sort results
    RangeOverMatches range = new RangeOverMatches(); // RangeOverMatches | Options to select results within ranges
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    try {
      List<Match> result = apiInstance.getTournamentsTournamentIdOrSlugMatches(tournamentIdOrSlug, filter, search, sort, range, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TournamentsApi#getTournamentsTournamentIdOrSlugMatches");
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
| **tournamentIdOrSlug** | [**TournamentIDOrSlug**](.md)| A tournament ID or slug | |
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

<a id="getTournamentsTournamentIdOrSlugPlayers"></a>
# **getTournamentsTournamentIdOrSlugPlayers**
> List&lt;Player&gt; getTournamentsTournamentIdOrSlugPlayers(tournamentIdOrSlug, filter, search, sort, range, page, perPage)

Get players for a tournament

List players for the given tournament

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TournamentsApi;

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

    TournamentsApi apiInstance = new TournamentsApi(defaultClient);
    String tournamentIdOrSlug = "tournamentIdOrSlug_example"; // String | Automatically added
    FilterOverPlayers filter = new FilterOverPlayers(); // FilterOverPlayers | Options to filter results. String fields are case sensitive
    SearchOverPlayers search = new SearchOverPlayers(); // SearchOverPlayers | Options to search results
    List<String> sort = Arrays.asList(); // List<String> | Options to sort results
    RangeOverPlayers range = new RangeOverPlayers(); // RangeOverPlayers | Options to select results within ranges
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    try {
      List<Player> result = apiInstance.getTournamentsTournamentIdOrSlugPlayers(tournamentIdOrSlug, filter, search, sort, range, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TournamentsApi#getTournamentsTournamentIdOrSlugPlayers");
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
| **tournamentIdOrSlug** | **String**| Automatically added | |
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

<a id="getTournamentsTournamentIdOrSlugRosters"></a>
# **getTournamentsTournamentIdOrSlugRosters**
> TournamentRosters getTournamentsTournamentIdOrSlugRosters(tournamentIdOrSlug)

Get rosters for a tournament

List participants (player or team) for a given tournament.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TournamentsApi;

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

    TournamentsApi apiInstance = new TournamentsApi(defaultClient);
    TournamentIDOrSlug tournamentIdOrSlug = new TournamentIDOrSlug(); // TournamentIDOrSlug | A tournament ID or slug
    try {
      TournamentRosters result = apiInstance.getTournamentsTournamentIdOrSlugRosters(tournamentIdOrSlug);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TournamentsApi#getTournamentsTournamentIdOrSlugRosters");
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
| **tournamentIdOrSlug** | [**TournamentIDOrSlug**](.md)| A tournament ID or slug | |

### Return type

[**TournamentRosters**](TournamentRosters.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tournament rosters (team or player) |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="getTournamentsTournamentIdOrSlugStandings"></a>
# **getTournamentsTournamentIdOrSlugStandings**
> List&lt;Standing&gt; getTournamentsTournamentIdOrSlugStandings(tournamentIdOrSlug, page, perPage)

Get tournament standings

Get the current standings for a given tournament

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TournamentsApi;

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

    TournamentsApi apiInstance = new TournamentsApi(defaultClient);
    TournamentIDOrSlug tournamentIdOrSlug = new TournamentIDOrSlug(); // TournamentIDOrSlug | A tournament ID or slug
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    try {
      List<Standing> result = apiInstance.getTournamentsTournamentIdOrSlugStandings(tournamentIdOrSlug, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TournamentsApi#getTournamentsTournamentIdOrSlugStandings");
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
| **tournamentIdOrSlug** | [**TournamentIDOrSlug**](.md)| A tournament ID or slug | |
| **page** | [**GetAdditionsPageParameter**](.md)| Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; | [optional] |
| **perPage** | **Integer**| Equivalent to &#x60;page[size]&#x60; | [optional] [default to 50] |

### Return type

[**List&lt;Standing&gt;**](Standing.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ranking of teams in a tournament |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="getTournamentsTournamentIdOrSlugTeams"></a>
# **getTournamentsTournamentIdOrSlugTeams**
> List&lt;Team&gt; getTournamentsTournamentIdOrSlugTeams(tournamentIdOrSlug, filter, search, sort, range, page, perPage)

Get teams for a tournament

List teams for the given tournament

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TournamentsApi;

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

    TournamentsApi apiInstance = new TournamentsApi(defaultClient);
    TournamentIDOrSlug tournamentIdOrSlug = new TournamentIDOrSlug(); // TournamentIDOrSlug | A tournament ID or slug
    FilterOverTeams filter = new FilterOverTeams(); // FilterOverTeams | Options to filter results. String fields are case sensitive
    SearchOverTeams search = new SearchOverTeams(); // SearchOverTeams | Options to search results
    List<String> sort = Arrays.asList(); // List<String> | Options to sort results
    RangeOverTeams range = new RangeOverTeams(); // RangeOverTeams | Options to select results within ranges
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    try {
      List<Team> result = apiInstance.getTournamentsTournamentIdOrSlugTeams(tournamentIdOrSlug, filter, search, sort, range, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TournamentsApi#getTournamentsTournamentIdOrSlugTeams");
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
| **tournamentIdOrSlug** | [**TournamentIDOrSlug**](.md)| A tournament ID or slug | |
| **filter** | [**FilterOverTeams**](.md)| Options to filter results. String fields are case sensitive | [optional] |
| **search** | [**SearchOverTeams**](.md)| Options to search results | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| Options to sort results | [optional] [enum: acronym, -acronym, id, -id, location, -location, modified_at, -modified_at, name, -name, slug, -slug, videogame_id, -videogame_id] |
| **range** | [**RangeOverTeams**](.md)| Options to select results within ranges | [optional] |
| **page** | [**GetAdditionsPageParameter**](.md)| Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; | [optional] |
| **perPage** | **Integer**| Equivalent to &#x60;page[size]&#x60; | [optional] [default to 50] |

### Return type

[**List&lt;Team&gt;**](Team.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of teams |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="getTournamentsUpcoming"></a>
# **getTournamentsUpcoming**
> List&lt;ShortTournament&gt; getTournamentsUpcoming(filter, search, sort, range, page, perPage)

Get upcoming tournaments

List upcoming tournaments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TournamentsApi;

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

    TournamentsApi apiInstance = new TournamentsApi(defaultClient);
    FilterOverShortTournaments filter = new FilterOverShortTournaments(); // FilterOverShortTournaments | Options to filter results. String fields are case sensitive
    SearchOverShortTournaments search = new SearchOverShortTournaments(); // SearchOverShortTournaments | Options to search results
    List<String> sort = Arrays.asList(); // List<String> | Options to sort results
    RangeOverShortTournaments range = new RangeOverShortTournaments(); // RangeOverShortTournaments | Options to select results within ranges
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    try {
      List<ShortTournament> result = apiInstance.getTournamentsUpcoming(filter, search, sort, range, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TournamentsApi#getTournamentsUpcoming");
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

