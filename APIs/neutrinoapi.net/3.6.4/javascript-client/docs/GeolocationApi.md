# NeutrinoApi.GeolocationApi

All URIs are relative to *https://neutrinoapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**geocodeAddress**](GeolocationApi.md#geocodeAddress) | **GET** /geocode-address | Geocode Address
[**geocodeReverse**](GeolocationApi.md#geocodeReverse) | **GET** /geocode-reverse | Geocode Reverse
[**iPInfo**](GeolocationApi.md#iPInfo) | **GET** /ip-info | IP Info



## geocodeAddress

> GeocodeAddressResponse geocodeAddress(opts)

Geocode Address

Geocode an address, partial address or just the name of a place

### Example

```javascript
import NeutrinoApi from 'neutrino_api';
let defaultClient = NeutrinoApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: user-id
let user-id = defaultClient.authentications['user-id'];
user-id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user-id.apiKeyPrefix = 'Token';

let apiInstance = new NeutrinoApi.GeolocationApi();
let opts = {
  'address': "address_example", // String | The full address, partial address or name of a place to try and locate. Comma separated address components are preferred.
  'houseNumber': "houseNumber_example", // String | The house/building number to locate
  'street': "street_example", // String | The street/road name to locate
  'city': "city_example", // String | The city/town name to locate
  'county': "county_example", // String | The county/region name to locate
  'state': "state_example", // String | The state name to locate
  'postalCode': "postalCode_example", // String | The postal code to locate
  'countryCode': "countryCode_example", // String | Limit result to this country (the default is no country bias)
  'languageCode': "'en'", // String | The language to display results in, available languages are: <ul> <li>de, en, es, fr, it, pt, ru, zh</li> </ul>
  'fuzzySearch': false // Boolean | If no matches are found for the given address, start performing a recursive fuzzy search until a geolocation is found. This option is recommended for processing user input or implementing auto-complete. We use a combination of approximate string matching and data cleansing to find possible location matches
};
apiInstance.geocodeAddress(opts, (error, data, response) => {
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
 **address** | **String**| The full address, partial address or name of a place to try and locate. Comma separated address components are preferred. | [optional] 
 **houseNumber** | **String**| The house/building number to locate | [optional] 
 **street** | **String**| The street/road name to locate | [optional] 
 **city** | **String**| The city/town name to locate | [optional] 
 **county** | **String**| The county/region name to locate | [optional] 
 **state** | **String**| The state name to locate | [optional] 
 **postalCode** | **String**| The postal code to locate | [optional] 
 **countryCode** | **String**| Limit result to this country (the default is no country bias) | [optional] 
 **languageCode** | **String**| The language to display results in, available languages are: &lt;ul&gt; &lt;li&gt;de, en, es, fr, it, pt, ru, zh&lt;/li&gt; &lt;/ul&gt; | [optional] [default to &#39;en&#39;]
 **fuzzySearch** | **Boolean**| If no matches are found for the given address, start performing a recursive fuzzy search until a geolocation is found. This option is recommended for processing user input or implementing auto-complete. We use a combination of approximate string matching and data cleansing to find possible location matches | [optional] [default to false]

### Return type

[**GeocodeAddressResponse**](GeocodeAddressResponse.md)

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## geocodeReverse

> GeocodeReverseResponse geocodeReverse(latitude, longitude, opts)

Geocode Reverse

Convert a geographic coordinate (latitude and longitude) into a real world address

### Example

```javascript
import NeutrinoApi from 'neutrino_api';
let defaultClient = NeutrinoApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: user-id
let user-id = defaultClient.authentications['user-id'];
user-id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user-id.apiKeyPrefix = 'Token';

let apiInstance = new NeutrinoApi.GeolocationApi();
let latitude = "latitude_example"; // String | The location latitude in decimal degrees format
let longitude = "longitude_example"; // String | The location longitude in decimal degrees format
let opts = {
  'languageCode': "'en'", // String | The language to display results in, available languages are: <ul> <li>de, en, es, fr, it, pt, ru</li> </ul>
  'zoom': "'address'" // String | The zoom level to respond with: <br> <ul> <li>address - the most precise address available</li> <li>street - the street level</li> <li>city - the city level</li> <li>state - the state level</li> <li>country - the country level</li> </ul>
};
apiInstance.geocodeReverse(latitude, longitude, opts, (error, data, response) => {
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
 **latitude** | **String**| The location latitude in decimal degrees format | 
 **longitude** | **String**| The location longitude in decimal degrees format | 
 **languageCode** | **String**| The language to display results in, available languages are: &lt;ul&gt; &lt;li&gt;de, en, es, fr, it, pt, ru&lt;/li&gt; &lt;/ul&gt; | [optional] [default to &#39;en&#39;]
 **zoom** | **String**| The zoom level to respond with: &lt;br&gt; &lt;ul&gt; &lt;li&gt;address - the most precise address available&lt;/li&gt; &lt;li&gt;street - the street level&lt;/li&gt; &lt;li&gt;city - the city level&lt;/li&gt; &lt;li&gt;state - the state level&lt;/li&gt; &lt;li&gt;country - the country level&lt;/li&gt; &lt;/ul&gt; | [optional] [default to &#39;address&#39;]

### Return type

[**GeocodeReverseResponse**](GeocodeReverseResponse.md)

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## iPInfo

> IPInfoResponse iPInfo(ip, opts)

IP Info

Get location information about an IP address and do reverse DNS (PTR) lookups

### Example

```javascript
import NeutrinoApi from 'neutrino_api';
let defaultClient = NeutrinoApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: user-id
let user-id = defaultClient.authentications['user-id'];
user-id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user-id.apiKeyPrefix = 'Token';

let apiInstance = new NeutrinoApi.GeolocationApi();
let ip = "ip_example"; // String | IPv4 or IPv6 address
let opts = {
  'reverseLookup': false // Boolean | Do a reverse DNS (PTR) lookup. This option can add extra delay to the request so only use it if you need it
};
apiInstance.iPInfo(ip, opts, (error, data, response) => {
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
 **ip** | **String**| IPv4 or IPv6 address | 
 **reverseLookup** | **Boolean**| Do a reverse DNS (PTR) lookup. This option can add extra delay to the request so only use it if you need it | [optional] [default to false]

### Return type

[**IPInfoResponse**](IPInfoResponse.md)

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

