# ResponsesApi

All URIs are relative to *https://rbaskets.in*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiBasketsNameResponsesMethodGet**](ResponsesApi.md#apiBasketsNameResponsesMethodGet) | **GET** /api/baskets/{name}/responses/{method} | Get response settings |
| [**apiBasketsNameResponsesMethodPut**](ResponsesApi.md#apiBasketsNameResponsesMethodPut) | **PUT** /api/baskets/{name}/responses/{method} | Update response settings |
| [**basketsNameResponsesMethodGet**](ResponsesApi.md#basketsNameResponsesMethodGet) | **GET** /baskets/{name}/responses/{method} | Get response settings |
| [**basketsNameResponsesMethodPut**](ResponsesApi.md#basketsNameResponsesMethodPut) | **PUT** /baskets/{name}/responses/{method} | Update response settings |


<a id="apiBasketsNameResponsesMethodGet"></a>
# **apiBasketsNameResponsesMethodGet**
> Response apiBasketsNameResponsesMethodGet(name, method)

Get response settings

Retrieves information about configured response of the basket. Service will reply with this response to any HTTP request sent to the basket with appropriate HTTP method.  If nothing is configured, the default response is HTTP 200 - OK with empty content. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResponsesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rbaskets.in");
    
    // Configure API key authorization: basket_token
    ApiKeyAuth basket_token = (ApiKeyAuth) defaultClient.getAuthentication("basket_token");
    basket_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //basket_token.setApiKeyPrefix("Token");

    ResponsesApi apiInstance = new ResponsesApi(defaultClient);
    String name = "name_example"; // String | The basket name
    String method = "GET"; // String | The HTTP method this response is configured for
    try {
      Response result = apiInstance.apiBasketsNameResponsesMethodGet(name, method);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResponsesApi#apiBasketsNameResponsesMethodGet");
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
| **method** | **String**| The HTTP method this response is configured for | [enum: GET, HEAD, POST, PUT, PATCH, DELETE, CONNECT, OPTIONS, TRACE] |

### Return type

[**Response**](Response.md)

### Authorization

[basket_token](../README.md#basket_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Returns configured response information |  -  |
| **401** | Unauthorized. Invalid or missing basket token |  -  |
| **404** | Not Found. No basket with such name |  -  |

<a id="apiBasketsNameResponsesMethodPut"></a>
# **apiBasketsNameResponsesMethodPut**
> apiBasketsNameResponsesMethodPut(name, method, response)

Update response settings

Allows to configure HTTP response of this basket. The service will reply with configured response to any HTTP request sent to the basket with appropriate HTTP method.  If nothing is configured, the default response is HTTP 200 - OK with empty content. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResponsesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rbaskets.in");
    
    // Configure API key authorization: basket_token
    ApiKeyAuth basket_token = (ApiKeyAuth) defaultClient.getAuthentication("basket_token");
    basket_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //basket_token.setApiKeyPrefix("Token");

    ResponsesApi apiInstance = new ResponsesApi(defaultClient);
    String name = "name_example"; // String | The basket name
    String method = "GET"; // String | The HTTP method this response is configured for
    Response response = new Response(); // Response | HTTP response configuration
    try {
      apiInstance.apiBasketsNameResponsesMethodPut(name, method, response);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResponsesApi#apiBasketsNameResponsesMethodPut");
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
| **method** | **String**| The HTTP method this response is configured for | [enum: GET, HEAD, POST, PUT, PATCH, DELETE, CONNECT, OPTIONS, TRACE] |
| **response** | [**Response**](Response.md)| HTTP response configuration | |

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
| **204** | No Content. Response configuration is updated |  -  |
| **400** | Bad Request. Failed to parse JSON into response configuration object. |  -  |
| **401** | Unauthorized. Invalid or missing basket token |  -  |
| **404** | Not Found. No basket with such name |  -  |
| **422** | Unprocessable Entity. Response configuration is not valid. |  -  |

<a id="basketsNameResponsesMethodGet"></a>
# **basketsNameResponsesMethodGet**
> Response basketsNameResponsesMethodGet(name, method)

Get response settings

Retrieves information about configured response of the basket. Service will reply with this response to any HTTP request sent to the basket with appropriate HTTP method.  If nothing is configured, the default response is HTTP 200 - OK with empty content. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResponsesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rbaskets.in");
    
    // Configure API key authorization: basket_token
    ApiKeyAuth basket_token = (ApiKeyAuth) defaultClient.getAuthentication("basket_token");
    basket_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //basket_token.setApiKeyPrefix("Token");

    ResponsesApi apiInstance = new ResponsesApi(defaultClient);
    String name = "name_example"; // String | The basket name
    String method = "GET"; // String | The HTTP method this response is configured for
    try {
      Response result = apiInstance.basketsNameResponsesMethodGet(name, method);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResponsesApi#basketsNameResponsesMethodGet");
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
| **method** | **String**| The HTTP method this response is configured for | [enum: GET, HEAD, POST, PUT, PATCH, DELETE, CONNECT, OPTIONS, TRACE] |

### Return type

[**Response**](Response.md)

### Authorization

[basket_token](../README.md#basket_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Returns configured response information |  -  |
| **401** | Unauthorized. Invalid or missing basket token |  -  |
| **404** | Not Found. No basket with such name |  -  |

<a id="basketsNameResponsesMethodPut"></a>
# **basketsNameResponsesMethodPut**
> basketsNameResponsesMethodPut(name, method, response)

Update response settings

Allows to configure HTTP response of this basket. The service will reply with configured response to any HTTP request sent to the basket with appropriate HTTP method.  If nothing is configured, the default response is HTTP 200 - OK with empty content. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResponsesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rbaskets.in");
    
    // Configure API key authorization: basket_token
    ApiKeyAuth basket_token = (ApiKeyAuth) defaultClient.getAuthentication("basket_token");
    basket_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //basket_token.setApiKeyPrefix("Token");

    ResponsesApi apiInstance = new ResponsesApi(defaultClient);
    String name = "name_example"; // String | The basket name
    String method = "GET"; // String | The HTTP method this response is configured for
    Response response = new Response(); // Response | HTTP response configuration
    try {
      apiInstance.basketsNameResponsesMethodPut(name, method, response);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResponsesApi#basketsNameResponsesMethodPut");
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
| **method** | **String**| The HTTP method this response is configured for | [enum: GET, HEAD, POST, PUT, PATCH, DELETE, CONNECT, OPTIONS, TRACE] |
| **response** | [**Response**](Response.md)| HTTP response configuration | |

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
| **204** | No Content. Response configuration is updated |  -  |
| **400** | Bad Request. Failed to parse JSON into response configuration object. |  -  |
| **401** | Unauthorized. Invalid or missing basket token |  -  |
| **404** | Not Found. No basket with such name |  -  |
| **422** | Unprocessable Entity. Response configuration is not valid. |  -  |

