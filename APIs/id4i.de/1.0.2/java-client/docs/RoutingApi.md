# RoutingApi

All URIs are relative to *http://backend.id4i.de*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAllRoutes**](RoutingApi.md#getAllRoutes) | **GET** /api/v1/routingfiles/{id4n}/routes/{type} | Retrieve all routes of a GUID (or ID4N) |
| [**getRoute**](RoutingApi.md#getRoute) | **GET** /api/v1/routingfiles/{id4n}/route/{type} | Retrieve current route of a GUID (or ID4N) |
| [**getRoutingFile**](RoutingApi.md#getRoutingFile) | **GET** /api/v1/routingfiles/{id4n} | Retrieve routing file |
| [**updateRoutingFile**](RoutingApi.md#updateRoutingFile) | **PUT** /api/v1/routingfiles/{id4n} | Store routing file |


<a id="getAllRoutes"></a>
# **getAllRoutes**
> List&lt;Route&gt; getAllRoutes(id4n, type, organizationId, interpolate)

Retrieve all routes of a GUID (or ID4N)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoutingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backend.id4i.de");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    RoutingApi apiInstance = new RoutingApi(defaultClient);
    String id4n = "id4n_example"; // String | id4n
    String type = "type_example"; // String | The type of route you want to have
    String organizationId = "organizationId_example"; // String | organizationId
    Boolean interpolate = true; // Boolean | interpolate
    try {
      List<Route> result = apiInstance.getAllRoutes(id4n, type, organizationId, interpolate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApi#getAllRoutes");
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
| **id4n** | **String**| id4n | |
| **type** | **String**| The type of route you want to have | |
| **organizationId** | **String**| organizationId | [optional] |
| **interpolate** | **Boolean**| interpolate | [optional] [default to true] |

### Return type

[**List&lt;Route&gt;**](Route.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method not allowed |  -  |
| **406** | Not Acceptable |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal Server Error |  -  |

<a id="getRoute"></a>
# **getRoute**
> Route getRoute(id4n, type, privateRoutes, publicRoutes, interpolate)

Retrieve current route of a GUID (or ID4N)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoutingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backend.id4i.de");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    RoutingApi apiInstance = new RoutingApi(defaultClient);
    String id4n = "id4n_example"; // String | id4n
    String type = "type_example"; // String | The type of route you want to have
    Boolean privateRoutes = true; // Boolean | privateRoutes
    Boolean publicRoutes = true; // Boolean | publicRoutes
    Boolean interpolate = true; // Boolean | interpolate
    try {
      Route result = apiInstance.getRoute(id4n, type, privateRoutes, publicRoutes, interpolate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApi#getRoute");
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
| **id4n** | **String**| id4n | |
| **type** | **String**| The type of route you want to have | |
| **privateRoutes** | **Boolean**| privateRoutes | [optional] [default to true] |
| **publicRoutes** | **Boolean**| publicRoutes | [optional] [default to true] |
| **interpolate** | **Boolean**| interpolate | [optional] [default to true] |

### Return type

[**Route**](Route.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method not allowed |  -  |
| **406** | Not Acceptable |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal Server Error |  -  |

<a id="getRoutingFile"></a>
# **getRoutingFile**
> RoutingFile getRoutingFile(id4n, organizationId)

Retrieve routing file

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoutingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backend.id4i.de");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    RoutingApi apiInstance = new RoutingApi(defaultClient);
    String id4n = "id4n_example"; // String | id4n
    String organizationId = "organizationId_example"; // String | organizationId
    try {
      RoutingFile result = apiInstance.getRoutingFile(id4n, organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApi#getRoutingFile");
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
| **id4n** | **String**| id4n | |
| **organizationId** | **String**| organizationId | [optional] |

### Return type

[**RoutingFile**](RoutingFile.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method not allowed |  -  |
| **406** | Not Acceptable |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal Server Error |  -  |

<a id="updateRoutingFile"></a>
# **updateRoutingFile**
> updateRoutingFile(id4n, routingFileRequest)

Store routing file

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoutingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backend.id4i.de");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    RoutingApi apiInstance = new RoutingApi(defaultClient);
    String id4n = "id4n_example"; // String | id4n
    RoutingFileRequest routingFileRequest = new RoutingFileRequest(); // RoutingFileRequest | rfr
    try {
      apiInstance.updateRoutingFile(id4n, routingFileRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApi#updateRoutingFile");
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
| **id4n** | **String**| id4n | |
| **routingFileRequest** | [**RoutingFileRequest**](RoutingFileRequest.md)| rfr | |

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method not allowed |  -  |
| **406** | Not Acceptable |  -  |
| **409** | Conflict |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal Server Error |  -  |

