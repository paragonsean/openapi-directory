# ContentGrooveApi.DefaultApi

All URIs are relative to *https://api.contentgroove.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createClip**](DefaultApi.md#createClip) | **POST** /clips | create clip
[**createMedia**](DefaultApi.md#createMedia) | **POST** /medias | create media
[**createWebhookSubscription**](DefaultApi.md#createWebhookSubscription) | **POST** /webhook_subscriptions | create webhook subscription
[**deleteClipById**](DefaultApi.md#deleteClipById) | **DELETE** /clips/{id} | delete clip
[**deleteMediaById**](DefaultApi.md#deleteMediaById) | **DELETE** /medias/{id} | delete media
[**deleteWebhookSubscriptionById**](DefaultApi.md#deleteWebhookSubscriptionById) | **DELETE** /webhook_subscriptions/{id} | delete webhook subscription
[**getClipById**](DefaultApi.md#getClipById) | **GET** /clips/{id} | show clip
[**getClips**](DefaultApi.md#getClips) | **GET** /clips | list clips
[**getMediaById**](DefaultApi.md#getMediaById) | **GET** /medias/{id} | show media
[**getMedias**](DefaultApi.md#getMedias) | **GET** /medias | list medias
[**getUploadUrl**](DefaultApi.md#getUploadUrl) | **GET** /direct_uploads | prepare presigned upload url
[**getWebhookSubscriptionById**](DefaultApi.md#getWebhookSubscriptionById) | **GET** /webhook_subscriptions/{id} | show webhook subscription
[**getWebhookSubscriptions**](DefaultApi.md#getWebhookSubscriptions) | **GET** /webhook_subscriptions | list webhook subscriptions
[**updateClipById**](DefaultApi.md#updateClipById) | **PUT** /clips/{id} | update clip
[**updateMediaById**](DefaultApi.md#updateMediaById) | **PUT** /medias/{id} | update media



## createClip

> ClipResponseObject createClip(createClipRequest)

create clip

### Example

```javascript
import ContentGrooveApi from 'content_groove_api';
let defaultClient = ContentGrooveApi.ApiClient.instance;
// Configure API key authorization: BearerHeader
let BearerHeader = defaultClient.authentications['BearerHeader'];
BearerHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//BearerHeader.apiKeyPrefix = 'Token';

let apiInstance = new ContentGrooveApi.DefaultApi();
let createClipRequest = new ContentGrooveApi.CreateClipRequest(); // CreateClipRequest | 
apiInstance.createClip(createClipRequest, (error, data, response) => {
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
 **createClipRequest** | [**CreateClipRequest**](CreateClipRequest.md)|  | 

### Return type

[**ClipResponseObject**](ClipResponseObject.md)

### Authorization

[BearerHeader](../README.md#BearerHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createMedia

> MediaResponseObject createMedia(createMediaRequest)

create media

### Example

```javascript
import ContentGrooveApi from 'content_groove_api';
let defaultClient = ContentGrooveApi.ApiClient.instance;
// Configure API key authorization: BearerHeader
let BearerHeader = defaultClient.authentications['BearerHeader'];
BearerHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//BearerHeader.apiKeyPrefix = 'Token';

let apiInstance = new ContentGrooveApi.DefaultApi();
let createMediaRequest = new ContentGrooveApi.CreateMediaRequest(); // CreateMediaRequest | 
apiInstance.createMedia(createMediaRequest, (error, data, response) => {
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
 **createMediaRequest** | [**CreateMediaRequest**](CreateMediaRequest.md)|  | 

### Return type

[**MediaResponseObject**](MediaResponseObject.md)

### Authorization

[BearerHeader](../README.md#BearerHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createWebhookSubscription

> WebhookSubscriptionResponseObject createWebhookSubscription(createWebhookSubscriptionRequest)

create webhook subscription

### Example

```javascript
import ContentGrooveApi from 'content_groove_api';
let defaultClient = ContentGrooveApi.ApiClient.instance;
// Configure API key authorization: BearerHeader
let BearerHeader = defaultClient.authentications['BearerHeader'];
BearerHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//BearerHeader.apiKeyPrefix = 'Token';

let apiInstance = new ContentGrooveApi.DefaultApi();
let createWebhookSubscriptionRequest = new ContentGrooveApi.CreateWebhookSubscriptionRequest(); // CreateWebhookSubscriptionRequest | 
apiInstance.createWebhookSubscription(createWebhookSubscriptionRequest, (error, data, response) => {
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
 **createWebhookSubscriptionRequest** | [**CreateWebhookSubscriptionRequest**](CreateWebhookSubscriptionRequest.md)|  | 

### Return type

[**WebhookSubscriptionResponseObject**](WebhookSubscriptionResponseObject.md)

### Authorization

[BearerHeader](../README.md#BearerHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteClipById

> deleteClipById(id)

delete clip

### Example

```javascript
import ContentGrooveApi from 'content_groove_api';
let defaultClient = ContentGrooveApi.ApiClient.instance;
// Configure API key authorization: BearerHeader
let BearerHeader = defaultClient.authentications['BearerHeader'];
BearerHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//BearerHeader.apiKeyPrefix = 'Token';

let apiInstance = new ContentGrooveApi.DefaultApi();
let id = "id_example"; // String | The id of the clip to be retrieved
apiInstance.deleteClipById(id, (error, data, response) => {
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
 **id** | **String**| The id of the clip to be retrieved | 

### Return type

null (empty response body)

### Authorization

[BearerHeader](../README.md#BearerHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteMediaById

> deleteMediaById(id)

delete media

### Example

```javascript
import ContentGrooveApi from 'content_groove_api';
let defaultClient = ContentGrooveApi.ApiClient.instance;
// Configure API key authorization: BearerHeader
let BearerHeader = defaultClient.authentications['BearerHeader'];
BearerHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//BearerHeader.apiKeyPrefix = 'Token';

let apiInstance = new ContentGrooveApi.DefaultApi();
let id = "id_example"; // String | id
apiInstance.deleteMediaById(id, (error, data, response) => {
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
 **id** | **String**| id | 

### Return type

null (empty response body)

### Authorization

[BearerHeader](../README.md#BearerHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteWebhookSubscriptionById

> deleteWebhookSubscriptionById(id)

delete webhook subscription

### Example

```javascript
import ContentGrooveApi from 'content_groove_api';
let defaultClient = ContentGrooveApi.ApiClient.instance;
// Configure API key authorization: BearerHeader
let BearerHeader = defaultClient.authentications['BearerHeader'];
BearerHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//BearerHeader.apiKeyPrefix = 'Token';

let apiInstance = new ContentGrooveApi.DefaultApi();
let id = "id_example"; // String | The id of the webhook subscription to be retrieved
apiInstance.deleteWebhookSubscriptionById(id, (error, data, response) => {
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
 **id** | **String**| The id of the webhook subscription to be retrieved | 

### Return type

null (empty response body)

### Authorization

[BearerHeader](../README.md#BearerHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getClipById

> ClipResponseObject getClipById(id)

show clip

### Example

```javascript
import ContentGrooveApi from 'content_groove_api';
let defaultClient = ContentGrooveApi.ApiClient.instance;
// Configure API key authorization: BearerHeader
let BearerHeader = defaultClient.authentications['BearerHeader'];
BearerHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//BearerHeader.apiKeyPrefix = 'Token';

let apiInstance = new ContentGrooveApi.DefaultApi();
let id = "id_example"; // String | The id of the clip to be retrieved
apiInstance.getClipById(id, (error, data, response) => {
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
 **id** | **String**| The id of the clip to be retrieved | 

### Return type

[**ClipResponseObject**](ClipResponseObject.md)

### Authorization

[BearerHeader](../README.md#BearerHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getClips

> ClipsResponseObject getClips(opts)

list clips

### Example

```javascript
import ContentGrooveApi from 'content_groove_api';
let defaultClient = ContentGrooveApi.ApiClient.instance;
// Configure API key authorization: BearerHeader
let BearerHeader = defaultClient.authentications['BearerHeader'];
BearerHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//BearerHeader.apiKeyPrefix = 'Token';

let apiInstance = new ContentGrooveApi.DefaultApi();
let opts = {
  'filter': {key: null}, // Object | Filters to be applied to the query.  Query params in the url must look like this: \"filter[attributeName_*matcher*]\"  (i.e. filter[name_eq]=chimp%20into%20space)  Available matchers can be found here: https://activerecord-hackery.github.io/ransack/getting-started/search-matches/  
  'page': {key: null}, // Object | Specify page number and page size for the query
  'sort': "sort_example" // String | Sorting to be applied to the query. For more info: https://jsonapi.org/format/#fetching-sorting
};
apiInstance.getClips(opts, (error, data, response) => {
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
 **filter** | [**Object**](.md)| Filters to be applied to the query.  Query params in the url must look like this: \&quot;filter[attributeName_*matcher*]\&quot;  (i.e. filter[name_eq]&#x3D;chimp%20into%20space)  Available matchers can be found here: https://activerecord-hackery.github.io/ransack/getting-started/search-matches/   | [optional] 
 **page** | [**Object**](.md)| Specify page number and page size for the query | [optional] 
 **sort** | **String**| Sorting to be applied to the query. For more info: https://jsonapi.org/format/#fetching-sorting | [optional] 

### Return type

[**ClipsResponseObject**](ClipsResponseObject.md)

### Authorization

[BearerHeader](../README.md#BearerHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMediaById

> MediaResponseObject getMediaById(id)

show media

### Example

```javascript
import ContentGrooveApi from 'content_groove_api';
let defaultClient = ContentGrooveApi.ApiClient.instance;
// Configure API key authorization: BearerHeader
let BearerHeader = defaultClient.authentications['BearerHeader'];
BearerHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//BearerHeader.apiKeyPrefix = 'Token';

let apiInstance = new ContentGrooveApi.DefaultApi();
let id = "id_example"; // String | id
apiInstance.getMediaById(id, (error, data, response) => {
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
 **id** | **String**| id | 

### Return type

[**MediaResponseObject**](MediaResponseObject.md)

### Authorization

[BearerHeader](../README.md#BearerHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMedias

> MediasResponseObject getMedias(opts)

list medias

### Example

```javascript
import ContentGrooveApi from 'content_groove_api';
let defaultClient = ContentGrooveApi.ApiClient.instance;
// Configure API key authorization: BearerHeader
let BearerHeader = defaultClient.authentications['BearerHeader'];
BearerHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//BearerHeader.apiKeyPrefix = 'Token';

let apiInstance = new ContentGrooveApi.DefaultApi();
let opts = {
  'filter': {key: null}, // Object | Filters to be applied to the query.  Query params in the url must look like this: \"filter[attributeName_*matcher*]\"  (i.e. filter[name_eq]=chimp%20into%20space)  Available matchers can be found here: https://activerecord-hackery.github.io/ransack/getting-started/search-matches/  
  'page': {key: null}, // Object | Specify page number and page size for the query
  'sort': "sort_example" // String | Sorting to be applied to the query. For more info: https://jsonapi.org/format/#fetching-sorting
};
apiInstance.getMedias(opts, (error, data, response) => {
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
 **filter** | [**Object**](.md)| Filters to be applied to the query.  Query params in the url must look like this: \&quot;filter[attributeName_*matcher*]\&quot;  (i.e. filter[name_eq]&#x3D;chimp%20into%20space)  Available matchers can be found here: https://activerecord-hackery.github.io/ransack/getting-started/search-matches/   | [optional] 
 **page** | [**Object**](.md)| Specify page number and page size for the query | [optional] 
 **sort** | **String**| Sorting to be applied to the query. For more info: https://jsonapi.org/format/#fetching-sorting | [optional] 

### Return type

[**MediasResponseObject**](MediasResponseObject.md)

### Authorization

[BearerHeader](../README.md#BearerHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUploadUrl

> DirectUploadResponseObject getUploadUrl()

prepare presigned upload url

### Example

```javascript
import ContentGrooveApi from 'content_groove_api';
let defaultClient = ContentGrooveApi.ApiClient.instance;
// Configure API key authorization: BearerHeader
let BearerHeader = defaultClient.authentications['BearerHeader'];
BearerHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//BearerHeader.apiKeyPrefix = 'Token';

let apiInstance = new ContentGrooveApi.DefaultApi();
apiInstance.getUploadUrl((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**DirectUploadResponseObject**](DirectUploadResponseObject.md)

### Authorization

[BearerHeader](../README.md#BearerHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getWebhookSubscriptionById

> WebhookSubscriptionResponseObject getWebhookSubscriptionById(id)

show webhook subscription

### Example

```javascript
import ContentGrooveApi from 'content_groove_api';
let defaultClient = ContentGrooveApi.ApiClient.instance;
// Configure API key authorization: BearerHeader
let BearerHeader = defaultClient.authentications['BearerHeader'];
BearerHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//BearerHeader.apiKeyPrefix = 'Token';

let apiInstance = new ContentGrooveApi.DefaultApi();
let id = "id_example"; // String | The id of the webhook subscription to be retrieved
apiInstance.getWebhookSubscriptionById(id, (error, data, response) => {
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
 **id** | **String**| The id of the webhook subscription to be retrieved | 

### Return type

[**WebhookSubscriptionResponseObject**](WebhookSubscriptionResponseObject.md)

### Authorization

[BearerHeader](../README.md#BearerHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getWebhookSubscriptions

> WebhookSubscriptionsResponseObject getWebhookSubscriptions(opts)

list webhook subscriptions

### Example

```javascript
import ContentGrooveApi from 'content_groove_api';
let defaultClient = ContentGrooveApi.ApiClient.instance;
// Configure API key authorization: BearerHeader
let BearerHeader = defaultClient.authentications['BearerHeader'];
BearerHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//BearerHeader.apiKeyPrefix = 'Token';

let apiInstance = new ContentGrooveApi.DefaultApi();
let opts = {
  'filter': {key: null}, // Object | Filters to be applied to the query.  Query params in the url must look like this: \"filter[attributeName_*matcher*]\"  (i.e. filter[name_eq]=chimp%20into%20space)  Available matchers can be found here: https://activerecord-hackery.github.io/ransack/getting-started/search-matches/  
  'sort': "sort_example" // String | Sorting to be applied to the query. For more info: https://jsonapi.org/format/#fetching-sorting
};
apiInstance.getWebhookSubscriptions(opts, (error, data, response) => {
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
 **filter** | [**Object**](.md)| Filters to be applied to the query.  Query params in the url must look like this: \&quot;filter[attributeName_*matcher*]\&quot;  (i.e. filter[name_eq]&#x3D;chimp%20into%20space)  Available matchers can be found here: https://activerecord-hackery.github.io/ransack/getting-started/search-matches/   | [optional] 
 **sort** | **String**| Sorting to be applied to the query. For more info: https://jsonapi.org/format/#fetching-sorting | [optional] 

### Return type

[**WebhookSubscriptionsResponseObject**](WebhookSubscriptionsResponseObject.md)

### Authorization

[BearerHeader](../README.md#BearerHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateClipById

> ClipResponseObject updateClipById(id, updateClipByIdRequest)

update clip

### Example

```javascript
import ContentGrooveApi from 'content_groove_api';
let defaultClient = ContentGrooveApi.ApiClient.instance;
// Configure API key authorization: BearerHeader
let BearerHeader = defaultClient.authentications['BearerHeader'];
BearerHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//BearerHeader.apiKeyPrefix = 'Token';

let apiInstance = new ContentGrooveApi.DefaultApi();
let id = "id_example"; // String | The id of the clip to be retrieved
let updateClipByIdRequest = new ContentGrooveApi.UpdateClipByIdRequest(); // UpdateClipByIdRequest | 
apiInstance.updateClipById(id, updateClipByIdRequest, (error, data, response) => {
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
 **id** | **String**| The id of the clip to be retrieved | 
 **updateClipByIdRequest** | [**UpdateClipByIdRequest**](UpdateClipByIdRequest.md)|  | 

### Return type

[**ClipResponseObject**](ClipResponseObject.md)

### Authorization

[BearerHeader](../README.md#BearerHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateMediaById

> MediaResponseObject updateMediaById(id, updateMediaByIdRequest)

update media

### Example

```javascript
import ContentGrooveApi from 'content_groove_api';
let defaultClient = ContentGrooveApi.ApiClient.instance;
// Configure API key authorization: BearerHeader
let BearerHeader = defaultClient.authentications['BearerHeader'];
BearerHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//BearerHeader.apiKeyPrefix = 'Token';

let apiInstance = new ContentGrooveApi.DefaultApi();
let id = "id_example"; // String | id
let updateMediaByIdRequest = new ContentGrooveApi.UpdateMediaByIdRequest(); // UpdateMediaByIdRequest | 
apiInstance.updateMediaById(id, updateMediaByIdRequest, (error, data, response) => {
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
 **id** | **String**| id | 
 **updateMediaByIdRequest** | [**UpdateMediaByIdRequest**](UpdateMediaByIdRequest.md)|  | 

### Return type

[**MediaResponseObject**](MediaResponseObject.md)

### Authorization

[BearerHeader](../README.md#BearerHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

