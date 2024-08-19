# SpectroCoinMerchant.CreateOrderApi

All URIs are relative to *https://spectrocoin.com/api/merchant/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createOrder**](CreateOrderApi.md#createOrder) | **POST** /api/createOrder | Create merchant order



## createOrder

> OrderInformationClass createOrder(apiId, merchantId, payCurrency, receiveCurrency, sign, opts)

Create merchant order

### Example

```javascript
import SpectroCoinMerchant from 'spectro_coin_merchant';

let apiInstance = new SpectroCoinMerchant.CreateOrderApi();
let apiId = 789; // Number | API ID of specific API you have configured on your merchant account
let merchantId = 789; // Number | Merchant ID assigned to your account
let payCurrency = "payCurrency_example"; // String | Currency of pay amount
let receiveCurrency = "receiveCurrency_example"; // String | Currency of receive amount
let sign = "sign_example"; // String | Signature required for signing create order request
let opts = {
  'callbackUrl': "callbackUrl_example", // String | Url of merchant endpoint callback about order status to be returned
  'culture': "culture_example", // String | Merchant customer culture payment window to be presented
  'description': "description_example", // String | Order description. Will be presented for merchant customer at payment window
  'failureUrl': "failureUrl_example", // String | Url of merchant page customer should be redirected after unsuccessful payment
  'orderId': "orderId_example", // String | Custom order ID. Must be unique per API. If not provided it will be generated.
  'payAmount': 3.4, // Number | Pay amount in pay currency of value which should be paid by merchant customer. If not provided receive amount will be used to calculate pay amount
  'payerEmail': "payerEmail_example", // String | Specified payer email.
  'payerName': "payerName_example", // String | Specified payer name.
  'payerSurname': "payerSurname_example", // String | Specified payer surname.
  'receiveAmount': 3.4, // Number | Receive amount in receive currency of value that merchant will be funded after merchant customers payment approval. If not provided pay amount will be used to calculate receive amount
  'successUrl': "successUrl_example" // String | Url of merchant page customer should be redirected after successful payment
};
apiInstance.createOrder(apiId, merchantId, payCurrency, receiveCurrency, sign, opts, (error, data, response) => {
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
 **apiId** | **Number**| API ID of specific API you have configured on your merchant account | 
 **merchantId** | **Number**| Merchant ID assigned to your account | 
 **payCurrency** | **String**| Currency of pay amount | 
 **receiveCurrency** | **String**| Currency of receive amount | 
 **sign** | **String**| Signature required for signing create order request | 
 **callbackUrl** | **String**| Url of merchant endpoint callback about order status to be returned | [optional] 
 **culture** | **String**| Merchant customer culture payment window to be presented | [optional] 
 **description** | **String**| Order description. Will be presented for merchant customer at payment window | [optional] 
 **failureUrl** | **String**| Url of merchant page customer should be redirected after unsuccessful payment | [optional] 
 **orderId** | **String**| Custom order ID. Must be unique per API. If not provided it will be generated. | [optional] 
 **payAmount** | **Number**| Pay amount in pay currency of value which should be paid by merchant customer. If not provided receive amount will be used to calculate pay amount | [optional] 
 **payerEmail** | **String**| Specified payer email. | [optional] 
 **payerName** | **String**| Specified payer name. | [optional] 
 **payerSurname** | **String**| Specified payer surname. | [optional] 
 **receiveAmount** | **Number**| Receive amount in receive currency of value that merchant will be funded after merchant customers payment approval. If not provided pay amount will be used to calculate receive amount | [optional] 
 **successUrl** | **String**| Url of merchant page customer should be redirected after successful payment | [optional] 

### Return type

[**OrderInformationClass**](OrderInformationClass.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

