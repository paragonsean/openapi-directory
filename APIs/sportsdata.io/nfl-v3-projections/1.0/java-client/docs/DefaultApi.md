# DefaultApi

All URIs are relative to *http://azure-api.sportsdata.io/v3/nfl/projections*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dfsSlateOwnershipProjectionsBySlateid**](DefaultApi.md#dfsSlateOwnershipProjectionsBySlateid) | **GET** /{format}/DfsSlateOwnershipProjectionsBySlateID/{slateId} | DFS Slate Ownership Projections by SlateID |
| [**dfsSlatesByDate**](DefaultApi.md#dfsSlatesByDate) | **GET** /{format}/DfsSlatesByDate/{date} | DFS Slates by Date |
| [**dfsSlatesByWeek**](DefaultApi.md#dfsSlatesByWeek) | **GET** /{format}/DfsSlatesByWeek/{season}/{week} | DFS Slates by Week |
| [**idpProjectedPlayerGameStatsByPlayerWInjuriesLineupsDfsSalaries**](DefaultApi.md#idpProjectedPlayerGameStatsByPlayerWInjuriesLineupsDfsSalaries) | **GET** /{format}/IdpPlayerGameProjectionStatsByPlayerID/{season}/{week}/{playerid} | IDP Projected Player Game Stats by Player (w/ Injuries, Lineups, DFS Salaries) |
| [**idpProjectedPlayerGameStatsByTeamWInjuriesLineupsDfsSalaries**](DefaultApi.md#idpProjectedPlayerGameStatsByTeamWInjuriesLineupsDfsSalaries) | **GET** /{format}/IdpPlayerGameProjectionStatsByTeam/{season}/{week}/{team} | IDP Projected Player Game Stats by Team (w/ Injuries, Lineups, DFS Salaries) |
| [**idpProjectedPlayerGameStatsByWeekWInjuriesLineupsDfsSalaries**](DefaultApi.md#idpProjectedPlayerGameStatsByWeekWInjuriesLineupsDfsSalaries) | **GET** /{format}/IdpPlayerGameProjectionStatsByWeek/{season}/{week} | IDP Projected Player Game Stats by Week (w/ Injuries, Lineups, DFS Salaries) |
| [**injuredPlayers**](DefaultApi.md#injuredPlayers) | **GET** /{format}/InjuredPlayers | Injured Players |
| [**projectedFantasyDefenseGameStatsWDfsSalaries**](DefaultApi.md#projectedFantasyDefenseGameStatsWDfsSalaries) | **GET** /{format}/FantasyDefenseProjectionsByGame/{season}/{week} | Projected Fantasy Defense Game Stats (w/ DFS Salaries) |
| [**projectedFantasyDefenseSeasonStatsWAdp**](DefaultApi.md#projectedFantasyDefenseSeasonStatsWAdp) | **GET** /{format}/FantasyDefenseProjectionsBySeason/{season} | Projected Fantasy Defense Season Stats (w/ ADP) |
| [**projectedPlayerGameStatsByPlayerWInjuriesLineupsDfsSalaries**](DefaultApi.md#projectedPlayerGameStatsByPlayerWInjuriesLineupsDfsSalaries) | **GET** /{format}/PlayerGameProjectionStatsByPlayerID/{season}/{week}/{playerid} | Projected Player Game Stats by Player (w/ Injuries, Lineups, DFS Salaries) |
| [**projectedPlayerGameStatsByTeamWInjuriesLineupsDfsSalaries**](DefaultApi.md#projectedPlayerGameStatsByTeamWInjuriesLineupsDfsSalaries) | **GET** /{format}/PlayerGameProjectionStatsByTeam/{season}/{week}/{team} | Projected Player Game Stats by Team (w/ Injuries, Lineups, DFS Salaries) |
| [**projectedPlayerGameStatsByWeekWInjuriesLineupsDfsSalaries**](DefaultApi.md#projectedPlayerGameStatsByWeekWInjuriesLineupsDfsSalaries) | **GET** /{format}/PlayerGameProjectionStatsByWeek/{season}/{week} | Projected Player Game Stats by Week (w/ Injuries, Lineups, DFS Salaries) |
| [**projectedPlayerSeasonStatsByPlayerWAdp**](DefaultApi.md#projectedPlayerSeasonStatsByPlayerWAdp) | **GET** /{format}/PlayerSeasonProjectionStatsByPlayerID/{season}/{playerid} | Projected Player Season Stats by Player (w/ ADP) |
| [**projectedPlayerSeasonStatsByTeamWAdp**](DefaultApi.md#projectedPlayerSeasonStatsByTeamWAdp) | **GET** /{format}/PlayerSeasonProjectionStatsByTeam/{season}/{team} | Projected Player Season Stats by Team (w/ ADP) |
| [**projectedPlayerSeasonStatsWAdp**](DefaultApi.md#projectedPlayerSeasonStatsWAdp) | **GET** /{format}/PlayerSeasonProjectionStats/{season} | Projected Player Season Stats (w/ ADP) |
| [**upcomingDfsSlateOwnershipProjections**](DefaultApi.md#upcomingDfsSlateOwnershipProjections) | **GET** /{format}/UpcomingDfsSlateOwnershipProjections | Upcoming DFS Slate Ownership Projections |


<a id="dfsSlateOwnershipProjectionsBySlateid"></a>
# **dfsSlateOwnershipProjectionsBySlateid**
> DfsSlateWithOwnershipProjection dfsSlateOwnershipProjectionsBySlateid(format, slateId)

DFS Slate Ownership Projections by SlateID

Slate Ownership Projections for a specific slate. Projections are for GPP format ownership. Will return an empty list if the slate is not yet projected or not a slate we have projections for.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure-api.sportsdata.io/v3/nfl/projections");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String format = "XML"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
    String slateId = "slateId_example"; // String | SlateID of the DFS Slate you wish to get ownership projections for. Will have an empty SlateOwnershipProjections if this slate was not projected
    try {
      DfsSlateWithOwnershipProjection result = apiInstance.dfsSlateOwnershipProjectionsBySlateid(format, slateId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#dfsSlateOwnershipProjectionsBySlateid");
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
| **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to XML] [enum: XML, JSON] |
| **slateId** | **String**| SlateID of the DFS Slate you wish to get ownership projections for. Will have an empty SlateOwnershipProjections if this slate was not projected | |

### Return type

[**DfsSlateWithOwnershipProjection**](DfsSlateWithOwnershipProjection.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dfsSlatesByDate"></a>
# **dfsSlatesByDate**
> List&lt;DfsSlate&gt; dfsSlatesByDate(format, date)

DFS Slates by Date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure-api.sportsdata.io/v3/nfl/projections");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String format = "XML"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
    String date = "date_example"; // String | The date of the slates. <br>Examples: <code>2017-SEP-25</code>, <code>2017-10-31</code>.
    try {
      List<DfsSlate> result = apiInstance.dfsSlatesByDate(format, date);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#dfsSlatesByDate");
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
| **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to XML] [enum: XML, JSON] |
| **date** | **String**| The date of the slates. &lt;br&gt;Examples: &lt;code&gt;2017-SEP-25&lt;/code&gt;, &lt;code&gt;2017-10-31&lt;/code&gt;. | |

### Return type

[**List&lt;DfsSlate&gt;**](DfsSlate.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dfsSlatesByWeek"></a>
# **dfsSlatesByWeek**
> List&lt;DfsSlate&gt; dfsSlatesByWeek(format, season, week)

DFS Slates by Week

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure-api.sportsdata.io/v3/nfl/projections");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String format = "XML"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
    String season = "season_example"; // String | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>
    String week = "week_example"; // String | Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>
    try {
      List<DfsSlate> result = apiInstance.dfsSlatesByWeek(format, season, week);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#dfsSlatesByWeek");
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
| **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to XML] [enum: XML, JSON] |
| **season** | **String**| Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt; | |
| **week** | **String**| Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt; | |

### Return type

[**List&lt;DfsSlate&gt;**](DfsSlate.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="idpProjectedPlayerGameStatsByPlayerWInjuriesLineupsDfsSalaries"></a>
# **idpProjectedPlayerGameStatsByPlayerWInjuriesLineupsDfsSalaries**
> PlayerGameProjection idpProjectedPlayerGameStatsByPlayerWInjuriesLineupsDfsSalaries(format, season, week, playerid)

IDP Projected Player Game Stats by Player (w/ Injuries, Lineups, DFS Salaries)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure-api.sportsdata.io/v3/nfl/projections");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String format = "XML"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
    String season = "season_example"; // String | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
    String week = "week_example"; // String | Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
    String playerid = "playerid_example"; // String | Each NFL player has a unique ID assigned by FantasyData. Player IDs can be determined by pulling player related data. Example:<code>14257</code>.
    try {
      PlayerGameProjection result = apiInstance.idpProjectedPlayerGameStatsByPlayerWInjuriesLineupsDfsSalaries(format, season, week, playerid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#idpProjectedPlayerGameStatsByPlayerWInjuriesLineupsDfsSalaries");
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
| **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to XML] [enum: XML, JSON] |
| **season** | **String**| Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | |
| **week** | **String**| Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | |
| **playerid** | **String**| Each NFL player has a unique ID assigned by FantasyData. Player IDs can be determined by pulling player related data. Example:&lt;code&gt;14257&lt;/code&gt;. | |

### Return type

[**PlayerGameProjection**](PlayerGameProjection.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="idpProjectedPlayerGameStatsByTeamWInjuriesLineupsDfsSalaries"></a>
# **idpProjectedPlayerGameStatsByTeamWInjuriesLineupsDfsSalaries**
> List&lt;PlayerGameProjection&gt; idpProjectedPlayerGameStatsByTeamWInjuriesLineupsDfsSalaries(format, season, week, team)

IDP Projected Player Game Stats by Team (w/ Injuries, Lineups, DFS Salaries)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure-api.sportsdata.io/v3/nfl/projections");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String format = "XML"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
    String season = "season_example"; // String | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
    String week = "week_example"; // String | Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
    String team = "team_example"; // String | Abbreviation of the team. Example: <code>WAS</code>.
    try {
      List<PlayerGameProjection> result = apiInstance.idpProjectedPlayerGameStatsByTeamWInjuriesLineupsDfsSalaries(format, season, week, team);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#idpProjectedPlayerGameStatsByTeamWInjuriesLineupsDfsSalaries");
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
| **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to XML] [enum: XML, JSON] |
| **season** | **String**| Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | |
| **week** | **String**| Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | |
| **team** | **String**| Abbreviation of the team. Example: &lt;code&gt;WAS&lt;/code&gt;. | |

### Return type

[**List&lt;PlayerGameProjection&gt;**](PlayerGameProjection.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="idpProjectedPlayerGameStatsByWeekWInjuriesLineupsDfsSalaries"></a>
# **idpProjectedPlayerGameStatsByWeekWInjuriesLineupsDfsSalaries**
> List&lt;PlayerGameProjection&gt; idpProjectedPlayerGameStatsByWeekWInjuriesLineupsDfsSalaries(format, season, week)

IDP Projected Player Game Stats by Week (w/ Injuries, Lineups, DFS Salaries)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure-api.sportsdata.io/v3/nfl/projections");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String format = "XML"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
    String season = "season_example"; // String | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
    String week = "week_example"; // String | Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
    try {
      List<PlayerGameProjection> result = apiInstance.idpProjectedPlayerGameStatsByWeekWInjuriesLineupsDfsSalaries(format, season, week);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#idpProjectedPlayerGameStatsByWeekWInjuriesLineupsDfsSalaries");
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
| **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to XML] [enum: XML, JSON] |
| **season** | **String**| Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | |
| **week** | **String**| Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | |

### Return type

[**List&lt;PlayerGameProjection&gt;**](PlayerGameProjection.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="injuredPlayers"></a>
# **injuredPlayers**
> List&lt;Player&gt; injuredPlayers(format)

Injured Players

This endpoint provides all currently injured NFL players, along with injury details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure-api.sportsdata.io/v3/nfl/projections");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String format = "XML"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
    try {
      List<Player> result = apiInstance.injuredPlayers(format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#injuredPlayers");
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
| **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to XML] [enum: XML, JSON] |

### Return type

[**List&lt;Player&gt;**](Player.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="projectedFantasyDefenseGameStatsWDfsSalaries"></a>
# **projectedFantasyDefenseGameStatsWDfsSalaries**
> List&lt;FantasyDefenseGameProjection&gt; projectedFantasyDefenseGameStatsWDfsSalaries(format, season, week)

Projected Fantasy Defense Game Stats (w/ DFS Salaries)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure-api.sportsdata.io/v3/nfl/projections");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String format = "XML"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
    String season = "season_example"; // String | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
    String week = "week_example"; // String | Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
    try {
      List<FantasyDefenseGameProjection> result = apiInstance.projectedFantasyDefenseGameStatsWDfsSalaries(format, season, week);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#projectedFantasyDefenseGameStatsWDfsSalaries");
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
| **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to XML] [enum: XML, JSON] |
| **season** | **String**| Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | |
| **week** | **String**| Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | |

### Return type

[**List&lt;FantasyDefenseGameProjection&gt;**](FantasyDefenseGameProjection.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="projectedFantasyDefenseSeasonStatsWAdp"></a>
# **projectedFantasyDefenseSeasonStatsWAdp**
> List&lt;FantasyDefenseSeasonProjection&gt; projectedFantasyDefenseSeasonStatsWAdp(format, season)

Projected Fantasy Defense Season Stats (w/ ADP)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure-api.sportsdata.io/v3/nfl/projections");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String format = "XML"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
    String season = "season_example"; // String | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
    try {
      List<FantasyDefenseSeasonProjection> result = apiInstance.projectedFantasyDefenseSeasonStatsWAdp(format, season);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#projectedFantasyDefenseSeasonStatsWAdp");
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
| **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to XML] [enum: XML, JSON] |
| **season** | **String**| Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | |

### Return type

[**List&lt;FantasyDefenseSeasonProjection&gt;**](FantasyDefenseSeasonProjection.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="projectedPlayerGameStatsByPlayerWInjuriesLineupsDfsSalaries"></a>
# **projectedPlayerGameStatsByPlayerWInjuriesLineupsDfsSalaries**
> PlayerGameProjection projectedPlayerGameStatsByPlayerWInjuriesLineupsDfsSalaries(format, season, week, playerid)

Projected Player Game Stats by Player (w/ Injuries, Lineups, DFS Salaries)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure-api.sportsdata.io/v3/nfl/projections");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String format = "XML"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
    String season = "season_example"; // String | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
    String week = "week_example"; // String |            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
    String playerid = "playerid_example"; // String | Each NFL player has a unique ID assigned by FantasyData. Player IDs can be determined by pulling player related data. Example:<code>14257</code>.
    try {
      PlayerGameProjection result = apiInstance.projectedPlayerGameStatsByPlayerWInjuriesLineupsDfsSalaries(format, season, week, playerid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#projectedPlayerGameStatsByPlayerWInjuriesLineupsDfsSalaries");
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
| **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to XML] [enum: XML, JSON] |
| **season** | **String**| Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | |
| **week** | **String**|            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | |
| **playerid** | **String**| Each NFL player has a unique ID assigned by FantasyData. Player IDs can be determined by pulling player related data. Example:&lt;code&gt;14257&lt;/code&gt;. | |

### Return type

[**PlayerGameProjection**](PlayerGameProjection.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="projectedPlayerGameStatsByTeamWInjuriesLineupsDfsSalaries"></a>
# **projectedPlayerGameStatsByTeamWInjuriesLineupsDfsSalaries**
> List&lt;PlayerGameProjection&gt; projectedPlayerGameStatsByTeamWInjuriesLineupsDfsSalaries(format, season, week, team)

Projected Player Game Stats by Team (w/ Injuries, Lineups, DFS Salaries)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure-api.sportsdata.io/v3/nfl/projections");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String format = "XML"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
    String season = "season_example"; // String | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
    String week = "week_example"; // String | Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
    String team = "team_example"; // String | Abbreviation of the team. Example: <code>WAS</code>.
    try {
      List<PlayerGameProjection> result = apiInstance.projectedPlayerGameStatsByTeamWInjuriesLineupsDfsSalaries(format, season, week, team);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#projectedPlayerGameStatsByTeamWInjuriesLineupsDfsSalaries");
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
| **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to XML] [enum: XML, JSON] |
| **season** | **String**| Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | |
| **week** | **String**| Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | |
| **team** | **String**| Abbreviation of the team. Example: &lt;code&gt;WAS&lt;/code&gt;. | |

### Return type

[**List&lt;PlayerGameProjection&gt;**](PlayerGameProjection.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="projectedPlayerGameStatsByWeekWInjuriesLineupsDfsSalaries"></a>
# **projectedPlayerGameStatsByWeekWInjuriesLineupsDfsSalaries**
> List&lt;PlayerGameProjection&gt; projectedPlayerGameStatsByWeekWInjuriesLineupsDfsSalaries(format, season, week)

Projected Player Game Stats by Week (w/ Injuries, Lineups, DFS Salaries)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure-api.sportsdata.io/v3/nfl/projections");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String format = "XML"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
    String season = "season_example"; // String | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
    String week = "week_example"; // String |            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: <code>1</code>         
    try {
      List<PlayerGameProjection> result = apiInstance.projectedPlayerGameStatsByWeekWInjuriesLineupsDfsSalaries(format, season, week);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#projectedPlayerGameStatsByWeekWInjuriesLineupsDfsSalaries");
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
| **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to XML] [enum: XML, JSON] |
| **season** | **String**| Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | |
| **week** | **String**|            Week of the season. Valid values are as follows: Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4.           Example: &lt;code&gt;1&lt;/code&gt;          | |

### Return type

[**List&lt;PlayerGameProjection&gt;**](PlayerGameProjection.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="projectedPlayerSeasonStatsByPlayerWAdp"></a>
# **projectedPlayerSeasonStatsByPlayerWAdp**
> PlayerSeasonProjection projectedPlayerSeasonStatsByPlayerWAdp(format, season, playerid)

Projected Player Season Stats by Player (w/ ADP)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure-api.sportsdata.io/v3/nfl/projections");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String format = "XML"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
    String season = "season_example"; // String | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
    String playerid = "playerid_example"; // String | Each NFL player has a unique ID assigned by FantasyData. Player IDs can be determined by pulling player related data. Example:<code>14257</code>.
    try {
      PlayerSeasonProjection result = apiInstance.projectedPlayerSeasonStatsByPlayerWAdp(format, season, playerid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#projectedPlayerSeasonStatsByPlayerWAdp");
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
| **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to XML] [enum: XML, JSON] |
| **season** | **String**| Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | |
| **playerid** | **String**| Each NFL player has a unique ID assigned by FantasyData. Player IDs can be determined by pulling player related data. Example:&lt;code&gt;14257&lt;/code&gt;. | |

### Return type

[**PlayerSeasonProjection**](PlayerSeasonProjection.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="projectedPlayerSeasonStatsByTeamWAdp"></a>
# **projectedPlayerSeasonStatsByTeamWAdp**
> List&lt;PlayerSeasonProjection&gt; projectedPlayerSeasonStatsByTeamWAdp(format, season, team)

Projected Player Season Stats by Team (w/ ADP)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure-api.sportsdata.io/v3/nfl/projections");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String format = "XML"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
    String season = "season_example"; // String | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
    String team = "team_example"; // String | Abbreviation of the team. Example: <code>WAS</code>.
    try {
      List<PlayerSeasonProjection> result = apiInstance.projectedPlayerSeasonStatsByTeamWAdp(format, season, team);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#projectedPlayerSeasonStatsByTeamWAdp");
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
| **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to XML] [enum: XML, JSON] |
| **season** | **String**| Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | |
| **team** | **String**| Abbreviation of the team. Example: &lt;code&gt;WAS&lt;/code&gt;. | |

### Return type

[**List&lt;PlayerSeasonProjection&gt;**](PlayerSeasonProjection.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="projectedPlayerSeasonStatsWAdp"></a>
# **projectedPlayerSeasonStatsWAdp**
> List&lt;PlayerSeasonProjection&gt; projectedPlayerSeasonStatsWAdp(format, season)

Projected Player Season Stats (w/ ADP)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure-api.sportsdata.io/v3/nfl/projections");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String format = "XML"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
    String season = "season_example"; // String | Year of the season and the season type. If no season type is provided, then the default is regular season.           <br>Examples: <code>2015REG</code>, <code>2015PRE</code>, <code>2015POST</code>.         
    try {
      List<PlayerSeasonProjection> result = apiInstance.projectedPlayerSeasonStatsWAdp(format, season);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#projectedPlayerSeasonStatsWAdp");
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
| **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to XML] [enum: XML, JSON] |
| **season** | **String**| Year of the season and the season type. If no season type is provided, then the default is regular season.           &lt;br&gt;Examples: &lt;code&gt;2015REG&lt;/code&gt;, &lt;code&gt;2015PRE&lt;/code&gt;, &lt;code&gt;2015POST&lt;/code&gt;.          | |

### Return type

[**List&lt;PlayerSeasonProjection&gt;**](PlayerSeasonProjection.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="upcomingDfsSlateOwnershipProjections"></a>
# **upcomingDfsSlateOwnershipProjections**
> List&lt;DfsSlateWithOwnershipProjection&gt; upcomingDfsSlateOwnershipProjections(format)

Upcoming DFS Slate Ownership Projections

Grabs DFS Slates which have not yet started for which we have DFS Ownership projections. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure-api.sportsdata.io/v3/nfl/projections");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String format = "XML"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
    try {
      List<DfsSlateWithOwnershipProjection> result = apiInstance.upcomingDfsSlateOwnershipProjections(format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#upcomingDfsSlateOwnershipProjections");
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
| **format** | **String**| Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;. | [default to XML] [enum: XML, JSON] |

### Return type

[**List&lt;DfsSlateWithOwnershipProjection&gt;**](DfsSlateWithOwnershipProjection.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

