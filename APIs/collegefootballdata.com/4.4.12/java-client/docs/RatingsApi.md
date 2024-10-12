# RatingsApi

All URIs are relative to *https://api.collegefootballdata.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getConferenceSPRatings**](RatingsApi.md#getConferenceSPRatings) | **GET** /ratings/sp/conferences | Historical SP+ ratings by conference |
| [**getEloRatings**](RatingsApi.md#getEloRatings) | **GET** /ratings/elo | Historical Elo ratings |
| [**getSPRatings**](RatingsApi.md#getSPRatings) | **GET** /ratings/sp | Historical SP+ ratings |
| [**getSRSRatings**](RatingsApi.md#getSRSRatings) | **GET** /ratings/srs | Historical SRS ratings |


<a id="getConferenceSPRatings"></a>
# **getConferenceSPRatings**
> List&lt;ConferenceSPRating&gt; getConferenceSPRatings(year, conference)

Historical SP+ ratings by conference

Get average SP+ historical rating data by conference

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RatingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    RatingsApi apiInstance = new RatingsApi(defaultClient);
    Integer year = 56; // Integer | Season filter
    String conference = "conference_example"; // String | Conference abbreviation filter
    try {
      List<ConferenceSPRating> result = apiInstance.getConferenceSPRatings(year, conference);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RatingsApi#getConferenceSPRatings");
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
| **year** | **Integer**| Season filter | [optional] |
| **conference** | **String**| Conference abbreviation filter | [optional] |

### Return type

[**List&lt;ConferenceSPRating&gt;**](ConferenceSPRating.md)

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

<a id="getEloRatings"></a>
# **getEloRatings**
> List&lt;TeamEloRating&gt; getEloRatings(year, week, team, conference)

Historical Elo ratings

Elo rating data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RatingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    RatingsApi apiInstance = new RatingsApi(defaultClient);
    Integer year = 56; // Integer | Season filter
    Integer week = 56; // Integer | Maximum week filter
    String team = "team_example"; // String | Team filter
    String conference = "conference_example"; // String | Conference filter
    try {
      List<TeamEloRating> result = apiInstance.getEloRatings(year, week, team, conference);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RatingsApi#getEloRatings");
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
| **year** | **Integer**| Season filter | [optional] |
| **week** | **Integer**| Maximum week filter | [optional] |
| **team** | **String**| Team filter | [optional] |
| **conference** | **String**| Conference filter | [optional] |

### Return type

[**List&lt;TeamEloRating&gt;**](TeamEloRating.md)

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

<a id="getSPRatings"></a>
# **getSPRatings**
> List&lt;TeamSPRating&gt; getSPRatings(year, team)

Historical SP+ ratings

SP+ rating data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RatingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    RatingsApi apiInstance = new RatingsApi(defaultClient);
    Integer year = 56; // Integer | Season filter (required if team not specified)
    String team = "team_example"; // String | Team filter (required if year not specified)
    try {
      List<TeamSPRating> result = apiInstance.getSPRatings(year, team);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RatingsApi#getSPRatings");
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
| **year** | **Integer**| Season filter (required if team not specified) | [optional] |
| **team** | **String**| Team filter (required if year not specified) | [optional] |

### Return type

[**List&lt;TeamSPRating&gt;**](TeamSPRating.md)

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

<a id="getSRSRatings"></a>
# **getSRSRatings**
> List&lt;TeamSRSRating&gt; getSRSRatings(year, team, conference)

Historical SRS ratings

SRS rating data (requires either a year or team specified)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RatingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    RatingsApi apiInstance = new RatingsApi(defaultClient);
    Integer year = 56; // Integer | Season filter (required if team not specified)
    String team = "team_example"; // String | Team filter (required if year not specified)
    String conference = "conference_example"; // String | Conference filter
    try {
      List<TeamSRSRating> result = apiInstance.getSRSRatings(year, team, conference);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RatingsApi#getSRSRatings");
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
| **year** | **Integer**| Season filter (required if team not specified) | [optional] |
| **team** | **String**| Team filter (required if year not specified) | [optional] |
| **conference** | **String**| Conference filter | [optional] |

### Return type

[**List&lt;TeamSRSRating&gt;**](TeamSRSRating.md)

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

