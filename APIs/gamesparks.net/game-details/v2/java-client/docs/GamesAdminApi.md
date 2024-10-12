# GamesAdminApi

All URIs are relative to *http://config2.gamesparks.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getGamesEndpointsUsingGET**](GamesAdminApi.md#getGamesEndpointsUsingGET) | **GET** /restv2/game/{apiKey}/endpoints | getGamesEndpoints |
| [**listDeletedUsingGET**](GamesAdminApi.md#listDeletedUsingGET) | **GET** /restv2/games/deleted | listDeleted |
| [**listUsingGET**](GamesAdminApi.md#listUsingGET) | **GET** /restv2/games | list |
| [**restoreDeletedGameUsingPOST**](GamesAdminApi.md#restoreDeletedGameUsingPOST) | **POST** /restv2/game/{apiKey}/restore | restoreDeletedGame |


<a id="getGamesEndpointsUsingGET"></a>
# **getGamesEndpointsUsingGET**
> GameEndpointsModel getGamesEndpointsUsingGET(apiKey)

getGamesEndpoints

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GamesAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    GamesAdminApi apiInstance = new GamesAdminApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    try {
      GameEndpointsModel result = apiInstance.getGamesEndpointsUsingGET(apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GamesAdminApi#getGamesEndpointsUsingGET");
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
| **apiKey** | **String**| apiKey | |

### Return type

[**GameEndpointsModel**](GameEndpointsModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="listDeletedUsingGET"></a>
# **listDeletedUsingGET**
> List&lt;DeletedGameModel&gt; listDeletedUsingGET()

listDeleted

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GamesAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    GamesAdminApi apiInstance = new GamesAdminApi(defaultClient);
    try {
      List<DeletedGameModel> result = apiInstance.listDeletedUsingGET();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GamesAdminApi#listDeletedUsingGET");
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

[**List&lt;DeletedGameModel&gt;**](DeletedGameModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="listUsingGET"></a>
# **listUsingGET**
> List&lt;GameModel&gt; listUsingGET()

list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GamesAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    GamesAdminApi apiInstance = new GamesAdminApi(defaultClient);
    try {
      List<GameModel> result = apiInstance.listUsingGET();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GamesAdminApi#listUsingGET");
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

[**List&lt;GameModel&gt;**](GameModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="restoreDeletedGameUsingPOST"></a>
# **restoreDeletedGameUsingPOST**
> MessageModel restoreDeletedGameUsingPOST(apiKey)

restoreDeletedGame

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GamesAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    GamesAdminApi apiInstance = new GamesAdminApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    try {
      MessageModel result = apiInstance.restoreDeletedGameUsingPOST(apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GamesAdminApi#restoreDeletedGameUsingPOST");
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
| **apiKey** | **String**| apiKey | |

### Return type

[**MessageModel**](MessageModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

