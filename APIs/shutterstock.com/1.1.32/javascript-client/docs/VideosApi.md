# ShutterstockApiExplorer.VideosApi

All URIs are relative to *https://api.shutterstock.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addVideoCollectionItems**](VideosApi.md#addVideoCollectionItems) | **POST** /v2/videos/collections/{id}/items | Add videos to collections
[**createVideoCollection**](VideosApi.md#createVideoCollection) | **POST** /v2/videos/collections | Create video collections
[**deleteVideoCollection**](VideosApi.md#deleteVideoCollection) | **DELETE** /v2/videos/collections/{id} | Delete video collections
[**deleteVideoCollectionItems**](VideosApi.md#deleteVideoCollectionItems) | **DELETE** /v2/videos/collections/{id}/items | Remove videos from collections
[**downloadVideos**](VideosApi.md#downloadVideos) | **POST** /v2/videos/licenses/{id}/downloads | Download videos
[**findSimilarVideos**](VideosApi.md#findSimilarVideos) | **GET** /v2/videos/{id}/similar | List similar videos
[**getFeaturedVideoCollection**](VideosApi.md#getFeaturedVideoCollection) | **GET** /v2/videos/collections/featured/{id} | Get the details of featured video collections
[**getFeaturedVideoCollectionItems**](VideosApi.md#getFeaturedVideoCollectionItems) | **GET** /v2/videos/collections/featured/{id}/items | Get the contents of featured video collections
[**getFeaturedVideoCollectionList**](VideosApi.md#getFeaturedVideoCollectionList) | **GET** /v2/videos/collections/featured | List featured video collections
[**getUpdatedVideos**](VideosApi.md#getUpdatedVideos) | **GET** /v2/videos/updated | List updated videos
[**getVideo**](VideosApi.md#getVideo) | **GET** /v2/videos/{id} | Get details about videos
[**getVideoCollection**](VideosApi.md#getVideoCollection) | **GET** /v2/videos/collections/{id} | Get the details of video collections
[**getVideoCollectionItems**](VideosApi.md#getVideoCollectionItems) | **GET** /v2/videos/collections/{id}/items | Get the contents of video collections
[**getVideoCollectionList**](VideosApi.md#getVideoCollectionList) | **GET** /v2/videos/collections | List video collections
[**getVideoLicenseList**](VideosApi.md#getVideoLicenseList) | **GET** /v2/videos/licenses | List video licenses
[**getVideoList**](VideosApi.md#getVideoList) | **GET** /v2/videos | List videos
[**getVideoSuggestions**](VideosApi.md#getVideoSuggestions) | **GET** /v2/videos/search/suggestions | Get suggestions for a search term
[**licenseVideos**](VideosApi.md#licenseVideos) | **POST** /v2/videos/licenses | License videos
[**listVideoCategories**](VideosApi.md#listVideoCategories) | **GET** /v2/videos/categories | List video categories
[**renameVideoCollection**](VideosApi.md#renameVideoCollection) | **POST** /v2/videos/collections/{id} | Rename video collections
[**searchVideos**](VideosApi.md#searchVideos) | **GET** /v2/videos/search | Search for videos



## addVideoCollectionItems

> addVideoCollectionItems(id, collectionItemRequest)

Add videos to collections

This endpoint adds one or more videos to a collection by video IDs.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.VideosApi();
let id = "17555176"; // String | The ID of the collection to which items should be added
let collectionItemRequest = {"items":[{"id":"10120264"},{"id":"24419024"}]}; // CollectionItemRequest | Array of video IDs to add to the collection
apiInstance.addVideoCollectionItems(id, collectionItemRequest, (error, data, response) => {
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
 **id** | **String**| The ID of the collection to which items should be added | 
 **collectionItemRequest** | [**CollectionItemRequest**](CollectionItemRequest.md)| Array of video IDs to add to the collection | 

### Return type

null (empty response body)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## createVideoCollection

> CollectionCreateResponse createVideoCollection(collectionCreateRequest)

Create video collections

This endpoint creates one or more collections (clipboxes). To add videos to collections, use &#x60;POST /v2/videos/collections/{id}/items&#x60;.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.VideosApi();
let collectionCreateRequest = {"$ref":"#/components/schemas/CollectionCreateRequest/example"}; // CollectionCreateRequest | Collection metadata
apiInstance.createVideoCollection(collectionCreateRequest, (error, data, response) => {
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


## deleteVideoCollection

> deleteVideoCollection(id)

Delete video collections

This endpoint deletes a collection.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.VideosApi();
let id = "17555176"; // String | The ID of the collection to delete
apiInstance.deleteVideoCollection(id, (error, data, response) => {
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
 **id** | **String**| The ID of the collection to delete | 

### Return type

null (empty response body)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteVideoCollectionItems

> deleteVideoCollectionItems(id, opts)

Remove videos from collections

This endpoint removes one or more videos from a collection.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.VideosApi();
let id = "17555176"; // String | The ID of the Collection from which items will be deleted
let opts = {
  'itemId': ["null"] // [String] | One or more video IDs to remove from the collection
};
apiInstance.deleteVideoCollectionItems(id, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the Collection from which items will be deleted | 
 **itemId** | [**[String]**](String.md)| One or more video IDs to remove from the collection | [optional] 

### Return type

null (empty response body)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## downloadVideos

> Url downloadVideos(id, redownloadVideo)

Download videos

This endpoint redownloads videos that you have already received a license for.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.VideosApi();
let id = "e123"; // String | The license ID of the item to (re)download. The download links in the response are valid for 8 hours.
let redownloadVideo = {"$ref":"#/components/schemas/RedownloadVideo/example"}; // RedownloadVideo | Information about the videos to redownload
apiInstance.downloadVideos(id, redownloadVideo, (error, data, response) => {
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
 **id** | **String**| The license ID of the item to (re)download. The download links in the response are valid for 8 hours. | 
 **redownloadVideo** | [**RedownloadVideo**](RedownloadVideo.md)| Information about the videos to redownload | 

### Return type

[**Url**](Url.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## findSimilarVideos

> VideoSearchResults findSimilarVideos(id, opts)

List similar videos

This endpoint searches for videos that are similar to a video that you specify.

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

let apiInstance = new ShutterstockApiExplorer.VideosApi();
let id = "2140697"; // String | The ID of a video for which similar videos should be returned
let opts = {
  'language': new ShutterstockApiExplorer.Language(), // Language | Language for the keywords and categories in the response
  'page': 1, // Number | Page number
  'perPage': 20, // Number | Number of results per page
  'view': "'minimal'" // String | Amount of detail to render in the response
};
apiInstance.findSimilarVideos(id, opts, (error, data, response) => {
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
 **id** | **String**| The ID of a video for which similar videos should be returned | 
 **language** | [**Language**](.md)| Language for the keywords and categories in the response | [optional] 
 **page** | **Number**| Page number | [optional] [default to 1]
 **perPage** | **Number**| Number of results per page | [optional] [default to 20]
 **view** | **String**| Amount of detail to render in the response | [optional] [default to &#39;minimal&#39;]

### Return type

[**VideoSearchResults**](VideoSearchResults.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFeaturedVideoCollection

> FeaturedCollection getFeaturedVideoCollection(id, opts)

Get the details of featured video collections

This endpoint gets more detailed information about a featured video collection, including its cover video and timestamps for its creation and most recent update. To get the videos, use &#x60;GET /v2/videos/collections/featured/{id}/items&#x60;.

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

let apiInstance = new ShutterstockApiExplorer.VideosApi();
let id = "136351027"; // String | Collection ID
let opts = {
  'embed': "embed_example" // String | What information to include in the response, such as a URL to the collection
};
apiInstance.getFeaturedVideoCollection(id, opts, (error, data, response) => {
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
 **embed** | **String**| What information to include in the response, such as a URL to the collection | [optional] 

### Return type

[**FeaturedCollection**](FeaturedCollection.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFeaturedVideoCollectionItems

> VideoCollectionItemDataList getFeaturedVideoCollectionItems(id, opts)

Get the contents of featured video collections

This endpoint lists the IDs of videos in a featured collection and the date that each was added.

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

let apiInstance = new ShutterstockApiExplorer.VideosApi();
let id = "136351027"; // String | Collection ID
let opts = {
  'page': 1, // Number | Page number
  'perPage': 100 // Number | Number of results per page
};
apiInstance.getFeaturedVideoCollectionItems(id, opts, (error, data, response) => {
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

### Return type

[**VideoCollectionItemDataList**](VideoCollectionItemDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFeaturedVideoCollectionList

> FeaturedCollectionDataList getFeaturedVideoCollectionList(opts)

List featured video collections

This endpoint lists featured video collections and a name and cover video for each collection.

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

let apiInstance = new ShutterstockApiExplorer.VideosApi();
let opts = {
  'embed': "share_url" // String | What information to include in the response, such as a URL to the collection
};
apiInstance.getFeaturedVideoCollectionList(opts, (error, data, response) => {
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
 **embed** | **String**| What information to include in the response, such as a URL to the collection | [optional] 

### Return type

[**FeaturedCollectionDataList**](FeaturedCollectionDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUpdatedVideos

> UpdatedMediaDataList getUpdatedVideos(opts)

List updated videos

This endpoint lists videos that have been updated in the specified time period to update content management systems (CMS) or digital asset management (DAM) systems. In most cases, use the &#x60;interval&#x60; parameter to show videos that were updated recently, but you can also use the &#x60;start_date&#x60; and &#x60;end_date&#x60; parameters to specify a range of no more than three days. Do not use the &#x60;interval&#x60; parameter with either &#x60;start_date&#x60; or &#x60;end_date&#x60;.

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

let apiInstance = new ShutterstockApiExplorer.VideosApi();
let opts = {
  'startDate': new Date("2020-05-29"), // Date | Show videos updated on or after the specified date
  'endDate': new Date("2021-05-29"), // Date | Show videos updated before the specified date
  'interval': "'1 HOUR'", // String | Show videos updated in the specified time period, where the time period is an interval (like SQL INTERVAL) such as 1 DAY, 6 HOUR, or 30 MINUTE; the default is 1 HOUR, which shows videos that were updated in the hour preceding the request
  'page': 1, // Number | Page number
  'perPage': 100, // Number | Number of results per page
  'sort': "'newest'" // String | Sort by oldest or newest videos first
};
apiInstance.getUpdatedVideos(opts, (error, data, response) => {
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
 **startDate** | **Date**| Show videos updated on or after the specified date | [optional] 
 **endDate** | **Date**| Show videos updated before the specified date | [optional] 
 **interval** | **String**| Show videos updated in the specified time period, where the time period is an interval (like SQL INTERVAL) such as 1 DAY, 6 HOUR, or 30 MINUTE; the default is 1 HOUR, which shows videos that were updated in the hour preceding the request | [optional] [default to &#39;1 HOUR&#39;]
 **page** | **Number**| Page number | [optional] [default to 1]
 **perPage** | **Number**| Number of results per page | [optional] [default to 100]
 **sort** | **String**| Sort by oldest or newest videos first | [optional] [default to &#39;newest&#39;]

### Return type

[**UpdatedMediaDataList**](UpdatedMediaDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVideo

> Video getVideo(id, opts)

Get details about videos

This endpoint shows information about a video, including URLs to previews and the sizes that it is available in.

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

let apiInstance = new ShutterstockApiExplorer.VideosApi();
let id = "639703"; // String | Video ID
let opts = {
  'language': new ShutterstockApiExplorer.Language(), // Language | Language for the keywords and categories in the response
  'view': "'full'", // String | Amount of detail to render in the response
  'searchId': "00000000-0000-0000-0000-000000000000" // String | The ID of the search that is related to this request
};
apiInstance.getVideo(id, opts, (error, data, response) => {
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
 **id** | **String**| Video ID | 
 **language** | [**Language**](.md)| Language for the keywords and categories in the response | [optional] 
 **view** | **String**| Amount of detail to render in the response | [optional] [default to &#39;full&#39;]
 **searchId** | **String**| The ID of the search that is related to this request | [optional] 

### Return type

[**Video**](Video.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVideoCollection

> Collection getVideoCollection(id, opts)

Get the details of video collections

This endpoint gets more detailed information about a collection, including the timestamp for its creation and the number of videos in it. To get the videos in collections, use GET /v2/videos/collections/{id}/items.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.VideosApi();
let id = "17555176"; // String | The ID of the collection to return
let opts = {
  'embed': ["null"], // [String] | Which sharing information to include in the response, such as a URL to the collection
  'shareCode': "shareCode_example" // String | Code to retrieve a shared collection
};
apiInstance.getVideoCollection(id, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the collection to return | 
 **embed** | [**[String]**](String.md)| Which sharing information to include in the response, such as a URL to the collection | [optional] 
 **shareCode** | **String**| Code to retrieve a shared collection | [optional] 

### Return type

[**Collection**](Collection.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVideoCollectionItems

> CollectionItemDataList getVideoCollectionItems(id, opts)

Get the contents of video collections

This endpoint lists the IDs of videos in a collection and the date that each was added.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.VideosApi();
let id = "17555176"; // String | Collection ID
let opts = {
  'page': 1, // Number | Page number
  'perPage': 100, // Number | Number of results per page
  'shareCode': "shareCode_example", // String | Code to retrieve the contents of a shared collection
  'sort': "'oldest'" // String | Sort order
};
apiInstance.getVideoCollectionItems(id, opts, (error, data, response) => {
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


## getVideoCollectionList

> CollectionDataList getVideoCollectionList(opts)

List video collections

This endpoint lists your collections of videos and their basic attributes.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.VideosApi();
let opts = {
  'page': 1, // Number | Page number
  'perPage': 100, // Number | Number of results per page
  'embed': ["null"] // [String] | Which sharing information to include in the response, such as a URL to the collection
};
apiInstance.getVideoCollectionList(opts, (error, data, response) => {
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


## getVideoLicenseList

> DownloadHistoryDataList getVideoLicenseList(opts)

List video licenses

This endpoint lists existing licenses.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.VideosApi();
let opts = {
  'videoId': "12345678", // String | Show licenses for the specified video ID
  'license': "standard", // String | Show videos that are available with the specified license, such as `standard` or `enhanced`; prepending a `-` sign excludes results from that license
  'page': 1, // Number | Page number
  'perPage': 20, // Number | Number of results per page
  'sort': "'newest'", // String | Sort by oldest or newest videos first
  'username': "aUniqueUsername", // String | Filter licenses by username of licensee
  'startDate': new Date("2021-03-29T13:25:13.521Z"), // Date | Show licenses created on or after the specified date
  'endDate': new Date("2021-03-29T13:25:13.521Z"), // Date | Show licenses created before the specified date
  'downloadAvailability': "'all'", // String | Filter licenses by download availability
  'teamHistory': false // Boolean | Set to true to see license history for all members of your team.
};
apiInstance.getVideoLicenseList(opts, (error, data, response) => {
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
 **videoId** | **String**| Show licenses for the specified video ID | [optional] 
 **license** | **String**| Show videos that are available with the specified license, such as &#x60;standard&#x60; or &#x60;enhanced&#x60;; prepending a &#x60;-&#x60; sign excludes results from that license | [optional] 
 **page** | **Number**| Page number | [optional] [default to 1]
 **perPage** | **Number**| Number of results per page | [optional] [default to 20]
 **sort** | **String**| Sort by oldest or newest videos first | [optional] [default to &#39;newest&#39;]
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


## getVideoList

> VideoDataList getVideoList(id, opts)

List videos

This endpoint lists information about one or more videos, including the aspect ratio and URLs to previews.

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

let apiInstance = new ShutterstockApiExplorer.VideosApi();
let id = ["null"]; // [String] | One or more video IDs
let opts = {
  'view': "'minimal'", // String | Amount of detail to render in the response
  'searchId': "00000000-0000-0000-0000-000000000000" // String | The ID of the search that is related to this request
};
apiInstance.getVideoList(id, opts, (error, data, response) => {
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
 **id** | [**[String]**](String.md)| One or more video IDs | 
 **view** | **String**| Amount of detail to render in the response | [optional] [default to &#39;minimal&#39;]
 **searchId** | **String**| The ID of the search that is related to this request | [optional] 

### Return type

[**VideoDataList**](VideoDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVideoSuggestions

> Suggestions getVideoSuggestions(query, opts)

Get suggestions for a search term

This endpoint provides autocomplete suggestions for partial search terms.

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

let apiInstance = new ShutterstockApiExplorer.VideosApi();
let query = "cats"; // String | Search term for which you want keyword suggestions
let opts = {
  'limit': 10 // Number | Limit the number of the suggestions
};
apiInstance.getVideoSuggestions(query, opts, (error, data, response) => {
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
 **query** | **String**| Search term for which you want keyword suggestions | 
 **limit** | **Number**| Limit the number of the suggestions | [optional] [default to 10]

### Return type

[**Suggestions**](Suggestions.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## licenseVideos

> LicenseVideoResultDataList licenseVideos(licenseVideoRequest, opts)

License videos

This endpoint gets licenses for one or more videos. You must specify the video IDs in the body parameter and the size and subscription ID either in the query parameter or with each video ID in the body parameter. Values in the body parameter override values in the query parameters. The download links in the response are valid for 8 hours.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.VideosApi();
let licenseVideoRequest = {"$ref":"#/components/schemas/LicenseVideoRequest/example"}; // LicenseVideoRequest | List of videos to request licenses for and information about each license transaction; these values override the defaults in the query parameters
let opts = {
  'subscriptionId': "s12345678", // String | The subscription ID to use for licensing
  'size': "'web'", // String | The size of the video to license
  'searchId': "searchId_example" // String | The Search ID that led to this licensing event
};
apiInstance.licenseVideos(licenseVideoRequest, opts, (error, data, response) => {
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
 **licenseVideoRequest** | [**LicenseVideoRequest**](LicenseVideoRequest.md)| List of videos to request licenses for and information about each license transaction; these values override the defaults in the query parameters | 
 **subscriptionId** | **String**| The subscription ID to use for licensing | [optional] 
 **size** | **String**| The size of the video to license | [optional] [default to &#39;web&#39;]
 **searchId** | **String**| The Search ID that led to this licensing event | [optional] 

### Return type

[**LicenseVideoResultDataList**](LicenseVideoResultDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listVideoCategories

> CategoryDataList listVideoCategories(opts)

List video categories

This endpoint lists the categories (Shutterstock-assigned genres) that videos can belong to.

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

let apiInstance = new ShutterstockApiExplorer.VideosApi();
let opts = {
  'language': new ShutterstockApiExplorer.Language() // Language | Language for the keywords and categories in the response
};
apiInstance.listVideoCategories(opts, (error, data, response) => {
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
 **language** | [**Language**](.md)| Language for the keywords and categories in the response | [optional] 

### Return type

[**CategoryDataList**](CategoryDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## renameVideoCollection

> renameVideoCollection(id, collectionUpdateRequest)

Rename video collections

This endpoint sets a new name for a collection.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.VideosApi();
let id = "17555176"; // String | The ID of the collection to rename
let collectionUpdateRequest = {"$ref":"#/components/schemas/CollectionUpdateRequest/example"}; // CollectionUpdateRequest | The new name for the collection
apiInstance.renameVideoCollection(id, collectionUpdateRequest, (error, data, response) => {
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
 **id** | **String**| The ID of the collection to rename | 
 **collectionUpdateRequest** | [**CollectionUpdateRequest**](CollectionUpdateRequest.md)| The new name for the collection | 

### Return type

null (empty response body)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## searchVideos

> VideoSearchResults searchVideos(opts)

Search for videos

This endpoint searches for videos. If you specify more than one search parameter, the API uses an AND condition. Array parameters can be specified multiple times; in this case, the API uses an AND or an OR condition with those values, depending on the parameter. You can also filter search terms out in the &#x60;query&#x60; parameter by prefixing the term with NOT.

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

let apiInstance = new ShutterstockApiExplorer.VideosApi();
let opts = {
  'addedDate': new Date("2020-05-29"), // Date | Show videos added on the specified date
  'addedDateStart': new Date("2020-05-29"), // Date | Show videos added on or after the specified date
  'addedDateEnd': new Date("2020-05-29"), // Date | Show videos added before the specified date
  'aspectRatio': "43", // String | Show videos with the specified aspect ratio
  'category': "category_example", // String | Show videos with the specified Shutterstock-defined category; specify a category name or ID
  'contributor': ["null"], // [String] | Show videos with the specified artist names or IDs
  'contributorCountry': ["null"], // [String] | Show videos from contributors in one or more specified countries
  'duration': 56, // Number | (Deprecated; use duration_from and duration_to instead) Show videos with the specified duration in seconds
  'durationFrom': 60, // Number | Show videos with the specified duration or longer in seconds
  'durationTo': 180, // Number | Show videos with the specified duration or shorter in seconds
  'fps': 3.4, // Number | (Deprecated; use fps_from and fps_to instead) Show videos with the specified frames per second
  'fpsFrom': 24, // Number | Show videos with the specified frames per second or more
  'fpsTo': 60, // Number | Show videos with the specified frames per second or fewer
  'keywordSafeSearch': true, // Boolean | Hide results with potentially unsafe keywords
  'language': new ShutterstockApiExplorer.Language(), // Language | Set query and result language (uses Accept-Language header if not set)
  'license': ["'commercial'"], // [String] | Show only videos with the specified license or licenses
  'model': ["null"], // [String] | Show videos with each of the specified models
  'page': 1, // Number | Page number
  'perPage': 20, // Number | Number of results per page
  'peopleAge': "20s", // String | Show videos that feature people of the specified age range
  'peopleEthnicity': ["null"], // [String] | Show videos with people of the specified ethnicities
  'peopleGender': "female", // String | Show videos with people with the specified gender
  'peopleNumber': 2, // Number | Show videos with the specified number of people
  'peopleModelReleased': true, // Boolean | Show only videos of people with a signed model release
  'query': "dogs running on the beach", // String | One or more search terms separated by spaces; you can use NOT to filter out videos that match a term
  'resolution': "4k", // String | Show videos with the specified resolution
  'safe': true, // Boolean | Enable or disable safe search
  'sort': "'popular'", // String | Sort by one of these categories
  'view': "'minimal'" // String | Amount of detail to render in the response
};
apiInstance.searchVideos(opts, (error, data, response) => {
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
 **addedDate** | **Date**| Show videos added on the specified date | [optional] 
 **addedDateStart** | **Date**| Show videos added on or after the specified date | [optional] 
 **addedDateEnd** | **Date**| Show videos added before the specified date | [optional] 
 **aspectRatio** | **String**| Show videos with the specified aspect ratio | [optional] 
 **category** | **String**| Show videos with the specified Shutterstock-defined category; specify a category name or ID | [optional] 
 **contributor** | [**[String]**](String.md)| Show videos with the specified artist names or IDs | [optional] 
 **contributorCountry** | [**[String]**](String.md)| Show videos from contributors in one or more specified countries | [optional] 
 **duration** | **Number**| (Deprecated; use duration_from and duration_to instead) Show videos with the specified duration in seconds | [optional] 
 **durationFrom** | **Number**| Show videos with the specified duration or longer in seconds | [optional] 
 **durationTo** | **Number**| Show videos with the specified duration or shorter in seconds | [optional] 
 **fps** | **Number**| (Deprecated; use fps_from and fps_to instead) Show videos with the specified frames per second | [optional] 
 **fpsFrom** | **Number**| Show videos with the specified frames per second or more | [optional] 
 **fpsTo** | **Number**| Show videos with the specified frames per second or fewer | [optional] 
 **keywordSafeSearch** | **Boolean**| Hide results with potentially unsafe keywords | [optional] [default to true]
 **language** | [**Language**](.md)| Set query and result language (uses Accept-Language header if not set) | [optional] 
 **license** | [**[String]**](String.md)| Show only videos with the specified license or licenses | [optional] 
 **model** | [**[String]**](String.md)| Show videos with each of the specified models | [optional] 
 **page** | **Number**| Page number | [optional] [default to 1]
 **perPage** | **Number**| Number of results per page | [optional] [default to 20]
 **peopleAge** | **String**| Show videos that feature people of the specified age range | [optional] 
 **peopleEthnicity** | [**[String]**](String.md)| Show videos with people of the specified ethnicities | [optional] 
 **peopleGender** | **String**| Show videos with people with the specified gender | [optional] 
 **peopleNumber** | **Number**| Show videos with the specified number of people | [optional] 
 **peopleModelReleased** | **Boolean**| Show only videos of people with a signed model release | [optional] 
 **query** | **String**| One or more search terms separated by spaces; you can use NOT to filter out videos that match a term | [optional] 
 **resolution** | **String**| Show videos with the specified resolution | [optional] 
 **safe** | **Boolean**| Enable or disable safe search | [optional] [default to true]
 **sort** | **String**| Sort by one of these categories | [optional] [default to &#39;popular&#39;]
 **view** | **String**| Amount of detail to render in the response | [optional] [default to &#39;minimal&#39;]

### Return type

[**VideoSearchResults**](VideoSearchResults.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

