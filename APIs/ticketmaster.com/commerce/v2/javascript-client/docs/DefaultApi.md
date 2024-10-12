# CommerceApi.DefaultApi

All URIs are relative to *http://www.ticketmaster.com/commerce/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getEventOffers**](DefaultApi.md#getEventOffers) | **GET** /commerce/v2/events/{eventId}/offers | Event Offers



## getEventOffers

> OfferingResponse getEventOffers(eventId, opts)

Event Offers

Returns Event Offers.

### Example

```javascript
import CommerceApi from 'commerce_api';

let apiInstance = new CommerceApi.DefaultApi();
let eventId = "eventId_example"; // String | Event Identifier
let opts = {
  'X_SSL_CERT_UID': "X_SSL_CERT_UID_example", // String | API Key for external API developer
  'X_TM_ACCESS_TOKEN': "X_TM_ACCESS_TOKEN_example", // String | Access token for
  'accessToken': "accessToken_example", // String | Query Param Access Token
  'apiKey': "apiKey_example", // String | Query Param API Key for external API developer
  'body': "body_example" // String | displayId to un-hide protected offers
};
apiInstance.getEventOffers(eventId, opts, (error, data, response) => {
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
 **eventId** | **String**| Event Identifier | 
 **X_SSL_CERT_UID** | **String**| API Key for external API developer | [optional] 
 **X_TM_ACCESS_TOKEN** | **String**| Access token for | [optional] 
 **accessToken** | **String**| Query Param Access Token | [optional] 
 **apiKey** | **String**| Query Param API Key for external API developer | [optional] 
 **body** | **String**| displayId to un-hide protected offers | [optional] 

### Return type

[**OfferingResponse**](OfferingResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

