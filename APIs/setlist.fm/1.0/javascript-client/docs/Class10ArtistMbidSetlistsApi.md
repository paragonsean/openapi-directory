# SetlistFmApi.Class10ArtistMbidSetlistsApi

All URIs are relative to */rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource10ArtistMbidSetlistsGetArtistSetlistsGET**](Class10ArtistMbidSetlistsApi.md#resource10ArtistMbidSetlistsGetArtistSetlistsGET) | **GET** /1.0/artist/{mbid}/setlists | .



## resource10ArtistMbidSetlistsGetArtistSetlistsGET

> JsonSetlists resource10ArtistMbidSetlistsGetArtistSetlistsGET(mbid, opts)

.

&lt;p&gt; Get a list of an artist&#39;s setlists. &lt;/p&gt;

### Example

```javascript
import SetlistFmApi from 'setlist_fm_api';

let apiInstance = new SetlistFmApi.Class10ArtistMbidSetlistsApi();
let mbid = "mbid_example"; // String | the Musicbrainz MBID of the artist
let opts = {
  'p': 1 // Number | the number of the result page
};
apiInstance.resource10ArtistMbidSetlistsGetArtistSetlistsGET(mbid, opts, (error, data, response) => {
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
 **mbid** | **String**| the Musicbrainz MBID of the artist | 
 **p** | **Number**| the number of the result page | [optional] [default to 1]

### Return type

[**JsonSetlists**](JsonSetlists.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml, application/json

