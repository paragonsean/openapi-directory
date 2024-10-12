# FlightDelayPrediction.FlightDelayPredictionApi

All URIs are relative to *https://test.api.amadeus.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getFlightDelayPrediction**](FlightDelayPredictionApi.md#getFlightDelayPrediction) | **GET** /travel/predictions/flight-delay | Return the delay segment where the flight is likely to lay.



## getFlightDelayPrediction

> Prediction getFlightDelayPrediction(originLocationCode, destinationLocationCode, departureDate, departureTime, arrivalDate, arrivalTime, aircraftCode, carrierCode, flightNumber, duration)

Return the delay segment where the flight is likely to lay.

### Example

```javascript
import FlightDelayPrediction from 'flight_delay_prediction';

let apiInstance = new FlightDelayPrediction.FlightDelayPredictionApi();
let originLocationCode = "NCE"; // String | city/airport [IATA code](http://www.iata.org/publications/Pages/code-search.aspx) from which the traveler is departing, e.g. PAR for Paris
let destinationLocationCode = "IST"; // String | city/airport [IATA code](http://www.iata.org/publications/Pages/code-search.aspx) to which the traveler is going, e.g. PAR for Paris
let departureDate = new Date("2020-08-01"); // Date | the date on which the traveler will depart from the origin to go to the destination. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2019-12-25
let departureTime = "66000"; // String | local time relative to originLocationCode on which the traveler will depart from the origin. Time respects ISO 8601 standard. e.g. 13:22:00
let arrivalDate = new Date("2020-08-01"); // Date | the date on which the traveler will arrive to the destination from the origin. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2019-12-25
let arrivalTime = "80100"; // String | local time relative to destinationLocationCode on which the traveler will arrive to destination. Time respects ISO 8601 standard. e.g. 13:22:00
let aircraftCode = "321"; // String | IATA aircraft code (http://www.flugzeuginfo.net/table_accodes_iata_en.php)
let carrierCode = "TK"; // String | airline / carrier code
let flightNumber = "1816"; // String | flight number as assigned by the carrier
let duration = "PT31H10M"; // String | flight duration in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) PnYnMnDTnHnMnS format, e.g. PT2H10M
apiInstance.getFlightDelayPrediction(originLocationCode, destinationLocationCode, departureDate, departureTime, arrivalDate, arrivalTime, aircraftCode, carrierCode, flightNumber, duration, (error, data, response) => {
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
 **originLocationCode** | **String**| city/airport [IATA code](http://www.iata.org/publications/Pages/code-search.aspx) from which the traveler is departing, e.g. PAR for Paris | 
 **destinationLocationCode** | **String**| city/airport [IATA code](http://www.iata.org/publications/Pages/code-search.aspx) to which the traveler is going, e.g. PAR for Paris | 
 **departureDate** | **Date**| the date on which the traveler will depart from the origin to go to the destination. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2019-12-25 | 
 **departureTime** | **String**| local time relative to originLocationCode on which the traveler will depart from the origin. Time respects ISO 8601 standard. e.g. 13:22:00 | 
 **arrivalDate** | **Date**| the date on which the traveler will arrive to the destination from the origin. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2019-12-25 | 
 **arrivalTime** | **String**| local time relative to destinationLocationCode on which the traveler will arrive to destination. Time respects ISO 8601 standard. e.g. 13:22:00 | 
 **aircraftCode** | **String**| IATA aircraft code (http://www.flugzeuginfo.net/table_accodes_iata_en.php) | 
 **carrierCode** | **String**| airline / carrier code | 
 **flightNumber** | **String**| flight number as assigned by the carrier | 
 **duration** | **String**| flight duration in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) PnYnMnDTnHnMnS format, e.g. PT2H10M | 

### Return type

[**Prediction**](Prediction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.amadeus+json, application/json

