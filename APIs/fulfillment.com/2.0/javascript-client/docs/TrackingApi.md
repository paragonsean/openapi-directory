# FulfillmentComApiv2.TrackingApi

All URIs are relative to *https://api.fulfillment.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getTrack**](TrackingApi.md#getTrack) | **GET** /track | Tracking



## getTrack

> TrackingResponse getTrack(opts)

Tracking

Get uniformed tracking events for any package, this response is carrier independent. Please note, an API Key is required for throttling purposes, please contact your success manager for details.

### Example

```javascript
import FulfillmentComApiv2 from 'fulfillment_com_apiv2';

let apiInstance = new FulfillmentComApiv2.TrackingApi();
let opts = {
  'trackingNumber': "trackingNumber_example" // String | 
};
apiInstance.getTrack(opts, (error, data, response) => {
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
 **trackingNumber** | **String**|  | [optional] 

### Return type

[**TrackingResponse**](TrackingResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

