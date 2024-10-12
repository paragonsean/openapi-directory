# Subscriptions.DefinitionApi

All URIs are relative to *https://api.hubapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCommunicationPreferencesV3DefinitionsGetPage**](DefinitionApi.md#getCommunicationPreferencesV3DefinitionsGetPage) | **GET** /communication-preferences/v3/definitions | Get subscription definitions



## getCommunicationPreferencesV3DefinitionsGetPage

> SubscriptionDefinitionsResponse getCommunicationPreferencesV3DefinitionsGetPage()

Get subscription definitions

Get a list of all subscription definitions for the portal

### Example

```javascript
import Subscriptions from 'subscriptions';
let defaultClient = Subscriptions.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2_legacy
let oauth2_legacy = defaultClient.authentications['oauth2_legacy'];
oauth2_legacy.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: private_apps_legacy
let private_apps_legacy = defaultClient.authentications['private_apps_legacy'];
private_apps_legacy.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//private_apps_legacy.apiKeyPrefix = 'Token';

let apiInstance = new Subscriptions.DefinitionApi();
apiInstance.getCommunicationPreferencesV3DefinitionsGetPage((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**SubscriptionDefinitionsResponse**](SubscriptionDefinitionsResponse.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*

