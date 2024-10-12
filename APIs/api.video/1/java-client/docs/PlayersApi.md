# PlayersApi

All URIs are relative to *https://ws.api.video*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dELETEPlayersPlayerId**](PlayersApi.md#dELETEPlayersPlayerId) | **DELETE** /players/{playerId} | Delete a player |
| [**dELETEPlayersPlayerIdLogo**](PlayersApi.md#dELETEPlayersPlayerIdLogo) | **DELETE** /players/{playerId}/logo | Delete logo |
| [**gETPlayers**](PlayersApi.md#gETPlayers) | **GET** /players | List all players |
| [**gETPlayersPlayerId**](PlayersApi.md#gETPlayersPlayerId) | **GET** /players/{playerId} | Show a player |
| [**pATCHPlayersPlayerId**](PlayersApi.md#pATCHPlayersPlayerId) | **PATCH** /players/{playerId} | Update a player |
| [**pOSTPlayers**](PlayersApi.md#pOSTPlayers) | **POST** /players | Create a player |
| [**pOSTPlayersPlayerIdLogo**](PlayersApi.md#pOSTPlayersPlayerIdLogo) | **POST** /players/{playerId}/logo | Upload a logo |


<a id="dELETEPlayersPlayerId"></a>
# **dELETEPlayersPlayerId**
> dELETEPlayersPlayerId(playerId)

Delete a player

Delete a player if you no longer need it. You can delete any player that you have the player ID for.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlayersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ws.api.video");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    PlayersApi apiInstance = new PlayersApi(defaultClient);
    String playerId = "pl45d5vFFGrfdsdsd156dGhh"; // String | The unique identifier for the player you want to delete.
    try {
      apiInstance.dELETEPlayersPlayerId(playerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlayersApi#dELETEPlayersPlayerId");
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
| **playerId** | **String**| The unique identifier for the player you want to delete. | |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **404** | Not Found |  -  |

<a id="dELETEPlayersPlayerIdLogo"></a>
# **dELETEPlayersPlayerIdLogo**
> Object dELETEPlayersPlayerIdLogo(playerId)

Delete logo

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlayersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ws.api.video");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    PlayersApi apiInstance = new PlayersApi(defaultClient);
    String playerId = "pl14Db6oMJRH6SRVoOwORacK"; // String | The unique identifier for the player.
    try {
      Object result = apiInstance.dELETEPlayersPlayerIdLogo(playerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlayersApi#dELETEPlayersPlayerIdLogo");
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
| **playerId** | **String**| The unique identifier for the player. | |

### Return type

**Object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **404** | Not Found |  -  |

<a id="gETPlayers"></a>
# **gETPlayers**
> PlayersListResponse gETPlayers().sortBy(sortBy).sortOrder(sortOrder).currentPage(currentPage).pageSize(pageSize).execute();

List all players

Retrieve a list of all the players you created, as well as details about each one. Tutorials that use the [player endpoint](https://api.video/blog/endpoints/player).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlayersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ws.api.video");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    PlayersApi apiInstance = new PlayersApi(defaultClient);
    String sortBy = "createdAt"; // String | createdAt is the time the player was created. updatedAt is the time the player was last updated. The time is presented in ISO-8601 format.
    String sortOrder = "asc"; // String | Allowed: asc, desc. Ascending for date and time means that earlier values precede later ones. Descending means that later values preced earlier ones.
    Integer currentPage = 1; // Integer | Choose the number of search results to return per page. Minimum value: 1
    Integer pageSize = 25; // Integer | Results per page. Allowed values 1-100, default is 25.
    try {
      PlayersListResponse result = apiInstance.gETPlayers()
            .sortBy(sortBy)
            .sortOrder(sortOrder)
            .currentPage(currentPage)
            .pageSize(pageSize)
            .execute();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlayersApi#gETPlayers");
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
| **sortBy** | **String**| createdAt is the time the player was created. updatedAt is the time the player was last updated. The time is presented in ISO-8601 format. | [optional] [enum: createdAt, updatedAt] |
| **sortOrder** | **String**| Allowed: asc, desc. Ascending for date and time means that earlier values precede later ones. Descending means that later values preced earlier ones. | [optional] [enum: asc, desc] |
| **currentPage** | **Integer**| Choose the number of search results to return per page. Minimum value: 1 | [optional] [default to 1] |
| **pageSize** | **Integer**| Results per page. Allowed values 1-100, default is 25. | [optional] [default to 25] |

### Return type

[**PlayersListResponse**](PlayersListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="gETPlayersPlayerId"></a>
# **gETPlayersPlayerId**
> Player gETPlayersPlayerId(playerId)

Show a player

Use a player ID to retrieve details about the player and display it for viewers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlayersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ws.api.video");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    PlayersApi apiInstance = new PlayersApi(defaultClient);
    String playerId = "pl45d5vFFGrfdsdsd156dGhh"; // String | The unique identifier for the player you want to retrieve. 
    try {
      Player result = apiInstance.gETPlayersPlayerId(playerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlayersApi#gETPlayersPlayerId");
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
| **playerId** | **String**| The unique identifier for the player you want to retrieve.  | |

### Return type

[**Player**](Player.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Not Found |  -  |

<a id="pATCHPlayersPlayerId"></a>
# **pATCHPlayersPlayerId**
> Player pATCHPlayersPlayerId(playerId, playerUpdatePayload)

Update a player

Use a player ID to update specific details for a player. NOTE: It may take up to 10 min before the new player configuration is available from our CDN.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlayersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ws.api.video");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    PlayersApi apiInstance = new PlayersApi(defaultClient);
    String playerId = "pl45d5vFFGrfdsdsd156dGhh"; // String | The unique identifier for the player.
    PlayerUpdatePayload playerUpdatePayload = new PlayerUpdatePayload(); // PlayerUpdatePayload | 
    try {
      Player result = apiInstance.pATCHPlayersPlayerId(playerId, playerUpdatePayload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlayersApi#pATCHPlayersPlayerId");
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
| **playerId** | **String**| The unique identifier for the player. | |
| **playerUpdatePayload** | [**PlayerUpdatePayload**](PlayerUpdatePayload.md)|  | |

### Return type

[**Player**](Player.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Not Found |  -  |

<a id="pOSTPlayers"></a>
# **pOSTPlayers**
> Player pOSTPlayers(playerCreationPayload)

Create a player

Create a player for your video, and customise it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlayersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ws.api.video");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    PlayersApi apiInstance = new PlayersApi(defaultClient);
    PlayerCreationPayload playerCreationPayload = new PlayerCreationPayload(); // PlayerCreationPayload | 
    try {
      Player result = apiInstance.pOSTPlayers(playerCreationPayload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlayersApi#pOSTPlayers");
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
| **playerCreationPayload** | [**PlayerCreationPayload**](PlayerCreationPayload.md)|  | |

### Return type

[**Player**](Player.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="pOSTPlayersPlayerIdLogo"></a>
# **pOSTPlayersPlayerIdLogo**
> Player pOSTPlayersPlayerIdLogo(playerId, _file, link)

Upload a logo

The uploaded image maximum size should be 200x100 and its weight should be 200KB.  It will be scaled down to 30px height and converted to PNG to be displayed in the player.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlayersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ws.api.video");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    PlayersApi apiInstance = new PlayersApi(defaultClient);
    String playerId = "pl14Db6oMJRH6SRVoOwORacK"; // String | The unique identifier for the player.
    File _file = new File("/path/to/file"); // File | The name of the file you want to use for your logo.
    String link = "link_example"; // String | The path to the file you want to upload and use as a logo.
    try {
      Player result = apiInstance.pOSTPlayersPlayerIdLogo(playerId, _file, link);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlayersApi#pOSTPlayersPlayerIdLogo");
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
| **playerId** | **String**| The unique identifier for the player. | |
| **_file** | **File**| The name of the file you want to use for your logo. | |
| **link** | **String**| The path to the file you want to upload and use as a logo. | |

### Return type

[**Player**](Player.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

