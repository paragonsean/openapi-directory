# HetznerCloudApi.SSHKeysApi

All URIs are relative to *https://api.hetzner.cloud/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sshKeysGet**](SSHKeysApi.md#sshKeysGet) | **GET** /ssh_keys | Get all SSH keys
[**sshKeysIdDelete**](SSHKeysApi.md#sshKeysIdDelete) | **DELETE** /ssh_keys/{id} | Delete an SSH key
[**sshKeysIdGet**](SSHKeysApi.md#sshKeysIdGet) | **GET** /ssh_keys/{id} | Get a SSH key
[**sshKeysIdPut**](SSHKeysApi.md#sshKeysIdPut) | **PUT** /ssh_keys/{id} | Update an SSH key
[**sshKeysPost**](SSHKeysApi.md#sshKeysPost) | **POST** /ssh_keys | Create an SSH key



## sshKeysGet

> SshKeysGet200Response sshKeysGet(opts)

Get all SSH keys

Returns all SSH key objects.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.SSHKeysApi();
let opts = {
  'sort': "sort_example", // String | Can be used multiple times.
  'name': "name_example", // String | Can be used to filter resources by their name. The response will only contain the resources matching the specified name
  'fingerprint': "fingerprint_example", // String | Can be used to filter SSH keys by their fingerprint. The response will only contain the SSH key matching the specified fingerprint.
  'labelSelector': "labelSelector_example" // String | Can be used to filter resources by labels. The response will only contain resources matching the label selector.
};
apiInstance.sshKeysGet(opts, (error, data, response) => {
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
 **fingerprint** | **String**| Can be used to filter SSH keys by their fingerprint. The response will only contain the SSH key matching the specified fingerprint. | [optional] 
 **labelSelector** | **String**| Can be used to filter resources by labels. The response will only contain resources matching the label selector. | [optional] 

### Return type

[**SshKeysGet200Response**](SshKeysGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sshKeysIdDelete

> sshKeysIdDelete(id)

Delete an SSH key

Deletes an SSH key. It cannot be used anymore.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.SSHKeysApi();
let id = "id_example"; // String | ID of the SSH key
apiInstance.sshKeysIdDelete(id, (error, data, response) => {
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
 **id** | **String**| ID of the SSH key | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## sshKeysIdGet

> SshKeysPost201Response sshKeysIdGet(id)

Get a SSH key

Returns a specific SSH key object.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.SSHKeysApi();
let id = 56; // Number | ID of the SSH key
apiInstance.sshKeysIdGet(id, (error, data, response) => {
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
 **id** | **Number**| ID of the SSH key | 

### Return type

[**SshKeysPost201Response**](SshKeysPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sshKeysIdPut

> SshKeysPost201Response sshKeysIdPut(id, opts)

Update an SSH key

Updates an SSH key. You can update an SSH key name and an SSH key labels.  Please note that when updating labels, the SSH key current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body. 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.SSHKeysApi();
let id = "id_example"; // String | ID of the SSH key
let opts = {
  'sshKeysIdPutRequest': new HetznerCloudApi.SshKeysIdPutRequest() // SshKeysIdPutRequest | 
};
apiInstance.sshKeysIdPut(id, opts, (error, data, response) => {
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
 **id** | **String**| ID of the SSH key | 
 **sshKeysIdPutRequest** | [**SshKeysIdPutRequest**](SshKeysIdPutRequest.md)|  | [optional] 

### Return type

[**SshKeysPost201Response**](SshKeysPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sshKeysPost

> SshKeysPost201Response sshKeysPost(opts)

Create an SSH key

Creates a new SSH key with the given &#x60;name&#x60; and &#x60;public_key&#x60;. Once an SSH key is created, it can be used in other calls such as creating Servers.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.SSHKeysApi();
let opts = {
  'sshKeysPostRequest': new HetznerCloudApi.SshKeysPostRequest() // SshKeysPostRequest | 
};
apiInstance.sshKeysPost(opts, (error, data, response) => {
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
 **sshKeysPostRequest** | [**SshKeysPostRequest**](SshKeysPostRequest.md)|  | [optional] 

### Return type

[**SshKeysPost201Response**](SshKeysPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

