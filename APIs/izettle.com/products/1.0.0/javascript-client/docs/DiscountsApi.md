# ProductLibraryApi.DiscountsApi

All URIs are relative to *https://products.izettle.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createDiscount**](DiscountsApi.md#createDiscount) | **POST** /organizations/{organizationUuid}/discounts | Create a discount
[**deleteDiscount**](DiscountsApi.md#deleteDiscount) | **DELETE** /organizations/{organizationUuid}/discounts/{discountUuid} | Delete a single discount 
[**getAllDiscounts**](DiscountsApi.md#getAllDiscounts) | **GET** /organizations/{organizationUuid}/discounts | Retrieve all discounts
[**getDiscount**](DiscountsApi.md#getDiscount) | **GET** /organizations/{organizationUuid}/discounts/{discountUuid} | Retrieve a single discount
[**updateDiscount**](DiscountsApi.md#updateDiscount) | **PUT** /organizations/{organizationUuid}/discounts/{discountUuid} | Update a single discount



## createDiscount

> createDiscount(organizationUuid, opts)

Create a discount

Creates a single discount entity. The location of the newly created discount will be available in the successful response as a HttpHeaders.LOCATION header

### Example

```javascript
import ProductLibraryApi from 'product_library_api';
let defaultClient = ProductLibraryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: ZettleOauth
let ZettleOauth = defaultClient.authentications['ZettleOauth'];
ZettleOauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ProductLibraryApi.DiscountsApi();
let organizationUuid = "organizationUuid_example"; // String | 
let opts = {
  'discountRequest': new ProductLibraryApi.DiscountRequest() // DiscountRequest | 
};
apiInstance.createDiscount(organizationUuid, opts, (error, data, response) => {
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
 **organizationUuid** | **String**|  | 
 **discountRequest** | [**DiscountRequest**](DiscountRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteDiscount

> deleteDiscount(organizationUuid, discountUuid)

Delete a single discount 

### Example

```javascript
import ProductLibraryApi from 'product_library_api';
let defaultClient = ProductLibraryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: ZettleOauth
let ZettleOauth = defaultClient.authentications['ZettleOauth'];
ZettleOauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ProductLibraryApi.DiscountsApi();
let organizationUuid = "organizationUuid_example"; // String | 
let discountUuid = "discountUuid_example"; // String | 
apiInstance.deleteDiscount(organizationUuid, discountUuid, (error, data, response) => {
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
 **organizationUuid** | **String**|  | 
 **discountUuid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAllDiscounts

> [DiscountResponse] getAllDiscounts(organizationUuid)

Retrieve all discounts

### Example

```javascript
import ProductLibraryApi from 'product_library_api';
let defaultClient = ProductLibraryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: ZettleOauth
let ZettleOauth = defaultClient.authentications['ZettleOauth'];
ZettleOauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ProductLibraryApi.DiscountsApi();
let organizationUuid = "organizationUuid_example"; // String | 
apiInstance.getAllDiscounts(organizationUuid, (error, data, response) => {
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
 **organizationUuid** | **String**|  | 

### Return type

[**[DiscountResponse]**](DiscountResponse.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDiscount

> DiscountResponse getDiscount(organizationUuid, discountUuid, opts)

Retrieve a single discount

Get the full discount with the provided UUID. The method supports conditional GET through providing a HttpHeaders.IF_NONE_MATCH header. If the conditional prerequisite is fullfilled, the full discount is returned: otherwise a 304 not modified will be returned with an empty body.

### Example

```javascript
import ProductLibraryApi from 'product_library_api';
let defaultClient = ProductLibraryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: ZettleOauth
let ZettleOauth = defaultClient.authentications['ZettleOauth'];
ZettleOauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ProductLibraryApi.DiscountsApi();
let organizationUuid = "organizationUuid_example"; // String | 
let discountUuid = "discountUuid_example"; // String | 
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | 
};
apiInstance.getDiscount(organizationUuid, discountUuid, opts, (error, data, response) => {
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
 **organizationUuid** | **String**|  | 
 **discountUuid** | **String**|  | 
 **ifNoneMatch** | **String**|  | [optional] 

### Return type

[**DiscountResponse**](DiscountResponse.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateDiscount

> updateDiscount(organizationUuid, discountUuid, discountRequest, opts)

Update a single discount

Updates a discount entity using JSON merge patch (https://tools.ietf.org/html/rfc7386). This means that only included fields will be changed: null values removes the field on the target entity, and other values updates the field. Conditional updates are supported through the HttpHeaders.IF_MATCH header. If the conditional prerequisite is fullfilled, the discount is updated: otherwise a 412 precondition failed will be returned with an empty body.

### Example

```javascript
import ProductLibraryApi from 'product_library_api';
let defaultClient = ProductLibraryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: ZettleOauth
let ZettleOauth = defaultClient.authentications['ZettleOauth'];
ZettleOauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ProductLibraryApi.DiscountsApi();
let organizationUuid = "organizationUuid_example"; // String | 
let discountUuid = "discountUuid_example"; // String | 
let discountRequest = new ProductLibraryApi.DiscountRequest(); // DiscountRequest | 
let opts = {
  'ifMatch': "ifMatch_example" // String | 
};
apiInstance.updateDiscount(organizationUuid, discountUuid, discountRequest, opts, (error, data, response) => {
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
 **organizationUuid** | **String**|  | 
 **discountUuid** | **String**|  | 
 **discountRequest** | [**DiscountRequest**](DiscountRequest.md)|  | 
 **ifMatch** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

