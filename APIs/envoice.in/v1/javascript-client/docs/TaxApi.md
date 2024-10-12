# ApiV100.TaxApi

All URIs are relative to *https://www.envoice.in*

Method | HTTP request | Description
------------- | ------------- | -------------
[**taxApiAll**](TaxApi.md#taxApiAll) | **GET** /api/tax/all | Return all taxes for the account
[**taxApiDelete**](TaxApi.md#taxApiDelete) | **POST** /api/tax/delete | Delete an existing tax
[**taxApiNew**](TaxApi.md#taxApiNew) | **POST** /api/tax/new | Create a tax
[**taxApiUpdate**](TaxApi.md#taxApiUpdate) | **POST** /api/tax/update | Update an existing tax



## taxApiAll

> [TaxDetailsApiModel] taxApiAll(xAuthKey, xAuthSecret)

Return all taxes for the account

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.TaxApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
apiInstance.taxApiAll(xAuthKey, xAuthSecret, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]

### Return type

[**[TaxDetailsApiModel]**](TaxDetailsApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## taxApiDelete

> Number taxApiDelete(xAuthKey, xAuthSecret, taxDeleteApiModel)

Delete an existing tax

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.TaxApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
let taxDeleteApiModel = new ApiV100.TaxDeleteApiModel(); // TaxDeleteApiModel | 
apiInstance.taxApiDelete(xAuthKey, xAuthSecret, taxDeleteApiModel, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]
 **taxDeleteApiModel** | [**TaxDeleteApiModel**](TaxDeleteApiModel.md)|  | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## taxApiNew

> Number taxApiNew(xAuthKey, xAuthSecret, taxCreateApiModel)

Create a tax

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.TaxApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
let taxCreateApiModel = new ApiV100.TaxCreateApiModel(); // TaxCreateApiModel | 
apiInstance.taxApiNew(xAuthKey, xAuthSecret, taxCreateApiModel, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]
 **taxCreateApiModel** | [**TaxCreateApiModel**](TaxCreateApiModel.md)|  | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## taxApiUpdate

> taxApiUpdate(xAuthKey, xAuthSecret, taxUpdateApiModel)

Update an existing tax

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.TaxApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
let taxUpdateApiModel = new ApiV100.TaxUpdateApiModel(); // TaxUpdateApiModel | 
apiInstance.taxApiUpdate(xAuthKey, xAuthSecret, taxUpdateApiModel, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]
 **taxUpdateApiModel** | [**TaxUpdateApiModel**](TaxUpdateApiModel.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
- **Accept**: Not defined

