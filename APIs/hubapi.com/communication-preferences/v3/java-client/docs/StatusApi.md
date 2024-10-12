# StatusApi

All URIs are relative to *https://api.hubapi.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCommunicationPreferencesV3StatusEmailEmailAddressGetEmailStatus**](StatusApi.md#getCommunicationPreferencesV3StatusEmailEmailAddressGetEmailStatus) | **GET** /communication-preferences/v3/status/email/{emailAddress} | Get subscription statuses for a contact |
| [**postCommunicationPreferencesV3SubscribeSubscribe**](StatusApi.md#postCommunicationPreferencesV3SubscribeSubscribe) | **POST** /communication-preferences/v3/subscribe | Subscribe a contact |
| [**postCommunicationPreferencesV3UnsubscribeUnsubscribe**](StatusApi.md#postCommunicationPreferencesV3UnsubscribeUnsubscribe) | **POST** /communication-preferences/v3/unsubscribe | Unsubscribe a contact |


<a id="getCommunicationPreferencesV3StatusEmailEmailAddressGetEmailStatus"></a>
# **getCommunicationPreferencesV3StatusEmailEmailAddressGetEmailStatus**
> PublicSubscriptionStatusesResponse getCommunicationPreferencesV3StatusEmailEmailAddressGetEmailStatus(emailAddress)

Get subscription statuses for a contact

Returns a list of subscriptions and their status for a given contact.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatusApi;

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

    StatusApi apiInstance = new StatusApi(defaultClient);
    String emailAddress = "emailAddress_example"; // String | 
    try {
      PublicSubscriptionStatusesResponse result = apiInstance.getCommunicationPreferencesV3StatusEmailEmailAddressGetEmailStatus(emailAddress);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusApi#getCommunicationPreferencesV3StatusEmailEmailAddressGetEmailStatus");
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
| **emailAddress** | **String**|  | |

### Return type

[**PublicSubscriptionStatusesResponse**](PublicSubscriptionStatusesResponse.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | An error occurred. |  -  |

<a id="postCommunicationPreferencesV3SubscribeSubscribe"></a>
# **postCommunicationPreferencesV3SubscribeSubscribe**
> PublicSubscriptionStatus postCommunicationPreferencesV3SubscribeSubscribe(publicUpdateSubscriptionStatusRequest)

Subscribe a contact

Subscribes a contact to the given subscription type. This API is not valid to use for subscribing a contact at a brand or portal level and will return an error.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatusApi;

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

    StatusApi apiInstance = new StatusApi(defaultClient);
    PublicUpdateSubscriptionStatusRequest publicUpdateSubscriptionStatusRequest = new PublicUpdateSubscriptionStatusRequest(); // PublicUpdateSubscriptionStatusRequest | 
    try {
      PublicSubscriptionStatus result = apiInstance.postCommunicationPreferencesV3SubscribeSubscribe(publicUpdateSubscriptionStatusRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusApi#postCommunicationPreferencesV3SubscribeSubscribe");
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
| **publicUpdateSubscriptionStatusRequest** | [**PublicUpdateSubscriptionStatusRequest**](PublicUpdateSubscriptionStatusRequest.md)|  | |

### Return type

[**PublicSubscriptionStatus**](PublicSubscriptionStatus.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** |  |  -  |
| **404** |  |  -  |
| **0** | An error occurred. |  -  |

<a id="postCommunicationPreferencesV3UnsubscribeUnsubscribe"></a>
# **postCommunicationPreferencesV3UnsubscribeUnsubscribe**
> PublicSubscriptionStatus postCommunicationPreferencesV3UnsubscribeUnsubscribe(publicUpdateSubscriptionStatusRequest)

Unsubscribe a contact

Unsubscribes a contact from the given subscription type. This API is not valid to use for unsubscribing a contact at a brand or portal level and will return an error.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatusApi;

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

    StatusApi apiInstance = new StatusApi(defaultClient);
    PublicUpdateSubscriptionStatusRequest publicUpdateSubscriptionStatusRequest = new PublicUpdateSubscriptionStatusRequest(); // PublicUpdateSubscriptionStatusRequest | 
    try {
      PublicSubscriptionStatus result = apiInstance.postCommunicationPreferencesV3UnsubscribeUnsubscribe(publicUpdateSubscriptionStatusRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusApi#postCommunicationPreferencesV3UnsubscribeUnsubscribe");
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
| **publicUpdateSubscriptionStatusRequest** | [**PublicUpdateSubscriptionStatusRequest**](PublicUpdateSubscriptionStatusRequest.md)|  | |

### Return type

[**PublicSubscriptionStatus**](PublicSubscriptionStatus.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** |  |  -  |
| **404** |  |  -  |
| **0** | An error occurred. |  -  |

