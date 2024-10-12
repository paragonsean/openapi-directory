# Subscriptions.StatusApi

All URIs are relative to *https://api.hubapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCommunicationPreferencesV3StatusEmailEmailAddressGetEmailStatus**](StatusApi.md#getCommunicationPreferencesV3StatusEmailEmailAddressGetEmailStatus) | **GET** /communication-preferences/v3/status/email/{emailAddress} | Get subscription statuses for a contact
[**postCommunicationPreferencesV3SubscribeSubscribe**](StatusApi.md#postCommunicationPreferencesV3SubscribeSubscribe) | **POST** /communication-preferences/v3/subscribe | Subscribe a contact
[**postCommunicationPreferencesV3UnsubscribeUnsubscribe**](StatusApi.md#postCommunicationPreferencesV3UnsubscribeUnsubscribe) | **POST** /communication-preferences/v3/unsubscribe | Unsubscribe a contact



## getCommunicationPreferencesV3StatusEmailEmailAddressGetEmailStatus

> PublicSubscriptionStatusesResponse getCommunicationPreferencesV3StatusEmailEmailAddressGetEmailStatus(emailAddress)

Get subscription statuses for a contact

Returns a list of subscriptions and their status for a given contact.

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

let apiInstance = new Subscriptions.StatusApi();
let emailAddress = "emailAddress_example"; // String | 
apiInstance.getCommunicationPreferencesV3StatusEmailEmailAddressGetEmailStatus(emailAddress, (error, data, response) => {
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
 **emailAddress** | **String**|  | 

### Return type

[**PublicSubscriptionStatusesResponse**](PublicSubscriptionStatusesResponse.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*


## postCommunicationPreferencesV3SubscribeSubscribe

> PublicSubscriptionStatus postCommunicationPreferencesV3SubscribeSubscribe(publicUpdateSubscriptionStatusRequest)

Subscribe a contact

Subscribes a contact to the given subscription type. This API is not valid to use for subscribing a contact at a brand or portal level and will return an error.

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

let apiInstance = new Subscriptions.StatusApi();
let publicUpdateSubscriptionStatusRequest = new Subscriptions.PublicUpdateSubscriptionStatusRequest(); // PublicUpdateSubscriptionStatusRequest | 
apiInstance.postCommunicationPreferencesV3SubscribeSubscribe(publicUpdateSubscriptionStatusRequest, (error, data, response) => {
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
 **publicUpdateSubscriptionStatusRequest** | [**PublicUpdateSubscriptionStatusRequest**](PublicUpdateSubscriptionStatusRequest.md)|  | 

### Return type

[**PublicSubscriptionStatus**](PublicSubscriptionStatus.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, */*


## postCommunicationPreferencesV3UnsubscribeUnsubscribe

> PublicSubscriptionStatus postCommunicationPreferencesV3UnsubscribeUnsubscribe(publicUpdateSubscriptionStatusRequest)

Unsubscribe a contact

Unsubscribes a contact from the given subscription type. This API is not valid to use for unsubscribing a contact at a brand or portal level and will return an error.

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

let apiInstance = new Subscriptions.StatusApi();
let publicUpdateSubscriptionStatusRequest = new Subscriptions.PublicUpdateSubscriptionStatusRequest(); // PublicUpdateSubscriptionStatusRequest | 
apiInstance.postCommunicationPreferencesV3UnsubscribeUnsubscribe(publicUpdateSubscriptionStatusRequest, (error, data, response) => {
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
 **publicUpdateSubscriptionStatusRequest** | [**PublicUpdateSubscriptionStatusRequest**](PublicUpdateSubscriptionStatusRequest.md)|  | 

### Return type

[**PublicSubscriptionStatus**](PublicSubscriptionStatus.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, */*

