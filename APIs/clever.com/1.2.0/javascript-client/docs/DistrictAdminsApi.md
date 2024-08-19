# DataApi.DistrictAdminsApi

All URIs are relative to *https://api.clever.com/v1.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDistrictAdmin**](DistrictAdminsApi.md#getDistrictAdmin) | **GET** /district_admins/{id} | 
[**getDistrictAdmins**](DistrictAdminsApi.md#getDistrictAdmins) | **GET** /district_admins | 



## getDistrictAdmin

> DistrictAdminResponse getDistrictAdmin(id)



Returns a specific district admin

### Example

```javascript
import DataApi from 'data_api';
let defaultClient = DataApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataApi.DistrictAdminsApi();
let id = "id_example"; // String | 
apiInstance.getDistrictAdmin(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**DistrictAdminResponse**](DistrictAdminResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDistrictAdmins

> DistrictAdminsResponse getDistrictAdmins(opts)



Returns a list of district admins

### Example

```javascript
import DataApi from 'data_api';
let defaultClient = DataApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataApi.DistrictAdminsApi();
let opts = {
  'startingAfter': "startingAfter_example", // String | 
  'endingBefore': "endingBefore_example", // String | 
  'showLinks': "showLinks_example" // String | 
};
apiInstance.getDistrictAdmins(opts, (error, data, response) => {
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
 **startingAfter** | **String**|  | [optional] 
 **endingBefore** | **String**|  | [optional] 
 **showLinks** | **String**|  | [optional] 

### Return type

[**DistrictAdminsResponse**](DistrictAdminsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

