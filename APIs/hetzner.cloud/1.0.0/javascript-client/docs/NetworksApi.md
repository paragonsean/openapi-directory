# HetznerCloudApi.NetworksApi

All URIs are relative to *https://api.hetzner.cloud/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**networksGet**](NetworksApi.md#networksGet) | **GET** /networks | Get all Networks
[**networksIdDelete**](NetworksApi.md#networksIdDelete) | **DELETE** /networks/{id} | Delete a Network
[**networksIdGet**](NetworksApi.md#networksIdGet) | **GET** /networks/{id} | Get a Network
[**networksIdPut**](NetworksApi.md#networksIdPut) | **PUT** /networks/{id} | Update a Network
[**networksPost**](NetworksApi.md#networksPost) | **POST** /networks | Create a Network



## networksGet

> NetworksGet200Response networksGet(opts)

Get all Networks

Gets all existing networks that you have available.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.NetworksApi();
let opts = {
  'name': "name_example", // String | Can be used to filter networks by their name. The response will only contain the networks matching the specified name.
  'labelSelector': "labelSelector_example" // String | Can be used to filter networks by labels. The response will only contain networks with a matching label selector pattern.
};
apiInstance.networksGet(opts, (error, data, response) => {
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
 **name** | **String**| Can be used to filter networks by their name. The response will only contain the networks matching the specified name. | [optional] 
 **labelSelector** | **String**| Can be used to filter networks by labels. The response will only contain networks with a matching label selector pattern. | [optional] 

### Return type

[**NetworksGet200Response**](NetworksGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## networksIdDelete

> networksIdDelete(id)

Delete a Network

Deletes a network. If there are Servers attached they will be detached in the background.  Note: if the network object changes during the request, the response will be a “conflict” error. 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.NetworksApi();
let id = 56; // Number | ID of the network
apiInstance.networksIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| ID of the network | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## networksIdGet

> NetworksPost201Response networksIdGet(id)

Get a Network

Gets a specific network object.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.NetworksApi();
let id = 56; // Number | ID of the network
apiInstance.networksIdGet(id, (error, data, response) => {
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
 **id** | **Number**| ID of the network | 

### Return type

[**NetworksPost201Response**](NetworksPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## networksIdPut

> NetworksPost201Response networksIdPut(id, opts)

Update a Network

Updates the network properties.  Note that when updating labels, the network’s current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.  Note: if the network object changes during the request, the response will be a “conflict” error. 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.NetworksApi();
let id = 56; // Number | ID of the network
let opts = {
  'updateNetworkRequest': new HetznerCloudApi.UpdateNetworkRequest() // UpdateNetworkRequest | 
};
apiInstance.networksIdPut(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the network | 
 **updateNetworkRequest** | [**UpdateNetworkRequest**](UpdateNetworkRequest.md)|  | [optional] 

### Return type

[**NetworksPost201Response**](NetworksPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## networksPost

> NetworksPost201Response networksPost(opts)

Create a Network

Creates a network with the specified &#x60;ip_range&#x60;.  You may specify one or more &#x60;subnets&#x60;. You can also add more Subnets later by using the [add subnet action](https://docs.hetzner.cloud/#network-actions-add-a-subnet-to-a-network). If you do not specify an &#x60;ip_range&#x60; in the subnet we will automatically pick the first available /24 range for you.  You may specify one or more routes in &#x60;routes&#x60;. You can also add more routes later by using the [add route action](https://docs.hetzner.cloud/#network-actions-add-a-route-to-a-network). 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.NetworksApi();
let opts = {
  'createNetworkRequest': new HetznerCloudApi.CreateNetworkRequest() // CreateNetworkRequest | 
};
apiInstance.networksPost(opts, (error, data, response) => {
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
 **createNetworkRequest** | [**CreateNetworkRequest**](CreateNetworkRequest.md)|  | [optional] 

### Return type

[**NetworksPost201Response**](NetworksPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

