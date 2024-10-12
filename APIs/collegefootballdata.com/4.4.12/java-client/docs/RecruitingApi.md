# RecruitingApi

All URIs are relative to *https://api.collegefootballdata.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getRecruitingGroups**](RecruitingApi.md#getRecruitingGroups) | **GET** /recruiting/groups | Recruit position group ratings |
| [**getRecruitingPlayers**](RecruitingApi.md#getRecruitingPlayers) | **GET** /recruiting/players | Player recruiting ratings and rankings |
| [**getRecruitingTeams**](RecruitingApi.md#getRecruitingTeams) | **GET** /recruiting/teams | Team recruiting rankings and ratings |


<a id="getRecruitingGroups"></a>
# **getRecruitingGroups**
> List&lt;PositionGroupRecruitingRating&gt; getRecruitingGroups(startYear, endYear, team, conference)

Recruit position group ratings

Gets a list of aggregated statistics by team and position grouping

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecruitingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    RecruitingApi apiInstance = new RecruitingApi(defaultClient);
    Integer startYear = 56; // Integer | Starting year
    Integer endYear = 56; // Integer | Ending year
    String team = "team_example"; // String | Team filter
    String conference = "conference_example"; // String | conference filter
    try {
      List<PositionGroupRecruitingRating> result = apiInstance.getRecruitingGroups(startYear, endYear, team, conference);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecruitingApi#getRecruitingGroups");
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
| **startYear** | **Integer**| Starting year | [optional] |
| **endYear** | **Integer**| Ending year | [optional] |
| **team** | **String**| Team filter | [optional] |
| **conference** | **String**| conference filter | [optional] |

### Return type

[**List&lt;PositionGroupRecruitingRating&gt;**](PositionGroupRecruitingRating.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | error |  -  |

<a id="getRecruitingPlayers"></a>
# **getRecruitingPlayers**
> List&lt;Recruit&gt; getRecruitingPlayers(year, classification, position, state, team)

Player recruiting ratings and rankings

Get player recruiting rankings and data. Requires either a year or team to be specified.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecruitingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    RecruitingApi apiInstance = new RecruitingApi(defaultClient);
    Integer year = 56; // Integer | Recruiting class year (required if team no specified)
    String classification = "HighSchool"; // String | Type of recruit (HighSchool, JUCO, PrepSchool)
    String position = "position_example"; // String | Position abbreviation filter
    String state = "state_example"; // String | State or province abbreviation filter
    String team = "team_example"; // String | Committed team filter (required if year not specified)
    try {
      List<Recruit> result = apiInstance.getRecruitingPlayers(year, classification, position, state, team);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecruitingApi#getRecruitingPlayers");
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
| **year** | **Integer**| Recruiting class year (required if team no specified) | [optional] |
| **classification** | **String**| Type of recruit (HighSchool, JUCO, PrepSchool) | [optional] [default to HighSchool] |
| **position** | **String**| Position abbreviation filter | [optional] |
| **state** | **String**| State or province abbreviation filter | [optional] |
| **team** | **String**| Committed team filter (required if year not specified) | [optional] |

### Return type

[**List&lt;Recruit&gt;**](Recruit.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | error |  -  |

<a id="getRecruitingTeams"></a>
# **getRecruitingTeams**
> List&lt;TeamRecruitingRank&gt; getRecruitingTeams(year, team)

Team recruiting rankings and ratings

Team recruiting rankings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecruitingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    RecruitingApi apiInstance = new RecruitingApi(defaultClient);
    Integer year = 56; // Integer | Recruiting class year
    String team = "team_example"; // String | Team filter
    try {
      List<TeamRecruitingRank> result = apiInstance.getRecruitingTeams(year, team);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecruitingApi#getRecruitingTeams");
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
| **year** | **Integer**| Recruiting class year | [optional] |
| **team** | **String**| Team filter | [optional] |

### Return type

[**List&lt;TeamRecruitingRank&gt;**](TeamRecruitingRank.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | error |  -  |

