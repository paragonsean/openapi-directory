# ApiV100.ClientApi

All URIs are relative to *https://www.envoice.in*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clientApiAll**](ClientApi.md#clientApiAll) | **GET** /api/client/all | Return all clients for the account
[**clientApiCanDelete**](ClientApi.md#clientApiCanDelete) | **GET** /api/client/candelete | Check if the provided client can be deleted
[**clientApiDelete**](ClientApi.md#clientApiDelete) | **POST** /api/client/delete | Delete an existing client
[**clientApiDetails**](ClientApi.md#clientApiDetails) | **GET** /api/client/details | Return client details. Activities and invoices included.
[**clientApiNew**](ClientApi.md#clientApiNew) | **POST** /api/client/new | Create a client
[**clientApiUpdate**](ClientApi.md#clientApiUpdate) | **POST** /api/client/update | Update an existing client



## clientApiAll

> [ClientDetailsApiModel] clientApiAll(xAuthKey, xAuthSecret)

Return all clients for the account

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.ClientApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
apiInstance.clientApiAll(xAuthKey, xAuthSecret, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]

### Return type

[**[ClientDetailsApiModel]**](ClientDetailsApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## clientApiCanDelete

> Boolean clientApiCanDelete(id, xAuthKey, xAuthSecret)

Check if the provided client can be deleted

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.ClientApi();
let id = 56; // Number | 
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
apiInstance.clientApiCanDelete(id, xAuthKey, xAuthSecret, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## clientApiDelete

> Number clientApiDelete(xAuthKey, xAuthSecret, clientDeleteApiModel)

Delete an existing client

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.ClientApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
let clientDeleteApiModel = new ApiV100.ClientDeleteApiModel(); // ClientDeleteApiModel | 
apiInstance.clientApiDelete(xAuthKey, xAuthSecret, clientDeleteApiModel, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]
 **clientDeleteApiModel** | [**ClientDeleteApiModel**](ClientDeleteApiModel.md)|  | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## clientApiDetails

> ClientDetailsApiModel clientApiDetails(id, xAuthKey, xAuthSecret)

Return client details. Activities and invoices included.

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.ClientApi();
let id = 56; // Number | 
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
apiInstance.clientApiDetails(id, xAuthKey, xAuthSecret, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]

### Return type

[**ClientDetailsApiModel**](ClientDetailsApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## clientApiNew

> Number clientApiNew(xAuthKey, xAuthSecret, clientCreateApiModel)

Create a client

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.ClientApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
let clientCreateApiModel = new ApiV100.ClientCreateApiModel(); // ClientCreateApiModel | 
apiInstance.clientApiNew(xAuthKey, xAuthSecret, clientCreateApiModel, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]
 **clientCreateApiModel** | [**ClientCreateApiModel**](ClientCreateApiModel.md)|  | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## clientApiUpdate

> clientApiUpdate(xAuthKey, xAuthSecret, clientUpdateApiModel)

Update an existing client

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.ClientApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
let clientUpdateApiModel = new ApiV100.ClientUpdateApiModel(); // ClientUpdateApiModel | 
apiInstance.clientApiUpdate(xAuthKey, xAuthSecret, clientUpdateApiModel, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]
 **clientUpdateApiModel** | [**ClientUpdateApiModel**](ClientUpdateApiModel.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
- **Accept**: Not defined

