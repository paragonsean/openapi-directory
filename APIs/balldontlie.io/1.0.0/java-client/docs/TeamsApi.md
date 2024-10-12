# TeamsApi

All URIs are relative to *https://balldontlie.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**allTeams**](TeamsApi.md#allTeams) | **GET** /api/v1/teams | all teams |
| [**specificTeam**](TeamsApi.md#specificTeam) | **GET** /api/v1/teams/1 | specific team |


<a id="allTeams"></a>
# **allTeams**
> allTeams()

all teams

all teams

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://balldontlie.io");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    try {
      apiInstance.allTeams();
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#allTeams");
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

<a id="specificTeam"></a>
# **specificTeam**
> specificTeam()

specific team

specific team

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://balldontlie.io");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    try {
      apiInstance.specificTeam();
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#specificTeam");
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

