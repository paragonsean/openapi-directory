# AgentFlushRequestApi

All URIs are relative to *https://api.redirection.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**agentFlushRequestsPost**](AgentFlushRequestApi.md#agentFlushRequestsPost) | **POST** /agent-flush-requests | Creates a AgentFlushRequest resource. |
| [**postLogsPost**](AgentFlushRequestApi.md#postLogsPost) | **POST** /post-logs | Creates a AgentFlushRequest resource. |


<a id="agentFlushRequestsPost"></a>
# **agentFlushRequestsPost**
> AgentFlushRequest agentFlushRequestsPost(agentFlushRequest)

Creates a AgentFlushRequest resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentFlushRequestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    AgentFlushRequestApi apiInstance = new AgentFlushRequestApi(defaultClient);
    AgentFlushRequest agentFlushRequest = new AgentFlushRequest(); // AgentFlushRequest | The new AgentFlushRequest resource
    try {
      AgentFlushRequest result = apiInstance.agentFlushRequestsPost(agentFlushRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentFlushRequestApi#agentFlushRequestsPost");
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
| **agentFlushRequest** | [**AgentFlushRequest**](AgentFlushRequest.md)| The new AgentFlushRequest resource | [optional] |

### Return type

[**AgentFlushRequest**](AgentFlushRequest.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, text/html, text/csv
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | AgentFlushRequest resource created |  -  |
| **400** | Invalid input |  -  |
| **404** | Resource not found |  -  |

<a id="postLogsPost"></a>
# **postLogsPost**
> AgentFlushRequest postLogsPost(agentFlushRequest)

Creates a AgentFlushRequest resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentFlushRequestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    AgentFlushRequestApi apiInstance = new AgentFlushRequestApi(defaultClient);
    AgentFlushRequest agentFlushRequest = new AgentFlushRequest(); // AgentFlushRequest | The new AgentFlushRequest resource
    try {
      AgentFlushRequest result = apiInstance.postLogsPost(agentFlushRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentFlushRequestApi#postLogsPost");
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
| **agentFlushRequest** | [**AgentFlushRequest**](AgentFlushRequest.md)| The new AgentFlushRequest resource | [optional] |

### Return type

[**AgentFlushRequest**](AgentFlushRequest.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, text/html, text/csv
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | AgentFlushRequest resource created |  -  |
| **400** | Invalid input |  -  |
| **404** | Resource not found |  -  |

