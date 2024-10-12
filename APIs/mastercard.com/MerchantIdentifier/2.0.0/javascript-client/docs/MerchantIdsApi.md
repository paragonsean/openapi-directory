# MerchantIdentifierApiV2.MerchantIdsApi

All URIs are relative to *http://api.mastercard.com/merchant-id/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getMerchantIdentifiers**](MerchantIdsApi.md#getMerchantIdentifiers) | **GET** /merchant-ids | Returns merchant descriptor and locator information based on the criteria you provide.  Information returned includes merchant DBA name, merchant category code (MCC), street address, city, state, postal code, country, and sales channels.



## getMerchantIdentifiers

> MerchantIds getMerchantIdentifiers(opts)

Returns merchant descriptor and locator information based on the criteria you provide.  Information returned includes merchant DBA name, merchant category code (MCC), street address, city, state, postal code, country, and sales channels.

### Example

```javascript
import MerchantIdentifierApiV2 from 'merchant_identifier_api_v2';

let apiInstance = new MerchantIdentifierApiV2.MerchantIdsApi();
let opts = {
  'merchantId': "DOLIUMPTYLTDWELSHPOOLWA", // String | Merchant's name as provided by the issuer found on a cardholder statement. __Important: Please remove all spaces before submitting a API request.__   
  'type': "ExactMatch" // String | Determines how the search is performed.              ExactMatch returns either the one merchant that best fits the description or no results at all.              FuzzyMatch returns 0-20 merchants that are similar to the transaction descriptor.               If Type is not provided, defaults to ExactMatch.              Example: FuzzyMatch
};
apiInstance.getMerchantIdentifiers(opts, (error, data, response) => {
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
 **merchantId** | **String**| Merchant&#39;s name as provided by the issuer found on a cardholder statement. __Important: Please remove all spaces before submitting a API request.__    | [optional] 
 **type** | **String**| Determines how the search is performed.              ExactMatch returns either the one merchant that best fits the description or no results at all.              FuzzyMatch returns 0-20 merchants that are similar to the transaction descriptor.               If Type is not provided, defaults to ExactMatch.              Example: FuzzyMatch | [optional] [default to &#39;ExactMatch&#39;]

### Return type

[**MerchantIds**](MerchantIds.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

