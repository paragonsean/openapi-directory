# AccessTokensApi

All URIs are relative to *https://api.hubapi.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getOauthV1AccessTokensTokenGet**](AccessTokensApi.md#getOauthV1AccessTokensTokenGet) | **GET** /oauth/v1/access-tokens/{token} |  |


<a id="getOauthV1AccessTokensTokenGet"></a>
# **getOauthV1AccessTokensTokenGet**
> AccessTokenInfoResponse getOauthV1AccessTokensTokenGet(token)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccessTokensApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");

    AccessTokensApi apiInstance = new AccessTokensApi(defaultClient);
    String token = "token_example"; // String | 
    try {
      AccessTokenInfoResponse result = apiInstance.getOauthV1AccessTokensTokenGet(token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccessTokensApi#getOauthV1AccessTokensTokenGet");
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
| **token** | **String**|  | |

### Return type

[**AccessTokenInfoResponse**](AccessTokenInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | An error occurred. |  -  |

