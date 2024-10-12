# RubrikRestApi.HypervVmApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getHypervVirtualMachineForceFullSpec**](HypervVmApi.md#getHypervVirtualMachineForceFullSpec) | **GET** /hyperv/vm/{id}/request/force_full_snapshot | Retrieve the configuration which has been set for forcing a full snapshot for a Hyper-V Virtual Machine
[**requestHypervVirtualMachineForceFullSnapshot**](HypervVmApi.md#requestHypervVirtualMachineForceFullSnapshot) | **POST** /hyperv/vm/{id}/request/force_full_snapshot | Request a full snapshot during next backup job of a Hyper-V virtual machine



## getHypervVirtualMachineForceFullSpec

> HypervVirtualMachineForceFullResponse getHypervVirtualMachineForceFullSpec(id)

Retrieve the configuration which has been set for forcing a full snapshot for a Hyper-V Virtual Machine

Retrieve the configuration created to force a full snapshot for a Hyper-V Virtual Machine.

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

let apiInstance = new RubrikRestApi.HypervVmApi();
let id = "id_example"; // String | The ID of the Hyper-V virtual machine.
apiInstance.getHypervVirtualMachineForceFullSpec(id, (error, data, response) => {
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
 **id** | **String**| The ID of the Hyper-V virtual machine. | 

### Return type

[**HypervVirtualMachineForceFullResponse**](HypervVirtualMachineForceFullResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestHypervVirtualMachineForceFullSnapshot

> HypervVirtualMachineForceFullResponse requestHypervVirtualMachineForceFullSnapshot(id, hypervVirtualMachineForceFullRequest)

Request a full snapshot during next backup job of a Hyper-V virtual machine

Request a full snapshot during the next backup job of a Hyper-V virtual machine.

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

let apiInstance = new RubrikRestApi.HypervVmApi();
let id = "id_example"; // String | ID of the Hyper-V virtual machine.
let hypervVirtualMachineForceFullRequest = new RubrikRestApi.HypervVirtualMachineForceFullRequest(); // HypervVirtualMachineForceFullRequest | Configuration created to force a full snapshot on the Hyper-V virtual machine.
apiInstance.requestHypervVirtualMachineForceFullSnapshot(id, hypervVirtualMachineForceFullRequest, (error, data, response) => {
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
 **id** | **String**| ID of the Hyper-V virtual machine. | 
 **hypervVirtualMachineForceFullRequest** | [**HypervVirtualMachineForceFullRequest**](HypervVirtualMachineForceFullRequest.md)| Configuration created to force a full snapshot on the Hyper-V virtual machine. | 

### Return type

[**HypervVirtualMachineForceFullResponse**](HypervVirtualMachineForceFullResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

