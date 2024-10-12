# Reverb.SalesApi

All URIs are relative to *https://api.reverb.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesReverbGet**](SalesApi.md#salesReverbGet) | **GET** /sales/reverb | View upcoming and live Reverb official sales.
[**salesSaleIdListingsDelete**](SalesApi.md#salesSaleIdListingsDelete) | **DELETE** /sales/{sale_id}/listings | Remove a listing from a sale
[**salesSaleIdListingsPost**](SalesApi.md#salesSaleIdListingsPost) | **POST** /sales/{sale_id}/listings | Add listings to a sale
[**salesSellerGet**](SalesApi.md#salesSellerGet) | **GET** /sales/seller | View your created sales.
[**salesSlugGet**](SalesApi.md#salesSlugGet) | **GET** /sales/{slug} | 



## salesReverbGet

> salesReverbGet()

View upcoming and live Reverb official sales.

View upcoming and live Reverb official sales.

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.SalesApi();
apiInstance.salesReverbGet((error, data, response) => {
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

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## salesSaleIdListingsDelete

> salesSaleIdListingsDelete(saleId)

Remove a listing from a sale

Remove a listing from a sale

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.SalesApi();
let saleId = "saleId_example"; // String | 
apiInstance.salesSaleIdListingsDelete(saleId, (error, data, response) => {
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
 **saleId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## salesSaleIdListingsPost

> salesSaleIdListingsPost(saleId)

Add listings to a sale

Add listings to a sale

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.SalesApi();
let saleId = "saleId_example"; // String | 
apiInstance.salesSaleIdListingsPost(saleId, (error, data, response) => {
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
 **saleId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## salesSellerGet

> salesSellerGet()

View your created sales.

View your created sales.

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.SalesApi();
apiInstance.salesSellerGet((error, data, response) => {
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

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## salesSlugGet

> salesSlugGet(slug)



### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.SalesApi();
let slug = "slug_example"; // String | 
apiInstance.salesSlugGet(slug, (error, data, response) => {
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
 **slug** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

