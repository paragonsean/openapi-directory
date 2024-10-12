# FlickrApiSchema.PublicApi

All URIs are relative to *https://api.flickr.com/services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**echo**](PublicApi.md#echo) | **GET** /rest?method&#x3D;flickr.test.echo | 
[**getAccessToken**](PublicApi.md#getAccessToken) | **GET** /oauth/access_token | 
[**getAlbumByID**](PublicApi.md#getAlbumByID) | **GET** /rest?method&#x3D;flickr.photosets.getPhotos | 
[**getAlbumContextByID**](PublicApi.md#getAlbumContextByID) | **GET** /rest?method&#x3D;flickr.photosets.getContext | 
[**getAlbumsByPersonID**](PublicApi.md#getAlbumsByPersonID) | **GET** /rest?method&#x3D;flickr.photosets.getList | 
[**getFavoritesByPersonID**](PublicApi.md#getFavoritesByPersonID) | **GET** /rest?method&#x3D;flickr.favorites.getList | 
[**getFavoritesContextByID**](PublicApi.md#getFavoritesContextByID) | **GET** /rest?method&#x3D;flickr.favorites.getContext | 
[**getGalleryPhotosByID**](PublicApi.md#getGalleryPhotosByID) | **GET** /rest?method&#x3D;flickr.galleries.getPhotos | 
[**getGroupByID**](PublicApi.md#getGroupByID) | **GET** /rest?method&#x3D;flickr.groups.getInfo | 
[**getGroupDiscussionsByID**](PublicApi.md#getGroupDiscussionsByID) | **GET** /rest?method&#x3D;flickr.groups.discuss.topics.getList | 
[**getGroupPhotosByID**](PublicApi.md#getGroupPhotosByID) | **GET** /rest?method&#x3D;flickr.groups.pools.getPhotos | 
[**getGroupTopicByID**](PublicApi.md#getGroupTopicByID) | **GET** /rest?method&#x3D;flickr.groups.discuss.topics.getInfo | 
[**getGroupTopicRepliesByID**](PublicApi.md#getGroupTopicRepliesByID) | **GET** /rest?method&#x3D;flickr.groups.discuss.replies.getInfo | 
[**getLicenseByID**](PublicApi.md#getLicenseByID) | **GET** /rest?method&#x3D;flickr.photos.licenses.getInfo | 
[**getMediaByPersonID**](PublicApi.md#getMediaByPersonID) | **GET** /rest?method&#x3D;flickr.people.getPhotos | 
[**getMediaBySearch**](PublicApi.md#getMediaBySearch) | **GET** /rest?method&#x3D;flickr.photos.search | 
[**getPersonByID**](PublicApi.md#getPersonByID) | **GET** /rest?method&#x3D;flickr.people.getInfo | 
[**getPhotoByID**](PublicApi.md#getPhotoByID) | **GET** /rest?method&#x3D;flickr.photos.getInfo | 
[**getPhotoExifByID**](PublicApi.md#getPhotoExifByID) | **GET** /rest?method&#x3D;flickr.photos.getExif | 
[**getPhotoSizesByID**](PublicApi.md#getPhotoSizesByID) | **GET** /rest?method&#x3D;flickr.photos.getSizes | 
[**getPhotolistContextByID**](PublicApi.md#getPhotolistContextByID) | **GET** /rest?method&#x3D;flickr.photolist.getContext | 
[**getPhotostreamContextByID**](PublicApi.md#getPhotostreamContextByID) | **GET** /rest?method&#x3D;flickr.photos.getContext | 
[**getRequestToken**](PublicApi.md#getRequestToken) | **GET** /oauth/request_token | 
[**restmethodflickrGroupsPoolsGetContextGet**](PublicApi.md#restmethodflickrGroupsPoolsGetContextGet) | **GET** /rest?method&#x3D;flickr.groups.pools.getContext | 
[**uploadPhoto**](PublicApi.md#uploadPhoto) | **POST** /upload | 



## echo

> Echo200Response echo(apiKey, opts)



Echos the input parameters back in the response

### Example

```javascript
import FlickrApiSchema from 'flickr_api_schema';

let apiInstance = new FlickrApiSchema.PublicApi();
let apiKey = "apiKey_example"; // String | 
let opts = {
  'echo': "echo_example" // String | 
};
apiInstance.echo(apiKey, opts, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **echo** | **String**|  | [optional] 

### Return type

[**Echo200Response**](Echo200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAccessToken

> String getAccessToken(oauthConsumerKey, oauthNonce, oauthTimestamp, oauthSignatureMethod, oauthVersion, oauthSignature, oauthVerifier, oauthToken)



Returns an access token

### Example

```javascript
import FlickrApiSchema from 'flickr_api_schema';

let apiInstance = new FlickrApiSchema.PublicApi();
let oauthConsumerKey = "oauthConsumerKey_example"; // String | 
let oauthNonce = "oauthNonce_example"; // String | 
let oauthTimestamp = "oauthTimestamp_example"; // String | 
let oauthSignatureMethod = "oauthSignatureMethod_example"; // String | 
let oauthVersion = "oauthVersion_example"; // String | 
let oauthSignature = "oauthSignature_example"; // String | 
let oauthVerifier = "oauthVerifier_example"; // String | 
let oauthToken = "oauthToken_example"; // String | 
apiInstance.getAccessToken(oauthConsumerKey, oauthNonce, oauthTimestamp, oauthSignatureMethod, oauthVersion, oauthSignature, oauthVerifier, oauthToken, (error, data, response) => {
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
 **oauthConsumerKey** | **String**|  | 
 **oauthNonce** | **String**|  | 
 **oauthTimestamp** | **String**|  | 
 **oauthSignatureMethod** | **String**|  | 
 **oauthVersion** | **String**|  | 
 **oauthSignature** | **String**|  | 
 **oauthVerifier** | **String**|  | 
 **oauthToken** | **String**|  | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAlbumByID

> GetAlbumByID200Response getAlbumByID(apiKey, photosetId)



Returns a list of photos in an album.

### Example

```javascript
import FlickrApiSchema from 'flickr_api_schema';

let apiInstance = new FlickrApiSchema.PublicApi();
let apiKey = "apiKey_example"; // String | 
let photosetId = "photosetId_example"; // String | 
apiInstance.getAlbumByID(apiKey, photosetId, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **photosetId** | **String**|  | 

### Return type

[**GetAlbumByID200Response**](GetAlbumByID200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAlbumContextByID

> GetFavoritesContextByID200Response getAlbumContextByID(apiKey, photoId, opts)



Returns next and previous photos for a photo in a set

### Example

```javascript
import FlickrApiSchema from 'flickr_api_schema';

let apiInstance = new FlickrApiSchema.PublicApi();
let apiKey = "apiKey_example"; // String | 
let photoId = "photoId_example"; // String | 
let opts = {
  'photosetId': "photosetId_example" // String | 
};
apiInstance.getAlbumContextByID(apiKey, photoId, opts, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **photoId** | **String**|  | 
 **photosetId** | **String**|  | [optional] 

### Return type

[**GetFavoritesContextByID200Response**](GetFavoritesContextByID200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAlbumsByPersonID

> GetAlbumsByPersonID200Response getAlbumsByPersonID(apiKey, userId, opts)



Returns the albums belonging to the specified user

### Example

```javascript
import FlickrApiSchema from 'flickr_api_schema';

let apiInstance = new FlickrApiSchema.PublicApi();
let apiKey = "apiKey_example"; // String | 
let userId = "userId_example"; // String | 
let opts = {
  'page': 3.4, // Number | 
  'perPage': 3.4 // Number | 
};
apiInstance.getAlbumsByPersonID(apiKey, userId, opts, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **userId** | **String**|  | 
 **page** | **Number**|  | [optional] 
 **perPage** | **Number**|  | [optional] 

### Return type

[**GetAlbumsByPersonID200Response**](GetAlbumsByPersonID200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFavoritesByPersonID

> GetFavoritesByPersonID200Response getFavoritesByPersonID(apiKey, userId, opts)



Returns a list of the user&#39;s favorite photos. Only photos which the calling user has permission to see are returned.

### Example

```javascript
import FlickrApiSchema from 'flickr_api_schema';

let apiInstance = new FlickrApiSchema.PublicApi();
let apiKey = "apiKey_example"; // String | 
let userId = "userId_example"; // String | 
let opts = {
  'minFaveDate': 3.4, // Number | 
  'maxFaveDate': 3.4, // Number | 
  'page': 3.4, // Number | 
  'perPage': 3.4 // Number | 
};
apiInstance.getFavoritesByPersonID(apiKey, userId, opts, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **userId** | **String**|  | 
 **minFaveDate** | **Number**|  | [optional] 
 **maxFaveDate** | **Number**|  | [optional] 
 **page** | **Number**|  | [optional] 
 **perPage** | **Number**|  | [optional] 

### Return type

[**GetFavoritesByPersonID200Response**](GetFavoritesByPersonID200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFavoritesContextByID

> GetFavoritesContextByID200Response getFavoritesContextByID(apiKey, photoId, opts)



Returns next and previous favorites for a photo in a user&#39;s favorites

### Example

```javascript
import FlickrApiSchema from 'flickr_api_schema';

let apiInstance = new FlickrApiSchema.PublicApi();
let apiKey = "apiKey_example"; // String | 
let photoId = "photoId_example"; // String | 
let opts = {
  'userId': "userId_example" // String | 
};
apiInstance.getFavoritesContextByID(apiKey, photoId, opts, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **photoId** | **String**|  | 
 **userId** | **String**|  | [optional] 

### Return type

[**GetFavoritesContextByID200Response**](GetFavoritesContextByID200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGalleryPhotosByID

> GetGalleryPhotosByID200Response getGalleryPhotosByID(apiKey, galleryId)



Returns a list of photos in a gallery.

### Example

```javascript
import FlickrApiSchema from 'flickr_api_schema';

let apiInstance = new FlickrApiSchema.PublicApi();
let apiKey = "apiKey_example"; // String | 
let galleryId = "galleryId_example"; // String | 
apiInstance.getGalleryPhotosByID(apiKey, galleryId, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **galleryId** | **String**|  | 

### Return type

[**GetGalleryPhotosByID200Response**](GetGalleryPhotosByID200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGroupByID

> GetGroupByID200Response getGroupByID(apiKey, opts)



Get information about a group

### Example

```javascript
import FlickrApiSchema from 'flickr_api_schema';

let apiInstance = new FlickrApiSchema.PublicApi();
let apiKey = "apiKey_example"; // String | 
let opts = {
  'groupId': "groupId_example", // String | 
  'groupPathAlias': "groupPathAlias_example", // String | 
  'lang': "lang_example" // String | 
};
apiInstance.getGroupByID(apiKey, opts, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **groupId** | **String**|  | [optional] 
 **groupPathAlias** | **String**|  | [optional] 
 **lang** | **String**|  | [optional] 

### Return type

[**GetGroupByID200Response**](GetGroupByID200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGroupDiscussionsByID

> GetGroupDiscussionsByID200Response getGroupDiscussionsByID(apiKey, opts)



Get a list of discussion topics in a group.

### Example

```javascript
import FlickrApiSchema from 'flickr_api_schema';

let apiInstance = new FlickrApiSchema.PublicApi();
let apiKey = "apiKey_example"; // String | 
let opts = {
  'groupId': "groupId_example", // String | 
  'page': 3.4, // Number | 
  'perPage': 3.4 // Number | 
};
apiInstance.getGroupDiscussionsByID(apiKey, opts, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **groupId** | **String**|  | [optional] 
 **page** | **Number**|  | [optional] 
 **perPage** | **Number**|  | [optional] 

### Return type

[**GetGroupDiscussionsByID200Response**](GetGroupDiscussionsByID200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGroupPhotosByID

> GetGalleryPhotosByID200Response getGroupPhotosByID(apiKey, opts)



Returns a list of pool photos for a given group

### Example

```javascript
import FlickrApiSchema from 'flickr_api_schema';

let apiInstance = new FlickrApiSchema.PublicApi();
let apiKey = "apiKey_example"; // String | 
let opts = {
  'groupId': "groupId_example" // String | 
};
apiInstance.getGroupPhotosByID(apiKey, opts, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **groupId** | **String**|  | [optional] 

### Return type

[**GetGalleryPhotosByID200Response**](GetGalleryPhotosByID200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGroupTopicByID

> GetGroupTopicByID200Response getGroupTopicByID(apiKey, topicId, opts)



Get information about a group discussion topic

### Example

```javascript
import FlickrApiSchema from 'flickr_api_schema';

let apiInstance = new FlickrApiSchema.PublicApi();
let apiKey = "apiKey_example"; // String | 
let topicId = "topicId_example"; // String | 
let opts = {
  'groupId': "groupId_example" // String | 
};
apiInstance.getGroupTopicByID(apiKey, topicId, opts, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **topicId** | **String**|  | 
 **groupId** | **String**|  | [optional] 

### Return type

[**GetGroupTopicByID200Response**](GetGroupTopicByID200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGroupTopicRepliesByID

> GetGroupTopicRepliesByID200Response getGroupTopicRepliesByID(apiKey, topicId, replyId, opts)



Get information on a group topic reply

### Example

```javascript
import FlickrApiSchema from 'flickr_api_schema';

let apiInstance = new FlickrApiSchema.PublicApi();
let apiKey = "apiKey_example"; // String | 
let topicId = "topicId_example"; // String | 
let replyId = "replyId_example"; // String | 
let opts = {
  'groupId': "groupId_example" // String | 
};
apiInstance.getGroupTopicRepliesByID(apiKey, topicId, replyId, opts, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **topicId** | **String**|  | 
 **replyId** | **String**|  | 
 **groupId** | **String**|  | [optional] 

### Return type

[**GetGroupTopicRepliesByID200Response**](GetGroupTopicRepliesByID200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLicenseByID

> GetLicenseByID200Response getLicenseByID(apiKey)



Fetches a list of available photo licenses for Flickr

### Example

```javascript
import FlickrApiSchema from 'flickr_api_schema';

let apiInstance = new FlickrApiSchema.PublicApi();
let apiKey = "apiKey_example"; // String | 
apiInstance.getLicenseByID(apiKey, (error, data, response) => {
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
 **apiKey** | **String**|  | 

### Return type

[**GetLicenseByID200Response**](GetLicenseByID200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMediaByPersonID

> GetFavoritesByPersonID200Response getMediaByPersonID(apiKey, userId, opts)



Return photos from the given user&#39;s photostream

### Example

```javascript
import FlickrApiSchema from 'flickr_api_schema';

let apiInstance = new FlickrApiSchema.PublicApi();
let apiKey = "apiKey_example"; // String | 
let userId = "userId_example"; // String | 
let opts = {
  'safeSearch': 3.4, // Number | 
  'minUploadDate': 3.4, // Number | 
  'maxUploadDate': 3.4, // Number | 
  'minTakenDate': 3.4, // Number | 
  'maxTakenDate': 3.4, // Number | 
  'contentType': 3.4, // Number | 
  'privacyFilter': 3.4, // Number | 
  'page': 3.4, // Number | 
  'perPage': 3.4 // Number | 
};
apiInstance.getMediaByPersonID(apiKey, userId, opts, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **userId** | **String**|  | 
 **safeSearch** | **Number**|  | [optional] 
 **minUploadDate** | **Number**|  | [optional] 
 **maxUploadDate** | **Number**|  | [optional] 
 **minTakenDate** | **Number**|  | [optional] 
 **maxTakenDate** | **Number**|  | [optional] 
 **contentType** | **Number**|  | [optional] 
 **privacyFilter** | **Number**|  | [optional] 
 **page** | **Number**|  | [optional] 
 **perPage** | **Number**|  | [optional] 

### Return type

[**GetFavoritesByPersonID200Response**](GetFavoritesByPersonID200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMediaBySearch

> GetFavoritesByPersonID200Response getMediaBySearch(apiKey, opts)



Return a list of photos matching some criteria.

### Example

```javascript
import FlickrApiSchema from 'flickr_api_schema';

let apiInstance = new FlickrApiSchema.PublicApi();
let apiKey = "apiKey_example"; // String | 
let opts = {
  'text': "text_example", // String | A free text search. Photos who's title, description or tags contain the text will be returned. You can exclude results that match a term by prepending it with a - character.
  'tags': "tags_example", // String | A comma-delimited list of tags. Photos with one or more of the tags listed will be returned. You can exclude results that match a term by prepending it with a - character.
  'userId': "userId_example", // String | The NSID of the user who's photo to search. If this parameter isn't passed then everybody's public photos will be searched. A value of \"me\" will search against the calling user's photos for authenticated calls.
  'minUploadDate': "minUploadDate_example", // String | Minimum upload date. Photos with an upload date greater than or equal to this value will be returned. The date can be in the form of a unix timestamp or mysql datetime.
  'maxUploadDate': "maxUploadDate_example", // String | Maximum upload date. Photos with an upload date less than or equal to this value will be returned. The date can be in the form of a unix timestamp or mysql datetime.
  'minTakenDate': "minTakenDate_example", // String | Minimum taken date. Photos with an taken date greater than or equal to this value will be returned. The date can be in the form of a mysql datetime or unix timestamp.
  'maxTakenDate': "maxTakenDate_example", // String | Maximum taken date. Photos with an taken date less than or equal to this value will be returned. The date can be in the form of a mysql datetime or unix timestamp.
  'license': "license_example", // String | The license id for photos (for possible values see the flickr.photos.licenses.getInfo method). Multiple licenses may be comma-separated.
  'sort': "sort_example", // String | The order in which to sort returned photos. Deafults to date-posted-desc (unless you are doing a radial geo query, in which case the default sorting is by ascending distance from the point specified). The possible values are:   date-posted-asc,   date-posted-desc,   date-taken-asc,   date-taken-desc,   interestingness-desc,   interestingness-asc, and   relevance. 
  'privacyFilter': 3.4, // Number | Return photos only matching a certain privacy level. This only applies when making an authenticated call to view photos you own. Valid values are:,   1: public photos,   2: private photos visible to friends,   3: private photos visible to family,   4: private photos visible to friends & family,   5: completely private photos 
  'bbox': "bbox_example", // String | A comma-delimited list of 4 values defining the Bounding Box of the area that will be searched.
  'accuracy': "accuracy_example", // String | Recorded accuracy level of the location information. Current range is 1-16:   World level is 1   Country is ~3   Region is ~6   City is ~11   Street is ~16 
  'safeSearch': 3.4, // Number | Safe search setting:   1: for safe,   2: for moderate,   3: for restricted 
  'contentType': 3.4, // Number | Content Type setting:   1: photos only.   2: screenshots only.   3: 'other' only.   4: photos and screenshots.   5: screenshots and 'other'.   6: photos and 'other'.   7: photos, screenshots, and 'other' (all). 
  'machineTags': "machineTags_example", // String | Aside from passing in a fully formed machine tag, there is a special syntax for searching on specific properties : Find photos using the 'dc' namespace : \"machine_tags\" => \"dc:\" Find photos with a title in the 'dc' namespace : \"machine_tags\" => \"dc:title=\" Find photos titled \"mr. camera\" in the 'dc' namespace : \"machine_tags\" => \"dc:title=\\\"mr. camera\\\" Find photos whose value is \"mr. camera\" : \"machine_tags\" => \"*:*=\\\"mr. camera\\\"\" Find photos that have a title, in any namespace : \"machine_tags\" => \"*:title=\" Find photos that have a title, in any namespace, whose value is \"mr. camera\" : \"machine_tags\" => \"*:title=\\\"mr. camera\\\"\" Find photos, in the 'dc' namespace whose value is \"mr. camera\" : \"machine_tags\" => \"dc:*=\\\"mr. camera\\\"\" Multiple machine tags may be queried by passing a comma-separated list. The number of machine tags you can pass in a single query depends on the tag mode (AND or OR) that you are querying with. \"AND\" queries are limited to (16) machine tags. \"OR\" queries are limited to (8). 
  'machineTagMode': "machineTagMode_example", // String | Either 'any' for an OR combination of tags, or 'all' for an AND combination. Defaults to 'any' if not specified.
  'groupId': "groupId_example", // String | The id of a group who's pool to search. If specified, only matching photos posted to the group's pool will be returned.
  'contacts': "contacts_example", // String | Search your contacts. Either 'all' or 'ff' for just friends and family. (Experimental)
  'woeId': "woeId_example", // String | A 32-bit identifier that uniquely represents spatial entities. (not used if bbox argument is present).
  'placeId': "placeId_example", // String | A Flickr place id. (not used if bbox argument is present). Geo queries require some sort of limiting agent in order to prevent the database from crying. This is basically like the check against \"parameterless searches\" for queries without a geo component. A tag, for instance, is considered a limiting agent as are user defined min_date_taken and min_date_upload parameters — If no limiting factor is passed we return only photos added in the last 12 hours (though we may extend the limit in the future). 
  'media': "media_example", // String | Filter results by media type. Possible values are all (default), photos or videos
  'hasGeo': "hasGeo_example", // String | Any photo that has been geotagged, or if the value is \"0\" any photo that has not been geotagged. Geo queries require some sort of limiting agent in order to prevent the database from crying. This is basically like the check against \"parameterless searches\" for queries without a geo component. A tag, for instance, is considered a limiting agent as are user defined min_date_taken and min_date_upload parameters — If no limiting factor is passed we return only photos added in the last 12 hours (though we may extend the limit in the future). 
  'geoContext': "geoContext_example", // String | Geo context is a numeric value representing the photo's geotagginess beyond latitude and longitude. For example, you may wish to search for photos that were taken \"indoors\" or \"outdoors\". The current list of context IDs is: 0, not defined. 1, indoors. 2, outdoors. Geo queries require some sort of limiting agent in order to prevent the database from crying. This is basically like the check against \"parameterless searches\" for queries without a geo component. A tag, for instance, is considered a limiting agent as are user defined min_date_taken and min_date_upload parameters — If no limiting factor is passed we return only photos added in the last 12 hours (though we may extend the limit in the future). 
  'lat': "lat_example", // String | A valid latitude, in decimal format, for doing radial geo queries. Geo queries require some sort of limiting agent in order to prevent the database from crying. This is basically like the check against \"parameterless searches\" for queries without a geo component. A tag, for instance, is considered a limiting agent as are user defined min_date_taken and min_date_upload parameters — If no limiting factor is passed we return only photos added in the last 12 hours (though we may extend the limit in the future). 
  'lon': "lon_example", // String | A valid longitude, in decimal format, for doing radial geo queries. Geo queries require some sort of limiting agent in order to prevent the database from crying. This is basically like the check against \"parameterless searches\" for queries without a geo component. A tag, for instance, is considered a limiting agent as are user defined min_date_taken and min_date_upload parameters — If no limiting factor is passed we return only photos added in the last 12 hours (though we may extend the limit in the future). 
  'radius': 3.4, // Number | A valid radius used for geo queries, greater than zero and less than 20 miles (or 32 kilometers), for use with point-based geo queries. The default value is 5 (km).
  'radiusUnits': "radiusUnits_example", // String | The unit of measure when doing radial geo queries. Valid options are \"mi\" (miles) and \"km\" (kilometers). The default is \"km\".
  'isCommons': true, // Boolean | Limit the scope of the search to only photos that are part of the Flickr Commons project. Default is false.
  'inGallery': true, // Boolean | Limit the scope of the search to only photos that are in a gallery? Default is false, search all photos.
  'isGetty': true, // Boolean | Limit the scope of the search to only photos that are for sale on Getty. Default is false.
  'perPage': 3.4, // Number | Number of photos to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is 500.
  'page': 3.4 // Number | The page of results to return. If this argument is omitted, it defaults to 1.
};
apiInstance.getMediaBySearch(apiKey, opts, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **text** | **String**| A free text search. Photos who&#39;s title, description or tags contain the text will be returned. You can exclude results that match a term by prepending it with a - character. | [optional] 
 **tags** | **String**| A comma-delimited list of tags. Photos with one or more of the tags listed will be returned. You can exclude results that match a term by prepending it with a - character. | [optional] 
 **userId** | **String**| The NSID of the user who&#39;s photo to search. If this parameter isn&#39;t passed then everybody&#39;s public photos will be searched. A value of \&quot;me\&quot; will search against the calling user&#39;s photos for authenticated calls. | [optional] 
 **minUploadDate** | **String**| Minimum upload date. Photos with an upload date greater than or equal to this value will be returned. The date can be in the form of a unix timestamp or mysql datetime. | [optional] 
 **maxUploadDate** | **String**| Maximum upload date. Photos with an upload date less than or equal to this value will be returned. The date can be in the form of a unix timestamp or mysql datetime. | [optional] 
 **minTakenDate** | **String**| Minimum taken date. Photos with an taken date greater than or equal to this value will be returned. The date can be in the form of a mysql datetime or unix timestamp. | [optional] 
 **maxTakenDate** | **String**| Maximum taken date. Photos with an taken date less than or equal to this value will be returned. The date can be in the form of a mysql datetime or unix timestamp. | [optional] 
 **license** | **String**| The license id for photos (for possible values see the flickr.photos.licenses.getInfo method). Multiple licenses may be comma-separated. | [optional] 
 **sort** | **String**| The order in which to sort returned photos. Deafults to date-posted-desc (unless you are doing a radial geo query, in which case the default sorting is by ascending distance from the point specified). The possible values are:   date-posted-asc,   date-posted-desc,   date-taken-asc,   date-taken-desc,   interestingness-desc,   interestingness-asc, and   relevance.  | [optional] 
 **privacyFilter** | **Number**| Return photos only matching a certain privacy level. This only applies when making an authenticated call to view photos you own. Valid values are:,   1: public photos,   2: private photos visible to friends,   3: private photos visible to family,   4: private photos visible to friends &amp; family,   5: completely private photos  | [optional] 
 **bbox** | **String**| A comma-delimited list of 4 values defining the Bounding Box of the area that will be searched. | [optional] 
 **accuracy** | **String**| Recorded accuracy level of the location information. Current range is 1-16:   World level is 1   Country is ~3   Region is ~6   City is ~11   Street is ~16  | [optional] 
 **safeSearch** | **Number**| Safe search setting:   1: for safe,   2: for moderate,   3: for restricted  | [optional] 
 **contentType** | **Number**| Content Type setting:   1: photos only.   2: screenshots only.   3: &#39;other&#39; only.   4: photos and screenshots.   5: screenshots and &#39;other&#39;.   6: photos and &#39;other&#39;.   7: photos, screenshots, and &#39;other&#39; (all).  | [optional] 
 **machineTags** | **String**| Aside from passing in a fully formed machine tag, there is a special syntax for searching on specific properties : Find photos using the &#39;dc&#39; namespace : \&quot;machine_tags\&quot; &#x3D;&gt; \&quot;dc:\&quot; Find photos with a title in the &#39;dc&#39; namespace : \&quot;machine_tags\&quot; &#x3D;&gt; \&quot;dc:title&#x3D;\&quot; Find photos titled \&quot;mr. camera\&quot; in the &#39;dc&#39; namespace : \&quot;machine_tags\&quot; &#x3D;&gt; \&quot;dc:title&#x3D;\\\&quot;mr. camera\\\&quot; Find photos whose value is \&quot;mr. camera\&quot; : \&quot;machine_tags\&quot; &#x3D;&gt; \&quot;*:*&#x3D;\\\&quot;mr. camera\\\&quot;\&quot; Find photos that have a title, in any namespace : \&quot;machine_tags\&quot; &#x3D;&gt; \&quot;*:title&#x3D;\&quot; Find photos that have a title, in any namespace, whose value is \&quot;mr. camera\&quot; : \&quot;machine_tags\&quot; &#x3D;&gt; \&quot;*:title&#x3D;\\\&quot;mr. camera\\\&quot;\&quot; Find photos, in the &#39;dc&#39; namespace whose value is \&quot;mr. camera\&quot; : \&quot;machine_tags\&quot; &#x3D;&gt; \&quot;dc:*&#x3D;\\\&quot;mr. camera\\\&quot;\&quot; Multiple machine tags may be queried by passing a comma-separated list. The number of machine tags you can pass in a single query depends on the tag mode (AND or OR) that you are querying with. \&quot;AND\&quot; queries are limited to (16) machine tags. \&quot;OR\&quot; queries are limited to (8).  | [optional] 
 **machineTagMode** | **String**| Either &#39;any&#39; for an OR combination of tags, or &#39;all&#39; for an AND combination. Defaults to &#39;any&#39; if not specified. | [optional] 
 **groupId** | **String**| The id of a group who&#39;s pool to search. If specified, only matching photos posted to the group&#39;s pool will be returned. | [optional] 
 **contacts** | **String**| Search your contacts. Either &#39;all&#39; or &#39;ff&#39; for just friends and family. (Experimental) | [optional] 
 **woeId** | **String**| A 32-bit identifier that uniquely represents spatial entities. (not used if bbox argument is present). | [optional] 
 **placeId** | **String**| A Flickr place id. (not used if bbox argument is present). Geo queries require some sort of limiting agent in order to prevent the database from crying. This is basically like the check against \&quot;parameterless searches\&quot; for queries without a geo component. A tag, for instance, is considered a limiting agent as are user defined min_date_taken and min_date_upload parameters — If no limiting factor is passed we return only photos added in the last 12 hours (though we may extend the limit in the future).  | [optional] 
 **media** | **String**| Filter results by media type. Possible values are all (default), photos or videos | [optional] 
 **hasGeo** | **String**| Any photo that has been geotagged, or if the value is \&quot;0\&quot; any photo that has not been geotagged. Geo queries require some sort of limiting agent in order to prevent the database from crying. This is basically like the check against \&quot;parameterless searches\&quot; for queries without a geo component. A tag, for instance, is considered a limiting agent as are user defined min_date_taken and min_date_upload parameters — If no limiting factor is passed we return only photos added in the last 12 hours (though we may extend the limit in the future).  | [optional] 
 **geoContext** | **String**| Geo context is a numeric value representing the photo&#39;s geotagginess beyond latitude and longitude. For example, you may wish to search for photos that were taken \&quot;indoors\&quot; or \&quot;outdoors\&quot;. The current list of context IDs is: 0, not defined. 1, indoors. 2, outdoors. Geo queries require some sort of limiting agent in order to prevent the database from crying. This is basically like the check against \&quot;parameterless searches\&quot; for queries without a geo component. A tag, for instance, is considered a limiting agent as are user defined min_date_taken and min_date_upload parameters — If no limiting factor is passed we return only photos added in the last 12 hours (though we may extend the limit in the future).  | [optional] 
 **lat** | **String**| A valid latitude, in decimal format, for doing radial geo queries. Geo queries require some sort of limiting agent in order to prevent the database from crying. This is basically like the check against \&quot;parameterless searches\&quot; for queries without a geo component. A tag, for instance, is considered a limiting agent as are user defined min_date_taken and min_date_upload parameters — If no limiting factor is passed we return only photos added in the last 12 hours (though we may extend the limit in the future).  | [optional] 
 **lon** | **String**| A valid longitude, in decimal format, for doing radial geo queries. Geo queries require some sort of limiting agent in order to prevent the database from crying. This is basically like the check against \&quot;parameterless searches\&quot; for queries without a geo component. A tag, for instance, is considered a limiting agent as are user defined min_date_taken and min_date_upload parameters — If no limiting factor is passed we return only photos added in the last 12 hours (though we may extend the limit in the future).  | [optional] 
 **radius** | **Number**| A valid radius used for geo queries, greater than zero and less than 20 miles (or 32 kilometers), for use with point-based geo queries. The default value is 5 (km). | [optional] 
 **radiusUnits** | **String**| The unit of measure when doing radial geo queries. Valid options are \&quot;mi\&quot; (miles) and \&quot;km\&quot; (kilometers). The default is \&quot;km\&quot;. | [optional] 
 **isCommons** | **Boolean**| Limit the scope of the search to only photos that are part of the Flickr Commons project. Default is false. | [optional] 
 **inGallery** | **Boolean**| Limit the scope of the search to only photos that are in a gallery? Default is false, search all photos. | [optional] 
 **isGetty** | **Boolean**| Limit the scope of the search to only photos that are for sale on Getty. Default is false. | [optional] 
 **perPage** | **Number**| Number of photos to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is 500. | [optional] 
 **page** | **Number**| The page of results to return. If this argument is omitted, it defaults to 1. | [optional] 

### Return type

[**GetFavoritesByPersonID200Response**](GetFavoritesByPersonID200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPersonByID

> GetPersonByID200Response getPersonByID(apiKey, opts)



Returns a person

### Example

```javascript
import FlickrApiSchema from 'flickr_api_schema';

let apiInstance = new FlickrApiSchema.PublicApi();
let apiKey = "apiKey_example"; // String | 
let opts = {
  'userId': "userId_example" // String | 
};
apiInstance.getPersonByID(apiKey, opts, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **userId** | **String**|  | [optional] 

### Return type

[**GetPersonByID200Response**](GetPersonByID200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPhotoByID

> GetPhotoByID200Response getPhotoByID(apiKey, photoId)



Returns a photo

### Example

```javascript
import FlickrApiSchema from 'flickr_api_schema';

let apiInstance = new FlickrApiSchema.PublicApi();
let apiKey = "apiKey_example"; // String | 
let photoId = "photoId_example"; // String | 
apiInstance.getPhotoByID(apiKey, photoId, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **photoId** | **String**|  | 

### Return type

[**GetPhotoByID200Response**](GetPhotoByID200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPhotoExifByID

> GetPhotoExifByID200Response getPhotoExifByID(apiKey, photoId, opts)



Retrieves a list of EXIF/TIFF/GPS tags for a given photo. The calling user must have permission to view the photo.

### Example

```javascript
import FlickrApiSchema from 'flickr_api_schema';

let apiInstance = new FlickrApiSchema.PublicApi();
let apiKey = "apiKey_example"; // String | 
let photoId = "photoId_example"; // String | 
let opts = {
  'secret': "secret_example" // String | 
};
apiInstance.getPhotoExifByID(apiKey, photoId, opts, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **photoId** | **String**|  | 
 **secret** | **String**|  | [optional] 

### Return type

[**GetPhotoExifByID200Response**](GetPhotoExifByID200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPhotoSizesByID

> GetPhotoSizesByID200Response getPhotoSizesByID(apiKey, photoId)



Returns photo sizes

### Example

```javascript
import FlickrApiSchema from 'flickr_api_schema';

let apiInstance = new FlickrApiSchema.PublicApi();
let apiKey = "apiKey_example"; // String | 
let photoId = "photoId_example"; // String | 
apiInstance.getPhotoSizesByID(apiKey, photoId, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **photoId** | **String**|  | 

### Return type

[**GetPhotoSizesByID200Response**](GetPhotoSizesByID200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPhotolistContextByID

> GetFavoritesContextByID200Response getPhotolistContextByID(apiKey, photoId, photolistId)



Returns next and previous photos in a photo list

### Example

```javascript
import FlickrApiSchema from 'flickr_api_schema';

let apiInstance = new FlickrApiSchema.PublicApi();
let apiKey = "apiKey_example"; // String | 
let photoId = "photoId_example"; // String | 
let photolistId = "photolistId_example"; // String | 
apiInstance.getPhotolistContextByID(apiKey, photoId, photolistId, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **photoId** | **String**|  | 
 **photolistId** | **String**|  | 

### Return type

[**GetFavoritesContextByID200Response**](GetFavoritesContextByID200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPhotostreamContextByID

> GetFavoritesContextByID200Response getPhotostreamContextByID(apiKey, photoId)



Returns next and previous photos for a photo in a photostream

### Example

```javascript
import FlickrApiSchema from 'flickr_api_schema';

let apiInstance = new FlickrApiSchema.PublicApi();
let apiKey = "apiKey_example"; // String | 
let photoId = "photoId_example"; // String | 
apiInstance.getPhotostreamContextByID(apiKey, photoId, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **photoId** | **String**|  | 

### Return type

[**GetFavoritesContextByID200Response**](GetFavoritesContextByID200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRequestToken

> String getRequestToken(oauthConsumerKey, oauthNonce, oauthTimestamp, oauthSignatureMethod, oauthVersion, oauthSignature, oauthCallback)



Returns an oauth token and oauth token secret

### Example

```javascript
import FlickrApiSchema from 'flickr_api_schema';

let apiInstance = new FlickrApiSchema.PublicApi();
let oauthConsumerKey = "oauthConsumerKey_example"; // String | 
let oauthNonce = "oauthNonce_example"; // String | 
let oauthTimestamp = "oauthTimestamp_example"; // String | 
let oauthSignatureMethod = "oauthSignatureMethod_example"; // String | 
let oauthVersion = "oauthVersion_example"; // String | 
let oauthSignature = "oauthSignature_example"; // String | 
let oauthCallback = "oauthCallback_example"; // String | 
apiInstance.getRequestToken(oauthConsumerKey, oauthNonce, oauthTimestamp, oauthSignatureMethod, oauthVersion, oauthSignature, oauthCallback, (error, data, response) => {
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
 **oauthConsumerKey** | **String**|  | 
 **oauthNonce** | **String**|  | 
 **oauthTimestamp** | **String**|  | 
 **oauthSignatureMethod** | **String**|  | 
 **oauthVersion** | **String**|  | 
 **oauthSignature** | **String**|  | 
 **oauthCallback** | **String**|  | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## restmethodflickrGroupsPoolsGetContextGet

> GetFavoritesContextByID200Response restmethodflickrGroupsPoolsGetContextGet(apiKey, photoId, opts)



Returns next and previous photos for a photo in a group pool

### Example

```javascript
import FlickrApiSchema from 'flickr_api_schema';

let apiInstance = new FlickrApiSchema.PublicApi();
let apiKey = "apiKey_example"; // String | 
let photoId = "photoId_example"; // String | 
let opts = {
  'groupId': "groupId_example" // String | 
};
apiInstance.restmethodflickrGroupsPoolsGetContextGet(apiKey, photoId, opts, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **photoId** | **String**|  | 
 **groupId** | **String**|  | [optional] 

### Return type

[**GetFavoritesContextByID200Response**](GetFavoritesContextByID200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## uploadPhoto

> Object uploadPhoto(apiKey, photo, opts)



Uploads a new photo to Flickr

### Example

```javascript
import FlickrApiSchema from 'flickr_api_schema';

let apiInstance = new FlickrApiSchema.PublicApi();
let apiKey = "apiKey_example"; // String | 
let photo = "/path/to/file"; // File | 
let opts = {
  'contentType': "contentType_example", // String | 
  'description': "description_example", // String | 
  'hidden': "hidden_example", // String | 
  'isFamily': "isFamily_example", // String | 
  'isFriend': "isFriend_example", // String | 
  'isPublic': "isPublic_example", // String | 
  'safetyLevel': "safetyLevel_example", // String | 
  'tags': "tags_example", // String | 
  'title': "title_example" // String | 
};
apiInstance.uploadPhoto(apiKey, photo, opts, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **photo** | **File**|  | 
 **contentType** | **String**|  | [optional] 
 **description** | **String**|  | [optional] 
 **hidden** | **String**|  | [optional] 
 **isFamily** | **String**|  | [optional] 
 **isFriend** | **String**|  | [optional] 
 **isPublic** | **String**|  | [optional] 
 **safetyLevel** | **String**|  | [optional] 
 **tags** | **String**|  | [optional] 
 **title** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

