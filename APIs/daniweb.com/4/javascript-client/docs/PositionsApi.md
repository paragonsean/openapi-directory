# DaniWebConnectApi.PositionsApi

All URIs are relative to *https://www.daniweb.com/connect/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**positionsIDDelete**](PositionsApi.md#positionsIDDelete) | **DELETE** /positions/{ID} | 
[**positionsIDPatch**](PositionsApi.md#positionsIDPatch) | **PATCH** /positions/{ID} | 
[**positionsPost**](PositionsApi.md#positionsPost) | **POST** /positions | 



## positionsIDDelete

> EndpointDeletePositionsID positionsIDDelete(ID)



Remove an item from the OAuth&#39;ed end user&#39;s Curriculum Vitae.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.PositionsApi();
let ID = 56; // Number | 
apiInstance.positionsIDDelete(ID, (error, data, response) => {
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
 **ID** | **Number**|  | 

### Return type

[**EndpointDeletePositionsID**](EndpointDeletePositionsID.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## positionsIDPatch

> EndpointPatchPositionsID positionsIDPatch(ID, category, organization, role, startDate, opts)



Update the OAuth&#39;ed end user&#39;s Curriculum Vitae by modifying an existing position.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.PositionsApi();
let ID = 56; // Number | 
let category = "category_example"; // String | 
let organization = "organization_example"; // String | 
let role = "role_example"; // String | 
let startDate = "startDate_example"; // String | 
let opts = {
  'endDate': "endDate_example", // String | 
  'organizationSize': "organizationSize_example", // String | 
  'position': "position_example", // String | 
  'summary': "summary_example", // String | 
  'url': "url_example" // String | 
};
apiInstance.positionsIDPatch(ID, category, organization, role, startDate, opts, (error, data, response) => {
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
 **ID** | **Number**|  | 
 **category** | **String**|  | 
 **organization** | **String**|  | 
 **role** | **String**|  | 
 **startDate** | **String**|  | 
 **endDate** | **String**|  | [optional] 
 **organizationSize** | **String**|  | [optional] 
 **position** | **String**|  | [optional] 
 **summary** | **String**|  | [optional] 
 **url** | **String**|  | [optional] 

### Return type

[**EndpointPatchPositionsID**](EndpointPatchPositionsID.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## positionsPost

> EndpointPostPositions positionsPost(category, organization, role, startDate, opts)



Update the OAuth&#39;ed end user&#39;s Curriculum Vitae by adding a position.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.PositionsApi();
let category = "category_example"; // String | 
let organization = "organization_example"; // String | 
let role = "role_example"; // String | 
let startDate = "startDate_example"; // String | 
let opts = {
  'endDate': "endDate_example", // String | 
  'organizationSize': "organizationSize_example", // String | 
  'position': "position_example", // String | 
  'summary': "summary_example", // String | 
  'url': "url_example" // String | 
};
apiInstance.positionsPost(category, organization, role, startDate, opts, (error, data, response) => {
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
 **category** | **String**|  | 
 **organization** | **String**|  | 
 **role** | **String**|  | 
 **startDate** | **String**|  | 
 **endDate** | **String**|  | [optional] 
 **organizationSize** | **String**|  | [optional] 
 **position** | **String**|  | [optional] 
 **summary** | **String**|  | [optional] 
 **url** | **String**|  | [optional] 

### Return type

[**EndpointPostPositions**](EndpointPostPositions.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

