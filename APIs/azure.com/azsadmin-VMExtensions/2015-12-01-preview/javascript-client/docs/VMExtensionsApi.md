# ComputeAdminClient.VMExtensionsApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vMExtensionsCreate**](VMExtensionsApi.md#vMExtensionsCreate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Compute.Admin/locations/{location}/artifactTypes/VMExtension/publishers/{publisher}/types/{type}/versions/{version} | Create a Virtual Machine Extension Image.
[**vMExtensionsDelete**](VMExtensionsApi.md#vMExtensionsDelete) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.Compute.Admin/locations/{location}/artifactTypes/VMExtension/publishers/{publisher}/types/{type}/versions/{version} | Deletes a Virtual Machine Extension Image.
[**vMExtensionsGet**](VMExtensionsApi.md#vMExtensionsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute.Admin/locations/{location}/artifactTypes/VMExtension/publishers/{publisher}/types/{type}/versions/{version} | Returns requested Virtual Machine Extension Image.
[**vMExtensionsList**](VMExtensionsApi.md#vMExtensionsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute.Admin/locations/{location}/artifactTypes/VMExtension | Returns a list of all Virtual Machine Extension Images.



## vMExtensionsCreate

> VMExtension vMExtensionsCreate(subscriptionId, location, publisher, type, version, apiVersion, extension)

Create a Virtual Machine Extension Image.

Create a Virtual Machine Extension Image with publisher, version.

### Example

```javascript
import ComputeAdminClient from 'compute_admin_client';
let defaultClient = ComputeAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeAdminClient.VMExtensionsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let location = "location_example"; // String | Location of the resource.
let publisher = "publisher_example"; // String | Name of the publisher.
let type = "type_example"; // String | Type of extension.
let version = "version_example"; // String | The version of the resource.
let apiVersion = "'2015-12-01-preview'"; // String | Client API Version.
let extension = new ComputeAdminClient.VMExtensionParameters(); // VMExtensionParameters | Virtual Machine Extension Image creation properties.
apiInstance.vMExtensionsCreate(subscriptionId, location, publisher, type, version, apiVersion, extension, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **location** | **String**| Location of the resource. | 
 **publisher** | **String**| Name of the publisher. | 
 **type** | **String**| Type of extension. | 
 **version** | **String**| The version of the resource. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2015-12-01-preview&#39;]
 **extension** | [**VMExtensionParameters**](VMExtensionParameters.md)| Virtual Machine Extension Image creation properties. | 

### Return type

[**VMExtension**](VMExtension.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## vMExtensionsDelete

> vMExtensionsDelete(subscriptionId, location, publisher, type, version, apiVersion)

Deletes a Virtual Machine Extension Image.

Deletes specified Virtual Machine Extension Image.

### Example

```javascript
import ComputeAdminClient from 'compute_admin_client';
let defaultClient = ComputeAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeAdminClient.VMExtensionsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let location = "location_example"; // String | Location of the resource.
let publisher = "publisher_example"; // String | Name of the publisher.
let type = "type_example"; // String | Type of extension.
let version = "version_example"; // String | The version of the resource.
let apiVersion = "'2015-12-01-preview'"; // String | Client API Version.
apiInstance.vMExtensionsDelete(subscriptionId, location, publisher, type, version, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **location** | **String**| Location of the resource. | 
 **publisher** | **String**| Name of the publisher. | 
 **type** | **String**| Type of extension. | 
 **version** | **String**| The version of the resource. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2015-12-01-preview&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## vMExtensionsGet

> VMExtension vMExtensionsGet(subscriptionId, location, publisher, type, version, apiVersion)

Returns requested Virtual Machine Extension Image.

Returns requested Virtual Machine Extension Image matching publisher, type, version.

### Example

```javascript
import ComputeAdminClient from 'compute_admin_client';
let defaultClient = ComputeAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeAdminClient.VMExtensionsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let location = "location_example"; // String | Location of the resource.
let publisher = "publisher_example"; // String | Name of the publisher.
let type = "type_example"; // String | Type of extension.
let version = "version_example"; // String | The version of the resource.
let apiVersion = "'2015-12-01-preview'"; // String | Client API Version.
apiInstance.vMExtensionsGet(subscriptionId, location, publisher, type, version, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **location** | **String**| Location of the resource. | 
 **publisher** | **String**| Name of the publisher. | 
 **type** | **String**| Type of extension. | 
 **version** | **String**| The version of the resource. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2015-12-01-preview&#39;]

### Return type

[**VMExtension**](VMExtension.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## vMExtensionsList

> [VMExtension] vMExtensionsList(subscriptionId, location, apiVersion)

Returns a list of all Virtual Machine Extension Images.

List of all Virtual Machine Extension Images for the current location are returned.

### Example

```javascript
import ComputeAdminClient from 'compute_admin_client';
let defaultClient = ComputeAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeAdminClient.VMExtensionsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let location = "location_example"; // String | Location of the resource.
let apiVersion = "'2015-12-01-preview'"; // String | Client API Version.
apiInstance.vMExtensionsList(subscriptionId, location, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **location** | **String**| Location of the resource. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2015-12-01-preview&#39;]

### Return type

[**[VMExtension]**](VMExtension.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

