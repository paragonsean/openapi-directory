# NetBoxApi.IpamApi

All URIs are relative to *http://netboxdemo.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ipamAggregatesCreate**](IpamApi.md#ipamAggregatesCreate) | **POST** /ipam/aggregates/ | 
[**ipamAggregatesDelete**](IpamApi.md#ipamAggregatesDelete) | **DELETE** /ipam/aggregates/{id}/ | 
[**ipamAggregatesList**](IpamApi.md#ipamAggregatesList) | **GET** /ipam/aggregates/ | 
[**ipamAggregatesPartialUpdate**](IpamApi.md#ipamAggregatesPartialUpdate) | **PATCH** /ipam/aggregates/{id}/ | 
[**ipamAggregatesRead**](IpamApi.md#ipamAggregatesRead) | **GET** /ipam/aggregates/{id}/ | 
[**ipamAggregatesUpdate**](IpamApi.md#ipamAggregatesUpdate) | **PUT** /ipam/aggregates/{id}/ | 
[**ipamChoicesList**](IpamApi.md#ipamChoicesList) | **GET** /ipam/_choices/ | 
[**ipamChoicesRead**](IpamApi.md#ipamChoicesRead) | **GET** /ipam/_choices/{id}/ | 
[**ipamIpAddressesCreate**](IpamApi.md#ipamIpAddressesCreate) | **POST** /ipam/ip-addresses/ | 
[**ipamIpAddressesDelete**](IpamApi.md#ipamIpAddressesDelete) | **DELETE** /ipam/ip-addresses/{id}/ | 
[**ipamIpAddressesList**](IpamApi.md#ipamIpAddressesList) | **GET** /ipam/ip-addresses/ | 
[**ipamIpAddressesPartialUpdate**](IpamApi.md#ipamIpAddressesPartialUpdate) | **PATCH** /ipam/ip-addresses/{id}/ | 
[**ipamIpAddressesRead**](IpamApi.md#ipamIpAddressesRead) | **GET** /ipam/ip-addresses/{id}/ | 
[**ipamIpAddressesUpdate**](IpamApi.md#ipamIpAddressesUpdate) | **PUT** /ipam/ip-addresses/{id}/ | 
[**ipamPrefixesAvailableIpsCreate**](IpamApi.md#ipamPrefixesAvailableIpsCreate) | **POST** /ipam/prefixes/{id}/available-ips/ | 
[**ipamPrefixesAvailableIpsRead**](IpamApi.md#ipamPrefixesAvailableIpsRead) | **GET** /ipam/prefixes/{id}/available-ips/ | 
[**ipamPrefixesAvailablePrefixesCreate**](IpamApi.md#ipamPrefixesAvailablePrefixesCreate) | **POST** /ipam/prefixes/{id}/available-prefixes/ | 
[**ipamPrefixesAvailablePrefixesRead**](IpamApi.md#ipamPrefixesAvailablePrefixesRead) | **GET** /ipam/prefixes/{id}/available-prefixes/ | 
[**ipamPrefixesCreate**](IpamApi.md#ipamPrefixesCreate) | **POST** /ipam/prefixes/ | 
[**ipamPrefixesDelete**](IpamApi.md#ipamPrefixesDelete) | **DELETE** /ipam/prefixes/{id}/ | 
[**ipamPrefixesList**](IpamApi.md#ipamPrefixesList) | **GET** /ipam/prefixes/ | 
[**ipamPrefixesPartialUpdate**](IpamApi.md#ipamPrefixesPartialUpdate) | **PATCH** /ipam/prefixes/{id}/ | 
[**ipamPrefixesRead**](IpamApi.md#ipamPrefixesRead) | **GET** /ipam/prefixes/{id}/ | 
[**ipamPrefixesUpdate**](IpamApi.md#ipamPrefixesUpdate) | **PUT** /ipam/prefixes/{id}/ | 
[**ipamRirsCreate**](IpamApi.md#ipamRirsCreate) | **POST** /ipam/rirs/ | 
[**ipamRirsDelete**](IpamApi.md#ipamRirsDelete) | **DELETE** /ipam/rirs/{id}/ | 
[**ipamRirsList**](IpamApi.md#ipamRirsList) | **GET** /ipam/rirs/ | 
[**ipamRirsPartialUpdate**](IpamApi.md#ipamRirsPartialUpdate) | **PATCH** /ipam/rirs/{id}/ | 
[**ipamRirsRead**](IpamApi.md#ipamRirsRead) | **GET** /ipam/rirs/{id}/ | 
[**ipamRirsUpdate**](IpamApi.md#ipamRirsUpdate) | **PUT** /ipam/rirs/{id}/ | 
[**ipamRolesCreate**](IpamApi.md#ipamRolesCreate) | **POST** /ipam/roles/ | 
[**ipamRolesDelete**](IpamApi.md#ipamRolesDelete) | **DELETE** /ipam/roles/{id}/ | 
[**ipamRolesList**](IpamApi.md#ipamRolesList) | **GET** /ipam/roles/ | 
[**ipamRolesPartialUpdate**](IpamApi.md#ipamRolesPartialUpdate) | **PATCH** /ipam/roles/{id}/ | 
[**ipamRolesRead**](IpamApi.md#ipamRolesRead) | **GET** /ipam/roles/{id}/ | 
[**ipamRolesUpdate**](IpamApi.md#ipamRolesUpdate) | **PUT** /ipam/roles/{id}/ | 
[**ipamServicesCreate**](IpamApi.md#ipamServicesCreate) | **POST** /ipam/services/ | 
[**ipamServicesDelete**](IpamApi.md#ipamServicesDelete) | **DELETE** /ipam/services/{id}/ | 
[**ipamServicesList**](IpamApi.md#ipamServicesList) | **GET** /ipam/services/ | 
[**ipamServicesPartialUpdate**](IpamApi.md#ipamServicesPartialUpdate) | **PATCH** /ipam/services/{id}/ | 
[**ipamServicesRead**](IpamApi.md#ipamServicesRead) | **GET** /ipam/services/{id}/ | 
[**ipamServicesUpdate**](IpamApi.md#ipamServicesUpdate) | **PUT** /ipam/services/{id}/ | 
[**ipamVlanGroupsCreate**](IpamApi.md#ipamVlanGroupsCreate) | **POST** /ipam/vlan-groups/ | 
[**ipamVlanGroupsDelete**](IpamApi.md#ipamVlanGroupsDelete) | **DELETE** /ipam/vlan-groups/{id}/ | 
[**ipamVlanGroupsList**](IpamApi.md#ipamVlanGroupsList) | **GET** /ipam/vlan-groups/ | 
[**ipamVlanGroupsPartialUpdate**](IpamApi.md#ipamVlanGroupsPartialUpdate) | **PATCH** /ipam/vlan-groups/{id}/ | 
[**ipamVlanGroupsRead**](IpamApi.md#ipamVlanGroupsRead) | **GET** /ipam/vlan-groups/{id}/ | 
[**ipamVlanGroupsUpdate**](IpamApi.md#ipamVlanGroupsUpdate) | **PUT** /ipam/vlan-groups/{id}/ | 
[**ipamVlansCreate**](IpamApi.md#ipamVlansCreate) | **POST** /ipam/vlans/ | 
[**ipamVlansDelete**](IpamApi.md#ipamVlansDelete) | **DELETE** /ipam/vlans/{id}/ | 
[**ipamVlansList**](IpamApi.md#ipamVlansList) | **GET** /ipam/vlans/ | 
[**ipamVlansPartialUpdate**](IpamApi.md#ipamVlansPartialUpdate) | **PATCH** /ipam/vlans/{id}/ | 
[**ipamVlansRead**](IpamApi.md#ipamVlansRead) | **GET** /ipam/vlans/{id}/ | 
[**ipamVlansUpdate**](IpamApi.md#ipamVlansUpdate) | **PUT** /ipam/vlans/{id}/ | 
[**ipamVrfsCreate**](IpamApi.md#ipamVrfsCreate) | **POST** /ipam/vrfs/ | 
[**ipamVrfsDelete**](IpamApi.md#ipamVrfsDelete) | **DELETE** /ipam/vrfs/{id}/ | 
[**ipamVrfsList**](IpamApi.md#ipamVrfsList) | **GET** /ipam/vrfs/ | 
[**ipamVrfsPartialUpdate**](IpamApi.md#ipamVrfsPartialUpdate) | **PATCH** /ipam/vrfs/{id}/ | 
[**ipamVrfsRead**](IpamApi.md#ipamVrfsRead) | **GET** /ipam/vrfs/{id}/ | 
[**ipamVrfsUpdate**](IpamApi.md#ipamVrfsUpdate) | **PUT** /ipam/vrfs/{id}/ | 



## ipamAggregatesCreate

> Aggregate ipamAggregatesCreate(writableAggregate)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let writableAggregate = new NetBoxApi.WritableAggregate(); // WritableAggregate | 
apiInstance.ipamAggregatesCreate(writableAggregate, (error, data, response) => {
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
 **writableAggregate** | [**WritableAggregate**](WritableAggregate.md)|  | 

### Return type

[**Aggregate**](Aggregate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ipamAggregatesDelete

> ipamAggregatesDelete(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let id = 56; // Number | A unique integer value identifying this aggregate.
apiInstance.ipamAggregatesDelete(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this aggregate. | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## ipamAggregatesList

> IpamAggregatesList200Response ipamAggregatesList(opts)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let opts = {
  'family': "family_example", // String | 
  'dateAdded': "dateAdded_example", // String | 
  'idIn': "idIn_example", // String | Multiple values may be separated by commas.
  'q': "q_example", // String | 
  'rirId': "rirId_example", // String | 
  'rir': "rir_example", // String | 
  'tag': "tag_example", // String | 
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.ipamAggregatesList(opts, (error, data, response) => {
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
 **family** | **String**|  | [optional] 
 **dateAdded** | **String**|  | [optional] 
 **idIn** | **String**| Multiple values may be separated by commas. | [optional] 
 **q** | **String**|  | [optional] 
 **rirId** | **String**|  | [optional] 
 **rir** | **String**|  | [optional] 
 **tag** | **String**|  | [optional] 
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**IpamAggregatesList200Response**](IpamAggregatesList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ipamAggregatesPartialUpdate

> Aggregate ipamAggregatesPartialUpdate(id, writableAggregate)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let id = 56; // Number | A unique integer value identifying this aggregate.
let writableAggregate = new NetBoxApi.WritableAggregate(); // WritableAggregate | 
apiInstance.ipamAggregatesPartialUpdate(id, writableAggregate, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this aggregate. | 
 **writableAggregate** | [**WritableAggregate**](WritableAggregate.md)|  | 

### Return type

[**Aggregate**](Aggregate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ipamAggregatesRead

> Aggregate ipamAggregatesRead(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let id = 56; // Number | A unique integer value identifying this aggregate.
apiInstance.ipamAggregatesRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this aggregate. | 

### Return type

[**Aggregate**](Aggregate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ipamAggregatesUpdate

> Aggregate ipamAggregatesUpdate(id, writableAggregate)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let id = 56; // Number | A unique integer value identifying this aggregate.
let writableAggregate = new NetBoxApi.WritableAggregate(); // WritableAggregate | 
apiInstance.ipamAggregatesUpdate(id, writableAggregate, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this aggregate. | 
 **writableAggregate** | [**WritableAggregate**](WritableAggregate.md)|  | 

### Return type

[**Aggregate**](Aggregate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ipamChoicesList

> ipamChoicesList()





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
apiInstance.ipamChoicesList((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## ipamChoicesRead

> ipamChoicesRead(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let id = "id_example"; // String | 
apiInstance.ipamChoicesRead(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## ipamIpAddressesCreate

> IPAddress ipamIpAddressesCreate(writableIPAddress)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let writableIPAddress = new NetBoxApi.WritableIPAddress(); // WritableIPAddress | 
apiInstance.ipamIpAddressesCreate(writableIPAddress, (error, data, response) => {
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
 **writableIPAddress** | [**WritableIPAddress**](WritableIPAddress.md)|  | 

### Return type

[**IPAddress**](IPAddress.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ipamIpAddressesDelete

> ipamIpAddressesDelete(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let id = 56; // Number | A unique integer value identifying this IP address.
apiInstance.ipamIpAddressesDelete(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this IP address. | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## ipamIpAddressesList

> IpamIpAddressesList200Response ipamIpAddressesList(opts)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let opts = {
  'family': "family_example", // String | 
  'idIn': "idIn_example", // String | Multiple values may be separated by commas.
  'q': "q_example", // String | 
  'parent': "parent_example", // String | 
  'address': "address_example", // String | 
  'maskLength': 3.4, // Number | 
  'vrfId': "vrfId_example", // String | 
  'vrf': "vrf_example", // String | 
  'tenantId': "tenantId_example", // String | 
  'tenant': "tenant_example", // String | 
  'device': "device_example", // String | 
  'deviceId': 3.4, // Number | 
  'virtualMachineId': "virtualMachineId_example", // String | 
  'virtualMachine': "virtualMachine_example", // String | 
  'interfaceId': "interfaceId_example", // String | 
  'status': "status_example", // String | 
  'role': "role_example", // String | 
  'tag': "tag_example", // String | 
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.ipamIpAddressesList(opts, (error, data, response) => {
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
 **family** | **String**|  | [optional] 
 **idIn** | **String**| Multiple values may be separated by commas. | [optional] 
 **q** | **String**|  | [optional] 
 **parent** | **String**|  | [optional] 
 **address** | **String**|  | [optional] 
 **maskLength** | **Number**|  | [optional] 
 **vrfId** | **String**|  | [optional] 
 **vrf** | **String**|  | [optional] 
 **tenantId** | **String**|  | [optional] 
 **tenant** | **String**|  | [optional] 
 **device** | **String**|  | [optional] 
 **deviceId** | **Number**|  | [optional] 
 **virtualMachineId** | **String**|  | [optional] 
 **virtualMachine** | **String**|  | [optional] 
 **interfaceId** | **String**|  | [optional] 
 **status** | **String**|  | [optional] 
 **role** | **String**|  | [optional] 
 **tag** | **String**|  | [optional] 
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**IpamIpAddressesList200Response**](IpamIpAddressesList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ipamIpAddressesPartialUpdate

> IPAddress ipamIpAddressesPartialUpdate(id, writableIPAddress)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let id = 56; // Number | A unique integer value identifying this IP address.
let writableIPAddress = new NetBoxApi.WritableIPAddress(); // WritableIPAddress | 
apiInstance.ipamIpAddressesPartialUpdate(id, writableIPAddress, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this IP address. | 
 **writableIPAddress** | [**WritableIPAddress**](WritableIPAddress.md)|  | 

### Return type

[**IPAddress**](IPAddress.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ipamIpAddressesRead

> IPAddress ipamIpAddressesRead(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let id = 56; // Number | A unique integer value identifying this IP address.
apiInstance.ipamIpAddressesRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this IP address. | 

### Return type

[**IPAddress**](IPAddress.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ipamIpAddressesUpdate

> IPAddress ipamIpAddressesUpdate(id, writableIPAddress)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let id = 56; // Number | A unique integer value identifying this IP address.
let writableIPAddress = new NetBoxApi.WritableIPAddress(); // WritableIPAddress | 
apiInstance.ipamIpAddressesUpdate(id, writableIPAddress, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this IP address. | 
 **writableIPAddress** | [**WritableIPAddress**](WritableIPAddress.md)|  | 

### Return type

[**IPAddress**](IPAddress.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ipamPrefixesAvailableIpsCreate

> Prefix ipamPrefixesAvailableIpsCreate(id, writablePrefix)



A convenience method for returning available IP addresses within a prefix. By default, the number of IPs returned will be equivalent to PAGINATE_COUNT. An arbitrary limit (up to MAX_PAGE_SIZE, if set) may be passed, however results will not be paginated.

### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let id = 56; // Number | A unique integer value identifying this prefix.
let writablePrefix = new NetBoxApi.WritablePrefix(); // WritablePrefix | 
apiInstance.ipamPrefixesAvailableIpsCreate(id, writablePrefix, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this prefix. | 
 **writablePrefix** | [**WritablePrefix**](WritablePrefix.md)|  | 

### Return type

[**Prefix**](Prefix.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ipamPrefixesAvailableIpsRead

> Prefix ipamPrefixesAvailableIpsRead(id)



A convenience method for returning available IP addresses within a prefix. By default, the number of IPs returned will be equivalent to PAGINATE_COUNT. An arbitrary limit (up to MAX_PAGE_SIZE, if set) may be passed, however results will not be paginated.

### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let id = 56; // Number | A unique integer value identifying this prefix.
apiInstance.ipamPrefixesAvailableIpsRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this prefix. | 

### Return type

[**Prefix**](Prefix.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ipamPrefixesAvailablePrefixesCreate

> Prefix ipamPrefixesAvailablePrefixesCreate(id, writablePrefix)



A convenience method for returning available child prefixes within a parent.

### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let id = 56; // Number | A unique integer value identifying this prefix.
let writablePrefix = new NetBoxApi.WritablePrefix(); // WritablePrefix | 
apiInstance.ipamPrefixesAvailablePrefixesCreate(id, writablePrefix, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this prefix. | 
 **writablePrefix** | [**WritablePrefix**](WritablePrefix.md)|  | 

### Return type

[**Prefix**](Prefix.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ipamPrefixesAvailablePrefixesRead

> Prefix ipamPrefixesAvailablePrefixesRead(id)



A convenience method for returning available child prefixes within a parent.

### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let id = 56; // Number | A unique integer value identifying this prefix.
apiInstance.ipamPrefixesAvailablePrefixesRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this prefix. | 

### Return type

[**Prefix**](Prefix.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ipamPrefixesCreate

> Prefix ipamPrefixesCreate(writablePrefix)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let writablePrefix = new NetBoxApi.WritablePrefix(); // WritablePrefix | 
apiInstance.ipamPrefixesCreate(writablePrefix, (error, data, response) => {
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
 **writablePrefix** | [**WritablePrefix**](WritablePrefix.md)|  | 

### Return type

[**Prefix**](Prefix.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ipamPrefixesDelete

> ipamPrefixesDelete(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let id = 56; // Number | A unique integer value identifying this prefix.
apiInstance.ipamPrefixesDelete(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this prefix. | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## ipamPrefixesList

> IpamPrefixesList200Response ipamPrefixesList(opts)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let opts = {
  'family': "family_example", // String | 
  'isPool': "isPool_example", // String | 
  'idIn': "idIn_example", // String | Multiple values may be separated by commas.
  'q': "q_example", // String | 
  'within': "within_example", // String | 
  'withinInclude': "withinInclude_example", // String | 
  'contains': "contains_example", // String | 
  'maskLength': 3.4, // Number | 
  'vrfId': "vrfId_example", // String | 
  'vrf': "vrf_example", // String | 
  'tenantId': "tenantId_example", // String | 
  'tenant': "tenant_example", // String | 
  'siteId': "siteId_example", // String | 
  'site': "site_example", // String | 
  'vlanId': "vlanId_example", // String | 
  'vlanVid': 3.4, // Number | 
  'roleId': "roleId_example", // String | 
  'role': "role_example", // String | 
  'status': "status_example", // String | 
  'tag': "tag_example", // String | 
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.ipamPrefixesList(opts, (error, data, response) => {
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
 **family** | **String**|  | [optional] 
 **isPool** | **String**|  | [optional] 
 **idIn** | **String**| Multiple values may be separated by commas. | [optional] 
 **q** | **String**|  | [optional] 
 **within** | **String**|  | [optional] 
 **withinInclude** | **String**|  | [optional] 
 **contains** | **String**|  | [optional] 
 **maskLength** | **Number**|  | [optional] 
 **vrfId** | **String**|  | [optional] 
 **vrf** | **String**|  | [optional] 
 **tenantId** | **String**|  | [optional] 
 **tenant** | **String**|  | [optional] 
 **siteId** | **String**|  | [optional] 
 **site** | **String**|  | [optional] 
 **vlanId** | **String**|  | [optional] 
 **vlanVid** | **Number**|  | [optional] 
 **roleId** | **String**|  | [optional] 
 **role** | **String**|  | [optional] 
 **status** | **String**|  | [optional] 
 **tag** | **String**|  | [optional] 
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**IpamPrefixesList200Response**](IpamPrefixesList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ipamPrefixesPartialUpdate

> Prefix ipamPrefixesPartialUpdate(id, writablePrefix)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let id = 56; // Number | A unique integer value identifying this prefix.
let writablePrefix = new NetBoxApi.WritablePrefix(); // WritablePrefix | 
apiInstance.ipamPrefixesPartialUpdate(id, writablePrefix, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this prefix. | 
 **writablePrefix** | [**WritablePrefix**](WritablePrefix.md)|  | 

### Return type

[**Prefix**](Prefix.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ipamPrefixesRead

> Prefix ipamPrefixesRead(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let id = 56; // Number | A unique integer value identifying this prefix.
apiInstance.ipamPrefixesRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this prefix. | 

### Return type

[**Prefix**](Prefix.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ipamPrefixesUpdate

> Prefix ipamPrefixesUpdate(id, writablePrefix)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let id = 56; // Number | A unique integer value identifying this prefix.
let writablePrefix = new NetBoxApi.WritablePrefix(); // WritablePrefix | 
apiInstance.ipamPrefixesUpdate(id, writablePrefix, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this prefix. | 
 **writablePrefix** | [**WritablePrefix**](WritablePrefix.md)|  | 

### Return type

[**Prefix**](Prefix.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ipamRirsCreate

> RIR ipamRirsCreate(RIR)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let RIR = new NetBoxApi.RIR(); // RIR | 
apiInstance.ipamRirsCreate(RIR, (error, data, response) => {
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
 **RIR** | [**RIR**](RIR.md)|  | 

### Return type

[**RIR**](RIR.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ipamRirsDelete

> ipamRirsDelete(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let id = 56; // Number | A unique integer value identifying this RIR.
apiInstance.ipamRirsDelete(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this RIR. | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## ipamRirsList

> IpamRirsList200Response ipamRirsList(opts)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let opts = {
  'name': "name_example", // String | 
  'slug': "slug_example", // String | 
  'isPrivate': "isPrivate_example", // String | 
  'idIn': "idIn_example", // String | Multiple values may be separated by commas.
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.ipamRirsList(opts, (error, data, response) => {
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
 **name** | **String**|  | [optional] 
 **slug** | **String**|  | [optional] 
 **isPrivate** | **String**|  | [optional] 
 **idIn** | **String**| Multiple values may be separated by commas. | [optional] 
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**IpamRirsList200Response**](IpamRirsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ipamRirsPartialUpdate

> RIR ipamRirsPartialUpdate(id, RIR)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let id = 56; // Number | A unique integer value identifying this RIR.
let RIR = new NetBoxApi.RIR(); // RIR | 
apiInstance.ipamRirsPartialUpdate(id, RIR, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this RIR. | 
 **RIR** | [**RIR**](RIR.md)|  | 

### Return type

[**RIR**](RIR.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ipamRirsRead

> RIR ipamRirsRead(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let id = 56; // Number | A unique integer value identifying this RIR.
apiInstance.ipamRirsRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this RIR. | 

### Return type

[**RIR**](RIR.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ipamRirsUpdate

> RIR ipamRirsUpdate(id, RIR)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let id = 56; // Number | A unique integer value identifying this RIR.
let RIR = new NetBoxApi.RIR(); // RIR | 
apiInstance.ipamRirsUpdate(id, RIR, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this RIR. | 
 **RIR** | [**RIR**](RIR.md)|  | 

### Return type

[**RIR**](RIR.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ipamRolesCreate

> Role ipamRolesCreate(role)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let role = new NetBoxApi.Role(); // Role | 
apiInstance.ipamRolesCreate(role, (error, data, response) => {
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
 **role** | [**Role**](Role.md)|  | 

### Return type

[**Role**](Role.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ipamRolesDelete

> ipamRolesDelete(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let id = 56; // Number | A unique integer value identifying this role.
apiInstance.ipamRolesDelete(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this role. | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## ipamRolesList

> IpamRolesList200Response ipamRolesList(opts)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let opts = {
  'name': "name_example", // String | 
  'slug': "slug_example", // String | 
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.ipamRolesList(opts, (error, data, response) => {
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
 **name** | **String**|  | [optional] 
 **slug** | **String**|  | [optional] 
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**IpamRolesList200Response**](IpamRolesList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ipamRolesPartialUpdate

> Role ipamRolesPartialUpdate(id, role)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let id = 56; // Number | A unique integer value identifying this role.
let role = new NetBoxApi.Role(); // Role | 
apiInstance.ipamRolesPartialUpdate(id, role, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this role. | 
 **role** | [**Role**](Role.md)|  | 

### Return type

[**Role**](Role.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ipamRolesRead

> Role ipamRolesRead(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let id = 56; // Number | A unique integer value identifying this role.
apiInstance.ipamRolesRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this role. | 

### Return type

[**Role**](Role.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ipamRolesUpdate

> Role ipamRolesUpdate(id, role)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let id = 56; // Number | A unique integer value identifying this role.
let role = new NetBoxApi.Role(); // Role | 
apiInstance.ipamRolesUpdate(id, role, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this role. | 
 **role** | [**Role**](Role.md)|  | 

### Return type

[**Role**](Role.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ipamServicesCreate

> Service ipamServicesCreate(writableService)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let writableService = new NetBoxApi.WritableService(); // WritableService | 
apiInstance.ipamServicesCreate(writableService, (error, data, response) => {
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
 **writableService** | [**WritableService**](WritableService.md)|  | 

### Return type

[**Service**](Service.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ipamServicesDelete

> ipamServicesDelete(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let id = 56; // Number | A unique integer value identifying this service.
apiInstance.ipamServicesDelete(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this service. | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## ipamServicesList

> IpamServicesList200Response ipamServicesList(opts)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let opts = {
  'name': "name_example", // String | 
  'protocol': "protocol_example", // String | 
  'port': 3.4, // Number | 
  'q': "q_example", // String | 
  'deviceId': "deviceId_example", // String | 
  'device': "device_example", // String | 
  'virtualMachineId': "virtualMachineId_example", // String | 
  'virtualMachine': "virtualMachine_example", // String | 
  'tag': "tag_example", // String | 
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.ipamServicesList(opts, (error, data, response) => {
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
 **name** | **String**|  | [optional] 
 **protocol** | **String**|  | [optional] 
 **port** | **Number**|  | [optional] 
 **q** | **String**|  | [optional] 
 **deviceId** | **String**|  | [optional] 
 **device** | **String**|  | [optional] 
 **virtualMachineId** | **String**|  | [optional] 
 **virtualMachine** | **String**|  | [optional] 
 **tag** | **String**|  | [optional] 
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**IpamServicesList200Response**](IpamServicesList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ipamServicesPartialUpdate

> Service ipamServicesPartialUpdate(id, writableService)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let id = 56; // Number | A unique integer value identifying this service.
let writableService = new NetBoxApi.WritableService(); // WritableService | 
apiInstance.ipamServicesPartialUpdate(id, writableService, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this service. | 
 **writableService** | [**WritableService**](WritableService.md)|  | 

### Return type

[**Service**](Service.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ipamServicesRead

> Service ipamServicesRead(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let id = 56; // Number | A unique integer value identifying this service.
apiInstance.ipamServicesRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this service. | 

### Return type

[**Service**](Service.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ipamServicesUpdate

> Service ipamServicesUpdate(id, writableService)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let id = 56; // Number | A unique integer value identifying this service.
let writableService = new NetBoxApi.WritableService(); // WritableService | 
apiInstance.ipamServicesUpdate(id, writableService, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this service. | 
 **writableService** | [**WritableService**](WritableService.md)|  | 

### Return type

[**Service**](Service.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ipamVlanGroupsCreate

> VLANGroup ipamVlanGroupsCreate(writableVLANGroup)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let writableVLANGroup = new NetBoxApi.WritableVLANGroup(); // WritableVLANGroup | 
apiInstance.ipamVlanGroupsCreate(writableVLANGroup, (error, data, response) => {
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
 **writableVLANGroup** | [**WritableVLANGroup**](WritableVLANGroup.md)|  | 

### Return type

[**VLANGroup**](VLANGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ipamVlanGroupsDelete

> ipamVlanGroupsDelete(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let id = 56; // Number | A unique integer value identifying this VLAN group.
apiInstance.ipamVlanGroupsDelete(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this VLAN group. | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## ipamVlanGroupsList

> IpamVlanGroupsList200Response ipamVlanGroupsList(opts)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let opts = {
  'name': "name_example", // String | 
  'slug': "slug_example", // String | 
  'siteId': "siteId_example", // String | 
  'site': "site_example", // String | 
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.ipamVlanGroupsList(opts, (error, data, response) => {
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
 **name** | **String**|  | [optional] 
 **slug** | **String**|  | [optional] 
 **siteId** | **String**|  | [optional] 
 **site** | **String**|  | [optional] 
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**IpamVlanGroupsList200Response**](IpamVlanGroupsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ipamVlanGroupsPartialUpdate

> VLANGroup ipamVlanGroupsPartialUpdate(id, writableVLANGroup)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let id = 56; // Number | A unique integer value identifying this VLAN group.
let writableVLANGroup = new NetBoxApi.WritableVLANGroup(); // WritableVLANGroup | 
apiInstance.ipamVlanGroupsPartialUpdate(id, writableVLANGroup, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this VLAN group. | 
 **writableVLANGroup** | [**WritableVLANGroup**](WritableVLANGroup.md)|  | 

### Return type

[**VLANGroup**](VLANGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ipamVlanGroupsRead

> VLANGroup ipamVlanGroupsRead(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let id = 56; // Number | A unique integer value identifying this VLAN group.
apiInstance.ipamVlanGroupsRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this VLAN group. | 

### Return type

[**VLANGroup**](VLANGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ipamVlanGroupsUpdate

> VLANGroup ipamVlanGroupsUpdate(id, writableVLANGroup)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let id = 56; // Number | A unique integer value identifying this VLAN group.
let writableVLANGroup = new NetBoxApi.WritableVLANGroup(); // WritableVLANGroup | 
apiInstance.ipamVlanGroupsUpdate(id, writableVLANGroup, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this VLAN group. | 
 **writableVLANGroup** | [**WritableVLANGroup**](WritableVLANGroup.md)|  | 

### Return type

[**VLANGroup**](VLANGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ipamVlansCreate

> VLAN ipamVlansCreate(writableVLAN)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let writableVLAN = new NetBoxApi.WritableVLAN(); // WritableVLAN | 
apiInstance.ipamVlansCreate(writableVLAN, (error, data, response) => {
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
 **writableVLAN** | [**WritableVLAN**](WritableVLAN.md)|  | 

### Return type

[**VLAN**](VLAN.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ipamVlansDelete

> ipamVlansDelete(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let id = 56; // Number | A unique integer value identifying this VLAN.
apiInstance.ipamVlansDelete(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this VLAN. | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## ipamVlansList

> IpamVlansList200Response ipamVlansList(opts)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let opts = {
  'vid': 3.4, // Number | 
  'name': "name_example", // String | 
  'idIn': "idIn_example", // String | Multiple values may be separated by commas.
  'q': "q_example", // String | 
  'siteId': "siteId_example", // String | 
  'site': "site_example", // String | 
  'groupId': "groupId_example", // String | 
  'group': "group_example", // String | 
  'tenantId': "tenantId_example", // String | 
  'tenant': "tenant_example", // String | 
  'roleId': "roleId_example", // String | 
  'role': "role_example", // String | 
  'status': "status_example", // String | 
  'tag': "tag_example", // String | 
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.ipamVlansList(opts, (error, data, response) => {
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
 **vid** | **Number**|  | [optional] 
 **name** | **String**|  | [optional] 
 **idIn** | **String**| Multiple values may be separated by commas. | [optional] 
 **q** | **String**|  | [optional] 
 **siteId** | **String**|  | [optional] 
 **site** | **String**|  | [optional] 
 **groupId** | **String**|  | [optional] 
 **group** | **String**|  | [optional] 
 **tenantId** | **String**|  | [optional] 
 **tenant** | **String**|  | [optional] 
 **roleId** | **String**|  | [optional] 
 **role** | **String**|  | [optional] 
 **status** | **String**|  | [optional] 
 **tag** | **String**|  | [optional] 
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**IpamVlansList200Response**](IpamVlansList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ipamVlansPartialUpdate

> VLAN ipamVlansPartialUpdate(id, writableVLAN)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let id = 56; // Number | A unique integer value identifying this VLAN.
let writableVLAN = new NetBoxApi.WritableVLAN(); // WritableVLAN | 
apiInstance.ipamVlansPartialUpdate(id, writableVLAN, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this VLAN. | 
 **writableVLAN** | [**WritableVLAN**](WritableVLAN.md)|  | 

### Return type

[**VLAN**](VLAN.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ipamVlansRead

> VLAN ipamVlansRead(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let id = 56; // Number | A unique integer value identifying this VLAN.
apiInstance.ipamVlansRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this VLAN. | 

### Return type

[**VLAN**](VLAN.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ipamVlansUpdate

> VLAN ipamVlansUpdate(id, writableVLAN)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let id = 56; // Number | A unique integer value identifying this VLAN.
let writableVLAN = new NetBoxApi.WritableVLAN(); // WritableVLAN | 
apiInstance.ipamVlansUpdate(id, writableVLAN, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this VLAN. | 
 **writableVLAN** | [**WritableVLAN**](WritableVLAN.md)|  | 

### Return type

[**VLAN**](VLAN.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ipamVrfsCreate

> VRF ipamVrfsCreate(writableVRF)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let writableVRF = new NetBoxApi.WritableVRF(); // WritableVRF | 
apiInstance.ipamVrfsCreate(writableVRF, (error, data, response) => {
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
 **writableVRF** | [**WritableVRF**](WritableVRF.md)|  | 

### Return type

[**VRF**](VRF.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ipamVrfsDelete

> ipamVrfsDelete(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let id = 56; // Number | A unique integer value identifying this VRF.
apiInstance.ipamVrfsDelete(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this VRF. | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## ipamVrfsList

> IpamVrfsList200Response ipamVrfsList(opts)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let opts = {
  'name': "name_example", // String | 
  'rd': "rd_example", // String | 
  'enforceUnique': "enforceUnique_example", // String | 
  'idIn': "idIn_example", // String | Multiple values may be separated by commas.
  'q': "q_example", // String | 
  'tenantId': "tenantId_example", // String | 
  'tenant': "tenant_example", // String | 
  'tag': "tag_example", // String | 
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.ipamVrfsList(opts, (error, data, response) => {
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
 **name** | **String**|  | [optional] 
 **rd** | **String**|  | [optional] 
 **enforceUnique** | **String**|  | [optional] 
 **idIn** | **String**| Multiple values may be separated by commas. | [optional] 
 **q** | **String**|  | [optional] 
 **tenantId** | **String**|  | [optional] 
 **tenant** | **String**|  | [optional] 
 **tag** | **String**|  | [optional] 
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**IpamVrfsList200Response**](IpamVrfsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ipamVrfsPartialUpdate

> VRF ipamVrfsPartialUpdate(id, writableVRF)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let id = 56; // Number | A unique integer value identifying this VRF.
let writableVRF = new NetBoxApi.WritableVRF(); // WritableVRF | 
apiInstance.ipamVrfsPartialUpdate(id, writableVRF, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this VRF. | 
 **writableVRF** | [**WritableVRF**](WritableVRF.md)|  | 

### Return type

[**VRF**](VRF.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ipamVrfsRead

> VRF ipamVrfsRead(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let id = 56; // Number | A unique integer value identifying this VRF.
apiInstance.ipamVrfsRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this VRF. | 

### Return type

[**VRF**](VRF.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ipamVrfsUpdate

> VRF ipamVrfsUpdate(id, writableVRF)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.IpamApi();
let id = 56; // Number | A unique integer value identifying this VRF.
let writableVRF = new NetBoxApi.WritableVRF(); // WritableVRF | 
apiInstance.ipamVrfsUpdate(id, writableVRF, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this VRF. | 
 **writableVRF** | [**WritableVRF**](WritableVRF.md)|  | 

### Return type

[**VRF**](VRF.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

