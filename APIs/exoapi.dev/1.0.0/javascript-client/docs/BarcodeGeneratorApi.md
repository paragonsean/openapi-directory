# ExoApi.BarcodeGeneratorApi

All URIs are relative to *https://api.exoapi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**barcodeGeneratorPost**](BarcodeGeneratorApi.md#barcodeGeneratorPost) | **POST** /barcode-generator | 



## barcodeGeneratorPost

> File barcodeGeneratorPost(barcodeGeneratorPostRequest)



Generate high quality QR code &amp; barcode images in a matter of seconds

### Example

```javascript
import ExoApi from 'exo_api';
let defaultClient = ExoApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ExoApi.BarcodeGeneratorApi();
let barcodeGeneratorPostRequest = new ExoApi.BarcodeGeneratorPostRequest(); // BarcodeGeneratorPostRequest | 
apiInstance.barcodeGeneratorPost(barcodeGeneratorPostRequest, (error, data, response) => {
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
 **barcodeGeneratorPostRequest** | [**BarcodeGeneratorPostRequest**](BarcodeGeneratorPostRequest.md)|  | 

### Return type

**File**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: image/png, image/svg+xml, application/json

