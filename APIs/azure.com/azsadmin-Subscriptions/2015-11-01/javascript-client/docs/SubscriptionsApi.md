# SubscriptionClient.SubscriptionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscriptionsCreateOrUpdate**](SubscriptionsApi.md#subscriptionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId} | 
[**subscriptionsDelete**](SubscriptionsApi.md#subscriptionsDelete) | **DELETE** /subscriptions/{subscriptionId} | 
[**subscriptionsGet**](SubscriptionsApi.md#subscriptionsGet) | **GET** /subscriptions/{subscriptionId} | 
[**subscriptionsList**](SubscriptionsApi.md#subscriptionsList) | **GET** /subscriptions | 



## subscriptionsCreateOrUpdate

> Subscription subscriptionsCreateOrUpdate(subscriptionId, apiVersion, newSubscription)



Create or updates a subscription.

### Example

```javascript
import SubscriptionClient from 'subscription_client';
let defaultClient = SubscriptionClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionClient.SubscriptionsApi();
let subscriptionId = "subscriptionId_example"; // String | Id of the subscription.
let apiVersion = "'2015-11-01'"; // String | Client Api Version.
let newSubscription = new SubscriptionClient.Subscription(); // Subscription | Subscription parameter.
apiInstance.subscriptionsCreateOrUpdate(subscriptionId, apiVersion, newSubscription, (error, data, response) => {
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
 **subscriptionId** | **String**| Id of the subscription. | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2015-11-01&#39;]
 **newSubscription** | [**Subscription**](Subscription.md)| Subscription parameter. | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## subscriptionsDelete

> subscriptionsDelete(subscriptionId, apiVersion)



Delete the specified subscription.

### Example

```javascript
import SubscriptionClient from 'subscription_client';
let defaultClient = SubscriptionClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionClient.SubscriptionsApi();
let subscriptionId = "subscriptionId_example"; // String | Id of the subscription.
let apiVersion = "'2015-11-01'"; // String | Client Api Version.
apiInstance.subscriptionsDelete(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Id of the subscription. | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2015-11-01&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## subscriptionsGet

> Subscription subscriptionsGet(subscriptionId, apiVersion)



Gets details about particular subscription.

### Example

```javascript
import SubscriptionClient from 'subscription_client';
let defaultClient = SubscriptionClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionClient.SubscriptionsApi();
let subscriptionId = "subscriptionId_example"; // String | Id of the subscription.
let apiVersion = "'2015-11-01'"; // String | Client Api Version.
apiInstance.subscriptionsGet(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Id of the subscription. | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2015-11-01&#39;]

### Return type

[**Subscription**](Subscription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## subscriptionsList

> SubscriptionList subscriptionsList(apiVersion)



Get the list of subscriptions.

### Example

```javascript
import SubscriptionClient from 'subscription_client';
let defaultClient = SubscriptionClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionClient.SubscriptionsApi();
let apiVersion = "'2015-11-01'"; // String | Client Api Version.
apiInstance.subscriptionsList(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2015-11-01&#39;]

### Return type

[**SubscriptionList**](SubscriptionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

