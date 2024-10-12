# LhPublicApi.OffersApi

All URIs are relative to *https://api.lufthansa.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**offersLoungesByLocationGet**](OffersApi.md#offersLoungesByLocationGet) | **GET** /offers/lounges/{location} | Lounges
[**offersSeatmapsDestinationDateCabinClassByFlightNumberAndOriginGet**](OffersApi.md#offersSeatmapsDestinationDateCabinClassByFlightNumberAndOriginGet) | **GET** /offers/seatmaps/{flightNumber}/{origin}/{destination}/{date}/{cabinClass} | Seat Maps



## offersLoungesByLocationGet

> Object offersLoungesByLocationGet(location, accept, opts)

Lounges

Lounge information

### Example

```javascript
import LhPublicApi from 'lh_public_api';
let defaultClient = LhPublicApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: auth
let auth = defaultClient.authentications['auth'];
auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LhPublicApi.OffersApi();
let location = "location_example"; // String | 3-leter IATA airport or city code (e.g. 'ZRH')
let accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
let opts = {
  'cabinClass': "cabinClass_example", // String | Cabin class: 'M', 'E', 'C', 'F' (Acceptable values are: \"\", \"M\", \"E\", \"C\", \"F\")
  'tierCode': "tierCode_example", // String | Frequent flyer level ('FTL', 'SGC', 'SEN', 'HON') (Acceptable values are: \"\", \"FTL\", \"SGC\", \"SEN\", \"HON\")
  'lang': "lang_example" // String | Language code.
};
apiInstance.offersLoungesByLocationGet(location, accept, opts, (error, data, response) => {
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
 **location** | **String**| 3-leter IATA airport or city code (e.g. &#39;ZRH&#39;) | 
 **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | 
 **cabinClass** | **String**| Cabin class: &#39;M&#39;, &#39;E&#39;, &#39;C&#39;, &#39;F&#39; (Acceptable values are: \&quot;\&quot;, \&quot;M\&quot;, \&quot;E\&quot;, \&quot;C\&quot;, \&quot;F\&quot;) | [optional] 
 **tierCode** | **String**| Frequent flyer level (&#39;FTL&#39;, &#39;SGC&#39;, &#39;SEN&#39;, &#39;HON&#39;) (Acceptable values are: \&quot;\&quot;, \&quot;FTL\&quot;, \&quot;SGC\&quot;, \&quot;SEN\&quot;, \&quot;HON\&quot;) | [optional] 
 **lang** | **String**| Language code. | [optional] 

### Return type

**Object**

### Authorization

[auth](../README.md#auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## offersSeatmapsDestinationDateCabinClassByFlightNumberAndOriginGet

> Object offersSeatmapsDestinationDateCabinClassByFlightNumberAndOriginGet(flightNumber, origin, destination, date, cabinClass, accept)

Seat Maps

Cabin layout and seat characteristics.

### Example

```javascript
import LhPublicApi from 'lh_public_api';
let defaultClient = LhPublicApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: auth
let auth = defaultClient.authentications['auth'];
auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LhPublicApi.OffersApi();
let flightNumber = "flightNumber_example"; // String | Flight number including carrier code and any suffix (e.g. 'LH2037')
let origin = "origin_example"; // String | Departure airport. 3-letter IATA airport code (e.g. 'TXL')
let destination = "destination_example"; // String | Destination airport. 3-letter IATA airport code (e.g. 'MUC')
let date = "date_example"; // String | Departure date (YYYY-MM-DD)
let cabinClass = "cabinClass_example"; // String | Cabin class: 'M', 'E', 'C', 'F'. Some flights have fewer classes (Acceptable values are: \"M\", \"E\", \"C\", \"F\")
let accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
apiInstance.offersSeatmapsDestinationDateCabinClassByFlightNumberAndOriginGet(flightNumber, origin, destination, date, cabinClass, accept, (error, data, response) => {
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
 **flightNumber** | **String**| Flight number including carrier code and any suffix (e.g. &#39;LH2037&#39;) | 
 **origin** | **String**| Departure airport. 3-letter IATA airport code (e.g. &#39;TXL&#39;) | 
 **destination** | **String**| Destination airport. 3-letter IATA airport code (e.g. &#39;MUC&#39;) | 
 **date** | **String**| Departure date (YYYY-MM-DD) | 
 **cabinClass** | **String**| Cabin class: &#39;M&#39;, &#39;E&#39;, &#39;C&#39;, &#39;F&#39;. Some flights have fewer classes (Acceptable values are: \&quot;M\&quot;, \&quot;E\&quot;, \&quot;C\&quot;, \&quot;F\&quot;) | 
 **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | 

### Return type

**Object**

### Authorization

[auth](../README.md#auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

