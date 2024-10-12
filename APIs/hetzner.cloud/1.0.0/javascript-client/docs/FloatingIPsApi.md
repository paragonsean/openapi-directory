# HetznerCloudApi.FloatingIPsApi

All URIs are relative to *https://api.hetzner.cloud/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**floatingIpsGet**](FloatingIPsApi.md#floatingIpsGet) | **GET** /floating_ips | Get all Floating IPs
[**floatingIpsIdDelete**](FloatingIPsApi.md#floatingIpsIdDelete) | **DELETE** /floating_ips/{id} | Delete a Floating IP
[**floatingIpsIdGet**](FloatingIPsApi.md#floatingIpsIdGet) | **GET** /floating_ips/{id} | Get a Floating IP
[**floatingIpsIdPut**](FloatingIPsApi.md#floatingIpsIdPut) | **PUT** /floating_ips/{id} | Update a Floating IP
[**floatingIpsPost**](FloatingIPsApi.md#floatingIpsPost) | **POST** /floating_ips | Create a Floating IP



## floatingIpsGet

> FloatingIpsGet200Response floatingIpsGet(opts)

Get all Floating IPs

Returns all Floating IP objects.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.FloatingIPsApi();
let opts = {
  'name': "name_example", // String | Can be used to filter Floating IPs by their name. The response will only contain the Floating IP matching the specified name.
  'labelSelector': "labelSelector_example", // String | Can be used to filter Floating IPs by labels. The response will only contain Floating IPs matching the label selector.
  'sort': "sort_example" // String | Can be used multiple times. Choices id id:asc id:desc created created:asc created:desc
};
apiInstance.floatingIpsGet(opts, (error, data, response) => {
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
 **name** | **String**| Can be used to filter Floating IPs by their name. The response will only contain the Floating IP matching the specified name. | [optional] 
 **labelSelector** | **String**| Can be used to filter Floating IPs by labels. The response will only contain Floating IPs matching the label selector. | [optional] 
 **sort** | **String**| Can be used multiple times. Choices id id:asc id:desc created created:asc created:desc | [optional] 

### Return type

[**FloatingIpsGet200Response**](FloatingIpsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## floatingIpsIdDelete

> floatingIpsIdDelete(id)

Delete a Floating IP

Deletes a Floating IP. If it is currently assigned to a Server it will automatically get unassigned.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.FloatingIPsApi();
let id = 56; // Number | ID of the Floating IP
apiInstance.floatingIpsIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| ID of the Floating IP | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## floatingIpsIdGet

> FloatingIpsIdGet200Response floatingIpsIdGet(id)

Get a Floating IP

Returns a specific Floating IP object.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.FloatingIPsApi();
let id = 56; // Number | ID of the Floating IP
apiInstance.floatingIpsIdGet(id, (error, data, response) => {
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

[**FloatingIpsIdGet200Response**](FloatingIpsIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## floatingIpsIdPut

> FloatingIpsIdGet200Response floatingIpsIdPut(id, opts)

Update a Floating IP

Updates the description or labels of a Floating IP. Also note that when updating labels, the Floating IP’s current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.FloatingIPsApi();
let id = 56; // Number | ID of the Floating IP
let opts = {
  'updateFloatingIPRequest': new HetznerCloudApi.UpdateFloatingIPRequest() // UpdateFloatingIPRequest | 
};
apiInstance.floatingIpsIdPut(id, opts, (error, data, response) => {
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
 **updateFloatingIPRequest** | [**UpdateFloatingIPRequest**](UpdateFloatingIPRequest.md)|  | [optional] 

### Return type

[**FloatingIpsIdGet200Response**](FloatingIpsIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## floatingIpsPost

> FloatingIpsPost201Response floatingIpsPost(opts)

Create a Floating IP

Creates a new Floating IP assigned to a Server. If you want to create a Floating IP that is not bound to a Server, you need to provide the &#x60;home_location&#x60; key instead of &#x60;server&#x60;. This can be either the ID or the name of the Location this IP shall be created in. Note that a Floating IP can be assigned to a Server in any Location later on. For optimal routing it is advised to use the Floating IP in the same Location it was created in.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.FloatingIPsApi();
let opts = {
  'createFloatingIPRequest': new HetznerCloudApi.CreateFloatingIPRequest() // CreateFloatingIPRequest | The `type` argument is required while `home_location` and `server` are mutually exclusive.
};
apiInstance.floatingIpsPost(opts, (error, data, response) => {
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
 **createFloatingIPRequest** | [**CreateFloatingIPRequest**](CreateFloatingIPRequest.md)| The &#x60;type&#x60; argument is required while &#x60;home_location&#x60; and &#x60;server&#x60; are mutually exclusive. | [optional] 

### Return type

[**FloatingIpsPost201Response**](FloatingIpsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

