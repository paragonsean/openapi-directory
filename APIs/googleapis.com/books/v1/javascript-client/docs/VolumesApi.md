# BooksApi.VolumesApi

All URIs are relative to *https://books.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**booksVolumesAssociatedList**](VolumesApi.md#booksVolumesAssociatedList) | **GET** /books/v1/volumes/{volumeId}/associated | 
[**booksVolumesGet**](VolumesApi.md#booksVolumesGet) | **GET** /books/v1/volumes/{volumeId} | 
[**booksVolumesList**](VolumesApi.md#booksVolumesList) | **GET** /books/v1/volumes | 
[**booksVolumesMybooksList**](VolumesApi.md#booksVolumesMybooksList) | **GET** /books/v1/volumes/mybooks | 
[**booksVolumesRecommendedList**](VolumesApi.md#booksVolumesRecommendedList) | **GET** /books/v1/volumes/recommended | 
[**booksVolumesRecommendedRate**](VolumesApi.md#booksVolumesRecommendedRate) | **POST** /books/v1/volumes/recommended/rate | 
[**booksVolumesUseruploadedList**](VolumesApi.md#booksVolumesUseruploadedList) | **GET** /books/v1/volumes/useruploaded | 



## booksVolumesAssociatedList

> Volumes booksVolumesAssociatedList(volumeId, opts)



Return a list of associated books.

### Example

```javascript
import BooksApi from 'books_api';
let defaultClient = BooksApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BooksApi.VolumesApi();
let volumeId = "volumeId_example"; // String | ID of the source volume.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'association': "association_example", // String | Association type.
  'locale': "locale_example", // String | ISO-639-1 language and ISO-3166-1 country code. Ex: 'en_US'. Used for generating recommendations.
  'maxAllowedMaturityRating': "maxAllowedMaturityRating_example", // String | The maximum allowed maturity rating of returned recommendations. Books with a higher maturity rating are filtered out.
  'source': "source_example" // String | String to identify the originator of this request.
};
apiInstance.booksVolumesAssociatedList(volumeId, opts, (error, data, response) => {
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
 **volumeId** | **String**| ID of the source volume. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **association** | **String**| Association type. | [optional] 
 **locale** | **String**| ISO-639-1 language and ISO-3166-1 country code. Ex: &#39;en_US&#39;. Used for generating recommendations. | [optional] 
 **maxAllowedMaturityRating** | **String**| The maximum allowed maturity rating of returned recommendations. Books with a higher maturity rating are filtered out. | [optional] 
 **source** | **String**| String to identify the originator of this request. | [optional] 

### Return type

[**Volumes**](Volumes.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## booksVolumesGet

> Volume booksVolumesGet(volumeId, opts)



Gets volume information for a single volume.

### Example

```javascript
import BooksApi from 'books_api';
let defaultClient = BooksApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BooksApi.VolumesApi();
let volumeId = "volumeId_example"; // String | ID of volume to retrieve.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'country': "country_example", // String | ISO-3166-1 code to override the IP-based location.
  'includeNonComicsSeries': true, // Boolean | Set to true to include non-comics series. Defaults to false.
  'partner': "partner_example", // String | Brand results for partner ID.
  'projection': "projection_example", // String | Restrict information returned to a set of selected fields.
  'source': "source_example", // String | string to identify the originator of this request.
  'userLibraryConsistentRead': true // Boolean | 
};
apiInstance.booksVolumesGet(volumeId, opts, (error, data, response) => {
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
 **volumeId** | **String**| ID of volume to retrieve. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **country** | **String**| ISO-3166-1 code to override the IP-based location. | [optional] 
 **includeNonComicsSeries** | **Boolean**| Set to true to include non-comics series. Defaults to false. | [optional] 
 **partner** | **String**| Brand results for partner ID. | [optional] 
 **projection** | **String**| Restrict information returned to a set of selected fields. | [optional] 
 **source** | **String**| string to identify the originator of this request. | [optional] 
 **userLibraryConsistentRead** | **Boolean**|  | [optional] 

### Return type

[**Volume**](Volume.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## booksVolumesList

> Volumes booksVolumesList(q, opts)



Performs a book search.

### Example

```javascript
import BooksApi from 'books_api';
let defaultClient = BooksApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BooksApi.VolumesApi();
let q = "q_example"; // String | Full-text search query string.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'download': "download_example", // String | Restrict to volumes by download availability.
  'filter': "filter_example", // String | Filter search results.
  'langRestrict': "langRestrict_example", // String | Restrict results to books with this language code.
  'libraryRestrict': "libraryRestrict_example", // String | Restrict search to this user's library.
  'maxAllowedMaturityRating': "maxAllowedMaturityRating_example", // String | The maximum allowed maturity rating of returned recommendations. Books with a higher maturity rating are filtered out.
  'maxResults': 56, // Number | Maximum number of results to return.
  'orderBy': "orderBy_example", // String | Sort search results.
  'partner': "partner_example", // String | Restrict and brand results for partner ID.
  'printType': "printType_example", // String | Restrict to books or magazines.
  'projection': "projection_example", // String | Restrict information returned to a set of selected fields.
  'showPreorders': true, // Boolean | Set to true to show books available for preorder. Defaults to false.
  'source': "source_example", // String | String to identify the originator of this request.
  'startIndex': 56 // Number | Index of the first result to return (starts at 0)
};
apiInstance.booksVolumesList(q, opts, (error, data, response) => {
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
 **q** | **String**| Full-text search query string. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **download** | **String**| Restrict to volumes by download availability. | [optional] 
 **filter** | **String**| Filter search results. | [optional] 
 **langRestrict** | **String**| Restrict results to books with this language code. | [optional] 
 **libraryRestrict** | **String**| Restrict search to this user&#39;s library. | [optional] 
 **maxAllowedMaturityRating** | **String**| The maximum allowed maturity rating of returned recommendations. Books with a higher maturity rating are filtered out. | [optional] 
 **maxResults** | **Number**| Maximum number of results to return. | [optional] 
 **orderBy** | **String**| Sort search results. | [optional] 
 **partner** | **String**| Restrict and brand results for partner ID. | [optional] 
 **printType** | **String**| Restrict to books or magazines. | [optional] 
 **projection** | **String**| Restrict information returned to a set of selected fields. | [optional] 
 **showPreorders** | **Boolean**| Set to true to show books available for preorder. Defaults to false. | [optional] 
 **source** | **String**| String to identify the originator of this request. | [optional] 
 **startIndex** | **Number**| Index of the first result to return (starts at 0) | [optional] 

### Return type

[**Volumes**](Volumes.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## booksVolumesMybooksList

> Volumes booksVolumesMybooksList(opts)



Return a list of books in My Library.

### Example

```javascript
import BooksApi from 'books_api';
let defaultClient = BooksApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BooksApi.VolumesApi();
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'acquireMethod': ["null"], // [String] | How the book was acquired
  'country': "country_example", // String | ISO-3166-1 code to override the IP-based location.
  'locale': "locale_example", // String | ISO-639-1 language and ISO-3166-1 country code. Ex:'en_US'. Used for generating recommendations.
  'maxResults': 56, // Number | Maximum number of results to return.
  'processingState': ["null"], // [String] | The processing state of the user uploaded volumes to be returned. Applicable only if the UPLOADED is specified in the acquireMethod.
  'source': "source_example", // String | String to identify the originator of this request.
  'startIndex': 56 // Number | Index of the first result to return (starts at 0)
};
apiInstance.booksVolumesMybooksList(opts, (error, data, response) => {
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
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **acquireMethod** | [**[String]**](String.md)| How the book was acquired | [optional] 
 **country** | **String**| ISO-3166-1 code to override the IP-based location. | [optional] 
 **locale** | **String**| ISO-639-1 language and ISO-3166-1 country code. Ex:&#39;en_US&#39;. Used for generating recommendations. | [optional] 
 **maxResults** | **Number**| Maximum number of results to return. | [optional] 
 **processingState** | [**[String]**](String.md)| The processing state of the user uploaded volumes to be returned. Applicable only if the UPLOADED is specified in the acquireMethod. | [optional] 
 **source** | **String**| String to identify the originator of this request. | [optional] 
 **startIndex** | **Number**| Index of the first result to return (starts at 0) | [optional] 

### Return type

[**Volumes**](Volumes.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## booksVolumesRecommendedList

> Volumes booksVolumesRecommendedList(opts)



Return a list of recommended books for the current user.

### Example

```javascript
import BooksApi from 'books_api';
let defaultClient = BooksApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BooksApi.VolumesApi();
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'locale': "locale_example", // String | ISO-639-1 language and ISO-3166-1 country code. Ex: 'en_US'. Used for generating recommendations.
  'maxAllowedMaturityRating': "maxAllowedMaturityRating_example", // String | The maximum allowed maturity rating of returned recommendations. Books with a higher maturity rating are filtered out.
  'source': "source_example" // String | String to identify the originator of this request.
};
apiInstance.booksVolumesRecommendedList(opts, (error, data, response) => {
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
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **locale** | **String**| ISO-639-1 language and ISO-3166-1 country code. Ex: &#39;en_US&#39;. Used for generating recommendations. | [optional] 
 **maxAllowedMaturityRating** | **String**| The maximum allowed maturity rating of returned recommendations. Books with a higher maturity rating are filtered out. | [optional] 
 **source** | **String**| String to identify the originator of this request. | [optional] 

### Return type

[**Volumes**](Volumes.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## booksVolumesRecommendedRate

> BooksVolumesRecommendedRateResponse booksVolumesRecommendedRate(rating, volumeId, opts)



Rate a recommended book for the current user.

### Example

```javascript
import BooksApi from 'books_api';
let defaultClient = BooksApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BooksApi.VolumesApi();
let rating = "rating_example"; // String | Rating to be given to the volume.
let volumeId = "volumeId_example"; // String | ID of the source volume.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'locale': "locale_example", // String | ISO-639-1 language and ISO-3166-1 country code. Ex: 'en_US'. Used for generating recommendations.
  'source': "source_example" // String | String to identify the originator of this request.
};
apiInstance.booksVolumesRecommendedRate(rating, volumeId, opts, (error, data, response) => {
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
 **rating** | **String**| Rating to be given to the volume. | 
 **volumeId** | **String**| ID of the source volume. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **locale** | **String**| ISO-639-1 language and ISO-3166-1 country code. Ex: &#39;en_US&#39;. Used for generating recommendations. | [optional] 
 **source** | **String**| String to identify the originator of this request. | [optional] 

### Return type

[**BooksVolumesRecommendedRateResponse**](BooksVolumesRecommendedRateResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## booksVolumesUseruploadedList

> Volumes booksVolumesUseruploadedList(opts)



Return a list of books uploaded by the current user.

### Example

```javascript
import BooksApi from 'books_api';
let defaultClient = BooksApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BooksApi.VolumesApi();
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'locale': "locale_example", // String | ISO-639-1 language and ISO-3166-1 country code. Ex: 'en_US'. Used for generating recommendations.
  'maxResults': 56, // Number | Maximum number of results to return.
  'processingState': ["null"], // [String] | The processing state of the user uploaded volumes to be returned.
  'source': "source_example", // String | String to identify the originator of this request.
  'startIndex': 56, // Number | Index of the first result to return (starts at 0)
  'volumeId': ["null"] // [String] | The ids of the volumes to be returned. If not specified all that match the processingState are returned.
};
apiInstance.booksVolumesUseruploadedList(opts, (error, data, response) => {
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
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **locale** | **String**| ISO-639-1 language and ISO-3166-1 country code. Ex: &#39;en_US&#39;. Used for generating recommendations. | [optional] 
 **maxResults** | **Number**| Maximum number of results to return. | [optional] 
 **processingState** | [**[String]**](String.md)| The processing state of the user uploaded volumes to be returned. | [optional] 
 **source** | **String**| String to identify the originator of this request. | [optional] 
 **startIndex** | **Number**| Index of the first result to return (starts at 0) | [optional] 
 **volumeId** | [**[String]**](String.md)| The ids of the volumes to be returned. If not specified all that match the processingState are returned. | [optional] 

### Return type

[**Volumes**](Volumes.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

