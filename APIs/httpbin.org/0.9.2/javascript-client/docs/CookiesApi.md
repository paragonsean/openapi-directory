# HttpbinOrg.CookiesApi

All URIs are relative to *https://httpbin.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cookiesDeleteGet**](CookiesApi.md#cookiesDeleteGet) | **GET** /cookies/delete | Deletes cookie(s) as provided by the query string and redirects to cookie list.
[**cookiesGet**](CookiesApi.md#cookiesGet) | **GET** /cookies | Returns cookie data.
[**cookiesSetGet**](CookiesApi.md#cookiesSetGet) | **GET** /cookies/set | Sets cookie(s) as provided by the query string and redirects to cookie list.
[**cookiesSetNameValueGet**](CookiesApi.md#cookiesSetNameValueGet) | **GET** /cookies/set/{name}/{value} | Sets a cookie and redirects to cookie list.



## cookiesDeleteGet

> cookiesDeleteGet(opts)

Deletes cookie(s) as provided by the query string and redirects to cookie list.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.CookiesApi();
let opts = {
  'freeform': {key: "null"} // {String: String} | 
};
apiInstance.cookiesDeleteGet(opts, (error, data, response) => {
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


## cookiesGet

> cookiesGet()

Returns cookie data.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.CookiesApi();
apiInstance.cookiesGet((error, data, response) => {
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


## cookiesSetGet

> cookiesSetGet(opts)

Sets cookie(s) as provided by the query string and redirects to cookie list.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.CookiesApi();
let opts = {
  'freeform': {key: "null"} // {String: String} | 
};
apiInstance.cookiesSetGet(opts, (error, data, response) => {
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


## cookiesSetNameValueGet

> cookiesSetNameValueGet(name, value)

Sets a cookie and redirects to cookie list.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.CookiesApi();
let name = "name_example"; // String | 
let value = "value_example"; // String | 
apiInstance.cookiesSetNameValueGet(name, value, (error, data, response) => {
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
 **value** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

