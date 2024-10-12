# HttpbinOrg.StatusCodesApi

All URIs are relative to *https://httpbin.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**statusCodesDelete**](StatusCodesApi.md#statusCodesDelete) | **DELETE** /status/{codes} | Return status code or random status code if more than one are given
[**statusCodesGet**](StatusCodesApi.md#statusCodesGet) | **GET** /status/{codes} | Return status code or random status code if more than one are given
[**statusCodesPatch**](StatusCodesApi.md#statusCodesPatch) | **PATCH** /status/{codes} | Return status code or random status code if more than one are given
[**statusCodesPost**](StatusCodesApi.md#statusCodesPost) | **POST** /status/{codes} | Return status code or random status code if more than one are given
[**statusCodesPut**](StatusCodesApi.md#statusCodesPut) | **PUT** /status/{codes} | Return status code or random status code if more than one are given
[**statusCodesTrace**](StatusCodesApi.md#statusCodesTrace) | **TRACE** /status/{codes} | Return status code or random status code if more than one are given



## statusCodesDelete

> statusCodesDelete(codes)

Return status code or random status code if more than one are given

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.StatusCodesApi();
let codes = "codes_example"; // String | 
apiInstance.statusCodesDelete(codes, (error, data, response) => {
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
 **codes** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## statusCodesGet

> statusCodesGet(codes)

Return status code or random status code if more than one are given

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.StatusCodesApi();
let codes = "codes_example"; // String | 
apiInstance.statusCodesGet(codes, (error, data, response) => {
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
 **codes** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## statusCodesPatch

> statusCodesPatch(codes)

Return status code or random status code if more than one are given

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.StatusCodesApi();
let codes = "codes_example"; // String | 
apiInstance.statusCodesPatch(codes, (error, data, response) => {
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
 **codes** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## statusCodesPost

> statusCodesPost(codes)

Return status code or random status code if more than one are given

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.StatusCodesApi();
let codes = "codes_example"; // String | 
apiInstance.statusCodesPost(codes, (error, data, response) => {
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
 **codes** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## statusCodesPut

> statusCodesPut(codes)

Return status code or random status code if more than one are given

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.StatusCodesApi();
let codes = "codes_example"; // String | 
apiInstance.statusCodesPut(codes, (error, data, response) => {
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
 **codes** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## statusCodesTrace

> statusCodesTrace(codes)

Return status code or random status code if more than one are given

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.StatusCodesApi();
let codes = "codes_example"; // String | 
apiInstance.statusCodesTrace(codes, (error, data, response) => {
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
 **codes** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

