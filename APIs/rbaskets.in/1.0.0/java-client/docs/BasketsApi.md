# BasketsApi

All URIs are relative to *https://rbaskets.in*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiBasketsGet**](BasketsApi.md#apiBasketsGet) | **GET** /api/baskets | Get baskets |
| [**apiBasketsNameDelete**](BasketsApi.md#apiBasketsNameDelete) | **DELETE** /api/baskets/{name} | Delete basket |
| [**apiBasketsNameGet**](BasketsApi.md#apiBasketsNameGet) | **GET** /api/baskets/{name} | Get basket settings |
| [**apiBasketsNamePost**](BasketsApi.md#apiBasketsNamePost) | **POST** /api/baskets/{name} | Create new basket |
| [**apiBasketsNamePut**](BasketsApi.md#apiBasketsNamePut) | **PUT** /api/baskets/{name} | Update basket settings |
| [**apiStatsGet**](BasketsApi.md#apiStatsGet) | **GET** /api/stats | Get baskets statistics |
| [**basketsGet**](BasketsApi.md#basketsGet) | **GET** /baskets | Get baskets |
| [**basketsNameDelete**](BasketsApi.md#basketsNameDelete) | **DELETE** /baskets/{name} | Delete basket |
| [**basketsNameGet**](BasketsApi.md#basketsNameGet) | **GET** /baskets/{name} | Get basket settings |
| [**basketsNamePost**](BasketsApi.md#basketsNamePost) | **POST** /baskets/{name} | Create new basket |
| [**basketsNamePut**](BasketsApi.md#basketsNamePut) | **PUT** /baskets/{name} | Update basket settings |


<a id="apiBasketsGet"></a>
# **apiBasketsGet**
> Baskets apiBasketsGet(max, skip, q)

Get baskets

Fetches a list of basket names managed by service. Require master token.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BasketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rbaskets.in");
    
    // Configure API key authorization: service_token
    ApiKeyAuth service_token = (ApiKeyAuth) defaultClient.getAuthentication("service_token");
    service_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //service_token.setApiKeyPrefix("Token");

    BasketsApi apiInstance = new BasketsApi(defaultClient);
    Integer max = 56; // Integer | Maximum number of basket names to return; default 20
    Integer skip = 56; // Integer | Number of basket names to skip; default 0
    String q = "q_example"; // String | Query string to filter result, only those basket names that match the query will be included in response
    try {
      Baskets result = apiInstance.apiBasketsGet(max, skip, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BasketsApi#apiBasketsGet");
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
| **max** | **Integer**| Maximum number of basket names to return; default 20 | [optional] |
| **skip** | **Integer**| Number of basket names to skip; default 0 | [optional] |
| **q** | **String**| Query string to filter result, only those basket names that match the query will be included in response | [optional] |

### Return type

[**Baskets**](Baskets.md)

### Authorization

[service_token](../README.md#service_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Returns list of available baskets. |  -  |
| **204** | No Content. No baskets available for specified limits |  -  |
| **401** | Unauthorized. Invalid or missing master token |  -  |

<a id="apiBasketsNameDelete"></a>
# **apiBasketsNameDelete**
> apiBasketsNameDelete(name)

Delete basket

Permanently deletes this basket and all collected requests.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BasketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rbaskets.in");
    
    // Configure API key authorization: basket_token
    ApiKeyAuth basket_token = (ApiKeyAuth) defaultClient.getAuthentication("basket_token");
    basket_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //basket_token.setApiKeyPrefix("Token");

    BasketsApi apiInstance = new BasketsApi(defaultClient);
    String name = "name_example"; // String | The basket name
    try {
      apiInstance.apiBasketsNameDelete(name);
    } catch (ApiException e) {
      System.err.println("Exception when calling BasketsApi#apiBasketsNameDelete");
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
| **name** | **String**| The basket name | |

### Return type

null (empty response body)

### Authorization

[basket_token](../README.md#basket_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content. Basket is deleted |  -  |
| **401** | Unauthorized. Invalid or missing basket token |  -  |
| **404** | Not Found. No basket with such name |  -  |

<a id="apiBasketsNameGet"></a>
# **apiBasketsNameGet**
> Config apiBasketsNameGet(name)

Get basket settings

Retrieves configuration settings of this basket.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BasketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rbaskets.in");
    
    // Configure API key authorization: basket_token
    ApiKeyAuth basket_token = (ApiKeyAuth) defaultClient.getAuthentication("basket_token");
    basket_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //basket_token.setApiKeyPrefix("Token");

    BasketsApi apiInstance = new BasketsApi(defaultClient);
    String name = "name_example"; // String | The basket name
    try {
      Config result = apiInstance.apiBasketsNameGet(name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BasketsApi#apiBasketsNameGet");
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
| **name** | **String**| The basket name | |

### Return type

[**Config**](Config.md)

### Authorization

[basket_token](../README.md#basket_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Returns basket configuration |  -  |
| **401** | Unauthorized. Invalid or missing basket token |  -  |
| **404** | Not Found. No basket with such name |  -  |

<a id="apiBasketsNamePost"></a>
# **apiBasketsNamePost**
> Token apiBasketsNamePost(name, config)

Create new basket

Creates a new basket with this name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BasketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rbaskets.in");

    BasketsApi apiInstance = new BasketsApi(defaultClient);
    String name = "name_example"; // String | The name of new basket
    Config config = new Config(); // Config | Basket configuration
    try {
      Token result = apiInstance.apiBasketsNamePost(name, config);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BasketsApi#apiBasketsNamePost");
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
| **name** | **String**| The name of new basket | |
| **config** | [**Config**](Config.md)| Basket configuration | [optional] |

### Return type

[**Token**](Token.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created. Indicates that basket is successfully created |  -  |
| **400** | Bad Request. Failed to parse JSON into basket configuration object. |  -  |
| **403** | Forbidden. Indicates that basket name conflicts with reserved paths; e.g. &#x60;baskets&#x60;, &#x60;web&#x60;, etc. |  -  |
| **409** | Conflict. Indicates that basket with such name already exists |  -  |
| **422** | Unprocessable Entity. Basket configuration is not valid. |  -  |

<a id="apiBasketsNamePut"></a>
# **apiBasketsNamePut**
> apiBasketsNamePut(name, config)

Update basket settings

Updates configuration settings of this basket.  Special configuration parameters for request forwarding:   * &#x60;insecure_tls&#x60; controls certificate verification when forwarding requests. Setting this parameter to &#x60;true&#x60;   allows to forward collected HTTP requests via HTTPS protocol even if the forward end-point is configured with   self-signed TLS/SSL certificate. **Warning:** enabling this feature has known security implications.   * &#x60;expand_path&#x60; changes the logic of constructing taget URL when forwarding requests. If this parameter is   set to &#x60;true&#x60; the forward URL path will be expanded when original HTTP request contains compound path. For   example, a basket with name **server1** is configured to forward all requests to &#x60;http://server1.intranet:8001/myservice&#x60;   and it has received an HTTP request like &#x60;GET http://baskets.example.com/server1/component/123/events?status&#x3D;OK&#x60;   then depending on &#x60;expand_path&#x60; settings the request will be forwarded to:     * &#x60;true&#x60; &#x3D;&gt; &#x60;GET http://server1.intranet:8001/myservice/component/123/events?status&#x3D;OK&#x60;     * &#x60;false&#x60; &#x3D;&gt; &#x60;GET http://server1.intranet:8001/myservice?status&#x3D;OK&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BasketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rbaskets.in");
    
    // Configure API key authorization: basket_token
    ApiKeyAuth basket_token = (ApiKeyAuth) defaultClient.getAuthentication("basket_token");
    basket_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //basket_token.setApiKeyPrefix("Token");

    BasketsApi apiInstance = new BasketsApi(defaultClient);
    String name = "name_example"; // String | The basket name
    Config config = new Config(); // Config | New configuration to apply
    try {
      apiInstance.apiBasketsNamePut(name, config);
    } catch (ApiException e) {
      System.err.println("Exception when calling BasketsApi#apiBasketsNamePut");
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
| **name** | **String**| The basket name | |
| **config** | [**Config**](Config.md)| New configuration to apply | |

### Return type

null (empty response body)

### Authorization

[basket_token](../README.md#basket_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content. Basket configuration is updated |  -  |
| **400** | Bad Request. Failed to parse JSON into basket configuration object. |  -  |
| **401** | Unauthorized. Invalid or missing basket token |  -  |
| **404** | Not Found. No basket with such name |  -  |
| **422** | Unprocessable Entity. Basket configuration is not valid. |  -  |

<a id="apiStatsGet"></a>
# **apiStatsGet**
> ServiceStats apiStatsGet(max)

Get baskets statistics

Get service statistics about baskets and collected HTTP requests. Require master token.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BasketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rbaskets.in");
    
    // Configure API key authorization: service_token
    ApiKeyAuth service_token = (ApiKeyAuth) defaultClient.getAuthentication("service_token");
    service_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //service_token.setApiKeyPrefix("Token");

    BasketsApi apiInstance = new BasketsApi(defaultClient);
    Integer max = 56; // Integer | Maximum number of basket names to return; default 5
    try {
      ServiceStats result = apiInstance.apiStatsGet(max);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BasketsApi#apiStatsGet");
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
| **max** | **Integer**| Maximum number of basket names to return; default 5 | [optional] |

### Return type

[**ServiceStats**](ServiceStats.md)

### Authorization

[service_token](../README.md#service_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Returns service statistics. |  -  |
| **401** | Unauthorized. Invalid or missing master token |  -  |

<a id="basketsGet"></a>
# **basketsGet**
> Baskets basketsGet(max, skip, q)

Get baskets

Fetches a list of basket names managed by service. Require master token.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BasketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rbaskets.in");
    
    // Configure API key authorization: service_token
    ApiKeyAuth service_token = (ApiKeyAuth) defaultClient.getAuthentication("service_token");
    service_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //service_token.setApiKeyPrefix("Token");

    BasketsApi apiInstance = new BasketsApi(defaultClient);
    Integer max = 56; // Integer | Maximum number of basket names to return; default 20
    Integer skip = 56; // Integer | Number of basket names to skip; default 0
    String q = "q_example"; // String | Query string to filter result, only those basket names that match the query will be included in response
    try {
      Baskets result = apiInstance.basketsGet(max, skip, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BasketsApi#basketsGet");
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
| **max** | **Integer**| Maximum number of basket names to return; default 20 | [optional] |
| **skip** | **Integer**| Number of basket names to skip; default 0 | [optional] |
| **q** | **String**| Query string to filter result, only those basket names that match the query will be included in response | [optional] |

### Return type

[**Baskets**](Baskets.md)

### Authorization

[service_token](../README.md#service_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Returns list of available baskets. |  -  |
| **204** | No Content. No baskets available for specified limits |  -  |
| **401** | Unauthorized. Invalid or missing master token |  -  |

<a id="basketsNameDelete"></a>
# **basketsNameDelete**
> basketsNameDelete(name)

Delete basket

Permanently deletes this basket and all collected requests.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BasketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rbaskets.in");
    
    // Configure API key authorization: basket_token
    ApiKeyAuth basket_token = (ApiKeyAuth) defaultClient.getAuthentication("basket_token");
    basket_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //basket_token.setApiKeyPrefix("Token");

    BasketsApi apiInstance = new BasketsApi(defaultClient);
    String name = "name_example"; // String | The basket name
    try {
      apiInstance.basketsNameDelete(name);
    } catch (ApiException e) {
      System.err.println("Exception when calling BasketsApi#basketsNameDelete");
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
| **name** | **String**| The basket name | |

### Return type

null (empty response body)

### Authorization

[basket_token](../README.md#basket_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content. Basket is deleted |  -  |
| **401** | Unauthorized. Invalid or missing basket token |  -  |
| **404** | Not Found. No basket with such name |  -  |

<a id="basketsNameGet"></a>
# **basketsNameGet**
> Config basketsNameGet(name)

Get basket settings

Retrieves configuration settings of this basket.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BasketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rbaskets.in");
    
    // Configure API key authorization: basket_token
    ApiKeyAuth basket_token = (ApiKeyAuth) defaultClient.getAuthentication("basket_token");
    basket_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //basket_token.setApiKeyPrefix("Token");

    BasketsApi apiInstance = new BasketsApi(defaultClient);
    String name = "name_example"; // String | The basket name
    try {
      Config result = apiInstance.basketsNameGet(name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BasketsApi#basketsNameGet");
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
| **name** | **String**| The basket name | |

### Return type

[**Config**](Config.md)

### Authorization

[basket_token](../README.md#basket_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Returns basket configuration |  -  |
| **401** | Unauthorized. Invalid or missing basket token |  -  |
| **404** | Not Found. No basket with such name |  -  |

<a id="basketsNamePost"></a>
# **basketsNamePost**
> Token basketsNamePost(name, config)

Create new basket

Creates a new basket with this name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BasketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rbaskets.in");

    BasketsApi apiInstance = new BasketsApi(defaultClient);
    String name = "name_example"; // String | The name of new basket
    Config config = new Config(); // Config | Basket configuration
    try {
      Token result = apiInstance.basketsNamePost(name, config);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BasketsApi#basketsNamePost");
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
| **name** | **String**| The name of new basket | |
| **config** | [**Config**](Config.md)| Basket configuration | [optional] |

### Return type

[**Token**](Token.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created. Indicates that basket is successfully created |  -  |
| **400** | Bad Request. Failed to parse JSON into basket configuration object. |  -  |
| **403** | Forbidden. Indicates that basket name conflicts with reserved paths; e.g. &#x60;baskets&#x60;, &#x60;web&#x60;, etc. |  -  |
| **409** | Conflict. Indicates that basket with such name already exists |  -  |
| **422** | Unprocessable Entity. Basket configuration is not valid. |  -  |

<a id="basketsNamePut"></a>
# **basketsNamePut**
> basketsNamePut(name, config)

Update basket settings

Updates configuration settings of this basket.  Special configuration parameters for request forwarding:   * &#x60;insecure_tls&#x60; controls certificate verification when forwarding requests. Setting this parameter to &#x60;true&#x60;   allows to forward collected HTTP requests via HTTPS protocol even if the forward end-point is configured with   self-signed TLS/SSL certificate. **Warning:** enabling this feature has known security implications.   * &#x60;expand_path&#x60; changes the logic of constructing taget URL when forwarding requests. If this parameter is   set to &#x60;true&#x60; the forward URL path will be expanded when original HTTP request contains compound path. For   example, a basket with name **server1** is configured to forward all requests to &#x60;http://server1.intranet:8001/myservice&#x60;   and it has received an HTTP request like &#x60;GET http://baskets.example.com/server1/component/123/events?status&#x3D;OK&#x60;   then depending on &#x60;expand_path&#x60; settings the request will be forwarded to:     * &#x60;true&#x60; &#x3D;&gt; &#x60;GET http://server1.intranet:8001/myservice/component/123/events?status&#x3D;OK&#x60;     * &#x60;false&#x60; &#x3D;&gt; &#x60;GET http://server1.intranet:8001/myservice?status&#x3D;OK&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BasketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rbaskets.in");
    
    // Configure API key authorization: basket_token
    ApiKeyAuth basket_token = (ApiKeyAuth) defaultClient.getAuthentication("basket_token");
    basket_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //basket_token.setApiKeyPrefix("Token");

    BasketsApi apiInstance = new BasketsApi(defaultClient);
    String name = "name_example"; // String | The basket name
    Config config = new Config(); // Config | New configuration to apply
    try {
      apiInstance.basketsNamePut(name, config);
    } catch (ApiException e) {
      System.err.println("Exception when calling BasketsApi#basketsNamePut");
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
| **name** | **String**| The basket name | |
| **config** | [**Config**](Config.md)| New configuration to apply | |

### Return type

null (empty response body)

### Authorization

[basket_token](../README.md#basket_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content. Basket configuration is updated |  -  |
| **400** | Bad Request. Failed to parse JSON into basket configuration object. |  -  |
| **401** | Unauthorized. Invalid or missing basket token |  -  |
| **404** | Not Found. No basket with such name |  -  |
| **422** | Unprocessable Entity. Basket configuration is not valid. |  -  |

