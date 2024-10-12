# LocationsApi.MerchantLocationsApi

All URIs are relative to *https://api.mastercard.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**merchantsV1MerchantGet**](MerchantLocationsApi.md#merchantsV1MerchantGet) | **GET** /merchants/v1/merchant | Returns merchant location information for merchants offering the following services: accept contactless-enabled cards and devices, allow customers to add money to an eligible MasterCard or Maestro prepaid card, issue MasterCard Prepaid Travel cards, participate in the MasterCard Easy Savings program, and offer cash at checkout when paying with a Debit MasterCard or Maestro Card. 



## merchantsV1MerchantGet

> MerchantsResponse merchantsV1MerchantGet(details, pageOffset, pageLength, opts)

Returns merchant location information for merchants offering the following services: accept contactless-enabled cards and devices, allow customers to add money to an eligible MasterCard or Maestro prepaid card, issue MasterCard Prepaid Travel cards, participate in the MasterCard Easy Savings program, and offer cash at checkout when paying with a Debit MasterCard or Maestro Card. 

Returns merchant location information for merchants offering the following services: accept contactless-enabled cards and devices, allow customers to add money to an eligible MasterCard or Maestro prepaid card, issue MasterCard Prepaid Travel cards, participate in the MasterCard Easy Savings program, and offer cash at checkout when paying with a Debit MasterCard or Maestro Card. 

### Example

