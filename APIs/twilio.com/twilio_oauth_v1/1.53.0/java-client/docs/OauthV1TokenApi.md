# OauthV1TokenApi

All URIs are relative to *https://oauth.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createToken**](OauthV1TokenApi.md#createToken) | **POST** /v1/token |  |


<a id="createToken"></a>
# **createToken**
> OauthV1Token createToken(clientSid, grantType, clientSecret, code, codeVerifier, deviceCode, deviceId, refreshToken)



Issues a new Access token (optionally identity_token &amp; refresh_token) in exchange of Oauth grant

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OauthV1TokenApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://oauth.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    OauthV1TokenApi apiInstance = new OauthV1TokenApi(defaultClient);
    String clientSid = "clientSid_example"; // String | A 34 character string that uniquely identifies this OAuth App.
    String grantType = "grantType_example"; // String | Grant type is a credential representing resource owner's authorization which can be used by client to obtain access token.
    String clientSecret = "clientSecret_example"; // String | The credential for confidential OAuth App.
    String code = "code_example"; // String | JWT token related to the authorization code grant type.
    String codeVerifier = "codeVerifier_example"; // String | A code which is generation cryptographically.
    String deviceCode = "deviceCode_example"; // String | JWT token related to the device code grant type.
    String deviceId = "deviceId_example"; // String | The Id of the device associated with the token (refresh token).
    String refreshToken = "refreshToken_example"; // String | JWT token related to the refresh token grant type.
    try {
      OauthV1Token result = apiInstance.createToken(clientSid, grantType, clientSecret, code, codeVerifier, deviceCode, deviceId, refreshToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OauthV1TokenApi#createToken");
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
| **clientSid** | **String**| A 34 character string that uniquely identifies this OAuth App. | |
| **grantType** | **String**| Grant type is a credential representing resource owner&#39;s authorization which can be used by client to obtain access token. | |
| **clientSecret** | **String**| The credential for confidential OAuth App. | [optional] |
| **code** | **String**| JWT token related to the authorization code grant type. | [optional] |
| **codeVerifier** | **String**| A code which is generation cryptographically. | [optional] |
| **deviceCode** | **String**| JWT token related to the device code grant type. | [optional] |
| **deviceId** | **String**| The Id of the device associated with the token (refresh token). | [optional] |
| **refreshToken** | **String**| JWT token related to the refresh token grant type. | [optional] |

### Return type

[**OauthV1Token**](OauthV1Token.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

