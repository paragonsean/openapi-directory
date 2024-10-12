# GenerateApi

All URIs are relative to *https://api.hubapi.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postConversationsV3VisitorIdentificationTokensCreateGenerateToken**](GenerateApi.md#postConversationsV3VisitorIdentificationTokensCreateGenerateToken) | **POST** /conversations/v3/visitor-identification/tokens/create | Generate a token |


<a id="postConversationsV3VisitorIdentificationTokensCreateGenerateToken"></a>
# **postConversationsV3VisitorIdentificationTokensCreateGenerateToken**
> IdentificationTokenResponse postConversationsV3VisitorIdentificationTokensCreateGenerateToken(identificationTokenGenerationRequest)

Generate a token

Generates a new visitor identification token. This token will be unique every time this endpoint is called, even if called with the same email address. This token is temporary and will expire after 12 hours

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GenerateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure OAuth2 access token for authorization: oauth2_legacy
    OAuth oauth2_legacy = (OAuth) defaultClient.getAuthentication("oauth2_legacy");
    oauth2_legacy.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: private_apps_legacy
    ApiKeyAuth private_apps_legacy = (ApiKeyAuth) defaultClient.getAuthentication("private_apps_legacy");
    private_apps_legacy.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_apps_legacy.setApiKeyPrefix("Token");

    GenerateApi apiInstance = new GenerateApi(defaultClient);
    IdentificationTokenGenerationRequest identificationTokenGenerationRequest = new IdentificationTokenGenerationRequest(); // IdentificationTokenGenerationRequest | 
    try {
      IdentificationTokenResponse result = apiInstance.postConversationsV3VisitorIdentificationTokensCreateGenerateToken(identificationTokenGenerationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GenerateApi#postConversationsV3VisitorIdentificationTokensCreateGenerateToken");
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
| **identificationTokenGenerationRequest** | [**IdentificationTokenGenerationRequest**](IdentificationTokenGenerationRequest.md)|  | |

### Return type

[**IdentificationTokenResponse**](IdentificationTokenResponse.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | An error occurred. |  -  |

