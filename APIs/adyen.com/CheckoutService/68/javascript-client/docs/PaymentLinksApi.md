# AdyenCheckoutApi.PaymentLinksApi

All URIs are relative to *https://checkout-test.adyen.com/v68*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPaymentLinksLinkId**](PaymentLinksApi.md#getPaymentLinksLinkId) | **GET** /paymentLinks/{linkId} | Get a payment link
[**patchPaymentLinksLinkId**](PaymentLinksApi.md#patchPaymentLinksLinkId) | **PATCH** /paymentLinks/{linkId} | Update the status of a payment link
[**postPaymentLinks**](PaymentLinksApi.md#postPaymentLinks) | **POST** /paymentLinks | Create a payment link



## getPaymentLinksLinkId

> PaymentLinkResponse getPaymentLinksLinkId(linkId)

Get a payment link

Retrieves the payment link details using the payment link &#x60;id&#x60;.

### Example

```javascript
import AdyenCheckoutApi from 'adyen_checkout_api';
let defaultClient = AdyenCheckoutApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenCheckoutApi.PaymentLinksApi();
let linkId = "linkId_example"; // String | Unique identifier of the payment link.
apiInstance.getPaymentLinksLinkId(linkId, (error, data, response) => {
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
 **linkId** | **String**| Unique identifier of the payment link. | 

### Return type

[**PaymentLinkResponse**](PaymentLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchPaymentLinksLinkId

> PaymentLinkResponse patchPaymentLinksLinkId(linkId, opts)

Update the status of a payment link

Updates the status of a payment link. Use this endpoint to [force the expiry of a payment link](https://docs.adyen.com/online-payments/pay-by-link#update-payment-link-status).

### Example

```javascript
import AdyenCheckoutApi from 'adyen_checkout_api';
let defaultClient = AdyenCheckoutApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenCheckoutApi.PaymentLinksApi();
let linkId = "linkId_example"; // String | Unique identifier of the payment link.
let opts = {
  'updatePaymentLinkRequest': new AdyenCheckoutApi.UpdatePaymentLinkRequest() // UpdatePaymentLinkRequest | 
};
apiInstance.patchPaymentLinksLinkId(linkId, opts, (error, data, response) => {
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
 **linkId** | **String**| Unique identifier of the payment link. | 
 **updatePaymentLinkRequest** | [**UpdatePaymentLinkRequest**](UpdatePaymentLinkRequest.md)|  | [optional] 

### Return type

[**PaymentLinkResponse**](PaymentLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postPaymentLinks

> PaymentLinkResponse postPaymentLinks(opts)

Create a payment link

Creates a payment link to our hosted payment form where shoppers can pay. The list of payment methods presented to the shopper depends on the &#x60;currency&#x60; and &#x60;country&#x60; parameters sent in the request.  For more information, refer to [Pay by Link documentation](https://docs.adyen.com/online-payments/pay-by-link#create-payment-links-through-api).

### Example

```javascript
import AdyenCheckoutApi from 'adyen_checkout_api';
let defaultClient = AdyenCheckoutApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenCheckoutApi.PaymentLinksApi();
let opts = {
  'idempotencyKey': "37ca9c97-d1d1-4c62-89e8-706891a563ed", // String | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
  'paymentLinkRequest': new AdyenCheckoutApi.PaymentLinkRequest() // PaymentLinkRequest | 
};
apiInstance.postPaymentLinks(opts, (error, data, response) => {
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
 **idempotencyKey** | **String**| A unique identifier for the message with a maximum of 64 characters (we recommend a UUID). | [optional] 
 **paymentLinkRequest** | [**PaymentLinkRequest**](PaymentLinkRequest.md)|  | [optional] 

### Return type

[**PaymentLinkResponse**](PaymentLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

