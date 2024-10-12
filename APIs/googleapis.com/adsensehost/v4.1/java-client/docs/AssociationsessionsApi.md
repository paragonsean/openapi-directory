# AssociationsessionsApi

All URIs are relative to *https://www.googleapis.com/adsensehost/v4.1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**adsensehostAssociationsessionsStart**](AssociationsessionsApi.md#adsensehostAssociationsessionsStart) | **GET** /associationsessions/start |  |
| [**adsensehostAssociationsessionsVerify**](AssociationsessionsApi.md#adsensehostAssociationsessionsVerify) | **GET** /associationsessions/verify |  |


<a id="adsensehostAssociationsessionsStart"></a>
# **adsensehostAssociationsessionsStart**
> AssociationSession adsensehostAssociationsessionsStart(productCode, websiteUrl, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, callbackUrl, userLocale, websiteLocale)



Create an association session for initiating an association with an AdSense user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssociationsessionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/adsensehost/v4.1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AssociationsessionsApi apiInstance = new AssociationsessionsApi(defaultClient);
    List<String> productCode = Arrays.asList(); // List<String> | Products to associate with the user.
    String websiteUrl = "websiteUrl_example"; // String | The URL of the user's hosted website.
    String alt = "csv"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String callbackUrl = "callbackUrl_example"; // String | The URL to redirect the user to once association is completed. It receives a token parameter that can then be used to retrieve the associated account.
    String userLocale = "userLocale_example"; // String | The preferred locale of the user.
    String websiteLocale = "websiteLocale_example"; // String | The locale of the user's hosted website.
    try {
      AssociationSession result = apiInstance.adsensehostAssociationsessionsStart(productCode, websiteUrl, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, callbackUrl, userLocale, websiteLocale);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssociationsessionsApi#adsensehostAssociationsessionsStart");
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
| **productCode** | [**List&lt;String&gt;**](String.md)| Products to associate with the user. | [enum: AFC, AFG, AFMC, AFS, AFV] |
| **websiteUrl** | **String**| The URL of the user&#39;s hosted website. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: csv, json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **callbackUrl** | **String**| The URL to redirect the user to once association is completed. It receives a token parameter that can then be used to retrieve the associated account. | [optional] |
| **userLocale** | **String**| The preferred locale of the user. | [optional] |
| **websiteLocale** | **String**| The locale of the user&#39;s hosted website. | [optional] |

### Return type

[**AssociationSession**](AssociationSession.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="adsensehostAssociationsessionsVerify"></a>
# **adsensehostAssociationsessionsVerify**
> AssociationSession adsensehostAssociationsessionsVerify(token, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Verify an association session after the association callback returns from AdSense signup.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssociationsessionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/adsensehost/v4.1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AssociationsessionsApi apiInstance = new AssociationsessionsApi(defaultClient);
    String token = "token_example"; // String | The token returned to the association callback URL.
    String alt = "csv"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      AssociationSession result = apiInstance.adsensehostAssociationsessionsVerify(token, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssociationsessionsApi#adsensehostAssociationsessionsVerify");
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
| **token** | **String**| The token returned to the association callback URL. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: csv, json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

[**AssociationSession**](AssociationSession.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

