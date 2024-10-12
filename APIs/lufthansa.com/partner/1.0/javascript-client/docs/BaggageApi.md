# LhPartnerApi.BaggageApi

All URIs are relative to *https://api.lufthansa.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**baggageTripAndContact**](BaggageApi.md#baggageTripAndContact) | **GET** /baggage/baggagetripandcontact/{searchID} | Baggage Trip and Contact



## baggageTripAndContact

> String baggageTripAndContact(searchID, accept)

Baggage Trip and Contact

Retrieve passenger trip, contact and baggage details. This service is only accessible for LH privileged partners

### Example

```javascript
import LhPartnerApi from 'lh_partner_api';
let defaultClient = LhPartnerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: auth
let auth = defaultClient.authentications['auth'];
auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LhPartnerApi.BaggageApi();
let searchID = "searchID_example"; // String | Bag tag number, PNR, boarding card or FQTV ID
let accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
apiInstance.baggageTripAndContact(searchID, accept, (error, data, response) => {
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
 **searchID** | **String**| Bag tag number, PNR, boarding card or FQTV ID | 
 **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | 

### Return type

**String**

### Authorization

[auth](../README.md#auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

