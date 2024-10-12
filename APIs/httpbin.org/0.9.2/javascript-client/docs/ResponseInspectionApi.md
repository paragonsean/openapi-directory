# HttpbinOrg.ResponseInspectionApi

All URIs are relative to *https://httpbin.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cacheGet**](ResponseInspectionApi.md#cacheGet) | **GET** /cache | Returns a 304 if an If-Modified-Since header or If-None-Match is present. Returns the same as a GET otherwise.
[**cacheValueGet**](ResponseInspectionApi.md#cacheValueGet) | **GET** /cache/{value} | Sets a Cache-Control header for n seconds.
[**etagEtagGet**](ResponseInspectionApi.md#etagEtagGet) | **GET** /etag/{etag} | Assumes the resource has the given etag and responds to If-None-Match and If-Match headers appropriately.
[**responseHeadersGet**](ResponseInspectionApi.md#responseHeadersGet) | **GET** /response-headers | Returns a set of response headers from the query string.
[**responseHeadersPost**](ResponseInspectionApi.md#responseHeadersPost) | **POST** /response-headers | Returns a set of response headers from the query string.



## cacheGet

> cacheGet(opts)

Returns a 304 if an If-Modified-Since header or If-None-Match is present. Returns the same as a GET otherwise.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.ResponseInspectionApi();
let opts = {
  'ifModifiedSince': "ifModifiedSince_example", // String | 
  'ifNoneMatch': "ifNoneMatch_example" // String | 
};
apiInstance.cacheGet(opts, (error, data, response) => {
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
 **ifModifiedSince** | **String**|  | [optional] 
 **ifNoneMatch** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## cacheValueGet

> cacheValueGet(value)

Sets a Cache-Control header for n seconds.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.ResponseInspectionApi();
let value = 56; // Number | 
apiInstance.cacheValueGet(value, (error, data, response) => {
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
 **value** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## etagEtagGet

> etagEtagGet(etag, opts)

Assumes the resource has the given etag and responds to If-None-Match and If-Match headers appropriately.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.ResponseInspectionApi();
let etag = "etag_example"; // String | Automatically added
let opts = {
  'ifNoneMatch': "ifNoneMatch_example", // String | 
  'ifMatch': "ifMatch_example" // String | 
};
apiInstance.etagEtagGet(etag, opts, (error, data, response) => {
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
 **etag** | **String**| Automatically added | 
 **ifNoneMatch** | **String**|  | [optional] 
 **ifMatch** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## responseHeadersGet

> responseHeadersGet(opts)

Returns a set of response headers from the query string.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.ResponseInspectionApi();
let opts = {
  'freeform': {key: "null"} // {String: String} | 
};
apiInstance.responseHeadersGet(opts, (error, data, response) => {
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
 **freeform** | [**{String: String}**](String.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## responseHeadersPost

> responseHeadersPost(opts)

Returns a set of response headers from the query string.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.ResponseInspectionApi();
let opts = {
  'freeform': {key: "null"} // {String: String} | 
};
apiInstance.responseHeadersPost(opts, (error, data, response) => {
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
 **freeform** | [**{String: String}**](String.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

