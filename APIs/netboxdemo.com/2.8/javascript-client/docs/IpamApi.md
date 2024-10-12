# NetBoxApi.IpamApi

All URIs are relative to *https://netboxdemo.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ipamAggregatesCreate**](IpamApi.md#ipamAggregatesCreate) | **POST** /ipam/aggregates/ | 
[**ipamAggregatesDelete**](IpamApi.md#ipamAggregatesDelete) | **DELETE** /ipam/aggregates/{id}/ | 
[**ipamAggregatesList**](IpamApi.md#ipamAggregatesList) | **GET** /ipam/aggregates/ | 
[**ipamAggregatesPartialUpdate**](IpamApi.md#ipamAggregatesPartialUpdate) | **PATCH** /ipam/aggregates/{id}/ | 
[**ipamAggregatesRead**](IpamApi.md#ipamAggregatesRead) | **GET** /ipam/aggregates/{id}/ | 
[**ipamAggregatesUpdate**](IpamApi.md#ipamAggregatesUpdate) | **PUT** /ipam/aggregates/{id}/ | 
[**ipamIpAddressesCreate**](IpamApi.md#ipamIpAddressesCreate) | **POST** /ipam/ip-addresses/ | 
[**ipamIpAddressesDelete**](IpamApi.md#ipamIpAddressesDelete) | **DELETE** /ipam/ip-addresses/{id}/ | 
[**ipamIpAddressesList**](IpamApi.md#ipamIpAddressesList) | **GET** /ipam/ip-addresses/ | 
[**ipamIpAddressesPartialUpdate**](IpamApi.md#ipamIpAddressesPartialUpdate) | **PATCH** /ipam/ip-addresses/{id}/ | 
[**ipamIpAddressesRead**](IpamApi.md#ipamIpAddressesRead) | **GET** /ipam/ip-addresses/{id}/ | 
[**ipamIpAddressesUpdate**](IpamApi.md#ipamIpAddressesUpdate) | **PUT** /ipam/ip-addresses/{id}/ | 
[**ipamPrefixesAvailableIpsCreate**](IpamApi.md#ipamPrefixesAvailableIpsCreate) | **POST** /ipam/prefixes/{id}/available-ips/ | 
[**ipamPrefixesAvailableIpsRead**](IpamApi.md#ipamPrefixesAvailableIpsRead) | **GET** /ipam/prefixes/{id}/available-ips/ | 
[**ipamPrefixesAvailablePrefixesCreate**](IpamApi.md#ipamPrefixesAvailablePrefixesCreate) | **POST** /ipam/prefixes/{id}/available-prefixes/ | A convenience method for returning available child prefixes within a parent.
[**ipamPrefixesAvailablePrefixesRead**](IpamApi.md#ipamPrefixesAvailablePrefixesRead) | **GET** /ipam/prefixes/{id}/available-prefixes/ | A convenience method for returning available child prefixes within a parent.
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



Call to super to allow for caching

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
  'id': "id_example", // String | 
  'dateAdded': "dateAdded_example", // String | 
  'created': "created_example", // String | 
  'createdGte': "createdGte_example", // String | 
  'createdLte': "createdLte_example", // String | 
  'lastUpdated': "lastUpdated_example", // String | 
  'lastUpdatedGte': "lastUpdatedGte_example", // String | 
  'lastUpdatedLte': "lastUpdatedLte_example", // String | 
  'q': "q_example", // String | 
  'family': 3.4, // Number | 
  'prefix': "prefix_example", // String | 
  'rirId': "rirId_example", // String | 
  'rir': "rir_example", // String | 
  'tag': "tag_example", // String | 
  'idN': "idN_example", // String | 
  'idLte': "idLte_example", // String | 
  'idLt': "idLt_example", // String | 
  'idGte': "idGte_example", // String | 
  'idGt': "idGt_example", // String | 
  'dateAddedN': "dateAddedN_example", // String | 
  'dateAddedLte': "dateAddedLte_example", // String | 
  'dateAddedLt': "dateAddedLt_example", // String | 
  'dateAddedGte': "dateAddedGte_example", // String | 
  'dateAddedGt': "dateAddedGt_example", // String | 
  'rirIdN': "rirIdN_example", // String | 
  'rirN': "rirN_example", // String | 
  'tagN': "tagN_example", // String | 
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
 **id** | **String**|  | [optional] 
 **dateAdded** | **String**|  | [optional] 
 **created** | **String**|  | [optional] 
 **createdGte** | **String**|  | [optional] 
 **createdLte** | **String**|  | [optional] 
 **lastUpdated** | **String**|  | [optional] 
 **lastUpdatedGte** | **String**|  | [optional] 
 **lastUpdatedLte** | **String**|  | [optional] 
 **q** | **String**|  | [optional] 
 **family** | **Number**|  | [optional] 
 **prefix** | **String**|  | [optional] 
 **rirId** | **String**|  | [optional] 
 **rir** | **String**|  | [optional] 
 **tag** | **String**|  | [optional] 
 **idN** | **String**|  | [optional] 
 **idLte** | **String**|  | [optional] 
 **idLt** | **String**|  | [optional] 
 **idGte** | **String**|  | [optional] 
 **idGt** | **String**|  | [optional] 
 **dateAddedN** | **String**|  | [optional] 
 **dateAddedLte** | **String**|  | [optional] 
 **dateAddedLt** | **String**|  | [optional] 
 **dateAddedGte** | **String**|  | [optional] 
 **dateAddedGt** | **String**|  | [optional] 
 **rirIdN** | **String**|  | [optional] 
 **rirN** | **String**|  | [optional] 
 **tagN** | **String**|  | [optional] 
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



Call to super to allow for caching

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



Call to super to allow for caching

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
  'id': "id_example", // String | 
  'dnsName': "dnsName_example", // String | 
  'tenantGroupId': "tenantGroupId_example", // String | 
  'tenantGroup': "tenantGroup_example", // String | 
  'tenantId': "tenantId_example", // String | 
  'tenant': "tenant_example", // String | 
  'created': "created_example", // String | 
  'createdGte': "createdGte_example", // String | 
  'createdLte': "createdLte_example", // String | 
  'lastUpdated': "lastUpdated_example", // String | 
  'lastUpdatedGte': "lastUpdatedGte_example", // String | 
  'lastUpdatedLte': "lastUpdatedLte_example", // String | 
  'q': "q_example", // String | 
  'family': 3.4, // Number | 
  'parent': "parent_example", // String | 
  'address': "address_example", // String | 
  'maskLength': 3.4, // Number | 
  'vrfId': "vrfId_example", // String | 
  'vrf': "vrf_example", // String | 
  'device': "device_example", // String | 
  'deviceId': "deviceId_example", // String | 
  'virtualMachineId': "virtualMachineId_example", // String | 
  'virtualMachine': "virtualMachine_example", // String | 
  '_interface': "_interface_example", // String | 
  'interfaceId': "interfaceId_example", // String | 
  'assignedToInterface': "assignedToInterface_example", // String | 
  'status': "status_example", // String | 
  'role': "role_example", // String | 
  'tag': "tag_example", // String | 
  'idN': "idN_example", // String | 
  'idLte': "idLte_example", // String | 
  'idLt': "idLt_example", // String | 
  'idGte': "idGte_example", // String | 
  'idGt': "idGt_example", // String | 
  'dnsNameN': "dnsNameN_example", // String | 
  'dnsNameIc': "dnsNameIc_example", // String | 
  'dnsNameNic': "dnsNameNic_example", // String | 
  'dnsNameIew': "dnsNameIew_example", // String | 
  'dnsNameNiew': "dnsNameNiew_example", // String | 
  'dnsNameIsw': "dnsNameIsw_example", // String | 
  'dnsNameNisw': "dnsNameNisw_example", // String | 
  'dnsNameIe': "dnsNameIe_example", // String | 
  'dnsNameNie': "dnsNameNie_example", // String | 
  'tenantGroupIdN': "tenantGroupIdN_example", // String | 
  'tenantGroupN': "tenantGroupN_example", // String | 
  'tenantIdN': "tenantIdN_example", // String | 
  'tenantN': "tenantN_example", // String | 
  'vrfIdN': "vrfIdN_example", // String | 
  'vrfN': "vrfN_example", // String | 
  'virtualMachineIdN': "virtualMachineIdN_example", // String | 
  'virtualMachineN': "virtualMachineN_example", // String | 
  'interfaceN': "interfaceN_example", // String | 
  'interfaceIdN': "interfaceIdN_example", // String | 
  'statusN': "statusN_example", // String | 
  'roleN': "roleN_example", // String | 
  'tagN': "tagN_example", // String | 
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
 **id** | **String**|  | [optional] 
 **dnsName** | **String**|  | [optional] 
 **tenantGroupId** | **String**|  | [optional] 
 **tenantGroup** | **String**|  | [optional] 
 **tenantId** | **String**|  | [optional] 
 **tenant** | **String**|  | [optional] 
 **created** | **String**|  | [optional] 
 **createdGte** | **String**|  | [optional] 
 **createdLte** | **String**|  | [optional] 
 **lastUpdated** | **String**|  | [optional] 
 **lastUpdatedGte** | **String**|  | [optional] 
 **lastUpdatedLte** | **String**|  | [optional] 
 **q** | **String**|  | [optional] 
 **family** | **Number**|  | [optional] 
 **parent** | **String**|  | [optional] 
 **address** | **String**|  | [optional] 
 **maskLength** | **Number**|  | [optional] 
 **vrfId** | **String**|  | [optional] 
 **vrf** | **String**|  | [optional] 
 **device** | **String**|  | [optional] 
 **deviceId** | **String**|  | [optional] 
 **virtualMachineId** | **String**|  | [optional] 
 **virtualMachine** | **String**|  | [optional] 
 **_interface** | **String**|  | [optional] 
 **interfaceId** | **String**|  | [optional] 
 **assignedToInterface** | **String**|  | [optional] 
 **status** | **String**|  | [optional] 
 **role** | **String**|  | [optional] 
 **tag** | **String**|  | [optional] 
 **idN** | **String**|  | [optional] 
 **idLte** | **String**|  | [optional] 
 **idLt** | **String**|  | [optional] 
 **idGte** | **String**|  | [optional] 
 **idGt** | **String**|  | [optional] 
 **dnsNameN** | **String**|  | [optional] 
 **dnsNameIc** | **String**|  | [optional] 
 **dnsNameNic** | **String**|  | [optional] 
 **dnsNameIew** | **String**|  | [optional] 
 **dnsNameNiew** | **String**|  | [optional] 
 **dnsNameIsw** | **String**|  | [optional] 
 **dnsNameNisw** | **String**|  | [optional] 
 **dnsNameIe** | **String**|  | [optional] 
 **dnsNameNie** | **String**|  | [optional] 
 **tenantGroupIdN** | **String**|  | [optional] 
 **tenantGroupN** | **String**|  | [optional] 
 **tenantIdN** | **String**|  | [optional] 
 **tenantN** | **String**|  | [optional] 
 **vrfIdN** | **String**|  | [optional] 
 **vrfN** | **String**|  | [optional] 
 **virtualMachineIdN** | **String**|  | [optional] 
 **virtualMachineN** | **String**|  | [optional] 
 **interfaceN** | **String**|  | [optional] 
 **interfaceIdN** | **String**|  | [optional] 
 **statusN** | **String**|  | [optional] 
 **roleN** | **String**|  | [optional] 
 **tagN** | **String**|  | [optional] 
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



Call to super to allow for caching

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

> [AvailableIP] ipamPrefixesAvailableIpsCreate(id, writableAvailableIP)



A convenience method for returning available IP addresses within a prefix. By default, the number of IPs returned will be equivalent to PAGINATE_COUNT. An arbitrary limit (up to MAX_PAGE_SIZE, if set) may be passed, however results will not be paginated.  The advisory lock decorator uses a PostgreSQL advisory lock to prevent this API from being invoked in parallel, which results in a race condition where multiple insertions can occur.

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
let writableAvailableIP = new NetBoxApi.WritableAvailableIP(); // WritableAvailableIP | 
apiInstance.ipamPrefixesAvailableIpsCreate(id, writableAvailableIP, (error, data, response) => {
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
 **writableAvailableIP** | [**WritableAvailableIP**](WritableAvailableIP.md)|  | 

### Return type

[**[AvailableIP]**](AvailableIP.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ipamPrefixesAvailableIpsRead

> [AvailableIP] ipamPrefixesAvailableIpsRead(id)



A convenience method for returning available IP addresses within a prefix. By default, the number of IPs returned will be equivalent to PAGINATE_COUNT. An arbitrary limit (up to MAX_PAGE_SIZE, if set) may be passed, however results will not be paginated.  The advisory lock decorator uses a PostgreSQL advisory lock to prevent this API from being invoked in parallel, which results in a race condition where multiple insertions can occur.

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

[**[AvailableIP]**](AvailableIP.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ipamPrefixesAvailablePrefixesCreate

> [AvailablePrefix] ipamPrefixesAvailablePrefixesCreate(id, writablePrefix)

A convenience method for returning available child prefixes within a parent.

The advisory lock decorator uses a PostgreSQL advisory lock to prevent this API from being invoked in parallel, which results in a race condition where multiple insertions can occur.

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

[**[AvailablePrefix]**](AvailablePrefix.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ipamPrefixesAvailablePrefixesRead

> [AvailablePrefix] ipamPrefixesAvailablePrefixesRead(id)

A convenience method for returning available child prefixes within a parent.

The advisory lock decorator uses a PostgreSQL advisory lock to prevent this API from being invoked in parallel, which results in a race condition where multiple insertions can occur.

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

[**[AvailablePrefix]**](AvailablePrefix.md)

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



Call to super to allow for caching

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
  'id': "id_example", // String | 
  'isPool': "isPool_example", // String | 
  'tenantGroupId': "tenantGroupId_example", // String | 
  'tenantGroup': "tenantGroup_example", // String | 
  'tenantId': "tenantId_example", // String | 
  'tenant': "tenant_example", // String | 
  'created': "created_example", // String | 
  'createdGte': "createdGte_example", // String | 
  'createdLte': "createdLte_example", // String | 
  'lastUpdated': "lastUpdated_example", // String | 
  'lastUpdatedGte': "lastUpdatedGte_example", // String | 
  'lastUpdatedLte': "lastUpdatedLte_example", // String | 
  'q': "q_example", // String | 
  'family': 3.4, // Number | 
  'prefix': "prefix_example", // String | 
  'within': "within_example", // String | 
  'withinInclude': "withinInclude_example", // String | 
  'contains': "contains_example", // String | 
  'maskLength': 3.4, // Number | 
  'vrfId': "vrfId_example", // String | 
  'vrf': "vrf_example", // String | 
  'regionId': "regionId_example", // String | 
  'region': "region_example", // String | 
  'siteId': "siteId_example", // String | 
  'site': "site_example", // String | 
  'vlanId': "vlanId_example", // String | 
  'vlanVid': 3.4, // Number | 
  'roleId': "roleId_example", // String | 
  'role': "role_example", // String | 
  'status': "status_example", // String | 
  'tag': "tag_example", // String | 
  'idN': "idN_example", // String | 
  'idLte': "idLte_example", // String | 
  'idLt': "idLt_example", // String | 
  'idGte': "idGte_example", // String | 
  'idGt': "idGt_example", // String | 
  'tenantGroupIdN': "tenantGroupIdN_example", // String | 
  'tenantGroupN': "tenantGroupN_example", // String | 
  'tenantIdN': "tenantIdN_example", // String | 
  'tenantN': "tenantN_example", // String | 
  'vrfIdN': "vrfIdN_example", // String | 
  'vrfN': "vrfN_example", // String | 
  'regionIdN': "regionIdN_example", // String | 
  'regionN': "regionN_example", // String | 
  'siteIdN': "siteIdN_example", // String | 
  'siteN': "siteN_example", // String | 
  'vlanIdN': "vlanIdN_example", // String | 
  'roleIdN': "roleIdN_example", // String | 
  'roleN': "roleN_example", // String | 
  'statusN': "statusN_example", // String | 
  'tagN': "tagN_example", // String | 
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
 **id** | **String**|  | [optional] 
 **isPool** | **String**|  | [optional] 
 **tenantGroupId** | **String**|  | [optional] 
 **tenantGroup** | **String**|  | [optional] 
 **tenantId** | **String**|  | [optional] 
 **tenant** | **String**|  | [optional] 
 **created** | **String**|  | [optional] 
 **createdGte** | **String**|  | [optional] 
 **createdLte** | **String**|  | [optional] 
 **lastUpdated** | **String**|  | [optional] 
 **lastUpdatedGte** | **String**|  | [optional] 
 **lastUpdatedLte** | **String**|  | [optional] 
 **q** | **String**|  | [optional] 
 **family** | **Number**|  | [optional] 
 **prefix** | **String**|  | [optional] 
 **within** | **String**|  | [optional] 
 **withinInclude** | **String**|  | [optional] 
 **contains** | **String**|  | [optional] 
 **maskLength** | **Number**|  | [optional] 
 **vrfId** | **String**|  | [optional] 
 **vrf** | **String**|  | [optional] 
 **regionId** | **String**|  | [optional] 
 **region** | **String**|  | [optional] 
 **siteId** | **String**|  | [optional] 
 **site** | **String**|  | [optional] 
 **vlanId** | **String**|  | [optional] 
 **vlanVid** | **Number**|  | [optional] 
 **roleId** | **String**|  | [optional] 
 **role** | **String**|  | [optional] 
 **status** | **String**|  | [optional] 
 **tag** | **String**|  | [optional] 
 **idN** | **String**|  | [optional] 
 **idLte** | **String**|  | [optional] 
 **idLt** | **String**|  | [optional] 
 **idGte** | **String**|  | [optional] 
 **idGt** | **String**|  | [optional] 
 **tenantGroupIdN** | **String**|  | [optional] 
 **tenantGroupN** | **String**|  | [optional] 
 **tenantIdN** | **String**|  | [optional] 
 **tenantN** | **String**|  | [optional] 
 **vrfIdN** | **String**|  | [optional] 
 **vrfN** | **String**|  | [optional] 
 **regionIdN** | **String**|  | [optional] 
 **regionN** | **String**|  | [optional] 
 **siteIdN** | **String**|  | [optional] 
 **siteN** | **String**|  | [optional] 
 **vlanIdN** | **String**|  | [optional] 
 **roleIdN** | **String**|  | [optional] 
 **roleN** | **String**|  | [optional] 
 **statusN** | **String**|  | [optional] 
 **tagN** | **String**|  | [optional] 
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



Call to super to allow for caching

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



Call to super to allow for caching

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
  'id': "id_example", // String | 
  'name': "name_example", // String | 
  'slug': "slug_example", // String | 
  'isPrivate': "isPrivate_example", // String | 
  'description': "description_example", // String | 
  'q': "q_example", // String | 
  'idN': "idN_example", // String | 
  'idLte': "idLte_example", // String | 
  'idLt': "idLt_example", // String | 
  'idGte': "idGte_example", // String | 
  'idGt': "idGt_example", // String | 
  'nameN': "nameN_example", // String | 
  'nameIc': "nameIc_example", // String | 
  'nameNic': "nameNic_example", // String | 
  'nameIew': "nameIew_example", // String | 
  'nameNiew': "nameNiew_example", // String | 
  'nameIsw': "nameIsw_example", // String | 
  'nameNisw': "nameNisw_example", // String | 
  'nameIe': "nameIe_example", // String | 
  'nameNie': "nameNie_example", // String | 
  'slugN': "slugN_example", // String | 
  'slugIc': "slugIc_example", // String | 
  'slugNic': "slugNic_example", // String | 
  'slugIew': "slugIew_example", // String | 
  'slugNiew': "slugNiew_example", // String | 
  'slugIsw': "slugIsw_example", // String | 
  'slugNisw': "slugNisw_example", // String | 
  'slugIe': "slugIe_example", // String | 
  'slugNie': "slugNie_example", // String | 
  'descriptionN': "descriptionN_example", // String | 
  'descriptionIc': "descriptionIc_example", // String | 
  'descriptionNic': "descriptionNic_example", // String | 
  'descriptionIew': "descriptionIew_example", // String | 
  'descriptionNiew': "descriptionNiew_example", // String | 
  'descriptionIsw': "descriptionIsw_example", // String | 
  'descriptionNisw': "descriptionNisw_example", // String | 
  'descriptionIe': "descriptionIe_example", // String | 
  'descriptionNie': "descriptionNie_example", // String | 
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
 **id** | **String**|  | [optional] 
 **name** | **String**|  | [optional] 
 **slug** | **String**|  | [optional] 
 **isPrivate** | **String**|  | [optional] 
 **description** | **String**|  | [optional] 
 **q** | **String**|  | [optional] 
 **idN** | **String**|  | [optional] 
 **idLte** | **String**|  | [optional] 
 **idLt** | **String**|  | [optional] 
 **idGte** | **String**|  | [optional] 
 **idGt** | **String**|  | [optional] 
 **nameN** | **String**|  | [optional] 
 **nameIc** | **String**|  | [optional] 
 **nameNic** | **String**|  | [optional] 
 **nameIew** | **String**|  | [optional] 
 **nameNiew** | **String**|  | [optional] 
 **nameIsw** | **String**|  | [optional] 
 **nameNisw** | **String**|  | [optional] 
 **nameIe** | **String**|  | [optional] 
 **nameNie** | **String**|  | [optional] 
 **slugN** | **String**|  | [optional] 
 **slugIc** | **String**|  | [optional] 
 **slugNic** | **String**|  | [optional] 
 **slugIew** | **String**|  | [optional] 
 **slugNiew** | **String**|  | [optional] 
 **slugIsw** | **String**|  | [optional] 
 **slugNisw** | **String**|  | [optional] 
 **slugIe** | **String**|  | [optional] 
 **slugNie** | **String**|  | [optional] 
 **descriptionN** | **String**|  | [optional] 
 **descriptionIc** | **String**|  | [optional] 
 **descriptionNic** | **String**|  | [optional] 
 **descriptionIew** | **String**|  | [optional] 
 **descriptionNiew** | **String**|  | [optional] 
 **descriptionIsw** | **String**|  | [optional] 
 **descriptionNisw** | **String**|  | [optional] 
 **descriptionIe** | **String**|  | [optional] 
 **descriptionNie** | **String**|  | [optional] 
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



Call to super to allow for caching

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



Call to super to allow for caching

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
  'id': "id_example", // String | 
  'name': "name_example", // String | 
  'slug': "slug_example", // String | 
  'q': "q_example", // String | 
  'idN': "idN_example", // String | 
  'idLte': "idLte_example", // String | 
  'idLt': "idLt_example", // String | 
  'idGte': "idGte_example", // String | 
  'idGt': "idGt_example", // String | 
  'nameN': "nameN_example", // String | 
  'nameIc': "nameIc_example", // String | 
  'nameNic': "nameNic_example", // String | 
  'nameIew': "nameIew_example", // String | 
  'nameNiew': "nameNiew_example", // String | 
  'nameIsw': "nameIsw_example", // String | 
  'nameNisw': "nameNisw_example", // String | 
  'nameIe': "nameIe_example", // String | 
  'nameNie': "nameNie_example", // String | 
  'slugN': "slugN_example", // String | 
  'slugIc': "slugIc_example", // String | 
  'slugNic': "slugNic_example", // String | 
  'slugIew': "slugIew_example", // String | 
  'slugNiew': "slugNiew_example", // String | 
  'slugIsw': "slugIsw_example", // String | 
  'slugNisw': "slugNisw_example", // String | 
  'slugIe': "slugIe_example", // String | 
  'slugNie': "slugNie_example", // String | 
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
 **id** | **String**|  | [optional] 
 **name** | **String**|  | [optional] 
 **slug** | **String**|  | [optional] 
 **q** | **String**|  | [optional] 
 **idN** | **String**|  | [optional] 
 **idLte** | **String**|  | [optional] 
 **idLt** | **String**|  | [optional] 
 **idGte** | **String**|  | [optional] 
 **idGt** | **String**|  | [optional] 
 **nameN** | **String**|  | [optional] 
 **nameIc** | **String**|  | [optional] 
 **nameNic** | **String**|  | [optional] 
 **nameIew** | **String**|  | [optional] 
 **nameNiew** | **String**|  | [optional] 
 **nameIsw** | **String**|  | [optional] 
 **nameNisw** | **String**|  | [optional] 
 **nameIe** | **String**|  | [optional] 
 **nameNie** | **String**|  | [optional] 
 **slugN** | **String**|  | [optional] 
 **slugIc** | **String**|  | [optional] 
 **slugNic** | **String**|  | [optional] 
 **slugIew** | **String**|  | [optional] 
 **slugNiew** | **String**|  | [optional] 
 **slugIsw** | **String**|  | [optional] 
 **slugNisw** | **String**|  | [optional] 
 **slugIe** | **String**|  | [optional] 
 **slugNie** | **String**|  | [optional] 
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



Call to super to allow for caching

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



Call to super to allow for caching

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
  'id': "id_example", // String | 
  'name': "name_example", // String | 
  'protocol': "protocol_example", // String | 
  'port': "port_example", // String | 
  'created': "created_example", // String | 
  'createdGte': "createdGte_example", // String | 
  'createdLte': "createdLte_example", // String | 
  'lastUpdated': "lastUpdated_example", // String | 
  'lastUpdatedGte': "lastUpdatedGte_example", // String | 
  'lastUpdatedLte': "lastUpdatedLte_example", // String | 
  'q': "q_example", // String | 
  'deviceId': "deviceId_example", // String | 
  'device': "device_example", // String | 
  'virtualMachineId': "virtualMachineId_example", // String | 
  'virtualMachine': "virtualMachine_example", // String | 
  'tag': "tag_example", // String | 
  'idN': "idN_example", // String | 
  'idLte': "idLte_example", // String | 
  'idLt': "idLt_example", // String | 
  'idGte': "idGte_example", // String | 
  'idGt': "idGt_example", // String | 
  'nameN': "nameN_example", // String | 
  'nameIc': "nameIc_example", // String | 
  'nameNic': "nameNic_example", // String | 
  'nameIew': "nameIew_example", // String | 
  'nameNiew': "nameNiew_example", // String | 
  'nameIsw': "nameIsw_example", // String | 
  'nameNisw': "nameNisw_example", // String | 
  'nameIe': "nameIe_example", // String | 
  'nameNie': "nameNie_example", // String | 
  'protocolN': "protocolN_example", // String | 
  'portN': "portN_example", // String | 
  'portLte': "portLte_example", // String | 
  'portLt': "portLt_example", // String | 
  'portGte': "portGte_example", // String | 
  'portGt': "portGt_example", // String | 
  'deviceIdN': "deviceIdN_example", // String | 
  'deviceN': "deviceN_example", // String | 
  'virtualMachineIdN': "virtualMachineIdN_example", // String | 
  'virtualMachineN': "virtualMachineN_example", // String | 
  'tagN': "tagN_example", // String | 
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
 **id** | **String**|  | [optional] 
 **name** | **String**|  | [optional] 
 **protocol** | **String**|  | [optional] 
 **port** | **String**|  | [optional] 
 **created** | **String**|  | [optional] 
 **createdGte** | **String**|  | [optional] 
 **createdLte** | **String**|  | [optional] 
 **lastUpdated** | **String**|  | [optional] 
 **lastUpdatedGte** | **String**|  | [optional] 
 **lastUpdatedLte** | **String**|  | [optional] 
 **q** | **String**|  | [optional] 
 **deviceId** | **String**|  | [optional] 
 **device** | **String**|  | [optional] 
 **virtualMachineId** | **String**|  | [optional] 
 **virtualMachine** | **String**|  | [optional] 
 **tag** | **String**|  | [optional] 
 **idN** | **String**|  | [optional] 
 **idLte** | **String**|  | [optional] 
 **idLt** | **String**|  | [optional] 
 **idGte** | **String**|  | [optional] 
 **idGt** | **String**|  | [optional] 
 **nameN** | **String**|  | [optional] 
 **nameIc** | **String**|  | [optional] 
 **nameNic** | **String**|  | [optional] 
 **nameIew** | **String**|  | [optional] 
 **nameNiew** | **String**|  | [optional] 
 **nameIsw** | **String**|  | [optional] 
 **nameNisw** | **String**|  | [optional] 
 **nameIe** | **String**|  | [optional] 
 **nameNie** | **String**|  | [optional] 
 **protocolN** | **String**|  | [optional] 
 **portN** | **String**|  | [optional] 
 **portLte** | **String**|  | [optional] 
 **portLt** | **String**|  | [optional] 
 **portGte** | **String**|  | [optional] 
 **portGt** | **String**|  | [optional] 
 **deviceIdN** | **String**|  | [optional] 
 **deviceN** | **String**|  | [optional] 
 **virtualMachineIdN** | **String**|  | [optional] 
 **virtualMachineN** | **String**|  | [optional] 
 **tagN** | **String**|  | [optional] 
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



Call to super to allow for caching

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



Call to super to allow for caching

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
  'id': "id_example", // String | 
  'name': "name_example", // String | 
  'slug': "slug_example", // String | 
  'description': "description_example", // String | 
  'q': "q_example", // String | 
  'regionId': "regionId_example", // String | 
  'region': "region_example", // String | 
  'siteId': "siteId_example", // String | 
  'site': "site_example", // String | 
  'idN': "idN_example", // String | 
  'idLte': "idLte_example", // String | 
  'idLt': "idLt_example", // String | 
  'idGte': "idGte_example", // String | 
  'idGt': "idGt_example", // String | 
  'nameN': "nameN_example", // String | 
  'nameIc': "nameIc_example", // String | 
  'nameNic': "nameNic_example", // String | 
  'nameIew': "nameIew_example", // String | 
  'nameNiew': "nameNiew_example", // String | 
  'nameIsw': "nameIsw_example", // String | 
  'nameNisw': "nameNisw_example", // String | 
  'nameIe': "nameIe_example", // String | 
  'nameNie': "nameNie_example", // String | 
  'slugN': "slugN_example", // String | 
  'slugIc': "slugIc_example", // String | 
  'slugNic': "slugNic_example", // String | 
  'slugIew': "slugIew_example", // String | 
  'slugNiew': "slugNiew_example", // String | 
  'slugIsw': "slugIsw_example", // String | 
  'slugNisw': "slugNisw_example", // String | 
  'slugIe': "slugIe_example", // String | 
  'slugNie': "slugNie_example", // String | 
  'descriptionN': "descriptionN_example", // String | 
  'descriptionIc': "descriptionIc_example", // String | 
  'descriptionNic': "descriptionNic_example", // String | 
  'descriptionIew': "descriptionIew_example", // String | 
  'descriptionNiew': "descriptionNiew_example", // String | 
  'descriptionIsw': "descriptionIsw_example", // String | 
  'descriptionNisw': "descriptionNisw_example", // String | 
  'descriptionIe': "descriptionIe_example", // String | 
  'descriptionNie': "descriptionNie_example", // String | 
  'regionIdN': "regionIdN_example", // String | 
  'regionN': "regionN_example", // String | 
  'siteIdN': "siteIdN_example", // String | 
  'siteN': "siteN_example", // String | 
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
 **id** | **String**|  | [optional] 
 **name** | **String**|  | [optional] 
 **slug** | **String**|  | [optional] 
 **description** | **String**|  | [optional] 
 **q** | **String**|  | [optional] 
 **regionId** | **String**|  | [optional] 
 **region** | **String**|  | [optional] 
 **siteId** | **String**|  | [optional] 
 **site** | **String**|  | [optional] 
 **idN** | **String**|  | [optional] 
 **idLte** | **String**|  | [optional] 
 **idLt** | **String**|  | [optional] 
 **idGte** | **String**|  | [optional] 
 **idGt** | **String**|  | [optional] 
 **nameN** | **String**|  | [optional] 
 **nameIc** | **String**|  | [optional] 
 **nameNic** | **String**|  | [optional] 
 **nameIew** | **String**|  | [optional] 
 **nameNiew** | **String**|  | [optional] 
 **nameIsw** | **String**|  | [optional] 
 **nameNisw** | **String**|  | [optional] 
 **nameIe** | **String**|  | [optional] 
 **nameNie** | **String**|  | [optional] 
 **slugN** | **String**|  | [optional] 
 **slugIc** | **String**|  | [optional] 
 **slugNic** | **String**|  | [optional] 
 **slugIew** | **String**|  | [optional] 
 **slugNiew** | **String**|  | [optional] 
 **slugIsw** | **String**|  | [optional] 
 **slugNisw** | **String**|  | [optional] 
 **slugIe** | **String**|  | [optional] 
 **slugNie** | **String**|  | [optional] 
 **descriptionN** | **String**|  | [optional] 
 **descriptionIc** | **String**|  | [optional] 
 **descriptionNic** | **String**|  | [optional] 
 **descriptionIew** | **String**|  | [optional] 
 **descriptionNiew** | **String**|  | [optional] 
 **descriptionIsw** | **String**|  | [optional] 
 **descriptionNisw** | **String**|  | [optional] 
 **descriptionIe** | **String**|  | [optional] 
 **descriptionNie** | **String**|  | [optional] 
 **regionIdN** | **String**|  | [optional] 
 **regionN** | **String**|  | [optional] 
 **siteIdN** | **String**|  | [optional] 
 **siteN** | **String**|  | [optional] 
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



Call to super to allow for caching

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



Call to super to allow for caching

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
  'id': "id_example", // String | 
  'vid': "vid_example", // String | 
  'name': "name_example", // String | 
  'tenantGroupId': "tenantGroupId_example", // String | 
  'tenantGroup': "tenantGroup_example", // String | 
  'tenantId': "tenantId_example", // String | 
  'tenant': "tenant_example", // String | 
  'created': "created_example", // String | 
  'createdGte': "createdGte_example", // String | 
  'createdLte': "createdLte_example", // String | 
  'lastUpdated': "lastUpdated_example", // String | 
  'lastUpdatedGte': "lastUpdatedGte_example", // String | 
  'lastUpdatedLte': "lastUpdatedLte_example", // String | 
  'q': "q_example", // String | 
  'regionId': "regionId_example", // String | 
  'region': "region_example", // String | 
  'siteId': "siteId_example", // String | 
  'site': "site_example", // String | 
  'groupId': "groupId_example", // String | 
  'group': "group_example", // String | 
  'roleId': "roleId_example", // String | 
  'role': "role_example", // String | 
  'status': "status_example", // String | 
  'tag': "tag_example", // String | 
  'idN': "idN_example", // String | 
  'idLte': "idLte_example", // String | 
  'idLt': "idLt_example", // String | 
  'idGte': "idGte_example", // String | 
  'idGt': "idGt_example", // String | 
  'vidN': "vidN_example", // String | 
  'vidLte': "vidLte_example", // String | 
  'vidLt': "vidLt_example", // String | 
  'vidGte': "vidGte_example", // String | 
  'vidGt': "vidGt_example", // String | 
  'nameN': "nameN_example", // String | 
  'nameIc': "nameIc_example", // String | 
  'nameNic': "nameNic_example", // String | 
  'nameIew': "nameIew_example", // String | 
  'nameNiew': "nameNiew_example", // String | 
  'nameIsw': "nameIsw_example", // String | 
  'nameNisw': "nameNisw_example", // String | 
  'nameIe': "nameIe_example", // String | 
  'nameNie': "nameNie_example", // String | 
  'tenantGroupIdN': "tenantGroupIdN_example", // String | 
  'tenantGroupN': "tenantGroupN_example", // String | 
  'tenantIdN': "tenantIdN_example", // String | 
  'tenantN': "tenantN_example", // String | 
  'regionIdN': "regionIdN_example", // String | 
  'regionN': "regionN_example", // String | 
  'siteIdN': "siteIdN_example", // String | 
  'siteN': "siteN_example", // String | 
  'groupIdN': "groupIdN_example", // String | 
  'groupN': "groupN_example", // String | 
  'roleIdN': "roleIdN_example", // String | 
  'roleN': "roleN_example", // String | 
  'statusN': "statusN_example", // String | 
  'tagN': "tagN_example", // String | 
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
 **id** | **String**|  | [optional] 
 **vid** | **String**|  | [optional] 
 **name** | **String**|  | [optional] 
 **tenantGroupId** | **String**|  | [optional] 
 **tenantGroup** | **String**|  | [optional] 
 **tenantId** | **String**|  | [optional] 
 **tenant** | **String**|  | [optional] 
 **created** | **String**|  | [optional] 
 **createdGte** | **String**|  | [optional] 
 **createdLte** | **String**|  | [optional] 
 **lastUpdated** | **String**|  | [optional] 
 **lastUpdatedGte** | **String**|  | [optional] 
 **lastUpdatedLte** | **String**|  | [optional] 
 **q** | **String**|  | [optional] 
 **regionId** | **String**|  | [optional] 
 **region** | **String**|  | [optional] 
 **siteId** | **String**|  | [optional] 
 **site** | **String**|  | [optional] 
 **groupId** | **String**|  | [optional] 
 **group** | **String**|  | [optional] 
 **roleId** | **String**|  | [optional] 
 **role** | **String**|  | [optional] 
 **status** | **String**|  | [optional] 
 **tag** | **String**|  | [optional] 
 **idN** | **String**|  | [optional] 
 **idLte** | **String**|  | [optional] 
 **idLt** | **String**|  | [optional] 
 **idGte** | **String**|  | [optional] 
 **idGt** | **String**|  | [optional] 
 **vidN** | **String**|  | [optional] 
 **vidLte** | **String**|  | [optional] 
 **vidLt** | **String**|  | [optional] 
 **vidGte** | **String**|  | [optional] 
 **vidGt** | **String**|  | [optional] 
 **nameN** | **String**|  | [optional] 
 **nameIc** | **String**|  | [optional] 
 **nameNic** | **String**|  | [optional] 
 **nameIew** | **String**|  | [optional] 
 **nameNiew** | **String**|  | [optional] 
 **nameIsw** | **String**|  | [optional] 
 **nameNisw** | **String**|  | [optional] 
 **nameIe** | **String**|  | [optional] 
 **nameNie** | **String**|  | [optional] 
 **tenantGroupIdN** | **String**|  | [optional] 
 **tenantGroupN** | **String**|  | [optional] 
 **tenantIdN** | **String**|  | [optional] 
 **tenantN** | **String**|  | [optional] 
 **regionIdN** | **String**|  | [optional] 
 **regionN** | **String**|  | [optional] 
 **siteIdN** | **String**|  | [optional] 
 **siteN** | **String**|  | [optional] 
 **groupIdN** | **String**|  | [optional] 
 **groupN** | **String**|  | [optional] 
 **roleIdN** | **String**|  | [optional] 
 **roleN** | **String**|  | [optional] 
 **statusN** | **String**|  | [optional] 
 **tagN** | **String**|  | [optional] 
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



Call to super to allow for caching

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



Call to super to allow for caching

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
  'id': "id_example", // String | 
  'name': "name_example", // String | 
  'rd': "rd_example", // String | 
  'enforceUnique': "enforceUnique_example", // String | 
  'tenantGroupId': "tenantGroupId_example", // String | 
  'tenantGroup': "tenantGroup_example", // String | 
  'tenantId': "tenantId_example", // String | 
  'tenant': "tenant_example", // String | 
  'created': "created_example", // String | 
  'createdGte': "createdGte_example", // String | 
  'createdLte': "createdLte_example", // String | 
  'lastUpdated': "lastUpdated_example", // String | 
  'lastUpdatedGte': "lastUpdatedGte_example", // String | 
  'lastUpdatedLte': "lastUpdatedLte_example", // String | 
  'q': "q_example", // String | 
  'tag': "tag_example", // String | 
  'idN': "idN_example", // String | 
  'idLte': "idLte_example", // String | 
  'idLt': "idLt_example", // String | 
  'idGte': "idGte_example", // String | 
  'idGt': "idGt_example", // String | 
  'nameN': "nameN_example", // String | 
  'nameIc': "nameIc_example", // String | 
  'nameNic': "nameNic_example", // String | 
  'nameIew': "nameIew_example", // String | 
  'nameNiew': "nameNiew_example", // String | 
  'nameIsw': "nameIsw_example", // String | 
  'nameNisw': "nameNisw_example", // String | 
  'nameIe': "nameIe_example", // String | 
  'nameNie': "nameNie_example", // String | 
  'rdN': "rdN_example", // String | 
  'rdIc': "rdIc_example", // String | 
  'rdNic': "rdNic_example", // String | 
  'rdIew': "rdIew_example", // String | 
  'rdNiew': "rdNiew_example", // String | 
  'rdIsw': "rdIsw_example", // String | 
  'rdNisw': "rdNisw_example", // String | 
  'rdIe': "rdIe_example", // String | 
  'rdNie': "rdNie_example", // String | 
  'tenantGroupIdN': "tenantGroupIdN_example", // String | 
  'tenantGroupN': "tenantGroupN_example", // String | 
  'tenantIdN': "tenantIdN_example", // String | 
  'tenantN': "tenantN_example", // String | 
  'tagN': "tagN_example", // String | 
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
 **id** | **String**|  | [optional] 
 **name** | **String**|  | [optional] 
 **rd** | **String**|  | [optional] 
 **enforceUnique** | **String**|  | [optional] 
 **tenantGroupId** | **String**|  | [optional] 
 **tenantGroup** | **String**|  | [optional] 
 **tenantId** | **String**|  | [optional] 
 **tenant** | **String**|  | [optional] 
 **created** | **String**|  | [optional] 
 **createdGte** | **String**|  | [optional] 
 **createdLte** | **String**|  | [optional] 
 **lastUpdated** | **String**|  | [optional] 
 **lastUpdatedGte** | **String**|  | [optional] 
 **lastUpdatedLte** | **String**|  | [optional] 
 **q** | **String**|  | [optional] 
 **tag** | **String**|  | [optional] 
 **idN** | **String**|  | [optional] 
 **idLte** | **String**|  | [optional] 
 **idLt** | **String**|  | [optional] 
 **idGte** | **String**|  | [optional] 
 **idGt** | **String**|  | [optional] 
 **nameN** | **String**|  | [optional] 
 **nameIc** | **String**|  | [optional] 
 **nameNic** | **String**|  | [optional] 
 **nameIew** | **String**|  | [optional] 
 **nameNiew** | **String**|  | [optional] 
 **nameIsw** | **String**|  | [optional] 
 **nameNisw** | **String**|  | [optional] 
 **nameIe** | **String**|  | [optional] 
 **nameNie** | **String**|  | [optional] 
 **rdN** | **String**|  | [optional] 
 **rdIc** | **String**|  | [optional] 
 **rdNic** | **String**|  | [optional] 
 **rdIew** | **String**|  | [optional] 
 **rdNiew** | **String**|  | [optional] 
 **rdIsw** | **String**|  | [optional] 
 **rdNisw** | **String**|  | [optional] 
 **rdIe** | **String**|  | [optional] 
 **rdNie** | **String**|  | [optional] 
 **tenantGroupIdN** | **String**|  | [optional] 
 **tenantGroupN** | **String**|  | [optional] 
 **tenantIdN** | **String**|  | [optional] 
 **tenantN** | **String**|  | [optional] 
 **tagN** | **String**|  | [optional] 
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



Call to super to allow for caching

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

