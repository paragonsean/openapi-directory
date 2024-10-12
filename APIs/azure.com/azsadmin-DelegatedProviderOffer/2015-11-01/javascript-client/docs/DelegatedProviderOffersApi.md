# SubscriptionsManagementClient.DelegatedProviderOffersApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delegatedProviderOffersGet**](DelegatedProviderOffersApi.md#delegatedProviderOffersGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Subscriptions.Admin/delegatedProviders/{delegatedProviderSubscriptionId}/offers/{offer} | 
[**delegatedProviderOffersList**](DelegatedProviderOffersApi.md#delegatedProviderOffersList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Subscriptions.Admin/delegatedProviders/{delegatedProviderSubscriptionId}/offers | 



## delegatedProviderOffersGet

> DelegatedProviderOffer delegatedProviderOffersGet(subscriptionId, delegatedProviderSubscriptionId, offer, apiVersion)



Get the specified delegated provider offer.

### Example

```javascript
import SubscriptionsManagementClient from 'subscriptions_management_client';
let defaultClient = SubscriptionsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionsManagementClient.DelegatedProviderOffersApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
let delegatedProviderSubscriptionId = "delegatedProviderSubscriptionId_example"; // String | Delegated provider subscription identifier.
let offer = "offer_example"; // String | Name of an offer.
let apiVersion = "'2015-11-01'"; // String | Client Api Version.
apiInstance.delegatedProviderOffersGet(subscriptionId, delegatedProviderSubscriptionId, offer, apiVersion, (error, data, response) => {
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
 **delegatedProviderSubscriptionId** | **String**| Delegated provider subscription identifier. | 
 **offer** | **String**| Name of an offer. | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2015-11-01&#39;]

### Return type

[**DelegatedProviderOffer**](DelegatedProviderOffer.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## delegatedProviderOffersList

> DelegatedProviderOfferList delegatedProviderOffersList(subscriptionId, delegatedProviderSubscriptionId, apiVersion)



Get the list of delegated provider offers.

### Example

```javascript
import SubscriptionsManagementClient from 'subscriptions_management_client';
let defaultClient = SubscriptionsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionsManagementClient.DelegatedProviderOffersApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
let delegatedProviderSubscriptionId = "delegatedProviderSubscriptionId_example"; // String | Delegated provider subscription identifier.
let apiVersion = "'2015-11-01'"; // String | Client Api Version.
apiInstance.delegatedProviderOffersList(subscriptionId, delegatedProviderSubscriptionId, apiVersion, (error, data, response) => {
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
 **delegatedProviderSubscriptionId** | **String**| Delegated provider subscription identifier. | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2015-11-01&#39;]

### Return type

[**DelegatedProviderOfferList**](DelegatedProviderOfferList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

