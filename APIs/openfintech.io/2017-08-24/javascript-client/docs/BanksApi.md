# OpenFinTechIo.BanksApi

All URIs are relative to *https://api.openfintech.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**banksGet**](BanksApi.md#banksGet) | **GET** /banks | List of banks
[**banksIdGet**](BanksApi.md#banksIdGet) | **GET** /banks/{id} | Bank by ID



## banksGet

> BanksResponse banksGet(opts)

List of banks

Returns list of banks. Each object contains general information about bank such as name and status, also information about bank details and related link to main organization. 

### Example

```javascript
import OpenFinTechIo from 'open_fin_tech_io';

let apiInstance = new OpenFinTechIo.BanksApi();
let opts = {
  'pageNumber': 56, // Number | Current page number.
  'pageSize': 56, // Number | Page size.<br>*Default value: 100* 
  'filterSortCode': "filterSortCode_example", // String | Filtering by banks code.
  'filterCode': "filterCode_example", // String | Filtering by code.
  'filterStatus': ["null"], // [String] | Filtration by status.
  'sort': ["null"] // [String] | Sort params:<br>  | ASC | DESC | |-----|------| | name | -name | | code | -code | | status | -status | | sort_code | -sort_code | 
};
apiInstance.banksGet(opts, (error, data, response) => {
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
 **filterSortCode** | **String**| Filtering by banks code. | [optional] 
 **filterCode** | **String**| Filtering by code. | [optional] 
 **filterStatus** | [**[String]**](String.md)| Filtration by status. | [optional] 
 **sort** | [**[String]**](String.md)| Sort params:&lt;br&gt;  | ASC | DESC | |-----|------| | name | -name | | code | -code | | status | -status | | sort_code | -sort_code |  | [optional] 

### Return type

[**BanksResponse**](BanksResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json


## banksIdGet

> BankResponse banksIdGet(id)

Bank by ID

Returns bank with specific ID. 

### Example

```javascript
import OpenFinTechIo from 'open_fin_tech_io';

let apiInstance = new OpenFinTechIo.BanksApi();
let id = "id_example"; // String | Unique ID.
apiInstance.banksIdGet(id, (error, data, response) => {
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

[**BankResponse**](BankResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json

