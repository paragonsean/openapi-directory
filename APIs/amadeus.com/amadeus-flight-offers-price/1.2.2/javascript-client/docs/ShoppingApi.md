# FlightOffersPrice.ShoppingApi

All URIs are relative to *https://test.api.amadeus.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quoteAirOffers**](ShoppingApi.md#quoteAirOffers) | **POST** /shopping/flight-offers/pricing | Confirm pricing of given flightOffers.



## quoteAirOffers

> SuccessPricing quoteAirOffers(xHTTPMethodOverride, priceFlightOffersBody, opts)

Confirm pricing of given flightOffers.

### Example

```javascript
import FlightOffersPrice from 'flight_offers_price';

let apiInstance = new FlightOffersPrice.ShoppingApi();
let xHTTPMethodOverride = "'GET'"; // String | the HTTP method to apply
let priceFlightOffersBody = new FlightOffersPrice.GetPriceQuery(); // GetPriceQuery | list of criteria to confirm the price of a dedicated flight-offers
let opts = {
  'include': ["null"], // [String] | Sub-resources to be included:  * **credit-card-fees** to get the credit card fee applied on the booking  * **bags** to get extra bag options  * **other-services** to get services options  * **detailed-fare-rules** to get detailed fare rules options 
  'forceClass': false // Boolean | parameter to force the usage of booking class for pricing - **true**, to for pricing with the specified booking class - **false**, to get the best available price 
};
apiInstance.quoteAirOffers(xHTTPMethodOverride, priceFlightOffersBody, opts, (error, data, response) => {
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
 **priceFlightOffersBody** | [**GetPriceQuery**](GetPriceQuery.md)| list of criteria to confirm the price of a dedicated flight-offers | 
 **include** | [**[String]**](String.md)| Sub-resources to be included:  * **credit-card-fees** to get the credit card fee applied on the booking  * **bags** to get extra bag options  * **other-services** to get services options  * **detailed-fare-rules** to get detailed fare rules options  | [optional] 
 **forceClass** | **Boolean**| parameter to force the usage of booking class for pricing - **true**, to for pricing with the specified booking class - **false**, to get the best available price  | [optional] [default to false]

### Return type

[**SuccessPricing**](SuccessPricing.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/vnd.amadeus+json
- **Accept**: application/vnd.amadeus+json

