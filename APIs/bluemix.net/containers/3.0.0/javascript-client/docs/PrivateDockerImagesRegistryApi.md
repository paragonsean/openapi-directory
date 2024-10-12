# IbmContainersApi.PrivateDockerImagesRegistryApi

All URIs are relative to *https://containers-api.ng.bluemix.net/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**registryNamespacesGet**](PrivateDockerImagesRegistryApi.md#registryNamespacesGet) | **GET** /registry/namespaces | Retrieve the namespace of an organization.
[**registryNamespacesNamespaceGet**](PrivateDockerImagesRegistryApi.md#registryNamespacesNamespaceGet) | **GET** /registry/namespaces/{namespace} | Check the availability of a namespace
[**registryNamespacesNamespacePut**](PrivateDockerImagesRegistryApi.md#registryNamespacesNamespacePut) | **PUT** /registry/namespaces/{namespace} | Set a namespace for your private Bluemix registry.



## registryNamespacesGet

> Namespace registryNamespacesGet(xAuthToken, xAuthProjectId)

Retrieve the namespace of an organization.

This endpoint retrieves the namespace that was set for the organization that owns the current space (corresponding IBM Containers command: &#x60;cf ic namespace get&#x60;).

### Example

```javascript
import IbmContainersApi from 'ibm_containers_api';

let apiInstance = new IbmContainersApi.PrivateDockerImagesRegistryApi();
let xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
let xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
apiInstance.registryNamespacesGet(xAuthToken, xAuthProjectId, (error, data, response) => {
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

[**Namespace**](Namespace.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## registryNamespacesNamespaceGet

> Namespace registryNamespacesNamespaceGet(xAuthToken, xAuthProjectId, namespace)

Check the availability of a namespace

This endpoint checks whether a namespace is available in Bluemix and can be used to set up the private Docker images registry for an organization. When a HTTP code &#x60;201 Ok&#x60; is returned, the namespace is already assigned to another organization in Bluemix and cannot be used. When a HTTP code &#x60;404 Not found&#x60; is returned, the namespace can be used for your organization.    Consider the following rules when choosing a namespace for your organization:   - Every organization can have one namespace at a time only  - The namespace must be unique in Bluemix.  - The namespace can be 4-30 characters long.  - The namespace must start with at least one letter or number.  - The namespace can only contain lowercase letters, numbers or underscores (_). 

### Example

```javascript
import IbmContainersApi from 'ibm_containers_api';

let apiInstance = new IbmContainersApi.PrivateDockerImagesRegistryApi();
let xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
let xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
let namespace = "namespace_example"; // String | The name of the namespace that you would like to use for your organization and for which you would like to check availability in Bluemix.
apiInstance.registryNamespacesNamespaceGet(xAuthToken, xAuthProjectId, namespace, (error, data, response) => {
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
 **namespace** | **String**| The name of the namespace that you would like to use for your organization and for which you would like to check availability in Bluemix. | 

### Return type

[**Namespace**](Namespace.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## registryNamespacesNamespacePut

> Namespace registryNamespacesNamespacePut(xAuthToken, xAuthProjectId, namespace)

Set a namespace for your private Bluemix registry.

Set up your own Docker images registry in Bluemix by defining a namespace for your organization (corresponding IBM Containers command: &#x60;cf ic namespace set &lt;namespace&gt;&#x60;). The namespace is used to generate a unique URL to your private Bluemix registry. In your private registry you store all Docker images that you want to share across your organization. To create a container from an image, you must first push the image to your registry.    The namespace cannot be changed after is has been set. Consider the following rules to choose a namespace for your organization:   - Every organization can have one namespace at a time only  - The namespace must be unique in Bluemix.  - The namespace can be 4-30 characters long.  - The namespace must start with at least one letter or number.  - The namespace can only contain lowercase letters, numbers or underscores (_).

### Example

```javascript
import IbmContainersApi from 'ibm_containers_api';

let apiInstance = new IbmContainersApi.PrivateDockerImagesRegistryApi();
let xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
let xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
let namespace = "namespace_example"; // String | The name for your namespace to create your private Docker images registry in Bluemix. You cannot change the name afterward. The namespace can be 4-30 characters long, must start with at least one letter or number, and can only contain lowercase letters, numbers or underscores (_). You can test the availability of your namespace by calling the `GET /registry/namespaces/<namespace>` endpoint. When a HTTP code `404 Not Found` is returned, the namespace is available in Bluemix. 
apiInstance.registryNamespacesNamespacePut(xAuthToken, xAuthProjectId, namespace, (error, data, response) => {
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
 **namespace** | **String**| The name for your namespace to create your private Docker images registry in Bluemix. You cannot change the name afterward. The namespace can be 4-30 characters long, must start with at least one letter or number, and can only contain lowercase letters, numbers or underscores (_). You can test the availability of your namespace by calling the &#x60;GET /registry/namespaces/&lt;namespace&gt;&#x60; endpoint. When a HTTP code &#x60;404 Not Found&#x60; is returned, the namespace is available in Bluemix.  | 

### Return type

[**Namespace**](Namespace.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

