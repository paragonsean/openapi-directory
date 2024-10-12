# HttpbinOrg.ResponseFormatsApi

All URIs are relative to *https://httpbin.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**brotliGet**](ResponseFormatsApi.md#brotliGet) | **GET** /brotli | Returns Brotli-encoded data.
[**deflateGet**](ResponseFormatsApi.md#deflateGet) | **GET** /deflate | Returns Deflate-encoded data.
[**denyGet**](ResponseFormatsApi.md#denyGet) | **GET** /deny | Returns page denied by robots.txt rules.
[**encodingUtf8Get**](ResponseFormatsApi.md#encodingUtf8Get) | **GET** /encoding/utf8 | Returns a UTF-8 encoded body.
[**gzipGet**](ResponseFormatsApi.md#gzipGet) | **GET** /gzip | Returns GZip-encoded data.
[**htmlGet**](ResponseFormatsApi.md#htmlGet) | **GET** /html | Returns a simple HTML document.
[**jsonGet**](ResponseFormatsApi.md#jsonGet) | **GET** /json | Returns a simple JSON document.
[**robotsTxtGet**](ResponseFormatsApi.md#robotsTxtGet) | **GET** /robots.txt | Returns some robots.txt rules.
[**xmlGet**](ResponseFormatsApi.md#xmlGet) | **GET** /xml | Returns a simple XML document.



## brotliGet

> brotliGet()

Returns Brotli-encoded data.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.ResponseFormatsApi();
apiInstance.brotliGet((error, data, response) => {
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


## deflateGet

> deflateGet()

Returns Deflate-encoded data.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.ResponseFormatsApi();
apiInstance.deflateGet((error, data, response) => {
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


## denyGet

> denyGet()

Returns page denied by robots.txt rules.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.ResponseFormatsApi();
apiInstance.denyGet((error, data, response) => {
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


## encodingUtf8Get

> encodingUtf8Get()

Returns a UTF-8 encoded body.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.ResponseFormatsApi();
apiInstance.encodingUtf8Get((error, data, response) => {
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


## gzipGet

> gzipGet()

Returns GZip-encoded data.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.ResponseFormatsApi();
apiInstance.gzipGet((error, data, response) => {
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


## htmlGet

> htmlGet()

Returns a simple HTML document.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.ResponseFormatsApi();
apiInstance.htmlGet((error, data, response) => {
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


## jsonGet

> jsonGet()

Returns a simple JSON document.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.ResponseFormatsApi();
apiInstance.jsonGet((error, data, response) => {
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


## robotsTxtGet

> robotsTxtGet()

Returns some robots.txt rules.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.ResponseFormatsApi();
apiInstance.robotsTxtGet((error, data, response) => {
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


## xmlGet

> xmlGet()

Returns a simple XML document.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.ResponseFormatsApi();
apiInstance.xmlGet((error, data, response) => {
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

