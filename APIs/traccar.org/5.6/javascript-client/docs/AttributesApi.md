# Traccar.AttributesApi

All URIs are relative to *https://demo.traccar.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attributesComputedGet**](AttributesApi.md#attributesComputedGet) | **GET** /attributes/computed | Fetch a list of Attributes
[**attributesComputedIdDelete**](AttributesApi.md#attributesComputedIdDelete) | **DELETE** /attributes/computed/{id} | Delete an Attribute
[**attributesComputedIdPut**](AttributesApi.md#attributesComputedIdPut) | **PUT** /attributes/computed/{id} | Update an Attribute
[**attributesComputedPost**](AttributesApi.md#attributesComputedPost) | **POST** /attributes/computed | Create an Attribute



## attributesComputedGet

> [Attribute] attributesComputedGet(opts)

Fetch a list of Attributes

Without params, it returns a list of Attributes the user has access to

### Example

```javascript
import Traccar from 'traccar';
let defaultClient = Traccar.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Traccar.AttributesApi();
let opts = {
  'all': true, // Boolean | Can only be used by admins or managers to fetch all entities
  'userId': 56, // Number | Standard users can use this only with their own _userId_
  'deviceId': 56, // Number | Standard users can use this only with _deviceId_s, they have access to
  'groupId': 56, // Number | Standard users can use this only with _groupId_s, they have access to
  'refresh': true // Boolean | 
};
apiInstance.attributesComputedGet(opts, (error, data, response) => {
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
 **all** | **Boolean**| Can only be used by admins or managers to fetch all entities | [optional] 
 **userId** | **Number**| Standard users can use this only with their own _userId_ | [optional] 
 **deviceId** | **Number**| Standard users can use this only with _deviceId_s, they have access to | [optional] 
 **groupId** | **Number**| Standard users can use this only with _groupId_s, they have access to | [optional] 
 **refresh** | **Boolean**|  | [optional] 

### Return type

[**[Attribute]**](Attribute.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## attributesComputedIdDelete

> attributesComputedIdDelete(id)

Delete an Attribute

### Example

```javascript
import Traccar from 'traccar';
let defaultClient = Traccar.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Traccar.AttributesApi();
let id = 56; // Number | 
apiInstance.attributesComputedIdDelete(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## attributesComputedIdPut

> Attribute attributesComputedIdPut(id, body)

Update an Attribute

### Example

```javascript
import Traccar from 'traccar';
let defaultClient = Traccar.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Traccar.AttributesApi();
let id = 56; // Number | 
let body = new Traccar.Attribute(); // Attribute | 
apiInstance.attributesComputedIdPut(id, body, (error, data, response) => {
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
 **id** | **Number**|  | 
 **body** | [**Attribute**](Attribute.md)|  | 

### Return type

[**Attribute**](Attribute.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## attributesComputedPost

> Attribute attributesComputedPost(body)

Create an Attribute

### Example

```javascript
import Traccar from 'traccar';
let defaultClient = Traccar.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Traccar.AttributesApi();
let body = new Traccar.Attribute(); // Attribute | 
apiInstance.attributesComputedPost(body, (error, data, response) => {
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
 **body** | [**Attribute**](Attribute.md)|  | 

### Return type

[**Attribute**](Attribute.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

