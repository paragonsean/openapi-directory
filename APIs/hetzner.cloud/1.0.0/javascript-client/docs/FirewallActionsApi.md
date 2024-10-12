# HetznerCloudApi.FirewallActionsApi

All URIs are relative to *https://api.hetzner.cloud/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**firewallsIdActionsActionIdGet**](FirewallActionsApi.md#firewallsIdActionsActionIdGet) | **GET** /firewalls/{id}/actions/{action_id} | Get an Action for a Firewall
[**firewallsIdActionsApplyToResourcesPost**](FirewallActionsApi.md#firewallsIdActionsApplyToResourcesPost) | **POST** /firewalls/{id}/actions/apply_to_resources | Apply to Resources
[**firewallsIdActionsGet**](FirewallActionsApi.md#firewallsIdActionsGet) | **GET** /firewalls/{id}/actions | Get all Actions for a Firewall
[**firewallsIdActionsRemoveFromResourcesPost**](FirewallActionsApi.md#firewallsIdActionsRemoveFromResourcesPost) | **POST** /firewalls/{id}/actions/remove_from_resources | Remove from Resources
[**firewallsIdActionsSetRulesPost**](FirewallActionsApi.md#firewallsIdActionsSetRulesPost) | **POST** /firewalls/{id}/actions/set_rules | Set Rules



## firewallsIdActionsActionIdGet

> ActionResponse firewallsIdActionsActionIdGet(id, actionId)

Get an Action for a Firewall

Returns a specific Action for a Firewall.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.FirewallActionsApi();
let id = 56; // Number | ID of the Firewall
let actionId = 56; // Number | ID of the Action
apiInstance.firewallsIdActionsActionIdGet(id, actionId, (error, data, response) => {
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
 **id** | **Number**| ID of the Firewall | 
 **actionId** | **Number**| ID of the Action | 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## firewallsIdActionsApplyToResourcesPost

> ActionsResponse firewallsIdActionsApplyToResourcesPost(id, opts)

Apply to Resources

Applies one Firewall to multiple resources.  Currently servers (public network interface) and label selectors are supported.  #### Call specific error codes  | Code                          | Description                                                   | |-------------------------------|---------------------------------------------------------------| | &#x60;firewall_already_applied&#x60;    | Firewall was already applied on resource                      | | &#x60;incompatible_network_type&#x60;   | The Network type is incompatible for the given resource       | | &#x60;firewall_resource_not_found&#x60; | The resource the Firewall should be attached to was not found | 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.FirewallActionsApi();
let id = 56; // Number | ID of the Firewall
let opts = {
  'applyToResourcesRequest': {"apply_to":[{"server":{"id":42},"type":"server"}]} // ApplyToResourcesRequest | 
};
apiInstance.firewallsIdActionsApplyToResourcesPost(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Firewall | 
 **applyToResourcesRequest** | [**ApplyToResourcesRequest**](ApplyToResourcesRequest.md)|  | [optional] 

### Return type

[**ActionsResponse**](ActionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## firewallsIdActionsGet

> ActionsResponse firewallsIdActionsGet(id, opts)

Get all Actions for a Firewall

Returns all Action objects for a Firewall. You can sort the results by using the &#x60;sort&#x60; URI parameter, and filter them with the &#x60;status&#x60; parameter.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.FirewallActionsApi();
let id = 56; // Number | ID of the Resource
let opts = {
  'sort': "sort_example", // String | Can be used multiple times.
  'status': "status_example" // String | Can be used multiple times, the response will contain only Actions with specified statuses
};
apiInstance.firewallsIdActionsGet(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Resource | 
 **sort** | **String**| Can be used multiple times. | [optional] 
 **status** | **String**| Can be used multiple times, the response will contain only Actions with specified statuses | [optional] 

### Return type

[**ActionsResponse**](ActionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## firewallsIdActionsRemoveFromResourcesPost

> ActionsResponse firewallsIdActionsRemoveFromResourcesPost(id, opts)

Remove from Resources

Removes one Firewall from multiple resources.  Currently only Servers (and their public network interfaces) are supported.  #### Call specific error codes  | Code                                  | Description                                                            | |---------------------------------------|------------------------------------------------------------------------| | &#x60;firewall_already_removed&#x60;            | Firewall was already removed from the resource                         | | &#x60;firewall_resource_not_found&#x60;         | The resource the Firewall should be attached to was not found          | | &#x60;firewall_managed_by_label_selector&#x60;  | Firewall was applied via label selector and cannot be removed manually | 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.FirewallActionsApi();
let id = 56; // Number | ID of the Firewall
let opts = {
  'removeFromResourcesRequest': {"remove_from":[{"server":{"id":42},"type":"server"}]} // RemoveFromResourcesRequest | 
};
apiInstance.firewallsIdActionsRemoveFromResourcesPost(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Firewall | 
 **removeFromResourcesRequest** | [**RemoveFromResourcesRequest**](RemoveFromResourcesRequest.md)|  | [optional] 

### Return type

[**ActionsResponse**](ActionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## firewallsIdActionsSetRulesPost

> ActionsResponse firewallsIdActionsSetRulesPost(id, opts)

Set Rules

Sets the rules of a Firewall.  All existing rules will be overwritten. Pass an empty &#x60;rules&#x60; array to remove all rules. The maximum amount of rules that can be defined is 50.  #### Call specific error codes  | Code                          | Description                                                   | |-------------------------------|---------------------------------------------------------------| | &#x60;firewall_resource_not_found&#x60; | The resource the Firewall should be attached to was not found | 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.FirewallActionsApi();
let id = 56; // Number | ID of the Firewall
let opts = {
  'setRulesRequest': {"rules":[{"description":"Allow port 80","direction":"in","port":"80","protocol":"tcp","source_ips":["28.239.13.1/32","28.239.14.0/24","ff21:1eac:9a3b:ee58:5ca:990c:8bc9:c03b/128"]}]} // SetRulesRequest | 
};
apiInstance.firewallsIdActionsSetRulesPost(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Firewall | 
 **setRulesRequest** | [**SetRulesRequest**](SetRulesRequest.md)|  | [optional] 

### Return type

[**ActionsResponse**](ActionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

