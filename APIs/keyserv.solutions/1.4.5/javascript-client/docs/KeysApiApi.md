# KeyServ.KeysApiApi

All URIs are relative to *https://keyserv.solutions*

Method | HTTP request | Description
------------- | ------------- | -------------
[**keysApiCurrent**](KeysApiApi.md#keysApiCurrent) | **GET** /v1/KeysApi/Current/{serial} | 
[**keysApiCustom**](KeysApiApi.md#keysApiCustom) | **GET** /v1/KeysApi/Custom/{serial} | 
[**keysApiExpiry**](KeysApiApi.md#keysApiExpiry) | **GET** /v1/KeysApi/Expiry/{serial} | 
[**keysApiFind**](KeysApiApi.md#keysApiFind) | **GET** /v1/KeysApi/Find/{serial} | 



## keysApiCurrent

> KeysApiCurrent200Response keysApiCurrent(serial)



### Example

```javascript
import KeyServ from 'key_serv';

let apiInstance = new KeyServ.KeysApiApi();
let serial = "serial_example"; // String | 
apiInstance.keysApiCurrent(serial, (error, data, response) => {
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
 **serial** | **String**|  | 

### Return type

[**KeysApiCurrent200Response**](KeysApiCurrent200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## keysApiCustom

> File keysApiCustom(serial)



### Example

```javascript
import KeyServ from 'key_serv';

let apiInstance = new KeyServ.KeysApiApi();
let serial = "serial_example"; // String | 
apiInstance.keysApiCustom(serial, (error, data, response) => {
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
 **serial** | **String**|  | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## keysApiExpiry

> KeysApiExpiry200Response keysApiExpiry(serial)



### Example

```javascript
import KeyServ from 'key_serv';

let apiInstance = new KeyServ.KeysApiApi();
let serial = "serial_example"; // String | 
apiInstance.keysApiExpiry(serial, (error, data, response) => {
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
 **serial** | **String**|  | 

### Return type

[**KeysApiExpiry200Response**](KeysApiExpiry200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## keysApiFind

> KeysApiFind200Response keysApiFind(serial)



### Example

```javascript
import KeyServ from 'key_serv';

let apiInstance = new KeyServ.KeysApiApi();
let serial = "serial_example"; // String | 
apiInstance.keysApiFind(serial, (error, data, response) => {
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
 **serial** | **String**|  | 

### Return type

[**KeysApiFind200Response**](KeysApiFind200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

