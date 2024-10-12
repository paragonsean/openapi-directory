# Labs64NetLicensingResTfulApiTestCenter.PaymentMethodApi

All URIs are relative to *https://go.netlicensing.io/core/v2/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPaymentMethod**](PaymentMethodApi.md#getPaymentMethod) | **GET** /paymentmethod/{paymentMethodNumber} | Get Payment Method
[**listPaymentMethods**](PaymentMethodApi.md#listPaymentMethods) | **GET** /paymentmethod | List Payment Methods
[**updatePaymentMethod**](PaymentMethodApi.md#updatePaymentMethod) | **POST** /paymentmethod/{paymentMethodNumber} | Update Payment Method



## getPaymentMethod

> Netlicensing getPaymentMethod(paymentMethodNumber)

Get Payment Method

Return a Payment Method info by &#39;paymentMethodNumber&#39;

### Example

```javascript
import Labs64NetLicensingResTfulApiTestCenter from 'labs64_net_licensing_res_tful_api_test_center';
let defaultClient = Labs64NetLicensingResTfulApiTestCenter.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Labs64NetLicensingResTfulApiTestCenter.PaymentMethodApi();
let paymentMethodNumber = "paymentMethodNumber_example"; // String | Payment method number
apiInstance.getPaymentMethod(paymentMethodNumber, (error, data, response) => {
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
 **paymentMethodNumber** | **String**| Payment method number | 

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## listPaymentMethods

> [Netlicensing] listPaymentMethods()

List Payment Methods

Return a list of all Payment Methods for the current Vendor

### Example

```javascript
import Labs64NetLicensingResTfulApiTestCenter from 'labs64_net_licensing_res_tful_api_test_center';
let defaultClient = Labs64NetLicensingResTfulApiTestCenter.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Labs64NetLicensingResTfulApiTestCenter.PaymentMethodApi();
apiInstance.listPaymentMethods((error, data, response) => {
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

[**[Netlicensing]**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## updatePaymentMethod

> Netlicensing updatePaymentMethod(paymentMethodNumber, opts)

Update Payment Method

Sets the provided properties to a Payment Method. Return an updated Payment Method

### Example

```javascript
import Labs64NetLicensingResTfulApiTestCenter from 'labs64_net_licensing_res_tful_api_test_center';
let defaultClient = Labs64NetLicensingResTfulApiTestCenter.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Labs64NetLicensingResTfulApiTestCenter.PaymentMethodApi();
let paymentMethodNumber = "paymentMethodNumber_example"; // String | Payment method number
let opts = {
  'active': true, // Boolean | If set to 'false', the Payment Method is disabled.
  'paypalSubject': "paypalSubject_example" // String | The e-mail address of the PayPal account for which you are making the API calls.
};
apiInstance.updatePaymentMethod(paymentMethodNumber, opts, (error, data, response) => {
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
 **paymentMethodNumber** | **String**| Payment method number | 
 **active** | **Boolean**| If set to &#39;false&#39;, the Payment Method is disabled. | [optional] 
 **paypalSubject** | **String**| The e-mail address of the PayPal account for which you are making the API calls. | [optional] 

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml

