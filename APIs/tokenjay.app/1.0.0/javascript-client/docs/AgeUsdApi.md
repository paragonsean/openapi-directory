# TokenJayApiServices.AgeUsdApi

All URIs are relative to *https://api.tokenjay.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calcSigmaRsvExchange**](AgeUsdApi.md#calcSigmaRsvExchange) | **GET** /sigrsv/exchange/{amount}/info | Calculates SigRSV exchange
[**calcSigmaUsdExchange**](AgeUsdApi.md#calcSigmaUsdExchange) | **GET** /sigusd/exchange/{amount}/info | Calculates SigUSD exchange
[**doSigmaRsvExchange**](AgeUsdApi.md#doSigmaRsvExchange) | **GET** /sigrsv/exchange/ | Builds ErgoPayRequest for SigRSV exchange
[**doSigmaUsdExchange**](AgeUsdApi.md#doSigmaUsdExchange) | **GET** /sigusd/exchange/ | Builds ErgoPayRequest for SigUSD exchange
[**getAgeUsdInfo**](AgeUsdApi.md#getAgeUsdInfo) | **GET** /ageusd/info | Returns state of AgeUSD at this moment
[**getSigmaRsvPrice**](AgeUsdApi.md#getSigmaRsvPrice) | **GET** /sigrsv/price | Lists price and available volume for SigmaRSV
[**getSigmaUsdPrice**](AgeUsdApi.md#getSigmaUsdPrice) | **GET** /sigusd/price | Lists price and available volume for SigmaUSD



## calcSigmaRsvExchange

> AgeUsdExchangeInfo calcSigmaRsvExchange(amount)

Calculates SigRSV exchange

### Example

```javascript
import TokenJayApiServices from 'token_jay_api_services';

let apiInstance = new TokenJayApiServices.AgeUsdApi();
let amount = 789; // Number | 
apiInstance.calcSigmaRsvExchange(amount, (error, data, response) => {
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
 **amount** | **Number**|  | 

### Return type

[**AgeUsdExchangeInfo**](AgeUsdExchangeInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## calcSigmaUsdExchange

> AgeUsdExchangeInfo calcSigmaUsdExchange(amount)

Calculates SigUSD exchange

### Example

```javascript
import TokenJayApiServices from 'token_jay_api_services';

let apiInstance = new TokenJayApiServices.AgeUsdApi();
let amount = 789; // Number | 
apiInstance.calcSigmaUsdExchange(amount, (error, data, response) => {
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
 **amount** | **Number**|  | 

### Return type

[**AgeUsdExchangeInfo**](AgeUsdExchangeInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## doSigmaRsvExchange

> ErgoPayResponse doSigmaRsvExchange(amount, address, opts)

Builds ErgoPayRequest for SigRSV exchange

### Example

```javascript
import TokenJayApiServices from 'token_jay_api_services';

let apiInstance = new TokenJayApiServices.AgeUsdApi();
let amount = 789; // Number | 
let address = "address_example"; // String | 
let opts = {
  'checkRate': 0, // Number | 
  'executionFee': 0 // Number | 
};
apiInstance.doSigmaRsvExchange(amount, address, opts, (error, data, response) => {
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
 **amount** | **Number**|  | 
 **address** | **String**|  | 
 **checkRate** | **Number**|  | [optional] [default to 0]
 **executionFee** | **Number**|  | [optional] [default to 0]

### Return type

[**ErgoPayResponse**](ErgoPayResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## doSigmaUsdExchange

> ErgoPayResponse doSigmaUsdExchange(amount, address, opts)

Builds ErgoPayRequest for SigUSD exchange

### Example

```javascript
import TokenJayApiServices from 'token_jay_api_services';

let apiInstance = new TokenJayApiServices.AgeUsdApi();
let amount = 789; // Number | 
let address = "address_example"; // String | 
let opts = {
  'checkRate': 0, // Number | 
  'executionFee': 0 // Number | 
};
apiInstance.doSigmaUsdExchange(amount, address, opts, (error, data, response) => {
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
 **amount** | **Number**|  | 
 **address** | **String**|  | 
 **checkRate** | **Number**|  | [optional] [default to 0]
 **executionFee** | **Number**|  | [optional] [default to 0]

### Return type

[**ErgoPayResponse**](ErgoPayResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getAgeUsdInfo

> AgeUsdInfo getAgeUsdInfo()

Returns state of AgeUSD at this moment

### Example

```javascript
import TokenJayApiServices from 'token_jay_api_services';

let apiInstance = new TokenJayApiServices.AgeUsdApi();
apiInstance.getAgeUsdInfo((error, data, response) => {
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

[**AgeUsdInfo**](AgeUsdInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getSigmaRsvPrice

> TokenPrice getSigmaRsvPrice()

Lists price and available volume for SigmaRSV

### Example

```javascript
import TokenJayApiServices from 'token_jay_api_services';

let apiInstance = new TokenJayApiServices.AgeUsdApi();
apiInstance.getSigmaRsvPrice((error, data, response) => {
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

[**TokenPrice**](TokenPrice.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getSigmaUsdPrice

> TokenPrice getSigmaUsdPrice()

Lists price and available volume for SigmaUSD

### Example

```javascript
import TokenJayApiServices from 'token_jay_api_services';

let apiInstance = new TokenJayApiServices.AgeUsdApi();
apiInstance.getSigmaUsdPrice((error, data, response) => {
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

[**TokenPrice**](TokenPrice.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

