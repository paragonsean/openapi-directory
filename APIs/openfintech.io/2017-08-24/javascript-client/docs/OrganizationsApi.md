# OpenFinTechIo.OrganizationsApi

All URIs are relative to *https://api.openfintech.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organizationsGet**](OrganizationsApi.md#organizationsGet) | **GET** /organizations | List of organizations
[**organizationsIdGet**](OrganizationsApi.md#organizationsIdGet) | **GET** /organizations/{id} | Organization by ID



## organizationsGet

> OrganizationsResponse organizationsGet(opts)

List of organizations

This endpoint retrievs the list of organizations present in the system. The data displays general, public information, without reference to the type of activity (for example - name, address, contacts, etc.). 

### Example

```javascript
import OpenFinTechIo from 'open_fin_tech_io';

let apiInstance = new OpenFinTechIo.OrganizationsApi();
let opts = {
  'pageNumber': 56, // Number | Current page number.
  'pageSize': 56, // Number | Page size.<br>*Default value: 100* 
  'filterSearch': "filterSearch_example", // String | Full text search with id, name, code.
  'filterName': "filterName_example", // String | Filtering by name.
  'filterCode': "filterCode_example", // String | Filtering by code.
  'filterStatus': ["null"], // [String] | Filtration by status.
  'filterIndustries': "filterIndustries_example", // String | Filtering by industries.
  'sort': ["null"] // [String] | Sort params:<br>  | ASC | DESC | |-----|------| | name | -name | | code | -code | | status | -status | | description | -description | 
};
apiInstance.organizationsGet(opts, (error, data, response) => {
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
 **filterSearch** | **String**| Full text search with id, name, code. | [optional] 
 **filterName** | **String**| Filtering by name. | [optional] 
 **filterCode** | **String**| Filtering by code. | [optional] 
 **filterStatus** | [**[String]**](String.md)| Filtration by status. | [optional] 
 **filterIndustries** | **String**| Filtering by industries. | [optional] 
 **sort** | [**[String]**](String.md)| Sort params:&lt;br&gt;  | ASC | DESC | |-----|------| | name | -name | | code | -code | | status | -status | | description | -description |  | [optional] 

### Return type

[**OrganizationsResponse**](OrganizationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json


## organizationsIdGet

> OrganizationResponse organizationsIdGet(id)

Organization by ID

Returns organization with specific ID. 

### Example

```javascript
import OpenFinTechIo from 'open_fin_tech_io';

let apiInstance = new OpenFinTechIo.OrganizationsApi();
let id = "id_example"; // String | Unique ID.
apiInstance.organizationsIdGet(id, (error, data, response) => {
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

[**OrganizationResponse**](OrganizationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json

