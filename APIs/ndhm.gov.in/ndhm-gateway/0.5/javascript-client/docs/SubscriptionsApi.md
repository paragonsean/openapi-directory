# Gateway.SubscriptionsApi

All URIs are relative to *https://dev.ndhm.gov.in/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05SubscriptionRequestsCmInitPost**](SubscriptionsApi.md#v05SubscriptionRequestsCmInitPost) | **POST** /v0.5/subscription-requests/cm/init | Request for subscription
[**v05SubscriptionRequestsCmOnInitPost**](SubscriptionsApi.md#v05SubscriptionRequestsCmOnInitPost) | **POST** /v0.5/subscription-requests/cm/on-init | callback API for the /subscription-requests/cm/init to notify a HIU on acceptance/acknowledgement of the request for subscription.
[**v05SubscriptionRequestsHiuNotifyPost**](SubscriptionsApi.md#v05SubscriptionRequestsHiuNotifyPost) | **POST** /v0.5/subscription-requests/hiu/notify | Notification for subscription grant/deny/revoke
[**v05SubscriptionRequestsHiuOnNotifyPost**](SubscriptionsApi.md#v05SubscriptionRequestsHiuOnNotifyPost) | **POST** /v0.5/subscription-requests/hiu/on-notify | Callback API for /subscription-requests/hiu/notify to acknowledge receipt of notification.
[**v05SubscriptionsHiuNotifyPost**](SubscriptionsApi.md#v05SubscriptionsHiuNotifyPost) | **POST** /v0.5/subscriptions/hiu/notify | Notification to HIU on basis of a granted subscription
[**v05SubscriptionsHiuOnNotifyPost**](SubscriptionsApi.md#v05SubscriptionsHiuOnNotifyPost) | **POST** /v0.5/subscriptions/hiu/on-notify | Callback API for /subscriptions/hiu/notify to acknowledge receipt of notification.



## v05SubscriptionRequestsCmInitPost

> v05SubscriptionRequestsCmInitPost(authorization, X_CM_ID, subscriptionRequest)

Request for subscription

creates a request for subscription. The subscription categories can be for care-contexts linkages or availability of data against existing care-contexts. Note that the requester must have HIU role

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.SubscriptionsApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
let subscriptionRequest = new Gateway.SubscriptionRequest(); // SubscriptionRequest | 
apiInstance.v05SubscriptionRequestsCmInitPost(authorization, X_CM_ID, subscriptionRequest, (error, data, response) => {
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
 **X_CM_ID** | **String**| Suffix of the consent manager to which the request was intended. | 
 **subscriptionRequest** | [**SubscriptionRequest**](SubscriptionRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05SubscriptionRequestsCmOnInitPost

> v05SubscriptionRequestsCmOnInitPost(authorization, X_HIU_ID, hIUSubscriptionRequestReceipt)

callback API for the /subscription-requests/cm/init to notify a HIU on acceptance/acknowledgement of the request for subscription.

This callback API acknowledges the request for subscription from a HIU, and sends back a \&quot;id\&quot; that will be used when the patient/user approves or denies the subscription.  

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.SubscriptionsApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_HIU_ID = "X_HIU_ID_example"; // String | Identifier of the health information user to which the request was intended.
let hIUSubscriptionRequestReceipt = new Gateway.HIUSubscriptionRequestReceipt(); // HIUSubscriptionRequestReceipt | 
apiInstance.v05SubscriptionRequestsCmOnInitPost(authorization, X_HIU_ID, hIUSubscriptionRequestReceipt, (error, data, response) => {
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
 **X_HIU_ID** | **String**| Identifier of the health information user to which the request was intended. | 
 **hIUSubscriptionRequestReceipt** | [**HIUSubscriptionRequestReceipt**](HIUSubscriptionRequestReceipt.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/xml


## v05SubscriptionRequestsHiuNotifyPost

> v05SubscriptionRequestsHiuNotifyPost(authorization, X_HIU_ID, subscriptionApprovalNotification)

Notification for subscription grant/deny/revoke

This API is used by CM to notify a HIU to grant or deny a request for subscription, and also to notify that in case an existing subscription is revoked or expired. For notifying that a particular subscription request was GRANTED or DENIED, the **subscriptionRequestId** is passed.  

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.SubscriptionsApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_HIU_ID = "X_HIU_ID_example"; // String | Identifier of the health information user to which the request was intended.
let subscriptionApprovalNotification = new Gateway.SubscriptionApprovalNotification(); // SubscriptionApprovalNotification | 
apiInstance.v05SubscriptionRequestsHiuNotifyPost(authorization, X_HIU_ID, subscriptionApprovalNotification, (error, data, response) => {
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
 **X_HIU_ID** | **String**| Identifier of the health information user to which the request was intended. | 
 **subscriptionApprovalNotification** | [**SubscriptionApprovalNotification**](SubscriptionApprovalNotification.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05SubscriptionRequestsHiuOnNotifyPost

> v05SubscriptionRequestsHiuOnNotifyPost(authorization, X_CM_ID, hIUSubscriptionRequestNotificationAcknowledgement)

Callback API for /subscription-requests/hiu/notify to acknowledge receipt of notification.

This API is called by HIU as acknowledgement to subscription request relevant notifications.  

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.SubscriptionsApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
let hIUSubscriptionRequestNotificationAcknowledgement = new Gateway.HIUSubscriptionRequestNotificationAcknowledgement(); // HIUSubscriptionRequestNotificationAcknowledgement | 
apiInstance.v05SubscriptionRequestsHiuOnNotifyPost(authorization, X_CM_ID, hIUSubscriptionRequestNotificationAcknowledgement, (error, data, response) => {
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
 **X_CM_ID** | **String**| Suffix of the consent manager to which the request was intended. | 
 **hIUSubscriptionRequestNotificationAcknowledgement** | [**HIUSubscriptionRequestNotificationAcknowledgement**](HIUSubscriptionRequestNotificationAcknowledgement.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/xml


## v05SubscriptionsHiuNotifyPost

> v05SubscriptionsHiuNotifyPost(authorization, X_HIU_ID, hIUSubscriptionNotification)

Notification to HIU on basis of a granted subscription

This API is used by CM to notify a HIU for notification relevant to subscription. Notifications are sent to subscribed HIUs whenever a new care-context is linked or new data is available on an existing linked care-context.  1. if event.category &#x3D; LINK, then only care-contexts are passed when new care-contexts are linked for patient.  2. If event.category &#x3D; DATA, then hiTypes are passed. Care-context is passed only if the subscribed HIU has any valid consent for that care-context 

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.SubscriptionsApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_HIU_ID = "X_HIU_ID_example"; // String | Identifier of the health information user to which the request was intended.
let hIUSubscriptionNotification = new Gateway.HIUSubscriptionNotification(); // HIUSubscriptionNotification | 
apiInstance.v05SubscriptionsHiuNotifyPost(authorization, X_HIU_ID, hIUSubscriptionNotification, (error, data, response) => {
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
 **X_HIU_ID** | **String**| Identifier of the health information user to which the request was intended. | 
 **hIUSubscriptionNotification** | [**HIUSubscriptionNotification**](HIUSubscriptionNotification.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05SubscriptionsHiuOnNotifyPost

> v05SubscriptionsHiuOnNotifyPost(authorization, X_CM_ID, hIUSubscriptionNotificationAcknowledgment)

Callback API for /subscriptions/hiu/notify to acknowledge receipt of notification.

This API is called by HIU as acknowledgement to consent notifications, specifically for cases when consent is REVOKED or EXPIRED. 

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.SubscriptionsApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
let hIUSubscriptionNotificationAcknowledgment = new Gateway.HIUSubscriptionNotificationAcknowledgment(); // HIUSubscriptionNotificationAcknowledgment | 
apiInstance.v05SubscriptionsHiuOnNotifyPost(authorization, X_CM_ID, hIUSubscriptionNotificationAcknowledgment, (error, data, response) => {
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
 **X_CM_ID** | **String**| Suffix of the consent manager to which the request was intended. | 
 **hIUSubscriptionNotificationAcknowledgment** | [**HIUSubscriptionNotificationAcknowledgment**](HIUSubscriptionNotificationAcknowledgment.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/xml

