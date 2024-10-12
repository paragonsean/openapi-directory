# OpenFinTechIo.CountriesApi

All URIs are relative to *https://api.openfintech.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**countriesGet**](CountriesApi.md#countriesGet) | **GET** /countries | List of countries
[**countriesIdGet**](CountriesApi.md#countriesIdGet) | **GET** /countries/{id} | Country by ID



## countriesGet

> CountriesResponse countriesGet(opts)

List of countries

Returns all available countries. 

### Example

```javascript
import OpenFinTechIo from 'open_fin_tech_io';

let apiInstance = new OpenFinTechIo.CountriesApi();
let opts = {
  'pageNumber': 56, // Number | Current page number.
  'pageSize': 56, // Number | Page size.<br>*Default value: 100* 
  'filterRegion': ["null"], // [String] | Filtration by region.
  'filterSubRegion': ["null"], // [String] | Filtration by sub region.
  'sort': ["null"] // [String] | Sort params:<br>  | ASC | DESC | |-----|------| | name | -name | | area | -area | | population | -population | | region | -region | | sub_region | -sub_region | 
};
apiInstance.countriesGet(opts, (error, data, response) => {
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
 **filterRegion** | [**[String]**](String.md)| Filtration by region. | [optional] 
 **filterSubRegion** | [**[String]**](String.md)| Filtration by sub region. | [optional] 
 **sort** | [**[String]**](String.md)| Sort params:&lt;br&gt;  | ASC | DESC | |-----|------| | name | -name | | area | -area | | population | -population | | region | -region | | sub_region | -sub_region |  | [optional] 

### Return type

[**CountriesResponse**](CountriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json


## countriesIdGet

> CountryResponse countriesIdGet(id)

Country by ID

Returns country with specific ID. 

### Example

```javascript
import OpenFinTechIo from 'open_fin_tech_io';

let apiInstance = new OpenFinTechIo.CountriesApi();
let id = "id_example"; // String | Unique ID.
apiInstance.countriesIdGet(id, (error, data, response) => {
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

[**CountryResponse**](CountryResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json

