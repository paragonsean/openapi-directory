# LocationsApi.MerchantCountrySubdivisionsApi

All URIs are relative to *https://api.mastercard.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**merchantsV1CountrysubdivisionGet**](MerchantCountrySubdivisionsApi.md#merchantsV1CountrysubdivisionGet) | **GET** /merchants/v1/countrysubdivision | Returns country subdivisions that have Merchants offering the following services: accept contactless-enabled cards and devices, allow customers to add money to an eligible MasterCard or Maestro prepaid card, issue MasterCard Prepaid Travel cards, offer cash at checkout when paying with a Debit MasterCard or Maestro Card. A country subdivision is a segment within a country (ex  state or province).  Please note country subdivisions are only available for the US and Canada. 



## merchantsV1CountrysubdivisionGet

> CountrySubdivisionResponse merchantsV1CountrysubdivisionGet(details, country)

Returns country subdivisions that have Merchants offering the following services: accept contactless-enabled cards and devices, allow customers to add money to an eligible MasterCard or Maestro prepaid card, issue MasterCard Prepaid Travel cards, offer cash at checkout when paying with a Debit MasterCard or Maestro Card. A country subdivision is a segment within a country (ex  state or province).  Please note country subdivisions are only available for the US and Canada. 

Returns country subdivisions that have Merchants offering the following services: accept contactless-enabled cards and devices, allow customers to add money to an eligible MasterCard or Maestro prepaid card, issue MasterCard Prepaid Travel cards, offer cash at checkout when paying with a Debit MasterCard or Maestro Card. A country subdivision is a segment within a country (ex  state or province).  Please note country subdivisions are only available for the US and Canada. 

### Example

```javascript
import LocationsApi from 'locations_api';

let apiInstance = new LocationsApi.MerchantCountrySubdivisionsApi();
let details = "topup.repower"; // String | This is the type of merchant location. Options  \"acceptance.paypass\" \"topup.repower\"  \"products.prepaidtravelcard\"  and \"offers.easysavings\"
let country = "USA"; // String | Any three digit country code as defined in ISO 3166-1. For example \"USA or \"CAN\"
apiInstance.merchantsV1CountrysubdivisionGet(details, country, (error, data, response) => {
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
 **country** | **String**| Any three digit country code as defined in ISO 3166-1. For example \&quot;USA or \&quot;CAN\&quot; | 

### Return type

[**CountrySubdivisionResponse**](CountrySubdivisionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

