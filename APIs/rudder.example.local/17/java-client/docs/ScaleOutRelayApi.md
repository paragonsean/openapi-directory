# ScaleOutRelayApi

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**demoteToNode**](ScaleOutRelayApi.md#demoteToNode) | **POST** /scaleoutrelay/demote/{nodeId} | Demote a relay to simple node |
| [**promoteToRelay**](ScaleOutRelayApi.md#promoteToRelay) | **POST** /scaleoutrelay/promote/{nodeId} | Promote a node to relay |


<a id="demoteToNode"></a>
# **demoteToNode**
> DemoteToNode200Response demoteToNode(nodeId)

Demote a relay to simple node

Demote a relay to a simple node.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScaleOutRelayApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    ScaleOutRelayApi apiInstance = new ScaleOutRelayApi(defaultClient);
    String nodeId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Id of the target node
    try {
      DemoteToNode200Response result = apiInstance.demoteToNode(nodeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScaleOutRelayApi#demoteToNode");
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
| **nodeId** | **String**| Id of the target node | |

### Return type

[**DemoteToNode200Response**](DemoteToNode200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Demote to node response |  -  |

<a id="promoteToRelay"></a>
# **promoteToRelay**
> PromoteToRelay200Response promoteToRelay(nodeId)

Promote a node to relay

Promote a node to relay

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScaleOutRelayApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    ScaleOutRelayApi apiInstance = new ScaleOutRelayApi(defaultClient);
    String nodeId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Id of the target node
    try {
      PromoteToRelay200Response result = apiInstance.promoteToRelay(nodeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScaleOutRelayApi#promoteToRelay");
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
| **nodeId** | **String**| Id of the target node | |

### Return type

[**PromoteToRelay200Response**](PromoteToRelay200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Promote response |  -  |

