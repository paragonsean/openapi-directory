# IxApi.NetworkServiceConfigsApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**networkServiceConfigCancellationPolicyRead**](NetworkServiceConfigsApi.md#networkServiceConfigCancellationPolicyRead) | **GET** /network-service-configs/{id}/cancellation-policy | 
[**networkServiceConfigsCreate**](NetworkServiceConfigsApi.md#networkServiceConfigsCreate) | **POST** /network-service-configs | 
[**networkServiceConfigsDestroy**](NetworkServiceConfigsApi.md#networkServiceConfigsDestroy) | **DELETE** /network-service-configs/{id} | 
[**networkServiceConfigsList**](NetworkServiceConfigsApi.md#networkServiceConfigsList) | **GET** /network-service-configs | 
[**networkServiceConfigsPartialUpdate**](NetworkServiceConfigsApi.md#networkServiceConfigsPartialUpdate) | **PATCH** /network-service-configs/{id} | 
[**networkServiceConfigsRead**](NetworkServiceConfigsApi.md#networkServiceConfigsRead) | **GET** /network-service-configs/{id} | 
[**networkServiceConfigsUpdate**](NetworkServiceConfigsApi.md#networkServiceConfigsUpdate) | **PUT** /network-service-configs/{id} | 



## networkServiceConfigCancellationPolicyRead

> CancellationPolicy networkServiceConfigCancellationPolicyRead(id, opts)



The cancellation-policy can be queried to answer the questions:  If I cancel my subscription, *when will it be technically decommissioned*? If I cancel my subscription, *until what date will I be charged*?  When the query parameter &#x60;decommision_at&#x60; is not provided it will provide the first possible cancellation date and charge period if cancelled at above date.  The granularity of the date field is a day, the start and end of which are to be interpreted by the IXP (some may use UTC, some may use their local time zone).

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.NetworkServiceConfigsApi();
let id = "id_example"; // String | Get by id
let opts = {
  'decommissionAt': "decommissionAt_example" // String | By providing a date in the format `YYYY-MM-DD` you can query the policy what would happen if you request a decommissioning on this date.
};
apiInstance.networkServiceConfigCancellationPolicyRead(id, opts, (error, data, response) => {
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
 **decommissionAt** | **String**| By providing a date in the format &#x60;YYYY-MM-DD&#x60; you can query the policy what would happen if you request a decommissioning on this date. | [optional] 

### Return type

[**CancellationPolicy**](CancellationPolicy.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## networkServiceConfigsCreate

> NetworkServiceConfig networkServiceConfigsCreate(opts)



Create a &#x60;network-service-config&#x60;.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.NetworkServiceConfigsApi();
let opts = {
  'networkServiceConfigRequest': new IxApi.NetworkServiceConfigRequest() // NetworkServiceConfigRequest | Polymorhic Network Service Config Request
};
apiInstance.networkServiceConfigsCreate(opts, (error, data, response) => {
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
 **networkServiceConfigRequest** | [**NetworkServiceConfigRequest**](NetworkServiceConfigRequest.md)| Polymorhic Network Service Config Request | [optional] 

### Return type

[**NetworkServiceConfig**](NetworkServiceConfig.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## networkServiceConfigsDestroy

> NetworkServiceConfig networkServiceConfigsDestroy(id, opts)



Request decommissioning the network service configuration.  The network service config will assume the state &#x60;decommission_requested&#x60;. This will cascade to related resources like &#x60;network-feature-configs&#x60;.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.NetworkServiceConfigsApi();
let id = "id_example"; // String | Get by id
let opts = {
  'cancellationRequest': new IxApi.CancellationRequest() // CancellationRequest | Service Cancellation Request
};
apiInstance.networkServiceConfigsDestroy(id, opts, (error, data, response) => {
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
 **cancellationRequest** | [**CancellationRequest**](CancellationRequest.md)| Service Cancellation Request | [optional] 

### Return type

[**NetworkServiceConfig**](NetworkServiceConfig.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## networkServiceConfigsList

> [NetworkServiceConfig] networkServiceConfigsList(opts)



Get all &#x60;network-service-config&#x60;s.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.NetworkServiceConfigsApi();
let opts = {
  'id': ["null"], // [String] | Filter by id
  'state': "state_example", // String | Filter by state
  'stateIsNot': "stateIsNot_example", // String | Filter by state__is_not
  'managingAccount': "managingAccount_example", // String | Filter by managing_account
  'consumingAccount': "consumingAccount_example", // String | Filter by consuming_account
  'externalRef': "externalRef_example", // String | Filter by external_ref
  'type': "type_example", // String | Filter by type
  'innerVlan': 56, // Number | Filter by inner_vlan
  'outerVlan': 56, // Number | Filter by outer_vlan
  'capacity': 56, // Number | Filter by capacity
  'networkService': "networkService_example", // String | Filter by network_service
  'connection': "connection_example", // String | Filter by connection
  'productOffering': "productOffering_example" // String | Filter by product_offering
};
apiInstance.networkServiceConfigsList(opts, (error, data, response) => {
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
 **state** | **String**| Filter by state | [optional] 
 **stateIsNot** | **String**| Filter by state__is_not | [optional] 
 **managingAccount** | **String**| Filter by managing_account | [optional] 
 **consumingAccount** | **String**| Filter by consuming_account | [optional] 
 **externalRef** | **String**| Filter by external_ref | [optional] 
 **type** | **String**| Filter by type | [optional] 
 **innerVlan** | **Number**| Filter by inner_vlan | [optional] 
 **outerVlan** | **Number**| Filter by outer_vlan | [optional] 
 **capacity** | **Number**| Filter by capacity | [optional] 
 **networkService** | **String**| Filter by network_service | [optional] 
 **connection** | **String**| Filter by connection | [optional] 
 **productOffering** | **String**| Filter by product_offering | [optional] 

### Return type

[**[NetworkServiceConfig]**](NetworkServiceConfig.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## networkServiceConfigsPartialUpdate

> NetworkServiceConfig networkServiceConfigsPartialUpdate(id, opts)



Update parts of an exisiting &#x60;network-service-config&#x60;.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.NetworkServiceConfigsApi();
let id = "id_example"; // String | Get by id
let opts = {
  'networkServiceConfigUpdatePartial': new IxApi.NetworkServiceConfigUpdatePartial() // NetworkServiceConfigUpdatePartial | Polymorphic Network Service Config
};
apiInstance.networkServiceConfigsPartialUpdate(id, opts, (error, data, response) => {
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
 **networkServiceConfigUpdatePartial** | [**NetworkServiceConfigUpdatePartial**](NetworkServiceConfigUpdatePartial.md)| Polymorphic Network Service Config | [optional] 

### Return type

[**NetworkServiceConfig**](NetworkServiceConfig.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json


## networkServiceConfigsRead

> NetworkServiceConfig networkServiceConfigsRead(id)



Get a &#x60;network-service-config&#x60;

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.NetworkServiceConfigsApi();
let id = "id_example"; // String | Get by id
apiInstance.networkServiceConfigsRead(id, (error, data, response) => {
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

[**NetworkServiceConfig**](NetworkServiceConfig.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## networkServiceConfigsUpdate

> NetworkServiceConfig networkServiceConfigsUpdate(id, opts)



Update an exisiting &#x60;network-service-config&#x60;

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.NetworkServiceConfigsApi();
let id = "id_example"; // String | Get by id
let opts = {
  'networkServiceConfigUpdate': new IxApi.NetworkServiceConfigUpdate() // NetworkServiceConfigUpdate | Polymorphic Network Service Config
};
apiInstance.networkServiceConfigsUpdate(id, opts, (error, data, response) => {
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
 **networkServiceConfigUpdate** | [**NetworkServiceConfigUpdate**](NetworkServiceConfigUpdate.md)| Polymorphic Network Service Config | [optional] 

### Return type

[**NetworkServiceConfig**](NetworkServiceConfig.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

