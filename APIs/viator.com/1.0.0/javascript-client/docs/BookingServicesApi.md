# ViatorApiDocumentationAmpSpecificationMerchantPartners.BookingServicesApi

All URIs are relative to *https://viatorapi.viator.com/service*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bookingAvailability**](BookingServicesApi.md#bookingAvailability) | **POST** /booking/availability | /booking/availability
[**bookingAvailabilityDates**](BookingServicesApi.md#bookingAvailabilityDates) | **GET** /booking/availability/dates | /booking/availability/dates
[**bookingAvailabilityTourgrades**](BookingServicesApi.md#bookingAvailabilityTourgrades) | **POST** /booking/availability/tourgrades | /booking/availability/tourgrades
[**bookingAvailabilityTourgradesPricingmatrix**](BookingServicesApi.md#bookingAvailabilityTourgradesPricingmatrix) | **POST** /booking/availability/tourgrades/pricingmatrix | /booking/availability/tourgrades/pricingmatrix
[**bookingBook**](BookingServicesApi.md#bookingBook) | **POST** /booking/book | /booking/book
[**bookingCalculateprice**](BookingServicesApi.md#bookingCalculateprice) | **POST** /booking/calculateprice | /booking/calculateprice
[**bookingHotels**](BookingServicesApi.md#bookingHotels) | **GET** /booking/hotels | /booking/hotels
[**bookingMybookings**](BookingServicesApi.md#bookingMybookings) | **GET** /booking/mybookings | /booking/mybookings
[**bookingPastbooking**](BookingServicesApi.md#bookingPastbooking) | **GET** /booking/pastbooking | /booking/pastbooking
[**bookingPricingmatrix**](BookingServicesApi.md#bookingPricingmatrix) | **POST** /booking/pricingmatrix | /booking/pricingmatrix
[**bookingStatus**](BookingServicesApi.md#bookingStatus) | **POST** /booking/status | /booking/status
[**bookingStatusItems**](BookingServicesApi.md#bookingStatusItems) | **POST** /booking/status/items | /booking/status/items
[**bookingVoucher**](BookingServicesApi.md#bookingVoucher) | **GET** /booking/voucher | /booking/voucher
[**cancelBooking**](BookingServicesApi.md#cancelBooking) | **POST** /bookings/{booking-reference}/cancel | /bookings/{booking-reference}/cancel
[**cancelBookingQuote**](BookingServicesApi.md#cancelBookingQuote) | **GET** /bookings/{booking-reference}/cancel-quote | /bookings/{booking-reference}/cancel-quote
[**cancellationReasons**](BookingServicesApi.md#cancellationReasons) | **GET** /bookings/cancel-reasons | /bookings/cancel-reasons



## bookingAvailability

> BookingAvailability200Response bookingAvailability(acceptLanguage, opts)

/booking/availability

Get the tour-grade with the lowest price that is available for a product on each day of the specified month  This service: - returns  - useful when displaying a calendar of available tours - For more information, see: [Availability services](#section/Key-concepts/Availability-services) - **Notes:**    - [/booking/availability/dates](#operation/bookingAvailabilityDates) provides all availability in one call and is more suitable for calendars, etc.    - Availability data is limited to a period of **12 months** into the future from the present time on the production server and **6 months** on the sandbox server.  

### Example

```javascript
import ViatorApiDocumentationAmpSpecificationMerchantPartners from 'viator_api_documentation_amp_specification__merchant_partners';
let defaultClient = ViatorApiDocumentationAmpSpecificationMerchantPartners.ApiClient.instance;
// Configure API key authorization: Legacy-API-key
let Legacy-API-key = defaultClient.authentications['Legacy-API-key'];
Legacy-API-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Legacy-API-key.apiKeyPrefix = 'Token';
// Configure API key authorization: API-key
let API-key = defaultClient.authentications['API-key'];
API-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-key.apiKeyPrefix = 'Token';

let apiInstance = new ViatorApiDocumentationAmpSpecificationMerchantPartners.BookingServicesApi();
let acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
let opts = {
  'bookingAvailabilityRequest': {"ageBands":[{"bandId":1,"count":1}],"currencyCode":"AUD","month":"12","productCode":"5010SYDNEY","year":"2020"} // BookingAvailabilityRequest | 
};
apiInstance.bookingAvailability(acceptLanguage, opts, (error, data, response) => {
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
 **acceptLanguage** | **String**| Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes)  | 
 **bookingAvailabilityRequest** | [**BookingAvailabilityRequest**](BookingAvailabilityRequest.md)|  | [optional] 

### Return type

[**BookingAvailability200Response**](BookingAvailability200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bookingAvailabilityDates

> BookingAvailabilityDates200Response bookingAvailabilityDates(acceptLanguage, opts)

/booking/availability/dates

Get dates on which a product is available  This service: - retrieves all available dates for a product, excluding days it does not operate and blocked-out dates - returns a multi-dimensional array of year-month -&amp;gt; days that have any availabile tour grade or traveler mix - useful to present the user with a list of dates for selection on which *this* product is available for booking - **Notes**:     - The user&#39;s desired traveler mix may not be eligible for booking; these details can be displayed when you retrieve its list of tour grades   - Availability data is limited to a period of **12 months** into the future from the present time on the production server and **6 months** on the sandbox server.  

### Example

```javascript
import ViatorApiDocumentationAmpSpecificationMerchantPartners from 'viator_api_documentation_amp_specification__merchant_partners';
let defaultClient = ViatorApiDocumentationAmpSpecificationMerchantPartners.ApiClient.instance;
// Configure API key authorization: Legacy-API-key
let Legacy-API-key = defaultClient.authentications['Legacy-API-key'];
Legacy-API-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Legacy-API-key.apiKeyPrefix = 'Token';
// Configure API key authorization: API-key
let API-key = defaultClient.authentications['API-key'];
API-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-key.apiKeyPrefix = 'Token';

let apiInstance = new ViatorApiDocumentationAmpSpecificationMerchantPartners.BookingServicesApi();
let acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
let opts = {
  'productCode': "2280AAHT" // String | **unique alphanumeric identifier** of the product
};
apiInstance.bookingAvailabilityDates(acceptLanguage, opts, (error, data, response) => {
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
 **acceptLanguage** | **String**| Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes)  | 
 **productCode** | **String**| **unique alphanumeric identifier** of the product | [optional] 

### Return type

[**BookingAvailabilityDates200Response**](BookingAvailabilityDates200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## bookingAvailabilityTourgrades

> BookingAvailabilityTourgrades200Response bookingAvailabilityTourgrades(acceptLanguage, opts)

/booking/availability/tourgrades

Get the tour grades of a product that are currently available  This service reports: - all tour grades for the specified product, on the specified day, that are available for the specified age bands - the pricing breakdown and the total depending on the travel date and traveler mix  **Note**: Availability data is limited to a period of **12 months** into the future from the present time on the production server and **6 months** on the sandbox server.  

### Example

```javascript
import ViatorApiDocumentationAmpSpecificationMerchantPartners from 'viator_api_documentation_amp_specification__merchant_partners';
let defaultClient = ViatorApiDocumentationAmpSpecificationMerchantPartners.ApiClient.instance;
// Configure API key authorization: Legacy-API-key
let Legacy-API-key = defaultClient.authentications['Legacy-API-key'];
Legacy-API-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Legacy-API-key.apiKeyPrefix = 'Token';
// Configure API key authorization: API-key
let API-key = defaultClient.authentications['API-key'];
API-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-key.apiKeyPrefix = 'Token';

let apiInstance = new ViatorApiDocumentationAmpSpecificationMerchantPartners.BookingServicesApi();
let acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
let opts = {
  'bookingAvailabilityTourgradesRequest': {"ageBands":[{"bandId":1,"count":1}],"bookingDate":"2020-12-28","currencyCode":"AUD","productCode":"5010SYDNEY"} // BookingAvailabilityTourgradesRequest | 
};
apiInstance.bookingAvailabilityTourgrades(acceptLanguage, opts, (error, data, response) => {
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
 **acceptLanguage** | **String**| Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes)  | 
 **bookingAvailabilityTourgradesRequest** | [**BookingAvailabilityTourgradesRequest**](BookingAvailabilityTourgradesRequest.md)|  | [optional] 

### Return type

[**BookingAvailabilityTourgrades200Response**](BookingAvailabilityTourgrades200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bookingAvailabilityTourgradesPricingmatrix

> BookingAvailabilityTourgradesPricingmatrix200Response bookingAvailabilityTourgradesPricingmatrix(acceptLanguage, opts)

/booking/availability/tourgrades/pricingmatrix

Get a pricing matrix that includes availability and tour-grades for a product  Given a month, this service returns days with available tour grades only (i.e., days which have at least one tourgrade available), and the pricing matrix for that tour grade for that day.  - **Note**: Availability data is limited to a period of **12 months** into the future from the present time on the production server and **6 months** on the sandbox server.  

### Example

```javascript
import ViatorApiDocumentationAmpSpecificationMerchantPartners from 'viator_api_documentation_amp_specification__merchant_partners';
let defaultClient = ViatorApiDocumentationAmpSpecificationMerchantPartners.ApiClient.instance;
// Configure API key authorization: Legacy-API-key
let Legacy-API-key = defaultClient.authentications['Legacy-API-key'];
Legacy-API-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Legacy-API-key.apiKeyPrefix = 'Token';
// Configure API key authorization: API-key
let API-key = defaultClient.authentications['API-key'];
API-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-key.apiKeyPrefix = 'Token';

let apiInstance = new ViatorApiDocumentationAmpSpecificationMerchantPartners.BookingServicesApi();
let acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
let opts = {
  'bookingAvailabilityTourgradesPricingmatrixRequest': {"currenctCode":"USD","month":"12","productCode":"2280AAHT","year":"2020"} // BookingAvailabilityTourgradesPricingmatrixRequest | 
};
apiInstance.bookingAvailabilityTourgradesPricingmatrix(acceptLanguage, opts, (error, data, response) => {
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
 **acceptLanguage** | **String**| Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes)  | 
 **bookingAvailabilityTourgradesPricingmatrixRequest** | [**BookingAvailabilityTourgradesPricingmatrixRequest**](BookingAvailabilityTourgradesPricingmatrixRequest.md)|  | [optional] 

### Return type

[**BookingAvailabilityTourgradesPricingmatrix200Response**](BookingAvailabilityTourgradesPricingmatrix200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bookingBook

> BookingBook200Response bookingBook(acceptLanguage, opts)

/booking/book

Make a booking  For more information, see:     - [Cancellation policy](#section/Key-concepts/Cancellation-policy)   - [Booking concepts](#section/Key-concepts/Booking-concepts)   - [Booking process flow](#section/Common-workflows-and-data-validation/Booking-process-flow)   - [Making a booking](#section/Common-workflows-and-data-validation/Making-a-booking)   - [Supplier communications](#section/Key-concepts/Supplier-communications) 

### Example

```javascript
import ViatorApiDocumentationAmpSpecificationMerchantPartners from 'viator_api_documentation_amp_specification__merchant_partners';
let defaultClient = ViatorApiDocumentationAmpSpecificationMerchantPartners.ApiClient.instance;
// Configure API key authorization: Legacy-API-key
let Legacy-API-key = defaultClient.authentications['Legacy-API-key'];
Legacy-API-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Legacy-API-key.apiKeyPrefix = 'Token';
// Configure API key authorization: API-key
let API-key = defaultClient.authentications['API-key'];
API-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-key.apiKeyPrefix = 'Token';

let apiInstance = new ViatorApiDocumentationAmpSpecificationMerchantPartners.BookingServicesApi();
let acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
let opts = {
  'bookingBookRequest': {"booker":{"email":"apitest@viator.com","firstname":"Homer Test","surname":"Simpson Test","title":"Mr"},"currencyCode":"USD","demo":true,"items":[{"bookingQuestionAnswers":[{"answer":"0123456789, 9876543210","questionId":5},{"answer":"Australia, Fiji","questionId":4},{"answer":"01 July 2022, 31 May 2022","questionId":3}],"hotelId":{"$ref":"#/components/examples/product-example-1/value/data/pas"},"languageOptionCode":"en/SERVICE_GUIDE","partnerItemDetail":{"distributorItemRef":"distroItemRef8348234535_1"},"pickupPoint":{"$ref":"#/components/examples/product-example-1/value/data/pas"},"productCode":"100022P1","specialRequirements":"","tourGradeCode":"TG1","travelDate":"2020-12-30","travellers":[{"bandId":1,"firstname":"Homer1","leadTraveller":true,"surname":"Simpson Test","title":"Mr"},{"bandId":1,"firstname":"Homer2","leadTraveller":true,"surname":"Simpson Test","title":"Mr"}]}],"partnerDetail":{"distributorRef":"distroRef34398534535"}} // BookingBookRequest | 
};
apiInstance.bookingBook(acceptLanguage, opts, (error, data, response) => {
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
 **acceptLanguage** | **String**| Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes)  | 
 **bookingBookRequest** | [**BookingBookRequest**](BookingBookRequest.md)|  | [optional] 

### Return type

[**BookingBook200Response**](BookingBook200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bookingCalculateprice

> BookingCalculateprice200Response bookingCalculateprice(acceptLanguage, opts)

/booking/calculateprice

Confirm the price of a tour / activity prior to booking  For more information, see: [Calculating prices](#section/Common-workflows-and-data-validation/Calculating-prices)    - **Note**: Availability and pricing data is limited to a period of **six months** into the future from the present time 

### Example

```javascript
import ViatorApiDocumentationAmpSpecificationMerchantPartners from 'viator_api_documentation_amp_specification__merchant_partners';
let defaultClient = ViatorApiDocumentationAmpSpecificationMerchantPartners.ApiClient.instance;
// Configure API key authorization: Legacy-API-key
let Legacy-API-key = defaultClient.authentications['Legacy-API-key'];
Legacy-API-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Legacy-API-key.apiKeyPrefix = 'Token';
// Configure API key authorization: API-key
let API-key = defaultClient.authentications['API-key'];
API-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-key.apiKeyPrefix = 'Token';

let apiInstance = new ViatorApiDocumentationAmpSpecificationMerchantPartners.BookingServicesApi();
let acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
let opts = {
  'bookingCalculatepriceRequest': {"currencyCode":"USD","items":[{"productCode":"5010SYDNEY","tourGradeCode":"24HOUR","travelDate":"2020-12-12","travellers":[{"bandId":1}]}]} // BookingCalculatepriceRequest | 
};
apiInstance.bookingCalculateprice(acceptLanguage, opts, (error, data, response) => {
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
 **acceptLanguage** | **String**| Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes)  | 
 **bookingCalculatepriceRequest** | [**BookingCalculatepriceRequest**](BookingCalculatepriceRequest.md)|  | [optional] 

### Return type

[**BookingCalculateprice200Response**](BookingCalculateprice200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bookingHotels

> BookingHotels200Response bookingHotels(acceptLanguage, opts)

/booking/hotels

Get hotel pick-ups Lists the hotel pickups available for either a product or a destination 

### Example

```javascript
import ViatorApiDocumentationAmpSpecificationMerchantPartners from 'viator_api_documentation_amp_specification__merchant_partners';
let defaultClient = ViatorApiDocumentationAmpSpecificationMerchantPartners.ApiClient.instance;
// Configure API key authorization: Legacy-API-key
let Legacy-API-key = defaultClient.authentications['Legacy-API-key'];
Legacy-API-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Legacy-API-key.apiKeyPrefix = 'Token';
// Configure API key authorization: API-key
let API-key = defaultClient.authentications['API-key'];
API-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-key.apiKeyPrefix = 'Token';

let apiInstance = new ViatorApiDocumentationAmpSpecificationMerchantPartners.BookingServicesApi();
let acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
let opts = {
  'productCode': "2280AAHT", // String | **unique alphanumeric identifier** of the product
  'destId': 123 // Number | **unique numeric identifier** of the destination
};
apiInstance.bookingHotels(acceptLanguage, opts, (error, data, response) => {
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
 **acceptLanguage** | **String**| Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes)  | 
 **productCode** | **String**| **unique alphanumeric identifier** of the product | [optional] 
 **destId** | **Number**| **unique numeric identifier** of the destination | [optional] 

### Return type

[**BookingHotels200Response**](BookingHotels200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## bookingMybookings

> BookingMybookings200Response bookingMybookings(acceptLanguage, opts)

/booking/mybookings

Get a user&#39;s bookings with travel dates in the future.   This service can also be used to check the status of a booking.   **Provide either:**  - A &#x60;voucherKey&#x60;, **or...**  - An email address (&#x60;email&#x60;) and a booking reference (&#x60;itineraryOrItemId&#x60;) ([Booking Reference](#section/Key-concepts/Booking-references)) 

### Example

```javascript
import ViatorApiDocumentationAmpSpecificationMerchantPartners from 'viator_api_documentation_amp_specification__merchant_partners';
let defaultClient = ViatorApiDocumentationAmpSpecificationMerchantPartners.ApiClient.instance;
// Configure API key authorization: Legacy-API-key
let Legacy-API-key = defaultClient.authentications['Legacy-API-key'];
Legacy-API-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Legacy-API-key.apiKeyPrefix = 'Token';
// Configure API key authorization: API-key
let API-key = defaultClient.authentications['API-key'];
API-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-key.apiKeyPrefix = 'Token';

let apiInstance = new ViatorApiDocumentationAmpSpecificationMerchantPartners.BookingServicesApi();
let acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
let opts = {
  'voucherKey': "3299307:93c7f36a56b18ba1068787ba7fb7988da5c8ad08db77604110141ff21498603e:600033670", // String | **voucher key** for the booking
  'email': "apitest@viator.com", // String | **email address** of the booker for the booking
  'itineraryOrItemId': "700179574" // String | The booking reference number of the item - **Note**: For more information, see [Booking references](#section/Key-concepts/Booking-references) 
};
apiInstance.bookingMybookings(acceptLanguage, opts, (error, data, response) => {
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
 **acceptLanguage** | **String**| Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes)  | 
 **voucherKey** | **String**| **voucher key** for the booking | [optional] 
 **email** | **String**| **email address** of the booker for the booking | [optional] 
 **itineraryOrItemId** | **String**| The booking reference number of the item - **Note**: For more information, see [Booking references](#section/Key-concepts/Booking-references)  | [optional] 

### Return type

[**BookingMybookings200Response**](BookingMybookings200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## bookingPastbooking

> BookingPastbooking200Response bookingPastbooking(acceptLanguage, opts)

/booking/pastbooking

Get the details of a single specific past booking based on the &#x60;voucherKey&#x60; or &#x60;itemId&#x60; and email address sent in the request.  **Note**: this service will only return past bookings that were made with the same API key that was used to make the booking  **Sample query parameters**: - email&#x3D;apitest@viator.com&amp;amp;itemId&#x3D;580669678  **or** - voucherKey&#x3D;1005851866:4af44c13ecf3f1a7d3f9ef2fc00c2257e08fa42ae20f877f3039ff9b52aba24e:580669678  **email** - The email address passed must match the email address associated with the booking  **Departure details**  - Departure details such as the &#x60;departurePoint&#x60;, &#x60;departurePointAddress&#x60; and &#x60;departurePointDirections&#x60; is included in the response.  - These fields may contain HTML escape characters such as &amp;amp;amp; and special characters that are escaped by a backslash. Ensure that these fields are parsed after receiving the response as it will cause your JSON to be invalid.  For more information, see: [Reviewing bookings](#section/Common-workflows-and-data-validation/Reviewing-bookings) 

### Example

```javascript
import ViatorApiDocumentationAmpSpecificationMerchantPartners from 'viator_api_documentation_amp_specification__merchant_partners';
let defaultClient = ViatorApiDocumentationAmpSpecificationMerchantPartners.ApiClient.instance;
// Configure API key authorization: Legacy-API-key
let Legacy-API-key = defaultClient.authentications['Legacy-API-key'];
Legacy-API-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Legacy-API-key.apiKeyPrefix = 'Token';
// Configure API key authorization: API-key
let API-key = defaultClient.authentications['API-key'];
API-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-key.apiKeyPrefix = 'Token';

let apiInstance = new ViatorApiDocumentationAmpSpecificationMerchantPartners.BookingServicesApi();
let acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
let opts = {
  'voucherKey': "1005851866:4af44c13ecf3f1a7d3f9ef2fc00c2257e08fa42ae20f877f3039ff9b52aba24e:580669678", // String | **specifier** of past booking type (use *one* of: `itemId` (booking reference) *and* `'voucherKey'` *or* `'email'`)
  'email': "apitest@viator.com", // String | **email address** by which to search for past bookings
  'itemId': "580669678" // String | Search for a booking with this **unique booking-reference number**. See [Booking references](#section/Key-concepts/Booking-references) for more information. 
};
apiInstance.bookingPastbooking(acceptLanguage, opts, (error, data, response) => {
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
 **acceptLanguage** | **String**| Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes)  | 
 **voucherKey** | **String**| **specifier** of past booking type (use *one* of: &#x60;itemId&#x60; (booking reference) *and* &#x60;&#39;voucherKey&#39;&#x60; *or* &#x60;&#39;email&#39;&#x60;) | [optional] 
 **email** | **String**| **email address** by which to search for past bookings | [optional] 
 **itemId** | **String**| Search for a booking with this **unique booking-reference number**. See [Booking references](#section/Key-concepts/Booking-references) for more information.  | [optional] 

### Return type

[**BookingPastbooking200Response**](BookingPastbooking200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## bookingPricingmatrix

> BookingPricingmatrix200Response bookingPricingmatrix(acceptLanguage, opts)

/booking/pricingmatrix

Get the pricing matrix for tour-grades, product age bands and pax mixes  For more information, see: [Get the tour-grade pricing matrix](#section/Common-workflows-and-data-validation/Get-the-tour-grade-pricing-matrix) 

### Example

```javascript
import ViatorApiDocumentationAmpSpecificationMerchantPartners from 'viator_api_documentation_amp_specification__merchant_partners';
let defaultClient = ViatorApiDocumentationAmpSpecificationMerchantPartners.ApiClient.instance;
// Configure API key authorization: Legacy-API-key
let Legacy-API-key = defaultClient.authentications['Legacy-API-key'];
Legacy-API-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Legacy-API-key.apiKeyPrefix = 'Token';
// Configure API key authorization: API-key
let API-key = defaultClient.authentications['API-key'];
API-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-key.apiKeyPrefix = 'Token';

let apiInstance = new ViatorApiDocumentationAmpSpecificationMerchantPartners.BookingServicesApi();
let acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
let opts = {
  'bookingPricingmatrixRequest': {"bookingDate":"2020-12-12","currencyCode":"EUR","productCode":"5010SYDNEY","tourGradeCode":"24HOUR"} // BookingPricingmatrixRequest | 
};
apiInstance.bookingPricingmatrix(acceptLanguage, opts, (error, data, response) => {
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
 **acceptLanguage** | **String**| Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes)  | 
 **bookingPricingmatrixRequest** | [**BookingPricingmatrixRequest**](BookingPricingmatrixRequest.md)|  | [optional] 

### Return type

[**BookingPricingmatrix200Response**](BookingPricingmatrix200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bookingStatus

> BookingStatus200Response bookingStatus(acceptLanguage, opts)

/booking/status

Get the booking status for multiple items based on different criteria  This service:  - is ideally be used in software for bulk updates of pending bookings - returns a maximum of 1000 bookings (narrow your search if you expect a greater number of results) - will return &amp;lt;u&amp;gt;both&amp;lt;/u&amp;gt; live &amp;lt;u&amp;gt;and&amp;lt;/u&amp;gt; test bookings - rate limited to &amp;lt;u&amp;gt;one request every 30 minutes&amp;lt;/u&amp;gt; - For more information, see: [Get the bookiing status for multiple items](#section/Common-workflows-and-data-validation/Get-the-booking-status-for-multiple-items)  **Exceeding the rate limit** - You will receive the following error message if you exceed the rate limit allowed for this service. Set &#x60;test&#x60; to &#x60;true&#x60; to bypass this limit: &#x60;&#x60;&#x60;javascript {     \&quot;data\&quot;: null     \&quot;vmid\&quot;: 221002     \&quot;errorMessage\&quot;: [\&quot;Access allowed every 30 minutes\&quot;]     \&quot;errorType\&quot;: \&quot;EXCEPTION\&quot;     \&quot;dateStamp\&quot;: \&quot;2013-03-26T10:28:51+0000\&quot;     \&quot;errorReference\&quot;: 55315512721712161381352771     \&quot;errorMessageText\&quot;: [\&quot;Access allowed every 30 minutes\&quot;]     \&quot;success\&quot;: false     \&quot;totalCount\&quot;: 1     \&quot;errorName\&quot;: \&quot;PollingDeniedException\&quot;   } &#x60;&#x60;&#x60; 

### Example

```javascript
import ViatorApiDocumentationAmpSpecificationMerchantPartners from 'viator_api_documentation_amp_specification__merchant_partners';
let defaultClient = ViatorApiDocumentationAmpSpecificationMerchantPartners.ApiClient.instance;
// Configure API key authorization: Legacy-API-key
let Legacy-API-key = defaultClient.authentications['Legacy-API-key'];
Legacy-API-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Legacy-API-key.apiKeyPrefix = 'Token';
// Configure API key authorization: API-key
let API-key = defaultClient.authentications['API-key'];
API-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-key.apiKeyPrefix = 'Token';

let apiInstance = new ViatorApiDocumentationAmpSpecificationMerchantPartners.BookingServicesApi();
let acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
let opts = {
  'bookingStatusRequest': {"bookingDateFrom":"2020-12-21","bookingDateTo":"2020-12-31","distributorItemRefs":["itemRef1000000"],"itemIds":[580669678],"leadFirstName":"Homer test","leadSurname":"Simpson test","test":true} // BookingStatusRequest | 
};
apiInstance.bookingStatus(acceptLanguage, opts, (error, data, response) => {
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
 **acceptLanguage** | **String**| Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes)  | 
 **bookingStatusRequest** | [**BookingStatusRequest**](BookingStatusRequest.md)|  | [optional] 

### Return type

[**BookingStatus200Response**](BookingStatus200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bookingStatusItems

> BookingStatusItems200Response bookingStatusItems(acceptLanguage, opts)

/booking/status/items

Get brief booking statuses  This service is similar to [/booking/status](#operation/bookingStatus) in that it: - retrieves the booking status for multiple items based on different criteria - has the same request parameters as [/booking/status](#operation/bookingStatus)  However, it differs in that it returns a multi-item array of booking items with less detail than what would be received from [/booking/status](#operation/bookingStatus). 

### Example

```javascript
import ViatorApiDocumentationAmpSpecificationMerchantPartners from 'viator_api_documentation_amp_specification__merchant_partners';
let defaultClient = ViatorApiDocumentationAmpSpecificationMerchantPartners.ApiClient.instance;
// Configure API key authorization: Legacy-API-key
let Legacy-API-key = defaultClient.authentications['Legacy-API-key'];
Legacy-API-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Legacy-API-key.apiKeyPrefix = 'Token';
// Configure API key authorization: API-key
let API-key = defaultClient.authentications['API-key'];
API-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-key.apiKeyPrefix = 'Token';

let apiInstance = new ViatorApiDocumentationAmpSpecificationMerchantPartners.BookingServicesApi();
let acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
let opts = {
  'bookingStatusItemsRequest': {"bookingDateFrom":"2020-12-21","bookingDateTo":"2020-12-31","distributorItemRefs":["itemRef1000000"],"itemIds":[580669678],"leadFirstName":"Homer test","leadSurname":"Simpson test","test":true} // BookingStatusItemsRequest | 
};
apiInstance.bookingStatusItems(acceptLanguage, opts, (error, data, response) => {
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
 **acceptLanguage** | **String**| Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes)  | 
 **bookingStatusItemsRequest** | [**BookingStatusItemsRequest**](BookingStatusItemsRequest.md)|  | [optional] 

### Return type

[**BookingStatusItems200Response**](BookingStatusItems200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bookingVoucher

> BookingVoucher200Response bookingVoucher(acceptLanguage, opts)

/booking/voucher

Get voucher details - Use this service to retrieve the voucher details of a booked item. - The data returned is HTML-formatted and can be wrapped in a header and/or footer.  **Sample query parameters** - leadLastName&#x3D;Simpson test&amp;amp;itemId&#x3D;580669678  **or**  - voucherKey&#x3D;1005851866:4af44c13ecf3f1a7d3f9ef2fc00c2257e08fa42ae20f877f3039ff9b52aba24e:580669678&amp;amp;fullHTML&#x3D;true&amp;amp;mobileVoucher&#x3D;true 

### Example

```javascript
import ViatorApiDocumentationAmpSpecificationMerchantPartners from 'viator_api_documentation_amp_specification__merchant_partners';
let defaultClient = ViatorApiDocumentationAmpSpecificationMerchantPartners.ApiClient.instance;
// Configure API key authorization: Legacy-API-key
let Legacy-API-key = defaultClient.authentications['Legacy-API-key'];
Legacy-API-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Legacy-API-key.apiKeyPrefix = 'Token';
// Configure API key authorization: API-key
let API-key = defaultClient.authentications['API-key'];
API-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-key.apiKeyPrefix = 'Token';

let apiInstance = new ViatorApiDocumentationAmpSpecificationMerchantPartners.BookingServicesApi();
let acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
let opts = {
  'leadLastName': "Simpson", // String | **surname** of *this* lead traveler
  'itemId': 600033670, // Number | Booking-reference number generated by Viator    - **Note**: For more information, see: [Booking references](#section/Key-concepts/Booking-references) 
  'embeddedResources': false, // Boolean | ignore (Viator only)
  'voucherKey': "3299307:93c7f36a56b18ba1068787ba7fb7988da5c8ad08db77604110141ff21498603e:600033670", // String | **identifier** for the voucher - **note**: use &lt;u&gt;either&lt;/u&gt; `voucherKey` &lt;u&gt;or&lt;/u&gt; the three separate parameters - if `voucherKey` is provided as well as the other parameters, then `voucherKey` overrides the other paramaters - `voucherKey` is obtained from [/booking/mybookings](#operation/bookingMybookings) or in the response from [/booking/book](#operation/bookingBook) when you make a booking 
  'fullHTML': true, // Boolean | **specifier**: - set to `true` if you wish to retrieve the full HTML-formatted voucher - set to `false` if you want the div fragment (optional) 
  'mobileVoucher': true // Boolean | **specifier**:  - if set to `true`, the service returns the mobile (cut down) HTML-formatted voucher - if `false` the full voucher HTML is returned (ignoring `fullHTML`) - default: `true`  - this field should only be enabled for products that have a `voucherOption` of `'VOUCHER_E'` - do not enable `mobileVouchers` for paper vouchers (`voucherOption` of `'VOUCHER_PAPER_ONLY'`) as no barcode is returned - the voucher information is available in the response from [/product](#operation/product), [/booking/book](#operation/bookingBook), [/booking/pastbooking](#operation/bookingPastbooking), [/booking/mybookings](#operation/bookingMybookings) (it is also displayed under the 'Redemption Info' heading in this service) 
};
apiInstance.bookingVoucher(acceptLanguage, opts, (error, data, response) => {
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
 **acceptLanguage** | **String**| Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes)  | 
 **leadLastName** | **String**| **surname** of *this* lead traveler | [optional] 
 **itemId** | **Number**| Booking-reference number generated by Viator    - **Note**: For more information, see: [Booking references](#section/Key-concepts/Booking-references)  | [optional] 
 **embeddedResources** | **Boolean**| ignore (Viator only) | [optional] 
 **voucherKey** | **String**| **identifier** for the voucher - **note**: use &amp;lt;u&amp;gt;either&amp;lt;/u&amp;gt; &#x60;voucherKey&#x60; &amp;lt;u&amp;gt;or&amp;lt;/u&amp;gt; the three separate parameters - if &#x60;voucherKey&#x60; is provided as well as the other parameters, then &#x60;voucherKey&#x60; overrides the other paramaters - &#x60;voucherKey&#x60; is obtained from [/booking/mybookings](#operation/bookingMybookings) or in the response from [/booking/book](#operation/bookingBook) when you make a booking  | [optional] 
 **fullHTML** | **Boolean**| **specifier**: - set to &#x60;true&#x60; if you wish to retrieve the full HTML-formatted voucher - set to &#x60;false&#x60; if you want the div fragment (optional)  | [optional] 
 **mobileVoucher** | **Boolean**| **specifier**:  - if set to &#x60;true&#x60;, the service returns the mobile (cut down) HTML-formatted voucher - if &#x60;false&#x60; the full voucher HTML is returned (ignoring &#x60;fullHTML&#x60;) - default: &#x60;true&#x60;  - this field should only be enabled for products that have a &#x60;voucherOption&#x60; of &#x60;&#39;VOUCHER_E&#39;&#x60; - do not enable &#x60;mobileVouchers&#x60; for paper vouchers (&#x60;voucherOption&#x60; of &#x60;&#39;VOUCHER_PAPER_ONLY&#39;&#x60;) as no barcode is returned - the voucher information is available in the response from [/product](#operation/product), [/booking/book](#operation/bookingBook), [/booking/pastbooking](#operation/bookingPastbooking), [/booking/mybookings](#operation/bookingMybookings) (it is also displayed under the &#39;Redemption Info&#39; heading in this service)  | [optional] 

### Return type

[**BookingVoucher200Response**](BookingVoucher200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cancelBooking

> CancelBookingResponse cancelBooking(bookingReference, acceptLanguage, opts)

/bookings/{booking-reference}/cancel

Submits a cancellation request for the specified booking  For information on how to use this service, see: [Cancellation API workflow](#section/Common-workflows-and-data-validation/Cancellation-API-workflow)  **Note**:     * This service &amp;lt;u&amp;gt;requires&amp;lt;/u&amp;gt; [exp-api-key](#section/Authentication/exp-api-key) to be included as a header parameter. Please speak to your account manager if you have not yet been issued an exp-api-key.   * The base URL for the server for this endpoint is different from the older endpoints described in this document. Use &#x60;https://api.sandbox.viator.com/partner/bookings/{booking-reference}/cancel&#x60; 

### Example

```javascript
import ViatorApiDocumentationAmpSpecificationMerchantPartners from 'viator_api_documentation_amp_specification__merchant_partners';
let defaultClient = ViatorApiDocumentationAmpSpecificationMerchantPartners.ApiClient.instance;
// Configure API key authorization: Legacy-API-key
let Legacy-API-key = defaultClient.authentications['Legacy-API-key'];
Legacy-API-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Legacy-API-key.apiKeyPrefix = 'Token';
// Configure API key authorization: API-key
let API-key = defaultClient.authentications['API-key'];
API-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-key.apiKeyPrefix = 'Token';

let apiInstance = new ViatorApiDocumentationAmpSpecificationMerchantPartners.BookingServicesApi();
let bookingReference = "bookingReference_example"; // String | The ID of the booking
let acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
let opts = {
  'cancellationRequest': {"reasonCode":"Customer_Service.I_canceled_my_entire_trip"} // CancellationRequest | 
};
apiInstance.cancelBooking(bookingReference, acceptLanguage, opts, (error, data, response) => {
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
 **bookingReference** | **String**| The ID of the booking | 
 **acceptLanguage** | **String**| Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes)  | 
 **cancellationRequest** | [**CancellationRequest**](CancellationRequest.md)|  | [optional] 

### Return type

[**CancelBookingResponse**](CancelBookingResponse.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cancelBookingQuote

> CancelBookingQuoteResponse cancelBookingQuote(bookingReference)

/bookings/{booking-reference}/cancel-quote

Retrieves a quote for the cancellation of a booking  For information on how to use this service, see: [Cancellation API workflow](#section/Common-workflows-and-data-validation/Cancellation-API-workflow)  **Note**:     * This service &amp;lt;u&amp;gt;requires&amp;lt;/u&amp;gt; [exp-api-key](#section/Authentication/exp-api-key) to be included as a header parameter. Please speak to your account manager if you have not yet been issued an exp-api-key.   * The base URL for the server for this endpoint is different from the older endpoints described in this document. Use &#x60;https://api.sandbox.viator.com/partner/bookings/{booking-reference}/cancel-quote&#x60; 

### Example

```javascript
import ViatorApiDocumentationAmpSpecificationMerchantPartners from 'viator_api_documentation_amp_specification__merchant_partners';
let defaultClient = ViatorApiDocumentationAmpSpecificationMerchantPartners.ApiClient.instance;
// Configure API key authorization: Legacy-API-key
let Legacy-API-key = defaultClient.authentications['Legacy-API-key'];
Legacy-API-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Legacy-API-key.apiKeyPrefix = 'Token';
// Configure API key authorization: API-key
let API-key = defaultClient.authentications['API-key'];
API-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-key.apiKeyPrefix = 'Token';

let apiInstance = new ViatorApiDocumentationAmpSpecificationMerchantPartners.BookingServicesApi();
let bookingReference = "bookingReference_example"; // String | Unique numeric identifier of the booking for which to retrieve a cancellation quote
apiInstance.cancelBookingQuote(bookingReference, (error, data, response) => {
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
 **bookingReference** | **String**| Unique numeric identifier of the booking for which to retrieve a cancellation quote | 

### Return type

[**CancelBookingQuoteResponse**](CancelBookingQuoteResponse.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cancellationReasons

> [CancellationReasonsResponse] cancellationReasons(acceptLanguage)

/bookings/cancel-reasons

Retrieves a dictionary of unique identification codes (&#x60;cancellationReasonCode&#x60;) and their associated natural-language descriptions (&#x60;cancellationReasonText&#x60;).  For information on how to use this service, see: [Cancellation API workflow](#section/Common-workflows-and-data-validation/Cancellation-API-workflow)  **Note**:     * This service &amp;lt;u&amp;gt;requires&amp;lt;/u&amp;gt; [exp-api-key](#section/Authentication/exp-api-key) to be included as a header parameter. Please speak to your account manager if you have not yet been issued an exp-api-key.   * The base URL for the server for this endpoint is different from the older endpoints described in this document. Use &#x60;https://api.sandbox.viator.com/partner/cancel-reasons&#x60; 

### Example

```javascript
import ViatorApiDocumentationAmpSpecificationMerchantPartners from 'viator_api_documentation_amp_specification__merchant_partners';
let defaultClient = ViatorApiDocumentationAmpSpecificationMerchantPartners.ApiClient.instance;
// Configure API key authorization: Legacy-API-key
let Legacy-API-key = defaultClient.authentications['Legacy-API-key'];
Legacy-API-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Legacy-API-key.apiKeyPrefix = 'Token';
// Configure API key authorization: API-key
let API-key = defaultClient.authentications['API-key'];
API-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-key.apiKeyPrefix = 'Token';

let apiInstance = new ViatorApiDocumentationAmpSpecificationMerchantPartners.BookingServicesApi();
let acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
apiInstance.cancellationReasons(acceptLanguage, (error, data, response) => {
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
 **acceptLanguage** | **String**| Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes)  | 

### Return type

[**[CancellationReasonsResponse]**](CancellationReasonsResponse.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

