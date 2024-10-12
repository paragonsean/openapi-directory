# OpenFinTechIo.PaymentMethodsApi

All URIs are relative to *https://api.openfintech.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**paymentMethodsGet**](PaymentMethodsApi.md#paymentMethodsGet) | **GET** /payment-methods | List of payment methods
[**paymentMethodsIdGet**](PaymentMethodsApi.md#paymentMethodsIdGet) | **GET** /payment-methods/{id} | Payment method by ID



## paymentMethodsGet

> PaymentMethodsResponse paymentMethodsGet(opts)

List of payment methods

Returns list of payment methods. Each object contains information about payment method such as name and category, also related link to payment method issuer (which processing it). 

### Example

```javascript
import OpenFinTechIo from 'open_fin_tech_io';

let apiInstance = new OpenFinTechIo.PaymentMethodsApi();
let opts = {
  'pageNumber': 56, // Number | Current page number.
  'pageSize': 56, // Number | Page size.<br>*Default value: 100* 
  'filterSearch': "filterSearch_example", // String | Full text search with id, name, code, category.
  'filterName': "filterName_example", // String | Filtering by name.
  'filterCode': "filterCode_example", // String | Filtering by code.
  'filterProcessorName': "filterProcessorName_example", // String | Filtering by processor_name.
  'filterCategory': ["null"], // [String] | Filtering by category.
  'sort': ["null"] // [String] | Sort params:<br>  | ASC | DESC | |-----|------| | name | -name | | code | -code | | processor_name | -processor_name | | category | -category | 
};
apiInstance.paymentMethodsGet(opts, (error, data, response) => {
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
 **filterSearch** | **String**| Full text search with id, name, code, category. | [optional] 
 **filterName** | **String**| Filtering by name. | [optional] 
 **filterCode** | **String**| Filtering by code. | [optional] 
 **filterProcessorName** | **String**| Filtering by processor_name. | [optional] 
 **filterCategory** | [**[String]**](String.md)| Filtering by category. | [optional] 
 **sort** | [**[String]**](String.md)| Sort params:&lt;br&gt;  | ASC | DESC | |-----|------| | name | -name | | code | -code | | processor_name | -processor_name | | category | -category |  | [optional] 

### Return type

[**PaymentMethodsResponse**](PaymentMethodsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json


## paymentMethodsIdGet

> PaymentMethodResponse paymentMethodsIdGet(id)

Payment method by ID

Returns payment method with specific ID. 

### Example

```javascript
import OpenFinTechIo from 'open_fin_tech_io';

let apiInstance = new OpenFinTechIo.PaymentMethodsApi();
let id = "id_example"; // String | Unique ID.
apiInstance.paymentMethodsIdGet(id, (error, data, response) => {
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

[**PaymentMethodResponse**](PaymentMethodResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json

