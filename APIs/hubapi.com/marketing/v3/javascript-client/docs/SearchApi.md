# MarketingEvents.SearchApi

All URIs are relative to *https://api.hubapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getMarketingV3MarketingEventsEventsSearchDoSearch**](SearchApi.md#getMarketingV3MarketingEventsEventsSearchDoSearch) | **GET** /marketing/v3/marketing-events/events/search | Search for marketing events



## getMarketingV3MarketingEventsEventsSearchDoSearch

> CollectionResponseMarketingEventExternalUniqueIdentifierNoPaging getMarketingV3MarketingEventsEventsSearchDoSearch(q)

Search for marketing events

Search for marketing events that have an event id that starts with the query string

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

let apiInstance = new MarketingEvents.SearchApi();
let q = "q_example"; // String | The id of the marketing event in the external event application
apiInstance.getMarketingV3MarketingEventsEventsSearchDoSearch(q, (error, data, response) => {
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
 **q** | **String**| The id of the marketing event in the external event application | 

### Return type

[**CollectionResponseMarketingEventExternalUniqueIdentifierNoPaging**](CollectionResponseMarketingEventExternalUniqueIdentifierNoPaging.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*

