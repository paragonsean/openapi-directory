# IxApi.NetworkFeatureConfigsApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**networkFeatureConfigsCreate**](NetworkFeatureConfigsApi.md#networkFeatureConfigsCreate) | **POST** /network-feature-configs | 
[**networkFeatureConfigsDestroy**](NetworkFeatureConfigsApi.md#networkFeatureConfigsDestroy) | **DELETE** /network-feature-configs/{id} | 
[**networkFeatureConfigsList**](NetworkFeatureConfigsApi.md#networkFeatureConfigsList) | **GET** /network-feature-configs | 
[**networkFeatureConfigsPartialUpdate**](NetworkFeatureConfigsApi.md#networkFeatureConfigsPartialUpdate) | **PATCH** /network-feature-configs/{id} | 
[**networkFeatureConfigsRead**](NetworkFeatureConfigsApi.md#networkFeatureConfigsRead) | **GET** /network-feature-configs/{id} | 
[**networkFeatureConfigsUpdate**](NetworkFeatureConfigsApi.md#networkFeatureConfigsUpdate) | **PUT** /network-feature-configs/{id} | 



## networkFeatureConfigsCreate

> NetworkFeatureConfig networkFeatureConfigsCreate(opts)



Create a configuration for a &#x60;NetworkFeature&#x60; defined in the &#x60;NetworkFeature&#x60;s collection.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.NetworkFeatureConfigsApi();
let opts = {
  'networkFeatureConfigRequest': new IxApi.NetworkFeatureConfigRequest() // NetworkFeatureConfigRequest | Polymorphic Network Feature Config Request
};
apiInstance.networkFeatureConfigsCreate(opts, (error, data, response) => {
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
 **networkFeatureConfigRequest** | [**NetworkFeatureConfigRequest**](NetworkFeatureConfigRequest.md)| Polymorphic Network Feature Config Request | [optional] 

### Return type

[**NetworkFeatureConfig**](NetworkFeatureConfig.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## networkFeatureConfigsDestroy

> NetworkFeatureConfig networkFeatureConfigsDestroy(id)



Remove a network feature config.  The network feature config will be marked as &#x60;decommission_requested&#x60;. Decommissioning a network feature config will not cascade to related services or service configs.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.NetworkFeatureConfigsApi();
let id = "id_example"; // String | Get by id
apiInstance.networkFeatureConfigsDestroy(id, (error, data, response) => {
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

[**NetworkFeatureConfig**](NetworkFeatureConfig.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## networkFeatureConfigsList

> [NetworkFeatureConfig] networkFeatureConfigsList(opts)



Get all network feature configs.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.NetworkFeatureConfigsApi();
let opts = {
  'id': ["null"], // [String] | Filter by id
  'state': "state_example", // String | Filter by state
  'stateIsNot': "stateIsNot_example", // String | Filter by state__is_not
  'managingAccount': "managingAccount_example", // String | Filter by managing_account
  'consumingAccount': "consumingAccount_example", // String | Filter by consuming_account
  'externalRef': "externalRef_example", // String | Filter by external_ref
  'type': "type_example", // String | Filter by type
  'serviceConfig': "serviceConfig_example", // String | Filter by service_config
  'networkFeature': "networkFeature_example" // String | Filter by network_feature
};
apiInstance.networkFeatureConfigsList(opts, (error, data, response) => {
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
 **serviceConfig** | **String**| Filter by service_config | [optional] 
 **networkFeature** | **String**| Filter by network_feature | [optional] 

### Return type

[**[NetworkFeatureConfig]**](NetworkFeatureConfig.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## networkFeatureConfigsPartialUpdate

> NetworkFeatureConfig networkFeatureConfigsPartialUpdate(id, opts)



Update parts of a network feature configuration

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.NetworkFeatureConfigsApi();
let id = "id_example"; // String | Get by id
let opts = {
  'networkFeatureConfigUpdatePartial': new IxApi.NetworkFeatureConfigUpdatePartial() // NetworkFeatureConfigUpdatePartial | Polymorphic Network Feauture Config Update
};
apiInstance.networkFeatureConfigsPartialUpdate(id, opts, (error, data, response) => {
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
 **networkFeatureConfigUpdatePartial** | [**NetworkFeatureConfigUpdatePartial**](NetworkFeatureConfigUpdatePartial.md)| Polymorphic Network Feauture Config Update | [optional] 

### Return type

[**NetworkFeatureConfig**](NetworkFeatureConfig.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json


## networkFeatureConfigsRead

> NetworkFeatureConfig networkFeatureConfigsRead(id)



Get a single network feature config.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.NetworkFeatureConfigsApi();
let id = "id_example"; // String | Get by id
apiInstance.networkFeatureConfigsRead(id, (error, data, response) => {
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

[**NetworkFeatureConfig**](NetworkFeatureConfig.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## networkFeatureConfigsUpdate

> NetworkFeatureConfig networkFeatureConfigsUpdate(id, opts)



Update a network feature configuration

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.NetworkFeatureConfigsApi();
let id = "id_example"; // String | Get by id
let opts = {
  'networkFeatureConfigUpdate': new IxApi.NetworkFeatureConfigUpdate() // NetworkFeatureConfigUpdate | Polymorphic Network Feauture Config Update
};
apiInstance.networkFeatureConfigsUpdate(id, opts, (error, data, response) => {
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
 **networkFeatureConfigUpdate** | [**NetworkFeatureConfigUpdate**](NetworkFeatureConfigUpdate.md)| Polymorphic Network Feauture Config Update | [optional] 

### Return type

[**NetworkFeatureConfig**](NetworkFeatureConfig.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

