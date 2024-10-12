# MusixmatchApi.ArtistApi

All URIs are relative to *https://api.musixmatch.com/ws/1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**artistGetGet**](ArtistApi.md#artistGetGet) | **GET** /artist.get | 
[**artistRelatedGetGet**](ArtistApi.md#artistRelatedGetGet) | **GET** /artist.related.get | 
[**artistSearchGet**](ArtistApi.md#artistSearchGet) | **GET** /artist.search | 
[**chartArtistsGetGet**](ArtistApi.md#chartArtistsGetGet) | **GET** /chart.artists.get | 



## artistGetGet

> ArtistGetGet200Response artistGetGet(artistId, opts)



### Example

```javascript
import MusixmatchApi from 'musixmatch_api';
let defaultClient = MusixmatchApi.ApiClient.instance;
// Configure API key authorization: key
let key = defaultClient.authentications['key'];
key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//key.apiKeyPrefix = 'Token';

let apiInstance = new MusixmatchApi.ArtistApi();
let artistId = "artistId_example"; // String |  The musiXmatch artist id
let opts = {
  'format': "'json'", // String | output format: json, jsonp, xml.
  'callback': "callback_example" // String | jsonp callback
};
apiInstance.artistGetGet(artistId, opts, (error, data, response) => {
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
 **artistId** | **String**|  The musiXmatch artist id | 
 **format** | **String**| output format: json, jsonp, xml. | [optional] [default to &#39;json&#39;]
 **callback** | **String**| jsonp callback | [optional] 

### Return type

[**ArtistGetGet200Response**](ArtistGetGet200Response.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## artistRelatedGetGet

> ArtistRelatedGetGet200Response artistRelatedGetGet(artistId, opts)



### Example

```javascript
import MusixmatchApi from 'musixmatch_api';
let defaultClient = MusixmatchApi.ApiClient.instance;
// Configure API key authorization: key
let key = defaultClient.authentications['key'];
key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//key.apiKeyPrefix = 'Token';

let apiInstance = new MusixmatchApi.ArtistApi();
let artistId = "artistId_example"; // String | The musiXmatch artist id
let opts = {
  'format': "'json'", // String | output format: json, jsonp, xml.
  'callback': "callback_example", // String | jsonp callback
  'pageSize': 3.4, // Number | Define the page size for paginated results.Range is 1 to 100.
  'page': 3.4 // Number | Define the page number for paginated results
};
apiInstance.artistRelatedGetGet(artistId, opts, (error, data, response) => {
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
 **artistId** | **String**| The musiXmatch artist id | 
 **format** | **String**| output format: json, jsonp, xml. | [optional] [default to &#39;json&#39;]
 **callback** | **String**| jsonp callback | [optional] 
 **pageSize** | **Number**| Define the page size for paginated results.Range is 1 to 100. | [optional] 
 **page** | **Number**| Define the page number for paginated results | [optional] 

### Return type

[**ArtistRelatedGetGet200Response**](ArtistRelatedGetGet200Response.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## artistSearchGet

> ArtistRelatedGetGet200Response artistSearchGet(opts)



### Example

```javascript
import MusixmatchApi from 'musixmatch_api';
let defaultClient = MusixmatchApi.ApiClient.instance;
// Configure API key authorization: key
let key = defaultClient.authentications['key'];
key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//key.apiKeyPrefix = 'Token';

let apiInstance = new MusixmatchApi.ArtistApi();
let opts = {
  'format': "'json'", // String | output format: json, jsonp, xml.
  'callback': "callback_example", // String | jsonp callback
  'qArtist': "qArtist_example", // String | The song artist
  'fArtistId': 3.4, // Number | When set, filter by this artist id
  'page': 3.4, // Number | Define the page number for paginated results
  'pageSize': 3.4 // Number | Define the page size for paginated results.Range is 1 to 100.
};
apiInstance.artistSearchGet(opts, (error, data, response) => {
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
 **format** | **String**| output format: json, jsonp, xml. | [optional] [default to &#39;json&#39;]
 **callback** | **String**| jsonp callback | [optional] 
 **qArtist** | **String**| The song artist | [optional] 
 **fArtistId** | **Number**| When set, filter by this artist id | [optional] 
 **page** | **Number**| Define the page number for paginated results | [optional] 
 **pageSize** | **Number**| Define the page size for paginated results.Range is 1 to 100. | [optional] 

### Return type

[**ArtistRelatedGetGet200Response**](ArtistRelatedGetGet200Response.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## chartArtistsGetGet

> ChartArtistsGetGet200Response chartArtistsGetGet(opts)



### Example

```javascript
import MusixmatchApi from 'musixmatch_api';
let defaultClient = MusixmatchApi.ApiClient.instance;
// Configure API key authorization: key
let key = defaultClient.authentications['key'];
key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//key.apiKeyPrefix = 'Token';

let apiInstance = new MusixmatchApi.ArtistApi();
let opts = {
  'format': "'json'", // String | output format: json, jsonp, xml.
  'callback': "callback_example", // String | jsonp callback
  'page': 3.4, // Number | Define the page number for paginated results
  'pageSize': 3.4, // Number | Define the page size for paginated results.Range is 1 to 100.
  'country': "'us'" // String | A valid ISO 3166 country code
};
apiInstance.chartArtistsGetGet(opts, (error, data, response) => {
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
 **format** | **String**| output format: json, jsonp, xml. | [optional] [default to &#39;json&#39;]
 **callback** | **String**| jsonp callback | [optional] 
 **page** | **Number**| Define the page number for paginated results | [optional] 
 **pageSize** | **Number**| Define the page size for paginated results.Range is 1 to 100. | [optional] 
 **country** | **String**| A valid ISO 3166 country code | [optional] [default to &#39;us&#39;]

### Return type

[**ChartArtistsGetGet200Response**](ChartArtistsGetGet200Response.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

