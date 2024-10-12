# RouteApi

All URIs are relative to *https://api.turbinelabs.io/v1.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**routeGet**](RouteApi.md#routeGet) | **GET** /route | get routes |
| [**routePost**](RouteApi.md#routePost) | **POST** /route | create route |
| [**routeRouteKeyDelete**](RouteApi.md#routeRouteKeyDelete) | **DELETE** /route/{routeKey} | delete route |
| [**routeRouteKeyGet**](RouteApi.md#routeRouteKeyGet) | **GET** /route/{routeKey} | get route |
| [**routeRouteKeyPut**](RouteApi.md#routeRouteKeyPut) | **PUT** /route/{routeKey} | modify route |
| [**sharedRulesSharedRulesKeyDelete**](RouteApi.md#sharedRulesSharedRulesKeyDelete) | **DELETE** /shared_rules/{sharedRulesKey} | delete shared_rules object |


<a id="routeGet"></a>
# **routeGet**
> MultiRouteResult routeGet(filters)

get routes

Get a list of routes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RouteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RouteApi apiInstance = new RouteApi(defaultClient);
    String filters = "filters_example"; // String | A JSON encoded array of RouteFilter objects. The filter is taken as a union of intersections. In other words an object that matches every constraint in any RouteFilter will be included. 
    try {
      MultiRouteResult result = apiInstance.routeGet(filters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RouteApi#routeGet");
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
| **filters** | **String**| A JSON encoded array of RouteFilter objects. The filter is taken as a union of intersections. In other words an object that matches every constraint in any RouteFilter will be included.  | [optional] |

### Return type

[**MultiRouteResult**](MultiRouteResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | a result containing a list of routes |  -  |
| **0** | Unexpected error |  -  |

<a id="routePost"></a>
# **routePost**
> RouteResult routePost(route)

create route

Create a new route

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RouteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RouteApi apiInstance = new RouteApi(defaultClient);
    RouteCreate route = new RouteCreate(); // RouteCreate | the route to create
    try {
      RouteResult result = apiInstance.routePost(route);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RouteApi#routePost");
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
| **route** | [**RouteCreate**](RouteCreate.md)| the route to create | |

### Return type

[**RouteResult**](RouteResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the newly created route |  -  |
| **0** | Unexpected error |  -  |

<a id="routeRouteKeyDelete"></a>
# **routeRouteKeyDelete**
> Object routeRouteKeyDelete(routeKey, checksum)

delete route

Delete an existing route

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RouteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RouteApi apiInstance = new RouteApi(defaultClient);
    String routeKey = "1c7b1c5e-1a23-4d04-5cb4-eccea4d5994c"; // String | the route key
    String checksum = "9cd24183-f848-48f8-6f55-0f07240700b9"; // String | the current checksum of the route to be deleted
    try {
      Object result = apiInstance.routeRouteKeyDelete(routeKey, checksum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RouteApi#routeRouteKeyDelete");
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
| **routeKey** | **String**| the route key | |
| **checksum** | **String**| the current checksum of the route to be deleted | |

### Return type

**Object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | an empty result |  -  |
| **0** | Unexpected error |  -  |

<a id="routeRouteKeyGet"></a>
# **routeRouteKeyGet**
> RouteResult routeRouteKeyGet(routeKey)

get route

Get details for an existing route

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RouteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RouteApi apiInstance = new RouteApi(defaultClient);
    String routeKey = "1c7b1c5e-1a23-4d04-5cb4-eccea4d5994c"; // String | the route key
    try {
      RouteResult result = apiInstance.routeRouteKeyGet(routeKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RouteApi#routeRouteKeyGet");
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
| **routeKey** | **String**| the route key | |

### Return type

[**RouteResult**](RouteResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | a result containing a single route |  -  |
| **0** | Unexpected error |  -  |

<a id="routeRouteKeyPut"></a>
# **routeRouteKeyPut**
> RouteResult routeRouteKeyPut(routeKey, route)

modify route

Modify an existing route

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RouteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RouteApi apiInstance = new RouteApi(defaultClient);
    String routeKey = "1c7b1c5e-1a23-4d04-5cb4-eccea4d5994c"; // String | the route key
    Route route = new Route(); // Route | the route to modify
    try {
      RouteResult result = apiInstance.routeRouteKeyPut(routeKey, route);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RouteApi#routeRouteKeyPut");
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
| **routeKey** | **String**| the route key | |
| **route** | [**Route**](Route.md)| the route to modify | |

### Return type

[**RouteResult**](RouteResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A result containing the modified route |  -  |
| **0** | Unexpected error |  -  |

<a id="sharedRulesSharedRulesKeyDelete"></a>
# **sharedRulesSharedRulesKeyDelete**
> Object sharedRulesSharedRulesKeyDelete(sharedRulesKey, checksum)

delete shared_rules object

Delete an existing shared_rules object

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RouteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RouteApi apiInstance = new RouteApi(defaultClient);
    String sharedRulesKey = "1c7b1c5e-1a23-4d04-5cb4-eccea4d5994c"; // String | the shared_rules key
    String checksum = "9cd24183-f848-48f8-6f55-0f07240700b9"; // String | the current checksum of the shared_rules to be deleted
    try {
      Object result = apiInstance.sharedRulesSharedRulesKeyDelete(sharedRulesKey, checksum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RouteApi#sharedRulesSharedRulesKeyDelete");
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
| **sharedRulesKey** | **String**| the shared_rules key | |
| **checksum** | **String**| the current checksum of the shared_rules to be deleted | |

### Return type

**Object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | an empty result |  -  |
| **0** | Unexpected error |  -  |

