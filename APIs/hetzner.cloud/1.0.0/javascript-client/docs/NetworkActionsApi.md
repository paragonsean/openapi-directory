# HetznerCloudApi.NetworkActionsApi

All URIs are relative to *https://api.hetzner.cloud/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**networksIdActionsActionIdGet**](NetworkActionsApi.md#networksIdActionsActionIdGet) | **GET** /networks/{id}/actions/{action_id} | Get an Action for a Network
[**networksIdActionsAddRoutePost**](NetworkActionsApi.md#networksIdActionsAddRoutePost) | **POST** /networks/{id}/actions/add_route | Add a route to a Network
[**networksIdActionsAddSubnetPost**](NetworkActionsApi.md#networksIdActionsAddSubnetPost) | **POST** /networks/{id}/actions/add_subnet | Add a subnet to a Network
[**networksIdActionsChangeIpRangePost**](NetworkActionsApi.md#networksIdActionsChangeIpRangePost) | **POST** /networks/{id}/actions/change_ip_range | Change IP range of a Network
[**networksIdActionsChangeProtectionPost**](NetworkActionsApi.md#networksIdActionsChangeProtectionPost) | **POST** /networks/{id}/actions/change_protection | Change Network Protection
[**networksIdActionsDeleteRoutePost**](NetworkActionsApi.md#networksIdActionsDeleteRoutePost) | **POST** /networks/{id}/actions/delete_route | Delete a route from a Network
[**networksIdActionsDeleteSubnetPost**](NetworkActionsApi.md#networksIdActionsDeleteSubnetPost) | **POST** /networks/{id}/actions/delete_subnet | Delete a subnet from a Network
[**networksIdActionsGet**](NetworkActionsApi.md#networksIdActionsGet) | **GET** /networks/{id}/actions | Get all Actions for a Network



## networksIdActionsActionIdGet

> ActionResponse networksIdActionsActionIdGet(id, actionId)

Get an Action for a Network

Returns a specific Action for a Network.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.NetworkActionsApi();
let id = 56; // Number | ID of the Network
let actionId = 56; // Number | ID of the Action
apiInstance.networksIdActionsActionIdGet(id, actionId, (error, data, response) => {
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
 **id** | **Number**| ID of the Network | 
 **actionId** | **Number**| ID of the Action | 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## networksIdActionsAddRoutePost

> ActionResponse networksIdActionsAddRoutePost(id, opts)

Add a route to a Network

Adds a route entry to a Network.  Note: if the Network object changes during the request, the response will be a “conflict” error. 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.NetworkActionsApi();
let id = 56; // Number | ID of the Network
let opts = {
  'addDeleteRouteRequest': new HetznerCloudApi.AddDeleteRouteRequest() // AddDeleteRouteRequest | 
};
apiInstance.networksIdActionsAddRoutePost(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Network | 
 **addDeleteRouteRequest** | [**AddDeleteRouteRequest**](AddDeleteRouteRequest.md)|  | [optional] 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## networksIdActionsAddSubnetPost

> ActionResponse networksIdActionsAddSubnetPost(id, opts)

Add a subnet to a Network

Adds a new subnet object to the Network. If you do not specify an &#x60;ip_range&#x60; for the subnet we will automatically pick the first available /24 range for you if possible.  Note: if the parent Network object changes during the request, the response will be a “conflict” error. 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.NetworkActionsApi();
let id = 56; // Number | ID of the Network
let opts = {
  'addSubnetRequest': new HetznerCloudApi.AddSubnetRequest() // AddSubnetRequest | 
};
apiInstance.networksIdActionsAddSubnetPost(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Network | 
 **addSubnetRequest** | [**AddSubnetRequest**](AddSubnetRequest.md)|  | [optional] 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## networksIdActionsChangeIpRangePost

> ActionResponse networksIdActionsChangeIpRangePost(id, opts)

Change IP range of a Network

Changes the IP range of a Network. IP ranges can only be extended and never shrunk. You can only add IPs at the end of an existing IP range. This means that the IP part of your existing range must stay the same and you can only change its netmask.  For example if you have a range &#x60;10.0.0.0/16&#x60; you want to extend then your new range must also start with the IP &#x60;10.0.0.0&#x60;. Your CIDR netmask &#x60;/16&#x60; may change to a number that is smaller than &#x60;16&#x60; thereby increasing the IP range. So valid entries would be &#x60;10.0.0.0/15&#x60;, &#x60;10.0.0.0/14&#x60;, &#x60;10.0.0.0/13&#x60; and so on.  After changing the IP range you will have to adjust the routes on your connected Servers by either rebooting them or manually changing the routes to your private Network interface.  Note: if the Network object changes during the request, the response will be a “conflict” error. 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.NetworkActionsApi();
let id = 56; // Number | ID of the Network
let opts = {
  'changeIPRangeRequest': new HetznerCloudApi.ChangeIPRangeRequest() // ChangeIPRangeRequest | 
};
apiInstance.networksIdActionsChangeIpRangePost(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Network | 
 **changeIPRangeRequest** | [**ChangeIPRangeRequest**](ChangeIPRangeRequest.md)|  | [optional] 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## networksIdActionsChangeProtectionPost

> ActionResponse networksIdActionsChangeProtectionPost(id, opts)

Change Network Protection

Changes the protection configuration of a Network.  Note: if the Network object changes during the request, the response will be a “conflict” error. 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.NetworkActionsApi();
let id = 56; // Number | ID of the Network
let opts = {
  'changeProtectionRequest1': new HetznerCloudApi.ChangeProtectionRequest1() // ChangeProtectionRequest1 | 
};
apiInstance.networksIdActionsChangeProtectionPost(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Network | 
 **changeProtectionRequest1** | [**ChangeProtectionRequest1**](ChangeProtectionRequest1.md)|  | [optional] 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## networksIdActionsDeleteRoutePost

> ActionResponse networksIdActionsDeleteRoutePost(id, opts)

Delete a route from a Network

Delete a route entry from a Network.  Note: if the Network object changes during the request, the response will be a “conflict” error. 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.NetworkActionsApi();
let id = 56; // Number | ID of the Network
let opts = {
  'addDeleteRouteRequest': new HetznerCloudApi.AddDeleteRouteRequest() // AddDeleteRouteRequest | 
};
apiInstance.networksIdActionsDeleteRoutePost(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Network | 
 **addDeleteRouteRequest** | [**AddDeleteRouteRequest**](AddDeleteRouteRequest.md)|  | [optional] 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## networksIdActionsDeleteSubnetPost

> ActionResponse networksIdActionsDeleteSubnetPost(id, opts)

Delete a subnet from a Network

Deletes a single subnet entry from a Network. You cannot delete subnets which still have Servers attached. If you have Servers attached you first need to detach all Servers that use IPs from this subnet before you can delete the subnet.  Note: if the Network object changes during the request, the response will be a “conflict” error. 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.NetworkActionsApi();
let id = 56; // Number | ID of the Network
let opts = {
  'deleteSubnetRequest': new HetznerCloudApi.DeleteSubnetRequest() // DeleteSubnetRequest | 
};
apiInstance.networksIdActionsDeleteSubnetPost(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Network | 
 **deleteSubnetRequest** | [**DeleteSubnetRequest**](DeleteSubnetRequest.md)|  | [optional] 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## networksIdActionsGet

> ActionsResponse networksIdActionsGet(id, opts)

Get all Actions for a Network

Returns all Action objects for a Network. You can sort the results by using the &#x60;sort&#x60; URI parameter, and filter them with the &#x60;status&#x60; parameter.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.NetworkActionsApi();
let id = 56; // Number | ID of the Network
let opts = {
  'sort': "sort_example", // String | Can be used multiple times.
  'status': "status_example" // String | Can be used multiple times, the response will contain only Actions with specified statuses
};
apiInstance.networksIdActionsGet(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Network | 
 **sort** | **String**| Can be used multiple times. | [optional] 
 **status** | **String**| Can be used multiple times, the response will contain only Actions with specified statuses | [optional] 

### Return type

[**ActionsResponse**](ActionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

