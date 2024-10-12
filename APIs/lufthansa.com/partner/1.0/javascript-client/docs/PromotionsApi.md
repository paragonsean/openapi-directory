# LhPartnerApi.PromotionsApi

All URIs are relative to *https://api.lufthansa.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**priceOffers**](PromotionsApi.md#priceOffers) | **GET** /promotions/priceoffers/flights/ond/{origin}/{destination} | Price Offers



## priceOffers

> String priceOffers(origin, destination, departureDate, returnDate, opts)

Price Offers

Retrieve a best price offer given an origin and destination.

### Example

```javascript
import LhPartnerApi from 'lh_partner_api';
let defaultClient = LhPartnerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: auth
let auth = defaultClient.authentications['auth'];
auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LhPartnerApi.PromotionsApi();
let origin = "origin_example"; // String | Departure city. 3-letter IATA city code
let destination = "destination_example"; // String | Destination city. 3-letter IATA city code
let departureDate = "departureDate_example"; // String | Departure date in local time (YYYY-MM-DD)
let returnDate = "returnDate_example"; // String | Return date in local time (YYYY-MM-DD)
let opts = {
  'service': "'amadeusBestPrice'" // String | Optional parameter.
};
apiInstance.priceOffers(origin, destination, departureDate, returnDate, opts, (error, data, response) => {
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
 **origin** | **String**| Departure city. 3-letter IATA city code | 
 **destination** | **String**| Destination city. 3-letter IATA city code | 
 **departureDate** | **String**| Departure date in local time (YYYY-MM-DD) | 
 **returnDate** | **String**| Return date in local time (YYYY-MM-DD) | 
 **service** | **String**| Optional parameter. | [optional] [default to &#39;amadeusBestPrice&#39;]

### Return type

**String**

### Authorization

[auth](../README.md#auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

