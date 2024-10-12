# RunnersApi

All URIs are relative to *https://gitlab.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteV3RunnersId**](RunnersApi.md#deleteV3RunnersId) | **DELETE** /v3/runners/{id} | Remove a runner |
| [**getV3Runners**](RunnersApi.md#getV3Runners) | **GET** /v3/runners | Get runners available for user |
| [**getV3RunnersAll**](RunnersApi.md#getV3RunnersAll) | **GET** /v3/runners/all | Get all runners - shared and specific |
| [**getV3RunnersId**](RunnersApi.md#getV3RunnersId) | **GET** /v3/runners/{id} | Get runner&#39;s details |
| [**putV3RunnersId**](RunnersApi.md#putV3RunnersId) | **PUT** /v3/runners/{id} | Update runner&#39;s details |


<a id="deleteV3RunnersId"></a>
# **deleteV3RunnersId**
> Runner deleteV3RunnersId(id)

Remove a runner

Remove a runner

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RunnersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    RunnersApi apiInstance = new RunnersApi(defaultClient);
    Integer id = 56; // Integer | The ID of the runner
    try {
      Runner result = apiInstance.deleteV3RunnersId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RunnersApi#deleteV3RunnersId");
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
| **id** | **Integer**| The ID of the runner | |

### Return type

[**Runner**](Runner.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Remove a runner |  -  |

<a id="getV3Runners"></a>
# **getV3Runners**
> Runner getV3Runners(scope, page, perPage)

Get runners available for user

Get runners available for user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RunnersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    RunnersApi apiInstance = new RunnersApi(defaultClient);
    String scope = "active"; // String | The scope of specific runners to show
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    try {
      Runner result = apiInstance.getV3Runners(scope, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RunnersApi#getV3Runners");
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
| **scope** | **String**| The scope of specific runners to show | [optional] [enum: active, paused, online] |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |

### Return type

[**Runner**](Runner.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get runners available for user |  -  |

<a id="getV3RunnersAll"></a>
# **getV3RunnersAll**
> Runner getV3RunnersAll(scope, page, perPage)

Get all runners - shared and specific

Get all runners - shared and specific

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RunnersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    RunnersApi apiInstance = new RunnersApi(defaultClient);
    String scope = "active"; // String | The scope of specific runners to show
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    try {
      Runner result = apiInstance.getV3RunnersAll(scope, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RunnersApi#getV3RunnersAll");
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
| **scope** | **String**| The scope of specific runners to show | [optional] [enum: active, paused, online, specific, shared] |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |

### Return type

[**Runner**](Runner.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get all runners - shared and specific |  -  |

<a id="getV3RunnersId"></a>
# **getV3RunnersId**
> RunnerDetails getV3RunnersId(id)

Get runner&#39;s details

Get runner&#39;s details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RunnersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    RunnersApi apiInstance = new RunnersApi(defaultClient);
    Integer id = 56; // Integer | The ID of the runner
    try {
      RunnerDetails result = apiInstance.getV3RunnersId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RunnersApi#getV3RunnersId");
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
| **id** | **Integer**| The ID of the runner | |

### Return type

[**RunnerDetails**](RunnerDetails.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get runner&#39;s details |  -  |

<a id="putV3RunnersId"></a>
# **putV3RunnersId**
> RunnerDetails putV3RunnersId(id, putV3RunnersIdRequest)

Update runner&#39;s details

Update runner&#39;s details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RunnersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    RunnersApi apiInstance = new RunnersApi(defaultClient);
    Integer id = 56; // Integer | The ID of the runner
    PutV3RunnersIdRequest putV3RunnersIdRequest = new PutV3RunnersIdRequest(); // PutV3RunnersIdRequest | 
    try {
      RunnerDetails result = apiInstance.putV3RunnersId(id, putV3RunnersIdRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RunnersApi#putV3RunnersId");
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
| **id** | **Integer**| The ID of the runner | |
| **putV3RunnersIdRequest** | [**PutV3RunnersIdRequest**](PutV3RunnersIdRequest.md)|  | [optional] |

### Return type

[**RunnerDetails**](RunnerDetails.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update runner&#39;s details |  -  |

