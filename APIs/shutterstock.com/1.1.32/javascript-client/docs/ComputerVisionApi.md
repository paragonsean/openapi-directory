# ShutterstockApiExplorer.ComputerVisionApi

All URIs are relative to *https://api.shutterstock.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getKeywords**](ComputerVisionApi.md#getKeywords) | **GET** /v2/cv/keywords | List suggested keywords
[**getSimilarImages**](ComputerVisionApi.md#getSimilarImages) | **GET** /v2/cv/similar/images | List similar images
[**getSimilarVideos**](ComputerVisionApi.md#getSimilarVideos) | **GET** /v2/cv/similar/videos | List similar videos
[**uploadEphemeralImage**](ComputerVisionApi.md#uploadEphemeralImage) | **POST** /v2/images | Upload ephemeral images
[**uploadImage**](ComputerVisionApi.md#uploadImage) | **POST** /v2/cv/images | Upload images



## getKeywords

> KeywordDataList getKeywords(assetId)

List suggested keywords

This endpoint returns a list of suggested keywords for a media item that you specify or upload.

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

let apiInstance = new ShutterstockApiExplorer.ComputerVisionApi();
let assetId = new ShutterstockApiExplorer.GetKeywordsAssetIdParameter(); // GetKeywordsAssetIdParameter | The asset ID or upload ID to suggest keywords for
apiInstance.getKeywords(assetId, (error, data, response) => {
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
 **assetId** | [**GetKeywordsAssetIdParameter**](.md)| The asset ID or upload ID to suggest keywords for | 

### Return type

[**KeywordDataList**](KeywordDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSimilarImages

> ImageSearchResults getSimilarImages(assetId, opts)

List similar images

This endpoint returns images that are visually similar to an image that you specify or upload.

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

let apiInstance = new ShutterstockApiExplorer.ComputerVisionApi();
let assetId = "U6ba16262e3bc2db470b8e3cfa8aaab25"; // String | The asset ID or upload ID to find similar images for
let opts = {
  'license': ["null"], // [String] | Show only images with the specified license
  'safe': true, // Boolean | Enable or disable safe search
  'language': new ShutterstockApiExplorer.Language(), // Language | Language for the keywords and categories in the response
  'page': 1, // Number | Page number
  'perPage': 20, // Number | Number of results per page
  'view': "'minimal'" // String | Amount of detail to render in the response
};
apiInstance.getSimilarImages(assetId, opts, (error, data, response) => {
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
 **assetId** | **String**| The asset ID or upload ID to find similar images for | 
 **license** | [**[String]**](String.md)| Show only images with the specified license | [optional] 
 **safe** | **Boolean**| Enable or disable safe search | [optional] [default to true]
 **language** | [**Language**](.md)| Language for the keywords and categories in the response | [optional] 
 **page** | **Number**| Page number | [optional] [default to 1]
 **perPage** | **Number**| Number of results per page | [optional] [default to 20]
 **view** | **String**| Amount of detail to render in the response | [optional] [default to &#39;minimal&#39;]

### Return type

[**ImageSearchResults**](ImageSearchResults.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSimilarVideos

> VideoSearchResults getSimilarVideos(assetId, opts)

List similar videos

This endpoint returns videos that are visually similar to an image that you specify or upload.

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

let apiInstance = new ShutterstockApiExplorer.ComputerVisionApi();
let assetId = "U6ba16262e3bc2db470b8e3cfa8aaab25"; // String | The asset ID or upload ID to find similar videos for
let opts = {
  'license': ["null"], // [String] | Show only videos with the specified license
  'safe': true, // Boolean | Enable or disable safe search
  'language': new ShutterstockApiExplorer.Language(), // Language | Language for the keywords and categories in the response
  'page': 1, // Number | Page number
  'perPage': 20, // Number | Number of results per page
  'view': "'minimal'" // String | Amount of detail to render in the response
};
apiInstance.getSimilarVideos(assetId, opts, (error, data, response) => {
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
 **assetId** | **String**| The asset ID or upload ID to find similar videos for | 
 **license** | [**[String]**](String.md)| Show only videos with the specified license | [optional] 
 **safe** | **Boolean**| Enable or disable safe search | [optional] [default to true]
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


## uploadEphemeralImage

> ImageCreateResponse uploadEphemeralImage(imageCreateRequest)

Upload ephemeral images

Deprecated; use &#x60;POST /v2/cv/images&#x60; instead. This endpoint uploads an image for reverse image search. The image must be in JPEG or PNG format. To get the search results, pass the ID that this endpoint returns to the &#x60;GET /v2/images/{id}/similar&#x60; endpoint.

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

let apiInstance = new ShutterstockApiExplorer.ComputerVisionApi();
let imageCreateRequest = {"$ref":"#/components/schemas/ImageCreateRequest/example"}; // ImageCreateRequest | The image data in JPEG or PNG format
apiInstance.uploadEphemeralImage(imageCreateRequest, (error, data, response) => {
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
 **imageCreateRequest** | [**ImageCreateRequest**](ImageCreateRequest.md)| The image data in JPEG or PNG format | 

### Return type

[**ImageCreateResponse**](ImageCreateResponse.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## uploadImage

> ComputerVisionImageCreateResponse uploadImage(imageCreateRequest)

Upload images

This endpoint uploads an image for reverse image or video search. Images must be in JPEG or PNG format. To get the search results, pass the upload ID that this endpoint returns to the GET /v2/cv/similar/images or GET /v2/cv/similar/videos endpoints. Contact us for access to this endpoint.

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

let apiInstance = new ShutterstockApiExplorer.ComputerVisionApi();
let imageCreateRequest = {"$ref":"#/components/schemas/ImageCreateRequest/example"}; // ImageCreateRequest | A Base 64 encoded jpeg or png; images can be no larger than 10mb and can be no larger than 10,000 pixels in width or height
apiInstance.uploadImage(imageCreateRequest, (error, data, response) => {
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
 **imageCreateRequest** | [**ImageCreateRequest**](ImageCreateRequest.md)| A Base 64 encoded jpeg or png; images can be no larger than 10mb and can be no larger than 10,000 pixels in width or height | 

### Return type

[**ComputerVisionImageCreateResponse**](ComputerVisionImageCreateResponse.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

