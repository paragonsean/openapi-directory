# JsonRpcApi

All URIs are relative to *https://ntp1node.nebl.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**jsonRpc**](JsonRpcApi.md#jsonRpc) | **POST** / | Send a JSON-RPC call to a localhost neblio-Qt or nebliod node |


<a id="jsonRpc"></a>
# **jsonRpc**
> RpcResponse jsonRpc(rpcRequest)

Send a JSON-RPC call to a localhost neblio-Qt or nebliod node

Call any Neblio RPC command from the Neblio API libraries. Useful for signing transactions with a local node and other functions. Will not work from a browser due to CORS restrictions. Requires a node to be running locally at 127.0.0.1

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JsonRpcApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");
    
    // Configure HTTP basic authorization: rpcAuth
    HttpBasicAuth rpcAuth = (HttpBasicAuth) defaultClient.getAuthentication("rpcAuth");
    rpcAuth.setUsername("YOUR USERNAME");
    rpcAuth.setPassword("YOUR PASSWORD");

    JsonRpcApi apiInstance = new JsonRpcApi(defaultClient);
    RpcRequest rpcRequest = new RpcRequest(); // RpcRequest | 
    try {
      RpcResponse result = apiInstance.jsonRpc(rpcRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JsonRpcApi#jsonRpc");
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
| **rpcRequest** | [**RpcRequest**](RpcRequest.md)|  | |

### Return type

[**RpcResponse**](RpcResponse.md)

### Authorization

[rpcAuth](../README.md#rpcAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Object containing the JSON response from the Neblio node. |  -  |
| **401** | Authentication information is missing or invalid |  * WWW_Authenticate -  <br>  |

