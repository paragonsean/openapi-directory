# HetznerCloudApi.PrimaryIPActionsApi

All URIs are relative to *https://api.hetzner.cloud/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**primaryIpsIdActionsAssignPost**](PrimaryIPActionsApi.md#primaryIpsIdActionsAssignPost) | **POST** /primary_ips/{id}/actions/assign | Assign a Primary IP to a resource
[**primaryIpsIdActionsChangeDnsPtrPost**](PrimaryIPActionsApi.md#primaryIpsIdActionsChangeDnsPtrPost) | **POST** /primary_ips/{id}/actions/change_dns_ptr | Change reverse DNS entry for a Primary IP
[**primaryIpsIdActionsChangeProtectionPost**](PrimaryIPActionsApi.md#primaryIpsIdActionsChangeProtectionPost) | **POST** /primary_ips/{id}/actions/change_protection | Change Primary IP Protection
[**primaryIpsIdActionsUnassignPost**](PrimaryIPActionsApi.md#primaryIpsIdActionsUnassignPost) | **POST** /primary_ips/{id}/actions/unassign | Unassign a Primary IP from a resource



## primaryIpsIdActionsAssignPost

> ActionResponse primaryIpsIdActionsAssignPost(id, opts)

Assign a Primary IP to a resource

Assigns a Primary IP to a Server.  A Server can only have one Primary IP of type &#x60;ipv4&#x60; and one of type &#x60;ipv6&#x60; assigned. If you need more IPs use Floating IPs.  The Server must be powered off (status &#x60;off&#x60;) in order for this operation to succeed.  #### Call specific error codes  | Code                          | Description                                                   | |------------------------------ |-------------------------------------------------------------- | | &#x60;server_not_stopped&#x60;          | The server is running, but needs to be powered off            | | &#x60;primary_ip_already_assigned&#x60; | Primary ip is already assigned to a different server          | | &#x60;server_has_ipv4&#x60;             | The server already has an ipv4 address                        | | &#x60;server_has_ipv6&#x60;             | The server already has an ipv6 address                        | 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.PrimaryIPActionsApi();
let id = 56; // Number | ID of the Primary IP
let opts = {
  'assignPrimaryIPRequest': new HetznerCloudApi.AssignPrimaryIPRequest() // AssignPrimaryIPRequest | 
};
apiInstance.primaryIpsIdActionsAssignPost(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Primary IP | 
 **assignPrimaryIPRequest** | [**AssignPrimaryIPRequest**](AssignPrimaryIPRequest.md)|  | [optional] 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## primaryIpsIdActionsChangeDnsPtrPost

> ActionResponse primaryIpsIdActionsChangeDnsPtrPost(id, opts)

Change reverse DNS entry for a Primary IP

Changes the hostname that will appear when getting the hostname belonging to this Primary IP.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.PrimaryIPActionsApi();
let id = 56; // Number | ID of the Primary IP
let opts = {
  'changeDNSPTRRequest': new HetznerCloudApi.ChangeDNSPTRRequest() // ChangeDNSPTRRequest | Select the IP address for which to change the DNS entry by passing `ip`. For a Primary IP of type `ipv4` this must exactly match the IP address of the Primary IP. For a Primary IP of type `ipv6` this must be a single IP within the IPv6 /64 range that belongs to this Primary IP. You can add up to 100 IPv6 reverse DNS entries.  The target hostname is set by passing `dns_ptr`. 
};
apiInstance.primaryIpsIdActionsChangeDnsPtrPost(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Primary IP | 
 **changeDNSPTRRequest** | [**ChangeDNSPTRRequest**](ChangeDNSPTRRequest.md)| Select the IP address for which to change the DNS entry by passing &#x60;ip&#x60;. For a Primary IP of type &#x60;ipv4&#x60; this must exactly match the IP address of the Primary IP. For a Primary IP of type &#x60;ipv6&#x60; this must be a single IP within the IPv6 /64 range that belongs to this Primary IP. You can add up to 100 IPv6 reverse DNS entries.  The target hostname is set by passing &#x60;dns_ptr&#x60;.  | [optional] 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## primaryIpsIdActionsChangeProtectionPost

> ActionResponse primaryIpsIdActionsChangeProtectionPost(id, opts)

Change Primary IP Protection

Changes the protection configuration of a Primary IP.  A Primary IP can only be delete protected if its &#x60;auto_delete&#x60; property is set to &#x60;false&#x60;. 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.PrimaryIPActionsApi();
let id = 56; // Number | ID of the Primary IP
let opts = {
  'changeProtectionRequest2': new HetznerCloudApi.ChangeProtectionRequest2() // ChangeProtectionRequest2 | 
};
apiInstance.primaryIpsIdActionsChangeProtectionPost(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Primary IP | 
 **changeProtectionRequest2** | [**ChangeProtectionRequest2**](ChangeProtectionRequest2.md)|  | [optional] 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## primaryIpsIdActionsUnassignPost

> ActionResponse primaryIpsIdActionsUnassignPost(id)

Unassign a Primary IP from a resource

Unassigns a Primary IP from a Server.  The Server must be powered off (status &#x60;off&#x60;) in order for this operation to succeed.  Note that only Servers that have at least one network interface (public or private) attached can be powered on.  #### Call specific error codes  | Code                              | Description                                                   | |---------------------------------- |-------------------------------------------------------------- | | &#x60;server_not_stopped&#x60;              | The server is running, but needs to be powered off            | | &#x60;server_is_load_balancer_target&#x60;  | The server ipv4 address is a loadbalancer target              | 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.PrimaryIPActionsApi();
let id = 56; // Number | ID of the Primary IP
apiInstance.primaryIpsIdActionsUnassignPost(id, (error, data, response) => {
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
 **id** | **Number**| ID of the Primary IP | 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

