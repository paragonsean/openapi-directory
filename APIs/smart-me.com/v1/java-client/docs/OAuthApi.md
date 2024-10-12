# OAuthApi

All URIs are relative to *https://smart-me.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiOauthAuthorizePost**](OAuthApi.md#apiOauthAuthorizePost) | **POST** /api/oauth/authorize |  |
| [**oAuthAuthorize**](OAuthApi.md#oAuthAuthorize) | **GET** /api/oauth/authorize |  |


<a id="apiOauthAuthorizePost"></a>
# **apiOauthAuthorizePost**
> Object apiOauthAuthorizePost(clientId, redirectUri, state, scope, clientSecret)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OAuthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    OAuthApi apiInstance = new OAuthApi(defaultClient);
    String clientId = "clientId_example"; // String | 
    String redirectUri = "redirectUri_example"; // String | 
    String state = "state_example"; // String | 
    String scope = "scope_example"; // String | 
    String clientSecret = "clientSecret_example"; // String | 
    try {
      Object result = apiInstance.apiOauthAuthorizePost(clientId, redirectUri, state, scope, clientSecret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OAuthApi#apiOauthAuthorizePost");
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
| **clientId** | **String**|  | |
| **redirectUri** | **String**|  | |
| **state** | **String**|  | |
| **scope** | **String**|  | [optional] |
| **clientSecret** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="oAuthAuthorize"></a>
# **oAuthAuthorize**
> Object oAuthAuthorize(clientId, redirectUri, state, scope, clientSecret)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OAuthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    OAuthApi apiInstance = new OAuthApi(defaultClient);
    String clientId = "clientId_example"; // String | 
    String redirectUri = "redirectUri_example"; // String | 
    String state = "state_example"; // String | 
    String scope = "scope_example"; // String | 
    String clientSecret = "clientSecret_example"; // String | 
    try {
      Object result = apiInstance.oAuthAuthorize(clientId, redirectUri, state, scope, clientSecret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OAuthApi#oAuthAuthorize");
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
| **clientId** | **String**|  | |
| **redirectUri** | **String**|  | |
| **state** | **String**|  | |
| **scope** | **String**|  | [optional] |
| **clientSecret** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

