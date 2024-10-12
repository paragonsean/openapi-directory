# AwsAppMesh.DefaultApi

All URIs are relative to *http://appmesh.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createMesh**](DefaultApi.md#createMesh) | **PUT** /meshes | 
[**createRoute**](DefaultApi.md#createRoute) | **PUT** /meshes/{meshName}/virtualRouter/{virtualRouterName}/routes | 
[**createVirtualNode**](DefaultApi.md#createVirtualNode) | **PUT** /meshes/{meshName}/virtualNodes | 
[**createVirtualRouter**](DefaultApi.md#createVirtualRouter) | **PUT** /meshes/{meshName}/virtualRouters | 
[**deleteMesh**](DefaultApi.md#deleteMesh) | **DELETE** /meshes/{meshName} | 
[**deleteRoute**](DefaultApi.md#deleteRoute) | **DELETE** /meshes/{meshName}/virtualRouter/{virtualRouterName}/routes/{routeName} | 
[**deleteVirtualNode**](DefaultApi.md#deleteVirtualNode) | **DELETE** /meshes/{meshName}/virtualNodes/{virtualNodeName} | 
[**deleteVirtualRouter**](DefaultApi.md#deleteVirtualRouter) | **DELETE** /meshes/{meshName}/virtualRouters/{virtualRouterName} | 
[**describeMesh**](DefaultApi.md#describeMesh) | **GET** /meshes/{meshName} | 
[**describeRoute**](DefaultApi.md#describeRoute) | **GET** /meshes/{meshName}/virtualRouter/{virtualRouterName}/routes/{routeName} | 
[**describeVirtualNode**](DefaultApi.md#describeVirtualNode) | **GET** /meshes/{meshName}/virtualNodes/{virtualNodeName} | 
[**describeVirtualRouter**](DefaultApi.md#describeVirtualRouter) | **GET** /meshes/{meshName}/virtualRouters/{virtualRouterName} | 
[**listMeshes**](DefaultApi.md#listMeshes) | **GET** /meshes | 
[**listRoutes**](DefaultApi.md#listRoutes) | **GET** /meshes/{meshName}/virtualRouter/{virtualRouterName}/routes | 
[**listVirtualNodes**](DefaultApi.md#listVirtualNodes) | **GET** /meshes/{meshName}/virtualNodes | 
[**listVirtualRouters**](DefaultApi.md#listVirtualRouters) | **GET** /meshes/{meshName}/virtualRouters | 
[**updateRoute**](DefaultApi.md#updateRoute) | **PUT** /meshes/{meshName}/virtualRouter/{virtualRouterName}/routes/{routeName} | 
[**updateVirtualNode**](DefaultApi.md#updateVirtualNode) | **PUT** /meshes/{meshName}/virtualNodes/{virtualNodeName} | 
[**updateVirtualRouter**](DefaultApi.md#updateVirtualRouter) | **PUT** /meshes/{meshName}/virtualRouters/{virtualRouterName} | 



## createMesh

> CreateMeshOutput createMesh(createMeshRequest, opts)



&lt;p&gt;Creates a new service mesh. A service mesh is a logical boundary for network traffic          between the services that reside within it.&lt;/p&gt;          &lt;p&gt;After you create your service mesh, you can create virtual nodes, virtual routers, and          routes to distribute traffic between the applications in your mesh.&lt;/p&gt;

### Example

```javascript
import AwsAppMesh from 'aws_app_mesh';
let defaultClient = AwsAppMesh.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppMesh.DefaultApi();
let createMeshRequest = new AwsAppMesh.CreateMeshRequest(); // CreateMeshRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createMesh(createMeshRequest, opts, (error, data, response) => {
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
 **createMeshRequest** | [**CreateMeshRequest**](CreateMeshRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateMeshOutput**](CreateMeshOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createRoute

> CreateRouteOutput createRoute(meshName, virtualRouterName, createRouteRequest, opts)



&lt;p&gt;Creates a new route that is associated with a virtual router.&lt;/p&gt;          &lt;p&gt;You can use the &lt;code&gt;prefix&lt;/code&gt; parameter in your route specification for path-based          routing of requests. For example, if your virtual router service name is             &lt;code&gt;my-service.local&lt;/code&gt;, and you want the route to match requests to             &lt;code&gt;my-service.local/metrics&lt;/code&gt;, then your prefix should be          &lt;code&gt;/metrics&lt;/code&gt;.&lt;/p&gt;          &lt;p&gt;If your route matches a request, you can distribute traffic to one or more target          virtual nodes with relative weighting.&lt;/p&gt;

### Example

```javascript
import AwsAppMesh from 'aws_app_mesh';
let defaultClient = AwsAppMesh.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppMesh.DefaultApi();
let meshName = "meshName_example"; // String | The name of the service mesh in which to create the route.
let virtualRouterName = "virtualRouterName_example"; // String | The name of the virtual router in which to create the route.
let createRouteRequest = new AwsAppMesh.CreateRouteRequest(); // CreateRouteRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createRoute(meshName, virtualRouterName, createRouteRequest, opts, (error, data, response) => {
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
 **meshName** | **String**| The name of the service mesh in which to create the route. | 
 **virtualRouterName** | **String**| The name of the virtual router in which to create the route. | 
 **createRouteRequest** | [**CreateRouteRequest**](CreateRouteRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateRouteOutput**](CreateRouteOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createVirtualNode

> CreateVirtualNodeOutput createVirtualNode(meshName, createVirtualNodeRequest, opts)



&lt;p&gt;Creates a new virtual node within a service mesh.&lt;/p&gt;          &lt;p&gt;A virtual node acts as logical pointer to a particular task group, such as an Amazon ECS          service or a Kubernetes deployment. When you create a virtual node, you must specify the          DNS service discovery name for your task group.&lt;/p&gt;          &lt;p&gt;Any inbound traffic that your virtual node expects should be specified as a             &lt;code&gt;listener&lt;/code&gt;. Any outbound traffic that your virtual node expects to reach          should be specified as a &lt;code&gt;backend&lt;/code&gt;.&lt;/p&gt;          &lt;p&gt;The response metadata for your new virtual node contains the &lt;code&gt;arn&lt;/code&gt; that is          associated with the virtual node. Set this value (either the full ARN or the truncated          resource name, for example, &lt;code&gt;mesh/default/virtualNode/simpleapp&lt;/code&gt;, as the             &lt;code&gt;APPMESH_VIRTUAL_NODE_NAME&lt;/code&gt; environment variable for your task group&#39;s Envoy          proxy container in your task definition or pod spec. This is then mapped to the             &lt;code&gt;node.id&lt;/code&gt; and &lt;code&gt;node.cluster&lt;/code&gt; Envoy parameters.&lt;/p&gt;          &lt;note&gt;             &lt;p&gt;If you require your Envoy stats or tracing to use a different name, you can override             the &lt;code&gt;node.cluster&lt;/code&gt; value that is set by                &lt;code&gt;APPMESH_VIRTUAL_NODE_NAME&lt;/code&gt; with the                &lt;code&gt;APPMESH_VIRTUAL_NODE_CLUSTER&lt;/code&gt; environment variable.&lt;/p&gt;          &lt;/note&gt;

### Example

```javascript
import AwsAppMesh from 'aws_app_mesh';
let defaultClient = AwsAppMesh.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppMesh.DefaultApi();
let meshName = "meshName_example"; // String | The name of the service mesh in which to create the virtual node.
let createVirtualNodeRequest = new AwsAppMesh.CreateVirtualNodeRequest(); // CreateVirtualNodeRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createVirtualNode(meshName, createVirtualNodeRequest, opts, (error, data, response) => {
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
 **meshName** | **String**| The name of the service mesh in which to create the virtual node. | 
 **createVirtualNodeRequest** | [**CreateVirtualNodeRequest**](CreateVirtualNodeRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateVirtualNodeOutput**](CreateVirtualNodeOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createVirtualRouter

> CreateVirtualRouterOutput createVirtualRouter(meshName, createVirtualRouterRequest, opts)



&lt;p&gt;Creates a new virtual router within a service mesh.&lt;/p&gt;          &lt;p&gt;Virtual routers handle traffic for one or more service names within your mesh. After you          create your virtual router, create and associate routes for your virtual router that direct          incoming requests to different virtual nodes.&lt;/p&gt;

### Example

```javascript
import AwsAppMesh from 'aws_app_mesh';
let defaultClient = AwsAppMesh.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppMesh.DefaultApi();
let meshName = "meshName_example"; // String | The name of the service mesh in which to create the virtual router.
let createVirtualRouterRequest = new AwsAppMesh.CreateVirtualRouterRequest(); // CreateVirtualRouterRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createVirtualRouter(meshName, createVirtualRouterRequest, opts, (error, data, response) => {
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
 **meshName** | **String**| The name of the service mesh in which to create the virtual router. | 
 **createVirtualRouterRequest** | [**CreateVirtualRouterRequest**](CreateVirtualRouterRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateVirtualRouterOutput**](CreateVirtualRouterOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteMesh

> DeleteMeshOutput deleteMesh(meshName, opts)



&lt;p&gt;Deletes an existing service mesh.&lt;/p&gt;          &lt;p&gt;You must delete all resources (routes, virtual routers, virtual nodes) in the service          mesh before you can delete the mesh itself.&lt;/p&gt;

### Example

```javascript
import AwsAppMesh from 'aws_app_mesh';
let defaultClient = AwsAppMesh.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppMesh.DefaultApi();
let meshName = "meshName_example"; // String | The name of the service mesh to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteMesh(meshName, opts, (error, data, response) => {
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
 **meshName** | **String**| The name of the service mesh to delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteMeshOutput**](DeleteMeshOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteRoute

> DeleteRouteOutput deleteRoute(meshName, routeName, virtualRouterName, opts)



Deletes an existing route.

### Example

```javascript
import AwsAppMesh from 'aws_app_mesh';
let defaultClient = AwsAppMesh.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppMesh.DefaultApi();
let meshName = "meshName_example"; // String | The name of the service mesh in which to delete the route.
let routeName = "routeName_example"; // String | The name of the route to delete.
let virtualRouterName = "virtualRouterName_example"; // String | The name of the virtual router in which to delete the route.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteRoute(meshName, routeName, virtualRouterName, opts, (error, data, response) => {
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
 **meshName** | **String**| The name of the service mesh in which to delete the route. | 
 **routeName** | **String**| The name of the route to delete. | 
 **virtualRouterName** | **String**| The name of the virtual router in which to delete the route. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteRouteOutput**](DeleteRouteOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteVirtualNode

> DeleteVirtualNodeOutput deleteVirtualNode(meshName, virtualNodeName, opts)



Deletes an existing virtual node.

### Example

```javascript
import AwsAppMesh from 'aws_app_mesh';
let defaultClient = AwsAppMesh.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppMesh.DefaultApi();
let meshName = "meshName_example"; // String | The name of the service mesh in which to delete the virtual node.
let virtualNodeName = "virtualNodeName_example"; // String | The name of the virtual node to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteVirtualNode(meshName, virtualNodeName, opts, (error, data, response) => {
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
 **meshName** | **String**| The name of the service mesh in which to delete the virtual node. | 
 **virtualNodeName** | **String**| The name of the virtual node to delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteVirtualNodeOutput**](DeleteVirtualNodeOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteVirtualRouter

> DeleteVirtualRouterOutput deleteVirtualRouter(meshName, virtualRouterName, opts)



&lt;p&gt;Deletes an existing virtual router.&lt;/p&gt;          &lt;p&gt;You must delete any routes associated with the virtual router before you can delete the          router itself.&lt;/p&gt;

### Example

```javascript
import AwsAppMesh from 'aws_app_mesh';
let defaultClient = AwsAppMesh.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppMesh.DefaultApi();
let meshName = "meshName_example"; // String | The name of the service mesh in which to delete the virtual router.
let virtualRouterName = "virtualRouterName_example"; // String | The name of the virtual router to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteVirtualRouter(meshName, virtualRouterName, opts, (error, data, response) => {
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
 **meshName** | **String**| The name of the service mesh in which to delete the virtual router. | 
 **virtualRouterName** | **String**| The name of the virtual router to delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteVirtualRouterOutput**](DeleteVirtualRouterOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeMesh

> DescribeMeshOutput describeMesh(meshName, opts)



Describes an existing service mesh.

### Example

```javascript
import AwsAppMesh from 'aws_app_mesh';
let defaultClient = AwsAppMesh.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppMesh.DefaultApi();
let meshName = "meshName_example"; // String | The name of the service mesh to describe.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeMesh(meshName, opts, (error, data, response) => {
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
 **meshName** | **String**| The name of the service mesh to describe. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeMeshOutput**](DescribeMeshOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeRoute

> DescribeRouteOutput describeRoute(meshName, routeName, virtualRouterName, opts)



Describes an existing route.

### Example

```javascript
import AwsAppMesh from 'aws_app_mesh';
let defaultClient = AwsAppMesh.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppMesh.DefaultApi();
let meshName = "meshName_example"; // String | The name of the service mesh in which the route resides.
let routeName = "routeName_example"; // String | The name of the route to describe.
let virtualRouterName = "virtualRouterName_example"; // String | The name of the virtual router with which the route is associated.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeRoute(meshName, routeName, virtualRouterName, opts, (error, data, response) => {
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
 **meshName** | **String**| The name of the service mesh in which the route resides. | 
 **routeName** | **String**| The name of the route to describe. | 
 **virtualRouterName** | **String**| The name of the virtual router with which the route is associated. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeRouteOutput**](DescribeRouteOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeVirtualNode

> DescribeVirtualNodeOutput describeVirtualNode(meshName, virtualNodeName, opts)



Describes an existing virtual node.

### Example

```javascript
import AwsAppMesh from 'aws_app_mesh';
let defaultClient = AwsAppMesh.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppMesh.DefaultApi();
let meshName = "meshName_example"; // String | The name of the service mesh in which the virtual node resides.
let virtualNodeName = "virtualNodeName_example"; // String | The name of the virtual node to describe.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeVirtualNode(meshName, virtualNodeName, opts, (error, data, response) => {
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
 **meshName** | **String**| The name of the service mesh in which the virtual node resides. | 
 **virtualNodeName** | **String**| The name of the virtual node to describe. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeVirtualNodeOutput**](DescribeVirtualNodeOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeVirtualRouter

> DescribeVirtualRouterOutput describeVirtualRouter(meshName, virtualRouterName, opts)



Describes an existing virtual router.

### Example

```javascript
import AwsAppMesh from 'aws_app_mesh';
let defaultClient = AwsAppMesh.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppMesh.DefaultApi();
let meshName = "meshName_example"; // String | The name of the service mesh in which the virtual router resides.
let virtualRouterName = "virtualRouterName_example"; // String | The name of the virtual router to describe.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeVirtualRouter(meshName, virtualRouterName, opts, (error, data, response) => {
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
 **meshName** | **String**| The name of the service mesh in which the virtual router resides. | 
 **virtualRouterName** | **String**| The name of the virtual router to describe. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeVirtualRouterOutput**](DescribeVirtualRouterOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listMeshes

> ListMeshesOutput listMeshes(opts)



Returns a list of existing service meshes.

### Example

```javascript
import AwsAppMesh from 'aws_app_mesh';
let defaultClient = AwsAppMesh.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppMesh.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'limit': 56, // Number | The maximum number of mesh results returned by <code>ListMeshes</code> in paginated          output. When this parameter is used, <code>ListMeshes</code> only returns             <code>limit</code> results in a single page along with a <code>nextToken</code> response          element. The remaining results of the initial request can be seen by sending another             <code>ListMeshes</code> request with the returned <code>nextToken</code> value. This          value can be between 1 and 100. If this parameter is not          used, then <code>ListMeshes</code> returns up to 100 results and a             <code>nextToken</code> value if applicable.
  'nextToken': "nextToken_example" // String | <p>The <code>nextToken</code> value returned from a previous paginated          <code>ListMeshes</code> request where <code>limit</code> was used and the          results exceeded the value of that parameter. Pagination continues from the end of the          previous results that returned the <code>nextToken</code> value.</p>          <note>             <p>This token should be treated as an opaque identifier that is only used to                 retrieve the next items in a list and not for other programmatic purposes.</p>         </note>
};
apiInstance.listMeshes(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **limit** | **Number**| The maximum number of mesh results returned by &lt;code&gt;ListMeshes&lt;/code&gt; in paginated          output. When this parameter is used, &lt;code&gt;ListMeshes&lt;/code&gt; only returns             &lt;code&gt;limit&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response          element. The remaining results of the initial request can be seen by sending another             &lt;code&gt;ListMeshes&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. This          value can be between 1 and 100. If this parameter is not          used, then &lt;code&gt;ListMeshes&lt;/code&gt; returns up to 100 results and a             &lt;code&gt;nextToken&lt;/code&gt; value if applicable. | [optional] 
 **nextToken** | **String**| &lt;p&gt;The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated          &lt;code&gt;ListMeshes&lt;/code&gt; request where &lt;code&gt;limit&lt;/code&gt; was used and the          results exceeded the value of that parameter. Pagination continues from the end of the          previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value.&lt;/p&gt;          &lt;note&gt;             &lt;p&gt;This token should be treated as an opaque identifier that is only used to                 retrieve the next items in a list and not for other programmatic purposes.&lt;/p&gt;         &lt;/note&gt; | [optional] 

### Return type

[**ListMeshesOutput**](ListMeshesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listRoutes

> ListRoutesOutput listRoutes(meshName, virtualRouterName, opts)



Returns a list of existing routes in a service mesh.

### Example

```javascript
import AwsAppMesh from 'aws_app_mesh';
let defaultClient = AwsAppMesh.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppMesh.DefaultApi();
let meshName = "meshName_example"; // String | The name of the service mesh in which to list routes.
let virtualRouterName = "virtualRouterName_example"; // String | The name of the virtual router in which to list routes.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'limit': 56, // Number | The maximum number of mesh results returned by <code>ListRoutes</code> in paginated          output. When this parameter is used, <code>ListRoutes</code> only returns             <code>limit</code> results in a single page along with a <code>nextToken</code> response          element. The remaining results of the initial request can be seen by sending another             <code>ListRoutes</code> request with the returned <code>nextToken</code> value. This          value can be between 1 and 100. If this parameter is not          used, then <code>ListRoutes</code> returns up to 100 results and a             <code>nextToken</code> value if applicable.
  'nextToken': "nextToken_example" // String | The <code>nextToken</code> value returned from a previous paginated          <code>ListRoutes</code> request where <code>limit</code> was used and the          results exceeded the value of that parameter. Pagination continues from the end of the          previous results that returned the <code>nextToken</code> value.
};
apiInstance.listRoutes(meshName, virtualRouterName, opts, (error, data, response) => {
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
 **meshName** | **String**| The name of the service mesh in which to list routes. | 
 **virtualRouterName** | **String**| The name of the virtual router in which to list routes. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **limit** | **Number**| The maximum number of mesh results returned by &lt;code&gt;ListRoutes&lt;/code&gt; in paginated          output. When this parameter is used, &lt;code&gt;ListRoutes&lt;/code&gt; only returns             &lt;code&gt;limit&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response          element. The remaining results of the initial request can be seen by sending another             &lt;code&gt;ListRoutes&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. This          value can be between 1 and 100. If this parameter is not          used, then &lt;code&gt;ListRoutes&lt;/code&gt; returns up to 100 results and a             &lt;code&gt;nextToken&lt;/code&gt; value if applicable. | [optional] 
 **nextToken** | **String**| The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated          &lt;code&gt;ListRoutes&lt;/code&gt; request where &lt;code&gt;limit&lt;/code&gt; was used and the          results exceeded the value of that parameter. Pagination continues from the end of the          previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value. | [optional] 

### Return type

[**ListRoutesOutput**](ListRoutesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listVirtualNodes

> ListVirtualNodesOutput listVirtualNodes(meshName, opts)



Returns a list of existing virtual nodes.

### Example

```javascript
import AwsAppMesh from 'aws_app_mesh';
let defaultClient = AwsAppMesh.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppMesh.DefaultApi();
let meshName = "meshName_example"; // String | The name of the service mesh in which to list virtual nodes.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'limit': 56, // Number | The maximum number of mesh results returned by <code>ListVirtualNodes</code> in          paginated output. When this parameter is used, <code>ListVirtualNodes</code> only returns          <code>limit</code> results in a single page along with a <code>nextToken</code>          response element. The remaining results of the initial request can be seen by sending          another <code>ListVirtualNodes</code> request with the returned <code>nextToken</code>          value. This value can be between 1 and 100. If this          parameter is not used, then <code>ListVirtualNodes</code> returns up to          100 results and a <code>nextToken</code> value if applicable.
  'nextToken': "nextToken_example" // String | The <code>nextToken</code> value returned from a previous paginated          <code>ListVirtualNodes</code> request where <code>limit</code> was used and the          results exceeded the value of that parameter. Pagination continues from the end of the          previous results that returned the <code>nextToken</code> value.
};
apiInstance.listVirtualNodes(meshName, opts, (error, data, response) => {
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
 **meshName** | **String**| The name of the service mesh in which to list virtual nodes. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **limit** | **Number**| The maximum number of mesh results returned by &lt;code&gt;ListVirtualNodes&lt;/code&gt; in          paginated output. When this parameter is used, &lt;code&gt;ListVirtualNodes&lt;/code&gt; only returns          &lt;code&gt;limit&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt;          response element. The remaining results of the initial request can be seen by sending          another &lt;code&gt;ListVirtualNodes&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt;          value. This value can be between 1 and 100. If this          parameter is not used, then &lt;code&gt;ListVirtualNodes&lt;/code&gt; returns up to          100 results and a &lt;code&gt;nextToken&lt;/code&gt; value if applicable. | [optional] 
 **nextToken** | **String**| The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated          &lt;code&gt;ListVirtualNodes&lt;/code&gt; request where &lt;code&gt;limit&lt;/code&gt; was used and the          results exceeded the value of that parameter. Pagination continues from the end of the          previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value. | [optional] 

### Return type

[**ListVirtualNodesOutput**](ListVirtualNodesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listVirtualRouters

> ListVirtualRoutersOutput listVirtualRouters(meshName, opts)



Returns a list of existing virtual routers in a service mesh.

### Example

```javascript
import AwsAppMesh from 'aws_app_mesh';
let defaultClient = AwsAppMesh.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppMesh.DefaultApi();
let meshName = "meshName_example"; // String | The name of the service mesh in which to list virtual routers.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'limit': 56, // Number | The maximum number of mesh results returned by <code>ListVirtualRouters</code> in          paginated output. When this parameter is used, <code>ListVirtualRouters</code> only returns          <code>limit</code> results in a single page along with a <code>nextToken</code>          response element. The remaining results of the initial request can be seen by sending          another <code>ListVirtualRouters</code> request with the returned <code>nextToken</code>          value. This value can be between 1 and 100. If this          parameter is not used, then <code>ListVirtualRouters</code> returns up to          100 results and a <code>nextToken</code> value if applicable.
  'nextToken': "nextToken_example" // String | The <code>nextToken</code> value returned from a previous paginated          <code>ListVirtualRouters</code> request where <code>limit</code> was used and the          results exceeded the value of that parameter. Pagination continues from the end of the          previous results that returned the <code>nextToken</code> value.
};
apiInstance.listVirtualRouters(meshName, opts, (error, data, response) => {
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
 **meshName** | **String**| The name of the service mesh in which to list virtual routers. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **limit** | **Number**| The maximum number of mesh results returned by &lt;code&gt;ListVirtualRouters&lt;/code&gt; in          paginated output. When this parameter is used, &lt;code&gt;ListVirtualRouters&lt;/code&gt; only returns          &lt;code&gt;limit&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt;          response element. The remaining results of the initial request can be seen by sending          another &lt;code&gt;ListVirtualRouters&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt;          value. This value can be between 1 and 100. If this          parameter is not used, then &lt;code&gt;ListVirtualRouters&lt;/code&gt; returns up to          100 results and a &lt;code&gt;nextToken&lt;/code&gt; value if applicable. | [optional] 
 **nextToken** | **String**| The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated          &lt;code&gt;ListVirtualRouters&lt;/code&gt; request where &lt;code&gt;limit&lt;/code&gt; was used and the          results exceeded the value of that parameter. Pagination continues from the end of the          previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value. | [optional] 

### Return type

[**ListVirtualRoutersOutput**](ListVirtualRoutersOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateRoute

> UpdateRouteOutput updateRoute(meshName, routeName, virtualRouterName, updateRouteRequest, opts)



Updates an existing route for a specified service mesh and virtual router.

### Example

```javascript
import AwsAppMesh from 'aws_app_mesh';
let defaultClient = AwsAppMesh.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppMesh.DefaultApi();
let meshName = "meshName_example"; // String | The name of the service mesh in which the route resides.
let routeName = "routeName_example"; // String | The name of the route to update.
let virtualRouterName = "virtualRouterName_example"; // String | The name of the virtual router with which the route is associated.
let updateRouteRequest = new AwsAppMesh.UpdateRouteRequest(); // UpdateRouteRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateRoute(meshName, routeName, virtualRouterName, updateRouteRequest, opts, (error, data, response) => {
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
 **meshName** | **String**| The name of the service mesh in which the route resides. | 
 **routeName** | **String**| The name of the route to update. | 
 **virtualRouterName** | **String**| The name of the virtual router with which the route is associated. | 
 **updateRouteRequest** | [**UpdateRouteRequest**](UpdateRouteRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateRouteOutput**](UpdateRouteOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateVirtualNode

> UpdateVirtualNodeOutput updateVirtualNode(meshName, virtualNodeName, updateVirtualNodeRequest, opts)



Updates an existing virtual node in a specified service mesh.

### Example

```javascript
import AwsAppMesh from 'aws_app_mesh';
let defaultClient = AwsAppMesh.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppMesh.DefaultApi();
let meshName = "meshName_example"; // String | The name of the service mesh in which the virtual node resides.
let virtualNodeName = "virtualNodeName_example"; // String | The name of the virtual node to update.
let updateVirtualNodeRequest = new AwsAppMesh.UpdateVirtualNodeRequest(); // UpdateVirtualNodeRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateVirtualNode(meshName, virtualNodeName, updateVirtualNodeRequest, opts, (error, data, response) => {
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
 **meshName** | **String**| The name of the service mesh in which the virtual node resides. | 
 **virtualNodeName** | **String**| The name of the virtual node to update. | 
 **updateVirtualNodeRequest** | [**UpdateVirtualNodeRequest**](UpdateVirtualNodeRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateVirtualNodeOutput**](UpdateVirtualNodeOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateVirtualRouter

> UpdateVirtualRouterOutput updateVirtualRouter(meshName, virtualRouterName, updateVirtualRouterRequest, opts)



Updates an existing virtual router in a specified service mesh.

### Example

```javascript
import AwsAppMesh from 'aws_app_mesh';
let defaultClient = AwsAppMesh.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAppMesh.DefaultApi();
let meshName = "meshName_example"; // String | The name of the service mesh in which the virtual router resides.
let virtualRouterName = "virtualRouterName_example"; // String | The name of the virtual router to update.
let updateVirtualRouterRequest = new AwsAppMesh.UpdateVirtualRouterRequest(); // UpdateVirtualRouterRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateVirtualRouter(meshName, virtualRouterName, updateVirtualRouterRequest, opts, (error, data, response) => {
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
 **meshName** | **String**| The name of the service mesh in which the virtual router resides. | 
 **virtualRouterName** | **String**| The name of the virtual router to update. | 
 **updateVirtualRouterRequest** | [**UpdateVirtualRouterRequest**](UpdateVirtualRouterRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateVirtualRouterOutput**](UpdateVirtualRouterOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

