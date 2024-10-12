# BeezUpMerchantApi.OMInvoiceAPIGenerationApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generateBatchOrderInvoice**](OMInvoiceAPIGenerationApi.md#generateBatchOrderInvoice) | **POST** /v2/user/marketplaces/orders/invoices/generate | Generate an Order Invoice batch
[**generateOrderInvoice**](OMInvoiceAPIGenerationApi.md#generateOrderInvoice) | **POST** /v2/user/marketplaces/orders/invoices/{marketplaceTechnicalCode}/{accountId}/{beezUPOrderUUID}/generate | Generate an Order Invoice
[**getOrderInvoicePdf**](OMInvoiceAPIGenerationApi.md#getOrderInvoicePdf) | **POST** /v2/user/marketplaces/orders/invoices/getPdfInvoice | Returns the PDF version of the invoice
[**getOrderInvoicePreview**](OMInvoiceAPIGenerationApi.md#getOrderInvoicePreview) | **POST** /v2/user/marketplaces/orders/invoices/{marketplaceTechnicalCode}/{accountId}/{beezUPOrderUUID}/preview | View a preview an Order Invoice



## generateBatchOrderInvoice

> [GenerateOrderInvoiceResponse] generateBatchOrderInvoice(userName, generateBatchOrderInvoiceRequestItem)

Generate an Order Invoice batch

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.OMInvoiceAPIGenerationApi();
let userName = "userName_example"; // String | Sometimes the user in the e-commerce application is not the same as user associated with the current subscription key. We recommend providing your application's user login.
let generateBatchOrderInvoiceRequestItem = [new BeezUpMerchantApi.GenerateBatchOrderInvoiceRequestItem()]; // [GenerateBatchOrderInvoiceRequestItem] | 
apiInstance.generateBatchOrderInvoice(userName, generateBatchOrderInvoiceRequestItem, (error, data, response) => {
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
 **userName** | **String**| Sometimes the user in the e-commerce application is not the same as user associated with the current subscription key. We recommend providing your application&#39;s user login. | 
 **generateBatchOrderInvoiceRequestItem** | [**[GenerateBatchOrderInvoiceRequestItem]**](GenerateBatchOrderInvoiceRequestItem.md)|  | 

### Return type

[**[GenerateOrderInvoiceResponse]**](GenerateOrderInvoiceResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## generateOrderInvoice

> generateOrderInvoice(marketplaceTechnicalCode, accountId, beezUPOrderUUID, userName, generateOrderInvoiceRequest)

Generate an Order Invoice

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.OMInvoiceAPIGenerationApi();
let marketplaceTechnicalCode = "marketplaceTechnicalCode_example"; // String | The Marketplace Technical Code
let accountId = "accountId_example"; // String | The Account Identifier
let beezUPOrderUUID = "beezUPOrderUUID_example"; // String | The BeezUP Order UUID
let userName = "userName_example"; // String | Sometimes the user in the e-commerce application is not the same as user associated with the current subscription key. We recommend providing your application's user login.
let generateOrderInvoiceRequest = new BeezUpMerchantApi.GenerateOrderInvoiceRequest(); // GenerateOrderInvoiceRequest | 
apiInstance.generateOrderInvoice(marketplaceTechnicalCode, accountId, beezUPOrderUUID, userName, generateOrderInvoiceRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplaceTechnicalCode** | **String**| The Marketplace Technical Code | 
 **accountId** | **String**| The Account Identifier | 
 **beezUPOrderUUID** | **String**| The BeezUP Order UUID | 
 **userName** | **String**| Sometimes the user in the e-commerce application is not the same as user associated with the current subscription key. We recommend providing your application&#39;s user login. | 
 **generateOrderInvoiceRequest** | [**GenerateOrderInvoiceRequest**](GenerateOrderInvoiceRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getOrderInvoicePdf

> File getOrderInvoicePdf(getOrderInvoicePdfFromHtmlInvoiceUrlRequest)

Returns the PDF version of the invoice

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.OMInvoiceAPIGenerationApi();
let getOrderInvoicePdfFromHtmlInvoiceUrlRequest = new BeezUpMerchantApi.GetOrderInvoicePdfFromHtmlInvoiceUrlRequest(); // GetOrderInvoicePdfFromHtmlInvoiceUrlRequest | 
apiInstance.getOrderInvoicePdf(getOrderInvoicePdfFromHtmlInvoiceUrlRequest, (error, data, response) => {
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
 **getOrderInvoicePdfFromHtmlInvoiceUrlRequest** | [**GetOrderInvoicePdfFromHtmlInvoiceUrlRequest**](GetOrderInvoicePdfFromHtmlInvoiceUrlRequest.md)|  | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## getOrderInvoicePreview

> PreviewOrderInvoiceResponse getOrderInvoicePreview(marketplaceTechnicalCode, accountId, beezUPOrderUUID, acceptEncoding, previewOrderInvoiceRequest)

View a preview an Order Invoice

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.OMInvoiceAPIGenerationApi();
let marketplaceTechnicalCode = "marketplaceTechnicalCode_example"; // String | The Marketplace Technical Code
let accountId = "accountId_example"; // String | The Account Identifier
let beezUPOrderUUID = "beezUPOrderUUID_example"; // String | The BeezUP Order UUID
let acceptEncoding = ["null"]; // [String] | Allows the client to indicate wether it accepts a compressed encoding to reduce traffic size
let previewOrderInvoiceRequest = new BeezUpMerchantApi.PreviewOrderInvoiceRequest(); // PreviewOrderInvoiceRequest | 
apiInstance.getOrderInvoicePreview(marketplaceTechnicalCode, accountId, beezUPOrderUUID, acceptEncoding, previewOrderInvoiceRequest, (error, data, response) => {
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
 **marketplaceTechnicalCode** | **String**| The Marketplace Technical Code | 
 **accountId** | **String**| The Account Identifier | 
 **beezUPOrderUUID** | **String**| The BeezUP Order UUID | 
 **acceptEncoding** | [**[String]**](String.md)| Allows the client to indicate wether it accepts a compressed encoding to reduce traffic size | 
 **previewOrderInvoiceRequest** | [**PreviewOrderInvoiceRequest**](PreviewOrderInvoiceRequest.md)|  | 

### Return type

[**PreviewOrderInvoiceResponse**](PreviewOrderInvoiceResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

