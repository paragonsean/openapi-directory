# SubscriptionsManagementClient.DelegatedProvidersApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delegatedProvidersGet**](DelegatedProvidersApi.md#delegatedProvidersGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Subscriptions.Admin/delegatedProviders/{delegatedProvider} | 
[**delegatedProvidersList**](DelegatedProvidersApi.md#delegatedProvidersList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Subscriptions.Admin/delegatedProviders | 



## delegatedProvidersGet

> DelegatedProvidersList200ResponseValueInner delegatedProvidersGet(subscriptionId, delegatedProvider, apiVersion)



Get the specified delegated provider.

### Example

```javascript
import SubscriptionsManagementClient from 'subscriptions_management_client';
let defaultClient = SubscriptionsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionsManagementClient.DelegatedProvidersApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
let delegatedProvider = "delegatedProvider_example"; // String | DelegatedProvider identifier.
let apiVersion = "'2015-11-01'"; // String | Client Api Version.
apiInstance.delegatedProvidersGet(subscriptionId, delegatedProvider, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | 
 **delegatedProvider** | **String**| DelegatedProvider identifier. | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2015-11-01&#39;]

### Return type

[**DelegatedProvidersList200ResponseValueInner**](DelegatedProvidersList200ResponseValueInner.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## delegatedProvidersList

> DelegatedProvidersList200Response delegatedProvidersList(subscriptionId, apiVersion)



Get the list of delegatedProviders.

### Example

```javascript
import SubscriptionsManagementClient from 'subscriptions_management_client';
let defaultClient = SubscriptionsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionsManagementClient.DelegatedProvidersApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
let apiVersion = "'2015-11-01'"; // String | Client Api Version.
apiInstance.delegatedProvidersList(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2015-11-01&#39;]

### Return type

[**DelegatedProvidersList200Response**](DelegatedProvidersList200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

