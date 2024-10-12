# SubscriptionClient.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscriptionsCancel**](DefaultApi.md#subscriptionsCancel) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Subscription/cancel | 
[**subscriptionsEnable**](DefaultApi.md#subscriptionsEnable) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Subscription/enable | 
[**subscriptionsRename**](DefaultApi.md#subscriptionsRename) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Subscription/rename | 



## subscriptionsCancel

> CanceledSubscriptionId subscriptionsCancel(subscriptionId, apiVersion)



The operation to cancel a subscription

### Example

```javascript
import SubscriptionClient from 'subscription_client';
let defaultClient = SubscriptionClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2019-03-01-preview
apiInstance.subscriptionsCancel(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2019-03-01-preview | 

### Return type

[**CanceledSubscriptionId**](CanceledSubscriptionId.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## subscriptionsEnable

> EnabledSubscriptionId subscriptionsEnable(subscriptionId, apiVersion)



The operation to enable a subscription

### Example

```javascript
import SubscriptionClient from 'subscription_client';
let defaultClient = SubscriptionClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2019-03-01-preview
apiInstance.subscriptionsEnable(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2019-03-01-preview | 

### Return type

[**EnabledSubscriptionId**](EnabledSubscriptionId.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## subscriptionsRename

> RenamedSubscriptionId subscriptionsRename(subscriptionId, apiVersion, body)



The operation to rename a subscription

### Example

```javascript
import SubscriptionClient from 'subscription_client';
let defaultClient = SubscriptionClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2019-03-01-preview
let body = new SubscriptionClient.SubscriptionName(); // SubscriptionName | Subscription Name
apiInstance.subscriptionsRename(subscriptionId, apiVersion, body, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2019-03-01-preview | 
 **body** | [**SubscriptionName**](SubscriptionName.md)| Subscription Name | 

### Return type

[**RenamedSubscriptionId**](RenamedSubscriptionId.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

