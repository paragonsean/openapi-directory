# Api.PackageApi

All URIs are relative to *https://tl-api.azurewebsites.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**packageDelete**](PackageApi.md#packageDelete) | **DELETE** /api/Package | Delete existing package             
[**packageGet**](PackageApi.md#packageGet) | **GET** /api/Package | Get package details by packageId             
[**packagePost**](PackageApi.md#packagePost) | **POST** /api/Package | Insert new package into the system             
[**packagePut**](PackageApi.md#packagePut) | **PUT** /api/Package | Update existing package by its ID             
[**packageSearch**](PackageApi.md#packageSearch) | **GET** /api/Package/Search | Search packages             
[**packageUpdateStatus**](PackageApi.md#packageUpdateStatus) | **PUT** /api/Package/UpdateStatus | Status update of existing package 



## packageDelete

> DefaultResponseDTOOfBoolean packageDelete(opts)

Delete existing package             

### Example

```javascript
import Api from 'api';
let defaultClient = Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Api.PackageApi();
let opts = {
  'packageId': 56 // Number | primary key of package entity
};
apiInstance.packageDelete(opts, (error, data, response) => {
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
 **packageId** | **Number**| primary key of package entity | [optional] 

### Return type

[**DefaultResponseDTOOfBoolean**](DefaultResponseDTOOfBoolean.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## packageGet

> DefaultResponseDTOOfPackageDTO packageGet(opts)

Get package details by packageId             

### Example

```javascript
import Api from 'api';
let defaultClient = Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Api.PackageApi();
let opts = {
  'packageId': 56 // Number | primary key of package entity
};
apiInstance.packageGet(opts, (error, data, response) => {
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
 **packageId** | **Number**| primary key of package entity | [optional] 

### Return type

[**DefaultResponseDTOOfPackageDTO**](DefaultResponseDTOOfPackageDTO.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## packagePost

> DefaultResponseDTOOfStatusDTO packagePost(packageDTO)

Insert new package into the system             

### Example

```javascript
import Api from 'api';
let defaultClient = Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Api.PackageApi();
let packageDTO = new Api.PackageDTO(); // PackageDTO | package object
apiInstance.packagePost(packageDTO, (error, data, response) => {
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
 **packageDTO** | [**PackageDTO**](PackageDTO.md)| package object | 

### Return type

[**DefaultResponseDTOOfStatusDTO**](DefaultResponseDTOOfStatusDTO.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## packagePut

> DefaultResponseDTOOfStatusDTO packagePut(packageDTO)

Update existing package by its ID             

### Example

```javascript
import Api from 'api';
let defaultClient = Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Api.PackageApi();
let packageDTO = new Api.PackageDTO(); // PackageDTO | package object
apiInstance.packagePut(packageDTO, (error, data, response) => {
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
 **packageDTO** | [**PackageDTO**](PackageDTO.md)| package object | 

### Return type

[**DefaultResponseDTOOfStatusDTO**](DefaultResponseDTOOfStatusDTO.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## packageSearch

> [DefaultResponseDTOOfPackageSearchDTO] packageSearch(opts)

Search packages             

### Example

```javascript
import Api from 'api';
let defaultClient = Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Api.PackageApi();
let opts = {
  'searchText': "searchText_example", // String | part of package name
  'gymId': -1, // Number | primary key of TL gym entity
  'type': "'all'", // String | filter package type.!-- default is 'all'
  'orderBy': "'1'", // String | order by column.!-- invalid column will give internal server error
  'limit': 100, // Number | number of recode in result and default is 100. use negative numbers to order by desc
  'offset': 0, // Number | number of recodes to skip
  'activeStatus': 1, // Number | active status active : 1, inactive : 2, all 3, deafult : 1
  'categoryId': -1, // Number | Packge Category Id
  'startpPrice': 0, // Number | Start price of the price Range
  'endPrice': 9999999, // Number | End Price of the price Range
  'requestSource': 1 // Number | 1 : MRM, 2 : Mobile 
};
apiInstance.packageSearch(opts, (error, data, response) => {
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
 **searchText** | **String**| part of package name | [optional] 
 **gymId** | **Number**| primary key of TL gym entity | [optional] [default to -1]
 **type** | **String**| filter package type.!-- default is &#39;all&#39; | [optional] [default to &#39;all&#39;]
 **orderBy** | **String**| order by column.!-- invalid column will give internal server error | [optional] [default to &#39;1&#39;]
 **limit** | **Number**| number of recode in result and default is 100. use negative numbers to order by desc | [optional] [default to 100]
 **offset** | **Number**| number of recodes to skip | [optional] [default to 0]
 **activeStatus** | **Number**| active status active : 1, inactive : 2, all 3, deafult : 1 | [optional] [default to 1]
 **categoryId** | **Number**| Packge Category Id | [optional] [default to -1]
 **startpPrice** | **Number**| Start price of the price Range | [optional] [default to 0]
 **endPrice** | **Number**| End Price of the price Range | [optional] [default to 9999999]
 **requestSource** | **Number**| 1 : MRM, 2 : Mobile  | [optional] [default to 1]

### Return type

[**[DefaultResponseDTOOfPackageSearchDTO]**](DefaultResponseDTOOfPackageSearchDTO.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## packageUpdateStatus

> DefaultResponseDTOOfBoolean packageUpdateStatus(opts)

Status update of existing package 

### Example

```javascript
import Api from 'api';
let defaultClient = Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Api.PackageApi();
let opts = {
  'packageId': 56, // Number | package Id
  'status': 1, // Number | status : 1 activate, 2 : deactivate
  'userName': "'system'" // String | Status updated User
};
apiInstance.packageUpdateStatus(opts, (error, data, response) => {
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
 **packageId** | **Number**| package Id | [optional] 
 **status** | **Number**| status : 1 activate, 2 : deactivate | [optional] [default to 1]
 **userName** | **String**| Status updated User | [optional] [default to &#39;system&#39;]

### Return type

[**DefaultResponseDTOOfBoolean**](DefaultResponseDTOOfBoolean.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

