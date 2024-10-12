# BarcodeApi.BarcodeApi

All URIs are relative to *http://api.fungenerators.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**barcodeDecodePost**](BarcodeApi.md#barcodeDecodePost) | **POST** /barcode/decode | 
[**barcodeDecodeTypesGet**](BarcodeApi.md#barcodeDecodeTypesGet) | **GET** /barcode/decode/types | 
[**barcodeEncodeGet**](BarcodeApi.md#barcodeEncodeGet) | **GET** /barcode/encode | 
[**barcodeEncodeTypesGet**](BarcodeApi.md#barcodeEncodeTypesGet) | **GET** /barcode/encode/types | 



## barcodeDecodePost

> barcodeDecodePost(barimage)



Decode a Barcode image and return the cotents if successful

### Example

```javascript
import BarcodeApi from 'barcode_api';
let defaultClient = BarcodeApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new BarcodeApi.BarcodeApi();
let barimage = "/path/to/file"; // File | Barcode image to decode and get the content value
apiInstance.barcodeDecodePost(barimage, (error, data, response) => {
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
 **barimage** | **File**| Barcode image to decode and get the content value | 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## barcodeDecodeTypesGet

> barcodeDecodeTypesGet()



Get the supported barcode types for the decoding process.

### Example

```javascript
import BarcodeApi from 'barcode_api';
let defaultClient = BarcodeApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new BarcodeApi.BarcodeApi();
apiInstance.barcodeDecodeTypesGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## barcodeEncodeGet

> barcodeEncodeGet(number, opts)



Get a Bar Code image for the given barcode number

### Example

```javascript
import BarcodeApi from 'barcode_api';
let defaultClient = BarcodeApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new BarcodeApi.BarcodeApi();
let number = "number_example"; // String | Barcode number
let opts = {
  'barcodeformat': "barcodeformat_example", // String | Barcode format default C39. Valid values are the keys to those returned from /barcode/encode/types.
  'outputformat': "outputformat_example", // String | Output image format. Must be one of png/html/jpg/svg
  'widthfactor': 56, // Number | Width factor of the image
  'totalheight': 56 // Number | Total height of the image
};
apiInstance.barcodeEncodeGet(number, opts, (error, data, response) => {
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
 **number** | **String**| Barcode number | 
 **barcodeformat** | **String**| Barcode format default C39. Valid values are the keys to those returned from /barcode/encode/types. | [optional] 
 **outputformat** | **String**| Output image format. Must be one of png/html/jpg/svg | [optional] 
 **widthfactor** | **Number**| Width factor of the image | [optional] 
 **totalheight** | **Number**| Total height of the image | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## barcodeEncodeTypesGet

> barcodeEncodeTypesGet()



Get the supported barcode types for encoding / image generation.

### Example

```javascript
import BarcodeApi from 'barcode_api';
let defaultClient = BarcodeApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new BarcodeApi.BarcodeApi();
apiInstance.barcodeEncodeTypesGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

