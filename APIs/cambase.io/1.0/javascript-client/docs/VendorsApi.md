# CambaseIo.VendorsApi

All URIs are relative to *http://api.cambase.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1VendorsCreate**](VendorsApi.md#apiV1VendorsCreate) | **POST** /api/v1/vendors.json | Creates a new Vendor
[**apiV1VendorsIdJsonPatch**](VendorsApi.md#apiV1VendorsIdJsonPatch) | **PATCH** /api/v1/vendors/{id}.json | Updates an existing Vendor
[**apiV1VendorsIdJsonPut**](VendorsApi.md#apiV1VendorsIdJsonPut) | **PUT** /api/v1/vendors/{id}.json | Updates an existing Vendor
[**apiV1VendorsIndex**](VendorsApi.md#apiV1VendorsIndex) | **GET** /api/v1/vendors.json | Fetches all Vendors
[**apiV1VendorsShow**](VendorsApi.md#apiV1VendorsShow) | **GET** /api/v1/vendors/{id}.json | Fetches a single Vendor



## apiV1VendorsCreate

> apiV1VendorsCreate(vendorName, opts)

Creates a new Vendor

### Example

```javascript
import CambaseIo from 'cambase_io';

let apiInstance = new CambaseIo.VendorsApi();
let vendorName = "vendorName_example"; // String | Name
let opts = {
  'vendorInfo': "vendorInfo_example", // String | Info.
  'vendorUrl': "vendorUrl_example", // String | Website
  'vendorMac': "vendorMac_example" // String | MAC
};
apiInstance.apiV1VendorsCreate(vendorName, opts, (error, data, response) => {
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
 **vendorName** | **String**| Name | 
 **vendorInfo** | **String**| Info. | [optional] 
 **vendorUrl** | **String**| Website | [optional] 
 **vendorMac** | **String**| MAC | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined


## apiV1VendorsIdJsonPatch

> apiV1VendorsIdJsonPatch(id, opts)

Updates an existing Vendor

### Example

```javascript
import CambaseIo from 'cambase_io';

let apiInstance = new CambaseIo.VendorsApi();
let id = "id_example"; // String | Vendor ID
let opts = {
  'vendorName': "vendorName_example", // String | Name
  'vendorInfo': "vendorInfo_example", // String | Info.
  'vendorUrl': "vendorUrl_example", // String | Website
  'vendorMac': "vendorMac_example" // String | MAC
};
apiInstance.apiV1VendorsIdJsonPatch(id, opts, (error, data, response) => {
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
 **id** | **String**| Vendor ID | 
 **vendorName** | **String**| Name | [optional] 
 **vendorInfo** | **String**| Info. | [optional] 
 **vendorUrl** | **String**| Website | [optional] 
 **vendorMac** | **String**| MAC | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined


## apiV1VendorsIdJsonPut

> apiV1VendorsIdJsonPut(id, opts)

Updates an existing Vendor

### Example

```javascript
import CambaseIo from 'cambase_io';

let apiInstance = new CambaseIo.VendorsApi();
let id = "id_example"; // String | Vendor ID
let opts = {
  'vendorName': "vendorName_example", // String | Name
  'vendorInfo': "vendorInfo_example", // String | Info.
  'vendorUrl': "vendorUrl_example", // String | Website
  'vendorMac': "vendorMac_example" // String | MAC
};
apiInstance.apiV1VendorsIdJsonPut(id, opts, (error, data, response) => {
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
 **id** | **String**| Vendor ID | 
 **vendorName** | **String**| Name | [optional] 
 **vendorInfo** | **String**| Info. | [optional] 
 **vendorUrl** | **String**| Website | [optional] 
 **vendorMac** | **String**| MAC | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined


## apiV1VendorsIndex

> apiV1VendorsIndex(opts)

Fetches all Vendors

### Example

```javascript
import CambaseIo from 'cambase_io';

let apiInstance = new CambaseIo.VendorsApi();
let opts = {
  'page': 56, // Number | Page number
  'order': "order_example" // String | Sort order
};
apiInstance.apiV1VendorsIndex(opts, (error, data, response) => {
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
 **page** | **Number**| Page number | [optional] 
 **order** | **String**| Sort order | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiV1VendorsShow

> apiV1VendorsShow(id, opts)

Fetches a single Vendor

### Example

```javascript
import CambaseIo from 'cambase_io';

let apiInstance = new CambaseIo.VendorsApi();
let id = "id_example"; // String | Vendor ID
let opts = {
  'order': "order_example" // String | Sort order
};
apiInstance.apiV1VendorsShow(id, opts, (error, data, response) => {
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
 **id** | **String**| Vendor ID | 
 **order** | **String**| Sort order | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

