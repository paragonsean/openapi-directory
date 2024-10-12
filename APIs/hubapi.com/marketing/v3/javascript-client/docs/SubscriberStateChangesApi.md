# MarketingEvents.SubscriberStateChangesApi

All URIs are relative to *https://api.hubapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postMarketingV3MarketingEventsEventsExternalEventIdSubscriberStateEmailUpsertDoEmailUpsertById**](SubscriberStateChangesApi.md#postMarketingV3MarketingEventsEventsExternalEventIdSubscriberStateEmailUpsertDoEmailUpsertById) | **POST** /marketing/v3/marketing-events/events/{externalEventId}/{subscriberState}/email-upsert | Record
[**postMarketingV3MarketingEventsEventsExternalEventIdSubscriberStateUpsertDoUpsertById**](SubscriberStateChangesApi.md#postMarketingV3MarketingEventsEventsExternalEventIdSubscriberStateUpsertDoUpsertById) | **POST** /marketing/v3/marketing-events/events/{externalEventId}/{subscriberState}/upsert | Record



## postMarketingV3MarketingEventsEventsExternalEventIdSubscriberStateEmailUpsertDoEmailUpsertById

> Error postMarketingV3MarketingEventsEventsExternalEventIdSubscriberStateEmailUpsertDoEmailUpsertById(externalEventId, subscriberState, externalAccountId, batchInputMarketingEventEmailSubscriber)

Record

Record a subscription state between multiple HubSpot contacts and a marketing event, using contact email addresses. Note that the contact must already exist in HubSpot; a contact will not be created.

### Example

```javascript
import MarketingEvents from 'marketing_events';
let defaultClient = MarketingEvents.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2_legacy
let oauth2_legacy = defaultClient.authentications['oauth2_legacy'];
oauth2_legacy.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: private_apps_legacy
let private_apps_legacy = defaultClient.authentications['private_apps_legacy'];
private_apps_legacy.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//private_apps_legacy.apiKeyPrefix = 'Token';

let apiInstance = new MarketingEvents.SubscriberStateChangesApi();
let externalEventId = "externalEventId_example"; // String | The id of the marketing event
let subscriberState = "subscriberState_example"; // String | The new subscriber state for the HubSpot contacts and the specified marketing event
let externalAccountId = "externalAccountId_example"; // String | The account id associated with the marketing event
let batchInputMarketingEventEmailSubscriber = new MarketingEvents.BatchInputMarketingEventEmailSubscriber(); // BatchInputMarketingEventEmailSubscriber | The details of the contacts to subscribe to the event
apiInstance.postMarketingV3MarketingEventsEventsExternalEventIdSubscriberStateEmailUpsertDoEmailUpsertById(externalEventId, subscriberState, externalAccountId, batchInputMarketingEventEmailSubscriber, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **externalEventId** | **String**| The id of the marketing event | 
 **subscriberState** | **String**| The new subscriber state for the HubSpot contacts and the specified marketing event | 
 **externalAccountId** | **String**| The account id associated with the marketing event | 
 **batchInputMarketingEventEmailSubscriber** | [**BatchInputMarketingEventEmailSubscriber**](BatchInputMarketingEventEmailSubscriber.md)| The details of the contacts to subscribe to the event | 

### Return type

[**Error**](Error.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## postMarketingV3MarketingEventsEventsExternalEventIdSubscriberStateUpsertDoUpsertById

> Error postMarketingV3MarketingEventsEventsExternalEventIdSubscriberStateUpsertDoUpsertById(externalEventId, subscriberState, externalAccountId, batchInputMarketingEventSubscriber)

Record

Record a subscription state between multiple HubSpot contacts and a marketing event, using HubSpot contact ids. Note that the contact must already exist in HubSpot; a contact will not be create.

### Example

```javascript
import MarketingEvents from 'marketing_events';
let defaultClient = MarketingEvents.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2_legacy
let oauth2_legacy = defaultClient.authentications['oauth2_legacy'];
oauth2_legacy.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: private_apps_legacy
let private_apps_legacy = defaultClient.authentications['private_apps_legacy'];
private_apps_legacy.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//private_apps_legacy.apiKeyPrefix = 'Token';

let apiInstance = new MarketingEvents.SubscriberStateChangesApi();
let externalEventId = "externalEventId_example"; // String | The id of the marketing event
let subscriberState = "subscriberState_example"; // String | The new subscriber state for the HubSpot contacts and the specified marketing event
let externalAccountId = "externalAccountId_example"; // String | The account id associated with the marketing event
let batchInputMarketingEventSubscriber = new MarketingEvents.BatchInputMarketingEventSubscriber(); // BatchInputMarketingEventSubscriber | The details of the contacts to subscribe to the event
apiInstance.postMarketingV3MarketingEventsEventsExternalEventIdSubscriberStateUpsertDoUpsertById(externalEventId, subscriberState, externalAccountId, batchInputMarketingEventSubscriber, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **externalEventId** | **String**| The id of the marketing event | 
 **subscriberState** | **String**| The new subscriber state for the HubSpot contacts and the specified marketing event | 
 **externalAccountId** | **String**| The account id associated with the marketing event | 
 **batchInputMarketingEventSubscriber** | [**BatchInputMarketingEventSubscriber**](BatchInputMarketingEventSubscriber.md)| The details of the contacts to subscribe to the event | 

### Return type

[**Error**](Error.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*

