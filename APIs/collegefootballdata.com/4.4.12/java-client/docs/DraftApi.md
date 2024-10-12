# DraftApi

All URIs are relative to *https://api.collegefootballdata.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDraftPicks**](DraftApi.md#getDraftPicks) | **GET** /draft/picks | List of NFL Draft picks |
| [**getNFLPositions**](DraftApi.md#getNFLPositions) | **GET** /draft/positions | List of NFL positions |
| [**getNFLTeams**](DraftApi.md#getNFLTeams) | **GET** /draft/teams | List of NFL teams |


<a id="getDraftPicks"></a>
# **getDraftPicks**
> List&lt;DraftPick&gt; getDraftPicks(year, nflTeam, college, conference, position)

List of NFL Draft picks

List of NFL Draft picks

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DraftApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    DraftApi apiInstance = new DraftApi(defaultClient);
    Integer year = 56; // Integer | Year filter
    String nflTeam = "nflTeam_example"; // String | NFL team filter
    String college = "college_example"; // String | Player college filter
    String conference = "conference_example"; // String | College confrence abbreviation filter
    String position = "position_example"; // String | NFL position filter
    try {
      List<DraftPick> result = apiInstance.getDraftPicks(year, nflTeam, college, conference, position);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DraftApi#getDraftPicks");
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
| **year** | **Integer**| Year filter | [optional] |
| **nflTeam** | **String**| NFL team filter | [optional] |
| **college** | **String**| Player college filter | [optional] |
| **conference** | **String**| College confrence abbreviation filter | [optional] |
| **position** | **String**| NFL position filter | [optional] |

### Return type

[**List&lt;DraftPick&gt;**](DraftPick.md)

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

<a id="getNFLPositions"></a>
# **getNFLPositions**
> List&lt;DraftPosition&gt; getNFLPositions()

List of NFL positions

List of NFL positions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DraftApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    DraftApi apiInstance = new DraftApi(defaultClient);
    try {
      List<DraftPosition> result = apiInstance.getNFLPositions();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DraftApi#getNFLPositions");
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

[**List&lt;DraftPosition&gt;**](DraftPosition.md)

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

<a id="getNFLTeams"></a>
# **getNFLTeams**
> List&lt;DraftTeam&gt; getNFLTeams()

List of NFL teams

List of NFL teams

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DraftApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    DraftApi apiInstance = new DraftApi(defaultClient);
    try {
      List<DraftTeam> result = apiInstance.getNFLTeams();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DraftApi#getNFLTeams");
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

[**List&lt;DraftTeam&gt;**](DraftTeam.md)

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

