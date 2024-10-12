# OpenFinTechIo.PaymentProvidersApi

All URIs are relative to *https://api.openfintech.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**paymentProvidersGet**](PaymentProvidersApi.md#paymentProvidersGet) | **GET** /payment-providers | List of payment providers
[**paymentProvidersIdGet**](PaymentProvidersApi.md#paymentProvidersIdGet) | **GET** /payment-providers/{id} | Payment provider by ID



## paymentProvidersGet

> PaymentProvidersResponse paymentProvidersGet(opts)

List of payment providers

A payment service provider (PSP) offers shops online services for accepting electronic payments by a variety of payment methods.&lt;br&gt; Endpoint returns list of PSPs. Each object contains: name, type, supported features and sales channels, also related link to available payment methods and main organization. 

### Example

```javascript
import OpenFinTechIo from 'open_fin_tech_io';

let apiInstance = new OpenFinTechIo.PaymentProvidersApi();
let opts = {
  'pageNumber': 56, // Number | Current page number.
  'pageSize': 56, // Number | Page size.<br>*Default value: 100* 
  'filterSearch': "filterSearch_example", // String | Full text search with id, code, name.
  'filterName': "filterName_example", // String | Filtering by name.
  'filterCode': "filterCode_example", // String | Filtering by code.
  'filterTypes': ["null"], // [String] | Filtering by types.
  'filterSalesChannels': ["null"], // [String] | Filtering by sales channels.
  'filterFeatures': ["null"], // [String] | Filtering by features.
  'sort': ["null"] // [String] | Sort params:<br>  | ASC | DESC | |-----|------| | name | -name | | code | -code | 
};
apiInstance.paymentProvidersGet(opts, (error, data, response) => {
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
 **filterSearch** | **String**| Full text search with id, code, name. | [optional] 
 **filterName** | **String**| Filtering by name. | [optional] 
 **filterCode** | **String**| Filtering by code. | [optional] 
 **filterTypes** | [**[String]**](String.md)| Filtering by types. | [optional] 
 **filterSalesChannels** | [**[String]**](String.md)| Filtering by sales channels. | [optional] 
 **filterFeatures** | [**[String]**](String.md)| Filtering by features. | [optional] 
 **sort** | [**[String]**](String.md)| Sort params:&lt;br&gt;  | ASC | DESC | |-----|------| | name | -name | | code | -code |  | [optional] 

### Return type

[**PaymentProvidersResponse**](PaymentProvidersResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json


## paymentProvidersIdGet

> PaymentProviderResponse paymentProvidersIdGet(id)

Payment provider by ID

Returns payment provider with specific ID. 

### Example

```javascript
import OpenFinTechIo from 'open_fin_tech_io';

let apiInstance = new OpenFinTechIo.PaymentProvidersApi();
let id = "id_example"; // String | Unique ID.
apiInstance.paymentProvidersIdGet(id, (error, data, response) => {
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

[**PaymentProviderResponse**](PaymentProviderResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json

