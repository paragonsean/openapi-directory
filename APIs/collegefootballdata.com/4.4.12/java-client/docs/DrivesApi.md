# DrivesApi

All URIs are relative to *https://api.collegefootballdata.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDrives**](DrivesApi.md#getDrives) | **GET** /drives | Drive data and results |


<a id="getDrives"></a>
# **getDrives**
> List&lt;Drive&gt; getDrives(year, seasonType, week, team, offense, defense, conference, offenseConference, defenseConference, classification)

Drive data and results

Get game drives

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DrivesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    DrivesApi apiInstance = new DrivesApi(defaultClient);
    Integer year = 56; // Integer | Year filter
    String seasonType = "regular"; // String | Season type filter
    Integer week = 56; // Integer | Week filter
    String team = "team_example"; // String | Team filter
    String offense = "offense_example"; // String | Offensive team filter
    String defense = "defense_example"; // String | Defensive team filter
    String conference = "conference_example"; // String | Conference filter
    String offenseConference = "offenseConference_example"; // String | Offensive conference filter
    String defenseConference = "defenseConference_example"; // String | Defensive conference filter
    String classification = "classification_example"; // String | Division classification filter (fbs/fcs/ii/iii)
    try {
      List<Drive> result = apiInstance.getDrives(year, seasonType, week, team, offense, defense, conference, offenseConference, defenseConference, classification);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DrivesApi#getDrives");
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
| **year** | **Integer**| Year filter | |
| **seasonType** | **String**| Season type filter | [optional] [default to regular] |
| **week** | **Integer**| Week filter | [optional] |
| **team** | **String**| Team filter | [optional] |
| **offense** | **String**| Offensive team filter | [optional] |
| **defense** | **String**| Defensive team filter | [optional] |
| **conference** | **String**| Conference filter | [optional] |
| **offenseConference** | **String**| Offensive conference filter | [optional] |
| **defenseConference** | **String**| Defensive conference filter | [optional] |
| **classification** | **String**| Division classification filter (fbs/fcs/ii/iii) | [optional] |

### Return type

[**List&lt;Drive&gt;**](Drive.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

