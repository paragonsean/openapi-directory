# PayoneLinkApi.LinkManagementApi

All URIs are relative to *https://onelink.pay1.de/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createPaymentLink**](LinkManagementApi.md#createPaymentLink) | **POST** /v1/payment-links | Create a payment link.
[**getPaymentLink**](LinkManagementApi.md#getPaymentLink) | **GET** /v1/payment-links/{linkId} | Get payment link by id.
[**getPaymentLinks**](LinkManagementApi.md#getPaymentLinks) | **GET** /v1/payment-links | List all payment links.
[**updatePaymentLink**](LinkManagementApi.md#updatePaymentLink) | **PUT** /v1/payment-links/{linkId} | Update a payment link.



## createPaymentLink

> LinkResponse createPaymentLink(opts)

Create a payment link.

### Example

```javascript
import PayoneLinkApi from 'payone_link_api';
let defaultClient = PayoneLinkApi.ApiClient.instance;

let apiInstance = new PayoneLinkApi.LinkManagementApi();
let opts = {
  'linkCreateRequest': new PayoneLinkApi.LinkCreateRequest() // LinkCreateRequest | 
};
apiInstance.createPaymentLink(opts, (error, data, response) => {
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
 **linkCreateRequest** | [**LinkCreateRequest**](LinkCreateRequest.md)|  | [optional] 

### Return type

[**LinkResponse**](LinkResponse.md)

### Authorization

[createAuth](../README.md#createAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getPaymentLink

> LinkResponse getPaymentLink(linkId)

Get payment link by id.

### Example

```javascript
import PayoneLinkApi from 'payone_link_api';
let defaultClient = PayoneLinkApi.ApiClient.instance;

let apiInstance = new PayoneLinkApi.LinkManagementApi();
let linkId = "linkId_example"; // String | 
apiInstance.getPaymentLink(linkId, (error, data, response) => {
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
 **linkId** | **String**|  | 

### Return type

[**LinkResponse**](LinkResponse.md)

### Authorization

[getSingleAuth](../README.md#getSingleAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPaymentLinks

> PageLinkResponse getPaymentLinks(merchantId, accountId, portalId, mode, opts)

List all payment links.

### Example

```javascript
import PayoneLinkApi from 'payone_link_api';
let defaultClient = PayoneLinkApi.ApiClient.instance;

let apiInstance = new PayoneLinkApi.LinkManagementApi();
let merchantId = "merchantId_example"; // String | 
let accountId = "accountId_example"; // String | 
let portalId = "portalId_example"; // String | 
let mode = "mode_example"; // String | 
let opts = {
  'page': 0, // Number | 
  'limit': 25 // Number | 
};
apiInstance.getPaymentLinks(merchantId, accountId, portalId, mode, opts, (error, data, response) => {
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
 **merchantId** | **String**|  | 
 **accountId** | **String**|  | 
 **portalId** | **String**|  | 
 **mode** | **String**|  | 
 **page** | **Number**|  | [optional] [default to 0]
 **limit** | **Number**|  | [optional] [default to 25]

### Return type

[**PageLinkResponse**](PageLinkResponse.md)

### Authorization

[getMultipleAuth](../README.md#getMultipleAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updatePaymentLink

> LinkResponse updatePaymentLink(linkId, opts)

Update a payment link.

### Example

```javascript
import PayoneLinkApi from 'payone_link_api';
let defaultClient = PayoneLinkApi.ApiClient.instance;

let apiInstance = new PayoneLinkApi.LinkManagementApi();
let linkId = "linkId_example"; // String | 
let opts = {
  'linkCreateRequest': new PayoneLinkApi.LinkCreateRequest() // LinkCreateRequest | 
};
apiInstance.updatePaymentLink(linkId, opts, (error, data, response) => {
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
 **linkId** | **String**|  | 
 **linkCreateRequest** | [**LinkCreateRequest**](LinkCreateRequest.md)|  | [optional] 

### Return type

[**LinkResponse**](LinkResponse.md)

### Authorization

[createAuth](../README.md#createAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

