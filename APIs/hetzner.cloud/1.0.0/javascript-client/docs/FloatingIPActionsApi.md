# HetznerCloudApi.FloatingIPActionsApi

All URIs are relative to *https://api.hetzner.cloud/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**floatingIpsIdActionsActionIdGet**](FloatingIPActionsApi.md#floatingIpsIdActionsActionIdGet) | **GET** /floating_ips/{id}/actions/{action_id} | Get an Action for a Floating IP
[**floatingIpsIdActionsAssignPost**](FloatingIPActionsApi.md#floatingIpsIdActionsAssignPost) | **POST** /floating_ips/{id}/actions/assign | Assign a Floating IP to a Server
[**floatingIpsIdActionsChangeDnsPtrPost**](FloatingIPActionsApi.md#floatingIpsIdActionsChangeDnsPtrPost) | **POST** /floating_ips/{id}/actions/change_dns_ptr | Change reverse DNS entry for a Floating IP
[**floatingIpsIdActionsChangeProtectionPost**](FloatingIPActionsApi.md#floatingIpsIdActionsChangeProtectionPost) | **POST** /floating_ips/{id}/actions/change_protection | Change Floating IP Protection
[**floatingIpsIdActionsGet**](FloatingIPActionsApi.md#floatingIpsIdActionsGet) | **GET** /floating_ips/{id}/actions | Get all Actions for a Floating IP
[**floatingIpsIdActionsUnassignPost**](FloatingIPActionsApi.md#floatingIpsIdActionsUnassignPost) | **POST** /floating_ips/{id}/actions/unassign | Unassign a Floating IP



## floatingIpsIdActionsActionIdGet

> ActionResponse floatingIpsIdActionsActionIdGet(id, actionId)

Get an Action for a Floating IP

Returns a specific Action object for a Floating IP.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.FloatingIPActionsApi();
let id = 56; // Number | ID of the Floating IP
let actionId = 56; // Number | ID of the Action
apiInstance.floatingIpsIdActionsActionIdGet(id, actionId, (error, data, response) => {
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
 **id** | **Number**| ID of the Floating IP | 
 **actionId** | **Number**| ID of the Action | 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## floatingIpsIdActionsAssignPost

> ActionResponse floatingIpsIdActionsAssignPost(id, opts)

Assign a Floating IP to a Server

Assigns a Floating IP to a Server.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.FloatingIPActionsApi();
let id = 56; // Number | ID of the Floating IP
let opts = {
  'assignFloatingIPRequest': new HetznerCloudApi.AssignFloatingIPRequest() // AssignFloatingIPRequest | 
};
apiInstance.floatingIpsIdActionsAssignPost(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Floating IP | 
 **assignFloatingIPRequest** | [**AssignFloatingIPRequest**](AssignFloatingIPRequest.md)|  | [optional] 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## floatingIpsIdActionsChangeDnsPtrPost

> ActionResponse floatingIpsIdActionsChangeDnsPtrPost(id, opts)

Change reverse DNS entry for a Floating IP

Changes the hostname that will appear when getting the hostname belonging to this Floating IP.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.FloatingIPActionsApi();
let id = 56; // Number | ID of the Floating IP
let opts = {
  'changeDNSPTRRequest': new HetznerCloudApi.ChangeDNSPTRRequest() // ChangeDNSPTRRequest | Select the IP address for which to change the DNS entry by passing `ip`. For a Floating IP of type `ipv4` this must exactly match the IP address of the Floating IP. For a Floating IP of type `ipv6` this must be a single IP within the IPv6 /64 range that belongs to this Floating IP. You can add up to 100 IPv6 reverse DNS entries.  The target hostname is set by passing `dns_ptr`. 
};
apiInstance.floatingIpsIdActionsChangeDnsPtrPost(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Floating IP | 
 **changeDNSPTRRequest** | [**ChangeDNSPTRRequest**](ChangeDNSPTRRequest.md)| Select the IP address for which to change the DNS entry by passing &#x60;ip&#x60;. For a Floating IP of type &#x60;ipv4&#x60; this must exactly match the IP address of the Floating IP. For a Floating IP of type &#x60;ipv6&#x60; this must be a single IP within the IPv6 /64 range that belongs to this Floating IP. You can add up to 100 IPv6 reverse DNS entries.  The target hostname is set by passing &#x60;dns_ptr&#x60;.  | [optional] 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## floatingIpsIdActionsChangeProtectionPost

> ActionResponse floatingIpsIdActionsChangeProtectionPost(id, opts)

Change Floating IP Protection

Changes the protection configuration of the Floating IP.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.FloatingIPActionsApi();
let id = 56; // Number | ID of the Floating IP
let opts = {
  'changeProtectionRequest': new HetznerCloudApi.ChangeProtectionRequest() // ChangeProtectionRequest | 
};
apiInstance.floatingIpsIdActionsChangeProtectionPost(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Floating IP | 
 **changeProtectionRequest** | [**ChangeProtectionRequest**](ChangeProtectionRequest.md)|  | [optional] 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## floatingIpsIdActionsGet

> FloatingIpsIdActionsGet200Response floatingIpsIdActionsGet(id, opts)

Get all Actions for a Floating IP

Returns all Action objects for a Floating IP. You can sort the results by using the &#x60;sort&#x60; URI parameter, and filter them with the &#x60;status&#x60; parameter.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.FloatingIPActionsApi();
let id = 56; // Number | ID of the Floating IP
let opts = {
  'sort': "sort_example", // String | Can be used multiple times.
  'status': "status_example" // String | Can be used multiple times, the response will contain only Actions with specified statuses
};
apiInstance.floatingIpsIdActionsGet(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Floating IP | 
 **sort** | **String**| Can be used multiple times. | [optional] 
 **status** | **String**| Can be used multiple times, the response will contain only Actions with specified statuses | [optional] 

### Return type

[**FloatingIpsIdActionsGet200Response**](FloatingIpsIdActionsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## floatingIpsIdActionsUnassignPost

> ActionResponse floatingIpsIdActionsUnassignPost(id)

Unassign a Floating IP

Unassigns a Floating IP, resulting in it being unreachable. You may assign it to a Server again at a later time.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.FloatingIPActionsApi();
let id = 56; // Number | ID of the Floating IP
apiInstance.floatingIpsIdActionsUnassignPost(id, (error, data, response) => {
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
 **id** | **Number**| ID of the Floating IP | 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