```javascript
import LocationsApi from 'locations_api';

let apiInstance = new LocationsApi.MerchantLocationsApi();
let details = "acceptance.paypass"; // String | Type of merchant location. Options are \"acceptance.paypass\" \"topup.repower\" \"products.prepaidtravelcard\" \"offers.easysavings\" and \"features.cashback\". Cash Back is currently only available in the US.
let pageOffset = 0; // Number | Zero-based offset where the response will start. The actual start position is this value +1. An offset of 10 starts at item 11. Combined with the PageLength option this allows pagination to be supported through the service requests.
let pageLength = 5; // Number | Maximum number of items to retrieve within the current \"page\" of results.
let opts = {
  'category': "features.cashback", // String | Category of the merchant location. See the Categories (Merchant) resource for a list of valid categories. This parameter is only valid for merchant queries with Details = \"acceptance.paypass\" or \"features.cashback\".
  'addressLine1': "42 Elm Street", // String | Line 1 of the street address for the merchant location.  Usually includes the street number and name. This parameter is ignored if latitude and longitude are provided. If you provide this parameter you must also provide the Country parameter and either City parameter or PostalCode parameter.
  'addressLine2': "Suite 101", // String | Line 2 of the street address usually an apartment number or suite number. This parameter is used rarely and is ignored if latitude and longitude are provided. If you provide this parameter you must also provide the Country parameter and either City parameter or PostalCode parameter.
  'city': "New York", // String | Name of the city for a merchant location.  This parameter is ignored if latitude and longitude are provided. If you provide this parameter you must also provide the Country parameter.
  'countrySubdivision': "NY", // String | State or province for a merchant location (only supported for US and Canada locations).  This parameter is ignored if latitude and longitude are provided. If you provide this parameter you must also provide the Country parameter.
  'postalCode': "11001", // String | Zip code or postal code for a merchant location.  This parameter is ignored if latitude and longitude are provided. If you provide this parameter you must also provide the Country parameter.
  'country': "USA", // String | Any three digit country code for an ATM location.  Valid values are Three digit alpha country code as defined in ISO 3166-1.  This parameter is ignored if latitude and longitude are provided. This parameter is required if any other address information is provided including AddressLine1 AddressLine2 City PostalCode or CountrySubdivision. By default we supply ATM location data for United States ATMs for up to twenty-five records per request.
  'latitude': 38.53463, // Number | Latitude of a merchant location.  If latitude is provided longitude must also be provided.
  'longitude': -90.286781, // Number | Longitude of a merchant location.  If longitude is provided latitude must also be provided.
  'distanceUnit': "MILE", // String | Indicates the unit for the radius as well as the units of the distance of each location from the basepoint in the response.
  'radius': 25, // Number | This is the radius from the search point in the distance unit you set.  For example if you want to search for locations within 50 miles of a certain point you would set DistanceUnit=mile and Radius=50.  This parameter is ignored in non-geocoded countries.
  'offerMerchantID': "34760" // String | Unique identifier that represents the merhcant sponsor of an offer. Any valid merchant ID.
};
apiInstance.merchantsV1MerchantGet(details, pageOffset, pageLength, opts, (error, data, response) => {
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
 **details** | **String**| Type of merchant location. Options are \&quot;acceptance.paypass\&quot; \&quot;topup.repower\&quot; \&quot;products.prepaidtravelcard\&quot; \&quot;offers.easysavings\&quot; and \&quot;features.cashback\&quot;. Cash Back is currently only available in the US. | 
 **pageOffset** | **Number**| Zero-based offset where the response will start. The actual start position is this value +1. An offset of 10 starts at item 11. Combined with the PageLength option this allows pagination to be supported through the service requests. | 
 **pageLength** | **Number**| Maximum number of items to retrieve within the current \&quot;page\&quot; of results. | 
 **category** | **String**| Category of the merchant location. See the Categories (Merchant) resource for a list of valid categories. This parameter is only valid for merchant queries with Details &#x3D; \&quot;acceptance.paypass\&quot; or \&quot;features.cashback\&quot;. | [optional] 
 **addressLine1** | **String**| Line 1 of the street address for the merchant location.  Usually includes the street number and name. This parameter is ignored if latitude and longitude are provided. If you provide this parameter you must also provide the Country parameter and either City parameter or PostalCode parameter. | [optional] 
 **addressLine2** | **String**| Line 2 of the street address usually an apartment number or suite number. This parameter is used rarely and is ignored if latitude and longitude are provided. If you provide this parameter you must also provide the Country parameter and either City parameter or PostalCode parameter. | [optional] 
 **city** | **String**| Name of the city for a merchant location.  This parameter is ignored if latitude and longitude are provided. If you provide this parameter you must also provide the Country parameter. | [optional] 
 **countrySubdivision** | **String**| State or province for a merchant location (only supported for US and Canada locations).  This parameter is ignored if latitude and longitude are provided. If you provide this parameter you must also provide the Country parameter. | [optional] 
 **postalCode** | **String**| Zip code or postal code for a merchant location.  This parameter is ignored if latitude and longitude are provided. If you provide this parameter you must also provide the Country parameter. | [optional] 
 **country** | **String**| Any three digit country code for an ATM location.  Valid values are Three digit alpha country code as defined in ISO 3166-1.  This parameter is ignored if latitude and longitude are provided. This parameter is required if any other address information is provided including AddressLine1 AddressLine2 City PostalCode or CountrySubdivision. By default we supply ATM location data for United States ATMs for up to twenty-five records per request. | [optional] 
 **latitude** | **Number**| Latitude of a merchant location.  If latitude is provided longitude must also be provided. | [optional] 
 **longitude** | **Number**| Longitude of a merchant location.  If longitude is provided latitude must also be provided. | [optional] 
 **distanceUnit** | **String**| Indicates the unit for the radius as well as the units of the distance of each location from the basepoint in the response. | [optional] 
 **radius** | **Number**| This is the radius from the search point in the distance unit you set.  For example if you want to search for locations within 50 miles of a certain point you would set DistanceUnit&#x3D;mile and Radius&#x3D;50.  This parameter is ignored in non-geocoded countries. | [optional] 
 **offerMerchantID** | **String**| Unique identifier that represents the merhcant sponsor of an offer. Any valid merchant ID. | [optional] 

### Return type

[**MerchantsResponse**](MerchantsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

