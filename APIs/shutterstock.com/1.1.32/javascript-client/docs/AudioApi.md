# ShutterstockApiExplorer.AudioApi

All URIs are relative to *https://api.shutterstock.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addTrackCollectionItems**](AudioApi.md#addTrackCollectionItems) | **POST** /v2/audio/collections/{id}/items | Add audio tracks to collections
[**createTrackCollection**](AudioApi.md#createTrackCollection) | **POST** /v2/audio/collections | Create audio collections
[**deleteTrackCollection**](AudioApi.md#deleteTrackCollection) | **DELETE** /v2/audio/collections/{id} | Delete audio collections
[**deleteTrackCollectionItems**](AudioApi.md#deleteTrackCollectionItems) | **DELETE** /v2/audio/collections/{id}/items | Remove audio tracks from collections
[**downloadTracks**](AudioApi.md#downloadTracks) | **POST** /v2/audio/licenses/{id}/downloads | Download audio tracks
[**getTrack**](AudioApi.md#getTrack) | **GET** /v2/audio/{id} | Get details about audio tracks
[**getTrackCollection**](AudioApi.md#getTrackCollection) | **GET** /v2/audio/collections/{id} | Get the details of audio collections
[**getTrackCollectionItems**](AudioApi.md#getTrackCollectionItems) | **GET** /v2/audio/collections/{id}/items | Get the contents of audio collections
[**getTrackCollectionList**](AudioApi.md#getTrackCollectionList) | **GET** /v2/audio/collections | List audio collections
[**getTrackLicenseList**](AudioApi.md#getTrackLicenseList) | **GET** /v2/audio/licenses | List audio licenses
[**getTrackList**](AudioApi.md#getTrackList) | **GET** /v2/audio | List audio tracks
[**licenseTrack**](AudioApi.md#licenseTrack) | **POST** /v2/audio/licenses | License audio tracks
[**listGenres**](AudioApi.md#listGenres) | **GET** /v2/audio/genres | List audio genres
[**listInstruments**](AudioApi.md#listInstruments) | **GET** /v2/audio/instruments | List audio instruments
[**listMoods**](AudioApi.md#listMoods) | **GET** /v2/audio/moods | List audio moods
[**renameTrackCollection**](AudioApi.md#renameTrackCollection) | **POST** /v2/audio/collections/{id} | Rename audio collections
[**searchTracks**](AudioApi.md#searchTracks) | **GET** /v2/audio/search | Search for tracks



## addTrackCollectionItems

> addTrackCollectionItems(id, collectionItemRequest)

Add audio tracks to collections

This endpoint adds one or more tracks to a collection by track IDs.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.AudioApi();
let id = "48433115"; // String | Collection ID
let collectionItemRequest = {"items":[{"id":"442583"},{"id":"7491192"}]}; // CollectionItemRequest | List of items to add to collection
apiInstance.addTrackCollectionItems(id, collectionItemRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Collection ID | 
 **collectionItemRequest** | [**CollectionItemRequest**](CollectionItemRequest.md)| List of items to add to collection | 

### Return type

null (empty response body)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## createTrackCollection

> CollectionCreateResponse createTrackCollection(collectionCreateRequest)

Create audio collections

This endpoint creates one or more collections (soundboxes). To add tracks, use &#x60;POST /v2/audio/collections/{id}/items&#x60;.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.AudioApi();
let collectionCreateRequest = {"name":"Best rock music"}; // CollectionCreateRequest | Collection metadata
apiInstance.createTrackCollection(collectionCreateRequest, (error, data, response) => {
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
 **collectionCreateRequest** | [**CollectionCreateRequest**](CollectionCreateRequest.md)| Collection metadata | 

### Return type

[**CollectionCreateResponse**](CollectionCreateResponse.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteTrackCollection

> deleteTrackCollection(id)

Delete audio collections

This endpoint deletes a collection.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.AudioApi();
let id = "48433111"; // String | Collection ID
apiInstance.deleteTrackCollection(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Collection ID | 

### Return type

null (empty response body)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteTrackCollectionItems

> deleteTrackCollectionItems(id, opts)

Remove audio tracks from collections

This endpoint removes one or more tracks from a collection.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.AudioApi();
let id = "48433119"; // String | Collection ID
let opts = {
  'itemId': ["null"] // [String] | One or more item IDs to remove from the collection
};
apiInstance.deleteTrackCollectionItems(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Collection ID | 
 **itemId** | [**[String]**](String.md)| One or more item IDs to remove from the collection | [optional] 

### Return type

null (empty response body)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## downloadTracks

> AudioUrl downloadTracks(id)

Download audio tracks

This endpoint redownloads tracks that you have already received a license for. The download links in the response are valid for 8 hours.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.AudioApi();
let id = "e123"; // String | License ID
apiInstance.downloadTracks(id, (error, data, response) => {
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
 **id** | **String**| License ID | 

### Return type

[**AudioUrl**](AudioUrl.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTrack

> Audio getTrack(id, opts)

Get details about audio tracks

This endpoint shows information about a track, including its genres, instruments, and other attributes.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new ShutterstockApiExplorer.AudioApi();
let id = 442583; // Number | Audio track ID
let opts = {
  'view': "full", // String | Amount of detail to render in the response
  'searchId': "00000000-0000-0000-0000-000000000000" // String | The ID of the search that is related to this request
};
apiInstance.getTrack(id, opts, (error, data, response) => {
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
 **id** | **Number**| Audio track ID | 
 **view** | **String**| Amount of detail to render in the response | [optional] [default to &#39;full&#39;]
 **searchId** | **String**| The ID of the search that is related to this request | [optional] 

### Return type

[**Audio**](Audio.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTrackCollection

> Collection getTrackCollection(id, opts)

Get the details of audio collections

This endpoint gets more detailed information about a collection, including the number of items in it and when it was last updated. To get the tracks in collections, use &#x60;GET /v2/audio/collections/{id}/items&#x60;.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.AudioApi();
let id = "48433107"; // String | Collection ID
let opts = {
  'embed': ["null"], // [String] | Which sharing information to include in the response, such as a URL to the collection
  'shareCode': "shareCode_example" // String | Code to retrieve a shared collection
};
apiInstance.getTrackCollection(id, opts, (error, data, response) => {
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
 **id** | **String**| Collection ID | 
 **embed** | [**[String]**](String.md)| Which sharing information to include in the response, such as a URL to the collection | [optional] 
 **shareCode** | **String**| Code to retrieve a shared collection | [optional] 

### Return type

[**Collection**](Collection.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTrackCollectionItems

> CollectionItemDataList getTrackCollectionItems(id, opts)

Get the contents of audio collections

This endpoint lists the IDs of tracks in a collection and the date that each was added.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.AudioApi();
let id = "126351027"; // String | Collection ID
let opts = {
  'page': 1, // Number | Page number
  'perPage': 100, // Number | Number of results per page
  'shareCode': "shareCode_example", // String | Code to retrieve the contents of a shared collection
  'sort': "'oldest'" // String | Sort order
};
apiInstance.getTrackCollectionItems(id, opts, (error, data, response) => {
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
 **id** | **String**| Collection ID | 
 **page** | **Number**| Page number | [optional] [default to 1]
 **perPage** | **Number**| Number of results per page | [optional] [default to 100]
 **shareCode** | **String**| Code to retrieve the contents of a shared collection | [optional] 
 **sort** | **String**| Sort order | [optional] [default to &#39;oldest&#39;]

### Return type

[**CollectionItemDataList**](CollectionItemDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTrackCollectionList

> CollectionDataList getTrackCollectionList(opts)

List audio collections

This endpoint lists your collections of audio tracks and their basic attributes.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.AudioApi();
let opts = {
  'page': 1, // Number | Page number
  'perPage': 100, // Number | Number of results per page
  'embed': ["null"] // [String] | Which sharing information to include in the response, such as a URL to the collection
};
apiInstance.getTrackCollectionList(opts, (error, data, response) => {
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
 **page** | **Number**| Page number | [optional] [default to 1]
 **perPage** | **Number**| Number of results per page | [optional] [default to 100]
 **embed** | [**[String]**](String.md)| Which sharing information to include in the response, such as a URL to the collection | [optional] 

### Return type

[**CollectionDataList**](CollectionDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTrackLicenseList

> DownloadHistoryDataList getTrackLicenseList(opts)

List audio licenses

This endpoint lists existing licenses. You can filter the results according to the track ID to see if you have an existing license for a specific track.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.AudioApi();
let opts = {
  'audioId': "1", // String | Show licenses for the specified track ID
  'license': "48433107", // String | Restrict results by license. Prepending a `-` sign will exclude results by license
  'page': 1, // Number | Page number
  'perPage': 20, // Number | Number of results per page
  'sort': "'newest'", // String | Sort order
  'username': "aUniqueUsername", // String | Filter licenses by username of licensee
  'startDate': new Date("2021-03-29T13:25:13.521Z"), // Date | Show licenses created on or after the specified date
  'endDate': new Date("2021-03-29T13:25:13.521Z"), // Date | Show licenses created before the specified date
  'downloadAvailability': "'all'", // String | Filter licenses by download availability
  'teamHistory': false // Boolean | Set to true to see license history for all members of your team.
};
apiInstance.getTrackLicenseList(opts, (error, data, response) => {
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
 **audioId** | **String**| Show licenses for the specified track ID | [optional] 
 **license** | **String**| Restrict results by license. Prepending a &#x60;-&#x60; sign will exclude results by license | [optional] 
 **page** | **Number**| Page number | [optional] [default to 1]
 **perPage** | **Number**| Number of results per page | [optional] [default to 20]
 **sort** | **String**| Sort order | [optional] [default to &#39;newest&#39;]
 **username** | **String**| Filter licenses by username of licensee | [optional] 
 **startDate** | **Date**| Show licenses created on or after the specified date | [optional] 
 **endDate** | **Date**| Show licenses created before the specified date | [optional] 
 **downloadAvailability** | **String**| Filter licenses by download availability | [optional] [default to &#39;all&#39;]
 **teamHistory** | **Boolean**| Set to true to see license history for all members of your team. | [optional] [default to false]

### Return type

[**DownloadHistoryDataList**](DownloadHistoryDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTrackList

> AudioDataList getTrackList(id, opts)

List audio tracks

This endpoint lists information about one or more audio tracks, including the description and publication date.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new ShutterstockApiExplorer.AudioApi();
let id = ["null"]; // [String] | One or more audio IDs
let opts = {
  'view': "full", // String | Amount of detail to render in the response
  'searchId': "00000000-0000-0000-0000-000000000000" // String | The ID of the search that is related to this request
};
apiInstance.getTrackList(id, opts, (error, data, response) => {
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
 **id** | [**[String]**](String.md)| One or more audio IDs | 
 **view** | **String**| Amount of detail to render in the response | [optional] [default to &#39;minimal&#39;]
 **searchId** | **String**| The ID of the search that is related to this request | [optional] 

### Return type

[**AudioDataList**](AudioDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## licenseTrack

> LicenseAudioResultDataList licenseTrack(licenseAudioRequest, opts)

License audio tracks

This endpoint gets licenses for one or more tracks. The download links in the response are valid for 8 hours.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.AudioApi();
let licenseAudioRequest = {"$ref":"#/components/schemas/LicenseAudioRequest/example"}; // LicenseAudioRequest | Tracks to license
let opts = {
  'license': "audio_platform", // String | License type
  'searchId': "p5S6QwRikdFJTHXwsoiqTg" // String | The ID of the search that led to licensing this track
};
apiInstance.licenseTrack(licenseAudioRequest, opts, (error, data, response) => {
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
 **licenseAudioRequest** | [**LicenseAudioRequest**](LicenseAudioRequest.md)| Tracks to license | 
 **license** | **String**| License type | [optional] 
 **searchId** | **String**| The ID of the search that led to licensing this track | [optional] 

### Return type

[**LicenseAudioResultDataList**](LicenseAudioResultDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listGenres

> GenreList listGenres(opts)

List audio genres

This endpoint returns a list of all audio genres.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new ShutterstockApiExplorer.AudioApi();
let opts = {
  'language': "language_example" // String | Which language the genres will be returned
};
apiInstance.listGenres(opts, (error, data, response) => {
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
 **language** | **String**| Which language the genres will be returned | [optional] 

### Return type

[**GenreList**](GenreList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listInstruments

> InstrumentList listInstruments(opts)

List audio instruments

This endpoint returns a list of all audio instruments.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new ShutterstockApiExplorer.AudioApi();
let opts = {
  'language': "language_example" // String | Which language the instruments will be returned in
};
apiInstance.listInstruments(opts, (error, data, response) => {
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
 **language** | **String**| Which language the instruments will be returned in | [optional] 

### Return type

[**InstrumentList**](InstrumentList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listMoods

> MoodList listMoods(opts)

List audio moods

This endpoint returns a list of all audio moods.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new ShutterstockApiExplorer.AudioApi();
let opts = {
  'language': "language_example" // String | Which language the moods will be returned in
};
apiInstance.listMoods(opts, (error, data, response) => {
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
 **language** | **String**| Which language the moods will be returned in | [optional] 

### Return type

[**MoodList**](MoodList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## renameTrackCollection

> renameTrackCollection(id, collectionUpdateRequest)

Rename audio collections

This endpoint sets a new name for a collection.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.AudioApi();
let id = "48433107"; // String | Collection ID
let collectionUpdateRequest = {"name":"Best rock music"}; // CollectionUpdateRequest | Collection changes
apiInstance.renameTrackCollection(id, collectionUpdateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Collection ID | 
 **collectionUpdateRequest** | [**CollectionUpdateRequest**](CollectionUpdateRequest.md)| Collection changes | 

### Return type

null (empty response body)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## searchTracks

> AudioSearchResults searchTracks(opts)

Search for tracks

This endpoint searches for tracks. If you specify more than one search parameter, the API uses an AND condition. Array parameters can be specified multiple times; in this case, the API uses an AND or an OR condition with those values, depending on the parameter.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new ShutterstockApiExplorer.AudioApi();
let opts = {
  'artists': ["null"], // [String] | Show tracks with one of the specified artist names or IDs
  'bpm': 56, // Number | (Deprecated; use bpm_from and bpm_to instead) Show tracks with the specified beats per minute
  'bpmFrom': 80, // Number | Show tracks with the specified beats per minute or faster
  'bpmTo': 120, // Number | Show tracks with the specified beats per minute or slower
  'duration': 180, // Number | Show tracks with the specified duration in seconds
  'durationFrom': 30, // Number | Show tracks with the specified duration or longer in seconds
  'durationTo': 180, // Number | Show tracks with the specified duration or shorter in seconds
  'genre': ["null"], // [String] | Show tracks with each of the specified genres; to get the list of genres, use `GET /v2/audio/genres`
  'isInstrumental': true, // Boolean | Show instrumental music only
  'instruments': ["null"], // [String] | Show tracks with each of the specified instruments; to get the list of instruments, use `GET /v2/audio/instruments`
  'moods': ["null"], // [String] | Show tracks with each of the specified moods; to get the list of moods, use `GET /v2/audio/moods`
  'page': 1, // Number | Page number
  'perPage': 1, // Number | Number of results per page
  'query': "drum", // String | One or more search terms separated by spaces
  'sort': "score", // String | Sort by
  'sortOrder': "'desc'", // String | Sort order
  'vocalDescription': "female", // String | Show tracks with the specified vocal description (male, female)
  'view': "full", // String | Amount of detail to render in the response
  'fields': "fields_example", // String | Fields to display in the response; see the documentation for the fields parameter in the overview section
  'library': "'premier'", // String | Which library to search
  'language': "language_example" // String | Which language to search in
};
apiInstance.searchTracks(opts, (error, data, response) => {
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
 **artists** | [**[String]**](String.md)| Show tracks with one of the specified artist names or IDs | [optional] 
 **bpm** | **Number**| (Deprecated; use bpm_from and bpm_to instead) Show tracks with the specified beats per minute | [optional] 
 **bpmFrom** | **Number**| Show tracks with the specified beats per minute or faster | [optional] 
 **bpmTo** | **Number**| Show tracks with the specified beats per minute or slower | [optional] 
 **duration** | **Number**| Show tracks with the specified duration in seconds | [optional] 
 **durationFrom** | **Number**| Show tracks with the specified duration or longer in seconds | [optional] 
 **durationTo** | **Number**| Show tracks with the specified duration or shorter in seconds | [optional] 
 **genre** | [**[String]**](String.md)| Show tracks with each of the specified genres; to get the list of genres, use &#x60;GET /v2/audio/genres&#x60; | [optional] 
 **isInstrumental** | **Boolean**| Show instrumental music only | [optional] 
 **instruments** | [**[String]**](String.md)| Show tracks with each of the specified instruments; to get the list of instruments, use &#x60;GET /v2/audio/instruments&#x60; | [optional] 
 **moods** | [**[String]**](String.md)| Show tracks with each of the specified moods; to get the list of moods, use &#x60;GET /v2/audio/moods&#x60; | [optional] 
 **page** | **Number**| Page number | [optional] [default to 1]
 **perPage** | **Number**| Number of results per page | [optional] [default to 20]
 **query** | **String**| One or more search terms separated by spaces | [optional] 
 **sort** | **String**| Sort by | [optional] 
 **sortOrder** | **String**| Sort order | [optional] [default to &#39;desc&#39;]
 **vocalDescription** | **String**| Show tracks with the specified vocal description (male, female) | [optional] 
 **view** | **String**| Amount of detail to render in the response | [optional] [default to &#39;minimal&#39;]
 **fields** | **String**| Fields to display in the response; see the documentation for the fields parameter in the overview section | [optional] 
 **library** | **String**| Which library to search | [optional] [default to &#39;premier&#39;]
 **language** | **String**| Which language to search in | [optional] 

### Return type

[**AudioSearchResults**](AudioSearchResults.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

