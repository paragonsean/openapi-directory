# BooksApi.LayersApi

All URIs are relative to *https://books.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**booksLayersAnnotationDataGet**](LayersApi.md#booksLayersAnnotationDataGet) | **GET** /books/v1/volumes/{volumeId}/layers/{layerId}/data/{annotationDataId} | 
[**booksLayersAnnotationDataList**](LayersApi.md#booksLayersAnnotationDataList) | **GET** /books/v1/volumes/{volumeId}/layers/{layerId}/data | 
[**booksLayersGet**](LayersApi.md#booksLayersGet) | **GET** /books/v1/volumes/{volumeId}/layersummary/{summaryId} | 
[**booksLayersList**](LayersApi.md#booksLayersList) | **GET** /books/v1/volumes/{volumeId}/layersummary | 
[**booksLayersVolumeAnnotationsGet**](LayersApi.md#booksLayersVolumeAnnotationsGet) | **GET** /books/v1/volumes/{volumeId}/layers/{layerId}/annotations/{annotationId} | 
[**booksLayersVolumeAnnotationsList**](LayersApi.md#booksLayersVolumeAnnotationsList) | **GET** /books/v1/volumes/{volumeId}/layers/{layerId} | 



## booksLayersAnnotationDataGet

> DictionaryAnnotationdata booksLayersAnnotationDataGet(volumeId, layerId, annotationDataId, contentVersion, opts)



Gets the annotation data.

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

let apiInstance = new BooksApi.LayersApi();
let volumeId = "volumeId_example"; // String | The volume to retrieve annotations for.
let layerId = "layerId_example"; // String | The ID for the layer to get the annotations.
let annotationDataId = "annotationDataId_example"; // String | The ID of the annotation data to retrieve.
let contentVersion = "contentVersion_example"; // String | The content version for the volume you are trying to retrieve.
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
  'allowWebDefinitions': true, // Boolean | For the dictionary layer. Whether or not to allow web definitions.
  'h': 56, // Number | The requested pixel height for any images. If height is provided width must also be provided.
  'locale': "locale_example", // String | The locale information for the data. ISO-639-1 language and ISO-3166-1 country code. Ex: 'en_US'.
  'scale': 56, // Number | The requested scale for the image.
  'source': "source_example", // String | String to identify the originator of this request.
  'w': 56 // Number | The requested pixel width for any images. If width is provided height must also be provided.
};
apiInstance.booksLayersAnnotationDataGet(volumeId, layerId, annotationDataId, contentVersion, opts, (error, data, response) => {
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
 **volumeId** | **String**| The volume to retrieve annotations for. | 
 **layerId** | **String**| The ID for the layer to get the annotations. | 
 **annotationDataId** | **String**| The ID of the annotation data to retrieve. | 
 **contentVersion** | **String**| The content version for the volume you are trying to retrieve. | 
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
 **allowWebDefinitions** | **Boolean**| For the dictionary layer. Whether or not to allow web definitions. | [optional] 
 **h** | **Number**| The requested pixel height for any images. If height is provided width must also be provided. | [optional] 
 **locale** | **String**| The locale information for the data. ISO-639-1 language and ISO-3166-1 country code. Ex: &#39;en_US&#39;. | [optional] 
 **scale** | **Number**| The requested scale for the image. | [optional] 
 **source** | **String**| String to identify the originator of this request. | [optional] 
 **w** | **Number**| The requested pixel width for any images. If width is provided height must also be provided. | [optional] 

### Return type

[**DictionaryAnnotationdata**](DictionaryAnnotationdata.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## booksLayersAnnotationDataList

> Annotationsdata booksLayersAnnotationDataList(volumeId, layerId, contentVersion, opts)



Gets the annotation data for a volume and layer.

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

let apiInstance = new BooksApi.LayersApi();
let volumeId = "volumeId_example"; // String | The volume to retrieve annotation data for.
let layerId = "layerId_example"; // String | The ID for the layer to get the annotation data.
let contentVersion = "contentVersion_example"; // String | The content version for the requested volume.
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
  'annotationDataId': ["null"], // [String] | The list of Annotation Data Ids to retrieve. Pagination is ignored if this is set.
  'h': 56, // Number | The requested pixel height for any images. If height is provided width must also be provided.
  'locale': "locale_example", // String | The locale information for the data. ISO-639-1 language and ISO-3166-1 country code. Ex: 'en_US'.
  'maxResults': 56, // Number | Maximum number of results to return
  'pageToken': "pageToken_example", // String | The value of the nextToken from the previous page.
  'scale': 56, // Number | The requested scale for the image.
  'source': "source_example", // String | String to identify the originator of this request.
  'updatedMax': "updatedMax_example", // String | RFC 3339 timestamp to restrict to items updated prior to this timestamp (exclusive).
  'updatedMin': "updatedMin_example", // String | RFC 3339 timestamp to restrict to items updated since this timestamp (inclusive).
  'w': 56 // Number | The requested pixel width for any images. If width is provided height must also be provided.
};
apiInstance.booksLayersAnnotationDataList(volumeId, layerId, contentVersion, opts, (error, data, response) => {
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
 **volumeId** | **String**| The volume to retrieve annotation data for. | 
 **layerId** | **String**| The ID for the layer to get the annotation data. | 
 **contentVersion** | **String**| The content version for the requested volume. | 
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
 **annotationDataId** | [**[String]**](String.md)| The list of Annotation Data Ids to retrieve. Pagination is ignored if this is set. | [optional] 
 **h** | **Number**| The requested pixel height for any images. If height is provided width must also be provided. | [optional] 
 **locale** | **String**| The locale information for the data. ISO-639-1 language and ISO-3166-1 country code. Ex: &#39;en_US&#39;. | [optional] 
 **maxResults** | **Number**| Maximum number of results to return | [optional] 
 **pageToken** | **String**| The value of the nextToken from the previous page. | [optional] 
 **scale** | **Number**| The requested scale for the image. | [optional] 
 **source** | **String**| String to identify the originator of this request. | [optional] 
 **updatedMax** | **String**| RFC 3339 timestamp to restrict to items updated prior to this timestamp (exclusive). | [optional] 
 **updatedMin** | **String**| RFC 3339 timestamp to restrict to items updated since this timestamp (inclusive). | [optional] 
 **w** | **Number**| The requested pixel width for any images. If width is provided height must also be provided. | [optional] 

### Return type

[**Annotationsdata**](Annotationsdata.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## booksLayersGet

> Layersummary booksLayersGet(volumeId, summaryId, opts)



Gets the layer summary for a volume.

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

let apiInstance = new BooksApi.LayersApi();
let volumeId = "volumeId_example"; // String | The volume to retrieve layers for.
let summaryId = "summaryId_example"; // String | The ID for the layer to get the summary for.
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
  'contentVersion': "contentVersion_example", // String | The content version for the requested volume.
  'source': "source_example" // String | String to identify the originator of this request.
};
apiInstance.booksLayersGet(volumeId, summaryId, opts, (error, data, response) => {
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
 **volumeId** | **String**| The volume to retrieve layers for. | 
 **summaryId** | **String**| The ID for the layer to get the summary for. | 
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
 **contentVersion** | **String**| The content version for the requested volume. | [optional] 
 **source** | **String**| String to identify the originator of this request. | [optional] 

### Return type

[**Layersummary**](Layersummary.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## booksLayersList

> Layersummaries booksLayersList(volumeId, opts)



List the layer summaries for a volume.

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

let apiInstance = new BooksApi.LayersApi();
let volumeId = "volumeId_example"; // String | The volume to retrieve layers for.
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
  'contentVersion': "contentVersion_example", // String | The content version for the requested volume.
  'maxResults': 56, // Number | Maximum number of results to return
  'pageToken': "pageToken_example", // String | The value of the nextToken from the previous page.
  'source': "source_example" // String | String to identify the originator of this request.
};
apiInstance.booksLayersList(volumeId, opts, (error, data, response) => {
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
 **volumeId** | **String**| The volume to retrieve layers for. | 
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
 **contentVersion** | **String**| The content version for the requested volume. | [optional] 
 **maxResults** | **Number**| Maximum number of results to return | [optional] 
 **pageToken** | **String**| The value of the nextToken from the previous page. | [optional] 
 **source** | **String**| String to identify the originator of this request. | [optional] 

### Return type

[**Layersummaries**](Layersummaries.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## booksLayersVolumeAnnotationsGet

> Volumeannotation booksLayersVolumeAnnotationsGet(volumeId, layerId, annotationId, opts)



Gets the volume annotation.

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

let apiInstance = new BooksApi.LayersApi();
let volumeId = "volumeId_example"; // String | The volume to retrieve annotations for.
let layerId = "layerId_example"; // String | The ID for the layer to get the annotations.
let annotationId = "annotationId_example"; // String | The ID of the volume annotation to retrieve.
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
  'locale': "locale_example", // String | The locale information for the data. ISO-639-1 language and ISO-3166-1 country code. Ex: 'en_US'.
  'source': "source_example" // String | String to identify the originator of this request.
};
apiInstance.booksLayersVolumeAnnotationsGet(volumeId, layerId, annotationId, opts, (error, data, response) => {
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
 **volumeId** | **String**| The volume to retrieve annotations for. | 
 **layerId** | **String**| The ID for the layer to get the annotations. | 
 **annotationId** | **String**| The ID of the volume annotation to retrieve. | 
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
 **locale** | **String**| The locale information for the data. ISO-639-1 language and ISO-3166-1 country code. Ex: &#39;en_US&#39;. | [optional] 
 **source** | **String**| String to identify the originator of this request. | [optional] 

### Return type

[**Volumeannotation**](Volumeannotation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## booksLayersVolumeAnnotationsList

> Volumeannotations booksLayersVolumeAnnotationsList(volumeId, layerId, contentVersion, opts)



Gets the volume annotations for a volume and layer.

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

let apiInstance = new BooksApi.LayersApi();
let volumeId = "volumeId_example"; // String | The volume to retrieve annotations for.
let layerId = "layerId_example"; // String | The ID for the layer to get the annotations.
let contentVersion = "contentVersion_example"; // String | The content version for the requested volume.
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
  'endOffset': "endOffset_example", // String | The end offset to end retrieving data from.
  'endPosition': "endPosition_example", // String | The end position to end retrieving data from.
  'locale': "locale_example", // String | The locale information for the data. ISO-639-1 language and ISO-3166-1 country code. Ex: 'en_US'.
  'maxResults': 56, // Number | Maximum number of results to return
  'pageToken': "pageToken_example", // String | The value of the nextToken from the previous page.
  'showDeleted': true, // Boolean | Set to true to return deleted annotations. updatedMin must be in the request to use this. Defaults to false.
  'source': "source_example", // String | String to identify the originator of this request.
  'startOffset': "startOffset_example", // String | The start offset to start retrieving data from.
  'startPosition': "startPosition_example", // String | The start position to start retrieving data from.
  'updatedMax': "updatedMax_example", // String | RFC 3339 timestamp to restrict to items updated prior to this timestamp (exclusive).
  'updatedMin': "updatedMin_example", // String | RFC 3339 timestamp to restrict to items updated since this timestamp (inclusive).
  'volumeAnnotationsVersion': "volumeAnnotationsVersion_example" // String | The version of the volume annotations that you are requesting.
};
apiInstance.booksLayersVolumeAnnotationsList(volumeId, layerId, contentVersion, opts, (error, data, response) => {
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
 **volumeId** | **String**| The volume to retrieve annotations for. | 
 **layerId** | **String**| The ID for the layer to get the annotations. | 
 **contentVersion** | **String**| The content version for the requested volume. | 
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
 **endOffset** | **String**| The end offset to end retrieving data from. | [optional] 
 **endPosition** | **String**| The end position to end retrieving data from. | [optional] 
 **locale** | **String**| The locale information for the data. ISO-639-1 language and ISO-3166-1 country code. Ex: &#39;en_US&#39;. | [optional] 
 **maxResults** | **Number**| Maximum number of results to return | [optional] 
 **pageToken** | **String**| The value of the nextToken from the previous page. | [optional] 
 **showDeleted** | **Boolean**| Set to true to return deleted annotations. updatedMin must be in the request to use this. Defaults to false. | [optional] 
 **source** | **String**| String to identify the originator of this request. | [optional] 
 **startOffset** | **String**| The start offset to start retrieving data from. | [optional] 
 **startPosition** | **String**| The start position to start retrieving data from. | [optional] 
 **updatedMax** | **String**| RFC 3339 timestamp to restrict to items updated prior to this timestamp (exclusive). | [optional] 
 **updatedMin** | **String**| RFC 3339 timestamp to restrict to items updated since this timestamp (inclusive). | [optional] 
 **volumeAnnotationsVersion** | **String**| The version of the volume annotations that you are requesting. | [optional] 

### Return type

[**Volumeannotations**](Volumeannotations.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

