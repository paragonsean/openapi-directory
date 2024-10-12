# HetznerCloudApi.ServersApi

All URIs are relative to *https://api.hetzner.cloud/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**serversGet**](ServersApi.md#serversGet) | **GET** /servers | Get all Servers
[**serversIdDelete**](ServersApi.md#serversIdDelete) | **DELETE** /servers/{id} | Delete a Server
[**serversIdGet**](ServersApi.md#serversIdGet) | **GET** /servers/{id} | Get a Server
[**serversIdMetricsGet**](ServersApi.md#serversIdMetricsGet) | **GET** /servers/{id}/metrics | Get Metrics for a Server
[**serversIdPut**](ServersApi.md#serversIdPut) | **PUT** /servers/{id} | Update a Server
[**serversPost**](ServersApi.md#serversPost) | **POST** /servers | Create a Server



## serversGet

> ServersGet200Response serversGet(opts)

Get all Servers

Returns all existing Server objects

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.ServersApi();
let opts = {
  'name': "name_example", // String | Can be used to filter resources by their name. The response will only contain the resources matching the specified name
  'labelSelector': "labelSelector_example", // String | Can be used to filter resources by labels. The response will only contain resources matching the label selector.
  'sort': "sort_example", // String | Can be used multiple times.
  'status': "status_example" // String | Can be used multiple times. The response will only contain Server matching the status
};
apiInstance.serversGet(opts, (error, data, response) => {
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
 **sort** | **String**| Can be used multiple times. | [optional] 
 **status** | **String**| Can be used multiple times. The response will only contain Server matching the status | [optional] 

### Return type

[**ServersGet200Response**](ServersGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serversIdDelete

> ServersIdDelete200Response serversIdDelete(id)

Delete a Server

Deletes a Server. This immediately removes the Server from your account, and it is no longer accessible.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.ServersApi();
let id = 56; // Number | ID of the Server
apiInstance.serversIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| ID of the Server | 

### Return type

[**ServersIdDelete200Response**](ServersIdDelete200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serversIdGet

> ServersIdGet200Response serversIdGet(id)

Get a Server

Returns a specific Server object. The Server must exist inside the Project

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.ServersApi();
let id = 56; // Number | ID of the Server
apiInstance.serversIdGet(id, (error, data, response) => {
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
 **id** | **Number**| ID of the Server | 

### Return type

[**ServersIdGet200Response**](ServersIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serversIdMetricsGet

> LoadBalancersIdMetricsGet200Response serversIdMetricsGet(id, type, start, end, opts)

Get Metrics for a Server

Get Metrics for specified Server.  You must specify the type of metric to get: cpu, disk or network. You can also specify more than one type by comma separation, e.g. cpu,disk.  Depending on the type you will get different time series data  | Type    | Timeseries              | Unit      | Description                                          | |---------|-------------------------|-----------|------------------------------------------------------| | cpu     | cpu                     | percent   | Percent CPU usage                                    | | disk    | disk.0.iops.read        | iop/s     | Number of read IO operations per second              | |         | disk.0.iops.write       | iop/s     | Number of write IO operations per second             | |         | disk.0.bandwidth.read   | bytes/s   | Bytes read per second                                | |         | disk.0.bandwidth.write  | bytes/s   | Bytes written per second                             | | network | network.0.pps.in        | packets/s | Public Network interface packets per second received | |         | network.0.pps.out       | packets/s | Public Network interface packets per second sent     | |         | network.0.bandwidth.in  | bytes/s   | Public Network interface bytes/s received            | |         | network.0.bandwidth.out | bytes/s   | Public Network interface bytes/s sent                |  Metrics are available for the last 30 days only.  If you do not provide the step argument we will automatically adjust it so that a maximum of 200 samples are returned.  We limit the number of samples returned to a maximum of 500 and will adjust the step parameter accordingly. 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.ServersApi();
let id = 56; // Number | ID of the Server
let type = "type_example"; // String | Type of metrics to get
let start = "start_example"; // String | Start of period to get Metrics for (in ISO-8601 format)
let end = "end_example"; // String | End of period to get Metrics for (in ISO-8601 format)
let opts = {
  'step': "step_example" // String | Resolution of results in seconds
};
apiInstance.serversIdMetricsGet(id, type, start, end, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Server | 
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


## serversIdPut

> ServersIdGet200Response serversIdPut(id, opts)

Update a Server

Updates a Server. You can update a Server’s name and a Server’s labels. Please note that Server names must be unique per Project and valid hostnames as per RFC 1123 (i.e. may only contain letters, digits, periods, and dashes). Also note that when updating labels, the Server’s current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.ServersApi();
let id = 56; // Number | ID of the Server
let opts = {
  'updateServerRequest': new HetznerCloudApi.UpdateServerRequest() // UpdateServerRequest | 
};
apiInstance.serversIdPut(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Server | 
 **updateServerRequest** | [**UpdateServerRequest**](UpdateServerRequest.md)|  | [optional] 

### Return type

[**ServersIdGet200Response**](ServersIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## serversPost

> CreateServerResponse serversPost(opts)

Create a Server

Creates a new Server. Returns preliminary information about the Server as well as an Action that covers progress of creation.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.ServersApi();
let opts = {
  'createServerRequest': new HetznerCloudApi.CreateServerRequest() // CreateServerRequest | Please note that Server names must be unique per Project and valid hostnames as per RFC 1123 (i.e. may only contain letters, digits, periods, and dashes).  For `server_type` you can either use the ID as listed in `/server_types` or its name.  For `image` you can either use the ID as listed in `/images` or its name.  If you want to create the Server in a Location, you must set `location` to the ID or name as listed in `/locations`. This is the recommended way. You can be even more specific by setting `datacenter` to the ID or name as listed in `/datacenters`. However we only recommend this if you want to assign a specific Primary IP to the Server which is located in the specified Datacenter.  Some properties like `start_after_create` or `automount` will trigger Actions after the Server is created. Those Actions are listed in the `next_actions` field in the response.  For accessing your Server we strongly recommend to use SSH keys by passing the respective key IDs in `ssh_keys`. If you do not specify any `ssh_keys` we will generate a root password for you and return it in the response.  Please note that provided user-data is stored in our systems. While we take measures to protect it we highly recommend that you don’t use it to store passwords or other sensitive information.  #### Call specific error codes  | Code                             | Description                                                | |----------------------------------|------------------------------------------------------------| | `placement_error`                | An error during the placement occurred                     | | `primary_ip_assigned`            | The specified Primary IP is already assigned to a server   | | `primary_ip_datacenter_mismatch` | The specified Primary IP is in a different datacenter      | | `primary_ip_version_mismatch`    | The specified Primary IP has the wrong IP Version          | 
};
apiInstance.serversPost(opts, (error, data, response) => {
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
 **createServerRequest** | [**CreateServerRequest**](CreateServerRequest.md)| Please note that Server names must be unique per Project and valid hostnames as per RFC 1123 (i.e. may only contain letters, digits, periods, and dashes).  For &#x60;server_type&#x60; you can either use the ID as listed in &#x60;/server_types&#x60; or its name.  For &#x60;image&#x60; you can either use the ID as listed in &#x60;/images&#x60; or its name.  If you want to create the Server in a Location, you must set &#x60;location&#x60; to the ID or name as listed in &#x60;/locations&#x60;. This is the recommended way. You can be even more specific by setting &#x60;datacenter&#x60; to the ID or name as listed in &#x60;/datacenters&#x60;. However we only recommend this if you want to assign a specific Primary IP to the Server which is located in the specified Datacenter.  Some properties like &#x60;start_after_create&#x60; or &#x60;automount&#x60; will trigger Actions after the Server is created. Those Actions are listed in the &#x60;next_actions&#x60; field in the response.  For accessing your Server we strongly recommend to use SSH keys by passing the respective key IDs in &#x60;ssh_keys&#x60;. If you do not specify any &#x60;ssh_keys&#x60; we will generate a root password for you and return it in the response.  Please note that provided user-data is stored in our systems. While we take measures to protect it we highly recommend that you don’t use it to store passwords or other sensitive information.  #### Call specific error codes  | Code                             | Description                                                | |----------------------------------|------------------------------------------------------------| | &#x60;placement_error&#x60;                | An error during the placement occurred                     | | &#x60;primary_ip_assigned&#x60;            | The specified Primary IP is already assigned to a server   | | &#x60;primary_ip_datacenter_mismatch&#x60; | The specified Primary IP is in a different datacenter      | | &#x60;primary_ip_version_mismatch&#x60;    | The specified Primary IP has the wrong IP Version          |  | [optional] 

### Return type

[**CreateServerResponse**](CreateServerResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

