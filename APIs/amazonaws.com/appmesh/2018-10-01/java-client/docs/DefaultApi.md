# DefaultApi

All URIs are relative to *http://appmesh.us-east-1.amazonaws.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createMesh**](DefaultApi.md#createMesh) | **PUT** /meshes |  |
| [**createRoute**](DefaultApi.md#createRoute) | **PUT** /meshes/{meshName}/virtualRouter/{virtualRouterName}/routes |  |
| [**createVirtualNode**](DefaultApi.md#createVirtualNode) | **PUT** /meshes/{meshName}/virtualNodes |  |
| [**createVirtualRouter**](DefaultApi.md#createVirtualRouter) | **PUT** /meshes/{meshName}/virtualRouters |  |
| [**deleteMesh**](DefaultApi.md#deleteMesh) | **DELETE** /meshes/{meshName} |  |
| [**deleteRoute**](DefaultApi.md#deleteRoute) | **DELETE** /meshes/{meshName}/virtualRouter/{virtualRouterName}/routes/{routeName} |  |
| [**deleteVirtualNode**](DefaultApi.md#deleteVirtualNode) | **DELETE** /meshes/{meshName}/virtualNodes/{virtualNodeName} |  |
| [**deleteVirtualRouter**](DefaultApi.md#deleteVirtualRouter) | **DELETE** /meshes/{meshName}/virtualRouters/{virtualRouterName} |  |
| [**describeMesh**](DefaultApi.md#describeMesh) | **GET** /meshes/{meshName} |  |
| [**describeRoute**](DefaultApi.md#describeRoute) | **GET** /meshes/{meshName}/virtualRouter/{virtualRouterName}/routes/{routeName} |  |
| [**describeVirtualNode**](DefaultApi.md#describeVirtualNode) | **GET** /meshes/{meshName}/virtualNodes/{virtualNodeName} |  |
| [**describeVirtualRouter**](DefaultApi.md#describeVirtualRouter) | **GET** /meshes/{meshName}/virtualRouters/{virtualRouterName} |  |
| [**listMeshes**](DefaultApi.md#listMeshes) | **GET** /meshes |  |
| [**listRoutes**](DefaultApi.md#listRoutes) | **GET** /meshes/{meshName}/virtualRouter/{virtualRouterName}/routes |  |
| [**listVirtualNodes**](DefaultApi.md#listVirtualNodes) | **GET** /meshes/{meshName}/virtualNodes |  |
| [**listVirtualRouters**](DefaultApi.md#listVirtualRouters) | **GET** /meshes/{meshName}/virtualRouters |  |
| [**updateRoute**](DefaultApi.md#updateRoute) | **PUT** /meshes/{meshName}/virtualRouter/{virtualRouterName}/routes/{routeName} |  |
| [**updateVirtualNode**](DefaultApi.md#updateVirtualNode) | **PUT** /meshes/{meshName}/virtualNodes/{virtualNodeName} |  |
| [**updateVirtualRouter**](DefaultApi.md#updateVirtualRouter) | **PUT** /meshes/{meshName}/virtualRouters/{virtualRouterName} |  |


<a id="createMesh"></a>
# **createMesh**
> CreateMeshOutput createMesh(createMeshRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a new service mesh. A service mesh is a logical boundary for network traffic          between the services that reside within it.&lt;/p&gt;          &lt;p&gt;After you create your service mesh, you can create virtual nodes, virtual routers, and          routes to distribute traffic between the applications in your mesh.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://appmesh.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateMeshRequest createMeshRequest = new CreateMeshRequest(); // CreateMeshRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateMeshOutput result = apiInstance.createMesh(createMeshRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createMesh");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createMeshRequest** | [**CreateMeshRequest**](CreateMeshRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateMeshOutput**](CreateMeshOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ConflictException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | InternalServerErrorException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | NotFoundException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | TooManyRequestsException |  -  |

<a id="createRoute"></a>
# **createRoute**
> CreateRouteOutput createRoute(meshName, virtualRouterName, createRouteRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a new route that is associated with a virtual router.&lt;/p&gt;          &lt;p&gt;You can use the &lt;code&gt;prefix&lt;/code&gt; parameter in your route specification for path-based          routing of requests. For example, if your virtual router service name is             &lt;code&gt;my-service.local&lt;/code&gt;, and you want the route to match requests to             &lt;code&gt;my-service.local/metrics&lt;/code&gt;, then your prefix should be          &lt;code&gt;/metrics&lt;/code&gt;.&lt;/p&gt;          &lt;p&gt;If your route matches a request, you can distribute traffic to one or more target          virtual nodes with relative weighting.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://appmesh.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String meshName = "meshName_example"; // String | The name of the service mesh in which to create the route.
    String virtualRouterName = "virtualRouterName_example"; // String | The name of the virtual router in which to create the route.
    CreateRouteRequest createRouteRequest = new CreateRouteRequest(); // CreateRouteRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateRouteOutput result = apiInstance.createRoute(meshName, virtualRouterName, createRouteRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createRoute");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **meshName** | **String**| The name of the service mesh in which to create the route. | |
| **virtualRouterName** | **String**| The name of the virtual router in which to create the route. | |
| **createRouteRequest** | [**CreateRouteRequest**](CreateRouteRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateRouteOutput**](CreateRouteOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ConflictException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | InternalServerErrorException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | NotFoundException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | TooManyRequestsException |  -  |

<a id="createVirtualNode"></a>
# **createVirtualNode**
> CreateVirtualNodeOutput createVirtualNode(meshName, createVirtualNodeRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a new virtual node within a service mesh.&lt;/p&gt;          &lt;p&gt;A virtual node acts as logical pointer to a particular task group, such as an Amazon ECS          service or a Kubernetes deployment. When you create a virtual node, you must specify the          DNS service discovery name for your task group.&lt;/p&gt;          &lt;p&gt;Any inbound traffic that your virtual node expects should be specified as a             &lt;code&gt;listener&lt;/code&gt;. Any outbound traffic that your virtual node expects to reach          should be specified as a &lt;code&gt;backend&lt;/code&gt;.&lt;/p&gt;          &lt;p&gt;The response metadata for your new virtual node contains the &lt;code&gt;arn&lt;/code&gt; that is          associated with the virtual node. Set this value (either the full ARN or the truncated          resource name, for example, &lt;code&gt;mesh/default/virtualNode/simpleapp&lt;/code&gt;, as the             &lt;code&gt;APPMESH_VIRTUAL_NODE_NAME&lt;/code&gt; environment variable for your task group&#39;s Envoy          proxy container in your task definition or pod spec. This is then mapped to the             &lt;code&gt;node.id&lt;/code&gt; and &lt;code&gt;node.cluster&lt;/code&gt; Envoy parameters.&lt;/p&gt;          &lt;note&gt;             &lt;p&gt;If you require your Envoy stats or tracing to use a different name, you can override             the &lt;code&gt;node.cluster&lt;/code&gt; value that is set by                &lt;code&gt;APPMESH_VIRTUAL_NODE_NAME&lt;/code&gt; with the                &lt;code&gt;APPMESH_VIRTUAL_NODE_CLUSTER&lt;/code&gt; environment variable.&lt;/p&gt;          &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://appmesh.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String meshName = "meshName_example"; // String | The name of the service mesh in which to create the virtual node.
    CreateVirtualNodeRequest createVirtualNodeRequest = new CreateVirtualNodeRequest(); // CreateVirtualNodeRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateVirtualNodeOutput result = apiInstance.createVirtualNode(meshName, createVirtualNodeRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createVirtualNode");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **meshName** | **String**| The name of the service mesh in which to create the virtual node. | |
| **createVirtualNodeRequest** | [**CreateVirtualNodeRequest**](CreateVirtualNodeRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateVirtualNodeOutput**](CreateVirtualNodeOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ConflictException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | InternalServerErrorException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | NotFoundException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | TooManyRequestsException |  -  |

<a id="createVirtualRouter"></a>
# **createVirtualRouter**
> CreateVirtualRouterOutput createVirtualRouter(meshName, createVirtualRouterRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a new virtual router within a service mesh.&lt;/p&gt;          &lt;p&gt;Virtual routers handle traffic for one or more service names within your mesh. After you          create your virtual router, create and associate routes for your virtual router that direct          incoming requests to different virtual nodes.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://appmesh.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String meshName = "meshName_example"; // String | The name of the service mesh in which to create the virtual router.
    CreateVirtualRouterRequest createVirtualRouterRequest = new CreateVirtualRouterRequest(); // CreateVirtualRouterRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateVirtualRouterOutput result = apiInstance.createVirtualRouter(meshName, createVirtualRouterRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createVirtualRouter");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **meshName** | **String**| The name of the service mesh in which to create the virtual router. | |
| **createVirtualRouterRequest** | [**CreateVirtualRouterRequest**](CreateVirtualRouterRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateVirtualRouterOutput**](CreateVirtualRouterOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ConflictException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | InternalServerErrorException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | NotFoundException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | TooManyRequestsException |  -  |

<a id="deleteMesh"></a>
# **deleteMesh**
> DeleteMeshOutput deleteMesh(meshName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes an existing service mesh.&lt;/p&gt;          &lt;p&gt;You must delete all resources (routes, virtual routers, virtual nodes) in the service          mesh before you can delete the mesh itself.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://appmesh.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String meshName = "meshName_example"; // String | The name of the service mesh to delete.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DeleteMeshOutput result = apiInstance.deleteMesh(meshName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteMesh");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **meshName** | **String**| The name of the service mesh to delete. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DeleteMeshOutput**](DeleteMeshOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | InternalServerErrorException |  -  |
| **483** | NotFoundException |  -  |
| **484** | ResourceInUseException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | TooManyRequestsException |  -  |

<a id="deleteRoute"></a>
# **deleteRoute**
> DeleteRouteOutput deleteRoute(meshName, routeName, virtualRouterName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Deletes an existing route.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://appmesh.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String meshName = "meshName_example"; // String | The name of the service mesh in which to delete the route.
    String routeName = "routeName_example"; // String | The name of the route to delete.
    String virtualRouterName = "virtualRouterName_example"; // String | The name of the virtual router in which to delete the route.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DeleteRouteOutput result = apiInstance.deleteRoute(meshName, routeName, virtualRouterName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteRoute");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **meshName** | **String**| The name of the service mesh in which to delete the route. | |
| **routeName** | **String**| The name of the route to delete. | |
| **virtualRouterName** | **String**| The name of the virtual router in which to delete the route. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DeleteRouteOutput**](DeleteRouteOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | InternalServerErrorException |  -  |
| **483** | NotFoundException |  -  |
| **484** | ResourceInUseException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | TooManyRequestsException |  -  |

<a id="deleteVirtualNode"></a>
# **deleteVirtualNode**
> DeleteVirtualNodeOutput deleteVirtualNode(meshName, virtualNodeName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Deletes an existing virtual node.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://appmesh.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String meshName = "meshName_example"; // String | The name of the service mesh in which to delete the virtual node.
    String virtualNodeName = "virtualNodeName_example"; // String | The name of the virtual node to delete.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DeleteVirtualNodeOutput result = apiInstance.deleteVirtualNode(meshName, virtualNodeName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteVirtualNode");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **meshName** | **String**| The name of the service mesh in which to delete the virtual node. | |
| **virtualNodeName** | **String**| The name of the virtual node to delete. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DeleteVirtualNodeOutput**](DeleteVirtualNodeOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | InternalServerErrorException |  -  |
| **483** | NotFoundException |  -  |
| **484** | ResourceInUseException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | TooManyRequestsException |  -  |

<a id="deleteVirtualRouter"></a>
# **deleteVirtualRouter**
> DeleteVirtualRouterOutput deleteVirtualRouter(meshName, virtualRouterName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes an existing virtual router.&lt;/p&gt;          &lt;p&gt;You must delete any routes associated with the virtual router before you can delete the          router itself.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://appmesh.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String meshName = "meshName_example"; // String | The name of the service mesh in which to delete the virtual router.
    String virtualRouterName = "virtualRouterName_example"; // String | The name of the virtual router to delete.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DeleteVirtualRouterOutput result = apiInstance.deleteVirtualRouter(meshName, virtualRouterName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteVirtualRouter");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **meshName** | **String**| The name of the service mesh in which to delete the virtual router. | |
| **virtualRouterName** | **String**| The name of the virtual router to delete. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DeleteVirtualRouterOutput**](DeleteVirtualRouterOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | InternalServerErrorException |  -  |
| **483** | NotFoundException |  -  |
| **484** | ResourceInUseException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | TooManyRequestsException |  -  |

<a id="describeMesh"></a>
# **describeMesh**
> DescribeMeshOutput describeMesh(meshName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Describes an existing service mesh.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://appmesh.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String meshName = "meshName_example"; // String | The name of the service mesh to describe.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeMeshOutput result = apiInstance.describeMesh(meshName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeMesh");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **meshName** | **String**| The name of the service mesh to describe. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeMeshOutput**](DescribeMeshOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | InternalServerErrorException |  -  |
| **483** | NotFoundException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | TooManyRequestsException |  -  |

<a id="describeRoute"></a>
# **describeRoute**
> DescribeRouteOutput describeRoute(meshName, routeName, virtualRouterName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Describes an existing route.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://appmesh.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String meshName = "meshName_example"; // String | The name of the service mesh in which the route resides.
    String routeName = "routeName_example"; // String | The name of the route to describe.
    String virtualRouterName = "virtualRouterName_example"; // String | The name of the virtual router with which the route is associated.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeRouteOutput result = apiInstance.describeRoute(meshName, routeName, virtualRouterName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeRoute");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **meshName** | **String**| The name of the service mesh in which the route resides. | |
| **routeName** | **String**| The name of the route to describe. | |
| **virtualRouterName** | **String**| The name of the virtual router with which the route is associated. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeRouteOutput**](DescribeRouteOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | InternalServerErrorException |  -  |
| **483** | NotFoundException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | TooManyRequestsException |  -  |

<a id="describeVirtualNode"></a>
# **describeVirtualNode**
> DescribeVirtualNodeOutput describeVirtualNode(meshName, virtualNodeName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Describes an existing virtual node.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://appmesh.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String meshName = "meshName_example"; // String | The name of the service mesh in which the virtual node resides.
    String virtualNodeName = "virtualNodeName_example"; // String | The name of the virtual node to describe.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeVirtualNodeOutput result = apiInstance.describeVirtualNode(meshName, virtualNodeName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeVirtualNode");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **meshName** | **String**| The name of the service mesh in which the virtual node resides. | |
| **virtualNodeName** | **String**| The name of the virtual node to describe. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeVirtualNodeOutput**](DescribeVirtualNodeOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | InternalServerErrorException |  -  |
| **483** | NotFoundException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | TooManyRequestsException |  -  |

<a id="describeVirtualRouter"></a>
# **describeVirtualRouter**
> DescribeVirtualRouterOutput describeVirtualRouter(meshName, virtualRouterName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Describes an existing virtual router.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://appmesh.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String meshName = "meshName_example"; // String | The name of the service mesh in which the virtual router resides.
    String virtualRouterName = "virtualRouterName_example"; // String | The name of the virtual router to describe.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeVirtualRouterOutput result = apiInstance.describeVirtualRouter(meshName, virtualRouterName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeVirtualRouter");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **meshName** | **String**| The name of the service mesh in which the virtual router resides. | |
| **virtualRouterName** | **String**| The name of the virtual router to describe. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeVirtualRouterOutput**](DescribeVirtualRouterOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | InternalServerErrorException |  -  |
| **483** | NotFoundException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | TooManyRequestsException |  -  |

<a id="listMeshes"></a>
# **listMeshes**
> ListMeshesOutput listMeshes(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, limit, nextToken)



Returns a list of existing service meshes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://appmesh.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Integer limit = 56; // Integer | The maximum number of mesh results returned by <code>ListMeshes</code> in paginated          output. When this parameter is used, <code>ListMeshes</code> only returns             <code>limit</code> results in a single page along with a <code>nextToken</code> response          element. The remaining results of the initial request can be seen by sending another             <code>ListMeshes</code> request with the returned <code>nextToken</code> value. This          value can be between 1 and 100. If this parameter is not          used, then <code>ListMeshes</code> returns up to 100 results and a             <code>nextToken</code> value if applicable.
    String nextToken = "nextToken_example"; // String | <p>The <code>nextToken</code> value returned from a previous paginated          <code>ListMeshes</code> request where <code>limit</code> was used and the          results exceeded the value of that parameter. Pagination continues from the end of the          previous results that returned the <code>nextToken</code> value.</p>          <note>             <p>This token should be treated as an opaque identifier that is only used to                 retrieve the next items in a list and not for other programmatic purposes.</p>         </note>
    try {
      ListMeshesOutput result = apiInstance.listMeshes(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, limit, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listMeshes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **limit** | **Integer**| The maximum number of mesh results returned by &lt;code&gt;ListMeshes&lt;/code&gt; in paginated          output. When this parameter is used, &lt;code&gt;ListMeshes&lt;/code&gt; only returns             &lt;code&gt;limit&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response          element. The remaining results of the initial request can be seen by sending another             &lt;code&gt;ListMeshes&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. This          value can be between 1 and 100. If this parameter is not          used, then &lt;code&gt;ListMeshes&lt;/code&gt; returns up to 100 results and a             &lt;code&gt;nextToken&lt;/code&gt; value if applicable. | [optional] |
| **nextToken** | **String**| &lt;p&gt;The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated          &lt;code&gt;ListMeshes&lt;/code&gt; request where &lt;code&gt;limit&lt;/code&gt; was used and the          results exceeded the value of that parameter. Pagination continues from the end of the          previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value.&lt;/p&gt;          &lt;note&gt;             &lt;p&gt;This token should be treated as an opaque identifier that is only used to                 retrieve the next items in a list and not for other programmatic purposes.&lt;/p&gt;         &lt;/note&gt; | [optional] |

### Return type

[**ListMeshesOutput**](ListMeshesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | InternalServerErrorException |  -  |
| **483** | NotFoundException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | TooManyRequestsException |  -  |

<a id="listRoutes"></a>
# **listRoutes**
> ListRoutesOutput listRoutes(meshName, virtualRouterName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, limit, nextToken)



Returns a list of existing routes in a service mesh.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://appmesh.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String meshName = "meshName_example"; // String | The name of the service mesh in which to list routes.
    String virtualRouterName = "virtualRouterName_example"; // String | The name of the virtual router in which to list routes.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Integer limit = 56; // Integer | The maximum number of mesh results returned by <code>ListRoutes</code> in paginated          output. When this parameter is used, <code>ListRoutes</code> only returns             <code>limit</code> results in a single page along with a <code>nextToken</code> response          element. The remaining results of the initial request can be seen by sending another             <code>ListRoutes</code> request with the returned <code>nextToken</code> value. This          value can be between 1 and 100. If this parameter is not          used, then <code>ListRoutes</code> returns up to 100 results and a             <code>nextToken</code> value if applicable.
    String nextToken = "nextToken_example"; // String | The <code>nextToken</code> value returned from a previous paginated          <code>ListRoutes</code> request where <code>limit</code> was used and the          results exceeded the value of that parameter. Pagination continues from the end of the          previous results that returned the <code>nextToken</code> value.
    try {
      ListRoutesOutput result = apiInstance.listRoutes(meshName, virtualRouterName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, limit, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listRoutes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **meshName** | **String**| The name of the service mesh in which to list routes. | |
| **virtualRouterName** | **String**| The name of the virtual router in which to list routes. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **limit** | **Integer**| The maximum number of mesh results returned by &lt;code&gt;ListRoutes&lt;/code&gt; in paginated          output. When this parameter is used, &lt;code&gt;ListRoutes&lt;/code&gt; only returns             &lt;code&gt;limit&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response          element. The remaining results of the initial request can be seen by sending another             &lt;code&gt;ListRoutes&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. This          value can be between 1 and 100. If this parameter is not          used, then &lt;code&gt;ListRoutes&lt;/code&gt; returns up to 100 results and a             &lt;code&gt;nextToken&lt;/code&gt; value if applicable. | [optional] |
| **nextToken** | **String**| The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated          &lt;code&gt;ListRoutes&lt;/code&gt; request where &lt;code&gt;limit&lt;/code&gt; was used and the          results exceeded the value of that parameter. Pagination continues from the end of the          previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value. | [optional] |

### Return type

[**ListRoutesOutput**](ListRoutesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | InternalServerErrorException |  -  |
| **483** | NotFoundException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | TooManyRequestsException |  -  |

<a id="listVirtualNodes"></a>
# **listVirtualNodes**
> ListVirtualNodesOutput listVirtualNodes(meshName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, limit, nextToken)



Returns a list of existing virtual nodes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://appmesh.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String meshName = "meshName_example"; // String | The name of the service mesh in which to list virtual nodes.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Integer limit = 56; // Integer | The maximum number of mesh results returned by <code>ListVirtualNodes</code> in          paginated output. When this parameter is used, <code>ListVirtualNodes</code> only returns          <code>limit</code> results in a single page along with a <code>nextToken</code>          response element. The remaining results of the initial request can be seen by sending          another <code>ListVirtualNodes</code> request with the returned <code>nextToken</code>          value. This value can be between 1 and 100. If this          parameter is not used, then <code>ListVirtualNodes</code> returns up to          100 results and a <code>nextToken</code> value if applicable.
    String nextToken = "nextToken_example"; // String | The <code>nextToken</code> value returned from a previous paginated          <code>ListVirtualNodes</code> request where <code>limit</code> was used and the          results exceeded the value of that parameter. Pagination continues from the end of the          previous results that returned the <code>nextToken</code> value.
    try {
      ListVirtualNodesOutput result = apiInstance.listVirtualNodes(meshName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, limit, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listVirtualNodes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **meshName** | **String**| The name of the service mesh in which to list virtual nodes. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **limit** | **Integer**| The maximum number of mesh results returned by &lt;code&gt;ListVirtualNodes&lt;/code&gt; in          paginated output. When this parameter is used, &lt;code&gt;ListVirtualNodes&lt;/code&gt; only returns          &lt;code&gt;limit&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt;          response element. The remaining results of the initial request can be seen by sending          another &lt;code&gt;ListVirtualNodes&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt;          value. This value can be between 1 and 100. If this          parameter is not used, then &lt;code&gt;ListVirtualNodes&lt;/code&gt; returns up to          100 results and a &lt;code&gt;nextToken&lt;/code&gt; value if applicable. | [optional] |
| **nextToken** | **String**| The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated          &lt;code&gt;ListVirtualNodes&lt;/code&gt; request where &lt;code&gt;limit&lt;/code&gt; was used and the          results exceeded the value of that parameter. Pagination continues from the end of the          previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value. | [optional] |

### Return type

[**ListVirtualNodesOutput**](ListVirtualNodesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | InternalServerErrorException |  -  |
| **483** | NotFoundException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | TooManyRequestsException |  -  |

<a id="listVirtualRouters"></a>
# **listVirtualRouters**
> ListVirtualRoutersOutput listVirtualRouters(meshName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, limit, nextToken)



Returns a list of existing virtual routers in a service mesh.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://appmesh.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String meshName = "meshName_example"; // String | The name of the service mesh in which to list virtual routers.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Integer limit = 56; // Integer | The maximum number of mesh results returned by <code>ListVirtualRouters</code> in          paginated output. When this parameter is used, <code>ListVirtualRouters</code> only returns          <code>limit</code> results in a single page along with a <code>nextToken</code>          response element. The remaining results of the initial request can be seen by sending          another <code>ListVirtualRouters</code> request with the returned <code>nextToken</code>          value. This value can be between 1 and 100. If this          parameter is not used, then <code>ListVirtualRouters</code> returns up to          100 results and a <code>nextToken</code> value if applicable.
    String nextToken = "nextToken_example"; // String | The <code>nextToken</code> value returned from a previous paginated          <code>ListVirtualRouters</code> request where <code>limit</code> was used and the          results exceeded the value of that parameter. Pagination continues from the end of the          previous results that returned the <code>nextToken</code> value.
    try {
      ListVirtualRoutersOutput result = apiInstance.listVirtualRouters(meshName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, limit, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listVirtualRouters");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **meshName** | **String**| The name of the service mesh in which to list virtual routers. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **limit** | **Integer**| The maximum number of mesh results returned by &lt;code&gt;ListVirtualRouters&lt;/code&gt; in          paginated output. When this parameter is used, &lt;code&gt;ListVirtualRouters&lt;/code&gt; only returns          &lt;code&gt;limit&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt;          response element. The remaining results of the initial request can be seen by sending          another &lt;code&gt;ListVirtualRouters&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt;          value. This value can be between 1 and 100. If this          parameter is not used, then &lt;code&gt;ListVirtualRouters&lt;/code&gt; returns up to          100 results and a &lt;code&gt;nextToken&lt;/code&gt; value if applicable. | [optional] |
| **nextToken** | **String**| The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated          &lt;code&gt;ListVirtualRouters&lt;/code&gt; request where &lt;code&gt;limit&lt;/code&gt; was used and the          results exceeded the value of that parameter. Pagination continues from the end of the          previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value. | [optional] |

### Return type

[**ListVirtualRoutersOutput**](ListVirtualRoutersOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | InternalServerErrorException |  -  |
| **483** | NotFoundException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | TooManyRequestsException |  -  |

<a id="updateRoute"></a>
# **updateRoute**
> UpdateRouteOutput updateRoute(meshName, routeName, virtualRouterName, updateRouteRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Updates an existing route for a specified service mesh and virtual router.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://appmesh.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String meshName = "meshName_example"; // String | The name of the service mesh in which the route resides.
    String routeName = "routeName_example"; // String | The name of the route to update.
    String virtualRouterName = "virtualRouterName_example"; // String | The name of the virtual router with which the route is associated.
    UpdateRouteRequest updateRouteRequest = new UpdateRouteRequest(); // UpdateRouteRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateRouteOutput result = apiInstance.updateRoute(meshName, routeName, virtualRouterName, updateRouteRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateRoute");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **meshName** | **String**| The name of the service mesh in which the route resides. | |
| **routeName** | **String**| The name of the route to update. | |
| **virtualRouterName** | **String**| The name of the virtual router with which the route is associated. | |
| **updateRouteRequest** | [**UpdateRouteRequest**](UpdateRouteRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateRouteOutput**](UpdateRouteOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ConflictException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | InternalServerErrorException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | NotFoundException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | TooManyRequestsException |  -  |

<a id="updateVirtualNode"></a>
# **updateVirtualNode**
> UpdateVirtualNodeOutput updateVirtualNode(meshName, virtualNodeName, updateVirtualNodeRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Updates an existing virtual node in a specified service mesh.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://appmesh.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String meshName = "meshName_example"; // String | The name of the service mesh in which the virtual node resides.
    String virtualNodeName = "virtualNodeName_example"; // String | The name of the virtual node to update.
    UpdateVirtualNodeRequest updateVirtualNodeRequest = new UpdateVirtualNodeRequest(); // UpdateVirtualNodeRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateVirtualNodeOutput result = apiInstance.updateVirtualNode(meshName, virtualNodeName, updateVirtualNodeRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateVirtualNode");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **meshName** | **String**| The name of the service mesh in which the virtual node resides. | |
| **virtualNodeName** | **String**| The name of the virtual node to update. | |
| **updateVirtualNodeRequest** | [**UpdateVirtualNodeRequest**](UpdateVirtualNodeRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateVirtualNodeOutput**](UpdateVirtualNodeOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ConflictException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | InternalServerErrorException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | NotFoundException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | TooManyRequestsException |  -  |

<a id="updateVirtualRouter"></a>
# **updateVirtualRouter**
> UpdateVirtualRouterOutput updateVirtualRouter(meshName, virtualRouterName, updateVirtualRouterRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Updates an existing virtual router in a specified service mesh.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://appmesh.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String meshName = "meshName_example"; // String | The name of the service mesh in which the virtual router resides.
    String virtualRouterName = "virtualRouterName_example"; // String | The name of the virtual router to update.
    UpdateVirtualRouterRequest updateVirtualRouterRequest = new UpdateVirtualRouterRequest(); // UpdateVirtualRouterRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateVirtualRouterOutput result = apiInstance.updateVirtualRouter(meshName, virtualRouterName, updateVirtualRouterRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateVirtualRouter");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **meshName** | **String**| The name of the service mesh in which the virtual router resides. | |
| **virtualRouterName** | **String**| The name of the virtual router to update. | |
| **updateVirtualRouterRequest** | [**UpdateVirtualRouterRequest**](UpdateVirtualRouterRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateVirtualRouterOutput**](UpdateVirtualRouterOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ConflictException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | InternalServerErrorException |  -  |
| **484** | LimitExceededException |  -  |
| **485** | NotFoundException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | TooManyRequestsException |  -  |

