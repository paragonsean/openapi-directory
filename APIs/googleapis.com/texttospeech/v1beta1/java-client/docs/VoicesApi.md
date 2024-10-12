# VoicesApi

All URIs are relative to *https://texttospeech.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**texttospeechVoicesList**](VoicesApi.md#texttospeechVoicesList) | **GET** /v1beta1/voices |  |


<a id="texttospeechVoicesList"></a>
# **texttospeechVoicesList**
> ListVoicesResponse texttospeechVoicesList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, languageCode)



Returns a list of Voice supported for synthesis.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://texttospeech.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    VoicesApi apiInstance = new VoicesApi(defaultClient);
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String languageCode = "languageCode_example"; // String | Optional. Recommended. [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tag. If not specified, the API will return all supported voices. If specified, the ListVoices call will only return voices that can be used to synthesize this language_code. For example, if you specify `\"en-NZ\"`, all `\"en-NZ\"` voices will be returned. If you specify `\"no\"`, both `\"no-\\*\"` (Norwegian) and `\"nb-\\*\"` (Norwegian Bokmal) voices will be returned.
    try {
      ListVoicesResponse result = apiInstance.texttospeechVoicesList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, languageCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VoicesApi#texttospeechVoicesList");
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
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **languageCode** | **String**| Optional. Recommended. [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tag. If not specified, the API will return all supported voices. If specified, the ListVoices call will only return voices that can be used to synthesize this language_code. For example, if you specify &#x60;\&quot;en-NZ\&quot;&#x60;, all &#x60;\&quot;en-NZ\&quot;&#x60; voices will be returned. If you specify &#x60;\&quot;no\&quot;&#x60;, both &#x60;\&quot;no-\\*\&quot;&#x60; (Norwegian) and &#x60;\&quot;nb-\\*\&quot;&#x60; (Norwegian Bokmal) voices will be returned. | [optional] |

### Return type

[**ListVoicesResponse**](ListVoicesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

