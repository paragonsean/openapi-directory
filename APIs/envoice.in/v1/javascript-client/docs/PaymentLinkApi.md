# ApiV100.PaymentLinkApi

All URIs are relative to *https://www.envoice.in*

Method | HTTP request | Description
------------- | ------------- | -------------
[**paymentLinkApiAll**](PaymentLinkApi.md#paymentLinkApiAll) | **GET** /api/paymentlink/all | Create a payment link
[**paymentLinkApiDelete**](PaymentLinkApi.md#paymentLinkApiDelete) | **POST** /api/paymentlink/delete | Delete an existing payment link
[**paymentLinkApiNew**](PaymentLinkApi.md#paymentLinkApiNew) | **POST** /api/paymentlink/new | Create a payment link
[**paymentLinkApiUri**](PaymentLinkApi.md#paymentLinkApiUri) | **GET** /api/paymentlink/uri | Return the unique url to the client&#39;s payment link



## paymentLinkApiAll

> ListResultPaymentLink paymentLinkApiAll(xAuthKey, xAuthSecret, opts)

Create a payment link

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.PaymentLinkApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
let opts = {
  'queryOptionsPage': 56, // Number | 
  'queryOptionsPageSize': 56 // Number | 
};
apiInstance.paymentLinkApiAll(xAuthKey, xAuthSecret, opts, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]
 **queryOptionsPage** | **Number**|  | [optional] 
 **queryOptionsPageSize** | **Number**|  | [optional] 

### Return type

[**ListResultPaymentLink**](ListResultPaymentLink.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## paymentLinkApiDelete

> Number paymentLinkApiDelete(xAuthKey, xAuthSecret, paymentLink)

Delete an existing payment link

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.PaymentLinkApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
let paymentLink = new ApiV100.PaymentLink(); // PaymentLink | 
apiInstance.paymentLinkApiDelete(xAuthKey, xAuthSecret, paymentLink, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]
 **paymentLink** | [**PaymentLink**](PaymentLink.md)|  | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## paymentLinkApiNew

> Number paymentLinkApiNew(xAuthKey, xAuthSecret, paymentLink)

Create a payment link

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.PaymentLinkApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
let paymentLink = new ApiV100.PaymentLink(); // PaymentLink | 
apiInstance.paymentLinkApiNew(xAuthKey, xAuthSecret, paymentLink, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]
 **paymentLink** | [**PaymentLink**](PaymentLink.md)|  | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## paymentLinkApiUri

> PaymentLinkUriApiModel paymentLinkApiUri(id, xAuthKey, xAuthSecret)

Return the unique url to the client&#39;s payment link

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.PaymentLinkApi();
let id = 56; // Number | 
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
apiInstance.paymentLinkApiUri(id, xAuthKey, xAuthSecret, (error, data, response) => {
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
 **id** | **Number**|  | 
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]

### Return type

[**PaymentLinkUriApiModel**](PaymentLinkUriApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/html, text/json, text/xml

