# ServiceFabricManagementClient.ClusterVersionApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clusterVersionsGet**](ClusterVersionApi.md#clusterVersionsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ServiceFabric/locations/{location}/clusterVersions/{clusterVersion} | Gets information about a Service Fabric cluster code version available in the specified location.
[**clusterVersionsGetByEnvironment**](ClusterVersionApi.md#clusterVersionsGetByEnvironment) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ServiceFabric/locations/{location}/environments/{environment}/clusterVersions/{clusterVersion} | Gets information about a Service Fabric cluster code version available for the specified environment.
[**clusterVersionsList**](ClusterVersionApi.md#clusterVersionsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ServiceFabric/locations/{location}/clusterVersions | Gets the list of Service Fabric cluster code versions available for the specified location.
[**clusterVersionsListByEnvironment**](ClusterVersionApi.md#clusterVersionsListByEnvironment) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ServiceFabric/locations/{location}/environments/{environment}/clusterVersions | Gets the list of Service Fabric cluster code versions available for the specified environment.



## clusterVersionsGet

> ClusterCodeVersionsListResult clusterVersionsGet(location, apiVersion, subscriptionId, clusterVersion)

Gets information about a Service Fabric cluster code version available in the specified location.

Gets information about an available Service Fabric cluster code version.

### Example

```javascript
import ServiceFabricManagementClient from 'service_fabric_management_client';
let defaultClient = ServiceFabricManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceFabricManagementClient.ClusterVersionApi();
let location = "location_example"; // String | The location for the cluster code versions. This is different from cluster location.
let apiVersion = "'2019-06-01-preview'"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-06-01-preview\" for this specification.
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
let clusterVersion = "clusterVersion_example"; // String | The cluster code version.
apiInstance.clusterVersionsGet(location, apiVersion, subscriptionId, clusterVersion, (error, data, response) => {
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
 **location** | **String**| The location for the cluster code versions. This is different from cluster location. | 
 **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-06-01-preview\&quot; for this specification. | [default to &#39;2019-06-01-preview&#39;]
 **subscriptionId** | **String**| The customer subscription identifier. | 
 **clusterVersion** | **String**| The cluster code version. | 

### Return type

[**ClusterCodeVersionsListResult**](ClusterCodeVersionsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clusterVersionsGetByEnvironment

> ClusterCodeVersionsListResult clusterVersionsGetByEnvironment(location, environment, apiVersion, subscriptionId, clusterVersion)

Gets information about a Service Fabric cluster code version available for the specified environment.

Gets information about an available Service Fabric cluster code version by environment.

### Example

```javascript
import ServiceFabricManagementClient from 'service_fabric_management_client';
let defaultClient = ServiceFabricManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceFabricManagementClient.ClusterVersionApi();
let location = "location_example"; // String | The location for the cluster code versions. This is different from cluster location.
let environment = "environment_example"; // String | The operating system of the cluster. The default means all.
let apiVersion = "'2019-06-01-preview'"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-06-01-preview\" for this specification.
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
let clusterVersion = "clusterVersion_example"; // String | The cluster code version.
apiInstance.clusterVersionsGetByEnvironment(location, environment, apiVersion, subscriptionId, clusterVersion, (error, data, response) => {
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
 **location** | **String**| The location for the cluster code versions. This is different from cluster location. | 
 **environment** | **String**| The operating system of the cluster. The default means all. | 
 **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-06-01-preview\&quot; for this specification. | [default to &#39;2019-06-01-preview&#39;]
 **subscriptionId** | **String**| The customer subscription identifier. | 
 **clusterVersion** | **String**| The cluster code version. | 

### Return type

[**ClusterCodeVersionsListResult**](ClusterCodeVersionsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clusterVersionsList

> ClusterCodeVersionsListResult clusterVersionsList(location, apiVersion, subscriptionId)

Gets the list of Service Fabric cluster code versions available for the specified location.

Gets all available code versions for Service Fabric cluster resources by location.

### Example

```javascript
import ServiceFabricManagementClient from 'service_fabric_management_client';
let defaultClient = ServiceFabricManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceFabricManagementClient.ClusterVersionApi();
let location = "location_example"; // String | The location for the cluster code versions. This is different from cluster location.
let apiVersion = "'2019-06-01-preview'"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-06-01-preview\" for this specification.
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
apiInstance.clusterVersionsList(location, apiVersion, subscriptionId, (error, data, response) => {
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
 **location** | **String**| The location for the cluster code versions. This is different from cluster location. | 
 **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-06-01-preview\&quot; for this specification. | [default to &#39;2019-06-01-preview&#39;]
 **subscriptionId** | **String**| The customer subscription identifier. | 

### Return type

[**ClusterCodeVersionsListResult**](ClusterCodeVersionsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clusterVersionsListByEnvironment

> ClusterCodeVersionsListResult clusterVersionsListByEnvironment(location, environment, apiVersion, subscriptionId)

Gets the list of Service Fabric cluster code versions available for the specified environment.

Gets all available code versions for Service Fabric cluster resources by environment.

### Example

```javascript
import ServiceFabricManagementClient from 'service_fabric_management_client';
let defaultClient = ServiceFabricManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceFabricManagementClient.ClusterVersionApi();
let location = "location_example"; // String | The location for the cluster code versions. This is different from cluster location.
let environment = "environment_example"; // String | The operating system of the cluster. The default means all.
let apiVersion = "'2019-06-01-preview'"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-06-01-preview\" for this specification.
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
apiInstance.clusterVersionsListByEnvironment(location, environment, apiVersion, subscriptionId, (error, data, response) => {
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
 **location** | **String**| The location for the cluster code versions. This is different from cluster location. | 
 **environment** | **String**| The operating system of the cluster. The default means all. | 
 **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-06-01-preview\&quot; for this specification. | [default to &#39;2019-06-01-preview&#39;]
 **subscriptionId** | **String**| The customer subscription identifier. | 

### Return type

[**ClusterCodeVersionsListResult**](ClusterCodeVersionsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

