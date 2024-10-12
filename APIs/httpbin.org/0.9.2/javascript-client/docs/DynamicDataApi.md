# HttpbinOrg.DynamicDataApi

All URIs are relative to *https://httpbin.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**base64ValueGet**](DynamicDataApi.md#base64ValueGet) | **GET** /base64/{value} | Decodes base64url-encoded string.
[**bytesNGet**](DynamicDataApi.md#bytesNGet) | **GET** /bytes/{n} | Returns n random bytes generated with given seed
[**delayDelayDelete**](DynamicDataApi.md#delayDelayDelete) | **DELETE** /delay/{delay} | Returns a delayed response (max of 10 seconds).
[**delayDelayGet**](DynamicDataApi.md#delayDelayGet) | **GET** /delay/{delay} | Returns a delayed response (max of 10 seconds).
[**delayDelayPatch**](DynamicDataApi.md#delayDelayPatch) | **PATCH** /delay/{delay} | Returns a delayed response (max of 10 seconds).
[**delayDelayPost**](DynamicDataApi.md#delayDelayPost) | **POST** /delay/{delay} | Returns a delayed response (max of 10 seconds).
[**delayDelayPut**](DynamicDataApi.md#delayDelayPut) | **PUT** /delay/{delay} | Returns a delayed response (max of 10 seconds).
[**delayDelayTrace**](DynamicDataApi.md#delayDelayTrace) | **TRACE** /delay/{delay} | Returns a delayed response (max of 10 seconds).
[**dripGet**](DynamicDataApi.md#dripGet) | **GET** /drip | Drips data over a duration after an optional initial delay.
[**linksNOffsetGet**](DynamicDataApi.md#linksNOffsetGet) | **GET** /links/{n}/{offset} | Generate a page containing n links to other pages which do the same.
[**rangeNumbytesGet**](DynamicDataApi.md#rangeNumbytesGet) | **GET** /range/{numbytes} | Streams n random bytes generated with given seed, at given chunk size per packet.
[**streamBytesNGet**](DynamicDataApi.md#streamBytesNGet) | **GET** /stream-bytes/{n} | Streams n random bytes generated with given seed, at given chunk size per packet.
[**streamNGet**](DynamicDataApi.md#streamNGet) | **GET** /stream/{n} | Stream n JSON responses
[**uuidGet**](DynamicDataApi.md#uuidGet) | **GET** /uuid | Return a UUID4.



## base64ValueGet

> base64ValueGet(value)

Decodes base64url-encoded string.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.DynamicDataApi();
let value = "'SFRUUEJJTiBpcyBhd2Vzb21l'"; // String | 
apiInstance.base64ValueGet(value, (error, data, response) => {
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
 **value** | **String**|  | [default to &#39;SFRUUEJJTiBpcyBhd2Vzb21l&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## bytesNGet

> bytesNGet(n)

Returns n random bytes generated with given seed

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.DynamicDataApi();
let n = 56; // Number | 
apiInstance.bytesNGet(n, (error, data, response) => {
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
 **n** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## delayDelayDelete

> delayDelayDelete(delay)

Returns a delayed response (max of 10 seconds).

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.DynamicDataApi();
let delay = 56; // Number | 
apiInstance.delayDelayDelete(delay, (error, data, response) => {
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
 **delay** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## delayDelayGet

> delayDelayGet(delay)

Returns a delayed response (max of 10 seconds).

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.DynamicDataApi();
let delay = 56; // Number | 
apiInstance.delayDelayGet(delay, (error, data, response) => {
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
 **delay** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## delayDelayPatch

> delayDelayPatch(delay)

Returns a delayed response (max of 10 seconds).

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.DynamicDataApi();
let delay = 56; // Number | 
apiInstance.delayDelayPatch(delay, (error, data, response) => {
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
 **delay** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## delayDelayPost

> delayDelayPost(delay)

Returns a delayed response (max of 10 seconds).

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.DynamicDataApi();
let delay = 56; // Number | 
apiInstance.delayDelayPost(delay, (error, data, response) => {
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
 **delay** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## delayDelayPut

> delayDelayPut(delay)

Returns a delayed response (max of 10 seconds).

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.DynamicDataApi();
let delay = 56; // Number | 
apiInstance.delayDelayPut(delay, (error, data, response) => {
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
 **delay** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## delayDelayTrace

> delayDelayTrace(delay)

Returns a delayed response (max of 10 seconds).

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.DynamicDataApi();
let delay = 56; // Number | 
apiInstance.delayDelayTrace(delay, (error, data, response) => {
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
 **delay** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## dripGet

> dripGet(opts)

Drips data over a duration after an optional initial delay.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.DynamicDataApi();
let opts = {
  'duration': 2, // Number | The amount of time (in seconds) over which to drip each byte
  'numbytes': 10, // Number | The number of bytes to respond with
  'code': 200, // Number | The response code that will be returned
  'delay': 2 // Number | The amount of time (in seconds) to delay before responding
};
apiInstance.dripGet(opts, (error, data, response) => {
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
 **duration** | **Number**| The amount of time (in seconds) over which to drip each byte | [optional] [default to 2]
 **numbytes** | **Number**| The number of bytes to respond with | [optional] [default to 10]
 **code** | **Number**| The response code that will be returned | [optional] [default to 200]
 **delay** | **Number**| The amount of time (in seconds) to delay before responding | [optional] [default to 2]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## linksNOffsetGet

> linksNOffsetGet(n, offset)

Generate a page containing n links to other pages which do the same.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.DynamicDataApi();
let n = 56; // Number | 
let offset = 56; // Number | 
apiInstance.linksNOffsetGet(n, offset, (error, data, response) => {
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
 **n** | **Number**|  | 
 **offset** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## rangeNumbytesGet

> rangeNumbytesGet(numbytes)

Streams n random bytes generated with given seed, at given chunk size per packet.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.DynamicDataApi();
let numbytes = 56; // Number | 
apiInstance.rangeNumbytesGet(numbytes, (error, data, response) => {
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
 **numbytes** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## streamBytesNGet

> streamBytesNGet(n)

Streams n random bytes generated with given seed, at given chunk size per packet.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.DynamicDataApi();
let n = 56; // Number | 
apiInstance.streamBytesNGet(n, (error, data, response) => {
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
 **n** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## streamNGet

> streamNGet(n)

Stream n JSON responses

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.DynamicDataApi();
let n = 56; // Number | 
apiInstance.streamNGet(n, (error, data, response) => {
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
 **n** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## uuidGet

> uuidGet()

Return a UUID4.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.DynamicDataApi();
apiInstance.uuidGet((error, data, response) => {
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

