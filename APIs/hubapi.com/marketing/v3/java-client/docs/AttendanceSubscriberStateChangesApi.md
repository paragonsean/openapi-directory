# AttendanceSubscriberStateChangesApi

All URIs are relative to *https://api.hubapi.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postMarketingV3MarketingEventsAttendanceExternalEventIdSubscriberStateCreateCreate**](AttendanceSubscriberStateChangesApi.md#postMarketingV3MarketingEventsAttendanceExternalEventIdSubscriberStateCreateCreate) | **POST** /marketing/v3/marketing-events/attendance/{externalEventId}/{subscriberState}/create | Record |
| [**postMarketingV3MarketingEventsAttendanceExternalEventIdSubscriberStateEmailCreateCreateByEmail**](AttendanceSubscriberStateChangesApi.md#postMarketingV3MarketingEventsAttendanceExternalEventIdSubscriberStateEmailCreateCreateByEmail) | **POST** /marketing/v3/marketing-events/attendance/{externalEventId}/{subscriberState}/email-create | Record |


<a id="postMarketingV3MarketingEventsAttendanceExternalEventIdSubscriberStateCreateCreate"></a>
# **postMarketingV3MarketingEventsAttendanceExternalEventIdSubscriberStateCreateCreate**
> BatchResponseSubscriberVidResponse postMarketingV3MarketingEventsAttendanceExternalEventIdSubscriberStateCreateCreate(externalEventId, subscriberState, batchInputMarketingEventSubscriber, externalAccountId)

Record

Record a subscription state between multiple HubSpot contacts and a marketing event, using HubSpot contact ids.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttendanceSubscriberStateChangesApi;

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

    AttendanceSubscriberStateChangesApi apiInstance = new AttendanceSubscriberStateChangesApi(defaultClient);
    String externalEventId = "externalEventId_example"; // String | The id of the marketing event
    String subscriberState = "subscriberState_example"; // String | The new subscriber state for the HubSpot contacts and the specified marketing event. For example: 'register', 'attend' or 'cancel'.
    BatchInputMarketingEventSubscriber batchInputMarketingEventSubscriber = new BatchInputMarketingEventSubscriber(); // BatchInputMarketingEventSubscriber | The details of the contacts to subscribe to the event. Parameters of join and left time if state is Attended.
    String externalAccountId = "externalAccountId_example"; // String | The account id associated with the marketing event
    try {
      BatchResponseSubscriberVidResponse result = apiInstance.postMarketingV3MarketingEventsAttendanceExternalEventIdSubscriberStateCreateCreate(externalEventId, subscriberState, batchInputMarketingEventSubscriber, externalAccountId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttendanceSubscriberStateChangesApi#postMarketingV3MarketingEventsAttendanceExternalEventIdSubscriberStateCreateCreate");
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
| **externalEventId** | **String**| The id of the marketing event | |
| **subscriberState** | **String**| The new subscriber state for the HubSpot contacts and the specified marketing event. For example: &#39;register&#39;, &#39;attend&#39; or &#39;cancel&#39;. | |
| **batchInputMarketingEventSubscriber** | [**BatchInputMarketingEventSubscriber**](BatchInputMarketingEventSubscriber.md)| The details of the contacts to subscribe to the event. Parameters of join and left time if state is Attended. | |
| **externalAccountId** | **String**| The account id associated with the marketing event | [optional] |

### Return type

[**BatchResponseSubscriberVidResponse**](BatchResponseSubscriberVidResponse.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | An error occurred. |  -  |

<a id="postMarketingV3MarketingEventsAttendanceExternalEventIdSubscriberStateEmailCreateCreateByEmail"></a>
# **postMarketingV3MarketingEventsAttendanceExternalEventIdSubscriberStateEmailCreateCreateByEmail**
> BatchResponseSubscriberEmailResponse postMarketingV3MarketingEventsAttendanceExternalEventIdSubscriberStateEmailCreateCreateByEmail(externalEventId, subscriberState, batchInputMarketingEventEmailSubscriber, externalAccountId)

Record

Record a subscription state between multiple HubSpot contacts and a marketing event, using contact email addresses. If contact is not present it will be automatically created.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttendanceSubscriberStateChangesApi;

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

    AttendanceSubscriberStateChangesApi apiInstance = new AttendanceSubscriberStateChangesApi(defaultClient);
    String externalEventId = "externalEventId_example"; // String | The id of the marketing event
    String subscriberState = "subscriberState_example"; // String | The new subscriber state for the HubSpot contacts and the specified marketing event. For example: 'register', 'attend' or 'cancel'.
    BatchInputMarketingEventEmailSubscriber batchInputMarketingEventEmailSubscriber = new BatchInputMarketingEventEmailSubscriber(); // BatchInputMarketingEventEmailSubscriber | The details of the contacts to subscribe to the event. Parameters of join and left time if state is Attended.
    String externalAccountId = "externalAccountId_example"; // String | The account id associated with the marketing event
    try {
      BatchResponseSubscriberEmailResponse result = apiInstance.postMarketingV3MarketingEventsAttendanceExternalEventIdSubscriberStateEmailCreateCreateByEmail(externalEventId, subscriberState, batchInputMarketingEventEmailSubscriber, externalAccountId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttendanceSubscriberStateChangesApi#postMarketingV3MarketingEventsAttendanceExternalEventIdSubscriberStateEmailCreateCreateByEmail");
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
| **externalEventId** | **String**| The id of the marketing event | |
| **subscriberState** | **String**| The new subscriber state for the HubSpot contacts and the specified marketing event. For example: &#39;register&#39;, &#39;attend&#39; or &#39;cancel&#39;. | |
| **batchInputMarketingEventEmailSubscriber** | [**BatchInputMarketingEventEmailSubscriber**](BatchInputMarketingEventEmailSubscriber.md)| The details of the contacts to subscribe to the event. Parameters of join and left time if state is Attended. | |
| **externalAccountId** | **String**| The account id associated with the marketing event | [optional] |

### Return type

[**BatchResponseSubscriberEmailResponse**](BatchResponseSubscriberEmailResponse.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | An error occurred. |  -  |

