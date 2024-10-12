# MarketingEvents.BatchApi

All URIs are relative to *https://api.hubapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postMarketingV3MarketingEventsEventsDeleteArchive**](BatchApi.md#postMarketingV3MarketingEventsEventsDeleteArchive) | **POST** /marketing/v3/marketing-events/events/delete | Delete multiple marketing events
[**postMarketingV3MarketingEventsEventsUpsertDoUpsert**](BatchApi.md#postMarketingV3MarketingEventsEventsUpsertDoUpsert) | **POST** /marketing/v3/marketing-events/events/upsert | Create or update multiple marketing events



## postMarketingV3MarketingEventsEventsDeleteArchive

> Error postMarketingV3MarketingEventsEventsDeleteArchive(batchInputMarketingEventExternalUniqueIdentifier)

Delete multiple marketing events

Bulk delete a number of marketing events in HubSpot

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

let apiInstance = new MarketingEvents.BatchApi();
let batchInputMarketingEventExternalUniqueIdentifier = new MarketingEvents.BatchInputMarketingEventExternalUniqueIdentifier(); // BatchInputMarketingEventExternalUniqueIdentifier | The details of the marketing events to delete
apiInstance.postMarketingV3MarketingEventsEventsDeleteArchive(batchInputMarketingEventExternalUniqueIdentifier, (error, data, response) => {
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
 **batchInputMarketingEventExternalUniqueIdentifier** | [**BatchInputMarketingEventExternalUniqueIdentifier**](BatchInputMarketingEventExternalUniqueIdentifier.md)| The details of the marketing events to delete | 

### Return type

[**Error**](Error.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## postMarketingV3MarketingEventsEventsUpsertDoUpsert

> BatchResponseMarketingEventPublicDefaultResponse postMarketingV3MarketingEventsEventsUpsertDoUpsert(batchInputMarketingEventCreateRequestParams)

Create or update multiple marketing events

Upset multiple Marketing Event. If there is an existing Marketing event with the specified id, it will be updated; otherwise a new event will be created.

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

let apiInstance = new MarketingEvents.BatchApi();
let batchInputMarketingEventCreateRequestParams = new MarketingEvents.BatchInputMarketingEventCreateRequestParams(); // BatchInputMarketingEventCreateRequestParams | The details of the marketing events to upsert
apiInstance.postMarketingV3MarketingEventsEventsUpsertDoUpsert(batchInputMarketingEventCreateRequestParams, (error, data, response) => {
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
 **batchInputMarketingEventCreateRequestParams** | [**BatchInputMarketingEventCreateRequestParams**](BatchInputMarketingEventCreateRequestParams.md)| The details of the marketing events to upsert | 

### Return type

[**BatchResponseMarketingEventPublicDefaultResponse**](BatchResponseMarketingEventPublicDefaultResponse.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, */*

