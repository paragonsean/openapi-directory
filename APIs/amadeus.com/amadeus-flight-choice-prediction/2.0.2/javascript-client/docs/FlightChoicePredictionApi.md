# FlightChoicePrediction.FlightChoicePredictionApi

All URIs are relative to *https://test.api.amadeus.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getFlightChoicePredict**](FlightChoicePredictionApi.md#getFlightChoicePredict) | **POST** /shopping/flight-offers/prediction | Predict the choice of flight offers.



## getFlightChoicePredict

> Success getFlightChoicePredict(xHTTPMethodOverride, body)

Predict the choice of flight offers.

### Example

```javascript
import FlightChoicePrediction from 'flight_choice_prediction';

let apiInstance = new FlightChoicePrediction.FlightChoicePredictionApi();
let xHTTPMethodOverride = "'GET'"; // String | the HTTP method to apply
let body = new FlightChoicePrediction.FlightOffersSearchReply(); // FlightOffersSearchReply | 
apiInstance.getFlightChoicePredict(xHTTPMethodOverride, body, (error, data, response) => {
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
 **body** | [**FlightOffersSearchReply**](FlightOffersSearchReply.md)|  | 

### Return type

[**Success**](Success.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/vnd.amadeus+json, application/json
- **Accept**: application/vnd.amadeus+json, application/json

