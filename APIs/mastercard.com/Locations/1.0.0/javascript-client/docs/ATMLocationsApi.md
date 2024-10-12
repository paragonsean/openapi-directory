# LocationsApi.ATMLocationsApi

All URIs are relative to *https://api.mastercard.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**atmsV1AtmGet**](ATMLocationsApi.md#atmsV1AtmGet) | **GET** /atms/v1/atm | Returns detailed information about an ATM location.  This information can be used to display ATMs on a map, provide driving directions, or show special ATM features.



## atmsV1AtmGet

> AtmsResponse atmsV1AtmGet(pageOffset, pageLength, opts)

Returns detailed information about an ATM location.  This information can be used to display ATMs on a map, provide driving directions, or show special ATM features.

Returns detailed information about an ATM location.  This information can be used to display ATMs on a map, provide driving directions, or show special ATM features. 

### Example

```javascript
import LocationsApi from 'locations_api';

let apiInstance = new LocationsApi.ATMLocationsApi();
let pageOffset = 0; // Number | Zero-based offset where the response will start. The actual start position is this value +1. An offset of 10 starts at item 11. Combined with the PageLength option this allows pagination to be supported through the service requests.
let pageLength = 5; // Number | Maximum number of items to retrieve within the current \"page\" of results.
let opts = {
  'addressLine1': "114 Fifth Avenue", // String | Line 1 of the street address for the merchant location.  Usually includes the street number and name. This parameter is ignored if latitude and longitude are provided. If you provide this parameter you must also provide the Country parameter and either City parameter or PostalCode parameter.
  'addressLine2': "Apartment 1", // String | Line 2 of the street address usually an apartment number or suite number. This parameter is used rarely and is ignored if latitude and longitude are provided. If you provide this parameter you must also provide the Country parameter and either City parameter or PostalCode parameter.
  'city': "New York City", // String | The name of the city for a merchant location.  This parameter is ignored if latitude and longitude are provided. If you provide this parameter you must also provide the Country parameter.
  'countrySubdivision': "NY", // String | The state or province for a merchant location (only supported for US and Canada locations).  This parameter is ignored if latitude and longitude are provided. If you provide this parameter you must also provide the Country parameter.
  'postalCode': "11101", // String | The zip code or postal code for a merchant location.  This parameter is ignored if latitude and longitude are provided. If you provide this parameter you must also provide the Country parameter.
  'country': "USA", // String | Any three digit country code for an ATM location.  Valid values are Three digit alpha country code as defined in ISO 3166-1.  This parameter is ignored if latitude and longitude are provided. This parameter is required if any other address information is provided including AddressLine1 AddressLine2 City PostalCode or CountrySubdivision.
  'latitude': 38.76006576913497, // Number | The latitude of a merchant location.  If latitude is provided longitude must also be provided.
  'longitude': -90.74615107952418, // Number | The longitude of a merchant location.  If longitude is provided latitude must also be provided.
  'distanceUnit': "MILE", // String | Indicates the unit for the radius as well as the units of the distance of each location from the basepoint in the response.
  'radius': 25, // Number | This is the radius from the search point in the distance unit you set.  For example if you want to search for locations within 50 miles of a certain point you would set DistanceUnit=mile and Radius=50.  This parameter is ignored in non-geocoded countries.
  'supportEMV': 1, // Number | This indicates whether the ATM should have the ability to read chip cards or not.
  'internationalMaestroAccepted': 1 // Number | This field will provide ATM Terminals which can still process Maestro transactions but are not yet EMV chip reader enabled. Information available only for USA and Argentina till October 2014.
};
apiInstance.atmsV1AtmGet(pageOffset, pageLength, opts, (error, data, response) => {
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
 **pageOffset** | **Number**| Zero-based offset where the response will start. The actual start position is this value +1. An offset of 10 starts at item 11. Combined with the PageLength option this allows pagination to be supported through the service requests. | 
 **pageLength** | **Number**| Maximum number of items to retrieve within the current \&quot;page\&quot; of results. | 
 **addressLine1** | **String**| Line 1 of the street address for the merchant location.  Usually includes the street number and name. This parameter is ignored if latitude and longitude are provided. If you provide this parameter you must also provide the Country parameter and either City parameter or PostalCode parameter. | [optional] 
 **addressLine2** | **String**| Line 2 of the street address usually an apartment number or suite number. This parameter is used rarely and is ignored if latitude and longitude are provided. If you provide this parameter you must also provide the Country parameter and either City parameter or PostalCode parameter. | [optional] 
 **city** | **String**| The name of the city for a merchant location.  This parameter is ignored if latitude and longitude are provided. If you provide this parameter you must also provide the Country parameter. | [optional] 
 **countrySubdivision** | **String**| The state or province for a merchant location (only supported for US and Canada locations).  This parameter is ignored if latitude and longitude are provided. If you provide this parameter you must also provide the Country parameter. | [optional] 
 **postalCode** | **String**| The zip code or postal code for a merchant location.  This parameter is ignored if latitude and longitude are provided. If you provide this parameter you must also provide the Country parameter. | [optional] 
 **country** | **String**| Any three digit country code for an ATM location.  Valid values are Three digit alpha country code as defined in ISO 3166-1.  This parameter is ignored if latitude and longitude are provided. This parameter is required if any other address information is provided including AddressLine1 AddressLine2 City PostalCode or CountrySubdivision. | [optional] 
 **latitude** | **Number**| The latitude of a merchant location.  If latitude is provided longitude must also be provided. | [optional] 
 **longitude** | **Number**| The longitude of a merchant location.  If longitude is provided latitude must also be provided. | [optional] 
 **distanceUnit** | **String**| Indicates the unit for the radius as well as the units of the distance of each location from the basepoint in the response. | [optional] 
 **radius** | **Number**| This is the radius from the search point in the distance unit you set.  For example if you want to search for locations within 50 miles of a certain point you would set DistanceUnit&#x3D;mile and Radius&#x3D;50.  This parameter is ignored in non-geocoded countries. | [optional] 
 **supportEMV** | **Number**| This indicates whether the ATM should have the ability to read chip cards or not. | [optional] 
 **internationalMaestroAccepted** | **Number**| This field will provide ATM Terminals which can still process Maestro transactions but are not yet EMV chip reader enabled. Information available only for USA and Argentina till October 2014. | [optional] 

### Return type

[**AtmsResponse**](AtmsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

