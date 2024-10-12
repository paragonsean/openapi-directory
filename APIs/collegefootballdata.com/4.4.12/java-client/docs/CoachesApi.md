# CoachesApi

All URIs are relative to *https://api.collegefootballdata.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCoaches**](CoachesApi.md#getCoaches) | **GET** /coaches | Coaching records and history |


<a id="getCoaches"></a>
# **getCoaches**
> List&lt;Coach&gt; getCoaches(firstName, lastName, team, year, minYear, maxYear)

Coaching records and history

Coaching history

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CoachesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    CoachesApi apiInstance = new CoachesApi(defaultClient);
    String firstName = "firstName_example"; // String | First name filter
    String lastName = "lastName_example"; // String | Last name filter
    String team = "team_example"; // String | Team name filter
    Integer year = 56; // Integer | Year filter
    Integer minYear = 56; // Integer | Minimum year filter (inclusive)
    Integer maxYear = 56; // Integer | Maximum year filter (inclusive)
    try {
      List<Coach> result = apiInstance.getCoaches(firstName, lastName, team, year, minYear, maxYear);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CoachesApi#getCoaches");
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
| **firstName** | **String**| First name filter | [optional] |
| **lastName** | **String**| Last name filter | [optional] |
| **team** | **String**| Team name filter | [optional] |
| **year** | **Integer**| Year filter | [optional] |
| **minYear** | **Integer**| Minimum year filter (inclusive) | [optional] |
| **maxYear** | **Integer**| Maximum year filter (inclusive) | [optional] |

### Return type

[**List&lt;Coach&gt;**](Coach.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

