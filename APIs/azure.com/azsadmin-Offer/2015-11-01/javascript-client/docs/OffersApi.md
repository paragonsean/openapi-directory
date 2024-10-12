# SubscriptionClient.OffersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**offersList**](OffersApi.md#offersList) | **GET** /offers | 



## offersList

> OfferList offersList(apiVersion)



Get the list of public offers for the root provider.

### Example

```javascript
import SubscriptionClient from 'subscription_client';
let defaultClient = SubscriptionClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionClient.OffersApi();
let apiVersion = "'2015-11-01'"; // String | Client Api Version.
apiInstance.offersList(apiVersion, (error, data, response) => {
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

[**OfferList**](OfferList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

