# DaniWebConnectApi.AudiencesApi

All URIs are relative to *https://www.daniweb.com/connect/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**audiencesGet**](AudiencesApi.md#audiencesGet) | **GET** /audiences | 
[**audiencesIDGet**](AudiencesApi.md#audiencesIDGet) | **GET** /audiences/{ID} | 
[**audiencesIDMembershipsPost**](AudiencesApi.md#audiencesIDMembershipsPost) | **POST** /audiences/{ID}/memberships | 



## audiencesGet

> EndpointGetAudiences audiencesGet(opts)



Fetch all Daniapp audience segments that comprise the current access token&#39;s bubble.

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

let apiInstance = new DaniWebConnectApi.AudiencesApi();
let opts = {
  'offset': 0, // Number | 
  'limit': 50 // Number | 
};
apiInstance.audiencesGet(opts, (error, data, response) => {
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
 **offset** | **Number**|  | [optional] [default to 0]
 **limit** | **Number**|  | [optional] [default to 50]

### Return type

[**EndpointGetAudiences**](EndpointGetAudiences.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## audiencesIDGet

> EndpointGetAudiencesID audiencesIDGet(ID)



Fetch an array of Daniapp audience segments that comprise the current access token&#39;s bubble.

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

let apiInstance = new DaniWebConnectApi.AudiencesApi();
let ID = [null]; // [Number] | 
apiInstance.audiencesIDGet(ID, (error, data, response) => {
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
 **ID** | [**[Number]**](Number.md)|  | 

### Return type

[**EndpointGetAudiencesID**](EndpointGetAudiencesID.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## audiencesIDMembershipsPost

> EndpointPostAudiencesIDMemberships audiencesIDMembershipsPost(ID)



Create a membership record for the OAuth&#39;ed end-user based on the current audience segment/bubble combination.

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

let apiInstance = new DaniWebConnectApi.AudiencesApi();
let ID = 56; // Number | 
apiInstance.audiencesIDMembershipsPost(ID, (error, data, response) => {
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

[**EndpointPostAudiencesIDMemberships**](EndpointPostAudiencesIDMemberships.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

