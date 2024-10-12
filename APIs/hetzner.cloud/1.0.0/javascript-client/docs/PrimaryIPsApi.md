# HetznerCloudApi.PrimaryIPsApi

All URIs are relative to *https://api.hetzner.cloud/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**primaryIpsGet**](PrimaryIPsApi.md#primaryIpsGet) | **GET** /primary_ips | Get all Primary IPs
[**primaryIpsIdDelete**](PrimaryIPsApi.md#primaryIpsIdDelete) | **DELETE** /primary_ips/{id} | Delete a Primary IP
[**primaryIpsIdGet**](PrimaryIPsApi.md#primaryIpsIdGet) | **GET** /primary_ips/{id} | Get a Primary IP
[**primaryIpsIdPut**](PrimaryIPsApi.md#primaryIpsIdPut) | **PUT** /primary_ips/{id} | Update a Primary IP
[**primaryIpsPost**](PrimaryIPsApi.md#primaryIpsPost) | **POST** /primary_ips | Create a Primary IP



## primaryIpsGet

> PrimaryIPsResponse primaryIpsGet(opts)

Get all Primary IPs

Returns all Primary IP objects.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.PrimaryIPsApi();
let opts = {
  'name': "name_example", // String | Can be used to filter resources by their name. The response will only contain the resources matching the specified name
  'labelSelector': "labelSelector_example", // String | Can be used to filter resources by labels. The response will only contain resources matching the label selector.
  'ip': "127.0.0.1", // String | Can be used to filter resources by their ip. The response will only contain the resources matching the specified ip.
  'sort': "sort_example" // String | Can be used multiple times. Choices id id:asc id:desc created created:asc created:desc
};
apiInstance.primaryIpsGet(opts, (error, data, response) => {
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
 **name** | **String**| Can be used to filter resources by their name. The response will only contain the resources matching the specified name | [optional] 
 **labelSelector** | **String**| Can be used to filter resources by labels. The response will only contain resources matching the label selector. | [optional] 
 **ip** | **String**| Can be used to filter resources by their ip. The response will only contain the resources matching the specified ip. | [optional] 
 **sort** | **String**| Can be used multiple times. Choices id id:asc id:desc created created:asc created:desc | [optional] 

### Return type

[**PrimaryIPsResponse**](PrimaryIPsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## primaryIpsIdDelete

> primaryIpsIdDelete(id)

Delete a Primary IP

Deletes a Primary IP.  The Primary IP may be assigned to a Server. In this case it is unassigned automatically. The Server must be powered off (status &#x60;off&#x60;) in order for this operation to succeed. 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.PrimaryIPsApi();
let id = 56; // Number | ID of the resource
apiInstance.primaryIpsIdDelete(id, (error, data, response) => {
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


## primaryIpsIdGet

> PrimaryIPResponse primaryIpsIdGet(id)

Get a Primary IP

Returns a specific Primary IP object.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.PrimaryIPsApi();
let id = 56; // Number | ID of the resource
apiInstance.primaryIpsIdGet(id, (error, data, response) => {
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

[**PrimaryIPResponse**](PrimaryIPResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## primaryIpsIdPut

> PrimaryIPResponse primaryIpsIdPut(id, opts)

Update a Primary IP

Updates the Primary IP.  Note that when updating labels, the Primary IP&#39;s current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.  If the Primary IP object changes during the request, the response will be a “conflict” error. 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.PrimaryIPsApi();
let id = 56; // Number | ID of the resource
let opts = {
  'updatePrimaryIPRequest': new HetznerCloudApi.UpdatePrimaryIPRequest() // UpdatePrimaryIPRequest | 
};
apiInstance.primaryIpsIdPut(id, opts, (error, data, response) => {
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
 **updatePrimaryIPRequest** | [**UpdatePrimaryIPRequest**](UpdatePrimaryIPRequest.md)|  | [optional] 

### Return type

[**PrimaryIPResponse**](PrimaryIPResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## primaryIpsPost

> CreatePrimaryIPResponse primaryIpsPost(opts)

Create a Primary IP

Creates a new Primary IP, optionally assigned to a Server.  If you want to create a Primary IP that is not assigned to a Server, you need to provide the &#x60;datacenter&#x60; key instead of &#x60;assignee_id&#x60;. This can be either the ID or the name of the Datacenter this Primary IP shall be created in.  Note that a Primary IP can only be assigned to a Server in the same Datacenter later on.  #### Call specific error codes  | Code                          | Description                                                   | |------------------------------ |-------------------------------------------------------------- | | &#x60;server_not_stopped&#x60;          | The specified server is running, but needs to be powered off  | | &#x60;server_has_ipv4&#x60;             | The server already has an ipv4 address                        | | &#x60;server_has_ipv6&#x60;             | The server already has an ipv6 address                        | 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.PrimaryIPsApi();
let opts = {
  'createPrimaryIPRequest': new HetznerCloudApi.CreatePrimaryIPRequest() // CreatePrimaryIPRequest | The `type` argument is required while `datacenter` and `assignee_id` are mutually exclusive.
};
apiInstance.primaryIpsPost(opts, (error, data, response) => {
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
 **createPrimaryIPRequest** | [**CreatePrimaryIPRequest**](CreatePrimaryIPRequest.md)| The &#x60;type&#x60; argument is required while &#x60;datacenter&#x60; and &#x60;assignee_id&#x60; are mutually exclusive. | [optional] 

### Return type

[**CreatePrimaryIPResponse**](CreatePrimaryIPResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

