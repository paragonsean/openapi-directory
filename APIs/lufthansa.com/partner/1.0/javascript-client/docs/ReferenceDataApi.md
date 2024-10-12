# LhPartnerApi.ReferenceDataApi

All URIs are relative to *https://api.lufthansa.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**seatDetails**](ReferenceDataApi.md#seatDetails) | **GET** /references/seatdetails/{aircraftCode}/{cabinCode} | Seat Details



## seatDetails

> String seatDetails(aircraftCode, accept, cabinCode, opts)

Seat Details

A description of all available seat details by aircraft type. You can retrieve the full set or details for a particular aircraft type.

### Example

```javascript
import LhPartnerApi from 'lh_partner_api';
let defaultClient = LhPartnerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: auth
let auth = defaultClient.authentications['auth'];
auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LhPartnerApi.ReferenceDataApi();
let aircraftCode = "aircraftCode_example"; // String | Aircraft type. 3-character IATA equipment code
let accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
let cabinCode = "'C'"; // String | Cabin class: M, E, C, F (Acceptable values are: \"\", \"M\", \"E\", \"C\", \"F\")
let opts = {
  'lang': "lang_example" // String | 2-letter ISO 3166-1 language code
};
apiInstance.seatDetails(aircraftCode, accept, cabinCode, opts, (error, data, response) => {
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
 **aircraftCode** | **String**| Aircraft type. 3-character IATA equipment code | 
 **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | 
 **cabinCode** | **String**| Cabin class: M, E, C, F (Acceptable values are: \&quot;\&quot;, \&quot;M\&quot;, \&quot;E\&quot;, \&quot;C\&quot;, \&quot;F\&quot;) | [default to &#39;C&#39;]
 **lang** | **String**| 2-letter ISO 3166-1 language code | [optional] 

### Return type

**String**

### Authorization

[auth](../README.md#auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

