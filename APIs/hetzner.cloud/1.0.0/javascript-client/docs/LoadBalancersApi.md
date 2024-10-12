# HetznerCloudApi.LoadBalancersApi

All URIs are relative to *https://api.hetzner.cloud/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**loadBalancersGet**](LoadBalancersApi.md#loadBalancersGet) | **GET** /load_balancers | Get all Load Balancers
[**loadBalancersIdDelete**](LoadBalancersApi.md#loadBalancersIdDelete) | **DELETE** /load_balancers/{id} | Delete a Load Balancer
[**loadBalancersIdGet**](LoadBalancersApi.md#loadBalancersIdGet) | **GET** /load_balancers/{id} | Get a Load Balancer
[**loadBalancersIdMetricsGet**](LoadBalancersApi.md#loadBalancersIdMetricsGet) | **GET** /load_balancers/{id}/metrics | Get Metrics for a LoadBalancer
[**loadBalancersIdPut**](LoadBalancersApi.md#loadBalancersIdPut) | **PUT** /load_balancers/{id} | Update a Load Balancer
[**loadBalancersPost**](LoadBalancersApi.md#loadBalancersPost) | **POST** /load_balancers | Create a Load Balancer



## loadBalancersGet

> LoadBalancersGet200Response loadBalancersGet(opts)

Get all Load Balancers

Gets all existing Load Balancers that you have available.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.LoadBalancersApi();
let opts = {
  'sort': "sort_example", // String | Can be used multiple times.
  'name': "name_example", // String | Can be used to filter resources by their name. The response will only contain the resources matching the specified name
  'labelSelector': "labelSelector_example" // String | Can be used to filter resources by labels. The response will only contain resources matching the label selector.
};
apiInstance.loadBalancersGet(opts, (error, data, response) => {
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

[**LoadBalancersGet200Response**](LoadBalancersGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## loadBalancersIdDelete

> loadBalancersIdDelete(id)

Delete a Load Balancer

Deletes a Load Balancer.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.LoadBalancersApi();
let id = 56; // Number | ID of the Load Balancer
apiInstance.loadBalancersIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| ID of the Load Balancer | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## loadBalancersIdGet

> LoadBalancersIdGet200Response loadBalancersIdGet(id)

Get a Load Balancer

Gets a specific Load Balancer object.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.LoadBalancersApi();
let id = 56; // Number | ID of the Load Balancer
apiInstance.loadBalancersIdGet(id, (error, data, response) => {
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

[**LoadBalancersIdGet200Response**](LoadBalancersIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## loadBalancersIdMetricsGet

> LoadBalancersIdMetricsGet200Response loadBalancersIdMetricsGet(id, type, start, end, opts)

Get Metrics for a LoadBalancer

You must specify the type of metric to get: &#x60;open_connections&#x60;, &#x60;connections_per_second&#x60;, &#x60;requests_per_second&#x60; or &#x60;bandwidth&#x60;. You can also specify more than one type by comma separation, e.g. &#x60;requests_per_second,bandwidth&#x60;.  Depending on the type you will get different time series data:  |Type | Timeseries | Unit | Description | |---- |------------|------|-------------| | open_connections | open_connections | number | Open connections | | connections_per_second | connections_per_second | connections/s | Connections per second | | requests_per_second | requests_per_second | requests/s | Requests per second | | bandwidth | bandwidth.in | bytes/s | Ingress bandwidth | || bandwidth.out | bytes/s | Egress bandwidth |  Metrics are available for the last 30 days only.  If you do not provide the step argument we will automatically adjust it so that 200 samples are returned.  We limit the number of samples to a maximum of 500 and will adjust the step parameter accordingly. 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.LoadBalancersApi();
let id = 56; // Number | ID of the Load Balancer
let type = "type_example"; // String | Type of metrics to get
let start = "start_example"; // String | Start of period to get Metrics for (in ISO-8601 format)
let end = "end_example"; // String | End of period to get Metrics for (in ISO-8601 format)
let opts = {
  'step': "step_example" // String | Resolution of results in seconds
};
apiInstance.loadBalancersIdMetricsGet(id, type, start, end, opts, (error, data, response) => {
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
 **type** | **String**| Type of metrics to get | 
 **start** | **String**| Start of period to get Metrics for (in ISO-8601 format) | 
 **end** | **String**| End of period to get Metrics for (in ISO-8601 format) | 
 **step** | **String**| Resolution of results in seconds | [optional] 

### Return type

[**LoadBalancersIdMetricsGet200Response**](LoadBalancersIdMetricsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## loadBalancersIdPut

> LoadBalancersIdGet200Response loadBalancersIdPut(id, opts)

Update a Load Balancer

Updates a Load Balancer. You can update a Load Balancer’s name and a Load Balancer’s labels.  Note that when updating labels, the Load Balancer’s current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.  Note: if the Load Balancer object changes during the request, the response will be a “conflict” error. 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.LoadBalancersApi();
let id = 56; // Number | ID of the Load Balancer
let opts = {
  'loadBalancersIdPutRequest': new HetznerCloudApi.LoadBalancersIdPutRequest() // LoadBalancersIdPutRequest | 
};
apiInstance.loadBalancersIdPut(id, opts, (error, data, response) => {
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
 **loadBalancersIdPutRequest** | [**LoadBalancersIdPutRequest**](LoadBalancersIdPutRequest.md)|  | [optional] 

### Return type

[**LoadBalancersIdGet200Response**](LoadBalancersIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## loadBalancersPost

> LoadBalancersPost201Response loadBalancersPost(opts)

Create a Load Balancer

Creates a Load Balancer.  #### Call specific error codes  | Code                                    | Description                                                                                           | |-----------------------------------------|-------------------------------------------------------------------------------------------------------| | &#x60;cloud_resource_ip_not_allowed&#x60;         | The IP you are trying to add as a target belongs to a Hetzner Cloud resource                          | | &#x60;ip_not_owned&#x60;                          | The IP is not owned by the owner of the project of the Load Balancer                                  | | &#x60;load_balancer_not_attached_to_network&#x60; | The Load Balancer is not attached to a network                                                        | | &#x60;robot_unavailable&#x60;                     | Robot was not available. The caller may retry the operation after a short delay.                      | | &#x60;server_not_attached_to_network&#x60;        | The server you are trying to add as a target is not attached to the same network as the Load Balancer | | &#x60;source_port_already_used&#x60;              | The source port you are trying to add is already in use                                               | | &#x60;target_already_defined&#x60;                | The Load Balancer target you are trying to define is already defined                                  | 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.LoadBalancersApi();
let opts = {
  'createLoadBalancerRequest': new HetznerCloudApi.CreateLoadBalancerRequest() // CreateLoadBalancerRequest | 
};
apiInstance.loadBalancersPost(opts, (error, data, response) => {
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
 **createLoadBalancerRequest** | [**CreateLoadBalancerRequest**](CreateLoadBalancerRequest.md)|  | [optional] 

### Return type

[**LoadBalancersPost201Response**](LoadBalancersPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

