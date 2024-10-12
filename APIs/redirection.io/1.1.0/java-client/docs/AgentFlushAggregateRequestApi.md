# AgentFlushAggregateRequestApi

All URIs are relative to *https://api.redirection.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postAgentFlushAggregateRequestCollection**](AgentFlushAggregateRequestApi.md#postAgentFlushAggregateRequestCollection) | **POST** /agent-flush-aggregate-requests | Creates a AgentFlushAggregateRequest resource. |


<a id="postAgentFlushAggregateRequestCollection"></a>
# **postAgentFlushAggregateRequestCollection**
> AgentFlushAggregateRequest postAgentFlushAggregateRequestCollection(agentFlushAggregateRequest)

Creates a AgentFlushAggregateRequest resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentFlushAggregateRequestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    AgentFlushAggregateRequestApi apiInstance = new AgentFlushAggregateRequestApi(defaultClient);
    AgentFlushAggregateRequest agentFlushAggregateRequest = new AgentFlushAggregateRequest(); // AgentFlushAggregateRequest | The new AgentFlushAggregateRequest resource
    try {
      AgentFlushAggregateRequest result = apiInstance.postAgentFlushAggregateRequestCollection(agentFlushAggregateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentFlushAggregateRequestApi#postAgentFlushAggregateRequestCollection");
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
| **agentFlushAggregateRequest** | [**AgentFlushAggregateRequest**](AgentFlushAggregateRequest.md)| The new AgentFlushAggregateRequest resource | [optional] |

### Return type

[**AgentFlushAggregateRequest**](AgentFlushAggregateRequest.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, text/html, text/csv
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | AgentFlushAggregateRequest resource created |  -  |
| **400** | Invalid input |  -  |
| **404** | Resource not found |  -  |

