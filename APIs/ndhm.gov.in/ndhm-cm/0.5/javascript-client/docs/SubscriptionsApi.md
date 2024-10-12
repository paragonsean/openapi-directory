# HealthDataConsentManager.SubscriptionsApi

All URIs are relative to *https://dev.ndhm.gov.in/cm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05SubscriptionRequestsCmInitPost**](SubscriptionsApi.md#v05SubscriptionRequestsCmInitPost) | **POST** /v0.5/subscription-requests/cm/init | Request for subscription
[**v05SubscriptionRequestsHiuOnNotifyPost**](SubscriptionsApi.md#v05SubscriptionRequestsHiuOnNotifyPost) | **POST** /v0.5/subscription-requests/hiu/on-notify | Callback API for /subscription-requests/hiu/notify to acknowledge receipt of notification.
[**v05SubscriptionsHiuOnNotifyPost**](SubscriptionsApi.md#v05SubscriptionsHiuOnNotifyPost) | **POST** /v0.5/subscriptions/hiu/on-notify | Callback API for /subscriptions/hiu/notify to acknowledge receipt of notification.



## v05SubscriptionRequestsCmInitPost

> v05SubscriptionRequestsCmInitPost(authorization, subscriptionRequest)

Request for subscription

creates a request for subscription. The subscription categories can be for care-contexts linkages or availability of data against existing care-contexts. Note that the requester must have HIU role

### Example

```javascript
import HealthDataConsentManager from 'health_data_consent_manager';

let apiInstance = new HealthDataConsentManager.SubscriptionsApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let subscriptionRequest = new HealthDataConsentManager.SubscriptionRequest(); // SubscriptionRequest | 
apiInstance.v05SubscriptionRequestsCmInitPost(authorization, subscriptionRequest, (error, data, response) => {
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
 **authorization** | **String**| Access token which was issued after successful login with gateway auth server. | 
 **subscriptionRequest** | [**SubscriptionRequest**](SubscriptionRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05SubscriptionRequestsHiuOnNotifyPost

> v05SubscriptionRequestsHiuOnNotifyPost(authorization, hIUSubscriptionRequestNotificationAcknowledgement)

Callback API for /subscription-requests/hiu/notify to acknowledge receipt of notification.

This API is called by HIU as acknowledgement to subscription request relevant notifications.  

### Example

```javascript
import HealthDataConsentManager from 'health_data_consent_manager';

let apiInstance = new HealthDataConsentManager.SubscriptionsApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let hIUSubscriptionRequestNotificationAcknowledgement = new HealthDataConsentManager.HIUSubscriptionRequestNotificationAcknowledgement(); // HIUSubscriptionRequestNotificationAcknowledgement | 
apiInstance.v05SubscriptionRequestsHiuOnNotifyPost(authorization, hIUSubscriptionRequestNotificationAcknowledgement, (error, data, response) => {
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
 **authorization** | **String**| Access token which was issued after successful login with gateway auth server. | 
 **hIUSubscriptionRequestNotificationAcknowledgement** | [**HIUSubscriptionRequestNotificationAcknowledgement**](HIUSubscriptionRequestNotificationAcknowledgement.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/xml


## v05SubscriptionsHiuOnNotifyPost

> v05SubscriptionsHiuOnNotifyPost(authorization, hIUSubscriptionNotificationAcknowledgment)

Callback API for /subscriptions/hiu/notify to acknowledge receipt of notification.

This API is called by HIU as acknowledgement to consent notifications, specifically for cases when consent is REVOKED or EXPIRED. 

### Example

```javascript
import HealthDataConsentManager from 'health_data_consent_manager';

let apiInstance = new HealthDataConsentManager.SubscriptionsApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let hIUSubscriptionNotificationAcknowledgment = new HealthDataConsentManager.HIUSubscriptionNotificationAcknowledgment(); // HIUSubscriptionNotificationAcknowledgment | 
apiInstance.v05SubscriptionsHiuOnNotifyPost(authorization, hIUSubscriptionNotificationAcknowledgment, (error, data, response) => {
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
 **authorization** | **String**| Access token which was issued after successful login with gateway auth server. | 
 **hIUSubscriptionNotificationAcknowledgment** | [**HIUSubscriptionNotificationAcknowledgment**](HIUSubscriptionNotificationAcknowledgment.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/xml

