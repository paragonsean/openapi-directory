# AuthenticationApi

All URIs are relative to *http://demo.akeneo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postToken**](AuthenticationApi.md#postToken) | **POST** /api/oauth/v1/token | Get authentication token |


<a id="postToken"></a>
# **postToken**
> PostToken200Response postToken(contentType, authorization, body)

Get authentication token

This endpoint allows you to get an authentication token. No need to be authenticated to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    String contentType = "contentType_example"; // String | Equal to 'application/json' or 'application/x-www-form-urlencoded', no other value allowed
    String authorization = "authorization_example"; // String | Equal to 'Basic xx', where 'xx' is the base 64 encoding of the client id and secret. Find out how to generate them in the <a href=\"/documentation/authentication.html#client-idsecret-generation\">Client ID/secret generation</a> section.
    PostTokenRequest body = new PostTokenRequest(); // PostTokenRequest | 
    try {
      PostToken200Response result = apiInstance.postToken(contentType, authorization, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#postToken");
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
| **contentType** | **String**| Equal to &#39;application/json&#39; or &#39;application/x-www-form-urlencoded&#39;, no other value allowed | |
| **authorization** | **String**| Equal to &#39;Basic xx&#39;, where &#39;xx&#39; is the base 64 encoding of the client id and secret. Find out how to generate them in the &lt;a href&#x3D;\&quot;/documentation/authentication.html#client-idsecret-generation\&quot;&gt;Client ID/secret generation&lt;/a&gt; section. | |
| **body** | [**PostTokenRequest**](PostTokenRequest.md)|  | [optional] |

### Return type

[**PostToken200Response**](PostToken200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, access_token, expires_in, refresh_token, token_type, code, message, _links

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return an authentication token |  -  |
| **400** | Bad request |  -  |
| **415** | Unsupported Media type |  -  |
| **422** | Unprocessable entity |  -  |

