# TokenJayApiServices.BabelFeeNewOfferControllerApi

All URIs are relative to *https://api.tokenjay.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**doCreateBabelBox**](BabelFeeNewOfferControllerApi.md#doCreateBabelBox) | **POST** /mosaik/babelfee/newoffer/doit | 
[**ergoPayCreateBabelBox**](BabelFeeNewOfferControllerApi.md#ergoPayCreateBabelBox) | **GET** /createbabel/{address} | 
[**getBabelFeeNewOffer**](BabelFeeNewOfferControllerApi.md#getBabelFeeNewOffer) | **GET** /mosaik/babelfee/newoffer | 
[**replaceTokenAmountInputFields**](BabelFeeNewOfferControllerApi.md#replaceTokenAmountInputFields) | **POST** /mosaik/babelfee/newoffer/new-input | 



## doCreateBabelBox

> FetchActionResponse doCreateBabelBox(requestBody)



### Example

```javascript
import TokenJayApiServices from 'token_jay_api_services';

let apiInstance = new TokenJayApiServices.BabelFeeNewOfferControllerApi();
let requestBody = {key: null}; // {String: Object} | 
apiInstance.doCreateBabelBox(requestBody, (error, data, response) => {
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
 **requestBody** | [**{String: Object}**](Object.md)|  | 

### Return type

[**FetchActionResponse**](FetchActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## ergoPayCreateBabelBox

> ErgoPayResponse ergoPayCreateBabelBox(address, tokenId, ergAmount, tokenAmount)



### Example

```javascript
import TokenJayApiServices from 'token_jay_api_services';

let apiInstance = new TokenJayApiServices.BabelFeeNewOfferControllerApi();
let address = "address_example"; // String | 
let tokenId = "tokenId_example"; // String | 
let ergAmount = 789; // Number | 
let tokenAmount = 789; // Number | 
apiInstance.ergoPayCreateBabelBox(address, tokenId, ergAmount, tokenAmount, (error, data, response) => {
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
 **address** | **String**|  | 
 **tokenId** | **String**|  | 
 **ergAmount** | **Number**|  | 
 **tokenAmount** | **Number**|  | 

### Return type

[**ErgoPayResponse**](ErgoPayResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getBabelFeeNewOffer

> MosaikApp getBabelFeeNewOffer()



### Example

```javascript
import TokenJayApiServices from 'token_jay_api_services';

let apiInstance = new TokenJayApiServices.BabelFeeNewOfferControllerApi();
apiInstance.getBabelFeeNewOffer((error, data, response) => {
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

[**MosaikApp**](MosaikApp.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## replaceTokenAmountInputFields

> FetchActionResponse replaceTokenAmountInputFields(requestBody)



### Example

```javascript
import TokenJayApiServices from 'token_jay_api_services';

let apiInstance = new TokenJayApiServices.BabelFeeNewOfferControllerApi();
let requestBody = {key: null}; // {String: Object} | 
apiInstance.replaceTokenAmountInputFields(requestBody, (error, data, response) => {
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
 **requestBody** | [**{String: Object}**](Object.md)|  | 

### Return type

[**FetchActionResponse**](FetchActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*

