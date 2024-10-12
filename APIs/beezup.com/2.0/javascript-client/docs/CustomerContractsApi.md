# BeezUpMerchantApi.CustomerContractsApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createContract**](CustomerContractsApi.md#createContract) | **POST** /v2/user/customer/contracts | Create a new contract
[**deleteNextContract**](CustomerContractsApi.md#deleteNextContract) | **DELETE** /v2/user/customer/contracts/next | Delete your next contract
[**getBillingPeriods**](CustomerContractsApi.md#getBillingPeriods) | **GET** /v2/user/customer/billingPeriods | Get billing periods conditions
[**getContracts**](CustomerContractsApi.md#getContracts) | **GET** /v2/user/customer/contracts | Get contract list
[**getOffer**](CustomerContractsApi.md#getOffer) | **POST** /v2/user/customer/offers | Get offer pricing
[**getStandardOffers**](CustomerContractsApi.md#getStandardOffers) | **GET** /v2/user/customer/offers | Get all standard offers
[**reactivateCurrentContract**](CustomerContractsApi.md#reactivateCurrentContract) | **POST** /v2/user/customer/contracts/current/reenableAutoRenewal | Reactivate your terminated contract.
[**terminateCurrentContract**](CustomerContractsApi.md#terminateCurrentContract) | **POST** /v2/user/customer/contracts/current/disableAutoRenewal | Schedule termination of your current contract at the end of the commitment.



## createContract

> CreateContractResponse createContract(createContract)

Create a new contract

Now you are ready to create your contract. Before that, please ensure that you check the offer with the same request parameterts. /offers 

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CustomerContractsApi();
let createContract = new BeezUpMerchantApi.CreateContract(); // CreateContract | 
apiInstance.createContract(createContract, (error, data, response) => {
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
 **createContract** | [**CreateContract**](CreateContract.md)|  | 

### Return type

[**CreateContractResponse**](CreateContractResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteNextContract

> deleteNextContract()

Delete your next contract

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CustomerContractsApi();
apiInstance.deleteNextContract((error, data, response) => {
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBillingPeriods

> BillingPeriodList getBillingPeriods(opts)

Get billing periods conditions

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CustomerContractsApi();
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
};
apiInstance.getBillingPeriods(opts, (error, data, response) => {
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
 **ifNoneMatch** | **String**| ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  | [optional] 

### Return type

[**BillingPeriodList**](BillingPeriodList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getContracts

> Contracts getContracts(opts)

Get contract list

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CustomerContractsApi();
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
};
apiInstance.getContracts(opts, (error, data, response) => {
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
 **ifNoneMatch** | **String**| ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  | [optional] 

### Return type

[**Contracts**](Contracts.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOffer

> Offer getOffer(offerRequest)

Get offer pricing

Get the offer pricing then you can create your contract with the same request parameters. /v2/user/customer/contracts 

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CustomerContractsApi();
let offerRequest = new BeezUpMerchantApi.OfferRequest(); // OfferRequest | 
apiInstance.getOffer(offerRequest, (error, data, response) => {
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
 **offerRequest** | [**OfferRequest**](OfferRequest.md)|  | 

### Return type

[**Offer**](Offer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getStandardOffers

> StandardOffers getStandardOffers(opts)

Get all standard offers

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CustomerContractsApi();
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
};
apiInstance.getStandardOffers(opts, (error, data, response) => {
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
 **ifNoneMatch** | **String**| ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  | [optional] 

### Return type

[**StandardOffers**](StandardOffers.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reactivateCurrentContract

> reactivateCurrentContract()

Reactivate your terminated contract.

By calling this operation you can re-enable the auto renewal.

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CustomerContractsApi();
apiInstance.reactivateCurrentContract((error, data, response) => {
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## terminateCurrentContract

> terminateCurrentContract(terminateContract)

Schedule termination of your current contract at the end of the commitment.

By default your contract are automatically renew. By calling this operation you can disable the auto renewal.

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CustomerContractsApi();
let terminateContract = new BeezUpMerchantApi.TerminateContract(); // TerminateContract | Indicate the termination reason
apiInstance.terminateCurrentContract(terminateContract, (error, data, response) => {
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
 **terminateContract** | [**TerminateContract**](TerminateContract.md)| Indicate the termination reason | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

