# TokenRevocationApiApi

All URIs are relative to *https://betaapi.digitallocker.gov.in/public*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getTokenRevocationId**](TokenRevocationApiApi.md#getTokenRevocationId) | **POST** /oauth2/1/revoke | Revoke Token. |


<a id="getTokenRevocationId"></a>
# **getTokenRevocationId**
> getTokenRevocationId(getTokenRevocationIdRequest)

Revoke Token.

Client applications can revoke a previously obtained refresh or access token when it is no longer needed. This is done by making a request to the token revocation endpoint. DigiLocker will invalidate the specified token and, if applicable, other tokens based on the same authorisation grant. This API may be used to sign out a user from DigiLocker. This API will work for server based web applications, mobile application and limited input devices.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TokenRevocationApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://betaapi.digitallocker.gov.in/public");
    
    // Configure OAuth2 access token for authorization: oauthsecurity
    OAuth oauthsecurity = (OAuth) defaultClient.getAuthentication("oauthsecurity");
    oauthsecurity.setAccessToken("YOUR ACCESS TOKEN");

    TokenRevocationApiApi apiInstance = new TokenRevocationApiApi(defaultClient);
    GetTokenRevocationIdRequest getTokenRevocationIdRequest = new GetTokenRevocationIdRequest(); // GetTokenRevocationIdRequest | 
    try {
      apiInstance.getTokenRevocationId(getTokenRevocationIdRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling TokenRevocationApiApi#getTokenRevocationId");
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
| **getTokenRevocationIdRequest** | [**GetTokenRevocationIdRequest**](GetTokenRevocationIdRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauthsecurity](../README.md#oauthsecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | The token is invalid |  -  |

