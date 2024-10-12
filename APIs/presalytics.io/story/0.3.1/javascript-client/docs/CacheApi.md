# Story.CacheApi

All URIs are relative to */story*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cacheNonceGet**](CacheApi.md#cacheNonceGet) | **GET** /cache/{nonce} | Cache: Get Subdocument
[**cachePost**](CacheApi.md#cachePost) | **POST** /cache | Cache: Store Subdocument



## cacheNonceGet

> String cacheNonceGet(nonce)

Cache: Get Subdocument

An endpoint for broswer retreive html documents that were cached durin the rendering process via a nonce (token)

### Example

```javascript
import Story from 'story';

let apiInstance = new Story.CacheApi();
let nonce = "nonce_example"; // String | A one-time use token for retieving items in the users cache
apiInstance.cacheNonceGet(nonce, (error, data, response) => {
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
 **nonce** | **String**| A one-time use token for retieving items in the users cache | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/html, application/json


## cachePost

> cachePost(cachePostRequest)

Cache: Store Subdocument

An endpoint for Presalytics Renderers to cache html subdocuments for subsequent retrieval by the browser.  Documents Are retrieved via token expire after 1 minute.

### Example

```javascript
import Story from 'story';

let apiInstance = new Story.CacheApi();
let cachePostRequest = new Story.CachePostRequest(); // CachePostRequest | parameters to identify an update a collaborator across multiple stories
apiInstance.cachePost(cachePostRequest, (error, data, response) => {
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
 **cachePostRequest** | [**CachePostRequest**](CachePostRequest.md)| parameters to identify an update a collaborator across multiple stories | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

