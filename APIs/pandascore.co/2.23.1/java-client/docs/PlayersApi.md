# PlayersApi

All URIs are relative to *https://api.pandascore.co*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getPlayers**](PlayersApi.md#getPlayers) | **GET** /players | List players |
| [**getPlayersPlayerIdOrSlug**](PlayersApi.md#getPlayersPlayerIdOrSlug) | **GET** /players/{player_id_or_slug} | Get a player |
| [**getPlayersPlayerIdOrSlugMatches**](PlayersApi.md#getPlayersPlayerIdOrSlugMatches) | **GET** /players/{player_id_or_slug}/matches | Get matches for a player |


<a id="getPlayers"></a>
# **getPlayers**
> List&lt;Player&gt; getPlayers(filter, search, sort, range, page, perPage)

List players

List players

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlayersApi;

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

    PlayersApi apiInstance = new PlayersApi(defaultClient);
    FilterOverPlayers filter = new FilterOverPlayers(); // FilterOverPlayers | Options to filter results. String fields are case sensitive
    SearchOverPlayers search = new SearchOverPlayers(); // SearchOverPlayers | Options to search results
    List<String> sort = Arrays.asList(); // List<String> | Options to sort results
    RangeOverPlayers range = new RangeOverPlayers(); // RangeOverPlayers | Options to select results within ranges
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    try {
      List<Player> result = apiInstance.getPlayers(filter, search, sort, range, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlayersApi#getPlayers");
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

<a id="getPlayersPlayerIdOrSlug"></a>
# **getPlayersPlayerIdOrSlug**
> Player getPlayersPlayerIdOrSlug(playerIdOrSlug)

Get a player

Get a single player by ID or by slug

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlayersApi;

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

    PlayersApi apiInstance = new PlayersApi(defaultClient);
    PlayerIDOrSlug playerIdOrSlug = new PlayerIDOrSlug(); // PlayerIDOrSlug | A player ID or slug
    try {
      Player result = apiInstance.getPlayersPlayerIdOrSlug(playerIdOrSlug);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlayersApi#getPlayersPlayerIdOrSlug");
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
| **playerIdOrSlug** | [**PlayerIDOrSlug**](.md)| A player ID or slug | |

### Return type

[**Player**](Player.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A player |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="getPlayersPlayerIdOrSlugMatches"></a>
# **getPlayersPlayerIdOrSlugMatches**
> List&lt;Match&gt; getPlayersPlayerIdOrSlugMatches(playerIdOrSlug, filter, search, sort, range, page, perPage)

Get matches for a player

List matches for the given player. Only matches with detailed stats. Available with the plan _Historical data_.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlayersApi;

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

    PlayersApi apiInstance = new PlayersApi(defaultClient);
    PlayerIDOrSlug playerIdOrSlug = new PlayerIDOrSlug(); // PlayerIDOrSlug | A player ID or slug
    FilterOverMatches filter = new FilterOverMatches(); // FilterOverMatches | Options to filter results. String fields are case sensitive
    SearchOverMatches search = new SearchOverMatches(); // SearchOverMatches | Options to search results
    List<String> sort = Arrays.asList(); // List<String> | Options to sort results
    RangeOverMatches range = new RangeOverMatches(); // RangeOverMatches | Options to select results within ranges
    GetAdditionsPageParameter page = new GetAdditionsPageParameter(); // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
    Integer perPage = 50; // Integer | Equivalent to `page[size]`
    try {
      List<Match> result = apiInstance.getPlayersPlayerIdOrSlugMatches(playerIdOrSlug, filter, search, sort, range, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlayersApi#getPlayersPlayerIdOrSlugMatches");
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
| **playerIdOrSlug** | [**PlayerIDOrSlug**](.md)| A player ID or slug | |
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

