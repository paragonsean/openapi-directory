# AtmLocatorApi.ATMsApi

All URIs are relative to *https://dikpeqbnwi3kx.cloudfront.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**openBankingV22AtmsGet**](ATMsApi.md#openBankingV22AtmsGet) | **GET** /open-banking/v2.2/atms | 
[**xOpenBankingV22AtmsCountryCountryGet**](ATMsApi.md#xOpenBankingV22AtmsCountryCountryGet) | **GET** /x-open-banking/v2.2/atms/country/{country} | 
[**xOpenBankingV22AtmsCountryCountryTownTownGet**](ATMsApi.md#xOpenBankingV22AtmsCountryCountryTownTownGet) | **GET** /x-open-banking/v2.2/atms/country/{country}/town/{town} | 
[**xOpenBankingV22AtmsGeoLocationLatLatitudeLongLongitudeGet**](ATMsApi.md#xOpenBankingV22AtmsGeoLocationLatLatitudeLongLongitudeGet) | **GET** /x-open-banking/v2.2/atms/geo-location/lat/{latitude}/long/{longitude} | 
[**xOpenBankingV22AtmsPostcodePostcodeGet**](ATMsApi.md#xOpenBankingV22AtmsPostcodePostcodeGet) | **GET** /x-open-banking/v2.2/atms/postcode/{postcode} | 



## openBankingV22AtmsGet

> ATMDefinitionMeta openBankingV22AtmsGet()



This API will return data about all our ATMs and is prepared to the Open Banking standards as defined by the Open Banking Implementation Entity (OBIE) in data dictionary version 2.2. It is regulated by the UK Competition and Markets Authority (CMA). Data is only available for the United Kingdom.

### Example

```javascript
import AtmLocatorApi from 'atm_locator_api';

let apiInstance = new AtmLocatorApi.ATMsApi();
apiInstance.openBankingV22AtmsGet((error, data, response) => {
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

[**ATMDefinitionMeta**](ATMDefinitionMeta.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/prs.openbanking.opendata.v2.2+json


## xOpenBankingV22AtmsCountryCountryGet

> ATMDefinitionMeta xOpenBankingV22AtmsCountryCountryGet(country)



This extended API will return data about all ATMs in the specified country. It is based-on the Open Banking standards as defined by the Open Banking Implementation Entity (OBIE) in data dictionary version 2.2. The extended functionality may not fully adhere to the non-functional requirements of the regulator. Data is only available for the United Kingdom.

### Example

```javascript
import AtmLocatorApi from 'atm_locator_api';

let apiInstance = new AtmLocatorApi.ATMsApi();
let country = "country_example"; // String | The ISO country code e.g. &quot;GB&quot;
apiInstance.xOpenBankingV22AtmsCountryCountryGet(country, (error, data, response) => {
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
 **country** | **String**| The ISO country code e.g. &amp;quot;GB&amp;quot; | 

### Return type

[**ATMDefinitionMeta**](ATMDefinitionMeta.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/prs.openbanking.opendata.v2.2+json


## xOpenBankingV22AtmsCountryCountryTownTownGet

> ATMDefinitionMeta xOpenBankingV22AtmsCountryCountryTownTownGet(country, town)



This extended API will return data about all ATMs in the specified town. It is based-on the Open Banking standards as defined by the Open Banking Implementation Entity (OBIE) in data dictionary version 2.2. The extended functionality may not fully adhere to the non-functional requirements of the regulator. Data is only available for the United Kingdom.

### Example

```javascript
import AtmLocatorApi from 'atm_locator_api';

let apiInstance = new AtmLocatorApi.ATMsApi();
let country = "country_example"; // String | The ISO country code e.g. &quot;GB&quot;
let town = "town_example"; // String | Town name, not case sensitive
apiInstance.xOpenBankingV22AtmsCountryCountryTownTownGet(country, town, (error, data, response) => {
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
 **country** | **String**| The ISO country code e.g. &amp;quot;GB&amp;quot; | 
 **town** | **String**| Town name, not case sensitive | 

### Return type

[**ATMDefinitionMeta**](ATMDefinitionMeta.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/prs.openbanking.opendata.v2.2+json


## xOpenBankingV22AtmsGeoLocationLatLatitudeLongLongitudeGet

> ATMDefinitionMeta xOpenBankingV22AtmsGeoLocationLatLatitudeLongLongitudeGet(latitude, longitude, radius)



This extended API will data about all ATMs within a specified radius (1 to 10 miles) of the specified latitude and longitude. It is based-on the Open Banking standards as defined by the Open Banking Implementation Entity (OBIE) in data dictionary version 2.2. The extended functionality may not fully adhere to the non-functional requirements of the regulator. Data is only available for the United Kingdom.

### Example

```javascript
import AtmLocatorApi from 'atm_locator_api';

let apiInstance = new AtmLocatorApi.ATMsApi();
let latitude = "latitude_example"; // String | Positive or negative decimal value in degrees. eg &quot;51.50551621597067&quot;
let longitude = "longitude_example"; // String | Positive or negative decimal value in degrees. eg &quot;-0.0180120225995&quot;
let radius = 3.4; // Number | Number of miles (1 to 10) as an integer. Default = 1
apiInstance.xOpenBankingV22AtmsGeoLocationLatLatitudeLongLongitudeGet(latitude, longitude, radius, (error, data, response) => {
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
 **latitude** | **String**| Positive or negative decimal value in degrees. eg &amp;quot;51.50551621597067&amp;quot; | 
 **longitude** | **String**| Positive or negative decimal value in degrees. eg &amp;quot;-0.0180120225995&amp;quot; | 
 **radius** | **Number**| Number of miles (1 to 10) as an integer. Default &#x3D; 1 | 

### Return type

[**ATMDefinitionMeta**](ATMDefinitionMeta.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/prs.openbanking.opendata.v2.2+json


## xOpenBankingV22AtmsPostcodePostcodeGet

> ATMDefinitionMeta xOpenBankingV22AtmsPostcodePostcodeGet(postcode)



This extended API will return data about all ATMs within a 5 mile radius of the specified postcode. It is based-on the Open Banking standards as defined by the Open Banking Implementation Entity (OBIE) in data dictionary version 2.2. The extended functionality may not fully adhere to the non-functional requirements of the regulator. Data is only available for the United Kingdom.

### Example

```javascript
import AtmLocatorApi from 'atm_locator_api';

let apiInstance = new AtmLocatorApi.ATMsApi();
let postcode = "postcode_example"; // String | Letters and numerals only. No spaces or special characters. eg  &quot;SW1A1AA&quot;
apiInstance.xOpenBankingV22AtmsPostcodePostcodeGet(postcode, (error, data, response) => {
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
 **postcode** | **String**| Letters and numerals only. No spaces or special characters. eg  &amp;quot;SW1A1AA&amp;quot; | 

### Return type

[**ATMDefinitionMeta**](ATMDefinitionMeta.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/prs.openbanking.opendata.v2.2+json

