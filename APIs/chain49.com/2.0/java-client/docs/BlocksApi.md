# BlocksApi

All URIs are relative to *https://api.chain49.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getBlockHashV2**](BlocksApi.md#getBlockHashV2) | **GET** /{blockchain}/v2/block-index/{blockHeight} | Get block hash V2 |
| [**getBlockV2**](BlocksApi.md#getBlockV2) | **GET** /{blockchain}/v2/block/{blockHashOrHeight} | Get Block V2 |
| [**getRawBlockV2**](BlocksApi.md#getRawBlockV2) | **GET** /{blockchain}/v2/rawblock/{blockHashOrHeight} | Get raw block data V2 |


<a id="getBlockHashV2"></a>
# **getBlockHashV2**
> GetBlockHashV2200Response getBlockHashV2(blockchain, blockHeight)

Get block hash V2

Get block hash by its height  Note: Blockbook always follows the main chain of the backend it is attached to.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlocksApi;

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

    BlocksApi apiInstance = new BlocksApi(defaultClient);
    String blockchain = "bitcoin"; // String | Blockchain name
    Integer blockHeight = 15; // Integer | Block height/index
    try {
      GetBlockHashV2200Response result = apiInstance.getBlockHashV2(blockchain, blockHeight);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlocksApi#getBlockHashV2");
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
| **blockHeight** | **Integer**| Block height/index | |

### Return type

[**GetBlockHashV2200Response**](GetBlockHashV2200Response.md)

### Authorization

[X-RapidAPI-Host](../README.md#X-RapidAPI-Host), [X-API-Key](../README.md#X-API-Key), [X-RapidAPI-Key](../README.md#X-RapidAPI-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getBlockV2"></a>
# **getBlockV2**
> GetBlockV2200Response getBlockV2(blockchain, blockHashOrHeight, page, pageSize)

Get Block V2

Returns information about block with transactions, subject to paging.  Note: Blockbook always follows the main chain of the backend it is attached to. If there is a rollback-reorg in the backend, Blockbook will also do rollback. When you ask for block by height, you will always get the main chain block. If you ask for block by hash, you may get the block from another fork but it is not guaranteed (backend may not keep it)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlocksApi;

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

    BlocksApi apiInstance = new BlocksApi(defaultClient);
    String blockchain = "bitcoin"; // String | Blockchain name
    String blockHashOrHeight = "00000000000000000035835503f43c878ebb643f3b40bdfd0dfda760da74e73c"; // String | Block hash or height
    Integer page = 1; // Integer | specifies page of returned transactions, starting from 1. If out of range, Blockbook returns the closest possible page.
    Integer pageSize = 1000; // Integer | number of transactions returned by call (default and maximum 1000)
    try {
      GetBlockV2200Response result = apiInstance.getBlockV2(blockchain, blockHashOrHeight, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlocksApi#getBlockV2");
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
| **blockHashOrHeight** | **String**| Block hash or height | |
| **page** | **Integer**| specifies page of returned transactions, starting from 1. If out of range, Blockbook returns the closest possible page. | [optional] |
| **pageSize** | **Integer**| number of transactions returned by call (default and maximum 1000) | [optional] |

### Return type

[**GetBlockV2200Response**](GetBlockV2200Response.md)

### Authorization

[X-RapidAPI-Host](../README.md#X-RapidAPI-Host), [X-API-Key](../README.md#X-API-Key), [X-RapidAPI-Key](../README.md#X-RapidAPI-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getRawBlockV2"></a>
# **getRawBlockV2**
> GetRawBlockV2200Response getRawBlockV2(blockchain, blockHashOrHeight)

Get raw block data V2

Returns the raw hex-encoded block data for a given block hash or height

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlocksApi;

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

    BlocksApi apiInstance = new BlocksApi(defaultClient);
    String blockchain = "bitcoin"; // String | Blockchain name
    String blockHashOrHeight = "00000000000000000035835503f43c878ebb643f3b40bdfd0dfda760da74e73c"; // String | Block hash or height
    try {
      GetRawBlockV2200Response result = apiInstance.getRawBlockV2(blockchain, blockHashOrHeight);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlocksApi#getRawBlockV2");
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
| **blockHashOrHeight** | **String**| Block hash or height | |

### Return type

[**GetRawBlockV2200Response**](GetRawBlockV2200Response.md)

### Authorization

[X-RapidAPI-Host](../README.md#X-RapidAPI-Host), [X-API-Key](../README.md#X-API-Key), [X-RapidAPI-Key](../README.md#X-RapidAPI-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

