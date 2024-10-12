# HotelSearchApi.ShoppingApi

All URIs are relative to *https://test.api.amadeus.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getMultiHotelOffers**](ShoppingApi.md#getMultiHotelOffers) | **GET** /shopping/hotel-offers | getMultiHotelOffers
[**getOfferPricing**](ShoppingApi.md#getOfferPricing) | **GET** /shopping/hotel-offers/{offerId} | getOfferPricing



## getMultiHotelOffers

> MultiResponse getMultiHotelOffers(hotelIds, opts)

getMultiHotelOffers

### Example

```javascript
import HotelSearchApi from 'hotel_search_api';

let apiInstance = new HotelSearchApi.ShoppingApi();
let hotelIds = ["null"]; // [String] | Amadeus property codes on 8 chars. Mandatory parameter for a search by predefined list of hotels.
let opts = {
  'adults': 1, // Number | Number of adult guests (1-9) per room.
  'checkInDate': new Date("2023-11-22"), // Date | Check-in date of the stay (hotel local date). Format YYYY-MM-DD. The lowest accepted value is the present date (no dates in the past). If not present, the default value will be today's date in the GMT time zone.
  'checkOutDate': new Date("2013-10-20"), // Date | Check-out date of the stay (hotel local date). Format YYYY-MM-DD. The lowest accepted value is checkInDate+1. If not present, it will default to checkInDate +1.
  'countryOfResidence': "countryOfResidence_example", // String | Code of the country of residence of the traveler expressed using ISO 3166-1 format.
  'roomQuantity': 1, // Number | Number of rooms requested (1-9).
  'priceRange': "priceRange_example", // String | Filter hotel offers by price per night interval (ex: 200-300 or -300 or 100). It is mandatory to include a currency when this field is set.
  'currency': "currency_example", // String | Use this parameter to request a specific currency. ISO currency code (http://www.iso.org/iso/home/standards/currency_codes.htm). If a hotel does not support the requested currency, the prices for the hotel will be returned in the local currency of the hotel.
  'paymentPolicy': "'NONE'", // String | Filter the response based on a specific payment type. NONE means all types (default).
  'boardType': "boardType_example", // String | Filter response based on available meals:         * ROOM_ONLY = Room Only         * BREAKFAST = Breakfast         * HALF_BOARD = Diner & Breakfast (only for Aggregators)         * FULL_BOARD = Full Board (only for Aggregators)         * ALL_INCLUSIVE = All Inclusive (only for Aggregators)
  'includeClosed': true, // Boolean | Show all properties (include sold out) or available only. For sold out properties, please check availability on other dates.
  'bestRateOnly': true, // Boolean | Used to return only the cheapest offer per hotel or all available offers.
  'lang': "lang_example" // String | Requested language of descriptive texts.  Examples: FR , fr , fr-FR. If a language is not available the text will be returned in english. ISO language code (https://www.iso.org/iso-639-language-codes.html).
};
apiInstance.getMultiHotelOffers(hotelIds, opts, (error, data, response) => {
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
 **hotelIds** | [**[String]**](String.md)| Amadeus property codes on 8 chars. Mandatory parameter for a search by predefined list of hotels. | 
 **adults** | **Number**| Number of adult guests (1-9) per room. | [optional] [default to 1]
 **checkInDate** | **Date**| Check-in date of the stay (hotel local date). Format YYYY-MM-DD. The lowest accepted value is the present date (no dates in the past). If not present, the default value will be today&#39;s date in the GMT time zone. | [optional] 
 **checkOutDate** | **Date**| Check-out date of the stay (hotel local date). Format YYYY-MM-DD. The lowest accepted value is checkInDate+1. If not present, it will default to checkInDate +1. | [optional] 
 **countryOfResidence** | **String**| Code of the country of residence of the traveler expressed using ISO 3166-1 format. | [optional] 
 **roomQuantity** | **Number**| Number of rooms requested (1-9). | [optional] [default to 1]
 **priceRange** | **String**| Filter hotel offers by price per night interval (ex: 200-300 or -300 or 100). It is mandatory to include a currency when this field is set. | [optional] 
 **currency** | **String**| Use this parameter to request a specific currency. ISO currency code (http://www.iso.org/iso/home/standards/currency_codes.htm). If a hotel does not support the requested currency, the prices for the hotel will be returned in the local currency of the hotel. | [optional] 
 **paymentPolicy** | **String**| Filter the response based on a specific payment type. NONE means all types (default). | [optional] [default to &#39;NONE&#39;]
 **boardType** | **String**| Filter response based on available meals:         * ROOM_ONLY &#x3D; Room Only         * BREAKFAST &#x3D; Breakfast         * HALF_BOARD &#x3D; Diner &amp; Breakfast (only for Aggregators)         * FULL_BOARD &#x3D; Full Board (only for Aggregators)         * ALL_INCLUSIVE &#x3D; All Inclusive (only for Aggregators) | [optional] 
 **includeClosed** | **Boolean**| Show all properties (include sold out) or available only. For sold out properties, please check availability on other dates. | [optional] 
 **bestRateOnly** | **Boolean**| Used to return only the cheapest offer per hotel or all available offers. | [optional] [default to true]
 **lang** | **String**| Requested language of descriptive texts.  Examples: FR , fr , fr-FR. If a language is not available the text will be returned in english. ISO language code (https://www.iso.org/iso-639-language-codes.html). | [optional] 

### Return type

[**MultiResponse**](MultiResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.amadeus+json


## getOfferPricing

> PricingResponse getOfferPricing(offerId, opts)

getOfferPricing

### Example

```javascript
import HotelSearchApi from 'hotel_search_api';

let apiInstance = new HotelSearchApi.ShoppingApi();
let offerId = "TSXOJ6LFQ2"; // String | Unique identifier of an offer. Either the GDS booking code or the aggregator offerId with a limited lifetime.
let opts = {
  'lang': "lang_example" // String | Requested language of descriptive texts.  Examples: FR , fr , fr-FR. If a language is not available the text will be returned in english. ISO language code (https://www.iso.org/iso-639-language-codes.html).
};
apiInstance.getOfferPricing(offerId, opts, (error, data, response) => {
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
 **offerId** | **String**| Unique identifier of an offer. Either the GDS booking code or the aggregator offerId with a limited lifetime. | 
 **lang** | **String**| Requested language of descriptive texts.  Examples: FR , fr , fr-FR. If a language is not available the text will be returned in english. ISO language code (https://www.iso.org/iso-639-language-codes.html). | [optional] 

### Return type

[**PricingResponse**](PricingResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.amadeus+json

