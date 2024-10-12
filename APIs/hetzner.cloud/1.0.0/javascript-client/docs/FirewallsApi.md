# HetznerCloudApi.FirewallsApi

All URIs are relative to *https://api.hetzner.cloud/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**firewallsGet**](FirewallsApi.md#firewallsGet) | **GET** /firewalls | Get all Firewalls
[**firewallsIdDelete**](FirewallsApi.md#firewallsIdDelete) | **DELETE** /firewalls/{id} | Delete a Firewall
[**firewallsIdGet**](FirewallsApi.md#firewallsIdGet) | **GET** /firewalls/{id} | Get a Firewall
[**firewallsIdPut**](FirewallsApi.md#firewallsIdPut) | **PUT** /firewalls/{id} | Update a Firewall
[**firewallsPost**](FirewallsApi.md#firewallsPost) | **POST** /firewalls | Create a Firewall



## firewallsGet

> FirewallsResponse firewallsGet(opts)

Get all Firewalls

Returns all Firewall objects.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.FirewallsApi();
let opts = {
  'sort': "sort_example", // String | Can be used multiple times.
  'name': "name_example", // String | Can be used to filter resources by their name. The response will only contain the resources matching the specified name
  'labelSelector': "labelSelector_example" // String | Can be used to filter resources by labels. The response will only contain resources matching the label selector.
};
apiInstance.firewallsGet(opts, (error, data, response) => {
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
 **sort** | **String**| Can be used multiple times. | [optional] 
 **name** | **String**| Can be used to filter resources by their name. The response will only contain the resources matching the specified name | [optional] 
 **labelSelector** | **String**| Can be used to filter resources by labels. The response will only contain resources matching the label selector. | [optional] 

### Return type

[**FirewallsResponse**](FirewallsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## firewallsIdDelete

> firewallsIdDelete(id)

Delete a Firewall

Deletes a Firewall.  #### Call specific error codes  | Code                 | Description                               | |--------------------- |-------------------------------------------| | &#x60;resource_in_use&#x60;    | Firewall must not be in use to be deleted | 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.FirewallsApi();
let id = 56; // Number | ID of the resource
apiInstance.firewallsIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| ID of the resource | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## firewallsIdGet

> FirewallResponse firewallsIdGet(id)

Get a Firewall

Gets a specific Firewall object.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.FirewallsApi();
let id = 56; // Number | ID of the resource
apiInstance.firewallsIdGet(id, (error, data, response) => {
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
 **id** | **Number**| ID of the resource | 

### Return type

[**FirewallResponse**](FirewallResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## firewallsIdPut

> FirewallResponse firewallsIdPut(id, opts)

Update a Firewall

Updates the Firewall.  Note that when updating labels, the Firewall&#39;s current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.  Note: if the Firewall object changes during the request, the response will be a “conflict” error. 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.FirewallsApi();
let id = 56; // Number | ID of the resource
let opts = {
  'updateFirewallRequest': new HetznerCloudApi.UpdateFirewallRequest() // UpdateFirewallRequest | 
};
apiInstance.firewallsIdPut(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the resource | 
 **updateFirewallRequest** | [**UpdateFirewallRequest**](UpdateFirewallRequest.md)|  | [optional] 

### Return type

[**FirewallResponse**](FirewallResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## firewallsPost

> CreateFirewallResponse firewallsPost(opts)

Create a Firewall

Creates a new Firewall.  #### Call specific error codes  | Code                          | Description                                                   | |------------------------------ |-------------------------------------------------------------- | | &#x60;server_already_added&#x60;        | Server added more than one time to resource                   | | &#x60;incompatible_network_type&#x60;   | The Network type is incompatible for the given resource       | | &#x60;firewall_resource_not_found&#x60; | The resource the Firewall should be attached to was not found | 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.FirewallsApi();
let opts = {
  'createFirewallRequest': {"apply_to":[{"server":{"id":42},"type":"server"}],"labels":{"env":"dev"},"name":"Corporate Intranet Protection","rules":[{"description":"Allow port 80","direction":"in","port":"80","protocol":"tcp","source_ips":["28.239.13.1/32","28.239.14.0/24","ff21:1eac:9a3b:ee58:5ca:990c:8bc9:c03b/128"]}]} // CreateFirewallRequest | 
};
apiInstance.firewallsPost(opts, (error, data, response) => {
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
 **createFirewallRequest** | [**CreateFirewallRequest**](CreateFirewallRequest.md)|  | [optional] 

### Return type

[**CreateFirewallResponse**](CreateFirewallResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

