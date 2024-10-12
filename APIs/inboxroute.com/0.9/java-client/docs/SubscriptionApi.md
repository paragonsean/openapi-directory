# SubscriptionApi

All URIs are relative to *https://api.inboxroute.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**subscriptionListidPost**](SubscriptionApi.md#subscriptionListidPost) | **POST** /subscription/{listid} |  |


<a id="subscriptionListidPost"></a>
# **subscriptionListidPost**
> subscriptionListidPost(listid, subscription)



Subscribe an email address to a list. This api call has the same behavior as a regular subscribe form. However, single opt-in is allowed for system integration purposes.  - If email address does not exist, a new contact will be added to the list. - If email address exists custom fields will be updated and status will be put   to unconfirmed or active depending of singleoptin value. - If current status if Active, this operation will only update the custom fields. - If singleoptin is true, no email confirmation will be sent. In that case,   you must provide the subscribe&#39;s origin ip and confirmation date-time. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.inboxroute.com/api");
    
    // Configure API key authorization: mqApiKey
    ApiKeyAuth mqApiKey = (ApiKeyAuth) defaultClient.getAuthentication("mqApiKey");
    mqApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //mqApiKey.setApiKeyPrefix("Token");

    SubscriptionApi apiInstance = new SubscriptionApi(defaultClient);
    String listid = "listid_example"; // String | Unique 16 characters ID of the contact list
    SubscriptionRequest subscription = new SubscriptionRequest(); // SubscriptionRequest | Subscription request
    try {
      apiInstance.subscriptionListidPost(listid, subscription);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionApi#subscriptionListidPost");
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
| **listid** | **String**| Unique 16 characters ID of the contact list | |
| **subscription** | [**SubscriptionRequest**](SubscriptionRequest.md)| Subscription request | |

### Return type

null (empty response body)

### Authorization

[mqApiKey](../README.md#mqApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Empty response |  -  |
| **401** | Invalid api key or key does not have access to this ressource |  -  |
| **404** | The requested resource was not found |  -  |
| **422** | The request parameters were invalid |  -  |

