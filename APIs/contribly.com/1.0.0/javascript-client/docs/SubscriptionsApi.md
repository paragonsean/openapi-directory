# Contribly.SubscriptionsApi

All URIs are relative to *https://api.contribly.com/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscriptionTypesGet**](SubscriptionsApi.md#subscriptionTypesGet) | **GET** /subscription-types | Subscription types
[**subscriptionsGet**](SubscriptionsApi.md#subscriptionsGet) | **GET** /subscriptions | List subscriptions for the authorised user.
[**subscriptionsIdDelete**](SubscriptionsApi.md#subscriptionsIdDelete) | **DELETE** /subscriptions/{id} | Delete a subscription.



## subscriptionTypesGet

> [SubscriptionType] subscriptionTypesGet()

Subscription types

List available subscription types

### Example

```javascript
import Contribly from 'contribly';

let apiInstance = new Contribly.SubscriptionsApi();
apiInstance.subscriptionTypesGet((error, data, response) => {
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

[**[SubscriptionType]**](SubscriptionType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## subscriptionsGet

> [Subscription] subscriptionsGet(subscriptionSubmission)

List subscriptions for the authorised user.

### Example

```javascript
import Contribly from 'contribly';

let apiInstance = new Contribly.SubscriptionsApi();
let subscriptionSubmission = new Contribly.SubscriptionSubmission(); // SubscriptionSubmission | Subscription to be created
apiInstance.subscriptionsGet(subscriptionSubmission, (error, data, response) => {
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
 **subscriptionSubmission** | [**SubscriptionSubmission**](SubscriptionSubmission.md)| Subscription to be created | 

### Return type

[**[Subscription]**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## subscriptionsIdDelete

> subscriptionsIdDelete(id)

Delete a subscription.

### Example

```javascript
import Contribly from 'contribly';

let apiInstance = new Contribly.SubscriptionsApi();
let id = "id_example"; // String | Id of the subscription to delete
apiInstance.subscriptionsIdDelete(id, (error, data, response) => {
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
 **id** | **String**| Id of the subscription to delete | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

