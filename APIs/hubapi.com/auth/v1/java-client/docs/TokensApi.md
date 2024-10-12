# TokensApi

All URIs are relative to *https://api.hubapi.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postOauthV1TokenCreate**](TokensApi.md#postOauthV1TokenCreate) | **POST** /oauth/v1/token |  |


<a id="postOauthV1TokenCreate"></a>
# **postOauthV1TokenCreate**
> TokenResponseIF postOauthV1TokenCreate(clientId, clientSecret, code, grantType, redirectUri, refreshToken)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TokensApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");

    TokensApi apiInstance = new TokensApi(defaultClient);
    String clientId = "clientId_example"; // String | 
    String clientSecret = "clientSecret_example"; // String | 
    String code = "code_example"; // String | 
    String grantType = "authorization_code"; // String | 
    String redirectUri = "redirectUri_example"; // String | 
    String refreshToken = "refreshToken_example"; // String | 
    try {
      TokenResponseIF result = apiInstance.postOauthV1TokenCreate(clientId, clientSecret, code, grantType, redirectUri, refreshToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TokensApi#postOauthV1TokenCreate");
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
| **clientId** | **String**|  | [optional] |
| **clientSecret** | **String**|  | [optional] |
| **code** | **String**|  | [optional] |
| **grantType** | **String**|  | [optional] [enum: authorization_code, refresh_token] |
| **redirectUri** | **String**|  | [optional] |
| **refreshToken** | **String**|  | [optional] |

### Return type

[**TokenResponseIF**](TokenResponseIF.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | An error occurred. |  -  |

