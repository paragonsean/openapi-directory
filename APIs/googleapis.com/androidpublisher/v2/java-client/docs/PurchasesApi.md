# PurchasesApi

All URIs are relative to *https://www.googleapis.com/androidpublisher/v2/applications*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**androidpublisherPurchasesProductsGet**](PurchasesApi.md#androidpublisherPurchasesProductsGet) | **GET** /{packageName}/purchases/products/{productId}/tokens/{token} |  |
| [**androidpublisherPurchasesSubscriptionsCancel**](PurchasesApi.md#androidpublisherPurchasesSubscriptionsCancel) | **POST** /{packageName}/purchases/subscriptions/{subscriptionId}/tokens/{token}:cancel |  |
| [**androidpublisherPurchasesSubscriptionsDefer**](PurchasesApi.md#androidpublisherPurchasesSubscriptionsDefer) | **POST** /{packageName}/purchases/subscriptions/{subscriptionId}/tokens/{token}:defer |  |
| [**androidpublisherPurchasesSubscriptionsGet**](PurchasesApi.md#androidpublisherPurchasesSubscriptionsGet) | **GET** /{packageName}/purchases/subscriptions/{subscriptionId}/tokens/{token} |  |
| [**androidpublisherPurchasesSubscriptionsRefund**](PurchasesApi.md#androidpublisherPurchasesSubscriptionsRefund) | **POST** /{packageName}/purchases/subscriptions/{subscriptionId}/tokens/{token}:refund |  |
| [**androidpublisherPurchasesSubscriptionsRevoke**](PurchasesApi.md#androidpublisherPurchasesSubscriptionsRevoke) | **POST** /{packageName}/purchases/subscriptions/{subscriptionId}/tokens/{token}:revoke |  |
| [**androidpublisherPurchasesVoidedpurchasesList**](PurchasesApi.md#androidpublisherPurchasesVoidedpurchasesList) | **GET** /{packageName}/purchases/voidedpurchases |  |


<a id="androidpublisherPurchasesProductsGet"></a>
# **androidpublisherPurchasesProductsGet**
> ProductPurchase androidpublisherPurchasesProductsGet(packageName, productId, token, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Checks the purchase and consumption status of an inapp item.

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
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PurchasesApi apiInstance = new PurchasesApi(defaultClient);
    String packageName = "packageName_example"; // String | The package name of the application the inapp product was sold in (for example, 'com.some.thing').
    String productId = "productId_example"; // String | The inapp product SKU (for example, 'com.some.thing.inapp1').
    String token = "token_example"; // String | The token provided to the user's device when the inapp product was purchased.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      ProductPurchase result = apiInstance.androidpublisherPurchasesProductsGet(packageName, productId, token, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PurchasesApi#androidpublisherPurchasesProductsGet");
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
| **packageName** | **String**| The package name of the application the inapp product was sold in (for example, &#39;com.some.thing&#39;). | |
| **productId** | **String**| The inapp product SKU (for example, &#39;com.some.thing.inapp1&#39;). | |
| **token** | **String**| The token provided to the user&#39;s device when the inapp product was purchased. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

[**ProductPurchase**](ProductPurchase.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherPurchasesSubscriptionsCancel"></a>
# **androidpublisherPurchasesSubscriptionsCancel**
> androidpublisherPurchasesSubscriptionsCancel(packageName, subscriptionId, token, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



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
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
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
      apiInstance.androidpublisherPurchasesSubscriptionsCancel(packageName, subscriptionId, token, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
    } catch (ApiException e) {
      System.err.println("Exception when calling PurchasesApi#androidpublisherPurchasesSubscriptionsCancel");
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

<a id="androidpublisherPurchasesSubscriptionsDefer"></a>
# **androidpublisherPurchasesSubscriptionsDefer**
> SubscriptionPurchasesDeferResponse androidpublisherPurchasesSubscriptionsDefer(packageName, subscriptionId, token, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, subscriptionPurchasesDeferRequest)



Defers a user&#39;s subscription purchase until a specified future expiration time.

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
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
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
    SubscriptionPurchasesDeferRequest subscriptionPurchasesDeferRequest = new SubscriptionPurchasesDeferRequest(); // SubscriptionPurchasesDeferRequest | 
    try {
      SubscriptionPurchasesDeferResponse result = apiInstance.androidpublisherPurchasesSubscriptionsDefer(packageName, subscriptionId, token, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, subscriptionPurchasesDeferRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PurchasesApi#androidpublisherPurchasesSubscriptionsDefer");
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
| **subscriptionPurchasesDeferRequest** | [**SubscriptionPurchasesDeferRequest**](SubscriptionPurchasesDeferRequest.md)|  | [optional] |

### Return type

[**SubscriptionPurchasesDeferResponse**](SubscriptionPurchasesDeferResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherPurchasesSubscriptionsGet"></a>
# **androidpublisherPurchasesSubscriptionsGet**
> SubscriptionPurchase androidpublisherPurchasesSubscriptionsGet(packageName, subscriptionId, token, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



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
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
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
      SubscriptionPurchase result = apiInstance.androidpublisherPurchasesSubscriptionsGet(packageName, subscriptionId, token, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PurchasesApi#androidpublisherPurchasesSubscriptionsGet");
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

<a id="androidpublisherPurchasesSubscriptionsRefund"></a>
# **androidpublisherPurchasesSubscriptionsRefund**
> androidpublisherPurchasesSubscriptionsRefund(packageName, subscriptionId, token, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Refunds a user&#39;s subscription purchase, but the subscription remains valid until its expiration time and it will continue to recur.

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
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
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
      apiInstance.androidpublisherPurchasesSubscriptionsRefund(packageName, subscriptionId, token, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
    } catch (ApiException e) {
      System.err.println("Exception when calling PurchasesApi#androidpublisherPurchasesSubscriptionsRefund");
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

<a id="androidpublisherPurchasesSubscriptionsRevoke"></a>
# **androidpublisherPurchasesSubscriptionsRevoke**
> androidpublisherPurchasesSubscriptionsRevoke(packageName, subscriptionId, token, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Refunds and immediately revokes a user&#39;s subscription purchase. Access to the subscription will be terminated immediately and it will stop recurring.

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
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
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
      apiInstance.androidpublisherPurchasesSubscriptionsRevoke(packageName, subscriptionId, token, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
    } catch (ApiException e) {
      System.err.println("Exception when calling PurchasesApi#androidpublisherPurchasesSubscriptionsRevoke");
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

<a id="androidpublisherPurchasesVoidedpurchasesList"></a>
# **androidpublisherPurchasesVoidedpurchasesList**
> VoidedPurchasesListResponse androidpublisherPurchasesVoidedpurchasesList(packageName, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, endTime, maxResults, startIndex, startTime, token)



Lists the purchases that were canceled, refunded or charged-back.

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
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PurchasesApi apiInstance = new PurchasesApi(defaultClient);
    String packageName = "packageName_example"; // String | The package name of the application for which voided purchases need to be returned (for example, 'com.some.thing').
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String endTime = "endTime_example"; // String | The time, in milliseconds since the Epoch, of the newest voided purchase that you want to see in the response. The value of this parameter cannot be greater than the current time and is ignored if a pagination token is set. Default value is current time. Note: This filter is applied on the time at which the record is seen as voided by our systems and not the actual voided time returned in the response.
    Integer maxResults = 56; // Integer | 
    Integer startIndex = 56; // Integer | 
    String startTime = "startTime_example"; // String | The time, in milliseconds since the Epoch, of the oldest voided purchase that you want to see in the response. The value of this parameter cannot be older than 30 days and is ignored if a pagination token is set. Default value is current time minus 30 days. Note: This filter is applied on the time at which the record is seen as voided by our systems and not the actual voided time returned in the response.
    String token = "token_example"; // String | 
    try {
      VoidedPurchasesListResponse result = apiInstance.androidpublisherPurchasesVoidedpurchasesList(packageName, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, endTime, maxResults, startIndex, startTime, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PurchasesApi#androidpublisherPurchasesVoidedpurchasesList");
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
| **packageName** | **String**| The package name of the application for which voided purchases need to be returned (for example, &#39;com.some.thing&#39;). | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **endTime** | **String**| The time, in milliseconds since the Epoch, of the newest voided purchase that you want to see in the response. The value of this parameter cannot be greater than the current time and is ignored if a pagination token is set. Default value is current time. Note: This filter is applied on the time at which the record is seen as voided by our systems and not the actual voided time returned in the response. | [optional] |
| **maxResults** | **Integer**|  | [optional] |
| **startIndex** | **Integer**|  | [optional] |
| **startTime** | **String**| The time, in milliseconds since the Epoch, of the oldest voided purchase that you want to see in the response. The value of this parameter cannot be older than 30 days and is ignored if a pagination token is set. Default value is current time minus 30 days. Note: This filter is applied on the time at which the record is seen as voided by our systems and not the actual voided time returned in the response. | [optional] |
| **token** | **String**|  | [optional] |

### Return type

[**VoidedPurchasesListResponse**](VoidedPurchasesListResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

