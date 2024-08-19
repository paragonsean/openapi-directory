# IxApi.MacsApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**macsCreate**](MacsApi.md#macsCreate) | **POST** /macs | 
[**macsDestroy**](MacsApi.md#macsDestroy) | **DELETE** /macs/{id} | 
[**macsList**](MacsApi.md#macsList) | **GET** /macs | 
[**macsRead**](MacsApi.md#macsRead) | **GET** /macs/{id} | 



## macsCreate

> MacAddress macsCreate(opts)



Register a mac address.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.MacsApi();
let opts = {
  'macAddressRequest': new IxApi.MacAddressRequest() // MacAddressRequest | MAC-Address Request
};
apiInstance.macsCreate(opts, (error, data, response) => {
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
 **macAddressRequest** | [**MacAddressRequest**](MacAddressRequest.md)| MAC-Address Request | [optional] 

### Return type

[**MacAddress**](MacAddress.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## macsDestroy

> MacAddress macsDestroy(id)



Remove a mac address.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.MacsApi();
let id = "id_example"; // String | Get by id
apiInstance.macsDestroy(id, (error, data, response) => {
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
 **id** | **String**| Get by id | 

### Return type

[**MacAddress**](MacAddress.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## macsList

> [MacAddress] macsList(opts)



List all mac addresses managed by the authorized customer.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.MacsApi();
let opts = {
  'id': ["null"], // [String] | Filter by id
  'managingAccount': "managingAccount_example", // String | Filter by managing_account
  'consumingAccount': "consumingAccount_example", // String | Filter by consuming_account
  'externalRef': "externalRef_example", // String | Filter by external_ref
  'networkServiceConfig': "networkServiceConfig_example", // String | Filter by network_service_config
  'address': "address_example", // String | Filter by address
  'assignedAt': "assignedAt_example", // String | Filter by assigned_at
  'validNotBefore': "validNotBefore_example", // String | Filter by valid_not_before
  'validNotAfter': "validNotAfter_example" // String | Filter by valid_not_after
};
apiInstance.macsList(opts, (error, data, response) => {
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
 **id** | [**[String]**](String.md)| Filter by id | [optional] 
 **managingAccount** | **String**| Filter by managing_account | [optional] 
 **consumingAccount** | **String**| Filter by consuming_account | [optional] 
 **externalRef** | **String**| Filter by external_ref | [optional] 
 **networkServiceConfig** | **String**| Filter by network_service_config | [optional] 
 **address** | **String**| Filter by address | [optional] 
 **assignedAt** | **String**| Filter by assigned_at | [optional] 
 **validNotBefore** | **String**| Filter by valid_not_before | [optional] 
 **validNotAfter** | **String**| Filter by valid_not_after | [optional] 

### Return type

[**[MacAddress]**](MacAddress.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## macsRead

> MacAddress macsRead(id)



Get a single mac address by it&#39;s id.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.MacsApi();
let id = "id_example"; // String | Get by id
apiInstance.macsRead(id, (error, data, response) => {
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
 **id** | **String**| Get by id | 

### Return type

[**MacAddress**](MacAddress.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

