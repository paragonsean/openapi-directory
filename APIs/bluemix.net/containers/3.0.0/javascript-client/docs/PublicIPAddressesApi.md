# IbmContainersApi.PublicIPAddressesApi

All URIs are relative to *https://containers-api.ng.bluemix.net/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**containersFloatingIpsGet**](PublicIPAddressesApi.md#containersFloatingIpsGet) | **GET** /containers/floating-ips | List available public IP addresses in a space
[**containersFloatingIpsIpReleasePost**](PublicIPAddressesApi.md#containersFloatingIpsIpReleasePost) | **POST** /containers/floating-ips/{ip}/release | Release public IP address
[**containersFloatingIpsRequestPost**](PublicIPAddressesApi.md#containersFloatingIpsRequestPost) | **POST** /containers/floating-ips/request | Request a public IP address for a space
[**containersNameOrIdFloatingIpsIpBindPost**](PublicIPAddressesApi.md#containersNameOrIdFloatingIpsIpBindPost) | **POST** /containers/{name_or_id}/floating-ips/{ip}/bind | Bind a public IP address to a single container
[**containersNameOrIdFloatingIpsIpUnbindPost**](PublicIPAddressesApi.md#containersNameOrIdFloatingIpsIpUnbindPost) | **POST** /containers/{name_or_id}/floating-ips/{ip}/unbind | Unbind a public IP address from a container



## containersFloatingIpsGet

> [FloatingIP] containersFloatingIpsGet(xAuthToken, xAuthProjectId, opts)

List available public IP addresses in a space

This endpoint returns a list of all public IP addresses that are allocated to a space and not bound to a container. If you want to list all public IP addresses that are allocated to a space, even those that are already bound to a container, use the &#x60;all&#x60; query parameter (corrsponding IBM Containers command: &#x60;cf ic ip list&#x60;).

### Example

```javascript
import IbmContainersApi from 'ibm_containers_api';

let apiInstance = new IbmContainersApi.PublicIPAddressesApi();
let xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
let xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
let opts = {
  'all': true // Boolean | If this option is set to `all=1`, `all=True`, or `all=true`, all public IP addresses that are allocated to a space are returned. If this option is set to `all=0`, `all=False`, or `all=false`, only available public IP addresses that are allocated but not bound to a container are returned. By default, only available public IP addresses are returned.
};
apiInstance.containersFloatingIpsGet(xAuthToken, xAuthProjectId, opts, (error, data, response) => {
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
 **xAuthToken** | **String**| The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token. | 
 **xAuthProjectId** | **String**| The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. | 
 **all** | **Boolean**| If this option is set to &#x60;all&#x3D;1&#x60;, &#x60;all&#x3D;True&#x60;, or &#x60;all&#x3D;true&#x60;, all public IP addresses that are allocated to a space are returned. If this option is set to &#x60;all&#x3D;0&#x60;, &#x60;all&#x3D;False&#x60;, or &#x60;all&#x3D;false&#x60;, only available public IP addresses that are allocated but not bound to a container are returned. By default, only available public IP addresses are returned. | [optional] 

### Return type

[**[FloatingIP]**](FloatingIP.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## containersFloatingIpsIpReleasePost

> containersFloatingIpsIpReleasePost(xAuthToken, xAuthProjectId, ip)

Release public IP address

This endpoint releases a public IP address from a space (corresponding IBM Containers command: &#x60;cf ic ip release &lt;ip_adress&gt;&#x60;). The public IP address is no longer allocated to the space. If a container was bound to the IP address, it is automatically unbound.

### Example

```javascript
import IbmContainersApi from 'ibm_containers_api';

let apiInstance = new IbmContainersApi.PublicIPAddressesApi();
let xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
let xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
let ip = "ip_example"; // String | The public IP address that you want to release. Run `cf ic ip list` or call the `GET /containers/floating-ips?all=true` endpoint to review all public IP address that are allocated to your space. After a public IP address is released, it will no longer be allocated to your space.
apiInstance.containersFloatingIpsIpReleasePost(xAuthToken, xAuthProjectId, ip, (error, data, response) => {
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
 **xAuthToken** | **String**| The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token. | 
 **xAuthProjectId** | **String**| The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. | 
 **ip** | **String**| The public IP address that you want to release. Run &#x60;cf ic ip list&#x60; or call the &#x60;GET /containers/floating-ips?all&#x3D;true&#x60; endpoint to review all public IP address that are allocated to your space. After a public IP address is released, it will no longer be allocated to your space. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## containersFloatingIpsRequestPost

> String containersFloatingIpsRequestPost(xAuthToken, xAuthProjectId)

Request a public IP address for a space

This endpoint requests a new public IP address for a space (corresponding IBM Containers command: &#x60;cf ic ip request&#x60;). The number of public IP addresses depends on the quota that is assigned to the space. If there is not enough quota left to request a new public IP address, you can either contact your organization manager to increase the quota, or unbind an existing IP address from a container by running &#x60;cf ic ip unbind &lt;ip_adress&gt; &lt;container&gt;&#x60; command, or  calling the &#x60;POST /container/{name_or_id}/floating-ips/{ip}/unbind&#x60; endpoint.

### Example

```javascript
import IbmContainersApi from 'ibm_containers_api';

let apiInstance = new IbmContainersApi.PublicIPAddressesApi();
let xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
let xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
apiInstance.containersFloatingIpsRequestPost(xAuthToken, xAuthProjectId, (error, data, response) => {
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
 **xAuthToken** | **String**| The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token. | 
 **xAuthProjectId** | **String**| The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## containersNameOrIdFloatingIpsIpBindPost

> containersNameOrIdFloatingIpsIpBindPost(xAuthToken, xAuthProjectId, nameOrId, ip)

Bind a public IP address to a single container

This endpoint binds an available public IP address to a single container (corresponding IBM Containers command: &#x60;cf ic ip bind &lt;ip_adress&gt; &lt;container&gt;&#x60;). After a container is bound to a public IP address, it can be accessed at &#x60;https://&lt;public_ip_adress&gt;:&lt;public_port&gt;&#x60;.

### Example

```javascript
import IbmContainersApi from 'ibm_containers_api';

let apiInstance = new IbmContainersApi.PublicIPAddressesApi();
let xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
let xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
let nameOrId = "nameOrId_example"; // String | The name or ID of the container that you want to bind to the public IP address. Run the `cf ic ps` command or call the `GET /containers/json` endpoint to retrieve a list of containers in your space.
let ip = "ip_example"; // String | The public IP address that you want to bind to your container.   Note: The public IP address must be available in the space and not bound to a container. Run `cf ic ip list` or call the `GET /containers/floating-ips` endpoint.
apiInstance.containersNameOrIdFloatingIpsIpBindPost(xAuthToken, xAuthProjectId, nameOrId, ip, (error, data, response) => {
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
 **xAuthToken** | **String**| The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token. | 
 **xAuthProjectId** | **String**| The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. | 
 **nameOrId** | **String**| The name or ID of the container that you want to bind to the public IP address. Run the &#x60;cf ic ps&#x60; command or call the &#x60;GET /containers/json&#x60; endpoint to retrieve a list of containers in your space. | 
 **ip** | **String**| The public IP address that you want to bind to your container.   Note: The public IP address must be available in the space and not bound to a container. Run &#x60;cf ic ip list&#x60; or call the &#x60;GET /containers/floating-ips&#x60; endpoint. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## containersNameOrIdFloatingIpsIpUnbindPost

> containersNameOrIdFloatingIpsIpUnbindPost(xAuthToken, xAuthProjectId, nameOrId, ip)

Unbind a public IP address from a container

This endpoint unbinds a public IP address from a container (corresponding IBM Containers command: &#x60;cf ic ip unbind &lt;ip_adress&gt; &lt;container&gt;&#x60;). The container that is unbound from the IP address will not be accessible from the internet anymore. The public IP address will be further allocated to the space and can be used to be bound to other containers. 

### Example

```javascript
import IbmContainersApi from 'ibm_containers_api';

let apiInstance = new IbmContainersApi.PublicIPAddressesApi();
let xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
let xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
let nameOrId = "nameOrId_example"; // String | The name or ID of the container that you want to bind to the public IP address. Run the `cf ic ps` command or call the `GET /containers/json` endpoint to retrieve a list of containers in your space. 
let ip = "ip_example"; // String | The public IP address that you want to unbind from your container.    Note: After unbinding a public IP address, this IP address will still be allocated to the space and can be used to be bound to other containers.
apiInstance.containersNameOrIdFloatingIpsIpUnbindPost(xAuthToken, xAuthProjectId, nameOrId, ip, (error, data, response) => {
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
 **xAuthToken** | **String**| The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token. | 
 **xAuthProjectId** | **String**| The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. | 
 **nameOrId** | **String**| The name or ID of the container that you want to bind to the public IP address. Run the &#x60;cf ic ps&#x60; command or call the &#x60;GET /containers/json&#x60; endpoint to retrieve a list of containers in your space.  | 
 **ip** | **String**| The public IP address that you want to unbind from your container.    Note: After unbinding a public IP address, this IP address will still be allocated to the space and can be used to be bound to other containers. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

