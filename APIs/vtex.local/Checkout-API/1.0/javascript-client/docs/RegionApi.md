# CheckoutApi.RegionApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSellersByRegion**](RegionApi.md#getSellersByRegion) | **GET** /api/checkout/pub/regions/{regionId} | Get sellers by region or address



## getSellersByRegion

> GetSellersByRegion200Response getSellersByRegion(contentType, accept, regionId, country, opts)

Get sellers by region or address

Retrieve a list of sellers that cater to a specific region or address, according to your set up of our [regionalization feature](https://help.vtex.com/en/tutorial/setting-up-price-and-availability-of-skus-by-region--12ne58BmvYsYuGsimmugoc#). Learn more about [Region v2](https://developers.vtex.com/vtex-developer-docs/changelog/region-v2).    To access the list of sellers, you must choose one of the following methods:    1. Send the identification of the list of sellers (&#x60;regionId&#x60;) as a path parameter through the URL. Or;  2. Send the &#x60;country&#x60; (3-digit ISO code) and at least one of the two values (&#x60;postal Code&#x60; or &#x60;geo Coordinates&#x60;) as query parameters through the URL. For this method, it is also allowed to send both values (&#x60;postalCode&#x60; or &#x60;geoCoordinates&#x60;) in the same request.

### Example

```javascript
import CheckoutApi from 'checkout_api';

let apiInstance = new CheckoutApi.RegionApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let regionId = "v2.1BB18CE648B5111D0933734ED83EC783"; // String | ID of the region corresponding to the shopper's location.
let country = "'BRA'"; // String | Three letter country code refering to the `postalCode` field.
let opts = {
  'postalCode': "'1234000'", // String | Postal code corresponding to the shopper's location.
  'geoCoordinates': [-47.924747467041016] // [Number] | Geocoordinates (first longitude, semicolon, then latitude) corresponding to the shopper's location.
};
apiInstance.getSellersByRegion(contentType, accept, regionId, country, opts, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **regionId** | **String**| ID of the region corresponding to the shopper&#39;s location. | 
 **country** | **String**| Three letter country code refering to the &#x60;postalCode&#x60; field. | [default to &#39;BRA&#39;]
 **postalCode** | **String**| Postal code corresponding to the shopper&#39;s location. | [optional] [default to &#39;1234000&#39;]
 **geoCoordinates** | [**[Number]**](Number.md)| Geocoordinates (first longitude, semicolon, then latitude) corresponding to the shopper&#39;s location. | [optional] 

### Return type

[**GetSellersByRegion200Response**](GetSellersByRegion200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

