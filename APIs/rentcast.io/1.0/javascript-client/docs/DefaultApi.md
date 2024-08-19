# RentCastApi.DefaultApi

All URIs are relative to *https://api.rentcast.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**marketStatistics**](DefaultApi.md#marketStatistics) | **GET** /markets | Market Statistics
[**propertyRecordById**](DefaultApi.md#propertyRecordById) | **GET** /properties/{id} | Property Record by Id
[**propertyRecords**](DefaultApi.md#propertyRecords) | **GET** /properties | Property Records
[**propertyRecordsRandom**](DefaultApi.md#propertyRecordsRandom) | **GET** /properties/random | Random Property Records
[**rentEstimateLongTerm**](DefaultApi.md#rentEstimateLongTerm) | **GET** /avm/rent/long-term | Rent Estimate
[**rentalListingLongTermById**](DefaultApi.md#rentalListingLongTermById) | **GET** /listings/rental/long-term/{id} | Rental Listing by Id
[**rentalListingsLongTerm**](DefaultApi.md#rentalListingsLongTerm) | **GET** /listings/rental/long-term | Rental Listings
[**saleListingById**](DefaultApi.md#saleListingById) | **GET** /listings/sale/{id} | Sale Listing by Id
[**saleListings**](DefaultApi.md#saleListings) | **GET** /listings/sale | Sale Listings
[**valueEstimate**](DefaultApi.md#valueEstimate) | **GET** /avm/value | Value Estimate



## marketStatistics

> MarketStatistics200Response marketStatistics(zipCode, opts)

Market Statistics

Returns aggregate rental statistics and listing trends for a single US zip code.

### Example

```javascript
import RentCastApi from 'rent_cast_api';
let defaultClient = RentCastApi.ApiClient.instance;
// Configure API key authorization: sec0
let sec0 = defaultClient.authentications['sec0'];
sec0.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//sec0.apiKeyPrefix = 'Token';

let apiInstance = new RentCastApi.DefaultApi();
let zipCode = "'29611'"; // String | A valid 5-digit US zip code
let opts = {
  'historyRange': 6 // Number | The time range for historical record entries, in months. Defaults to 12 if not provided
};
apiInstance.marketStatistics(zipCode, opts, (error, data, response) => {
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
 **zipCode** | **String**| A valid 5-digit US zip code | [default to &#39;29611&#39;]
 **historyRange** | **Number**| The time range for historical record entries, in months. Defaults to 12 if not provided | [optional] [default to 6]

### Return type

[**MarketStatistics200Response**](MarketStatistics200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## propertyRecordById

> PropertyRecords200ResponseInner propertyRecordById(id)

Property Record by Id

Returns a single property record matching the specified id.

### Example

```javascript
import RentCastApi from 'rent_cast_api';
let defaultClient = RentCastApi.ApiClient.instance;
// Configure API key authorization: sec0
let sec0 = defaultClient.authentications['sec0'];
sec0.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//sec0.apiKeyPrefix = 'Token';

let apiInstance = new RentCastApi.DefaultApi();
let id = "'5500-Grand-Lake-Dr,-San-Antonio,-TX-78244'"; // String | The id of the property record to return
apiInstance.propertyRecordById(id, (error, data, response) => {
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
 **id** | **String**| The id of the property record to return | [default to &#39;5500-Grand-Lake-Dr,-San-Antonio,-TX-78244&#39;]

### Return type

[**PropertyRecords200ResponseInner**](PropertyRecords200ResponseInner.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## propertyRecords

> [PropertyRecords200ResponseInner] propertyRecords(opts)

Property Records

Search for property records in a geographical area, or by a specific address.

### Example

```javascript
import RentCastApi from 'rent_cast_api';
let defaultClient = RentCastApi.ApiClient.instance;
// Configure API key authorization: sec0
let sec0 = defaultClient.authentications['sec0'];
sec0.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//sec0.apiKeyPrefix = 'Token';

let apiInstance = new RentCastApi.DefaultApi();
let opts = {
  'address': "'5500 Grand Lake Dr, San Antonio, TX, 78244'", // String | The full address of the property, in the format of `Street, City, State, Zip`. Used to retrieve data for a specific property, or together with the `radius` parameter to search for properties in a specific area
  'city': "city_example", // String | The name of the city, used to search for properties in a specific city. This parameter is case-sensitive
  'state': "state_example", // String | The 2-character state abbreviation, used to search for properties in a specific state. This parameter is case-sensitive
  'zipCode': "zipCode_example", // String | The 5-digit zip code, used to search for properties in a specific zip code
  'latitude': 3.4, // Number | The latitude of the search area. Use the `latitude`/`longitude` and `radius` parameters to search for properties in a specific area
  'longitude': 3.4, // Number | The longitude of the search area. Use the `latitude`/`longitude` and `radius` parameters to search for properties in a specific area
  'radius': 3.4, // Number | The radius of the search area in miles, with a maximum of 100. Use in combination with the `latitude`/`longitude` or `address` parameters to search for properties in a specific area
  'propertyType': "propertyType_example", // String | The type of the property, used to search for properties matching this criteria. See [explanation of property types](https://developers.rentcast.io/reference/property-types)
  'bedrooms': 3.4, // Number | The number of bedrooms, used to search for properties matching this criteria. Use `0` to indicate a studio layout
  'bathrooms': 3.4, // Number | The number of bathrooms, used to search for properties matching this criteria. Supports fractions to indicate partial bathrooms
  'limit': 56, // Number | The maximum number of property records to return, between 1 and 500. Defaults to 50 if not provided. [Learn more](https://developers.rentcast.io/reference/pagination) about pagination
  'offset': 56 // Number | The index of the first property record to return, used to paginate through large lists of results. Defaults to 0 if not provided. [Learn more](https://developers.rentcast.io/reference/pagination) about pagination
};
apiInstance.propertyRecords(opts, (error, data, response) => {
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
 **address** | **String**| The full address of the property, in the format of &#x60;Street, City, State, Zip&#x60;. Used to retrieve data for a specific property, or together with the &#x60;radius&#x60; parameter to search for properties in a specific area | [optional] [default to &#39;5500 Grand Lake Dr, San Antonio, TX, 78244&#39;]
 **city** | **String**| The name of the city, used to search for properties in a specific city. This parameter is case-sensitive | [optional] 
 **state** | **String**| The 2-character state abbreviation, used to search for properties in a specific state. This parameter is case-sensitive | [optional] 
 **zipCode** | **String**| The 5-digit zip code, used to search for properties in a specific zip code | [optional] 
 **latitude** | **Number**| The latitude of the search area. Use the &#x60;latitude&#x60;/&#x60;longitude&#x60; and &#x60;radius&#x60; parameters to search for properties in a specific area | [optional] 
 **longitude** | **Number**| The longitude of the search area. Use the &#x60;latitude&#x60;/&#x60;longitude&#x60; and &#x60;radius&#x60; parameters to search for properties in a specific area | [optional] 
 **radius** | **Number**| The radius of the search area in miles, with a maximum of 100. Use in combination with the &#x60;latitude&#x60;/&#x60;longitude&#x60; or &#x60;address&#x60; parameters to search for properties in a specific area | [optional] 
 **propertyType** | **String**| The type of the property, used to search for properties matching this criteria. See [explanation of property types](https://developers.rentcast.io/reference/property-types) | [optional] 
 **bedrooms** | **Number**| The number of bedrooms, used to search for properties matching this criteria. Use &#x60;0&#x60; to indicate a studio layout | [optional] 
 **bathrooms** | **Number**| The number of bathrooms, used to search for properties matching this criteria. Supports fractions to indicate partial bathrooms | [optional] 
 **limit** | **Number**| The maximum number of property records to return, between 1 and 500. Defaults to 50 if not provided. [Learn more](https://developers.rentcast.io/reference/pagination) about pagination | [optional] 
 **offset** | **Number**| The index of the first property record to return, used to paginate through large lists of results. Defaults to 0 if not provided. [Learn more](https://developers.rentcast.io/reference/pagination) about pagination | [optional] 

### Return type

[**[PropertyRecords200ResponseInner]**](PropertyRecords200ResponseInner.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## propertyRecordsRandom

> [PropertyRecordsRandom200ResponseInner] propertyRecordsRandom(opts)

Random Property Records

Returns a list of property records selected at random.

### Example

```javascript
import RentCastApi from 'rent_cast_api';
let defaultClient = RentCastApi.ApiClient.instance;
// Configure API key authorization: sec0
let sec0 = defaultClient.authentications['sec0'];
sec0.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//sec0.apiKeyPrefix = 'Token';

let apiInstance = new RentCastApi.DefaultApi();
let opts = {
  'limit': 5 // Number | The number of records to return, between 1 and 500. Defaults to 50 if not provided
};
apiInstance.propertyRecordsRandom(opts, (error, data, response) => {
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
 **limit** | **Number**| The number of records to return, between 1 and 500. Defaults to 50 if not provided | [optional] [default to 5]

### Return type

[**[PropertyRecordsRandom200ResponseInner]**](PropertyRecordsRandom200ResponseInner.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## rentEstimateLongTerm

> RentEstimateLongTerm200Response rentEstimateLongTerm(opts)

Rent Estimate

Returns a property rent estimate and comparable properties.

### Example

```javascript
import RentCastApi from 'rent_cast_api';
let defaultClient = RentCastApi.ApiClient.instance;
// Configure API key authorization: sec0
let sec0 = defaultClient.authentications['sec0'];
sec0.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//sec0.apiKeyPrefix = 'Token';

let apiInstance = new RentCastApi.DefaultApi();
let opts = {
  'address': "'5500 Grand Lake Drive, San Antonio, TX, 78244'", // String | The full property address, in the format of `Street, City, State, Zip`. You need to provide either the `address` or the `latitude`/`longitude` parameters
  'latitude': 3.4, // Number | The latitude of the property. The `latitude`/`longitude` can be provided instead of the `address` parameter
  'longitude': 3.4, // Number | The longitude of the property. The `latitude`/`longitude` can be provided instead of the `address` parameter
  'propertyType': "'Single Family'", // String | The type of the property. See [explanation of property types](https://developers.rentcast.io/reference/property-types)
  'bedrooms': 4, // Number | The number of bedrooms in the property. Use `0` to indicate a studio layout
  'bathrooms': 2, // Number | The number of bathrooms in the property. Supports fractions to indicate partial bathrooms
  'squareFootage': 1600, // Number | The total living area size of the property, in square feet
  'maxRadius': 3.4, // Number | The maximum distance between comparable listings and the subject property, in miles
  'daysOld': 3.4, // Number | The maximum number of days since comparable listings were last seen on the market, with a minimum of 1
  'compCount': 5 // Number | The number of comparable listings to use when calculating the rent estimate, between 5 and 25. Defaults to 10 if not provided
};
apiInstance.rentEstimateLongTerm(opts, (error, data, response) => {
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
 **address** | **String**| The full property address, in the format of &#x60;Street, City, State, Zip&#x60;. You need to provide either the &#x60;address&#x60; or the &#x60;latitude&#x60;/&#x60;longitude&#x60; parameters | [optional] [default to &#39;5500 Grand Lake Drive, San Antonio, TX, 78244&#39;]
 **latitude** | **Number**| The latitude of the property. The &#x60;latitude&#x60;/&#x60;longitude&#x60; can be provided instead of the &#x60;address&#x60; parameter | [optional] 
 **longitude** | **Number**| The longitude of the property. The &#x60;latitude&#x60;/&#x60;longitude&#x60; can be provided instead of the &#x60;address&#x60; parameter | [optional] 
 **propertyType** | **String**| The type of the property. See [explanation of property types](https://developers.rentcast.io/reference/property-types) | [optional] [default to &#39;Single Family&#39;]
 **bedrooms** | **Number**| The number of bedrooms in the property. Use &#x60;0&#x60; to indicate a studio layout | [optional] [default to 4]
 **bathrooms** | **Number**| The number of bathrooms in the property. Supports fractions to indicate partial bathrooms | [optional] [default to 2]
 **squareFootage** | **Number**| The total living area size of the property, in square feet | [optional] [default to 1600]
 **maxRadius** | **Number**| The maximum distance between comparable listings and the subject property, in miles | [optional] 
 **daysOld** | **Number**| The maximum number of days since comparable listings were last seen on the market, with a minimum of 1 | [optional] 
 **compCount** | **Number**| The number of comparable listings to use when calculating the rent estimate, between 5 and 25. Defaults to 10 if not provided | [optional] [default to 5]

### Return type

[**RentEstimateLongTerm200Response**](RentEstimateLongTerm200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## rentalListingLongTermById

> RentalListingLongTermById200Response rentalListingLongTermById(id)

Rental Listing by Id

Returns a single rental listing matching the specified id.

### Example

```javascript
import RentCastApi from 'rent_cast_api';
let defaultClient = RentCastApi.ApiClient.instance;
// Configure API key authorization: sec0
let sec0 = defaultClient.authentications['sec0'];
sec0.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//sec0.apiKeyPrefix = 'Token';

let apiInstance = new RentCastApi.DefaultApi();
let id = "'1702-Cherry-Orchard-Dr,-Austin,-TX-78745'"; // String | The id of the property listing to return
apiInstance.rentalListingLongTermById(id, (error, data, response) => {
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
 **id** | **String**| The id of the property listing to return | [default to &#39;1702-Cherry-Orchard-Dr,-Austin,-TX-78745&#39;]

### Return type

[**RentalListingLongTermById200Response**](RentalListingLongTermById200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## rentalListingsLongTerm

> [RentalListingsLongTerm200ResponseInner] rentalListingsLongTerm(opts)

Rental Listings

Search for rental listings in a geographical area, or by a specific address.

### Example

```javascript
import RentCastApi from 'rent_cast_api';
let defaultClient = RentCastApi.ApiClient.instance;
// Configure API key authorization: sec0
let sec0 = defaultClient.authentications['sec0'];
sec0.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//sec0.apiKeyPrefix = 'Token';

let apiInstance = new RentCastApi.DefaultApi();
let opts = {
  'address': "address_example", // String | The full address of the property, in the format of `Street, City, State, Zip`. Used to retrieve data for a specific property, or together with the `radius` parameter to search for listings in a specific area
  'city': "'Austin'", // String | The name of the city, used to search for listings in a specific city. This parameter is case-sensitive
  'state': "'TX'", // String | The 2-character state abbreviation, used to search for listings in a specific state. This parameter is case-sensitive
  'zipCode': "zipCode_example", // String | The 5-digit zip code, used to search for listings in a specific zip code
  'latitude': 3.4, // Number | The latitude of the search area. Use the `latitude`/`longitude` and `radius` parameters to search for listings in a specific area
  'longitude': 3.4, // Number | The longitude of the search area. Use the `latitude`/`longitude` and `radius` parameters to search for listings in a specific area
  'radius': 3.4, // Number | The radius of the search area in miles, with a maximum of 100. Use in combination with the `latitude`/`longitude` or `address` parameters to search for listings in a specific area
  'propertyType': "propertyType_example", // String | The type of the property, used to search for listings matching this criteria. See [explanation of property types](https://developers.rentcast.io/reference/property-types)
  'bedrooms': 3.4, // Number | The number of bedrooms, used to search for listings matching this criteria. Use `0` to indicate a studio layout
  'bathrooms': 3.4, // Number | The number of bathrooms, used to search for listings matching this criteria. Supports fractions to indicate partial bathrooms
  'status': "'Active'", // String | The current listing status, used to search for listings matching this criteria
  'daysOld': 3.4, // Number | The maximum number of days since a property was listed on the market, with a minimum of 1
  'limit': 5, // Number | The maximum number of listings to return, between 1 and 500. Defaults to 50 if not provided. [Learn more](https://developers.rentcast.io/reference/pagination) about pagination
  'offset': 56 // Number | The index of the first listing to return, used to paginate through large lists of results. Defaults to 0 if not provided. [Learn more](https://developers.rentcast.io/reference/pagination) about pagination
};
apiInstance.rentalListingsLongTerm(opts, (error, data, response) => {
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
 **address** | **String**| The full address of the property, in the format of &#x60;Street, City, State, Zip&#x60;. Used to retrieve data for a specific property, or together with the &#x60;radius&#x60; parameter to search for listings in a specific area | [optional] 
 **city** | **String**| The name of the city, used to search for listings in a specific city. This parameter is case-sensitive | [optional] [default to &#39;Austin&#39;]
 **state** | **String**| The 2-character state abbreviation, used to search for listings in a specific state. This parameter is case-sensitive | [optional] [default to &#39;TX&#39;]
 **zipCode** | **String**| The 5-digit zip code, used to search for listings in a specific zip code | [optional] 
 **latitude** | **Number**| The latitude of the search area. Use the &#x60;latitude&#x60;/&#x60;longitude&#x60; and &#x60;radius&#x60; parameters to search for listings in a specific area | [optional] 
 **longitude** | **Number**| The longitude of the search area. Use the &#x60;latitude&#x60;/&#x60;longitude&#x60; and &#x60;radius&#x60; parameters to search for listings in a specific area | [optional] 
 **radius** | **Number**| The radius of the search area in miles, with a maximum of 100. Use in combination with the &#x60;latitude&#x60;/&#x60;longitude&#x60; or &#x60;address&#x60; parameters to search for listings in a specific area | [optional] 
 **propertyType** | **String**| The type of the property, used to search for listings matching this criteria. See [explanation of property types](https://developers.rentcast.io/reference/property-types) | [optional] 
 **bedrooms** | **Number**| The number of bedrooms, used to search for listings matching this criteria. Use &#x60;0&#x60; to indicate a studio layout | [optional] 
 **bathrooms** | **Number**| The number of bathrooms, used to search for listings matching this criteria. Supports fractions to indicate partial bathrooms | [optional] 
 **status** | **String**| The current listing status, used to search for listings matching this criteria | [optional] [default to &#39;Active&#39;]
 **daysOld** | **Number**| The maximum number of days since a property was listed on the market, with a minimum of 1 | [optional] 
 **limit** | **Number**| The maximum number of listings to return, between 1 and 500. Defaults to 50 if not provided. [Learn more](https://developers.rentcast.io/reference/pagination) about pagination | [optional] [default to 5]
 **offset** | **Number**| The index of the first listing to return, used to paginate through large lists of results. Defaults to 0 if not provided. [Learn more](https://developers.rentcast.io/reference/pagination) about pagination | [optional] 

### Return type

[**[RentalListingsLongTerm200ResponseInner]**](RentalListingsLongTerm200ResponseInner.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## saleListingById

> SaleListingById200Response saleListingById(id)

Sale Listing by Id

Returns a single sale listing matching the specified id.

### Example

```javascript
import RentCastApi from 'rent_cast_api';
let defaultClient = RentCastApi.ApiClient.instance;
// Configure API key authorization: sec0
let sec0 = defaultClient.authentications['sec0'];
sec0.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//sec0.apiKeyPrefix = 'Token';

let apiInstance = new RentCastApi.DefaultApi();
let id = "'1702-Cherry-Orchard-Dr,-Austin,-TX-78745'"; // String | The id of the property listing to return
apiInstance.saleListingById(id, (error, data, response) => {
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
 **id** | **String**| The id of the property listing to return | [default to &#39;1702-Cherry-Orchard-Dr,-Austin,-TX-78745&#39;]

### Return type

[**SaleListingById200Response**](SaleListingById200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## saleListings

> [SaleListings200ResponseInner] saleListings(opts)

Sale Listings

Search for sale listings in a geographical area, or by a specific address.

### Example

```javascript
import RentCastApi from 'rent_cast_api';
let defaultClient = RentCastApi.ApiClient.instance;
// Configure API key authorization: sec0
let sec0 = defaultClient.authentications['sec0'];
sec0.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//sec0.apiKeyPrefix = 'Token';

let apiInstance = new RentCastApi.DefaultApi();
let opts = {
  'address': "address_example", // String | The full address of the property, in the format of `Street, City, State, Zip`. Used to retrieve data for a specific property, or together with the `radius` parameter to search for listings in a specific area
  'city': "'Austin'", // String | The name of the city, used to search for listings in a specific city. This parameter is case-sensitive
  'state': "'TX'", // String | The 2-character state abbreviation, used to search for listings in a specific state. This parameter is case-sensitive
  'zipCode': "zipCode_example", // String | The 5-digit zip code, used to search for listings in a specific zip code
  'latitude': 3.4, // Number | The latitude of the search area. Use the `latitude`/`longitude` and `radius` parameters to search for listings in a specific area
  'longitude': 3.4, // Number | The longitude of the search area. Use the `latitude`/`longitude` and `radius` parameters to search for listings in a specific area
  'radius': 3.4, // Number | The radius of the search area in miles, with a maximum of 100. Use in combination with the `latitude`/`longitude` or `address` parameters to search for listings in a specific area
  'propertyType': "propertyType_example", // String | The type of the property, used to search for listings matching this criteria. See [explanation of property types](https://developers.rentcast.io/reference/property-types)
  'bedrooms': 3.4, // Number | The number of bedrooms, used to search for listings matching this criteria. Use `0` to indicate a studio layout
  'bathrooms': 3.4, // Number | The number of bathrooms, used to search for listings matching this criteria. Supports fractions to indicate partial bathrooms
  'status': "'Active'", // String | The current listing status, used to search for listings matching this criteria
  'daysOld': 3.4, // Number | The maximum number of days since a property was listed on the market, with a minimum of 1
  'limit': 5, // Number | The maximum number of listings to return, between 1 and 500. Defaults to 50 if not provided. [Learn more](https://developers.rentcast.io/reference/pagination) about pagination
  'offset': 56 // Number | The index of the first listing to return, used to paginate through large lists of results. Defaults to 0 if not provided. [Learn more](https://developers.rentcast.io/reference/pagination) about pagination
};
apiInstance.saleListings(opts, (error, data, response) => {
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
 **address** | **String**| The full address of the property, in the format of &#x60;Street, City, State, Zip&#x60;. Used to retrieve data for a specific property, or together with the &#x60;radius&#x60; parameter to search for listings in a specific area | [optional] 
 **city** | **String**| The name of the city, used to search for listings in a specific city. This parameter is case-sensitive | [optional] [default to &#39;Austin&#39;]
 **state** | **String**| The 2-character state abbreviation, used to search for listings in a specific state. This parameter is case-sensitive | [optional] [default to &#39;TX&#39;]
 **zipCode** | **String**| The 5-digit zip code, used to search for listings in a specific zip code | [optional] 
 **latitude** | **Number**| The latitude of the search area. Use the &#x60;latitude&#x60;/&#x60;longitude&#x60; and &#x60;radius&#x60; parameters to search for listings in a specific area | [optional] 
 **longitude** | **Number**| The longitude of the search area. Use the &#x60;latitude&#x60;/&#x60;longitude&#x60; and &#x60;radius&#x60; parameters to search for listings in a specific area | [optional] 
 **radius** | **Number**| The radius of the search area in miles, with a maximum of 100. Use in combination with the &#x60;latitude&#x60;/&#x60;longitude&#x60; or &#x60;address&#x60; parameters to search for listings in a specific area | [optional] 
 **propertyType** | **String**| The type of the property, used to search for listings matching this criteria. See [explanation of property types](https://developers.rentcast.io/reference/property-types) | [optional] 
 **bedrooms** | **Number**| The number of bedrooms, used to search for listings matching this criteria. Use &#x60;0&#x60; to indicate a studio layout | [optional] 
 **bathrooms** | **Number**| The number of bathrooms, used to search for listings matching this criteria. Supports fractions to indicate partial bathrooms | [optional] 
 **status** | **String**| The current listing status, used to search for listings matching this criteria | [optional] [default to &#39;Active&#39;]
 **daysOld** | **Number**| The maximum number of days since a property was listed on the market, with a minimum of 1 | [optional] 
 **limit** | **Number**| The maximum number of listings to return, between 1 and 500. Defaults to 50 if not provided. [Learn more](https://developers.rentcast.io/reference/pagination) about pagination | [optional] [default to 5]
 **offset** | **Number**| The index of the first listing to return, used to paginate through large lists of results. Defaults to 0 if not provided. [Learn more](https://developers.rentcast.io/reference/pagination) about pagination | [optional] 

### Return type

[**[SaleListings200ResponseInner]**](SaleListings200ResponseInner.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## valueEstimate

> ValueEstimate200Response valueEstimate(opts)

Value Estimate

Returns a property value estimate and comparable properties.

### Example

```javascript
import RentCastApi from 'rent_cast_api';
let defaultClient = RentCastApi.ApiClient.instance;
// Configure API key authorization: sec0
let sec0 = defaultClient.authentications['sec0'];
sec0.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//sec0.apiKeyPrefix = 'Token';

let apiInstance = new RentCastApi.DefaultApi();
let opts = {
  'address': "'5500 Grand Lake Drive, San Antonio, TX, 78244'", // String | The full property address, in the format of `Street, City, State, Zip`. You need to provide either the `address` or the `latitude`/`longitude` parameters
  'latitude': 3.4, // Number | The latitude of the property. The `latitude`/`longitude` can be provided instead of the `address` parameter
  'longitude': 3.4, // Number | The longitude of the property. The `latitude`/`longitude` can be provided instead of the `address` parameter
  'propertyType': "'Single Family'", // String | The type of the property. See [explanation of property types](https://developers.rentcast.io/reference/property-types)
  'bedrooms': 4, // Number | The number of bedrooms in the property. Use `0` to indicate a studio layout
  'bathrooms': 2, // Number | The number of bathrooms in the property. Supports fractions to indicate partial bathrooms
  'squareFootage': 1600, // Number | The total living area size of the property, in square feet
  'maxRadius': 3.4, // Number | The maximum distance between comparable listings and the subject property, in miles
  'daysOld': 3.4, // Number | The maximum number of days since comparable listings were last seen on the market, with a minimum of 1
  'compCount': 5 // Number | The number of comparable listings to use when calculating the value estimate, between 5 and 25. Defaults to 10 if not provided
};
apiInstance.valueEstimate(opts, (error, data, response) => {
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
 **address** | **String**| The full property address, in the format of &#x60;Street, City, State, Zip&#x60;. You need to provide either the &#x60;address&#x60; or the &#x60;latitude&#x60;/&#x60;longitude&#x60; parameters | [optional] [default to &#39;5500 Grand Lake Drive, San Antonio, TX, 78244&#39;]
 **latitude** | **Number**| The latitude of the property. The &#x60;latitude&#x60;/&#x60;longitude&#x60; can be provided instead of the &#x60;address&#x60; parameter | [optional] 
 **longitude** | **Number**| The longitude of the property. The &#x60;latitude&#x60;/&#x60;longitude&#x60; can be provided instead of the &#x60;address&#x60; parameter | [optional] 
 **propertyType** | **String**| The type of the property. See [explanation of property types](https://developers.rentcast.io/reference/property-types) | [optional] [default to &#39;Single Family&#39;]
 **bedrooms** | **Number**| The number of bedrooms in the property. Use &#x60;0&#x60; to indicate a studio layout | [optional] [default to 4]
 **bathrooms** | **Number**| The number of bathrooms in the property. Supports fractions to indicate partial bathrooms | [optional] [default to 2]
 **squareFootage** | **Number**| The total living area size of the property, in square feet | [optional] [default to 1600]
 **maxRadius** | **Number**| The maximum distance between comparable listings and the subject property, in miles | [optional] 
 **daysOld** | **Number**| The maximum number of days since comparable listings were last seen on the market, with a minimum of 1 | [optional] 
 **compCount** | **Number**| The number of comparable listings to use when calculating the value estimate, between 5 and 25. Defaults to 10 if not provided | [optional] [default to 5]

### Return type

[**ValueEstimate200Response**](ValueEstimate200Response.md)

### Authorization

[sec0](../README.md#sec0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

