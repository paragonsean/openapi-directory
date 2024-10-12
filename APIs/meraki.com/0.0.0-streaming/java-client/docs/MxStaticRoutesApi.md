# MxStaticRoutesApi

All URIs are relative to *https://api.meraki.com/api/v0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkStaticRoute**](MxStaticRoutesApi.md#createNetworkStaticRoute) | **POST** /networks/{networkId}/staticRoutes | Add a static route for an MX or teleworker network |
| [**deleteNetworkStaticRoute**](MxStaticRoutesApi.md#deleteNetworkStaticRoute) | **DELETE** /networks/{networkId}/staticRoutes/{staticRouteId} | Delete a static route from an MX or teleworker network |
| [**getNetworkStaticRoute**](MxStaticRoutesApi.md#getNetworkStaticRoute) | **GET** /networks/{networkId}/staticRoutes/{staticRouteId} | Return a static route for an MX or teleworker network |
| [**getNetworkStaticRoutes**](MxStaticRoutesApi.md#getNetworkStaticRoutes) | **GET** /networks/{networkId}/staticRoutes | List the static routes for an MX or teleworker network |
| [**updateNetworkStaticRoute**](MxStaticRoutesApi.md#updateNetworkStaticRoute) | **PUT** /networks/{networkId}/staticRoutes/{staticRouteId} | Update a static route for an MX or teleworker network |


<a id="createNetworkStaticRoute"></a>
# **createNetworkStaticRoute**
> Object createNetworkStaticRoute(networkId, createNetworkStaticRouteRequest)

Add a static route for an MX or teleworker network

Add a static route for an MX or teleworker network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MxStaticRoutesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MxStaticRoutesApi apiInstance = new MxStaticRoutesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkStaticRouteRequest createNetworkStaticRouteRequest = new CreateNetworkStaticRouteRequest(); // CreateNetworkStaticRouteRequest | 
    try {
      Object result = apiInstance.createNetworkStaticRoute(networkId, createNetworkStaticRouteRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MxStaticRoutesApi#createNetworkStaticRoute");
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
| **networkId** | **String**|  | |
| **createNetworkStaticRouteRequest** | [**CreateNetworkStaticRouteRequest**](CreateNetworkStaticRouteRequest.md)|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="deleteNetworkStaticRoute"></a>
# **deleteNetworkStaticRoute**
> deleteNetworkStaticRoute(networkId, staticRouteId)

Delete a static route from an MX or teleworker network

Delete a static route from an MX or teleworker network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MxStaticRoutesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MxStaticRoutesApi apiInstance = new MxStaticRoutesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String staticRouteId = "staticRouteId_example"; // String | 
    try {
      apiInstance.deleteNetworkStaticRoute(networkId, staticRouteId);
    } catch (ApiException e) {
      System.err.println("Exception when calling MxStaticRoutesApi#deleteNetworkStaticRoute");
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
| **networkId** | **String**|  | |
| **staticRouteId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful operation |  -  |

<a id="getNetworkStaticRoute"></a>
# **getNetworkStaticRoute**
> Object getNetworkStaticRoute(networkId, staticRouteId)

Return a static route for an MX or teleworker network

Return a static route for an MX or teleworker network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MxStaticRoutesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MxStaticRoutesApi apiInstance = new MxStaticRoutesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String staticRouteId = "staticRouteId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkStaticRoute(networkId, staticRouteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MxStaticRoutesApi#getNetworkStaticRoute");
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
| **networkId** | **String**|  | |
| **staticRouteId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkStaticRoutes"></a>
# **getNetworkStaticRoutes**
> List&lt;Object&gt; getNetworkStaticRoutes(networkId)

List the static routes for an MX or teleworker network

List the static routes for an MX or teleworker network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MxStaticRoutesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MxStaticRoutesApi apiInstance = new MxStaticRoutesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkStaticRoutes(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MxStaticRoutesApi#getNetworkStaticRoutes");
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
| **networkId** | **String**|  | |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkStaticRoute"></a>
# **updateNetworkStaticRoute**
> Object updateNetworkStaticRoute(networkId, staticRouteId, updateNetworkStaticRouteRequest)

Update a static route for an MX or teleworker network

Update a static route for an MX or teleworker network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MxStaticRoutesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MxStaticRoutesApi apiInstance = new MxStaticRoutesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String staticRouteId = "staticRouteId_example"; // String | 
    UpdateNetworkStaticRouteRequest updateNetworkStaticRouteRequest = new UpdateNetworkStaticRouteRequest(); // UpdateNetworkStaticRouteRequest | 
    try {
      Object result = apiInstance.updateNetworkStaticRoute(networkId, staticRouteId, updateNetworkStaticRouteRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MxStaticRoutesApi#updateNetworkStaticRoute");
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
| **networkId** | **String**|  | |
| **staticRouteId** | **String**|  | |
| **updateNetworkStaticRouteRequest** | [**UpdateNetworkStaticRouteRequest**](UpdateNetworkStaticRouteRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

