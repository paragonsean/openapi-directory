# SetlistFmApi.Class10VenueVenueIdSetlistsApi

All URIs are relative to */rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource10VenueVenueIdSetlistsGetVenueSetlistsGET**](Class10VenueVenueIdSetlistsApi.md#resource10VenueVenueIdSetlistsGetVenueSetlistsGET) | **GET** /1.0/venue/{venueId}/setlists | .



## resource10VenueVenueIdSetlistsGetVenueSetlistsGET

> JsonSetlists resource10VenueVenueIdSetlistsGetVenueSetlistsGET(venueId, opts)

.

&lt;p&gt; Get setlists for a specific venue. &lt;/p&gt;

### Example

```javascript
import SetlistFmApi from 'setlist_fm_api';

let apiInstance = new SetlistFmApi.Class10VenueVenueIdSetlistsApi();
let venueId = "venueId_example"; // String | the id of the venue
let opts = {
  'p': 1 // Number | the number of the result page
};
apiInstance.resource10VenueVenueIdSetlistsGetVenueSetlistsGET(venueId, opts, (error, data, response) => {
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
 **venueId** | **String**| the id of the venue | 
 **p** | **Number**| the number of the result page | [optional] [default to 1]

### Return type

[**JsonSetlists**](JsonSetlists.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml, application/json

