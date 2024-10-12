# OpenFinTechIo.MerchantIndustriesApi

All URIs are relative to *https://api.openfintech.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**merchantIndustriesGet**](MerchantIndustriesApi.md#merchantIndustriesGet) | **GET** /merchant-industries | List of merchant industries
[**merchantIndustriesIdGet**](MerchantIndustriesApi.md#merchantIndustriesIdGet) | **GET** /merchant-industries/{id} | Merchant industry by ID



## merchantIndustriesGet

> MerchantIndustriesResponse merchantIndustriesGet(opts)

List of merchant industries

Returns all available merchant fields of activity. 

### Example

```javascript
import OpenFinTechIo from 'open_fin_tech_io';

let apiInstance = new OpenFinTechIo.MerchantIndustriesApi();
let opts = {
  'pageNumber': 56, // Number | Current page number.
  'pageSize': 56, // Number | Page size.<br>*Default value: 100* 
  'filterName': "filterName_example" // String | Filtering by name.
};
apiInstance.merchantIndustriesGet(opts, (error, data, response) => {
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
 **pageNumber** | **Number**| Current page number. | [optional] 
 **pageSize** | **Number**| Page size.&lt;br&gt;*Default value: 100*  | [optional] 
 **filterName** | **String**| Filtering by name. | [optional] 

### Return type

[**MerchantIndustriesResponse**](MerchantIndustriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json


## merchantIndustriesIdGet

> MerchantIndustryResponse merchantIndustriesIdGet(id)

Merchant industry by ID

Returns merchant industry with specific ID. 

### Example

```javascript
import OpenFinTechIo from 'open_fin_tech_io';

let apiInstance = new OpenFinTechIo.MerchantIndustriesApi();
let id = "id_example"; // String | Unique ID.
apiInstance.merchantIndustriesIdGet(id, (error, data, response) => {
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
 **id** | **String**| Unique ID. | 

### Return type

[**MerchantIndustryResponse**](MerchantIndustryResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json

