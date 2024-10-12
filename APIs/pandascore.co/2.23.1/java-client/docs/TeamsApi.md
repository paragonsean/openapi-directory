# TeamsApi

All URIs are relative to *https://api.pandascore.co*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getTeams**](TeamsApi.md#getTeams) | **GET** /teams | List teams |
| [**getTeamsTeamIdOrSlug**](TeamsApi.md#getTeamsTeamIdOrSlug) | **GET** /teams/{team_id_or_slug} | Get a team |
| [**getTeamsTeamIdOrSlugLeagues**](TeamsApi.md#getTeamsTeamIdOrSlugLeagues) | **GET** /teams/{team_id_or_slug}/leagues | Get leagues for a team |
| [**getTeamsTeamIdOrSlugMatches**](TeamsApi.md#getTeamsTeamIdOrSlugMatches) | **GET** /teams/{team_id_or_slug}/matches | Get matches for team |
| [**getTeamsTeamIdOrSlugSeries**](TeamsApi.md#getTeamsTeamIdOrSlugSeries) | **GET** /teams/{team_id_or_slug}/series | Get series for a team |
| [**getTeamsTeamIdOrSlugTournaments**](TeamsApi.md#getTeamsTeamIdOrSlugTournaments) | **GET** /teams/{team_id_or_slug}/tournaments | Get tournaments for a team |


<a id="getTeams"></a>
# **getTeams**
> List&lt;Team&gt; getTeams(filter, search, sort, range, page, perPage)

List teams

List teams

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

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

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    FilterOverTeams filter = new FilterOverTeams(); // FilterOverTeams | Options to filter results. String fields are case sensitive
    SearchOverTeams search = new SearchOverTeams(); // SearchOverTeams | Options to search results
    List<String> sort = Arrays.asList(); // List<String> | Options to sort results
    RangeOverTeams range = new RangeOverTeams(); // RangeOverTeams | Options to select results within ranges
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    try {
      List<Team> result = apiInstance.getTeams(filter, search, sort, range, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#getTeams");
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

<a id="getTeamsTeamIdOrSlug"></a>
# **getTeamsTeamIdOrSlug**
> Team getTeamsTeamIdOrSlug(teamIdOrSlug)

Get a team

Get a single team by ID or by slug

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

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

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    TeamIDOrSlug teamIdOrSlug = new TeamIDOrSlug(); // TeamIDOrSlug | A team ID or slug
    try {
      Team result = apiInstance.getTeamsTeamIdOrSlug(teamIdOrSlug);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#getTeamsTeamIdOrSlug");
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
| **teamIdOrSlug** | [**TeamIDOrSlug**](.md)| A team ID or slug | |

### Return type

[**Team**](Team.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A team |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="getTeamsTeamIdOrSlugLeagues"></a>
# **getTeamsTeamIdOrSlugLeagues**
> List&lt;League&gt; getTeamsTeamIdOrSlugLeagues(teamIdOrSlug, search, sort, range, filter, page, perPage)

Get leagues for a team

List leagues in which the given team was part of

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

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

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    TeamIDOrSlug teamIdOrSlug = new TeamIDOrSlug(); // TeamIDOrSlug | A team ID or slug
    SearchOverLeagues search = new SearchOverLeagues(); // SearchOverLeagues | Options to search results
    List<String> sort = Arrays.asList(); // List<String> | Options to sort results
    RangeOverLeagues range = new RangeOverLeagues(); // RangeOverLeagues | Options to select results within ranges
    FilterOverLeagues filter = new FilterOverLeagues(); // FilterOverLeagues | Options to filter results. String fields are case sensitive
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    try {
      List<League> result = apiInstance.getTeamsTeamIdOrSlugLeagues(teamIdOrSlug, search, sort, range, filter, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#getTeamsTeamIdOrSlugLeagues");
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
| **teamIdOrSlug** | [**TeamIDOrSlug**](.md)| A team ID or slug | |
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

<a id="getTeamsTeamIdOrSlugMatches"></a>
# **getTeamsTeamIdOrSlugMatches**
> List&lt;Match&gt; getTeamsTeamIdOrSlugMatches(teamIdOrSlug, filter, search, sort, range, page, perPage)

Get matches for team

List matches for the given team

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

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

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    TeamIDOrSlug teamIdOrSlug = new TeamIDOrSlug(); // TeamIDOrSlug | A team ID or slug
    FilterOverMatches filter = new FilterOverMatches(); // FilterOverMatches | Options to filter results. String fields are case sensitive
    SearchOverMatches search = new SearchOverMatches(); // SearchOverMatches | Options to search results
    List<String> sort = Arrays.asList(); // List<String> | Options to sort results
    RangeOverMatches range = new RangeOverMatches(); // RangeOverMatches | Options to select results within ranges
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    try {
      List<Match> result = apiInstance.getTeamsTeamIdOrSlugMatches(teamIdOrSlug, filter, search, sort, range, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#getTeamsTeamIdOrSlugMatches");
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
| **teamIdOrSlug** | [**TeamIDOrSlug**](.md)| A team ID or slug | |
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

<a id="getTeamsTeamIdOrSlugSeries"></a>
# **getTeamsTeamIdOrSlugSeries**
> List&lt;Serie&gt; getTeamsTeamIdOrSlugSeries(teamIdOrSlug, filter, search, sort, range, page, perPage)

Get series for a team

List series in which the given team was part of

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

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

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    TeamIDOrSlug teamIdOrSlug = new TeamIDOrSlug(); // TeamIDOrSlug | A team ID or slug
    FilterOverSeries filter = new FilterOverSeries(); // FilterOverSeries | Options to filter results. String fields are case sensitive
    SearchOverSeries search = new SearchOverSeries(); // SearchOverSeries | Options to search results
    List<String> sort = Arrays.asList(); // List<String> | Options to sort results
    RangeOverSeries range = new RangeOverSeries(); // RangeOverSeries | Options to select results within ranges
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    try {
      List<Serie> result = apiInstance.getTeamsTeamIdOrSlugSeries(teamIdOrSlug, filter, search, sort, range, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#getTeamsTeamIdOrSlugSeries");
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
| **teamIdOrSlug** | [**TeamIDOrSlug**](.md)| A team ID or slug | |
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

<a id="getTeamsTeamIdOrSlugTournaments"></a>
# **getTeamsTeamIdOrSlugTournaments**
> List&lt;ShortTournament&gt; getTeamsTeamIdOrSlugTournaments(teamIdOrSlug, filter, search, sort, range, page, perPage)

Get tournaments for a team

List tournaments in which the given team was part of

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

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

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    TeamIDOrSlug teamIdOrSlug = new TeamIDOrSlug(); // TeamIDOrSlug | A team ID or slug
    FilterOverShortTournaments filter = new FilterOverShortTournaments(); // FilterOverShortTournaments | Options to filter results. String fields are case sensitive
    SearchOverShortTournaments search = new SearchOverShortTournaments(); // SearchOverShortTournaments | Options to search results
    List<String> sort = Arrays.asList(); // List<String> | Options to sort results
    RangeOverShortTournaments range = new RangeOverShortTournaments(); // RangeOverShortTournaments | Options to select results within ranges
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    try {
      List<ShortTournament> result = apiInstance.getTeamsTeamIdOrSlugTournaments(teamIdOrSlug, filter, search, sort, range, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#getTeamsTeamIdOrSlugTournaments");
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
| **teamIdOrSlug** | [**TeamIDOrSlug**](.md)| A team ID or slug | |
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

