# SetlistFmApi.Class10ArtistMbidApi

All URIs are relative to */rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource10ArtistMbidGetArtistGET**](Class10ArtistMbidApi.md#resource10ArtistMbidGetArtistGET) | **GET** /1.0/artist/{mbid} | .



## resource10ArtistMbidGetArtistGET

> JsonArtist resource10ArtistMbidGetArtistGET(mbid)

.

&lt;p&gt; Returns an artist for a given Musicbrainz MBID &lt;/p&gt;

### Example

```javascript
import SetlistFmApi from 'setlist_fm_api';

let apiInstance = new SetlistFmApi.Class10ArtistMbidApi();
let mbid = "mbid_example"; // String | a Musicbrainz MBID, e.g. 0bfba3d3-6a04-4779-bb0a-df07df5b0558
apiInstance.resource10ArtistMbidGetArtistGET(mbid, (error, data, response) => {
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
 **mbid** | **String**| a Musicbrainz MBID, e.g. 0bfba3d3-6a04-4779-bb0a-df07df5b0558 | 

### Return type

[**JsonArtist**](JsonArtist.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml, application/json

