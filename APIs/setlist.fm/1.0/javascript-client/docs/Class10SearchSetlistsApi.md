# SetlistFmApi.Class10SearchSetlistsApi

All URIs are relative to */rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource10SearchSetlistsGetSetlistsGET**](Class10SearchSetlistsApi.md#resource10SearchSetlistsGetSetlistsGET) | **GET** /1.0/search/setlists | Search for setlists.



## resource10SearchSetlistsGetSetlistsGET

> JsonSetlists resource10SearchSetlistsGetSetlistsGET(opts)

Search for setlists.

Search for setlists.

### Example

```javascript
import SetlistFmApi from 'setlist_fm_api';

let apiInstance = new SetlistFmApi.Class10SearchSetlistsApi();
let opts = {
  'artistMbid': "artistMbid_example", // String | the artist's Musicbrainz Identifier (mbid)
  'artistName': "artistName_example", // String | the artist's name
  'artistTmid': 56, // Number | the artist's Ticketmaster Identifier (tmid)
  'cityId': "cityId_example", // String | the city's geoId
  'cityName': "cityName_example", // String | the name of the city
  'countryCode': "countryCode_example", // String | the country code
  'date': "date_example", // String | the date of the event (format dd-MM-yyyy)
  'lastFm': 56, // Number | the event's Last.fm Event ID (deprecated)
  'lastUpdated': "lastUpdated_example", // String | the date and time (UTC) when this setlist was last updated (format yyyyMMddHHmmss) - either edited or reverted. search will return setlists that were updated on or after this date
  'p': 1, // Number | the number of the result page
  'state': "state_example", // String | the state
  'stateCode': "stateCode_example", // String | the state code
  'tourName': "tourName_example", // String | 
  'venueId': "venueId_example", // String | the venue id
  'venueName': "venueName_example", // String | the name of the venue
  'year': "year_example" // String | the year of the event
};
apiInstance.resource10SearchSetlistsGetSetlistsGET(opts, (error, data, response) => {
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
 **artistMbid** | **String**| the artist&#39;s Musicbrainz Identifier (mbid) | [optional] 
 **artistName** | **String**| the artist&#39;s name | [optional] 
 **artistTmid** | **Number**| the artist&#39;s Ticketmaster Identifier (tmid) | [optional] 
 **cityId** | **String**| the city&#39;s geoId | [optional] 
 **cityName** | **String**| the name of the city | [optional] 
 **countryCode** | **String**| the country code | [optional] 
 **date** | **String**| the date of the event (format dd-MM-yyyy) | [optional] 
 **lastFm** | **Number**| the event&#39;s Last.fm Event ID (deprecated) | [optional] 
 **lastUpdated** | **String**| the date and time (UTC) when this setlist was last updated (format yyyyMMddHHmmss) - either edited or reverted. search will return setlists that were updated on or after this date | [optional] 
 **p** | **Number**| the number of the result page | [optional] [default to 1]
 **state** | **String**| the state | [optional] 
 **stateCode** | **String**| the state code | [optional] 
 **tourName** | **String**|  | [optional] 
 **venueId** | **String**| the venue id | [optional] 
 **venueName** | **String**| the name of the venue | [optional] 
 **year** | **String**| the year of the event | [optional] 

### Return type

[**JsonSetlists**](JsonSetlists.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml, application/json

