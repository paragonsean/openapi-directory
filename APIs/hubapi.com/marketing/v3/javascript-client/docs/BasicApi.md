# MarketingEvents.BasicApi

All URIs are relative to *https://api.hubapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteMarketingV3MarketingEventsEventsExternalEventIdArchive**](BasicApi.md#deleteMarketingV3MarketingEventsEventsExternalEventIdArchive) | **DELETE** /marketing/v3/marketing-events/events/{externalEventId} | Delete a marketing event
[**getMarketingV3MarketingEventsEventsExternalEventIdGetById**](BasicApi.md#getMarketingV3MarketingEventsEventsExternalEventIdGetById) | **GET** /marketing/v3/marketing-events/events/{externalEventId} | Get a marketing event
[**patchMarketingV3MarketingEventsEventsExternalEventIdUpdate**](BasicApi.md#patchMarketingV3MarketingEventsEventsExternalEventIdUpdate) | **PATCH** /marketing/v3/marketing-events/events/{externalEventId} | Update a marketing event
[**postMarketingV3MarketingEventsEventsCreate**](BasicApi.md#postMarketingV3MarketingEventsEventsCreate) | **POST** /marketing/v3/marketing-events/events | Create a marketing event
[**postMarketingV3MarketingEventsEventsExternalEventIdCancelDoCancel**](BasicApi.md#postMarketingV3MarketingEventsEventsExternalEventIdCancelDoCancel) | **POST** /marketing/v3/marketing-events/events/{externalEventId}/cancel | Mark a marketing event as cancelled
[**putMarketingV3MarketingEventsEventsExternalEventIdReplace**](BasicApi.md#putMarketingV3MarketingEventsEventsExternalEventIdReplace) | **PUT** /marketing/v3/marketing-events/events/{externalEventId} | Create or update a marketing event



## deleteMarketingV3MarketingEventsEventsExternalEventIdArchive

> deleteMarketingV3MarketingEventsEventsExternalEventIdArchive(externalEventId, externalAccountId)

Delete a marketing event

Deletes an existing Marketing Event with the specified id, if one exists.

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

let apiInstance = new MarketingEvents.BasicApi();
let externalEventId = "externalEventId_example"; // String | The id of the marketing event to delete
let externalAccountId = "externalAccountId_example"; // String | The account id associated with the marketing event
apiInstance.deleteMarketingV3MarketingEventsEventsExternalEventIdArchive(externalEventId, externalAccountId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **externalEventId** | **String**| The id of the marketing event to delete | 
 **externalAccountId** | **String**| The account id associated with the marketing event | 

### Return type

null (empty response body)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getMarketingV3MarketingEventsEventsExternalEventIdGetById

> MarketingEventPublicReadResponse getMarketingV3MarketingEventsEventsExternalEventIdGetById(externalEventId, externalAccountId)

Get a marketing event

Returns the details of the Marketing Event with the specified id, if one exists.

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

let apiInstance = new MarketingEvents.BasicApi();
let externalEventId = "externalEventId_example"; // String | The id of the marketing event to return
let externalAccountId = "externalAccountId_example"; // String | The account id associated with the marketing event
apiInstance.getMarketingV3MarketingEventsEventsExternalEventIdGetById(externalEventId, externalAccountId, (error, data, response) => {
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
 **externalEventId** | **String**| The id of the marketing event to return | 
 **externalAccountId** | **String**| The account id associated with the marketing event | 

### Return type

[**MarketingEventPublicReadResponse**](MarketingEventPublicReadResponse.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*


## patchMarketingV3MarketingEventsEventsExternalEventIdUpdate

> MarketingEventPublicDefaultResponse patchMarketingV3MarketingEventsEventsExternalEventIdUpdate(externalEventId, externalAccountId, marketingEventUpdateRequestParams)

Update a marketing event

Updates an existing Marketing Event with the specified id, if one exists.

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

let apiInstance = new MarketingEvents.BasicApi();
let externalEventId = "externalEventId_example"; // String | The id of the marketing event to update
let externalAccountId = "externalAccountId_example"; // String | The account id associated with the marketing event
let marketingEventUpdateRequestParams = new MarketingEvents.MarketingEventUpdateRequestParams(); // MarketingEventUpdateRequestParams | The details of the marketing event to update
apiInstance.patchMarketingV3MarketingEventsEventsExternalEventIdUpdate(externalEventId, externalAccountId, marketingEventUpdateRequestParams, (error, data, response) => {
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
 **externalEventId** | **String**| The id of the marketing event to update | 
 **externalAccountId** | **String**| The account id associated with the marketing event | 
 **marketingEventUpdateRequestParams** | [**MarketingEventUpdateRequestParams**](MarketingEventUpdateRequestParams.md)| The details of the marketing event to update | 

### Return type

[**MarketingEventPublicDefaultResponse**](MarketingEventPublicDefaultResponse.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, */*


## postMarketingV3MarketingEventsEventsCreate

> MarketingEventDefaultResponse postMarketingV3MarketingEventsEventsCreate(marketingEventCreateRequestParams)

Create a marketing event

Creates a new marketing event in HubSpot

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

let apiInstance = new MarketingEvents.BasicApi();
let marketingEventCreateRequestParams = new MarketingEvents.MarketingEventCreateRequestParams(); // MarketingEventCreateRequestParams | The details of the marketing event to create
apiInstance.postMarketingV3MarketingEventsEventsCreate(marketingEventCreateRequestParams, (error, data, response) => {
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
 **marketingEventCreateRequestParams** | [**MarketingEventCreateRequestParams**](MarketingEventCreateRequestParams.md)| The details of the marketing event to create | 

### Return type

[**MarketingEventDefaultResponse**](MarketingEventDefaultResponse.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, */*


## postMarketingV3MarketingEventsEventsExternalEventIdCancelDoCancel

> MarketingEventDefaultResponse postMarketingV3MarketingEventsEventsExternalEventIdCancelDoCancel(externalEventId, externalAccountId)

Mark a marketing event as cancelled

Mark a marketing event as cancelled.

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

let apiInstance = new MarketingEvents.BasicApi();
let externalEventId = "externalEventId_example"; // String | The id of the marketing event to mark as cancelled
let externalAccountId = "externalAccountId_example"; // String | The account id associated with the marketing event
apiInstance.postMarketingV3MarketingEventsEventsExternalEventIdCancelDoCancel(externalEventId, externalAccountId, (error, data, response) => {
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
 **externalEventId** | **String**| The id of the marketing event to mark as cancelled | 
 **externalAccountId** | **String**| The account id associated with the marketing event | 

### Return type

[**MarketingEventDefaultResponse**](MarketingEventDefaultResponse.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*


## putMarketingV3MarketingEventsEventsExternalEventIdReplace

> MarketingEventPublicDefaultResponse putMarketingV3MarketingEventsEventsExternalEventIdReplace(externalEventId, marketingEventCreateRequestParams)

Create or update a marketing event

Upsets a Marketing Event. If there is an existing Marketing event with the specified id, it will be updated; otherwise a new event will be created.

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

let apiInstance = new MarketingEvents.BasicApi();
let externalEventId = "externalEventId_example"; // String | The id of the marketing event to upsert
let marketingEventCreateRequestParams = new MarketingEvents.MarketingEventCreateRequestParams(); // MarketingEventCreateRequestParams | The details of the marketing event to upsert
apiInstance.putMarketingV3MarketingEventsEventsExternalEventIdReplace(externalEventId, marketingEventCreateRequestParams, (error, data, response) => {
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
 **externalEventId** | **String**| The id of the marketing event to upsert | 
 **marketingEventCreateRequestParams** | [**MarketingEventCreateRequestParams**](MarketingEventCreateRequestParams.md)| The details of the marketing event to upsert | 

### Return type

[**MarketingEventPublicDefaultResponse**](MarketingEventPublicDefaultResponse.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, */*

