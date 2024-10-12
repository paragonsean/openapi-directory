# HashlookupCirclApi.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getChildren**](DefaultApi.md#getChildren) | **GET** /children/{sha1}/{count}/{cursor} | 
[**getInfo**](DefaultApi.md#getInfo) | **GET** /info | 
[**getLookupMd5**](DefaultApi.md#getLookupMd5) | **GET** /lookup/md5/{md5} | 
[**getLookupSha1**](DefaultApi.md#getLookupSha1) | **GET** /lookup/sha1/{sha1} | 
[**getLookupSha256**](DefaultApi.md#getLookupSha256) | **GET** /lookup/sha256/{sha256} | 
[**getParents**](DefaultApi.md#getParents) | **GET** /parents/{sha1}/{count}/{cursor} | 
[**getSessionCreate**](DefaultApi.md#getSessionCreate) | **GET** /session/create/{name} | 
[**getSessionMatches**](DefaultApi.md#getSessionMatches) | **GET** /session/get/{name} | 
[**getStattop**](DefaultApi.md#getStattop) | **GET** /stats/top | 
[**postBulkmd5**](DefaultApi.md#postBulkmd5) | **POST** /bulk/md5 | 
[**postBulksha1**](DefaultApi.md#postBulksha1) | **POST** /bulk/sha1 | 



## getChildren

> getChildren(sha1, count, cursor)



Return children from a given SHA1.  A number of element to return and an offset must be given. If not set it will be the 100 first elements. A cursor must be given to paginate over. The starting cursor is 0.

### Example

```javascript
import HashlookupCirclApi from 'hashlookup_circl_api';

let apiInstance = new HashlookupCirclApi.DefaultApi();
let sha1 = "sha1_example"; // String | 
let count = 56; // Number | 
let cursor = "cursor_example"; // String | 
apiInstance.getChildren(sha1, count, cursor, (error, data, response) => {
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
 **sha1** | **String**|  | 
 **count** | **Number**|  | 
 **cursor** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getInfo

> getInfo()



Info about the hashlookup database

### Example

```javascript
import HashlookupCirclApi from 'hashlookup_circl_api';

let apiInstance = new HashlookupCirclApi.DefaultApi();
apiInstance.getInfo((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getLookupMd5

> getLookupMd5(md5)



Lookup MD5.

### Example

```javascript
import HashlookupCirclApi from 'hashlookup_circl_api';

let apiInstance = new HashlookupCirclApi.DefaultApi();
let md5 = "md5_example"; // String | 
apiInstance.getLookupMd5(md5, (error, data, response) => {
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
 **md5** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getLookupSha1

> getLookupSha1(sha1)



Lookup SHA-1.

### Example

```javascript
import HashlookupCirclApi from 'hashlookup_circl_api';

let apiInstance = new HashlookupCirclApi.DefaultApi();
let sha1 = "sha1_example"; // String | 
apiInstance.getLookupSha1(sha1, (error, data, response) => {
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
 **sha1** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getLookupSha256

> getLookupSha256(sha256)



Lookup SHA-256.

### Example

```javascript
import HashlookupCirclApi from 'hashlookup_circl_api';

let apiInstance = new HashlookupCirclApi.DefaultApi();
let sha256 = "sha256_example"; // String | 
apiInstance.getLookupSha256(sha256, (error, data, response) => {
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
 **sha256** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getParents

> getParents(sha1, count, cursor)



Return parents from a given SHA1. A number of element to return and an offset must be given. If not set it will be the 100 first elements. A cursor must be given to paginate over. The starting cursor is 0.

### Example

```javascript
import HashlookupCirclApi from 'hashlookup_circl_api';

let apiInstance = new HashlookupCirclApi.DefaultApi();
let sha1 = "sha1_example"; // String | 
let count = 56; // Number | 
let cursor = "cursor_example"; // String | 
apiInstance.getParents(sha1, count, cursor, (error, data, response) => {
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
 **sha1** | **String**|  | 
 **count** | **Number**|  | 
 **cursor** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getSessionCreate

> getSessionCreate(name)



Create a session key to keep search context. The session is attached to a name. After the session is created, the header &#x60;hashlookup_session&#x60; can be set to the session name.

### Example

```javascript
import HashlookupCirclApi from 'hashlookup_circl_api';

let apiInstance = new HashlookupCirclApi.DefaultApi();
let name = "name_example"; // String | 
apiInstance.getSessionCreate(name, (error, data, response) => {
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
 **name** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getSessionMatches

> getSessionMatches(name)



Return set of matching and non-matching hashes from a session.

### Example

```javascript
import HashlookupCirclApi from 'hashlookup_circl_api';

let apiInstance = new HashlookupCirclApi.DefaultApi();
let name = "name_example"; // String | 
apiInstance.getSessionMatches(name, (error, data, response) => {
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
 **name** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getStattop

> getStattop()



Return the top 100 of most queried values.

### Example

```javascript
import HashlookupCirclApi from 'hashlookup_circl_api';

let apiInstance = new HashlookupCirclApi.DefaultApi();
apiInstance.getStattop((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postBulkmd5

> postBulkmd5()



Bulk search of MD5 hashes in a JSON array with the key &#39;hashes&#39;.

### Example

```javascript
import HashlookupCirclApi from 'hashlookup_circl_api';

let apiInstance = new HashlookupCirclApi.DefaultApi();
apiInstance.postBulkmd5((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postBulksha1

> postBulksha1()



Bulk search of SHA1 hashes in a JSON array with the &#39;hashes&#39;.

### Example

```javascript
import HashlookupCirclApi from 'hashlookup_circl_api';

let apiInstance = new HashlookupCirclApi.DefaultApi();
apiInstance.postBulksha1((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

