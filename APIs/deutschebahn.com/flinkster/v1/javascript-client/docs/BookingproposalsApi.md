# FlinksterApiNg.BookingproposalsApi

All URIs are relative to *https://api.deutschebahn.com/flinkster-api-ng/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listBookingProposals**](BookingproposalsApi.md#listBookingProposals) | **GET** /bookingproposals | Query for available RentalObjects of a specific view



## listBookingProposals

> RentalObjectJO listBookingProposals(opts)

Query for available RentalObjects of a specific view

Here you can query all bookable Rental Objects with different Parameters (Time, Location,...)

### Example

```javascript
import FlinksterApiNg from 'flinkster_api_ng';

let apiInstance = new FlinksterApiNg.BookingproposalsApi();
let opts = {
  'lat': 3.4, // Number | 
  'lon': 3.4, // Number | 
  'radius': 56, // Number | 
  'offset': 56, // Number | 
  'limit': 56, // Number | 
  'providernetwork': "providernetwork_example", // String | 
  'begin': "begin_example", // String | 
  'end': "end_example", // String | 
  'expand': "expand_example", // String | 
  'view': "view_example" // String | 
};
apiInstance.listBookingProposals(opts, (error, data, response) => {
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
 **lat** | **Number**|  | [optional] 
 **lon** | **Number**|  | [optional] 
 **radius** | **Number**|  | [optional] 
 **offset** | **Number**|  | [optional] 
 **limit** | **Number**|  | [optional] 
 **providernetwork** | **String**|  | [optional] 
 **begin** | **String**|  | [optional] 
 **end** | **String**|  | [optional] 
 **expand** | **String**|  | [optional] 
 **view** | **String**|  | [optional] 

### Return type

[**RentalObjectJO**](RentalObjectJO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

