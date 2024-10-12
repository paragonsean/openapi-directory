# LhPublicApi.ReferenceDataApi

All URIs are relative to *https://api.lufthansa.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**referencesAircraftByAircraftCodeGet**](ReferenceDataApi.md#referencesAircraftByAircraftCodeGet) | **GET** /references/aircraft/{aircraftCode} | Aircraft
[**referencesAirlinesByAirlineCodeGet**](ReferenceDataApi.md#referencesAirlinesByAirlineCodeGet) | **GET** /references/airlines/{airlineCode} | Airlines
[**referencesAirportsByAirportCodeGet**](ReferenceDataApi.md#referencesAirportsByAirportCodeGet) | **GET** /references/airports/{airportCode} | Airports
[**referencesAirportsNearestByLatitudeAndLongitudeGet**](ReferenceDataApi.md#referencesAirportsNearestByLatitudeAndLongitudeGet) | **GET** /references/airports/nearest/{latitude},{longitude} | Nearest Airports
[**referencesCitiesByCityCodeGet**](ReferenceDataApi.md#referencesCitiesByCityCodeGet) | **GET** /references/cities/{cityCode} | Cities
[**referencesCountriesByCountryCodeGet**](ReferenceDataApi.md#referencesCountriesByCountryCodeGet) | **GET** /references/countries/{countryCode} | Countries



## referencesAircraftByAircraftCodeGet

> Object referencesAircraftByAircraftCodeGet(accept, aircraftCode, opts)

Aircraft

List all aircraft types or one specific aircraft type.

### Example

```javascript
import LhPublicApi from 'lh_public_api';
let defaultClient = LhPublicApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: auth
let auth = defaultClient.authentications['auth'];
auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LhPublicApi.ReferenceDataApi();
let accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
let aircraftCode = "'33P'"; // String | 3-character IATA aircraft code
let opts = {
  'limit': "'20'", // String | Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken)
  'offset': "'0'" // String | Number of records skipped. Defaults to 0
};
apiInstance.referencesAircraftByAircraftCodeGet(accept, aircraftCode, opts, (error, data, response) => {
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
 **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | 
 **aircraftCode** | **String**| 3-character IATA aircraft code | [default to &#39;33P&#39;]
 **limit** | **String**| Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken) | [optional] [default to &#39;20&#39;]
 **offset** | **String**| Number of records skipped. Defaults to 0 | [optional] [default to &#39;0&#39;]

### Return type

**Object**

### Authorization

[auth](../README.md#auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## referencesAirlinesByAirlineCodeGet

> Object referencesAirlinesByAirlineCodeGet(accept, airlineCode, opts)

Airlines

List all airlines or one specific airline.

### Example

```javascript
import LhPublicApi from 'lh_public_api';
let defaultClient = LhPublicApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: auth
let auth = defaultClient.authentications['auth'];
auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LhPublicApi.ReferenceDataApi();
let accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
let airlineCode = "'LH'"; // String | 2-character IATA airline/carrier code
let opts = {
  'limit': "'20'", // String | Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken)
  'offset': "'0'" // String | Number of records skipped. Defaults to 0
};
apiInstance.referencesAirlinesByAirlineCodeGet(accept, airlineCode, opts, (error, data, response) => {
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
 **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | 
 **airlineCode** | **String**| 2-character IATA airline/carrier code | [default to &#39;LH&#39;]
 **limit** | **String**| Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken) | [optional] [default to &#39;20&#39;]
 **offset** | **String**| Number of records skipped. Defaults to 0 | [optional] [default to &#39;0&#39;]

### Return type

**Object**

### Authorization

[auth](../README.md#auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## referencesAirportsByAirportCodeGet

> AirportResponse referencesAirportsByAirportCodeGet(accept, airportCode, opts)

Airports

List all airports or one specific airport. All airports response is very large. It is possible to request the response in a specific language.

### Example

```javascript
import LhPublicApi from 'lh_public_api';
let defaultClient = LhPublicApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: auth
let auth = defaultClient.authentications['auth'];
auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LhPublicApi.ReferenceDataApi();
let accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
let airportCode = "'TXL'"; // String | 3-letter IATA airport code
let opts = {
  'lang': "lang_example", // String | 2-letter ISO 3166-1 language code
  'limit': "'20'", // String | Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken)
  'offset': "'0'", // String | Number of records skipped. Defaults to 0
  'lHoperated': true // Boolean | Restrict the results to locations with flights operated by LH (false=0, true=1)
};
apiInstance.referencesAirportsByAirportCodeGet(accept, airportCode, opts, (error, data, response) => {
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
 **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | 
 **airportCode** | **String**| 3-letter IATA airport code | [default to &#39;TXL&#39;]
 **lang** | **String**| 2-letter ISO 3166-1 language code | [optional] 
 **limit** | **String**| Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken) | [optional] [default to &#39;20&#39;]
 **offset** | **String**| Number of records skipped. Defaults to 0 | [optional] [default to &#39;0&#39;]
 **lHoperated** | **Boolean**| Restrict the results to locations with flights operated by LH (false&#x3D;0, true&#x3D;1) | [optional] 

### Return type

[**AirportResponse**](AirportResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## referencesAirportsNearestByLatitudeAndLongitudeGet

> Object referencesAirportsNearestByLatitudeAndLongitudeGet(latitude, longitude, accept, opts)

Nearest Airports

List the 5 closest airports to the given latitude and longitude, irrespective of the radius of the reference point.

### Example

```javascript
import LhPublicApi from 'lh_public_api';
let defaultClient = LhPublicApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: auth
let auth = defaultClient.authentications['auth'];
auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LhPublicApi.ReferenceDataApi();
let latitude = 56; // Number | Latitude in decimal format to at most 3 decimal places
let longitude = 56; // Number | Longitude in decimal format to at most 3 decimal places
let accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
let opts = {
  'lang': "lang_example" // String | 2 letter ISO 3166-1 language code
};
apiInstance.referencesAirportsNearestByLatitudeAndLongitudeGet(latitude, longitude, accept, opts, (error, data, response) => {
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
 **latitude** | **Number**| Latitude in decimal format to at most 3 decimal places | 
 **longitude** | **Number**| Longitude in decimal format to at most 3 decimal places | 
 **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | 
 **lang** | **String**| 2 letter ISO 3166-1 language code | [optional] 

### Return type

**Object**

### Authorization

[auth](../README.md#auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## referencesCitiesByCityCodeGet

> Object referencesCitiesByCityCodeGet(accept, cityCode, opts)

Cities

List all cities or one specific city. It is possible to request the response in a specific language.

### Example

```javascript
import LhPublicApi from 'lh_public_api';
let defaultClient = LhPublicApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: auth
let auth = defaultClient.authentications['auth'];
auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LhPublicApi.ReferenceDataApi();
let accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
let cityCode = "'BER'"; // String | 3-letter IATA city code
let opts = {
  'lang': "lang_example", // String | 2 letter ISO 3166-1 language code
  'limit': "'20'", // String | Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken)
  'offset': "'0'" // String | Number of records skipped. Defaults to 0
};
apiInstance.referencesCitiesByCityCodeGet(accept, cityCode, opts, (error, data, response) => {
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
 **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | 
 **cityCode** | **String**| 3-letter IATA city code | [default to &#39;BER&#39;]
 **lang** | **String**| 2 letter ISO 3166-1 language code | [optional] 
 **limit** | **String**| Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken) | [optional] [default to &#39;20&#39;]
 **offset** | **String**| Number of records skipped. Defaults to 0 | [optional] [default to &#39;0&#39;]

### Return type

**Object**

### Authorization

[auth](../README.md#auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## referencesCountriesByCountryCodeGet

> Object referencesCountriesByCountryCodeGet(accept, countryCode, opts)

Countries

List all countries or one specific country. It is possible to request the response in a specific language.

### Example

```javascript
import LhPublicApi from 'lh_public_api';
let defaultClient = LhPublicApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: auth
let auth = defaultClient.authentications['auth'];
auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LhPublicApi.ReferenceDataApi();
let accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
let countryCode = "'DK'"; // String | 2-letter ISO 3166-1 country code
let opts = {
  'lang': "lang_example", // String | 2 letter ISO 3166-1 language code
  'limit': "'20'", // String | Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken)
  'offset': "'0'" // String | Number of records skipped. Defaults to 0
};
apiInstance.referencesCountriesByCountryCodeGet(accept, countryCode, opts, (error, data, response) => {
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
 **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | 
 **countryCode** | **String**| 2-letter ISO 3166-1 country code | [default to &#39;DK&#39;]
 **lang** | **String**| 2 letter ISO 3166-1 language code | [optional] 
 **limit** | **String**| Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken) | [optional] [default to &#39;20&#39;]
 **offset** | **String**| Number of records skipped. Defaults to 0 | [optional] [default to &#39;0&#39;]

### Return type

**Object**

### Authorization

[auth](../README.md#auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

