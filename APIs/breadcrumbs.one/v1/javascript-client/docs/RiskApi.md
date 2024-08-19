# BreadcrumbsOne.RiskApi

All URIs are relative to *https://api.breadcrumbs.one*

Method | HTTP request | Description
------------- | ------------- | -------------
[**riskAddressGet**](RiskApi.md#riskAddressGet) | **GET** /risk/address | Will check the risk score for single address
[**riskTransactionGet**](RiskApi.md#riskTransactionGet) | **GET** /risk/transaction | Will check the risk score for every addresses in a transaction



## riskAddressGet

> BreadcrumbsAPIModelsAddressRiskExposureResponse riskAddressGet(chain, address, opts)

Will check the risk score for single address

### Example

```javascript
import BreadcrumbsOne from 'breadcrumbs_one';
let defaultClient = BreadcrumbsOne.ApiClient.instance;
// Configure API key authorization: X-API-KEY
let X-API-KEY = defaultClient.authentications['X-API-KEY'];
X-API-KEY.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-API-KEY.apiKeyPrefix = 'Token';

let apiInstance = new BreadcrumbsOne.RiskApi();
let chain = "'ETH'"; // String | Blockchain eg: ETH, BTC, MATIC, RON, SOL, TRX
let address = "address_example"; // String | Blockchain address
let opts = {
  'includeExposure': false // Boolean | If set to `true`, will search the one nearest illicit address (incoming and outgoing) from the specified address
};
apiInstance.riskAddressGet(chain, address, opts, (error, data, response) => {
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
 **chain** | **String**| Blockchain eg: ETH, BTC, MATIC, RON, SOL, TRX | [default to &#39;ETH&#39;]
 **address** | **String**| Blockchain address | 
 **includeExposure** | **Boolean**| If set to &#x60;true&#x60;, will search the one nearest illicit address (incoming and outgoing) from the specified address | [optional] [default to false]

### Return type

[**BreadcrumbsAPIModelsAddressRiskExposureResponse**](BreadcrumbsAPIModelsAddressRiskExposureResponse.md)

### Authorization

[X-API-KEY](../README.md#X-API-KEY)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## riskTransactionGet

> BreadcrumbsAPIModelsTransactionRiskResponse riskTransactionGet(chain, hash)

Will check the risk score for every addresses in a transaction

### Example

```javascript
import BreadcrumbsOne from 'breadcrumbs_one';
let defaultClient = BreadcrumbsOne.ApiClient.instance;
// Configure API key authorization: X-API-KEY
let X-API-KEY = defaultClient.authentications['X-API-KEY'];
X-API-KEY.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-API-KEY.apiKeyPrefix = 'Token';

let apiInstance = new BreadcrumbsOne.RiskApi();
let chain = "'ETH'"; // String | Blockchain eg: ETH, BTC, MATIC, RON, SOL, TRX
let hash = "hash_example"; // String | Blockchain hash
apiInstance.riskTransactionGet(chain, hash, (error, data, response) => {
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
 **chain** | **String**| Blockchain eg: ETH, BTC, MATIC, RON, SOL, TRX | [default to &#39;ETH&#39;]
 **hash** | **String**| Blockchain hash | 

### Return type

[**BreadcrumbsAPIModelsTransactionRiskResponse**](BreadcrumbsAPIModelsTransactionRiskResponse.md)

### Authorization

[X-API-KEY](../README.md#X-API-KEY)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

