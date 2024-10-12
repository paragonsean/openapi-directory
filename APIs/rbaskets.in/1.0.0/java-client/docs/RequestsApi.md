# RequestsApi

All URIs are relative to *https://rbaskets.in*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiBasketsNameRequestsDelete**](RequestsApi.md#apiBasketsNameRequestsDelete) | **DELETE** /api/baskets/{name}/requests | Delete all requests |
| [**apiBasketsNameRequestsGet**](RequestsApi.md#apiBasketsNameRequestsGet) | **GET** /api/baskets/{name}/requests | Get collected requests |
| [**basketsNameRequestsDelete**](RequestsApi.md#basketsNameRequestsDelete) | **DELETE** /baskets/{name}/requests | Delete all requests |
| [**basketsNameRequestsGet**](RequestsApi.md#basketsNameRequestsGet) | **GET** /baskets/{name}/requests | Get collected requests |


<a id="apiBasketsNameRequestsDelete"></a>
# **apiBasketsNameRequestsDelete**
> apiBasketsNameRequestsDelete(name)

Delete all requests

Deletes all requests collected by this basket.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rbaskets.in");
    
    // Configure API key authorization: basket_token
    ApiKeyAuth basket_token = (ApiKeyAuth) defaultClient.getAuthentication("basket_token");
    basket_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //basket_token.setApiKeyPrefix("Token");

    RequestsApi apiInstance = new RequestsApi(defaultClient);
    String name = "name_example"; // String | The basket name
    try {
      apiInstance.apiBasketsNameRequestsDelete(name);
    } catch (ApiException e) {
      System.err.println("Exception when calling RequestsApi#apiBasketsNameRequestsDelete");
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
| **204** | No Content. Basket requests are cleared |  -  |
| **401** | Unauthorized. Invalid or missing basket token |  -  |
| **404** | Not Found. No basket with such name |  -  |

<a id="apiBasketsNameRequestsGet"></a>
# **apiBasketsNameRequestsGet**
> Requests apiBasketsNameRequestsGet(name, max, skip, q, in)

Get collected requests

Fetches collection of requests collected by this basket.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rbaskets.in");
    
    // Configure API key authorization: basket_token
    ApiKeyAuth basket_token = (ApiKeyAuth) defaultClient.getAuthentication("basket_token");
    basket_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //basket_token.setApiKeyPrefix("Token");

    RequestsApi apiInstance = new RequestsApi(defaultClient);
    String name = "name_example"; // String | The basket name
    Integer max = 56; // Integer | Maximum number of requests to return; default 20
    Integer skip = 56; // Integer | Number of requests to skip; default 0
    String q = "q_example"; // String | Query string to filter result, only requests that match the query will be included in response
    String in = "any"; // String | Defines what is taken into account when filtering is applied: `body` - search in content body of collected requests, `query` - search among query parameters of collected requests, `headers` - search among request header values, `any` - search anywhere; default `any` 
    try {
      Requests result = apiInstance.apiBasketsNameRequestsGet(name, max, skip, q, in);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RequestsApi#apiBasketsNameRequestsGet");
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
| **max** | **Integer**| Maximum number of requests to return; default 20 | [optional] |
| **skip** | **Integer**| Number of requests to skip; default 0 | [optional] |
| **q** | **String**| Query string to filter result, only requests that match the query will be included in response | [optional] |
| **in** | **String**| Defines what is taken into account when filtering is applied: &#x60;body&#x60; - search in content body of collected requests, &#x60;query&#x60; - search among query parameters of collected requests, &#x60;headers&#x60; - search among request header values, &#x60;any&#x60; - search anywhere; default &#x60;any&#x60;  | [optional] [enum: any, body, query, headers] |

### Return type

[**Requests**](Requests.md)

### Authorization

[basket_token](../README.md#basket_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Returns list of basket requests. |  -  |
| **204** | No Content. No requests found for specified limits |  -  |
| **401** | Unauthorized. Invalid or missing basket token |  -  |
| **404** | Not Found. No basket with such name |  -  |

<a id="basketsNameRequestsDelete"></a>
# **basketsNameRequestsDelete**
> basketsNameRequestsDelete(name)

Delete all requests

Deletes all requests collected by this basket.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rbaskets.in");
    
    // Configure API key authorization: basket_token
    ApiKeyAuth basket_token = (ApiKeyAuth) defaultClient.getAuthentication("basket_token");
    basket_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //basket_token.setApiKeyPrefix("Token");

    RequestsApi apiInstance = new RequestsApi(defaultClient);
    String name = "name_example"; // String | The basket name
    try {
      apiInstance.basketsNameRequestsDelete(name);
    } catch (ApiException e) {
      System.err.println("Exception when calling RequestsApi#basketsNameRequestsDelete");
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
| **204** | No Content. Basket requests are cleared |  -  |
| **401** | Unauthorized. Invalid or missing basket token |  -  |
| **404** | Not Found. No basket with such name |  -  |

<a id="basketsNameRequestsGet"></a>
# **basketsNameRequestsGet**
> Requests basketsNameRequestsGet(name, max, skip, q, in)

Get collected requests

Fetches collection of requests collected by this basket.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rbaskets.in");
    
    // Configure API key authorization: basket_token
    ApiKeyAuth basket_token = (ApiKeyAuth) defaultClient.getAuthentication("basket_token");
    basket_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //basket_token.setApiKeyPrefix("Token");

    RequestsApi apiInstance = new RequestsApi(defaultClient);
    String name = "name_example"; // String | The basket name
    Integer max = 56; // Integer | Maximum number of requests to return; default 20
    Integer skip = 56; // Integer | Number of requests to skip; default 0
    String q = "q_example"; // String | Query string to filter result, only requests that match the query will be included in response
    String in = "any"; // String | Defines what is taken into account when filtering is applied: `body` - search in content body of collected requests, `query` - search among query parameters of collected requests, `headers` - search among request header values, `any` - search anywhere; default `any` 
    try {
      Requests result = apiInstance.basketsNameRequestsGet(name, max, skip, q, in);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RequestsApi#basketsNameRequestsGet");
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
| **max** | **Integer**| Maximum number of requests to return; default 20 | [optional] |
| **skip** | **Integer**| Number of requests to skip; default 0 | [optional] |
| **q** | **String**| Query string to filter result, only requests that match the query will be included in response | [optional] |
| **in** | **String**| Defines what is taken into account when filtering is applied: &#x60;body&#x60; - search in content body of collected requests, &#x60;query&#x60; - search among query parameters of collected requests, &#x60;headers&#x60; - search among request header values, &#x60;any&#x60; - search anywhere; default &#x60;any&#x60;  | [optional] [enum: any, body, query, headers] |

### Return type

[**Requests**](Requests.md)

### Authorization

[basket_token](../README.md#basket_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Returns list of basket requests. |  -  |
| **204** | No Content. No requests found for specified limits |  -  |
| **401** | Unauthorized. Invalid or missing basket token |  -  |
| **404** | Not Found. No basket with such name |  -  |

