# HttpbinOrg.ImagesApi

All URIs are relative to *https://httpbin.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**imageGet**](ImagesApi.md#imageGet) | **GET** /image | Returns a simple image of the type suggest by the Accept header.
[**imageJpegGet**](ImagesApi.md#imageJpegGet) | **GET** /image/jpeg | Returns a simple JPEG image.
[**imagePngGet**](ImagesApi.md#imagePngGet) | **GET** /image/png | Returns a simple PNG image.
[**imageSvgGet**](ImagesApi.md#imageSvgGet) | **GET** /image/svg | Returns a simple SVG image.
[**imageWebpGet**](ImagesApi.md#imageWebpGet) | **GET** /image/webp | Returns a simple WEBP image.



## imageGet

> imageGet()

Returns a simple image of the type suggest by the Accept header.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.ImagesApi();
apiInstance.imageGet((error, data, response) => {
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


## imageJpegGet

> imageJpegGet()

Returns a simple JPEG image.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.ImagesApi();
apiInstance.imageJpegGet((error, data, response) => {
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


## imagePngGet

> imagePngGet()

Returns a simple PNG image.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.ImagesApi();
apiInstance.imagePngGet((error, data, response) => {
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


## imageSvgGet

> imageSvgGet()

Returns a simple SVG image.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.ImagesApi();
apiInstance.imageSvgGet((error, data, response) => {
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


## imageWebpGet

> imageWebpGet()

Returns a simple WEBP image.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.ImagesApi();
apiInstance.imageWebpGet((error, data, response) => {
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

