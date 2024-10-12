# Reverb.CspsApi

All URIs are relative to *https://api.reverb.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cspsCategoriesGet**](CspsApi.md#cspsCategoriesGet) | **GET** /csps/categories | 
[**cspsFindGet**](CspsApi.md#cspsFindGet) | **GET** /csps/find | Show comparison shopping page
[**cspsGet**](CspsApi.md#cspsGet) | **GET** /csps | Returns a set of comparison shopping pages based on the current params
[**cspsIdGet**](CspsApi.md#cspsIdGet) | **GET** /csps/{id} | 



## cspsCategoriesGet

> cspsCategoriesGet()



### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.CspsApi();
apiInstance.cspsCategoriesGet((error, data, response) => {
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


## cspsFindGet

> cspsFindGet(opts)

Show comparison shopping page

Show comparison shopping page

### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.CspsApi();
let opts = {
  'id': "id_example", // String | ID of the comparison shopping page
  'slug': "slug_example" // String | Slug of the comparison shopping page
};
apiInstance.cspsFindGet(opts, (error, data, response) => {
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
 **id** | **String**| ID of the comparison shopping page | [optional] 
 **slug** | **String**| Slug of the comparison shopping page | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## cspsGet

> cspsGet()

Returns a set of comparison shopping pages based on the current params

Returns a set of comparison shopping pages based on the current params

### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.CspsApi();
apiInstance.cspsGet((error, data, response) => {
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


## cspsIdGet

> cspsIdGet(id)



### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.CspsApi();
let id = "id_example"; // String | 
apiInstance.cspsIdGet(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

