# BrandedFaresUpsell.ShoppingApi

All URIs are relative to *https://test.api.amadeus.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**upsellAirOffers**](ShoppingApi.md#upsellAirOffers) | **POST** /shopping/flight-offers/upselling | Return a list of upsell Flight Offers based on given Flight Offers



## upsellAirOffers

> SuccessUpsell upsellAirOffers(xHTTPMethodOverride, upsellFlightOffersBody)

Return a list of upsell Flight Offers based on given Flight Offers

### Example

```javascript
import BrandedFaresUpsell from 'branded_fares_upsell';

let apiInstance = new BrandedFaresUpsell.ShoppingApi();
let xHTTPMethodOverride = "'GET'"; // String | the HTTP method to apply
let upsellFlightOffersBody = new BrandedFaresUpsell.GetUpsellQuery(); // GetUpsellQuery | list of criteria to upsell a dedicated flight-offers
apiInstance.upsellAirOffers(xHTTPMethodOverride, upsellFlightOffersBody, (error, data, response) => {
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
 **upsellFlightOffersBody** | [**GetUpsellQuery**](GetUpsellQuery.md)| list of criteria to upsell a dedicated flight-offers | 

### Return type

[**SuccessUpsell**](SuccessUpsell.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/vnd.amadeus+json
- **Accept**: application/vnd.amadeus+json

