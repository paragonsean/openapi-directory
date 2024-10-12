# TripPurposePrediction.TripPurposePredictionApi

All URIs are relative to *https://test.api.amadeus.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getTripPurposePrediction**](TripPurposePredictionApi.md#getTripPurposePrediction) | **GET** /travel/predictions/trip-purpose | Returns the forecast purpose of a trip



## getTripPurposePrediction

> Prediction getTripPurposePrediction(originLocationCode, destinationLocationCode, departureDate, returnDate, opts)

Returns the forecast purpose of a trip

### Example

```javascript
import TripPurposePrediction from 'trip_purpose_prediction';

let apiInstance = new TripPurposePrediction.TripPurposePredictionApi();
let originLocationCode = "NYC"; // String | city/airport [IATA code](http://www.iata.org/publications/Pages/code-search.aspx) from which the traveler will depart, e.g. BOS for Boston
let destinationLocationCode = "MAD"; // String | city/airport [IATA code](http://www.iata.org/publications/Pages/code-search.aspx) to which the traveler is going, e.g. PAR for Paris
let departureDate = "2023-12-01"; // String | the date on which the traveler will depart from the origin to go to the destination. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2017-12-25
let returnDate = "2023-12-12"; // String | the date on which the traveler will depart from the destination to return to the origin. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2018-02-28
let opts = {
  'searchDate': "searchDate_example" // String | the date on which the traveler is performing the search. If this parameter is not specified, current date will be used. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2018-02-28
};
apiInstance.getTripPurposePrediction(originLocationCode, destinationLocationCode, departureDate, returnDate, opts, (error, data, response) => {
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
 **departureDate** | **String**| the date on which the traveler will depart from the origin to go to the destination. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2017-12-25 | 
 **returnDate** | **String**| the date on which the traveler will depart from the destination to return to the origin. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2018-02-28 | 
 **searchDate** | **String**| the date on which the traveler is performing the search. If this parameter is not specified, current date will be used. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2018-02-28 | [optional] 

### Return type

[**Prediction**](Prediction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.amadeus+json

