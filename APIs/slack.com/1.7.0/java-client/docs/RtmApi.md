# RtmApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**rtmConnect**](RtmApi.md#rtmConnect) | **GET** /rtm.connect |  |


<a id="rtmConnect"></a>
# **rtmConnect**
> RtmConnectSchema rtmConnect(token, batchPresenceAware, presenceSub)



Starts a Real Time Messaging session.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RtmApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    RtmApi apiInstance = new RtmApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `rtm:stream`
    Boolean batchPresenceAware = true; // Boolean | Batch presence deliveries via subscription. Enabling changes the shape of `presence_change` events. See [batch presence](/docs/presence-and-status#batching).
    Boolean presenceSub = true; // Boolean | Only deliver presence events when requested by subscription. See [presence subscriptions](/docs/presence-and-status#subscriptions).
    try {
      RtmConnectSchema result = apiInstance.rtmConnect(token, batchPresenceAware, presenceSub);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RtmApi#rtmConnect");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;rtm:stream&#x60; | |
| **batchPresenceAware** | **Boolean**| Batch presence deliveries via subscription. Enabling changes the shape of &#x60;presence_change&#x60; events. See [batch presence](/docs/presence-and-status#batching). | [optional] |
| **presenceSub** | **Boolean**| Only deliver presence events when requested by subscription. See [presence subscriptions](/docs/presence-and-status#subscriptions). | [optional] |

### Return type

[**RtmConnectSchema**](RtmConnectSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

