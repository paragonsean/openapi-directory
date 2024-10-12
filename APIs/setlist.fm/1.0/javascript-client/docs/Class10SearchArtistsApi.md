# SetlistFmApi.Class10SearchArtistsApi

All URIs are relative to */rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource10SearchArtistsGetArtistsGET**](Class10SearchArtistsApi.md#resource10SearchArtistsGetArtistsGET) | **GET** /1.0/search/artists | Search for artists.



## resource10SearchArtistsGetArtistsGET

> JsonArtists resource10SearchArtistsGetArtistsGET(opts)

Search for artists.

Search for artists.

### Example

```javascript
import SetlistFmApi from 'setlist_fm_api';

let apiInstance = new SetlistFmApi.Class10SearchArtistsApi();
let opts = {
  'artistMbid': "artistMbid_example", // String | the artist's Musicbrainz Identifier (mbid)
  'artistName': "artistName_example", // String | the artist's name
  'artistTmid': 56, // Number | the artist's Ticketmaster Identifier (tmid)
  'p': 1, // Number | the number of the result page you'd like to have
  'sort': "'sortName'" // String | the sort of the result, either sortName (default) or relevance
};
apiInstance.resource10SearchArtistsGetArtistsGET(opts, (error, data, response) => {
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
 **p** | **Number**| the number of the result page you&#39;d like to have | [optional] [default to 1]
 **sort** | **String**| the sort of the result, either sortName (default) or relevance | [optional] [default to &#39;sortName&#39;]

### Return type

[**JsonArtists**](JsonArtists.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml, application/json

