# OnDemandFlightStatus.FlightsApi

All URIs are relative to *https://test.api.amadeus.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getFlightsStatus**](FlightsApi.md#getFlightsStatus) | **GET** /schedule/flights | Retrieves a unique flight by search criteria.



## getFlightsStatus

> SuccessFlights getFlightsStatus(carrierCode, flightNumber, scheduledDepartureDate, opts)

Retrieves a unique flight by search criteria.

### Example

```javascript
import OnDemandFlightStatus from 'on_demand_flight_status';

let apiInstance = new OnDemandFlightStatus.FlightsApi();
let carrierCode = "TP"; // String | 2 to 3-character IATA carrier code ([IATA table codes](http://www.iata.org/publications/Pages/code-search.aspx)). 
let flightNumber = "487"; // String | 1 to 4-digit number of the flight. e.g. 4537
let scheduledDepartureDate = new Date("2023-08-01"); // Date | scheduled departure date of the flight, local to the departure airport, format YYYY-MM-DD.
let opts = {
  'operationalSuffix': "operationalSuffix_example" // String | 1-letter operational suffix assigned by the carrier to differentiate flight in case of delay changing the departure date e.g. A 
};
apiInstance.getFlightsStatus(carrierCode, flightNumber, scheduledDepartureDate, opts, (error, data, response) => {
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
 **carrierCode** | **String**| 2 to 3-character IATA carrier code ([IATA table codes](http://www.iata.org/publications/Pages/code-search.aspx)).  | 
 **flightNumber** | **String**| 1 to 4-digit number of the flight. e.g. 4537 | 
 **scheduledDepartureDate** | **Date**| scheduled departure date of the flight, local to the departure airport, format YYYY-MM-DD. | 
 **operationalSuffix** | **String**| 1-letter operational suffix assigned by the carrier to differentiate flight in case of delay changing the departure date e.g. A  | [optional] 

### Return type

[**SuccessFlights**](SuccessFlights.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.amadeus+json

