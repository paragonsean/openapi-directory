# GettyImages.ArtistsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3ArtistsImagesGet**](ArtistsApi.md#v3ArtistsImagesGet) | **GET** /v3/artists/images | Search for images by a photographer
[**v3ArtistsVideosGet**](ArtistsApi.md#v3ArtistsVideosGet) | **GET** /v3/artists/videos | Search for videos by a photographer



## v3ArtistsImagesGet

> v3ArtistsImagesGet(opts)

Search for images by a photographer

### Example

```javascript
import GettyImages from 'getty_images';
let defaultClient = GettyImages.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: Api-Key
let Api-Key = defaultClient.authentications['Api-Key'];
Api-Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Api-Key.apiKeyPrefix = 'Token';

let apiInstance = new GettyImages.ArtistsApi();
let opts = {
  'acceptLanguage': "acceptLanguage_example", // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
  'artistName': "artistName_example", // String | Name of artist for desired images
  'fields': [new GettyImages.ArtistsImageSearchFieldValues()], // [ArtistsImageSearchFieldValues] | Comma separated list of fields. Allows restricting which fields are returned. If no fields are selected, the summary_set of fields are returned.
  'page': 1, // Number | Identifies page to return. Default page is 1.
  'pageSize': 10 // Number | Specifies page size. Default page_size is 10, maximum page_size is 100.
};
apiInstance.v3ArtistsImagesGet(opts, (error, data, response) => {
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
 **acceptLanguage** | **String**| Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only). | [optional] 
 **artistName** | **String**| Name of artist for desired images | [optional] 
 **fields** | [**[ArtistsImageSearchFieldValues]**](ArtistsImageSearchFieldValues.md)| Comma separated list of fields. Allows restricting which fields are returned. If no fields are selected, the summary_set of fields are returned. | [optional] 
 **page** | **Number**| Identifies page to return. Default page is 1. | [optional] [default to 1]
 **pageSize** | **Number**| Specifies page size. Default page_size is 10, maximum page_size is 100. | [optional] [default to 10]

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## v3ArtistsVideosGet

> v3ArtistsVideosGet(opts)

Search for videos by a photographer

### Example

```javascript
import GettyImages from 'getty_images';
let defaultClient = GettyImages.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: Api-Key
let Api-Key = defaultClient.authentications['Api-Key'];
Api-Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Api-Key.apiKeyPrefix = 'Token';

let apiInstance = new GettyImages.ArtistsApi();
let opts = {
  'acceptLanguage': "acceptLanguage_example", // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
  'artistName': "artistName_example", // String | Name of artist for desired images
  'fields': [new GettyImages.ArtistsVideoSearchFieldValues()], // [ArtistsVideoSearchFieldValues] | Comma separated list of fields. Allows restricting which fields are returned. If no fields are selected, the summary_set of fields are returned.
  'page': 1, // Number | Identifies page to return. Default page is 1.
  'pageSize': 10 // Number | Specifies page size. Default page_size is 10, maximum page_size is 100.
};
apiInstance.v3ArtistsVideosGet(opts, (error, data, response) => {
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
 **acceptLanguage** | **String**| Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only). | [optional] 
 **artistName** | **String**| Name of artist for desired images | [optional] 
 **fields** | [**[ArtistsVideoSearchFieldValues]**](ArtistsVideoSearchFieldValues.md)| Comma separated list of fields. Allows restricting which fields are returned. If no fields are selected, the summary_set of fields are returned. | [optional] 
 **page** | **Number**| Identifies page to return. Default page is 1. | [optional] [default to 1]
 **pageSize** | **Number**| Specifies page size. Default page_size is 10, maximum page_size is 100. | [optional] [default to 10]

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

