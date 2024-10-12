# LocationsApi.MerchantCountriesApi

All URIs are relative to *https://api.mastercard.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**merchantsV1CountryGet**](MerchantCountriesApi.md#merchantsV1CountryGet) | **GET** /merchants/v1/country | Returns countries that have Merchants offering the following services: accept contactless-enabled cards and devices, allow customers to add money to an eligible MasterCard or Maestro prepaid card, issue MasterCard Prepaid Travel cards, offer cash at checkout when paying with a Debit MasterCard or Maestro Card. 



## merchantsV1CountryGet

> CountriesResponse merchantsV1CountryGet(details)

Returns countries that have Merchants offering the following services: accept contactless-enabled cards and devices, allow customers to add money to an eligible MasterCard or Maestro prepaid card, issue MasterCard Prepaid Travel cards, offer cash at checkout when paying with a Debit MasterCard or Maestro Card. 

Returns countries that have Merchants offering the following services: accept contactless-enabled cards and devices, allow customers to add money to an eligible MasterCard or Maestro prepaid card, issue MasterCard Prepaid Travel cards, offer cash at checkout when paying with a Debit MasterCard or Maestro Card. 

### Example

```javascript
import LocationsApi from 'locations_api';

let apiInstance = new LocationsApi.MerchantCountriesApi();
let details = "acceptance.paypass"; // String | This is the type of merchant location. Options  \"acceptance.paypass\" \"topup.repower\"  \"products.prepaidtravelcard\"  and \"offers.easysavings\"
apiInstance.merchantsV1CountryGet(details, (error, data, response) => {
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
 **details** | **String**| This is the type of merchant location. Options  \&quot;acceptance.paypass\&quot; \&quot;topup.repower\&quot;  \&quot;products.prepaidtravelcard\&quot;  and \&quot;offers.easysavings\&quot; | 

### Return type

[**CountriesResponse**](CountriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

