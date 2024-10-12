# PlayersApi

All URIs are relative to *https://balldontlie.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**allPlayersSearch**](PlayersApi.md#allPlayersSearch) | **GET** /api/v1/players | all players (search) |
| [**specificPlayer**](PlayersApi.md#specificPlayer) | **GET** /api/v1/players/237 | specific player |


<a id="allPlayersSearch"></a>
# **allPlayersSearch**
> allPlayersSearch(search)

all players (search)

all players (search)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlayersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://balldontlie.io");

    PlayersApi apiInstance = new PlayersApi(defaultClient);
    String search = "lebron"; // String | 
    try {
      apiInstance.allPlayersSearch(search);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlayersApi#allPlayersSearch");
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
| **search** | **String**|  | [optional] |

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

<a id="specificPlayer"></a>
# **specificPlayer**
> specificPlayer()

specific player

specific player

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlayersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://balldontlie.io");

    PlayersApi apiInstance = new PlayersApi(defaultClient);
    try {
      apiInstance.specificPlayer();
    } catch (ApiException e) {
      System.err.println("Exception when calling PlayersApi#specificPlayer");
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

