# OrderHookApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteHookConfiguration**](OrderHookApi.md#deleteHookConfiguration) | **DELETE** /api/orders/hook/config | Delete hook configuration |
| [**getHookConfiguration**](OrderHookApi.md#getHookConfiguration) | **GET** /api/orders/hook/config | Get hook configuration |
| [**hookConfiguration**](OrderHookApi.md#hookConfiguration) | **POST** /api/orders/hook/config | Create or update hook configuration |


<a id="deleteHookConfiguration"></a>
# **deleteHookConfiguration**
> deleteHookConfiguration(accept, contentType)

Delete hook configuration

Deletes a given hook configuration.    Learn more with the [orders hook guide](https://developers.vtex.com/vtex-rest-api/docs/orders-feed#hook).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderHookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    OrderHookApi apiInstance = new OrderHookApi(defaultClient);
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String contentType = "application/json"; // String | Type of the content being sent.
    try {
      apiInstance.deleteHookConfiguration(accept, contentType);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderHookApi#deleteHookConfiguration");
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
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | The credentials are not enabled to access the service |  -  |
| **404** | Value not found |  -  |
| **429** | Too many requests |  -  |

<a id="getHookConfiguration"></a>
# **getHookConfiguration**
> getHookConfiguration(contentType, accept, clientEmail, page, perPage)

Get hook configuration

Retrieves a given hook&#39;s configuration details. Learn more with the [orders hook guide](https://developers.vtex.com/vtex-rest-api/docs/orders-feed#hook).     &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Orders onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/orders-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Orders and is organized by focusing on the developer&#39;s journey.    

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderHookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    OrderHookApi apiInstance = new OrderHookApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String clientEmail = "customer@mail.com"; // String | Customer email.
    String page = "10"; // String | Page number for result pagination.
    String perPage = "15"; // String | Page quantity for result pagination.
    try {
      apiInstance.getHookConfiguration(contentType, accept, clientEmail, page, perPage);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderHookApi#getHookConfiguration");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **clientEmail** | **String**| Customer email. | [optional] |
| **page** | **String**| Page number for result pagination. | [optional] |
| **perPage** | **String**| Page quantity for result pagination. | [optional] |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="hookConfiguration"></a>
# **hookConfiguration**
> HookConfiguration hookConfiguration(contentType, accept, hookConfigurationRequest)

Create or update hook configuration

Configures filtering rules applied to orders hook. Learn more with the [orders hook guide](https://developers.vtex.com/vtex-rest-api/docs/orders-feed#hook).    There are two types of filtering that can be used:      - &#x60;FromWorkflow&#x60;: filters orders by status.     - &#x60;FromOrders&#x60;: uses JSONata expressions to filter orders according to any property in the orders JSON document.     This enables stores to filter delivered orders and orders in which products have been added or removed, for example.    To learn more, access the [JSONata documentation](https://docs.jsonata.org/overview.html) and test filtering JSONata expressions with our [expressions API](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/orders/expressions/jsonata).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderHookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    OrderHookApi apiInstance = new OrderHookApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    HookConfigurationRequest hookConfigurationRequest = new HookConfigurationRequest(); // HookConfigurationRequest | 
    try {
      HookConfiguration result = apiInstance.hookConfiguration(contentType, accept, hookConfigurationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderHookApi#hookConfiguration");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **hookConfigurationRequest** | [**HookConfigurationRequest**](HookConfigurationRequest.md)|  | |

### Return type

[**HookConfiguration**](HookConfiguration.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

