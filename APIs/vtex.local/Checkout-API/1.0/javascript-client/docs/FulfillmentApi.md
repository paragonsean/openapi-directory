# CheckoutApi.FulfillmentApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAddressByPostalCode**](FulfillmentApi.md#getAddressByPostalCode) | **GET** /api/checkout/pub/postal-code/{countryCode}/{postalCode} | Get address by postal code
[**listPickupPpointsByLocation**](FulfillmentApi.md#listPickupPpointsByLocation) | **GET** /api/checkout/pub/pickup-points | List pickup points by location



## getAddressByPostalCode

> getAddressByPostalCode(contentType, accept, countryCode, postalCode)

Get address by postal code

Retrieves address information for a given postal code and country.    This request can be used to implement auto complete functionality when a customer needs to fill in an address.

### Example

```javascript
import CheckoutApi from 'checkout_api';

let apiInstance = new CheckoutApi.FulfillmentApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let countryCode = "'BRA'"; // String | Three letter country code refering to the `postalCode` field.
let postalCode = "'1234000'"; // String | Postal code.
apiInstance.getAddressByPostalCode(contentType, accept, countryCode, postalCode, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **countryCode** | **String**| Three letter country code refering to the &#x60;postalCode&#x60; field. | [default to &#39;BRA&#39;]
 **postalCode** | **String**| Postal code. | [default to &#39;1234000&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listPickupPpointsByLocation

> listPickupPpointsByLocation(contentType, accept, opts)

List pickup points by location

Retrieves information on pickup points close to a given location determined by geocoordinates or postal code.    The pickup points returned are not necessarily all active ones. Make sure to validate the information consumed by integrations.

### Example

```javascript
import CheckoutApi from 'checkout_api';

let apiInstance = new CheckoutApi.FulfillmentApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let opts = {
  'geoCoordinates': [-47.924747467041016], // [Number] | Geocoordinates (first longitude, then latitude) around which to search for pickup points. If you use this type of search, do not pass postal and country codes.
  'postalCode': "'1234000'", // String | Postal code around which to search for pickup points. If you use this type of search, make sure to pass a `countryCode` and do not pass `geoCoordinates`.
  'countryCode': "'BRA'" // String | Three letter country code refering to the `postalCode` field. Pass the country code only if you are searching pickup points by postal code.
};
apiInstance.listPickupPpointsByLocation(contentType, accept, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **geoCoordinates** | [**[Number]**](Number.md)| Geocoordinates (first longitude, then latitude) around which to search for pickup points. If you use this type of search, do not pass postal and country codes. | [optional] 
 **postalCode** | **String**| Postal code around which to search for pickup points. If you use this type of search, make sure to pass a &#x60;countryCode&#x60; and do not pass &#x60;geoCoordinates&#x60;. | [optional] [default to &#39;1234000&#39;]
 **countryCode** | **String**| Three letter country code refering to the &#x60;postalCode&#x60; field. Pass the country code only if you are searching pickup points by postal code. | [optional] [default to &#39;BRA&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

