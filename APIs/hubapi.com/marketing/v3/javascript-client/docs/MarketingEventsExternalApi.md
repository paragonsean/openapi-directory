# MarketingEvents.MarketingEventsExternalApi

All URIs are relative to *https://api.hubapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postMarketingV3MarketingEventsEventsExternalEventIdCompleteComplete**](MarketingEventsExternalApi.md#postMarketingV3MarketingEventsEventsExternalEventIdCompleteComplete) | **POST** /marketing/v3/marketing-events/events/{externalEventId}/complete | 



## postMarketingV3MarketingEventsEventsExternalEventIdCompleteComplete

> MarketingEventDefaultResponse postMarketingV3MarketingEventsEventsExternalEventIdCompleteComplete(externalEventId, externalAccountId, marketingEventCompleteRequestParams)



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

let apiInstance = new MarketingEvents.MarketingEventsExternalApi();
let externalEventId = "externalEventId_example"; // String | 
let externalAccountId = "externalAccountId_example"; // String | 
let marketingEventCompleteRequestParams = new MarketingEvents.MarketingEventCompleteRequestParams(); // MarketingEventCompleteRequestParams | 
apiInstance.postMarketingV3MarketingEventsEventsExternalEventIdCompleteComplete(externalEventId, externalAccountId, marketingEventCompleteRequestParams, (error, data, response) => {
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
 **externalEventId** | **String**|  | 
 **externalAccountId** | **String**|  | 
 **marketingEventCompleteRequestParams** | [**MarketingEventCompleteRequestParams**](MarketingEventCompleteRequestParams.md)|  | 

### Return type

[**MarketingEventDefaultResponse**](MarketingEventDefaultResponse.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, */*

