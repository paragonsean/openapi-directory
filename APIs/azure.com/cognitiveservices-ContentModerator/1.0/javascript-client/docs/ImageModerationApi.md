# ContentModeratorClient.ImageModerationApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**imageModerationEvaluate**](ImageModerationApi.md#imageModerationEvaluate) | **POST** /contentmoderator/moderate/v1.0/ProcessImage/Evaluate | 
[**imageModerationFindFaces**](ImageModerationApi.md#imageModerationFindFaces) | **POST** /contentmoderator/moderate/v1.0/ProcessImage/FindFaces | 
[**imageModerationMatch**](ImageModerationApi.md#imageModerationMatch) | **POST** /contentmoderator/moderate/v1.0/ProcessImage/Match | 
[**imageModerationOCR**](ImageModerationApi.md#imageModerationOCR) | **POST** /contentmoderator/moderate/v1.0/ProcessImage/OCR | 



## imageModerationEvaluate

> Evaluate imageModerationEvaluate(opts)



Returns probabilities of the image containing racy or adult content.

### Example

```javascript
import ContentModeratorClient from 'content_moderator_client';
let defaultClient = ContentModeratorClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ContentModeratorClient.ImageModerationApi();
let opts = {
  'cacheImage': true // Boolean | Whether to retain the submitted image for future use; defaults to false if omitted.
};
apiInstance.imageModerationEvaluate(opts, (error, data, response) => {
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
 **cacheImage** | **Boolean**| Whether to retain the submitted image for future use; defaults to false if omitted. | [optional] 

### Return type

[**Evaluate**](Evaluate.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## imageModerationFindFaces

> FoundFaces imageModerationFindFaces(opts)



Returns the list of faces found.

### Example

```javascript
import ContentModeratorClient from 'content_moderator_client';
let defaultClient = ContentModeratorClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ContentModeratorClient.ImageModerationApi();
let opts = {
  'cacheImage': true // Boolean | Whether to retain the submitted image for future use; defaults to false if omitted.
};
apiInstance.imageModerationFindFaces(opts, (error, data, response) => {
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
 **cacheImage** | **Boolean**| Whether to retain the submitted image for future use; defaults to false if omitted. | [optional] 

### Return type

[**FoundFaces**](FoundFaces.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## imageModerationMatch

> MatchResponse imageModerationMatch(opts)



Fuzzily match an image against one of your custom Image Lists. You can create and manage your custom image lists using &lt;a href&#x3D;\&quot;/docs/services/578ff44d2703741568569ab9/operations/578ff7b12703741568569abe\&quot;&gt;this&lt;/a&gt; API.     Returns ID and tags of matching image.&lt;br/&gt;  &lt;br/&gt;  Note: Refresh Index must be run on the corresponding Image List before additions and removals are reflected in the response.

### Example

```javascript
import ContentModeratorClient from 'content_moderator_client';
let defaultClient = ContentModeratorClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ContentModeratorClient.ImageModerationApi();
let opts = {
  'listId': "listId_example", // String | The list Id.
  'cacheImage': true // Boolean | Whether to retain the submitted image for future use; defaults to false if omitted.
};
apiInstance.imageModerationMatch(opts, (error, data, response) => {
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
 **listId** | **String**| The list Id. | [optional] 
 **cacheImage** | **Boolean**| Whether to retain the submitted image for future use; defaults to false if omitted. | [optional] 

### Return type

[**MatchResponse**](MatchResponse.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## imageModerationOCR

> OCR imageModerationOCR(language, opts)



Returns any text found in the image for the language specified. If no language is specified in input then the detection defaults to English.

### Example

```javascript
import ContentModeratorClient from 'content_moderator_client';
let defaultClient = ContentModeratorClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ContentModeratorClient.ImageModerationApi();
let language = "language_example"; // String | Language of the terms.
let opts = {
  'cacheImage': true, // Boolean | Whether to retain the submitted image for future use; defaults to false if omitted.
  'enhanced': false // Boolean | When set to True, the image goes through additional processing to come with additional candidates.  image/tiff is not supported when enhanced is set to true  Note: This impacts the response time.
};
apiInstance.imageModerationOCR(language, opts, (error, data, response) => {
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
 **language** | **String**| Language of the terms. | 
 **cacheImage** | **Boolean**| Whether to retain the submitted image for future use; defaults to false if omitted. | [optional] 
 **enhanced** | **Boolean**| When set to True, the image goes through additional processing to come with additional candidates.  image/tiff is not supported when enhanced is set to true  Note: This impacts the response time. | [optional] [default to false]

### Return type

[**OCR**](OCR.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

