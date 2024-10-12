# PiecesApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV2PiecesGet**](PiecesApi.md#apiV2PiecesGet) | **GET** /api/v2/pieces | Returns the pieces matching the query parameters. |
| [**apiV2PiecesIdDelete**](PiecesApi.md#apiV2PiecesIdDelete) | **DELETE** /api/v2/pieces/{id} | Deletes the piece with the given ID. |
| [**apiV2PiecesIdGet**](PiecesApi.md#apiV2PiecesIdGet) | **GET** /api/v2/pieces/{id} | Returns the piece matching the given ID. |
| [**apiV2PiecesPost**](PiecesApi.md#apiV2PiecesPost) | **POST** /api/v2/pieces | Create a new piece. |


<a id="apiV2PiecesGet"></a>
# **apiV2PiecesGet**
> List&lt;Piece&gt; apiV2PiecesGet(episodeId)

Returns the pieces matching the query parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PiecesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: cd_oauth2
    OAuth cd_oauth2 = (OAuth) defaultClient.getAuthentication("cd_oauth2");
    cd_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PiecesApi apiInstance = new PiecesApi(defaultClient);
    Long episodeId = 56L; // Long | The ID of the episode that owns the piece.
    try {
      List<Piece> result = apiInstance.apiV2PiecesGet(episodeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PiecesApi#apiV2PiecesGet");
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
| **episodeId** | **Long**| The ID of the episode that owns the piece. | |

### Return type

[**List&lt;Piece&gt;**](Piece.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The pieces matching the query parameters |  -  |
| **403** | Authorization failed, Username or password not found or incorrect. |  -  |
| **404** | Either the pieces or the episode aren&#39;t found. |  -  |

<a id="apiV2PiecesIdDelete"></a>
# **apiV2PiecesIdDelete**
> apiV2PiecesIdDelete(id)

Deletes the piece with the given ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PiecesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: cd_oauth2
    OAuth cd_oauth2 = (OAuth) defaultClient.getAuthentication("cd_oauth2");
    cd_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PiecesApi apiInstance = new PiecesApi(defaultClient);
    Long id = 56L; // Long | 
    try {
      apiInstance.apiV2PiecesIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling PiecesApi#apiV2PiecesIdDelete");
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
| **id** | **Long**|  | |

### Return type

null (empty response body)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The piece was deleted. |  -  |
| **403** | The user isn&#39;t permitted to delete the piece. |  -  |
| **404** | The piece isn&#39;t found. |  -  |

<a id="apiV2PiecesIdGet"></a>
# **apiV2PiecesIdGet**
> Piece apiV2PiecesIdGet(id)

Returns the piece matching the given ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PiecesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: cd_oauth2
    OAuth cd_oauth2 = (OAuth) defaultClient.getAuthentication("cd_oauth2");
    cd_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PiecesApi apiInstance = new PiecesApi(defaultClient);
    Long id = 56L; // Long | 
    try {
      Piece result = apiInstance.apiV2PiecesIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PiecesApi#apiV2PiecesIdGet");
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
| **id** | **Long**|  | |

### Return type

[**Piece**](Piece.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The piece with the given ID. |  -  |
| **403** | Authorization failed |  -  |
| **404** | The piece isn&#39;t found or the user doesn&#39;t have permission to get it. |  -  |

<a id="apiV2PiecesPost"></a>
# **apiV2PiecesPost**
> Piece apiV2PiecesPost(piece)

Create a new piece.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PiecesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: cd_oauth2
    OAuth cd_oauth2 = (OAuth) defaultClient.getAuthentication("cd_oauth2");
    cd_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PiecesApi apiInstance = new PiecesApi(defaultClient);
    Piece piece = new Piece(); // Piece | 
    try {
      Piece result = apiInstance.apiV2PiecesPost(piece);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PiecesApi#apiV2PiecesPost");
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
| **piece** | [**Piece**](Piece.md)|  | [optional] |

### Return type

[**Piece**](Piece.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The created piece with fields populated. |  -  |
| **400** | If the request is missing required data or invalid. |  -  |
| **403** | The user isn&#39;t permitted to create the piece. |  -  |

