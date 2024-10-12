# Apacta.ChangelogApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**offersOfferIdChangelogGet**](ChangelogApi.md#offersOfferIdChangelogGet) | **GET** /offers/{offer_id}/changelog | Get list of changelog history for the offer. Returns offer object with contact and user objects if they are provided



## offersOfferIdChangelogGet

> OffersOfferIdChangelogGet200Response offersOfferIdChangelogGet(offerId)

Get list of changelog history for the offer. Returns offer object with contact and user objects if they are provided

### Example

```javascript
import Apacta from 'apacta';

let apiInstance = new Apacta.ChangelogApi();
let offerId = "offerId_example"; // String | 
apiInstance.offersOfferIdChangelogGet(offerId, (error, data, response) => {
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
 **offerId** | **String**|  | 

### Return type

[**OffersOfferIdChangelogGet200Response**](OffersOfferIdChangelogGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

