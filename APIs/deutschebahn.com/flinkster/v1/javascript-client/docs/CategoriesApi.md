# FlinksterApiNg.CategoriesApi

All URIs are relative to *https://api.deutschebahn.com/flinkster-api-ng/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCategory**](CategoriesApi.md#getCategory) | **GET** /providernetworks/{providernetworkUID}/categories/{categoryUID} | Get a Category by UID
[**listCategories**](CategoriesApi.md#listCategories) | **GET** /providernetworks/{providernetworkUID}/categories | Lists all categories



## getCategory

> CategoryJO getCategory(providernetworkUID, categoryUID, opts)

Get a Category by UID

Search for categorie.

### Example

```javascript
import FlinksterApiNg from 'flinkster_api_ng';

let apiInstance = new FlinksterApiNg.CategoriesApi();
let providernetworkUID = "providernetworkUID_example"; // String | Provider Network UID
let categoryUID = "categoryUID_example"; // String | 
let opts = {
  'expand': "expand_example" // String | 
};
apiInstance.getCategory(providernetworkUID, categoryUID, opts, (error, data, response) => {
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
 **providernetworkUID** | **String**| Provider Network UID | 
 **categoryUID** | **String**|  | 
 **expand** | **String**|  | [optional] 

### Return type

[**CategoryJO**](CategoryJO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listCategories

> CategoryJO listCategories(providernetworkUID, opts)

Lists all categories

Search for categorie.

### Example

```javascript
import FlinksterApiNg from 'flinkster_api_ng';

let apiInstance = new FlinksterApiNg.CategoriesApi();
let providernetworkUID = "providernetworkUID_example"; // String | 
let opts = {
  'expand': "expand_example" // String | 
};
apiInstance.listCategories(providernetworkUID, opts, (error, data, response) => {
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
 **providernetworkUID** | **String**|  | 
 **expand** | **String**|  | [optional] 

### Return type

[**CategoryJO**](CategoryJO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

