# SetlistFmApi.Class10VenueVenueIdApi

All URIs are relative to */rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource10VenueVenueIdGetVenueGET**](Class10VenueVenueIdApi.md#resource10VenueVenueIdGetVenueGET) | **GET** /1.0/venue/{venueId} | Get a venue by its unique id.



## resource10VenueVenueIdGetVenueGET

> JsonVenue resource10VenueVenueIdGetVenueGET(venueId)

Get a venue by its unique id.

Get a venue by its unique id.

### Example

```javascript
import SetlistFmApi from 'setlist_fm_api';

let apiInstance = new SetlistFmApi.Class10VenueVenueIdApi();
let venueId = "venueId_example"; // String | the venue's id
apiInstance.resource10VenueVenueIdGetVenueGET(venueId, (error, data, response) => {
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
 **venueId** | **String**| the venue&#39;s id | 

### Return type

[**JsonVenue**](JsonVenue.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml, application/json

