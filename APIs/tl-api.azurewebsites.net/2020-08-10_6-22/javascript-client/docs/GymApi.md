# Api.GymApi

All URIs are relative to *https://tl-api.azurewebsites.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gymGet**](GymApi.md#gymGet) | **GET** /api/Gym/{gymID} | Get gym details This will return all properties related to gym entity             



## gymGet

> DefaultResponseDTOOfGymDTO gymGet(gymID)

Get gym details This will return all properties related to gym entity             

### Example

```javascript
import Api from 'api';
let defaultClient = Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Api.GymApi();
let gymID = 56; // Number | indentity number (primary key) for gym object
apiInstance.gymGet(gymID, (error, data, response) => {
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
 **gymID** | **Number**| indentity number (primary key) for gym object | 

### Return type

[**DefaultResponseDTOOfGymDTO**](DefaultResponseDTOOfGymDTO.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

