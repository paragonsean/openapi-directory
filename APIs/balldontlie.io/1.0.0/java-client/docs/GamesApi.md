# GamesApi

All URIs are relative to *https://balldontlie.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**allGamesExampleParameters**](GamesApi.md#allGamesExampleParameters) | **GET** /api/v1/games | all games (example parameters) |
| [**specificGame**](GamesApi.md#specificGame) | **GET** /api/v1/games/32881 | specific game |


<a id="allGamesExampleParameters"></a>
# **allGamesExampleParameters**
> allGamesExampleParameters(seasons, teamIds)

all games (example parameters)

all games (example parameters)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GamesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://balldontlie.io");

    GamesApi apiInstance = new GamesApi(defaultClient);
    String seasons = "2018"; // String | 
    String teamIds = "1"; // String | 
    try {
      apiInstance.allGamesExampleParameters(seasons, teamIds);
    } catch (ApiException e) {
      System.err.println("Exception when calling GamesApi#allGamesExampleParameters");
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
| **seasons** | **String**|  | [optional] |
| **teamIds** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="specificGame"></a>
# **specificGame**
> specificGame()

specific game

specific game

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GamesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://balldontlie.io");

    GamesApi apiInstance = new GamesApi(defaultClient);
    try {
      apiInstance.specificGame();
    } catch (ApiException e) {
      System.err.println("Exception when calling GamesApi#specificGame");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

