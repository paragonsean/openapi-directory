# SubscriptionClient.DelegatedProviderOffersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delegatedProviderOffersGet**](DelegatedProviderOffersApi.md#delegatedProviderOffersGet) | **GET** /delegatedProviders/{delegatedProviderId}/offers/{offerName} | 
[**delegatedProviderOffersList**](DelegatedProviderOffersApi.md#delegatedProviderOffersList) | **GET** /delegatedProviders/{delegatedProviderId}/offers | 



## delegatedProviderOffersGet

> Offer delegatedProviderOffersGet(delegatedProviderId, offerName, apiVersion)



Get the specified offer for the delegated provider.

### Example

```javascript
import SubscriptionClient from 'subscription_client';
let defaultClient = SubscriptionClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionClient.DelegatedProviderOffersApi();
let delegatedProviderId = "delegatedProviderId_example"; // String | Id of the delegated provider.
let offerName = "offerName_example"; // String | Name of the offer.
let apiVersion = "'2015-11-01'"; // String | Client Api Version.
apiInstance.delegatedProviderOffersGet(delegatedProviderId, offerName, apiVersion, (error, data, response) => {
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
 **delegatedProviderId** | **String**| Id of the delegated provider. | 
 **offerName** | **String**| Name of the offer. | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2015-11-01&#39;]

### Return type

[**Offer**](Offer.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## delegatedProviderOffersList

> OfferList delegatedProviderOffersList(delegatedProviderId, apiVersion)



Get the list of offers for the specified delegated provider.

### Example

```javascript
import SubscriptionClient from 'subscription_client';
let defaultClient = SubscriptionClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionClient.DelegatedProviderOffersApi();
let delegatedProviderId = "delegatedProviderId_example"; // String | Id of the delegated provider.
let apiVersion = "'2015-11-01'"; // String | Client Api Version.
apiInstance.delegatedProviderOffersList(delegatedProviderId, apiVersion, (error, data, response) => {
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
 **delegatedProviderId** | **String**| Id of the delegated provider. | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2015-11-01&#39;]

### Return type

[**OfferList**](OfferList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

