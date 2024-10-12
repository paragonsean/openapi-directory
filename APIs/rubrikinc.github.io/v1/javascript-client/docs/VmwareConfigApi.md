# RubrikRestApi.VmwareConfigApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPreferredCdpNetworkProtocol**](VmwareConfigApi.md#getPreferredCdpNetworkProtocol) | **GET** /vmware/config/cdp/get_preferred_cdp_network_protocol | Returns the current preference of CDM between IPv4 and IPv6 for CDP data transfer
[**getVmwareRecoveryNetworks**](VmwareConfigApi.md#getVmwareRecoveryNetworks) | **GET** /vmware/config/recovery/networks | Get all the VMware recovery networks for a compute resource ID
[**setPreferredCdpNetworkProtocol**](VmwareConfigApi.md#setPreferredCdpNetworkProtocol) | **PATCH** /vmware/config/cdp/set_preferred_cdp_network_protocol | Set the current preference of CDM between IPv4 and IPv6 for CDP data transfer



## getPreferredCdpNetworkProtocol

> PreferredCdpNetworkProtocolObject getPreferredCdpNetworkProtocol()

Returns the current preference of CDM between IPv4 and IPv6 for CDP data transfer

Returns the current preference of CDM between IPv4 and IPv6 for CDP data transfer.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.VmwareConfigApi();
apiInstance.getPreferredCdpNetworkProtocol((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**PreferredCdpNetworkProtocolObject**](PreferredCdpNetworkProtocolObject.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVmwareRecoveryNetworks

> VmwareNetworkCollection getVmwareRecoveryNetworks(computeResourceId, computeResourceType)

Get all the VMware recovery networks for a compute resource ID

Get all the networks for snapshot recovery for the specified compute resource.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.VmwareConfigApi();
let computeResourceId = "computeResourceId_example"; // String | Get VMware recovery networks for the compute resource ID.
let computeResourceType = "computeResourceType_example"; // String | The type of the compute resource.
apiInstance.getVmwareRecoveryNetworks(computeResourceId, computeResourceType, (error, data, response) => {
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
 **computeResourceId** | **String**| Get VMware recovery networks for the compute resource ID. | 
 **computeResourceType** | **String**| The type of the compute resource. | 

### Return type

[**VmwareNetworkCollection**](VmwareNetworkCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setPreferredCdpNetworkProtocol

> PreferredCdpNetworkProtocolObject setPreferredCdpNetworkProtocol(body)

Set the current preference of CDM between IPv4 and IPv6 for CDP data transfer

Set the current preference of CDM between IPv4 and IPv6 for CDP data transfer.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.VmwareConfigApi();
let body = null; // String | The preferred network protocol to use for transferring CDP data.
apiInstance.setPreferredCdpNetworkProtocol(body, (error, data, response) => {
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
 **body** | **String**| The preferred network protocol to use for transferring CDP data. | 

### Return type

[**PreferredCdpNetworkProtocolObject**](PreferredCdpNetworkProtocolObject.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

