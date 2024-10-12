# StatusApi

All URIs are relative to *https://api.chain49.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAvailableBlockchains**](StatusApi.md#getAvailableBlockchains) | **GET** / | List available blockchains |
| [**getBlockchain**](StatusApi.md#getBlockchain) | **GET** /{blockchain} | Blockchain Info Summary |


<a id="getAvailableBlockchains"></a>
# **getAvailableBlockchains**
> List&lt;String&gt; getAvailableBlockchains()

List available blockchains

Get an array of active blockchains

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.chain49.com");
    
    // Configure API key authorization: X-RapidAPI-Host
    ApiKeyAuth X-RapidAPI-Host = (ApiKeyAuth) defaultClient.getAuthentication("X-RapidAPI-Host");
    X-RapidAPI-Host.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-RapidAPI-Host.setApiKeyPrefix("Token");

    // Configure API key authorization: X-API-Key
    ApiKeyAuth X-API-Key = (ApiKeyAuth) defaultClient.getAuthentication("X-API-Key");
    X-API-Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-API-Key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-RapidAPI-Key
    ApiKeyAuth X-RapidAPI-Key = (ApiKeyAuth) defaultClient.getAuthentication("X-RapidAPI-Key");
    X-RapidAPI-Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-RapidAPI-Key.setApiKeyPrefix("Token");

    StatusApi apiInstance = new StatusApi(defaultClient);
    try {
      List<String> result = apiInstance.getAvailableBlockchains();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusApi#getAvailableBlockchains");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**List&lt;String&gt;**

### Authorization

[X-RapidAPI-Host](../README.md#X-RapidAPI-Host), [X-API-Key](../README.md#X-API-Key), [X-RapidAPI-Key](../README.md#X-RapidAPI-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getBlockchain"></a>
# **getBlockchain**
> GetBlockchain200Response getBlockchain(blockchain)

Blockchain Info Summary

Get basic summary of info relating to the currently selected blockchain

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.chain49.com");
    
    // Configure API key authorization: X-RapidAPI-Host
    ApiKeyAuth X-RapidAPI-Host = (ApiKeyAuth) defaultClient.getAuthentication("X-RapidAPI-Host");
    X-RapidAPI-Host.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-RapidAPI-Host.setApiKeyPrefix("Token");

    // Configure API key authorization: X-API-Key
    ApiKeyAuth X-API-Key = (ApiKeyAuth) defaultClient.getAuthentication("X-API-Key");
    X-API-Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-API-Key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-RapidAPI-Key
    ApiKeyAuth X-RapidAPI-Key = (ApiKeyAuth) defaultClient.getAuthentication("X-RapidAPI-Key");
    X-RapidAPI-Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-RapidAPI-Key.setApiKeyPrefix("Token");

    StatusApi apiInstance = new StatusApi(defaultClient);
    String blockchain = "bitcoin"; // String | Blockchain name
    try {
      GetBlockchain200Response result = apiInstance.getBlockchain(blockchain);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusApi#getBlockchain");
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
| **blockchain** | **String**| Blockchain name | |

### Return type

[**GetBlockchain200Response**](GetBlockchain200Response.md)

### Authorization

[X-RapidAPI-Host](../README.md#X-RapidAPI-Host), [X-API-Key](../README.md#X-API-Key), [X-RapidAPI-Key](../README.md#X-RapidAPI-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

