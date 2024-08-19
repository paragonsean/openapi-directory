# OpenChannelMarketApi.CustomGatewayProcessPaymentsAndRefundsApi

All URIs are relative to *https://market.openchannel.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customGatewayPaymentOwnershipIdPost**](CustomGatewayProcessPaymentsAndRefundsApi.md#customGatewayPaymentOwnershipIdPost) | **POST** /custom-gateway/payment/{ownershipId} | Adds a payment for an app on behalf of a user
[**customGatewayRefundOwnershipIdPost**](CustomGatewayProcessPaymentsAndRefundsApi.md#customGatewayRefundOwnershipIdPost) | **POST** /custom-gateway/refund/{ownershipId} | Fully or partially refund payment for an app on behalf of a user



## customGatewayPaymentOwnershipIdPost

> Transaction customGatewayPaymentOwnershipIdPost(ownershipId, amount, opts)

Adds a payment for an app on behalf of a user

- Results are returned for the market provided within the basic authentication credentials  - Payments must be enabled and &#39;Custom&#39; must be selected as the gateway in order to use this API endpoint 

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.CustomGatewayProcessPaymentsAndRefundsApi();
let ownershipId = "ownershipId_example"; // String | The id of the ownership record involved in this transaction
let amount = 56; // Number | The total amount paid in cents
let opts = {
  'date': 789, // Number | The date (in milliseconds) of when this payment was made
  'feeAmount': 56, // Number | The fee (in cents) paid to a payment processors or third parties to process this payment. Default is 0.
  'marketplaceAmount': 56, // Number | The amount (in cents) paid to the marketplace owner as a commission for the purchase of this app. Defaults based on the commission amount configured for this marketplace.
  'developerAmount': 56, // Number | The amount (in cents) paid to the owner of the app. Defaults based on the commission amount configured for this marketplace.
  'customData': "customData_example" // String | A custom JSON object to attach to this transaction
};
apiInstance.customGatewayPaymentOwnershipIdPost(ownershipId, amount, opts, (error, data, response) => {
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
 **ownershipId** | **String**| The id of the ownership record involved in this transaction | 
 **amount** | **Number**| The total amount paid in cents | 
 **date** | **Number**| The date (in milliseconds) of when this payment was made | [optional] 
 **feeAmount** | **Number**| The fee (in cents) paid to a payment processors or third parties to process this payment. Default is 0. | [optional] 
 **marketplaceAmount** | **Number**| The amount (in cents) paid to the marketplace owner as a commission for the purchase of this app. Defaults based on the commission amount configured for this marketplace. | [optional] 
 **developerAmount** | **Number**| The amount (in cents) paid to the owner of the app. Defaults based on the commission amount configured for this marketplace. | [optional] 
 **customData** | **String**| A custom JSON object to attach to this transaction | [optional] 

### Return type

[**Transaction**](Transaction.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## customGatewayRefundOwnershipIdPost

> Transaction customGatewayRefundOwnershipIdPost(ownershipId, amount, opts)

Fully or partially refund payment for an app on behalf of a user

- Results are returned for the market provided within the basic authentication credentials - Payments must be enabled and &#39;Custom&#39; must be selected as the gateway in order to use this API endpoint 

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.CustomGatewayProcessPaymentsAndRefundsApi();
let ownershipId = "ownershipId_example"; // String | The id of the ownership record involved in this transaction
let amount = 56; // Number | The total amount refunded in cents
let opts = {
  'date': 789, // Number | The date (in milliseconds) of when this refund was made
  'feeAmount': 56, // Number | The fee (in cents) recovered from a payment processor or third party to process this payment. The default value is 0
  'marketplaceAmount': 56, // Number | The amount (in cents) recovered from the marketplace owner as a commission refund for the purchase of this app
  'developerAmount': 56, // Number | The amount (in cents) recovered from the owner of the app
  'customData': "customData_example" // String | A custom JSON object to attach to this transaction
};
apiInstance.customGatewayRefundOwnershipIdPost(ownershipId, amount, opts, (error, data, response) => {
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
 **ownershipId** | **String**| The id of the ownership record involved in this transaction | 
 **amount** | **Number**| The total amount refunded in cents | 
 **date** | **Number**| The date (in milliseconds) of when this refund was made | [optional] 
 **feeAmount** | **Number**| The fee (in cents) recovered from a payment processor or third party to process this payment. The default value is 0 | [optional] 
 **marketplaceAmount** | **Number**| The amount (in cents) recovered from the marketplace owner as a commission refund for the purchase of this app | [optional] 
 **developerAmount** | **Number**| The amount (in cents) recovered from the owner of the app | [optional] 
 **customData** | **String**| A custom JSON object to attach to this transaction | [optional] 

### Return type

[**Transaction**](Transaction.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

