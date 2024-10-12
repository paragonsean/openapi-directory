# HttpbinOrg.RedirectsApi

All URIs are relative to *https://httpbin.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**absoluteRedirectNGet**](RedirectsApi.md#absoluteRedirectNGet) | **GET** /absolute-redirect/{n} | Absolutely 302 Redirects n times.
[**redirectNGet**](RedirectsApi.md#redirectNGet) | **GET** /redirect/{n} | 302 Redirects n times.
[**redirectToDelete**](RedirectsApi.md#redirectToDelete) | **DELETE** /redirect-to | 302/3XX Redirects to the given URL.
[**redirectToGet**](RedirectsApi.md#redirectToGet) | **GET** /redirect-to | 302/3XX Redirects to the given URL.
[**redirectToPatch**](RedirectsApi.md#redirectToPatch) | **PATCH** /redirect-to | 302/3XX Redirects to the given URL.
[**redirectToPost**](RedirectsApi.md#redirectToPost) | **POST** /redirect-to | 302/3XX Redirects to the given URL.
[**redirectToPut**](RedirectsApi.md#redirectToPut) | **PUT** /redirect-to | 302/3XX Redirects to the given URL.
[**redirectToTrace**](RedirectsApi.md#redirectToTrace) | **TRACE** /redirect-to | 302/3XX Redirects to the given URL.
[**relativeRedirectNGet**](RedirectsApi.md#relativeRedirectNGet) | **GET** /relative-redirect/{n} | Relatively 302 Redirects n times.



## absoluteRedirectNGet

> absoluteRedirectNGet(n)

Absolutely 302 Redirects n times.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.RedirectsApi();
let n = 56; // Number | 
apiInstance.absoluteRedirectNGet(n, (error, data, response) => {
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


## redirectNGet

> redirectNGet(n)

302 Redirects n times.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.RedirectsApi();
let n = 56; // Number | 
apiInstance.redirectNGet(n, (error, data, response) => {
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


## redirectToDelete

> redirectToDelete()

302/3XX Redirects to the given URL.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.RedirectsApi();
apiInstance.redirectToDelete((error, data, response) => {
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


## redirectToGet

> redirectToGet(url, opts)

302/3XX Redirects to the given URL.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.RedirectsApi();
let url = "url_example"; // String | 
let opts = {
  'statusCode': 56 // Number | 
};
apiInstance.redirectToGet(url, opts, (error, data, response) => {
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
 **url** | **String**|  | 
 **statusCode** | **Number**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## redirectToPatch

> redirectToPatch()

302/3XX Redirects to the given URL.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.RedirectsApi();
apiInstance.redirectToPatch((error, data, response) => {
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


## redirectToPost

> redirectToPost(url, opts)

302/3XX Redirects to the given URL.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.RedirectsApi();
let url = "url_example"; // String | 
let opts = {
  'statusCode': 56 // Number | 
};
apiInstance.redirectToPost(url, opts, (error, data, response) => {
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
 **url** | **String**|  | 
 **statusCode** | **Number**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## redirectToPut

> redirectToPut(url, opts)

302/3XX Redirects to the given URL.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.RedirectsApi();
let url = "url_example"; // String | 
let opts = {
  'statusCode': 56 // Number | 
};
apiInstance.redirectToPut(url, opts, (error, data, response) => {
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
 **url** | **String**|  | 
 **statusCode** | **Number**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## redirectToTrace

> redirectToTrace()

302/3XX Redirects to the given URL.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.RedirectsApi();
apiInstance.redirectToTrace((error, data, response) => {
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


## relativeRedirectNGet

> relativeRedirectNGet(n)

Relatively 302 Redirects n times.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.RedirectsApi();
let n = 56; // Number | 
apiInstance.relativeRedirectNGet(n, (error, data, response) => {
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

