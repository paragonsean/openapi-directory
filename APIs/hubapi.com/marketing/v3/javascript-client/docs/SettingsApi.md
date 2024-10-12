# MarketingEvents.SettingsApi

All URIs are relative to *https://api.hubapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getMarketingV3MarketingEventsAppIdSettingsGetAll**](SettingsApi.md#getMarketingV3MarketingEventsAppIdSettingsGetAll) | **GET** /marketing/v3/marketing-events/{appId}/settings | Retrieve the application settings
[**postMarketingV3MarketingEventsAppIdSettingsCreate**](SettingsApi.md#postMarketingV3MarketingEventsAppIdSettingsCreate) | **POST** /marketing/v3/marketing-events/{appId}/settings | Update the application settings



## getMarketingV3MarketingEventsAppIdSettingsGetAll

> EventDetailSettings getMarketingV3MarketingEventsAppIdSettingsGetAll(appId)

Retrieve the application settings

Retrieve the current settings for the application.

### Example

```javascript
import MarketingEvents from 'marketing_events';
let defaultClient = MarketingEvents.ApiClient.instance;
// Configure API key authorization: developer_hapikey
let developer_hapikey = defaultClient.authentications['developer_hapikey'];
developer_hapikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developer_hapikey.apiKeyPrefix = 'Token';

let apiInstance = new MarketingEvents.SettingsApi();
let appId = 56; // Number | The id of the application to retrieve the settings for.
apiInstance.getMarketingV3MarketingEventsAppIdSettingsGetAll(appId, (error, data, response) => {
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
 **appId** | **Number**| The id of the application to retrieve the settings for. | 

### Return type

[**EventDetailSettings**](EventDetailSettings.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*


## postMarketingV3MarketingEventsAppIdSettingsCreate

> EventDetailSettings postMarketingV3MarketingEventsAppIdSettingsCreate(appId, eventDetailSettingsUrl)

Update the application settings

Create or update the current settings for the application.

### Example

```javascript
import MarketingEvents from 'marketing_events';
let defaultClient = MarketingEvents.ApiClient.instance;
// Configure API key authorization: developer_hapikey
let developer_hapikey = defaultClient.authentications['developer_hapikey'];
developer_hapikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developer_hapikey.apiKeyPrefix = 'Token';

let apiInstance = new MarketingEvents.SettingsApi();
let appId = 56; // Number | The id of the application to update the settings for.
let eventDetailSettingsUrl = new MarketingEvents.EventDetailSettingsUrl(); // EventDetailSettingsUrl | The new application settings
apiInstance.postMarketingV3MarketingEventsAppIdSettingsCreate(appId, eventDetailSettingsUrl, (error, data, response) => {
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
 **appId** | **Number**| The id of the application to update the settings for. | 
 **eventDetailSettingsUrl** | [**EventDetailSettingsUrl**](EventDetailSettingsUrl.md)| The new application settings | 

### Return type

[**EventDetailSettings**](EventDetailSettings.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, */*

