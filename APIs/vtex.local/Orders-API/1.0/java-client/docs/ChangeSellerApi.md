# ChangeSellerApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getWindowToChangeSeller**](ChangeSellerApi.md#getWindowToChangeSeller) | **GET** /api/checkout/pvt/configuration/window-to-change-seller | Get window to change seller |
| [**updateWindowToChangeSeller**](ChangeSellerApi.md#updateWindowToChangeSeller) | **POST** /api/checkout/pvt/configuration/window-to-change-seller | Update window to change seller |


<a id="getWindowToChangeSeller"></a>
# **getWindowToChangeSeller**
> Integer getWindowToChangeSeller(contentType, accept)

Get window to change seller

Retrieves a marketplace’s window to change seller, that is, the period when it is possible to choose another seller to fulfill a given order after the original seller has canceled it.    The default period for this window is of 2 days, but it can be configured by the request Update window to change seller.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChangeSellerApi;

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

    ChangeSellerApi apiInstance = new ChangeSellerApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    try {
      Integer result = apiInstance.getWindowToChangeSeller(contentType, accept);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChangeSellerApi#getWindowToChangeSeller");
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
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |

### Return type

**Integer**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateWindowToChangeSeller"></a>
# **updateWindowToChangeSeller**
> updateWindowToChangeSeller(contentType, accept, updateWindowToChangeSellerRequest)

Update window to change seller

Updates a marketplace’s window to change seller, that is, the period when it is possible to choose another seller to fulfill a given order after the original seller has canceled it.    It is possible to check the current window using the request Get window to change seller.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChangeSellerApi;

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

    ChangeSellerApi apiInstance = new ChangeSellerApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    UpdateWindowToChangeSellerRequest updateWindowToChangeSellerRequest = new UpdateWindowToChangeSellerRequest(); // UpdateWindowToChangeSellerRequest | 
    try {
      apiInstance.updateWindowToChangeSeller(contentType, accept, updateWindowToChangeSellerRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChangeSellerApi#updateWindowToChangeSeller");
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
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **updateWindowToChangeSellerRequest** | [**UpdateWindowToChangeSellerRequest**](UpdateWindowToChangeSellerRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

