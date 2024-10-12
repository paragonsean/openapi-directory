# HetznerCloudApi.LoadBalancerActionsApi

All URIs are relative to *https://api.hetzner.cloud/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**loadBalancersIdActionsActionIdGet**](LoadBalancerActionsApi.md#loadBalancersIdActionsActionIdGet) | **GET** /load_balancers/{id}/actions/{action_id} | Get an Action for a Load Balancer
[**loadBalancersIdActionsAddServicePost**](LoadBalancerActionsApi.md#loadBalancersIdActionsAddServicePost) | **POST** /load_balancers/{id}/actions/add_service | Add Service
[**loadBalancersIdActionsAddTargetPost**](LoadBalancerActionsApi.md#loadBalancersIdActionsAddTargetPost) | **POST** /load_balancers/{id}/actions/add_target | Add Target
[**loadBalancersIdActionsAttachToNetworkPost**](LoadBalancerActionsApi.md#loadBalancersIdActionsAttachToNetworkPost) | **POST** /load_balancers/{id}/actions/attach_to_network | Attach a Load Balancer to a Network
[**loadBalancersIdActionsChangeAlgorithmPost**](LoadBalancerActionsApi.md#loadBalancersIdActionsChangeAlgorithmPost) | **POST** /load_balancers/{id}/actions/change_algorithm | Change Algorithm
[**loadBalancersIdActionsChangeDnsPtrPost**](LoadBalancerActionsApi.md#loadBalancersIdActionsChangeDnsPtrPost) | **POST** /load_balancers/{id}/actions/change_dns_ptr | Change reverse DNS entry for this Load Balancer
[**loadBalancersIdActionsChangeProtectionPost**](LoadBalancerActionsApi.md#loadBalancersIdActionsChangeProtectionPost) | **POST** /load_balancers/{id}/actions/change_protection | Change Load Balancer Protection
[**loadBalancersIdActionsChangeTypePost**](LoadBalancerActionsApi.md#loadBalancersIdActionsChangeTypePost) | **POST** /load_balancers/{id}/actions/change_type | Change the Type of a Load Balancer
[**loadBalancersIdActionsDeleteServicePost**](LoadBalancerActionsApi.md#loadBalancersIdActionsDeleteServicePost) | **POST** /load_balancers/{id}/actions/delete_service | Delete Service
[**loadBalancersIdActionsDetachFromNetworkPost**](LoadBalancerActionsApi.md#loadBalancersIdActionsDetachFromNetworkPost) | **POST** /load_balancers/{id}/actions/detach_from_network | Detach a Load Balancer from a Network
[**loadBalancersIdActionsDisablePublicInterfacePost**](LoadBalancerActionsApi.md#loadBalancersIdActionsDisablePublicInterfacePost) | **POST** /load_balancers/{id}/actions/disable_public_interface | Disable the public interface of a Load Balancer
[**loadBalancersIdActionsEnablePublicInterfacePost**](LoadBalancerActionsApi.md#loadBalancersIdActionsEnablePublicInterfacePost) | **POST** /load_balancers/{id}/actions/enable_public_interface | Enable the public interface of a Load Balancer
[**loadBalancersIdActionsGet**](LoadBalancerActionsApi.md#loadBalancersIdActionsGet) | **GET** /load_balancers/{id}/actions | Get all Actions for a Load Balancer
[**loadBalancersIdActionsRemoveTargetPost**](LoadBalancerActionsApi.md#loadBalancersIdActionsRemoveTargetPost) | **POST** /load_balancers/{id}/actions/remove_target | Remove Target
[**loadBalancersIdActionsUpdateServicePost**](LoadBalancerActionsApi.md#loadBalancersIdActionsUpdateServicePost) | **POST** /load_balancers/{id}/actions/update_service | Update Service



## loadBalancersIdActionsActionIdGet

> ActionResponse loadBalancersIdActionsActionIdGet(id, actionId)

Get an Action for a Load Balancer

Returns a specific Action for a Load Balancer.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.LoadBalancerActionsApi();
let id = 56; // Number | ID of the Load Balancer
let actionId = 56; // Number | ID of the Action
apiInstance.loadBalancersIdActionsActionIdGet(id, actionId, (error, data, response) => {
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
 **id** | **Number**| ID of the Load Balancer | 
 **actionId** | **Number**| ID of the Action | 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## loadBalancersIdActionsAddServicePost

> ActionResponse loadBalancersIdActionsAddServicePost(id, opts)

Add Service

Adds a service to a Load Balancer.  #### Call specific error codes  | Code                       | Description                                             | |----------------------------|---------------------------------------------------------| | &#x60;source_port_already_used&#x60; | The source port you are trying to add is already in use | 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.LoadBalancerActionsApi();
let id = 56; // Number | ID of the Load Balancer
let opts = {
  'loadBalancerService': new HetznerCloudApi.LoadBalancerService() // LoadBalancerService | 
};
apiInstance.loadBalancersIdActionsAddServicePost(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Load Balancer | 
 **loadBalancerService** | [**LoadBalancerService**](LoadBalancerService.md)|  | [optional] 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## loadBalancersIdActionsAddTargetPost

> ActionResponse loadBalancersIdActionsAddTargetPost(id, opts)

Add Target

Adds a target to a Load Balancer.  #### Call specific error codes  | Code                                    | Description                                                                                           | |-----------------------------------------|-------------------------------------------------------------------------------------------------------| | &#x60;cloud_resource_ip_not_allowed&#x60;         | The IP you are trying to add as a target belongs to a Hetzner Cloud resource                          | | &#x60;ip_not_owned&#x60;                          | The IP you are trying to add as a target is not owned by the Project owner                            | | &#x60;load_balancer_not_attached_to_network&#x60; | The Load Balancer is not attached to a network                                                        | | &#x60;robot_unavailable&#x60;                     | Robot was not available. The caller may retry the operation after a short delay.                      | | &#x60;server_not_attached_to_network&#x60;        | The server you are trying to add as a target is not attached to the same network as the Load Balancer | | &#x60;target_already_defined&#x60;                | The Load Balancer target you are trying to define is already defined                                  | 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.LoadBalancerActionsApi();
let id = 56; // Number | ID of the Load Balancer
let opts = {
  'addTargetRequest': new HetznerCloudApi.AddTargetRequest() // AddTargetRequest | 
};
apiInstance.loadBalancersIdActionsAddTargetPost(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Load Balancer | 
 **addTargetRequest** | [**AddTargetRequest**](AddTargetRequest.md)|  | [optional] 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## loadBalancersIdActionsAttachToNetworkPost

> ActionResponse loadBalancersIdActionsAttachToNetworkPost(id, opts)

Attach a Load Balancer to a Network

Attach a Load Balancer to a Network.  **Call specific error codes**  | Code                             | Description                                                           | |----------------------------------|-----------------------------------------------------------------------| | &#x60;load_balancer_already_attached&#x60; | The Load Balancer is already attached to a network                    | | &#x60;ip_not_available&#x60;               | The provided Network IP is not available                              | | &#x60;no_subnet_available&#x60;            | No Subnet or IP is available for the Load Balancer within the network | 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.LoadBalancerActionsApi();
let id = 56; // Number | ID of the Load Balancer
let opts = {
  'loadBalancersIdActionsAttachToNetworkPostRequest': new HetznerCloudApi.LoadBalancersIdActionsAttachToNetworkPostRequest() // LoadBalancersIdActionsAttachToNetworkPostRequest | 
};
apiInstance.loadBalancersIdActionsAttachToNetworkPost(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Load Balancer | 
 **loadBalancersIdActionsAttachToNetworkPostRequest** | [**LoadBalancersIdActionsAttachToNetworkPostRequest**](LoadBalancersIdActionsAttachToNetworkPostRequest.md)|  | [optional] 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## loadBalancersIdActionsChangeAlgorithmPost

> ActionResponse loadBalancersIdActionsChangeAlgorithmPost(id, opts)

Change Algorithm

Change the algorithm that determines to which target new requests are sent.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.LoadBalancerActionsApi();
let id = 56; // Number | ID of the Load Balancer
let opts = {
  'loadBalancersIdActionsChangeAlgorithmPostRequest': new HetznerCloudApi.LoadBalancersIdActionsChangeAlgorithmPostRequest() // LoadBalancersIdActionsChangeAlgorithmPostRequest | 
};
apiInstance.loadBalancersIdActionsChangeAlgorithmPost(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Load Balancer | 
 **loadBalancersIdActionsChangeAlgorithmPostRequest** | [**LoadBalancersIdActionsChangeAlgorithmPostRequest**](LoadBalancersIdActionsChangeAlgorithmPostRequest.md)|  | [optional] 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## loadBalancersIdActionsChangeDnsPtrPost

> ActionResponse loadBalancersIdActionsChangeDnsPtrPost(id, opts)

Change reverse DNS entry for this Load Balancer

Changes the hostname that will appear when getting the hostname belonging to the public IPs (IPv4 and IPv6) of this Load Balancer.  Floating IPs assigned to the Server are not affected by this. 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.LoadBalancerActionsApi();
let id = 56; // Number | ID of the Load Balancer
let opts = {
  'changeLoadbalancerDnsPtrRequest': new HetznerCloudApi.ChangeLoadbalancerDnsPtrRequest() // ChangeLoadbalancerDnsPtrRequest | Select the IP address for which to change the DNS entry by passing `ip`. It can be either IPv4 or IPv6. The target hostname is set by passing `dns_ptr`.
};
apiInstance.loadBalancersIdActionsChangeDnsPtrPost(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Load Balancer | 
 **changeLoadbalancerDnsPtrRequest** | [**ChangeLoadbalancerDnsPtrRequest**](ChangeLoadbalancerDnsPtrRequest.md)| Select the IP address for which to change the DNS entry by passing &#x60;ip&#x60;. It can be either IPv4 or IPv6. The target hostname is set by passing &#x60;dns_ptr&#x60;. | [optional] 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## loadBalancersIdActionsChangeProtectionPost

> ActionResponse loadBalancersIdActionsChangeProtectionPost(id, opts)

Change Load Balancer Protection

Changes the protection configuration of a Load Balancer.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.LoadBalancerActionsApi();
let id = 56; // Number | ID of the Load Balancer
let opts = {
  'loadBalancersIdActionsChangeProtectionPostRequest': new HetznerCloudApi.LoadBalancersIdActionsChangeProtectionPostRequest() // LoadBalancersIdActionsChangeProtectionPostRequest | 
};
apiInstance.loadBalancersIdActionsChangeProtectionPost(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Load Balancer | 
 **loadBalancersIdActionsChangeProtectionPostRequest** | [**LoadBalancersIdActionsChangeProtectionPostRequest**](LoadBalancersIdActionsChangeProtectionPostRequest.md)|  | [optional] 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## loadBalancersIdActionsChangeTypePost

> ActionResponse loadBalancersIdActionsChangeTypePost(id, opts)

Change the Type of a Load Balancer

Changes the type (Max Services, Max Targets and Max Connections) of a Load Balancer.  **Call specific error codes**  | Code                         | Description                                                     | |------------------------------|-----------------------------------------------------------------| | &#x60;invalid_load_balancer_type&#x60; | The Load Balancer type does not fit for the given Load Balancer | 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.LoadBalancerActionsApi();
let id = 56; // Number | ID of the Load Balancer
let opts = {
  'changeTypeRequest': new HetznerCloudApi.ChangeTypeRequest() // ChangeTypeRequest | 
};
apiInstance.loadBalancersIdActionsChangeTypePost(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Load Balancer | 
 **changeTypeRequest** | [**ChangeTypeRequest**](ChangeTypeRequest.md)|  | [optional] 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## loadBalancersIdActionsDeleteServicePost

> ActionResponse loadBalancersIdActionsDeleteServicePost(id, opts)

Delete Service

Delete a service of a Load Balancer.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.LoadBalancerActionsApi();
let id = 56; // Number | ID of the Load Balancer
let opts = {
  'loadBalancersIdActionsDeleteServicePostRequest': new HetznerCloudApi.LoadBalancersIdActionsDeleteServicePostRequest() // LoadBalancersIdActionsDeleteServicePostRequest | 
};
apiInstance.loadBalancersIdActionsDeleteServicePost(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Load Balancer | 
 **loadBalancersIdActionsDeleteServicePostRequest** | [**LoadBalancersIdActionsDeleteServicePostRequest**](LoadBalancersIdActionsDeleteServicePostRequest.md)|  | [optional] 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## loadBalancersIdActionsDetachFromNetworkPost

> ActionResponse loadBalancersIdActionsDetachFromNetworkPost(id, opts)

Detach a Load Balancer from a Network

Detaches a Load Balancer from a network.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.LoadBalancerActionsApi();
let id = 56; // Number | ID of the Load Balancer
let opts = {
  'loadBalancersIdActionsDetachFromNetworkPostRequest': new HetznerCloudApi.LoadBalancersIdActionsDetachFromNetworkPostRequest() // LoadBalancersIdActionsDetachFromNetworkPostRequest | 
};
apiInstance.loadBalancersIdActionsDetachFromNetworkPost(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Load Balancer | 
 **loadBalancersIdActionsDetachFromNetworkPostRequest** | [**LoadBalancersIdActionsDetachFromNetworkPostRequest**](LoadBalancersIdActionsDetachFromNetworkPostRequest.md)|  | [optional] 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## loadBalancersIdActionsDisablePublicInterfacePost

> ActionResponse loadBalancersIdActionsDisablePublicInterfacePost(id)

Disable the public interface of a Load Balancer

Disable the public interface of a Load Balancer. The Load Balancer will be not accessible from the internet via its public IPs.  #### Call specific error codes  | Code                                      | Description                                                                    | |-------------------------------------------|--------------------------------------------------------------------------------| | &#x60;load_balancer_not_attached_to_network&#x60;   |  The Load Balancer is not attached to a network                                | | &#x60;targets_without_use_private_ip&#x60;          | The Load Balancer has targets that use the public IP instead of the private IP | 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.LoadBalancerActionsApi();
let id = 56; // Number | ID of the Load Balancer
apiInstance.loadBalancersIdActionsDisablePublicInterfacePost(id, (error, data, response) => {
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
 **id** | **Number**| ID of the Load Balancer | 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## loadBalancersIdActionsEnablePublicInterfacePost

> ActionResponse loadBalancersIdActionsEnablePublicInterfacePost(id)

Enable the public interface of a Load Balancer

Enable the public interface of a Load Balancer. The Load Balancer will be accessible from the internet via its public IPs.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.LoadBalancerActionsApi();
let id = 56; // Number | ID of the Load Balancer
apiInstance.loadBalancersIdActionsEnablePublicInterfacePost(id, (error, data, response) => {
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
 **id** | **Number**| ID of the Load Balancer | 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## loadBalancersIdActionsGet

> ActionsResponse loadBalancersIdActionsGet(id, opts)

Get all Actions for a Load Balancer

Returns all Action objects for a Load Balancer. You can sort the results by using the &#x60;sort&#x60; URI parameter, and filter them with the &#x60;status&#x60; parameter.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.LoadBalancerActionsApi();
let id = 56; // Number | ID of the Load Balancer
let opts = {
  'sort': "sort_example", // String | Can be used multiple times.
  'status': "status_example" // String | Can be used multiple times, the response will contain only Actions with specified statuses
};
apiInstance.loadBalancersIdActionsGet(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Load Balancer | 
 **sort** | **String**| Can be used multiple times. | [optional] 
 **status** | **String**| Can be used multiple times, the response will contain only Actions with specified statuses | [optional] 

### Return type

[**ActionsResponse**](ActionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## loadBalancersIdActionsRemoveTargetPost

> ActionResponse loadBalancersIdActionsRemoveTargetPost(id, opts)

Remove Target

Removes a target from a Load Balancer.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.LoadBalancerActionsApi();
let id = 56; // Number | ID of the Load Balancer
let opts = {
  'removeTargetRequest': new HetznerCloudApi.RemoveTargetRequest() // RemoveTargetRequest | 
};
apiInstance.loadBalancersIdActionsRemoveTargetPost(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Load Balancer | 
 **removeTargetRequest** | [**RemoveTargetRequest**](RemoveTargetRequest.md)|  | [optional] 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## loadBalancersIdActionsUpdateServicePost

> ActionResponse loadBalancersIdActionsUpdateServicePost(id, opts)

Update Service

Updates a Load Balancer Service.  #### Call specific error codes  | Code                       | Description                                             | |----------------------------|---------------------------------------------------------| | &#x60;source_port_already_used&#x60; | The source port you are trying to add is already in use | 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.LoadBalancerActionsApi();
let id = 56; // Number | ID of the Load Balancer
let opts = {
  'loadBalancerService': new HetznerCloudApi.LoadBalancerService() // LoadBalancerService | 
};
apiInstance.loadBalancersIdActionsUpdateServicePost(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Load Balancer | 
 **loadBalancerService** | [**LoadBalancerService**](LoadBalancerService.md)|  | [optional] 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

