# OpenFinTechIo.ExchangersApi

All URIs are relative to *https://api.openfintech.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exchangersGet**](ExchangersApi.md#exchangersGet) | **GET** /exchangers | List of exchangers
[**exchangersIdGet**](ExchangersApi.md#exchangersIdGet) | **GET** /exchangers/{id} | Exchanger by ID



## exchangersGet

> ExchangersResponse exchangersGet(opts)

List of exchangers

Returns list of exchange markets. Each object contains general information about exchanger such as name and status, also information about rates export and related link to main organization.&lt;br&gt; Rates export standards is represented by: * [estandards](http://estandards.info) * [jsons](http://jsons.info) * ratex - our internal standard 

### Example

```javascript
import OpenFinTechIo from 'open_fin_tech_io';

let apiInstance = new OpenFinTechIo.ExchangersApi();
let opts = {
  'pageNumber': 56, // Number | Current page number.
  'pageSize': 56, // Number | Page size.<br>*Default value: 100* 
  'filterName': "filterName_example", // String | Filtering by name.
  'filterStatus': ["null"], // [String] | Filtration by status.
  'sort': ["null"] // [String] | Sort params:<br>  | ASC | DESC | |-----|------| | name | -name | | status | -status | | wmid | -wmid | | rate_type | -rate_type | | rates_export_standard | <nobr>-rates_export_standard</nobr> | 
};
apiInstance.exchangersGet(opts, (error, data, response) => {
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
 **filterStatus** | [**[String]**](String.md)| Filtration by status. | [optional] 
 **sort** | [**[String]**](String.md)| Sort params:&lt;br&gt;  | ASC | DESC | |-----|------| | name | -name | | status | -status | | wmid | -wmid | | rate_type | -rate_type | | rates_export_standard | &lt;nobr&gt;-rates_export_standard&lt;/nobr&gt; |  | [optional] 

### Return type

[**ExchangersResponse**](ExchangersResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json


## exchangersIdGet

> ExchangerResponse exchangersIdGet(id)

Exchanger by ID

Returns exchanger with specific ID. 

### Example

```javascript
import OpenFinTechIo from 'open_fin_tech_io';

let apiInstance = new OpenFinTechIo.ExchangersApi();
let id = "id_example"; // String | Unique ID.
apiInstance.exchangersIdGet(id, (error, data, response) => {
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

[**ExchangerResponse**](ExchangerResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json

