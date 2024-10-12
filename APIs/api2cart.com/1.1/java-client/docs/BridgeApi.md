# BridgeApi

All URIs are relative to *https://api.api2cart.com/v1.1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bridgeDelete**](BridgeApi.md#bridgeDelete) | **POST** /bridge.delete.json |  |
| [**bridgeUpdate**](BridgeApi.md#bridgeUpdate) | **POST** /bridge.update.json |  |


<a id="bridgeDelete"></a>
# **bridgeDelete**
> BridgeDelete200Response bridgeDelete()



Delete bridge from the store.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BridgeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    BridgeApi apiInstance = new BridgeApi(defaultClient);
    try {
      BridgeDelete200Response result = apiInstance.bridgeDelete();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BridgeApi#bridgeDelete");
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

[**BridgeDelete200Response**](BridgeDelete200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="bridgeUpdate"></a>
# **bridgeUpdate**
> AttributeUpdate200Response bridgeUpdate()



Update bridge in the store.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BridgeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    BridgeApi apiInstance = new BridgeApi(defaultClient);
    try {
      AttributeUpdate200Response result = apiInstance.bridgeUpdate();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BridgeApi#bridgeUpdate");
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

[**AttributeUpdate200Response**](AttributeUpdate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

