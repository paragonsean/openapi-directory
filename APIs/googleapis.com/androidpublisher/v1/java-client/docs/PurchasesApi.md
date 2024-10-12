# PurchasesApi

All URIs are relative to *https://www.googleapis.com/androidpublisher/v1/applications*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**androidpublisherPurchasesCancel**](PurchasesApi.md#androidpublisherPurchasesCancel) | **POST** /{packageName}/subscriptions/{subscriptionId}/purchases/{token}/cancel |  |
| [**androidpublisherPurchasesGet**](PurchasesApi.md#androidpublisherPurchasesGet) | **GET** /{packageName}/subscriptions/{subscriptionId}/purchases/{token} |  |


<a id="androidpublisherPurchasesCancel"></a>
# **androidpublisherPurchasesCancel**
> androidpublisherPurchasesCancel(packageName, subscriptionId, token, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Cancels a user&#39;s subscription purchase. The subscription remains valid until its expiration time.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PurchasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v1/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PurchasesApi apiInstance = new PurchasesApi(defaultClient);
    String packageName = "packageName_example"; // String | The package name of the application for which this subscription was purchased (for example, 'com.some.thing').
    String subscriptionId = "subscriptionId_example"; // String | The purchased subscription ID (for example, 'monthly001').
    String token = "token_example"; // String | The token provided to the user's device when the subscription was purchased.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      apiInstance.androidpublisherPurchasesCancel(packageName, subscriptionId, token, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
    } catch (ApiException e) {
      System.err.println("Exception when calling PurchasesApi#androidpublisherPurchasesCancel");
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
| **packageName** | **String**| The package name of the application for which this subscription was purchased (for example, &#39;com.some.thing&#39;). | |
| **subscriptionId** | **String**| The purchased subscription ID (for example, &#39;monthly001&#39;). | |
| **token** | **String**| The token provided to the user&#39;s device when the subscription was purchased. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

null (empty response body)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherPurchasesGet"></a>
# **androidpublisherPurchasesGet**
> SubscriptionPurchase androidpublisherPurchasesGet(packageName, subscriptionId, token, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Checks whether a user&#39;s subscription purchase is valid and returns its expiry time.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PurchasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v1/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PurchasesApi apiInstance = new PurchasesApi(defaultClient);
    String packageName = "packageName_example"; // String | The package name of the application for which this subscription was purchased (for example, 'com.some.thing').
    String subscriptionId = "subscriptionId_example"; // String | The purchased subscription ID (for example, 'monthly001').
    String token = "token_example"; // String | The token provided to the user's device when the subscription was purchased.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      SubscriptionPurchase result = apiInstance.androidpublisherPurchasesGet(packageName, subscriptionId, token, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PurchasesApi#androidpublisherPurchasesGet");
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
| **packageName** | **String**| The package name of the application for which this subscription was purchased (for example, &#39;com.some.thing&#39;). | |
| **subscriptionId** | **String**| The purchased subscription ID (for example, &#39;monthly001&#39;). | |
| **token** | **String**| The token provided to the user&#39;s device when the subscription was purchased. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

[**SubscriptionPurchase**](SubscriptionPurchase.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

