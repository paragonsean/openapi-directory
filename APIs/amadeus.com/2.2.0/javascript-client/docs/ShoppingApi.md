# FlightOffersSearch.ShoppingApi

All URIs are relative to *https://test.api.amadeus.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getFlightOffers**](ShoppingApi.md#getFlightOffers) | **GET** /shopping/flight-offers | Return list of Flight Offers based on searching criteria.
[**searchFlightOffers**](ShoppingApi.md#searchFlightOffers) | **POST** /shopping/flight-offers | Return list of Flight Offers based on posted searching criteria.



## getFlightOffers

> Success getFlightOffers(originLocationCode, destinationLocationCode, departureDate, adults, opts)

Return list of Flight Offers based on searching criteria.



### Example

```javascript
import FlightOffersSearch from 'flight_offers_search';

let apiInstance = new FlightOffersSearch.ShoppingApi();
let originLocationCode = "SYD"; // String | city/airport [IATA code](http://www.iata.org/publications/Pages/code-search.aspx) from which the traveler will depart, e.g. BOS for Boston
let destinationLocationCode = "BKK"; // String | city/airport [IATA code](http://www.iata.org/publications/Pages/code-search.aspx) to which the traveler is going, e.g. PAR for Paris
let departureDate = new Date("2021-02-01"); // Date | the date on which the traveler will depart from the origin to go to the destination. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2017-12-25
let adults = 1; // Number | the number of adult travelers (age 12 or older on date of departure).
let opts = {
  'returnDate': new Date("2013-10-20"), // Date | the date on which the traveler will depart from the destination to return to the origin. If this parameter is not specified, only one-way itineraries are found. If this parameter is specified, only round-trip itineraries are found. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2018-02-28
  'children': 56, // Number | the number of child travelers (older than age 2 and younger than age 12 on date of departure) who will each have their own separate seat. If specified, this number should be greater than or equal to 0
  'infants': 56, // Number | the number of infant travelers (whose age is less or equal to 2 on date of departure). Infants travel on the lap of an adult traveler, and thus the number of infants must not exceed the number of adults. If specified, this number should be greater than or equal to 0
  'travelClass': "travelClass_example", // String | most of the flight time should be spent in a cabin of this quality or higher. The accepted travel class is economy, premium economy, business or first class. If no travel class is specified, the search considers any travel class
  'includedAirlineCodes': "includedAirlineCodes_example", // String | This option ensures that the system will only consider these airlines. This can not be cumulated with parameter excludedAirlineCodes.  Airlines are specified as [IATA airline codes](http://www.iata.org/publications/Pages/code-search.aspx) and are comma-separated, e.g. 6X,7X,8X 
  'excludedAirlineCodes': "excludedAirlineCodes_example", // String | This option ensures that the system will ignore these airlines. This can not be cumulated with parameter includedAirlineCodes.  Airlines are specified as [IATA airline codes](http://www.iata.org/publications/Pages/code-search.aspx) and are comma-separated, e.g. 6X,7X,8X 
  'nonStop': false, // Boolean | if set to true, the search will find only flights going from the origin to the destination with no stop in between
  'currencyCode': "currencyCode_example", // String | the preferred currency for the flight offers. Currency is specified in the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) format, e.g. EUR for Euro
  'maxPrice': 56, // Number | maximum price per traveler. By default, no limit is applied. If specified, the value should be a positive number with no decimals
  'max': 250 // Number | maximum number of flight offers to return. If specified, the value should be greater than or equal to 1
};
apiInstance.getFlightOffers(originLocationCode, destinationLocationCode, departureDate, adults, opts, (error, data, response) => {
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
 **originLocationCode** | **String**| city/airport [IATA code](http://www.iata.org/publications/Pages/code-search.aspx) from which the traveler will depart, e.g. BOS for Boston | 
 **destinationLocationCode** | **String**| city/airport [IATA code](http://www.iata.org/publications/Pages/code-search.aspx) to which the traveler is going, e.g. PAR for Paris | 
 **departureDate** | **Date**| the date on which the traveler will depart from the origin to go to the destination. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2017-12-25 | 
 **adults** | **Number**| the number of adult travelers (age 12 or older on date of departure). | [default to 1]
 **returnDate** | **Date**| the date on which the traveler will depart from the destination to return to the origin. If this parameter is not specified, only one-way itineraries are found. If this parameter is specified, only round-trip itineraries are found. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2018-02-28 | [optional] 
 **children** | **Number**| the number of child travelers (older than age 2 and younger than age 12 on date of departure) who will each have their own separate seat. If specified, this number should be greater than or equal to 0 | [optional] 
 **infants** | **Number**| the number of infant travelers (whose age is less or equal to 2 on date of departure). Infants travel on the lap of an adult traveler, and thus the number of infants must not exceed the number of adults. If specified, this number should be greater than or equal to 0 | [optional] 
 **travelClass** | **String**| most of the flight time should be spent in a cabin of this quality or higher. The accepted travel class is economy, premium economy, business or first class. If no travel class is specified, the search considers any travel class | [optional] 
 **includedAirlineCodes** | **String**| This option ensures that the system will only consider these airlines. This can not be cumulated with parameter excludedAirlineCodes.  Airlines are specified as [IATA airline codes](http://www.iata.org/publications/Pages/code-search.aspx) and are comma-separated, e.g. 6X,7X,8X  | [optional] 
 **excludedAirlineCodes** | **String**| This option ensures that the system will ignore these airlines. This can not be cumulated with parameter includedAirlineCodes.  Airlines are specified as [IATA airline codes](http://www.iata.org/publications/Pages/code-search.aspx) and are comma-separated, e.g. 6X,7X,8X  | [optional] 
 **nonStop** | **Boolean**| if set to true, the search will find only flights going from the origin to the destination with no stop in between | [optional] [default to false]
 **currencyCode** | **String**| the preferred currency for the flight offers. Currency is specified in the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) format, e.g. EUR for Euro | [optional] 
 **maxPrice** | **Number**| maximum price per traveler. By default, no limit is applied. If specified, the value should be a positive number with no decimals | [optional] 
 **max** | **Number**| maximum number of flight offers to return. If specified, the value should be greater than or equal to 1 | [optional] [default to 250]

### Return type

[**Success**](Success.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.amadeus+json


## searchFlightOffers

> Success1 searchFlightOffers(xHTTPMethodOverride, getFlightOffersQuery)

Return list of Flight Offers based on posted searching criteria.



### Example

```javascript
import FlightOffersSearch from 'flight_offers_search';

let apiInstance = new FlightOffersSearch.ShoppingApi();
let xHTTPMethodOverride = "'GET'"; // String | the HTTP method to apply
let getFlightOffersQuery = new FlightOffersSearch.GetFlightOffersQuery(); // GetFlightOffersQuery | list of criteria to retrieve a list of flight offers
apiInstance.searchFlightOffers(xHTTPMethodOverride, getFlightOffersQuery, (error, data, response) => {
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
 **xHTTPMethodOverride** | **String**| the HTTP method to apply | [default to &#39;GET&#39;]
 **getFlightOffersQuery** | [**GetFlightOffersQuery**](GetFlightOffersQuery.md)| list of criteria to retrieve a list of flight offers | 

### Return type

[**Success1**](Success1.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/vnd.amadeus+json
- **Accept**: application/vnd.amadeus+json

