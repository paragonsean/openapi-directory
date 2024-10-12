# SubscriberStateChangesApi

All URIs are relative to *https://api.hubapi.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postMarketingV3MarketingEventsEventsExternalEventIdSubscriberStateEmailUpsertDoEmailUpsertById**](SubscriberStateChangesApi.md#postMarketingV3MarketingEventsEventsExternalEventIdSubscriberStateEmailUpsertDoEmailUpsertById) | **POST** /marketing/v3/marketing-events/events/{externalEventId}/{subscriberState}/email-upsert | Record |
| [**postMarketingV3MarketingEventsEventsExternalEventIdSubscriberStateUpsertDoUpsertById**](SubscriberStateChangesApi.md#postMarketingV3MarketingEventsEventsExternalEventIdSubscriberStateUpsertDoUpsertById) | **POST** /marketing/v3/marketing-events/events/{externalEventId}/{subscriberState}/upsert | Record |


<a id="postMarketingV3MarketingEventsEventsExternalEventIdSubscriberStateEmailUpsertDoEmailUpsertById"></a>
# **postMarketingV3MarketingEventsEventsExternalEventIdSubscriberStateEmailUpsertDoEmailUpsertById**
> Error postMarketingV3MarketingEventsEventsExternalEventIdSubscriberStateEmailUpsertDoEmailUpsertById(externalEventId, subscriberState, externalAccountId, batchInputMarketingEventEmailSubscriber)

Record

Record a subscription state between multiple HubSpot contacts and a marketing event, using contact email addresses. Note that the contact must already exist in HubSpot; a contact will not be created.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriberStateChangesApi;

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

    SubscriberStateChangesApi apiInstance = new SubscriberStateChangesApi(defaultClient);
    String externalEventId = "externalEventId_example"; // String | The id of the marketing event
    String subscriberState = "subscriberState_example"; // String | The new subscriber state for the HubSpot contacts and the specified marketing event
    String externalAccountId = "externalAccountId_example"; // String | The account id associated with the marketing event
    BatchInputMarketingEventEmailSubscriber batchInputMarketingEventEmailSubscriber = new BatchInputMarketingEventEmailSubscriber(); // BatchInputMarketingEventEmailSubscriber | The details of the contacts to subscribe to the event
    try {
      Error result = apiInstance.postMarketingV3MarketingEventsEventsExternalEventIdSubscriberStateEmailUpsertDoEmailUpsertById(externalEventId, subscriberState, externalAccountId, batchInputMarketingEventEmailSubscriber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriberStateChangesApi#postMarketingV3MarketingEventsEventsExternalEventIdSubscriberStateEmailUpsertDoEmailUpsertById");
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
| **subscriberState** | **String**| The new subscriber state for the HubSpot contacts and the specified marketing event | |
| **externalAccountId** | **String**| The account id associated with the marketing event | |
| **batchInputMarketingEventEmailSubscriber** | [**BatchInputMarketingEventEmailSubscriber**](BatchInputMarketingEventEmailSubscriber.md)| The details of the contacts to subscribe to the event | |

### Return type

[**Error**](Error.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | An error occurred. |  -  |

<a id="postMarketingV3MarketingEventsEventsExternalEventIdSubscriberStateUpsertDoUpsertById"></a>
# **postMarketingV3MarketingEventsEventsExternalEventIdSubscriberStateUpsertDoUpsertById**
> Error postMarketingV3MarketingEventsEventsExternalEventIdSubscriberStateUpsertDoUpsertById(externalEventId, subscriberState, externalAccountId, batchInputMarketingEventSubscriber)

Record

Record a subscription state between multiple HubSpot contacts and a marketing event, using HubSpot contact ids. Note that the contact must already exist in HubSpot; a contact will not be create.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriberStateChangesApi;

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

    SubscriberStateChangesApi apiInstance = new SubscriberStateChangesApi(defaultClient);
    String externalEventId = "externalEventId_example"; // String | The id of the marketing event
    String subscriberState = "subscriberState_example"; // String | The new subscriber state for the HubSpot contacts and the specified marketing event
    String externalAccountId = "externalAccountId_example"; // String | The account id associated with the marketing event
    BatchInputMarketingEventSubscriber batchInputMarketingEventSubscriber = new BatchInputMarketingEventSubscriber(); // BatchInputMarketingEventSubscriber | The details of the contacts to subscribe to the event
    try {
      Error result = apiInstance.postMarketingV3MarketingEventsEventsExternalEventIdSubscriberStateUpsertDoUpsertById(externalEventId, subscriberState, externalAccountId, batchInputMarketingEventSubscriber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriberStateChangesApi#postMarketingV3MarketingEventsEventsExternalEventIdSubscriberStateUpsertDoUpsertById");
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
| **subscriberState** | **String**| The new subscriber state for the HubSpot contacts and the specified marketing event | |
| **externalAccountId** | **String**| The account id associated with the marketing event | |
| **batchInputMarketingEventSubscriber** | [**BatchInputMarketingEventSubscriber**](BatchInputMarketingEventSubscriber.md)| The details of the contacts to subscribe to the event | |

### Return type

[**Error**](Error.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | An error occurred. |  -  |

