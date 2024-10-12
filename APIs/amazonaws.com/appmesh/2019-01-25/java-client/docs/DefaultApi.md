# DefaultApi

All URIs are relative to *http://appmesh.us-east-1.amazonaws.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createGatewayRoute**](DefaultApi.md#createGatewayRoute) | **PUT** /v20190125/meshes/{meshName}/virtualGateway/{virtualGatewayName}/gatewayRoutes |  |
| [**createMesh**](DefaultApi.md#createMesh) | **PUT** /v20190125/meshes |  |
| [**createRoute**](DefaultApi.md#createRoute) | **PUT** /v20190125/meshes/{meshName}/virtualRouter/{virtualRouterName}/routes |  |
| [**createVirtualGateway**](DefaultApi.md#createVirtualGateway) | **PUT** /v20190125/meshes/{meshName}/virtualGateways |  |
| [**createVirtualNode**](DefaultApi.md#createVirtualNode) | **PUT** /v20190125/meshes/{meshName}/virtualNodes |  |
| [**createVirtualRouter**](DefaultApi.md#createVirtualRouter) | **PUT** /v20190125/meshes/{meshName}/virtualRouters |  |
| [**createVirtualService**](DefaultApi.md#createVirtualService) | **PUT** /v20190125/meshes/{meshName}/virtualServices |  |
| [**deleteGatewayRoute**](DefaultApi.md#deleteGatewayRoute) | **DELETE** /v20190125/meshes/{meshName}/virtualGateway/{virtualGatewayName}/gatewayRoutes/{gatewayRouteName} |  |
| [**deleteMesh**](DefaultApi.md#deleteMesh) | **DELETE** /v20190125/meshes/{meshName} |  |
| [**deleteRoute**](DefaultApi.md#deleteRoute) | **DELETE** /v20190125/meshes/{meshName}/virtualRouter/{virtualRouterName}/routes/{routeName} |  |
| [**deleteVirtualGateway**](DefaultApi.md#deleteVirtualGateway) | **DELETE** /v20190125/meshes/{meshName}/virtualGateways/{virtualGatewayName} |  |
| [**deleteVirtualNode**](DefaultApi.md#deleteVirtualNode) | **DELETE** /v20190125/meshes/{meshName}/virtualNodes/{virtualNodeName} |  |
| [**deleteVirtualRouter**](DefaultApi.md#deleteVirtualRouter) | **DELETE** /v20190125/meshes/{meshName}/virtualRouters/{virtualRouterName} |  |
| [**deleteVirtualService**](DefaultApi.md#deleteVirtualService) | **DELETE** /v20190125/meshes/{meshName}/virtualServices/{virtualServiceName} |  |
| [**describeGatewayRoute**](DefaultApi.md#describeGatewayRoute) | **GET** /v20190125/meshes/{meshName}/virtualGateway/{virtualGatewayName}/gatewayRoutes/{gatewayRouteName} |  |
| [**describeMesh**](DefaultApi.md#describeMesh) | **GET** /v20190125/meshes/{meshName} |  |
| [**describeRoute**](DefaultApi.md#describeRoute) | **GET** /v20190125/meshes/{meshName}/virtualRouter/{virtualRouterName}/routes/{routeName} |  |
| [**describeVirtualGateway**](DefaultApi.md#describeVirtualGateway) | **GET** /v20190125/meshes/{meshName}/virtualGateways/{virtualGatewayName} |  |
| [**describeVirtualNode**](DefaultApi.md#describeVirtualNode) | **GET** /v20190125/meshes/{meshName}/virtualNodes/{virtualNodeName} |  |
| [**describeVirtualRouter**](DefaultApi.md#describeVirtualRouter) | **GET** /v20190125/meshes/{meshName}/virtualRouters/{virtualRouterName} |  |
| [**describeVirtualService**](DefaultApi.md#describeVirtualService) | **GET** /v20190125/meshes/{meshName}/virtualServices/{virtualServiceName} |  |
| [**listGatewayRoutes**](DefaultApi.md#listGatewayRoutes) | **GET** /v20190125/meshes/{meshName}/virtualGateway/{virtualGatewayName}/gatewayRoutes |  |
| [**listMeshes**](DefaultApi.md#listMeshes) | **GET** /v20190125/meshes |  |
| [**listRoutes**](DefaultApi.md#listRoutes) | **GET** /v20190125/meshes/{meshName}/virtualRouter/{virtualRouterName}/routes |  |
| [**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /v20190125/tags#resourceArn |  |
| [**listVirtualGateways**](DefaultApi.md#listVirtualGateways) | **GET** /v20190125/meshes/{meshName}/virtualGateways |  |
| [**listVirtualNodes**](DefaultApi.md#listVirtualNodes) | **GET** /v20190125/meshes/{meshName}/virtualNodes |  |
| [**listVirtualRouters**](DefaultApi.md#listVirtualRouters) | **GET** /v20190125/meshes/{meshName}/virtualRouters |  |
| [**listVirtualServices**](DefaultApi.md#listVirtualServices) | **GET** /v20190125/meshes/{meshName}/virtualServices |  |
| [**tagResource**](DefaultApi.md#tagResource) | **PUT** /v20190125/tag#resourceArn |  |
| [**untagResource**](DefaultApi.md#untagResource) | **PUT** /v20190125/untag#resourceArn |  |
| [**updateGatewayRoute**](DefaultApi.md#updateGatewayRoute) | **PUT** /v20190125/meshes/{meshName}/virtualGateway/{virtualGatewayName}/gatewayRoutes/{gatewayRouteName} |  |
| [**updateMesh**](DefaultApi.md#updateMesh) | **PUT** /v20190125/meshes/{meshName} |  |
| [**updateRoute**](DefaultApi.md#updateRoute) | **PUT** /v20190125/meshes/{meshName}/virtualRouter/{virtualRouterName}/routes/{routeName} |  |
| [**updateVirtualGateway**](DefaultApi.md#updateVirtualGateway) | **PUT** /v20190125/meshes/{meshName}/virtualGateways/{virtualGatewayName} |  |
| [**updateVirtualNode**](DefaultApi.md#updateVirtualNode) | **PUT** /v20190125/meshes/{meshName}/virtualNodes/{virtualNodeName} |  |
| [**updateVirtualRouter**](DefaultApi.md#updateVirtualRouter) | **PUT** /v20190125/meshes/{meshName}/virtualRouters/{virtualRouterName} |  |
| [**updateVirtualService**](DefaultApi.md#updateVirtualService) | **PUT** /v20190125/meshes/{meshName}/virtualServices/{virtualServiceName} |  |


<a id="createGatewayRoute"></a>
# **createGatewayRoute**
> CreateGatewayRouteOutput createGatewayRoute(meshName, virtualGatewayName, createGatewayRouteRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner)



&lt;p&gt;Creates a gateway route.&lt;/p&gt; &lt;p&gt;A gateway route is attached to a virtual gateway and routes traffic to an existing virtual service. If a route matches a request, it can distribute traffic to a target virtual service.&lt;/p&gt; &lt;p&gt;For more information about gateway routes, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/gateway-routes.html\&quot;&gt;Gateway routes&lt;/a&gt;.&lt;/p&gt;

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
    String meshName = "meshName_example"; // String | The name of the service mesh to create the gateway route in.
    String virtualGatewayName = "virtualGatewayName_example"; // String | The name of the virtual gateway to associate the gateway route with. If the virtual gateway is in a shared mesh, then you must be the owner of the virtual gateway resource.
    CreateGatewayRouteRequest createGatewayRouteRequest = new CreateGatewayRouteRequest(); // CreateGatewayRouteRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String meshOwner = "meshOwner_example"; // String | The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then the account that you specify must share the mesh with your account before you can create the resource in the service mesh. For more information about mesh sharing, see <a href=\"https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\">Working with shared meshes</a>.
    try {
      CreateGatewayRouteOutput result = apiInstance.createGatewayRoute(meshName, virtualGatewayName, createGatewayRouteRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createGatewayRoute");
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
| **meshName** | **String**| The name of the service mesh to create the gateway route in. | |
| **virtualGatewayName** | **String**| The name of the virtual gateway to associate the gateway route with. If the virtual gateway is in a shared mesh, then you must be the owner of the virtual gateway resource. | |
| **createGatewayRouteRequest** | [**CreateGatewayRouteRequest**](CreateGatewayRouteRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **meshOwner** | **String**| The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then the account that you specify must share the mesh with your account before you can create the resource in the service mesh. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;. | [optional] |

### Return type

[**CreateGatewayRouteOutput**](CreateGatewayRouteOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | ConflictException |  -  |
| **483** | TooManyRequestsException |  -  |
| **484** | ForbiddenException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | InternalServerErrorException |  -  |
| **487** | LimitExceededException |  -  |

<a id="createMesh"></a>
# **createMesh**
> CreateMeshOutput createMesh(createMeshRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a service mesh.&lt;/p&gt; &lt;p&gt; A service mesh is a logical boundary for network traffic between services that are represented by resources within the mesh. After you create your service mesh, you can create virtual services, virtual nodes, virtual routers, and routes to distribute traffic between the applications in your mesh.&lt;/p&gt; &lt;p&gt;For more information about service meshes, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/meshes.html\&quot;&gt;Service meshes&lt;/a&gt;.&lt;/p&gt;

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
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | ConflictException |  -  |
| **483** | TooManyRequestsException |  -  |
| **484** | ForbiddenException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | InternalServerErrorException |  -  |
| **487** | LimitExceededException |  -  |

<a id="createRoute"></a>
# **createRoute**
> CreateRouteOutput createRoute(meshName, virtualRouterName, createRouteRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner)



&lt;p&gt;Creates a route that is associated with a virtual router.&lt;/p&gt; &lt;p&gt; You can route several different protocols and define a retry policy for a route. Traffic can be routed to one or more virtual nodes.&lt;/p&gt; &lt;p&gt;For more information about routes, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/routes.html\&quot;&gt;Routes&lt;/a&gt;.&lt;/p&gt;

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
    String meshName = "meshName_example"; // String | The name of the service mesh to create the route in.
    String virtualRouterName = "virtualRouterName_example"; // String | The name of the virtual router in which to create the route. If the virtual router is in a shared mesh, then you must be the owner of the virtual router resource.
    CreateRouteRequest createRouteRequest = new CreateRouteRequest(); // CreateRouteRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String meshOwner = "meshOwner_example"; // String | The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then the account that you specify must share the mesh with your account before you can create the resource in the service mesh. For more information about mesh sharing, see <a href=\"https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\">Working with shared meshes</a>.
    try {
      CreateRouteOutput result = apiInstance.createRoute(meshName, virtualRouterName, createRouteRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner);
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
| **meshName** | **String**| The name of the service mesh to create the route in. | |
| **virtualRouterName** | **String**| The name of the virtual router in which to create the route. If the virtual router is in a shared mesh, then you must be the owner of the virtual router resource. | |
| **createRouteRequest** | [**CreateRouteRequest**](CreateRouteRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **meshOwner** | **String**| The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then the account that you specify must share the mesh with your account before you can create the resource in the service mesh. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;. | [optional] |

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
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | ConflictException |  -  |
| **483** | TooManyRequestsException |  -  |
| **484** | ForbiddenException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | InternalServerErrorException |  -  |
| **487** | LimitExceededException |  -  |

<a id="createVirtualGateway"></a>
# **createVirtualGateway**
> CreateVirtualGatewayOutput createVirtualGateway(meshName, createVirtualGatewayRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner)



&lt;p&gt;Creates a virtual gateway.&lt;/p&gt; &lt;p&gt;A virtual gateway allows resources outside your mesh to communicate to resources that are inside your mesh. The virtual gateway represents an Envoy proxy running in an Amazon ECS task, in a Kubernetes service, or on an Amazon EC2 instance. Unlike a virtual node, which represents an Envoy running with an application, a virtual gateway represents Envoy deployed by itself.&lt;/p&gt; &lt;p&gt;For more information about virtual gateways, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_gateways.html\&quot;&gt;Virtual gateways&lt;/a&gt;. &lt;/p&gt;

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
    String meshName = "meshName_example"; // String | The name of the service mesh to create the virtual gateway in.
    CreateVirtualGatewayRequest createVirtualGatewayRequest = new CreateVirtualGatewayRequest(); // CreateVirtualGatewayRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String meshOwner = "meshOwner_example"; // String | The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then the account that you specify must share the mesh with your account before you can create the resource in the service mesh. For more information about mesh sharing, see <a href=\"https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\">Working with shared meshes</a>.
    try {
      CreateVirtualGatewayOutput result = apiInstance.createVirtualGateway(meshName, createVirtualGatewayRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createVirtualGateway");
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
| **meshName** | **String**| The name of the service mesh to create the virtual gateway in. | |
| **createVirtualGatewayRequest** | [**CreateVirtualGatewayRequest**](CreateVirtualGatewayRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **meshOwner** | **String**| The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then the account that you specify must share the mesh with your account before you can create the resource in the service mesh. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;. | [optional] |

### Return type

[**CreateVirtualGatewayOutput**](CreateVirtualGatewayOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | ConflictException |  -  |
| **483** | TooManyRequestsException |  -  |
| **484** | ForbiddenException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | InternalServerErrorException |  -  |
| **487** | LimitExceededException |  -  |

<a id="createVirtualNode"></a>
# **createVirtualNode**
> CreateVirtualNodeOutput createVirtualNode(meshName, createVirtualNodeRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner)



&lt;p&gt;Creates a virtual node within a service mesh.&lt;/p&gt; &lt;p&gt; A virtual node acts as a logical pointer to a particular task group, such as an Amazon ECS service or a Kubernetes deployment. When you create a virtual node, you can specify the service discovery information for your task group, and whether the proxy running in a task group will communicate with other proxies using Transport Layer Security (TLS).&lt;/p&gt; &lt;p&gt;You define a &lt;code&gt;listener&lt;/code&gt; for any inbound traffic that your virtual node expects. Any virtual service that your virtual node expects to communicate to is specified as a &lt;code&gt;backend&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;The response metadata for your new virtual node contains the &lt;code&gt;arn&lt;/code&gt; that is associated with the virtual node. Set this value to the full ARN; for example, &lt;code&gt;arn:aws:appmesh:us-west-2:123456789012:myMesh/default/virtualNode/myApp&lt;/code&gt;) as the &lt;code&gt;APPMESH_RESOURCE_ARN&lt;/code&gt; environment variable for your task group&#39;s Envoy proxy container in your task definition or pod spec. This is then mapped to the &lt;code&gt;node.id&lt;/code&gt; and &lt;code&gt;node.cluster&lt;/code&gt; Envoy parameters.&lt;/p&gt; &lt;note&gt; &lt;p&gt;By default, App Mesh uses the name of the resource you specified in &lt;code&gt;APPMESH_RESOURCE_ARN&lt;/code&gt; when Envoy is referring to itself in metrics and traces. You can override this behavior by setting the &lt;code&gt;APPMESH_RESOURCE_CLUSTER&lt;/code&gt; environment variable with your own name.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;For more information about virtual nodes, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_nodes.html\&quot;&gt;Virtual nodes&lt;/a&gt;. You must be using &lt;code&gt;1.15.0&lt;/code&gt; or later of the Envoy image when setting these variables. For more information aboutApp Mesh Envoy variables, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/envoy.html\&quot;&gt;Envoy image&lt;/a&gt; in the App Mesh User Guide.&lt;/p&gt;

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
    String meshName = "meshName_example"; // String | The name of the service mesh to create the virtual node in.
    CreateVirtualNodeRequest createVirtualNodeRequest = new CreateVirtualNodeRequest(); // CreateVirtualNodeRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String meshOwner = "meshOwner_example"; // String | The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then the account that you specify must share the mesh with your account before you can create the resource in the service mesh. For more information about mesh sharing, see <a href=\"https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\">Working with shared meshes</a>.
    try {
      CreateVirtualNodeOutput result = apiInstance.createVirtualNode(meshName, createVirtualNodeRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner);
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
| **meshName** | **String**| The name of the service mesh to create the virtual node in. | |
| **createVirtualNodeRequest** | [**CreateVirtualNodeRequest**](CreateVirtualNodeRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **meshOwner** | **String**| The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then the account that you specify must share the mesh with your account before you can create the resource in the service mesh. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;. | [optional] |

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
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | ConflictException |  -  |
| **483** | TooManyRequestsException |  -  |
| **484** | ForbiddenException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | InternalServerErrorException |  -  |
| **487** | LimitExceededException |  -  |

<a id="createVirtualRouter"></a>
# **createVirtualRouter**
> CreateVirtualRouterOutput createVirtualRouter(meshName, createVirtualRouterRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner)



&lt;p&gt;Creates a virtual router within a service mesh.&lt;/p&gt; &lt;p&gt;Specify a &lt;code&gt;listener&lt;/code&gt; for any inbound traffic that your virtual router receives. Create a virtual router for each protocol and port that you need to route. Virtual routers handle traffic for one or more virtual services within your mesh. After you create your virtual router, create and associate routes for your virtual router that direct incoming requests to different virtual nodes.&lt;/p&gt; &lt;p&gt;For more information about virtual routers, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_routers.html\&quot;&gt;Virtual routers&lt;/a&gt;.&lt;/p&gt;

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
    String meshName = "meshName_example"; // String | The name of the service mesh to create the virtual router in.
    CreateVirtualRouterRequest createVirtualRouterRequest = new CreateVirtualRouterRequest(); // CreateVirtualRouterRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String meshOwner = "meshOwner_example"; // String | The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then the account that you specify must share the mesh with your account before you can create the resource in the service mesh. For more information about mesh sharing, see <a href=\"https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\">Working with shared meshes</a>.
    try {
      CreateVirtualRouterOutput result = apiInstance.createVirtualRouter(meshName, createVirtualRouterRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner);
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
| **meshName** | **String**| The name of the service mesh to create the virtual router in. | |
| **createVirtualRouterRequest** | [**CreateVirtualRouterRequest**](CreateVirtualRouterRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **meshOwner** | **String**| The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then the account that you specify must share the mesh with your account before you can create the resource in the service mesh. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;. | [optional] |

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
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | ConflictException |  -  |
| **483** | TooManyRequestsException |  -  |
| **484** | ForbiddenException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | InternalServerErrorException |  -  |
| **487** | LimitExceededException |  -  |

<a id="createVirtualService"></a>
# **createVirtualService**
> CreateVirtualServiceOutput createVirtualService(meshName, createVirtualServiceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner)



&lt;p&gt;Creates a virtual service within a service mesh.&lt;/p&gt; &lt;p&gt;A virtual service is an abstraction of a real service that is provided by a virtual node directly or indirectly by means of a virtual router. Dependent services call your virtual service by its &lt;code&gt;virtualServiceName&lt;/code&gt;, and those requests are routed to the virtual node or virtual router that is specified as the provider for the virtual service.&lt;/p&gt; &lt;p&gt;For more information about virtual services, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_services.html\&quot;&gt;Virtual services&lt;/a&gt;.&lt;/p&gt;

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
    String meshName = "meshName_example"; // String | The name of the service mesh to create the virtual service in.
    CreateVirtualServiceRequest createVirtualServiceRequest = new CreateVirtualServiceRequest(); // CreateVirtualServiceRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String meshOwner = "meshOwner_example"; // String | The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then the account that you specify must share the mesh with your account before you can create the resource in the service mesh. For more information about mesh sharing, see <a href=\"https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\">Working with shared meshes</a>.
    try {
      CreateVirtualServiceOutput result = apiInstance.createVirtualService(meshName, createVirtualServiceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createVirtualService");
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
| **meshName** | **String**| The name of the service mesh to create the virtual service in. | |
| **createVirtualServiceRequest** | [**CreateVirtualServiceRequest**](CreateVirtualServiceRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **meshOwner** | **String**| The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then the account that you specify must share the mesh with your account before you can create the resource in the service mesh. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;. | [optional] |

### Return type

[**CreateVirtualServiceOutput**](CreateVirtualServiceOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | ConflictException |  -  |
| **483** | TooManyRequestsException |  -  |
| **484** | ForbiddenException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | InternalServerErrorException |  -  |
| **487** | LimitExceededException |  -  |

<a id="deleteGatewayRoute"></a>
# **deleteGatewayRoute**
> DeleteGatewayRouteOutput deleteGatewayRoute(gatewayRouteName, meshName, virtualGatewayName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner)



Deletes an existing gateway route.

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
    String gatewayRouteName = "gatewayRouteName_example"; // String | The name of the gateway route to delete.
    String meshName = "meshName_example"; // String | The name of the service mesh to delete the gateway route from.
    String virtualGatewayName = "virtualGatewayName_example"; // String | The name of the virtual gateway to delete the route from.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String meshOwner = "meshOwner_example"; // String | The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href=\"https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\">Working with shared meshes</a>.
    try {
      DeleteGatewayRouteOutput result = apiInstance.deleteGatewayRoute(gatewayRouteName, meshName, virtualGatewayName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteGatewayRoute");
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
| **gatewayRouteName** | **String**| The name of the gateway route to delete. | |
| **meshName** | **String**| The name of the service mesh to delete the gateway route from. | |
| **virtualGatewayName** | **String**| The name of the virtual gateway to delete the route from. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **meshOwner** | **String**| The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;. | [optional] |

### Return type

[**DeleteGatewayRouteOutput**](DeleteGatewayRouteOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | TooManyRequestsException |  -  |
| **483** | ForbiddenException |  -  |
| **484** | ResourceInUseException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | InternalServerErrorException |  -  |

<a id="deleteMesh"></a>
# **deleteMesh**
> DeleteMeshOutput deleteMesh(meshName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes an existing service mesh.&lt;/p&gt; &lt;p&gt;You must delete all resources (virtual services, routes, virtual routers, and virtual nodes) in the service mesh before you can delete the mesh itself.&lt;/p&gt;

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
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | TooManyRequestsException |  -  |
| **483** | ForbiddenException |  -  |
| **484** | ResourceInUseException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | InternalServerErrorException |  -  |

<a id="deleteRoute"></a>
# **deleteRoute**
> DeleteRouteOutput deleteRoute(meshName, routeName, virtualRouterName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner)



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
    String meshName = "meshName_example"; // String | The name of the service mesh to delete the route in.
    String routeName = "routeName_example"; // String | The name of the route to delete.
    String virtualRouterName = "virtualRouterName_example"; // String | The name of the virtual router to delete the route in.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String meshOwner = "meshOwner_example"; // String | The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href=\"https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\">Working with shared meshes</a>.
    try {
      DeleteRouteOutput result = apiInstance.deleteRoute(meshName, routeName, virtualRouterName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner);
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
| **meshName** | **String**| The name of the service mesh to delete the route in. | |
| **routeName** | **String**| The name of the route to delete. | |
| **virtualRouterName** | **String**| The name of the virtual router to delete the route in. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **meshOwner** | **String**| The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;. | [optional] |

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
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | TooManyRequestsException |  -  |
| **483** | ForbiddenException |  -  |
| **484** | ResourceInUseException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | InternalServerErrorException |  -  |

<a id="deleteVirtualGateway"></a>
# **deleteVirtualGateway**
> DeleteVirtualGatewayOutput deleteVirtualGateway(meshName, virtualGatewayName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner)



Deletes an existing virtual gateway. You cannot delete a virtual gateway if any gateway routes are associated to it.

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
    String meshName = "meshName_example"; // String | The name of the service mesh to delete the virtual gateway from.
    String virtualGatewayName = "virtualGatewayName_example"; // String | The name of the virtual gateway to delete.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String meshOwner = "meshOwner_example"; // String | The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href=\"https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\">Working with shared meshes</a>.
    try {
      DeleteVirtualGatewayOutput result = apiInstance.deleteVirtualGateway(meshName, virtualGatewayName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteVirtualGateway");
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
| **meshName** | **String**| The name of the service mesh to delete the virtual gateway from. | |
| **virtualGatewayName** | **String**| The name of the virtual gateway to delete. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **meshOwner** | **String**| The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;. | [optional] |

### Return type

[**DeleteVirtualGatewayOutput**](DeleteVirtualGatewayOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | TooManyRequestsException |  -  |
| **483** | ForbiddenException |  -  |
| **484** | ResourceInUseException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | InternalServerErrorException |  -  |

<a id="deleteVirtualNode"></a>
# **deleteVirtualNode**
> DeleteVirtualNodeOutput deleteVirtualNode(meshName, virtualNodeName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner)



&lt;p&gt;Deletes an existing virtual node.&lt;/p&gt; &lt;p&gt;You must delete any virtual services that list a virtual node as a service provider before you can delete the virtual node itself.&lt;/p&gt;

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
    String meshName = "meshName_example"; // String | The name of the service mesh to delete the virtual node in.
    String virtualNodeName = "virtualNodeName_example"; // String | The name of the virtual node to delete.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String meshOwner = "meshOwner_example"; // String | The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href=\"https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\">Working with shared meshes</a>.
    try {
      DeleteVirtualNodeOutput result = apiInstance.deleteVirtualNode(meshName, virtualNodeName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner);
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
| **meshName** | **String**| The name of the service mesh to delete the virtual node in. | |
| **virtualNodeName** | **String**| The name of the virtual node to delete. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **meshOwner** | **String**| The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;. | [optional] |

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
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | TooManyRequestsException |  -  |
| **483** | ForbiddenException |  -  |
| **484** | ResourceInUseException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | InternalServerErrorException |  -  |

<a id="deleteVirtualRouter"></a>
# **deleteVirtualRouter**
> DeleteVirtualRouterOutput deleteVirtualRouter(meshName, virtualRouterName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner)



&lt;p&gt;Deletes an existing virtual router.&lt;/p&gt; &lt;p&gt;You must delete any routes associated with the virtual router before you can delete the router itself.&lt;/p&gt;

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
    String meshName = "meshName_example"; // String | The name of the service mesh to delete the virtual router in.
    String virtualRouterName = "virtualRouterName_example"; // String | The name of the virtual router to delete.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String meshOwner = "meshOwner_example"; // String | The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href=\"https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\">Working with shared meshes</a>.
    try {
      DeleteVirtualRouterOutput result = apiInstance.deleteVirtualRouter(meshName, virtualRouterName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner);
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
| **meshName** | **String**| The name of the service mesh to delete the virtual router in. | |
| **virtualRouterName** | **String**| The name of the virtual router to delete. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **meshOwner** | **String**| The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;. | [optional] |

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
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | TooManyRequestsException |  -  |
| **483** | ForbiddenException |  -  |
| **484** | ResourceInUseException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | InternalServerErrorException |  -  |

<a id="deleteVirtualService"></a>
# **deleteVirtualService**
> DeleteVirtualServiceOutput deleteVirtualService(meshName, virtualServiceName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner)



Deletes an existing virtual service.

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
    String meshName = "meshName_example"; // String | The name of the service mesh to delete the virtual service in.
    String virtualServiceName = "virtualServiceName_example"; // String | The name of the virtual service to delete.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String meshOwner = "meshOwner_example"; // String | The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href=\"https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\">Working with shared meshes</a>.
    try {
      DeleteVirtualServiceOutput result = apiInstance.deleteVirtualService(meshName, virtualServiceName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteVirtualService");
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
| **meshName** | **String**| The name of the service mesh to delete the virtual service in. | |
| **virtualServiceName** | **String**| The name of the virtual service to delete. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **meshOwner** | **String**| The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;. | [optional] |

### Return type

[**DeleteVirtualServiceOutput**](DeleteVirtualServiceOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | TooManyRequestsException |  -  |
| **483** | ForbiddenException |  -  |
| **484** | ResourceInUseException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | InternalServerErrorException |  -  |

<a id="describeGatewayRoute"></a>
# **describeGatewayRoute**
> DescribeGatewayRouteOutput describeGatewayRoute(gatewayRouteName, meshName, virtualGatewayName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner)



Describes an existing gateway route.

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
    String gatewayRouteName = "gatewayRouteName_example"; // String | The name of the gateway route to describe.
    String meshName = "meshName_example"; // String | The name of the service mesh that the gateway route resides in.
    String virtualGatewayName = "virtualGatewayName_example"; // String | The name of the virtual gateway that the gateway route is associated with.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String meshOwner = "meshOwner_example"; // String | The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href=\"https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\">Working with shared meshes</a>.
    try {
      DescribeGatewayRouteOutput result = apiInstance.describeGatewayRoute(gatewayRouteName, meshName, virtualGatewayName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeGatewayRoute");
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
| **gatewayRouteName** | **String**| The name of the gateway route to describe. | |
| **meshName** | **String**| The name of the service mesh that the gateway route resides in. | |
| **virtualGatewayName** | **String**| The name of the virtual gateway that the gateway route is associated with. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **meshOwner** | **String**| The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;. | [optional] |

### Return type

[**DescribeGatewayRouteOutput**](DescribeGatewayRouteOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | TooManyRequestsException |  -  |
| **483** | ForbiddenException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | InternalServerErrorException |  -  |

<a id="describeMesh"></a>
# **describeMesh**
> DescribeMeshOutput describeMesh(meshName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner)



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
    String meshOwner = "meshOwner_example"; // String | The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href=\"https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\">Working with shared meshes</a>.
    try {
      DescribeMeshOutput result = apiInstance.describeMesh(meshName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner);
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
| **meshOwner** | **String**| The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;. | [optional] |

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
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | TooManyRequestsException |  -  |
| **483** | ForbiddenException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | InternalServerErrorException |  -  |

<a id="describeRoute"></a>
# **describeRoute**
> DescribeRouteOutput describeRoute(meshName, routeName, virtualRouterName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner)



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
    String meshName = "meshName_example"; // String | The name of the service mesh that the route resides in.
    String routeName = "routeName_example"; // String | The name of the route to describe.
    String virtualRouterName = "virtualRouterName_example"; // String | The name of the virtual router that the route is associated with.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String meshOwner = "meshOwner_example"; // String | The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href=\"https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\">Working with shared meshes</a>.
    try {
      DescribeRouteOutput result = apiInstance.describeRoute(meshName, routeName, virtualRouterName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner);
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
| **meshName** | **String**| The name of the service mesh that the route resides in. | |
| **routeName** | **String**| The name of the route to describe. | |
| **virtualRouterName** | **String**| The name of the virtual router that the route is associated with. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **meshOwner** | **String**| The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;. | [optional] |

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
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | TooManyRequestsException |  -  |
| **483** | ForbiddenException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | InternalServerErrorException |  -  |

<a id="describeVirtualGateway"></a>
# **describeVirtualGateway**
> DescribeVirtualGatewayOutput describeVirtualGateway(meshName, virtualGatewayName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner)



Describes an existing virtual gateway.

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
    String meshName = "meshName_example"; // String | The name of the service mesh that the gateway route resides in.
    String virtualGatewayName = "virtualGatewayName_example"; // String | The name of the virtual gateway to describe.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String meshOwner = "meshOwner_example"; // String | The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href=\"https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\">Working with shared meshes</a>.
    try {
      DescribeVirtualGatewayOutput result = apiInstance.describeVirtualGateway(meshName, virtualGatewayName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeVirtualGateway");
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
| **meshName** | **String**| The name of the service mesh that the gateway route resides in. | |
| **virtualGatewayName** | **String**| The name of the virtual gateway to describe. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **meshOwner** | **String**| The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;. | [optional] |

### Return type

[**DescribeVirtualGatewayOutput**](DescribeVirtualGatewayOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | TooManyRequestsException |  -  |
| **483** | ForbiddenException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | InternalServerErrorException |  -  |

<a id="describeVirtualNode"></a>
# **describeVirtualNode**
> DescribeVirtualNodeOutput describeVirtualNode(meshName, virtualNodeName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner)



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
    String meshName = "meshName_example"; // String | The name of the service mesh that the virtual node resides in.
    String virtualNodeName = "virtualNodeName_example"; // String | The name of the virtual node to describe.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String meshOwner = "meshOwner_example"; // String | The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href=\"https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\">Working with shared meshes</a>.
    try {
      DescribeVirtualNodeOutput result = apiInstance.describeVirtualNode(meshName, virtualNodeName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner);
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
| **meshName** | **String**| The name of the service mesh that the virtual node resides in. | |
| **virtualNodeName** | **String**| The name of the virtual node to describe. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **meshOwner** | **String**| The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;. | [optional] |

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
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | TooManyRequestsException |  -  |
| **483** | ForbiddenException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | InternalServerErrorException |  -  |

<a id="describeVirtualRouter"></a>
# **describeVirtualRouter**
> DescribeVirtualRouterOutput describeVirtualRouter(meshName, virtualRouterName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner)



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
    String meshName = "meshName_example"; // String | The name of the service mesh that the virtual router resides in.
    String virtualRouterName = "virtualRouterName_example"; // String | The name of the virtual router to describe.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String meshOwner = "meshOwner_example"; // String | The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href=\"https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\">Working with shared meshes</a>.
    try {
      DescribeVirtualRouterOutput result = apiInstance.describeVirtualRouter(meshName, virtualRouterName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner);
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
| **meshName** | **String**| The name of the service mesh that the virtual router resides in. | |
| **virtualRouterName** | **String**| The name of the virtual router to describe. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **meshOwner** | **String**| The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;. | [optional] |

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
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | TooManyRequestsException |  -  |
| **483** | ForbiddenException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | InternalServerErrorException |  -  |

<a id="describeVirtualService"></a>
# **describeVirtualService**
> DescribeVirtualServiceOutput describeVirtualService(meshName, virtualServiceName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner)



Describes an existing virtual service.

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
    String meshName = "meshName_example"; // String | The name of the service mesh that the virtual service resides in.
    String virtualServiceName = "virtualServiceName_example"; // String | The name of the virtual service to describe.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String meshOwner = "meshOwner_example"; // String | The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href=\"https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\">Working with shared meshes</a>.
    try {
      DescribeVirtualServiceOutput result = apiInstance.describeVirtualService(meshName, virtualServiceName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeVirtualService");
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
| **meshName** | **String**| The name of the service mesh that the virtual service resides in. | |
| **virtualServiceName** | **String**| The name of the virtual service to describe. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **meshOwner** | **String**| The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;. | [optional] |

### Return type

[**DescribeVirtualServiceOutput**](DescribeVirtualServiceOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | TooManyRequestsException |  -  |
| **483** | ForbiddenException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | InternalServerErrorException |  -  |

<a id="listGatewayRoutes"></a>
# **listGatewayRoutes**
> ListGatewayRoutesOutput listGatewayRoutes(meshName, virtualGatewayName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, limit, meshOwner, nextToken)



Returns a list of existing gateway routes that are associated to a virtual gateway.

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
    String meshName = "meshName_example"; // String | The name of the service mesh to list gateway routes in.
    String virtualGatewayName = "virtualGatewayName_example"; // String | The name of the virtual gateway to list gateway routes in.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Integer limit = 56; // Integer | The maximum number of results returned by <code>ListGatewayRoutes</code> in paginated output. When you use this parameter, <code>ListGatewayRoutes</code> returns only <code>limit</code> results in a single page along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another <code>ListGatewayRoutes</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, <code>ListGatewayRoutes</code> returns up to 100 results and a <code>nextToken</code> value if applicable.
    String meshOwner = "meshOwner_example"; // String | The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href=\"https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\">Working with shared meshes</a>.
    String nextToken = "nextToken_example"; // String | The <code>nextToken</code> value returned from a previous paginated <code>ListGatewayRoutes</code> request where <code>limit</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value.
    try {
      ListGatewayRoutesOutput result = apiInstance.listGatewayRoutes(meshName, virtualGatewayName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, limit, meshOwner, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listGatewayRoutes");
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
| **meshName** | **String**| The name of the service mesh to list gateway routes in. | |
| **virtualGatewayName** | **String**| The name of the virtual gateway to list gateway routes in. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **limit** | **Integer**| The maximum number of results returned by &lt;code&gt;ListGatewayRoutes&lt;/code&gt; in paginated output. When you use this parameter, &lt;code&gt;ListGatewayRoutes&lt;/code&gt; returns only &lt;code&gt;limit&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response element. You can see the remaining results of the initial request by sending another &lt;code&gt;ListGatewayRoutes&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. This value can be between 1 and 100. If you don&#39;t use this parameter, &lt;code&gt;ListGatewayRoutes&lt;/code&gt; returns up to 100 results and a &lt;code&gt;nextToken&lt;/code&gt; value if applicable. | [optional] |
| **meshOwner** | **String**| The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;. | [optional] |
| **nextToken** | **String**| The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated &lt;code&gt;ListGatewayRoutes&lt;/code&gt; request where &lt;code&gt;limit&lt;/code&gt; was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value. | [optional] |

### Return type

[**ListGatewayRoutesOutput**](ListGatewayRoutesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | TooManyRequestsException |  -  |
| **483** | ForbiddenException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | InternalServerErrorException |  -  |

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
    Integer limit = 56; // Integer | The maximum number of results returned by <code>ListMeshes</code> in paginated output. When you use this parameter, <code>ListMeshes</code> returns only <code>limit</code> results in a single page along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another <code>ListMeshes</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, <code>ListMeshes</code> returns up to 100 results and a <code>nextToken</code> value if applicable.
    String nextToken = "nextToken_example"; // String | <p>The <code>nextToken</code> value returned from a previous paginated <code>ListMeshes</code> request where <code>limit</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value.</p> <note> <p>This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
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
| **limit** | **Integer**| The maximum number of results returned by &lt;code&gt;ListMeshes&lt;/code&gt; in paginated output. When you use this parameter, &lt;code&gt;ListMeshes&lt;/code&gt; returns only &lt;code&gt;limit&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response element. You can see the remaining results of the initial request by sending another &lt;code&gt;ListMeshes&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. This value can be between 1 and 100. If you don&#39;t use this parameter, &lt;code&gt;ListMeshes&lt;/code&gt; returns up to 100 results and a &lt;code&gt;nextToken&lt;/code&gt; value if applicable. | [optional] |
| **nextToken** | **String**| &lt;p&gt;The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated &lt;code&gt;ListMeshes&lt;/code&gt; request where &lt;code&gt;limit&lt;/code&gt; was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.&lt;/p&gt; &lt;/note&gt; | [optional] |

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
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | TooManyRequestsException |  -  |
| **483** | ForbiddenException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | InternalServerErrorException |  -  |

<a id="listRoutes"></a>
# **listRoutes**
> ListRoutesOutput listRoutes(meshName, virtualRouterName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, limit, meshOwner, nextToken)



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
    String meshName = "meshName_example"; // String | The name of the service mesh to list routes in.
    String virtualRouterName = "virtualRouterName_example"; // String | The name of the virtual router to list routes in.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Integer limit = 56; // Integer | The maximum number of results returned by <code>ListRoutes</code> in paginated output. When you use this parameter, <code>ListRoutes</code> returns only <code>limit</code> results in a single page along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another <code>ListRoutes</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, <code>ListRoutes</code> returns up to 100 results and a <code>nextToken</code> value if applicable.
    String meshOwner = "meshOwner_example"; // String | The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href=\"https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\">Working with shared meshes</a>.
    String nextToken = "nextToken_example"; // String | The <code>nextToken</code> value returned from a previous paginated <code>ListRoutes</code> request where <code>limit</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value.
    try {
      ListRoutesOutput result = apiInstance.listRoutes(meshName, virtualRouterName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, limit, meshOwner, nextToken);
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
| **meshName** | **String**| The name of the service mesh to list routes in. | |
| **virtualRouterName** | **String**| The name of the virtual router to list routes in. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **limit** | **Integer**| The maximum number of results returned by &lt;code&gt;ListRoutes&lt;/code&gt; in paginated output. When you use this parameter, &lt;code&gt;ListRoutes&lt;/code&gt; returns only &lt;code&gt;limit&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response element. You can see the remaining results of the initial request by sending another &lt;code&gt;ListRoutes&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. This value can be between 1 and 100. If you don&#39;t use this parameter, &lt;code&gt;ListRoutes&lt;/code&gt; returns up to 100 results and a &lt;code&gt;nextToken&lt;/code&gt; value if applicable. | [optional] |
| **meshOwner** | **String**| The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;. | [optional] |
| **nextToken** | **String**| The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated &lt;code&gt;ListRoutes&lt;/code&gt; request where &lt;code&gt;limit&lt;/code&gt; was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value. | [optional] |

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
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | TooManyRequestsException |  -  |
| **483** | ForbiddenException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | InternalServerErrorException |  -  |

<a id="listTagsForResource"></a>
# **listTagsForResource**
> ListTagsForResourceOutput listTagsForResource(resourceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, limit, nextToken)



List the tags for an App Mesh resource.

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
    String resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) that identifies the resource to list the tags for.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Integer limit = 56; // Integer | The maximum number of tag results returned by <code>ListTagsForResource</code> in paginated output. When this parameter is used, <code>ListTagsForResource</code> returns only <code>limit</code> results in a single page along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another <code>ListTagsForResource</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, <code>ListTagsForResource</code> returns up to 100 results and a <code>nextToken</code> value if applicable.
    String nextToken = "nextToken_example"; // String | The <code>nextToken</code> value returned from a previous paginated <code>ListTagsForResource</code> request where <code>limit</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value.
    try {
      ListTagsForResourceOutput result = apiInstance.listTagsForResource(resourceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, limit, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listTagsForResource");
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
| **resourceArn** | **String**| The Amazon Resource Name (ARN) that identifies the resource to list the tags for. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **limit** | **Integer**| The maximum number of tag results returned by &lt;code&gt;ListTagsForResource&lt;/code&gt; in paginated output. When this parameter is used, &lt;code&gt;ListTagsForResource&lt;/code&gt; returns only &lt;code&gt;limit&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response element. You can see the remaining results of the initial request by sending another &lt;code&gt;ListTagsForResource&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. This value can be between 1 and 100. If you don&#39;t use this parameter, &lt;code&gt;ListTagsForResource&lt;/code&gt; returns up to 100 results and a &lt;code&gt;nextToken&lt;/code&gt; value if applicable. | [optional] |
| **nextToken** | **String**| The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated &lt;code&gt;ListTagsForResource&lt;/code&gt; request where &lt;code&gt;limit&lt;/code&gt; was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value. | [optional] |

### Return type

[**ListTagsForResourceOutput**](ListTagsForResourceOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | TooManyRequestsException |  -  |
| **483** | ForbiddenException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | InternalServerErrorException |  -  |

<a id="listVirtualGateways"></a>
# **listVirtualGateways**
> ListVirtualGatewaysOutput listVirtualGateways(meshName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, limit, meshOwner, nextToken)



Returns a list of existing virtual gateways in a service mesh.

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
    String meshName = "meshName_example"; // String | The name of the service mesh to list virtual gateways in.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Integer limit = 56; // Integer | The maximum number of results returned by <code>ListVirtualGateways</code> in paginated output. When you use this parameter, <code>ListVirtualGateways</code> returns only <code>limit</code> results in a single page along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another <code>ListVirtualGateways</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, <code>ListVirtualGateways</code> returns up to 100 results and a <code>nextToken</code> value if applicable.
    String meshOwner = "meshOwner_example"; // String | The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href=\"https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\">Working with shared meshes</a>.
    String nextToken = "nextToken_example"; // String | The <code>nextToken</code> value returned from a previous paginated <code>ListVirtualGateways</code> request where <code>limit</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value.
    try {
      ListVirtualGatewaysOutput result = apiInstance.listVirtualGateways(meshName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, limit, meshOwner, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listVirtualGateways");
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
| **meshName** | **String**| The name of the service mesh to list virtual gateways in. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **limit** | **Integer**| The maximum number of results returned by &lt;code&gt;ListVirtualGateways&lt;/code&gt; in paginated output. When you use this parameter, &lt;code&gt;ListVirtualGateways&lt;/code&gt; returns only &lt;code&gt;limit&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response element. You can see the remaining results of the initial request by sending another &lt;code&gt;ListVirtualGateways&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. This value can be between 1 and 100. If you don&#39;t use this parameter, &lt;code&gt;ListVirtualGateways&lt;/code&gt; returns up to 100 results and a &lt;code&gt;nextToken&lt;/code&gt; value if applicable. | [optional] |
| **meshOwner** | **String**| The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;. | [optional] |
| **nextToken** | **String**| The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated &lt;code&gt;ListVirtualGateways&lt;/code&gt; request where &lt;code&gt;limit&lt;/code&gt; was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value. | [optional] |

### Return type

[**ListVirtualGatewaysOutput**](ListVirtualGatewaysOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | TooManyRequestsException |  -  |
| **483** | ForbiddenException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | InternalServerErrorException |  -  |

<a id="listVirtualNodes"></a>
# **listVirtualNodes**
> ListVirtualNodesOutput listVirtualNodes(meshName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, limit, meshOwner, nextToken)



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
    String meshName = "meshName_example"; // String | The name of the service mesh to list virtual nodes in.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Integer limit = 56; // Integer | The maximum number of results returned by <code>ListVirtualNodes</code> in paginated output. When you use this parameter, <code>ListVirtualNodes</code> returns only <code>limit</code> results in a single page along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another <code>ListVirtualNodes</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, <code>ListVirtualNodes</code> returns up to 100 results and a <code>nextToken</code> value if applicable.
    String meshOwner = "meshOwner_example"; // String | The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href=\"https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\">Working with shared meshes</a>.
    String nextToken = "nextToken_example"; // String | The <code>nextToken</code> value returned from a previous paginated <code>ListVirtualNodes</code> request where <code>limit</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value.
    try {
      ListVirtualNodesOutput result = apiInstance.listVirtualNodes(meshName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, limit, meshOwner, nextToken);
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
| **meshName** | **String**| The name of the service mesh to list virtual nodes in. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **limit** | **Integer**| The maximum number of results returned by &lt;code&gt;ListVirtualNodes&lt;/code&gt; in paginated output. When you use this parameter, &lt;code&gt;ListVirtualNodes&lt;/code&gt; returns only &lt;code&gt;limit&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response element. You can see the remaining results of the initial request by sending another &lt;code&gt;ListVirtualNodes&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. This value can be between 1 and 100. If you don&#39;t use this parameter, &lt;code&gt;ListVirtualNodes&lt;/code&gt; returns up to 100 results and a &lt;code&gt;nextToken&lt;/code&gt; value if applicable. | [optional] |
| **meshOwner** | **String**| The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;. | [optional] |
| **nextToken** | **String**| The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated &lt;code&gt;ListVirtualNodes&lt;/code&gt; request where &lt;code&gt;limit&lt;/code&gt; was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value. | [optional] |

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
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | TooManyRequestsException |  -  |
| **483** | ForbiddenException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | InternalServerErrorException |  -  |

<a id="listVirtualRouters"></a>
# **listVirtualRouters**
> ListVirtualRoutersOutput listVirtualRouters(meshName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, limit, meshOwner, nextToken)



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
    String meshName = "meshName_example"; // String | The name of the service mesh to list virtual routers in.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Integer limit = 56; // Integer | The maximum number of results returned by <code>ListVirtualRouters</code> in paginated output. When you use this parameter, <code>ListVirtualRouters</code> returns only <code>limit</code> results in a single page along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another <code>ListVirtualRouters</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, <code>ListVirtualRouters</code> returns up to 100 results and a <code>nextToken</code> value if applicable.
    String meshOwner = "meshOwner_example"; // String | The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href=\"https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\">Working with shared meshes</a>.
    String nextToken = "nextToken_example"; // String | The <code>nextToken</code> value returned from a previous paginated <code>ListVirtualRouters</code> request where <code>limit</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value.
    try {
      ListVirtualRoutersOutput result = apiInstance.listVirtualRouters(meshName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, limit, meshOwner, nextToken);
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
| **meshName** | **String**| The name of the service mesh to list virtual routers in. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **limit** | **Integer**| The maximum number of results returned by &lt;code&gt;ListVirtualRouters&lt;/code&gt; in paginated output. When you use this parameter, &lt;code&gt;ListVirtualRouters&lt;/code&gt; returns only &lt;code&gt;limit&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response element. You can see the remaining results of the initial request by sending another &lt;code&gt;ListVirtualRouters&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. This value can be between 1 and 100. If you don&#39;t use this parameter, &lt;code&gt;ListVirtualRouters&lt;/code&gt; returns up to 100 results and a &lt;code&gt;nextToken&lt;/code&gt; value if applicable. | [optional] |
| **meshOwner** | **String**| The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;. | [optional] |
| **nextToken** | **String**| The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated &lt;code&gt;ListVirtualRouters&lt;/code&gt; request where &lt;code&gt;limit&lt;/code&gt; was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value. | [optional] |

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
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | TooManyRequestsException |  -  |
| **483** | ForbiddenException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | InternalServerErrorException |  -  |

<a id="listVirtualServices"></a>
# **listVirtualServices**
> ListVirtualServicesOutput listVirtualServices(meshName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, limit, meshOwner, nextToken)



Returns a list of existing virtual services in a service mesh.

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
    String meshName = "meshName_example"; // String | The name of the service mesh to list virtual services in.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Integer limit = 56; // Integer | The maximum number of results returned by <code>ListVirtualServices</code> in paginated output. When you use this parameter, <code>ListVirtualServices</code> returns only <code>limit</code> results in a single page along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another <code>ListVirtualServices</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, <code>ListVirtualServices</code> returns up to 100 results and a <code>nextToken</code> value if applicable.
    String meshOwner = "meshOwner_example"; // String | The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href=\"https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\">Working with shared meshes</a>.
    String nextToken = "nextToken_example"; // String | The <code>nextToken</code> value returned from a previous paginated <code>ListVirtualServices</code> request where <code>limit</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value.
    try {
      ListVirtualServicesOutput result = apiInstance.listVirtualServices(meshName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, limit, meshOwner, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listVirtualServices");
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
| **meshName** | **String**| The name of the service mesh to list virtual services in. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **limit** | **Integer**| The maximum number of results returned by &lt;code&gt;ListVirtualServices&lt;/code&gt; in paginated output. When you use this parameter, &lt;code&gt;ListVirtualServices&lt;/code&gt; returns only &lt;code&gt;limit&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response element. You can see the remaining results of the initial request by sending another &lt;code&gt;ListVirtualServices&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. This value can be between 1 and 100. If you don&#39;t use this parameter, &lt;code&gt;ListVirtualServices&lt;/code&gt; returns up to 100 results and a &lt;code&gt;nextToken&lt;/code&gt; value if applicable. | [optional] |
| **meshOwner** | **String**| The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;. | [optional] |
| **nextToken** | **String**| The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated &lt;code&gt;ListVirtualServices&lt;/code&gt; request where &lt;code&gt;limit&lt;/code&gt; was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value. | [optional] |

### Return type

[**ListVirtualServicesOutput**](ListVirtualServicesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | TooManyRequestsException |  -  |
| **483** | ForbiddenException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | InternalServerErrorException |  -  |

<a id="tagResource"></a>
# **tagResource**
> Object tagResource(resourceArn, tagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Associates the specified tags to a resource with the specified &lt;code&gt;resourceArn&lt;/code&gt;. If existing tags on a resource aren&#39;t specified in the request parameters, they aren&#39;t changed. When a resource is deleted, the tags associated with that resource are also deleted.

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
    String resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the resource to add tags to.
    TagResourceRequest tagResourceRequest = new TagResourceRequest(); // TagResourceRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.tagResource(resourceArn, tagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tagResource");
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
| **resourceArn** | **String**| The Amazon Resource Name (ARN) of the resource to add tags to. | |
| **tagResourceRequest** | [**TagResourceRequest**](TagResourceRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | TooManyTagsException |  -  |
| **483** | TooManyRequestsException |  -  |
| **484** | ForbiddenException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | InternalServerErrorException |  -  |

<a id="untagResource"></a>
# **untagResource**
> Object untagResource(resourceArn, untagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Deletes specified tags from a resource.

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
    String resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the resource to delete tags from.
    UntagResourceRequest untagResourceRequest = new UntagResourceRequest(); // UntagResourceRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.untagResource(resourceArn, untagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#untagResource");
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
| **resourceArn** | **String**| The Amazon Resource Name (ARN) of the resource to delete tags from. | |
| **untagResourceRequest** | [**UntagResourceRequest**](UntagResourceRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | TooManyRequestsException |  -  |
| **483** | ForbiddenException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | InternalServerErrorException |  -  |

<a id="updateGatewayRoute"></a>
# **updateGatewayRoute**
> UpdateGatewayRouteOutput updateGatewayRoute(gatewayRouteName, meshName, virtualGatewayName, updateGatewayRouteRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner)



Updates an existing gateway route that is associated to a specified virtual gateway in a service mesh.

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
    String gatewayRouteName = "gatewayRouteName_example"; // String | The name of the gateway route to update.
    String meshName = "meshName_example"; // String | The name of the service mesh that the gateway route resides in.
    String virtualGatewayName = "virtualGatewayName_example"; // String | The name of the virtual gateway that the gateway route is associated with.
    UpdateGatewayRouteRequest updateGatewayRouteRequest = new UpdateGatewayRouteRequest(); // UpdateGatewayRouteRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String meshOwner = "meshOwner_example"; // String | The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href=\"https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\">Working with shared meshes</a>.
    try {
      UpdateGatewayRouteOutput result = apiInstance.updateGatewayRoute(gatewayRouteName, meshName, virtualGatewayName, updateGatewayRouteRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateGatewayRoute");
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
| **gatewayRouteName** | **String**| The name of the gateway route to update. | |
| **meshName** | **String**| The name of the service mesh that the gateway route resides in. | |
| **virtualGatewayName** | **String**| The name of the virtual gateway that the gateway route is associated with. | |
| **updateGatewayRouteRequest** | [**UpdateGatewayRouteRequest**](UpdateGatewayRouteRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **meshOwner** | **String**| The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;. | [optional] |

### Return type

[**UpdateGatewayRouteOutput**](UpdateGatewayRouteOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | ConflictException |  -  |
| **483** | TooManyRequestsException |  -  |
| **484** | ForbiddenException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | InternalServerErrorException |  -  |
| **487** | LimitExceededException |  -  |

<a id="updateMesh"></a>
# **updateMesh**
> UpdateMeshOutput updateMesh(meshName, updateMeshRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Updates an existing service mesh.

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
    String meshName = "meshName_example"; // String | The name of the service mesh to update.
    UpdateMeshRequest updateMeshRequest = new UpdateMeshRequest(); // UpdateMeshRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateMeshOutput result = apiInstance.updateMesh(meshName, updateMeshRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateMesh");
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
| **meshName** | **String**| The name of the service mesh to update. | |
| **updateMeshRequest** | [**UpdateMeshRequest**](UpdateMeshRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateMeshOutput**](UpdateMeshOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | ConflictException |  -  |
| **483** | TooManyRequestsException |  -  |
| **484** | ForbiddenException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | InternalServerErrorException |  -  |

<a id="updateRoute"></a>
# **updateRoute**
> UpdateRouteOutput updateRoute(meshName, routeName, virtualRouterName, updateRouteRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner)



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
    String meshName = "meshName_example"; // String | The name of the service mesh that the route resides in.
    String routeName = "routeName_example"; // String | The name of the route to update.
    String virtualRouterName = "virtualRouterName_example"; // String | The name of the virtual router that the route is associated with.
    UpdateRouteRequest updateRouteRequest = new UpdateRouteRequest(); // UpdateRouteRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String meshOwner = "meshOwner_example"; // String | The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href=\"https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\">Working with shared meshes</a>.
    try {
      UpdateRouteOutput result = apiInstance.updateRoute(meshName, routeName, virtualRouterName, updateRouteRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner);
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
| **meshName** | **String**| The name of the service mesh that the route resides in. | |
| **routeName** | **String**| The name of the route to update. | |
| **virtualRouterName** | **String**| The name of the virtual router that the route is associated with. | |
| **updateRouteRequest** | [**UpdateRouteRequest**](UpdateRouteRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **meshOwner** | **String**| The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;. | [optional] |

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
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | ConflictException |  -  |
| **483** | TooManyRequestsException |  -  |
| **484** | ForbiddenException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | InternalServerErrorException |  -  |
| **487** | LimitExceededException |  -  |

<a id="updateVirtualGateway"></a>
# **updateVirtualGateway**
> UpdateVirtualGatewayOutput updateVirtualGateway(meshName, virtualGatewayName, updateVirtualGatewayRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner)



Updates an existing virtual gateway in a specified service mesh.

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
    String meshName = "meshName_example"; // String | The name of the service mesh that the virtual gateway resides in.
    String virtualGatewayName = "virtualGatewayName_example"; // String | The name of the virtual gateway to update.
    UpdateVirtualGatewayRequest updateVirtualGatewayRequest = new UpdateVirtualGatewayRequest(); // UpdateVirtualGatewayRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String meshOwner = "meshOwner_example"; // String | The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href=\"https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\">Working with shared meshes</a>.
    try {
      UpdateVirtualGatewayOutput result = apiInstance.updateVirtualGateway(meshName, virtualGatewayName, updateVirtualGatewayRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateVirtualGateway");
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
| **meshName** | **String**| The name of the service mesh that the virtual gateway resides in. | |
| **virtualGatewayName** | **String**| The name of the virtual gateway to update. | |
| **updateVirtualGatewayRequest** | [**UpdateVirtualGatewayRequest**](UpdateVirtualGatewayRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **meshOwner** | **String**| The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;. | [optional] |

### Return type

[**UpdateVirtualGatewayOutput**](UpdateVirtualGatewayOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | ConflictException |  -  |
| **483** | TooManyRequestsException |  -  |
| **484** | ForbiddenException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | InternalServerErrorException |  -  |
| **487** | LimitExceededException |  -  |

<a id="updateVirtualNode"></a>
# **updateVirtualNode**
> UpdateVirtualNodeOutput updateVirtualNode(meshName, virtualNodeName, updateVirtualNodeRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner)



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
    String meshName = "meshName_example"; // String | The name of the service mesh that the virtual node resides in.
    String virtualNodeName = "virtualNodeName_example"; // String | The name of the virtual node to update.
    UpdateVirtualNodeRequest updateVirtualNodeRequest = new UpdateVirtualNodeRequest(); // UpdateVirtualNodeRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String meshOwner = "meshOwner_example"; // String | The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href=\"https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\">Working with shared meshes</a>.
    try {
      UpdateVirtualNodeOutput result = apiInstance.updateVirtualNode(meshName, virtualNodeName, updateVirtualNodeRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner);
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
| **meshName** | **String**| The name of the service mesh that the virtual node resides in. | |
| **virtualNodeName** | **String**| The name of the virtual node to update. | |
| **updateVirtualNodeRequest** | [**UpdateVirtualNodeRequest**](UpdateVirtualNodeRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **meshOwner** | **String**| The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;. | [optional] |

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
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | ConflictException |  -  |
| **483** | TooManyRequestsException |  -  |
| **484** | ForbiddenException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | InternalServerErrorException |  -  |
| **487** | LimitExceededException |  -  |

<a id="updateVirtualRouter"></a>
# **updateVirtualRouter**
> UpdateVirtualRouterOutput updateVirtualRouter(meshName, virtualRouterName, updateVirtualRouterRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner)



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
    String meshName = "meshName_example"; // String | The name of the service mesh that the virtual router resides in.
    String virtualRouterName = "virtualRouterName_example"; // String | The name of the virtual router to update.
    UpdateVirtualRouterRequest updateVirtualRouterRequest = new UpdateVirtualRouterRequest(); // UpdateVirtualRouterRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String meshOwner = "meshOwner_example"; // String | The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href=\"https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\">Working with shared meshes</a>.
    try {
      UpdateVirtualRouterOutput result = apiInstance.updateVirtualRouter(meshName, virtualRouterName, updateVirtualRouterRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner);
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
| **meshName** | **String**| The name of the service mesh that the virtual router resides in. | |
| **virtualRouterName** | **String**| The name of the virtual router to update. | |
| **updateVirtualRouterRequest** | [**UpdateVirtualRouterRequest**](UpdateVirtualRouterRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **meshOwner** | **String**| The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;. | [optional] |

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
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | ConflictException |  -  |
| **483** | TooManyRequestsException |  -  |
| **484** | ForbiddenException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | InternalServerErrorException |  -  |
| **487** | LimitExceededException |  -  |

<a id="updateVirtualService"></a>
# **updateVirtualService**
> UpdateVirtualServiceOutput updateVirtualService(meshName, virtualServiceName, updateVirtualServiceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner)



Updates an existing virtual service in a specified service mesh.

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
    String meshName = "meshName_example"; // String | The name of the service mesh that the virtual service resides in.
    String virtualServiceName = "virtualServiceName_example"; // String | The name of the virtual service to update.
    UpdateVirtualServiceRequest updateVirtualServiceRequest = new UpdateVirtualServiceRequest(); // UpdateVirtualServiceRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String meshOwner = "meshOwner_example"; // String | The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href=\"https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\">Working with shared meshes</a>.
    try {
      UpdateVirtualServiceOutput result = apiInstance.updateVirtualService(meshName, virtualServiceName, updateVirtualServiceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, meshOwner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateVirtualService");
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
| **meshName** | **String**| The name of the service mesh that the virtual service resides in. | |
| **virtualServiceName** | **String**| The name of the virtual service to update. | |
| **updateVirtualServiceRequest** | [**UpdateVirtualServiceRequest**](UpdateVirtualServiceRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **meshOwner** | **String**| The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it&#39;s the ID of the account that shared the mesh with your account. For more information about mesh sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\&quot;&gt;Working with shared meshes&lt;/a&gt;. | [optional] |

### Return type

[**UpdateVirtualServiceOutput**](UpdateVirtualServiceOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | ConflictException |  -  |
| **483** | TooManyRequestsException |  -  |
| **484** | ForbiddenException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | InternalServerErrorException |  -  |
| **487** | LimitExceededException |  -  |

