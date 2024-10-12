# NodeBalancersApi

All URIs are relative to *https://api.linode.com/v4*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNodeBalancer**](NodeBalancersApi.md#createNodeBalancer) | **POST** /nodebalancers | NodeBalancer Create |
| [**createNodeBalancerConfig**](NodeBalancersApi.md#createNodeBalancerConfig) | **POST** /nodebalancers/{nodeBalancerId}/configs | Config Create |
| [**createNodeBalancerNode**](NodeBalancersApi.md#createNodeBalancerNode) | **POST** /nodebalancers/{nodeBalancerId}/configs/{configId}/nodes | Node Create |
| [**deleteNodeBalancer**](NodeBalancersApi.md#deleteNodeBalancer) | **DELETE** /nodebalancers/{nodeBalancerId} | NodeBalancer Delete |
| [**deleteNodeBalancerConfig**](NodeBalancersApi.md#deleteNodeBalancerConfig) | **DELETE** /nodebalancers/{nodeBalancerId}/configs/{configId} | Config Delete |
| [**deleteNodeBalancerConfigNode**](NodeBalancersApi.md#deleteNodeBalancerConfigNode) | **DELETE** /nodebalancers/{nodeBalancerId}/configs/{configId}/nodes/{nodeId} | Node Delete |
| [**getNodeBalancer**](NodeBalancersApi.md#getNodeBalancer) | **GET** /nodebalancers/{nodeBalancerId} | NodeBalancer View |
| [**getNodeBalancerConfig**](NodeBalancersApi.md#getNodeBalancerConfig) | **GET** /nodebalancers/{nodeBalancerId}/configs/{configId} | Config View |
| [**getNodeBalancerConfigNodes**](NodeBalancersApi.md#getNodeBalancerConfigNodes) | **GET** /nodebalancers/{nodeBalancerId}/configs/{configId}/nodes | Nodes List |
| [**getNodeBalancerConfigs**](NodeBalancersApi.md#getNodeBalancerConfigs) | **GET** /nodebalancers/{nodeBalancerId}/configs | Configs List |
| [**getNodeBalancerNode**](NodeBalancersApi.md#getNodeBalancerNode) | **GET** /nodebalancers/{nodeBalancerId}/configs/{configId}/nodes/{nodeId} | Node View |
| [**getNodeBalancers**](NodeBalancersApi.md#getNodeBalancers) | **GET** /nodebalancers | NodeBalancers List |
| [**nodebalancersNodeBalancerIdStatsGet**](NodeBalancersApi.md#nodebalancersNodeBalancerIdStatsGet) | **GET** /nodebalancers/{nodeBalancerId}/stats | NodeBalancer Statistics View |
| [**rebuildNodeBalancerConfig**](NodeBalancersApi.md#rebuildNodeBalancerConfig) | **POST** /nodebalancers/{nodeBalancerId}/configs/{configId}/rebuild | Config Rebuild |
| [**updateNodeBalancer**](NodeBalancersApi.md#updateNodeBalancer) | **PUT** /nodebalancers/{nodeBalancerId} | NodeBalancer Update |
| [**updateNodeBalancerConfig**](NodeBalancersApi.md#updateNodeBalancerConfig) | **PUT** /nodebalancers/{nodeBalancerId}/configs/{configId} | Config Update |
| [**updateNodeBalancerNode**](NodeBalancersApi.md#updateNodeBalancerNode) | **PUT** /nodebalancers/{nodeBalancerId}/configs/{configId}/nodes/{nodeId} | Node Update |


<a id="createNodeBalancer"></a>
# **createNodeBalancer**
> NodeBalancer createNodeBalancer(createNodeBalancerRequest)

NodeBalancer Create

Creates a NodeBalancer in the requested Region.  NodeBalancers require a port Config with at least one backend Node to start serving requests.  When using the Linode CLI to create a NodeBalancer, first create a NodeBalancer without any Configs. Then, create Configs and Nodes for that NodeBalancer with the respective [Config Create](/docs/api/nodebalancers/#config-create) and [Node Create](/docs/api/nodebalancers/#node-create) commands. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NodeBalancersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    NodeBalancersApi apiInstance = new NodeBalancersApi(defaultClient);
    CreateNodeBalancerRequest createNodeBalancerRequest = new CreateNodeBalancerRequest(); // CreateNodeBalancerRequest | Information about the NodeBalancer to create.
    try {
      NodeBalancer result = apiInstance.createNodeBalancer(createNodeBalancerRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NodeBalancersApi#createNodeBalancer");
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
| **createNodeBalancerRequest** | [**CreateNodeBalancerRequest**](CreateNodeBalancerRequest.md)| Information about the NodeBalancer to create. | |

### Return type

[**NodeBalancer**](NodeBalancer.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | NodeBalancer created successfully. |  -  |
| **0** | Error |  -  |

<a id="createNodeBalancerConfig"></a>
# **createNodeBalancerConfig**
> NodeBalancerConfig createNodeBalancerConfig(nodeBalancerId, nodeBalancerConfig)

Config Create

Creates a NodeBalancer Config, which allows the NodeBalancer to accept traffic on a new port. You will need to add NodeBalancer Nodes to the new Config before it can actually serve requests. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NodeBalancersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    NodeBalancersApi apiInstance = new NodeBalancersApi(defaultClient);
    Integer nodeBalancerId = 56; // Integer | The ID of the NodeBalancer to access.
    NodeBalancerConfig nodeBalancerConfig = new NodeBalancerConfig(); // NodeBalancerConfig | Information about the port to configure.
    try {
      NodeBalancerConfig result = apiInstance.createNodeBalancerConfig(nodeBalancerId, nodeBalancerConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NodeBalancersApi#createNodeBalancerConfig");
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
| **nodeBalancerId** | **Integer**| The ID of the NodeBalancer to access. | |
| **nodeBalancerConfig** | [**NodeBalancerConfig**](NodeBalancerConfig.md)| Information about the port to configure. | [optional] |

### Return type

[**NodeBalancerConfig**](NodeBalancerConfig.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Config created successfully. |  -  |
| **0** | Error |  -  |

<a id="createNodeBalancerNode"></a>
# **createNodeBalancerNode**
> NodeBalancerNode createNodeBalancerNode(nodeBalancerId, configId, nodeBalancerNode)

Node Create

Creates a NodeBalancer Node, a backend that can accept traffic for this NodeBalancer Config. Nodes are routed requests on the configured port based on their status. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NodeBalancersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    NodeBalancersApi apiInstance = new NodeBalancersApi(defaultClient);
    Integer nodeBalancerId = 56; // Integer | The ID of the NodeBalancer to access.
    Integer configId = 56; // Integer | The ID of the NodeBalancer config to access.
    NodeBalancerNode nodeBalancerNode = new NodeBalancerNode(); // NodeBalancerNode | Information about the Node to create.
    try {
      NodeBalancerNode result = apiInstance.createNodeBalancerNode(nodeBalancerId, configId, nodeBalancerNode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NodeBalancersApi#createNodeBalancerNode");
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
| **nodeBalancerId** | **Integer**| The ID of the NodeBalancer to access. | |
| **configId** | **Integer**| The ID of the NodeBalancer config to access. | |
| **nodeBalancerNode** | [**NodeBalancerNode**](NodeBalancerNode.md)| Information about the Node to create. | |

### Return type

[**NodeBalancerNode**](NodeBalancerNode.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Node created successfully. |  -  |
| **0** | Error |  -  |

<a id="deleteNodeBalancer"></a>
# **deleteNodeBalancer**
> Object deleteNodeBalancer(nodeBalancerId)

NodeBalancer Delete

Deletes a NodeBalancer.  **This is a destructive action and cannot be undone.**  Deleting a NodeBalancer will also delete all associated Configs and Nodes, although the backend servers represented by the Nodes will not be changed or removed. Deleting a NodeBalancer will cause you to lose access to the IP Addresses assigned to this NodeBalancer. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NodeBalancersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    NodeBalancersApi apiInstance = new NodeBalancersApi(defaultClient);
    Integer nodeBalancerId = 56; // Integer | The ID of the NodeBalancer to access.
    try {
      Object result = apiInstance.deleteNodeBalancer(nodeBalancerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NodeBalancersApi#deleteNodeBalancer");
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
| **nodeBalancerId** | **Integer**| The ID of the NodeBalancer to access. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | NodeBalancer deleted successfully. |  -  |
| **0** | Error |  -  |

<a id="deleteNodeBalancerConfig"></a>
# **deleteNodeBalancerConfig**
> Object deleteNodeBalancerConfig(nodeBalancerId, configId)

Config Delete

Deletes the Config for a port of this NodeBalancer.  **This cannot be undone.**  Once completed, this NodeBalancer will no longer respond to requests on the given port. This also deletes all associated NodeBalancerNodes, but the Linodes they were routing traffic to will be unchanged and will not be removed. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NodeBalancersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    NodeBalancersApi apiInstance = new NodeBalancersApi(defaultClient);
    Integer nodeBalancerId = 56; // Integer | The ID of the NodeBalancer to access.
    Integer configId = 56; // Integer | The ID of the config to access.
    try {
      Object result = apiInstance.deleteNodeBalancerConfig(nodeBalancerId, configId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NodeBalancersApi#deleteNodeBalancerConfig");
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
| **nodeBalancerId** | **Integer**| The ID of the NodeBalancer to access. | |
| **configId** | **Integer**| The ID of the config to access. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | NodeBalancer Config deleted successfully. |  -  |
| **0** | Error |  -  |

<a id="deleteNodeBalancerConfigNode"></a>
# **deleteNodeBalancerConfigNode**
> Object deleteNodeBalancerConfigNode(nodeBalancerId, configId, nodeId)

Node Delete

Deletes a Node from this Config. This backend will no longer receive traffic for the configured port of this NodeBalancer.  This does not change or remove the Linode whose address was used in the creation of this Node. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NodeBalancersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    NodeBalancersApi apiInstance = new NodeBalancersApi(defaultClient);
    Integer nodeBalancerId = 56; // Integer | The ID of the NodeBalancer to access.
    Integer configId = 56; // Integer | The ID of the Config to access
    Integer nodeId = 56; // Integer | The ID of the Node to access
    try {
      Object result = apiInstance.deleteNodeBalancerConfigNode(nodeBalancerId, configId, nodeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NodeBalancersApi#deleteNodeBalancerConfigNode");
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
| **nodeBalancerId** | **Integer**| The ID of the NodeBalancer to access. | |
| **configId** | **Integer**| The ID of the Config to access | |
| **nodeId** | **Integer**| The ID of the Node to access | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Node deleted successfully. |  -  |
| **0** | Error |  -  |

<a id="getNodeBalancer"></a>
# **getNodeBalancer**
> NodeBalancer getNodeBalancer(nodeBalancerId)

NodeBalancer View

Returns a single NodeBalancer you can access. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NodeBalancersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    NodeBalancersApi apiInstance = new NodeBalancersApi(defaultClient);
    Integer nodeBalancerId = 56; // Integer | The ID of the NodeBalancer to access.
    try {
      NodeBalancer result = apiInstance.getNodeBalancer(nodeBalancerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NodeBalancersApi#getNodeBalancer");
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
| **nodeBalancerId** | **Integer**| The ID of the NodeBalancer to access. | |

### Return type

[**NodeBalancer**](NodeBalancer.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested NodeBalancer object. |  -  |
| **0** | Error |  -  |

<a id="getNodeBalancerConfig"></a>
# **getNodeBalancerConfig**
> NodeBalancerConfig getNodeBalancerConfig(nodeBalancerId, configId)

Config View

Returns configuration information for a single port of this NodeBalancer. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NodeBalancersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    NodeBalancersApi apiInstance = new NodeBalancersApi(defaultClient);
    Integer nodeBalancerId = 56; // Integer | The ID of the NodeBalancer to access.
    Integer configId = 56; // Integer | The ID of the config to access.
    try {
      NodeBalancerConfig result = apiInstance.getNodeBalancerConfig(nodeBalancerId, configId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NodeBalancersApi#getNodeBalancerConfig");
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
| **nodeBalancerId** | **Integer**| The ID of the NodeBalancer to access. | |
| **configId** | **Integer**| The ID of the config to access. | |

### Return type

[**NodeBalancerConfig**](NodeBalancerConfig.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested NodeBalancer config. |  -  |
| **0** | Error |  -  |

<a id="getNodeBalancerConfigNodes"></a>
# **getNodeBalancerConfigNodes**
> GetNodeBalancerConfigNodes200Response getNodeBalancerConfigNodes(nodeBalancerId, configId, page, pageSize)

Nodes List

Returns a paginated list of NodeBalancer nodes associated with this Config. These are the backends that will be sent traffic for this port. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NodeBalancersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    NodeBalancersApi apiInstance = new NodeBalancersApi(defaultClient);
    Integer nodeBalancerId = 56; // Integer | The ID of the NodeBalancer to access.
    Integer configId = 56; // Integer | The ID of the NodeBalancer config to access.
    Integer page = 1; // Integer | The page of a collection to return.
    Integer pageSize = 100; // Integer | The number of items to return per page.
    try {
      GetNodeBalancerConfigNodes200Response result = apiInstance.getNodeBalancerConfigNodes(nodeBalancerId, configId, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NodeBalancersApi#getNodeBalancerConfigNodes");
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
| **nodeBalancerId** | **Integer**| The ID of the NodeBalancer to access. | |
| **configId** | **Integer**| The ID of the NodeBalancer config to access. | |
| **page** | **Integer**| The page of a collection to return. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return per page. | [optional] [default to 100] |

### Return type

[**GetNodeBalancerConfigNodes200Response**](GetNodeBalancerConfigNodes200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A paginated list of NodeBalancer nodes. |  -  |
| **0** | Error |  -  |

<a id="getNodeBalancerConfigs"></a>
# **getNodeBalancerConfigs**
> GetNodeBalancerConfigs200Response getNodeBalancerConfigs(nodeBalancerId, page, pageSize)

Configs List

Returns a paginated list of NodeBalancer Configs associated with this NodeBalancer. NodeBalancer Configs represent individual ports that this NodeBalancer will accept traffic on, one Config per port.  For example, if you wanted to accept standard HTTP traffic, you would need a Config listening on port 80. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NodeBalancersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    NodeBalancersApi apiInstance = new NodeBalancersApi(defaultClient);
    Integer nodeBalancerId = 56; // Integer | The ID of the NodeBalancer to access.
    Integer page = 1; // Integer | The page of a collection to return.
    Integer pageSize = 100; // Integer | The number of items to return per page.
    try {
      GetNodeBalancerConfigs200Response result = apiInstance.getNodeBalancerConfigs(nodeBalancerId, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NodeBalancersApi#getNodeBalancerConfigs");
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
| **nodeBalancerId** | **Integer**| The ID of the NodeBalancer to access. | |
| **page** | **Integer**| The page of a collection to return. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return per page. | [optional] [default to 100] |

### Return type

[**GetNodeBalancerConfigs200Response**](GetNodeBalancerConfigs200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A paginted list of NodeBalancer Configs |  -  |
| **0** | Error |  -  |

<a id="getNodeBalancerNode"></a>
# **getNodeBalancerNode**
> NodeBalancerNode getNodeBalancerNode(nodeBalancerId, configId, nodeId)

Node View

Returns information about a single Node, a backend for this NodeBalancer&#39;s configured port. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NodeBalancersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    NodeBalancersApi apiInstance = new NodeBalancersApi(defaultClient);
    Integer nodeBalancerId = 56; // Integer | The ID of the NodeBalancer to access.
    Integer configId = 56; // Integer | The ID of the Config to access
    Integer nodeId = 56; // Integer | The ID of the Node to access
    try {
      NodeBalancerNode result = apiInstance.getNodeBalancerNode(nodeBalancerId, configId, nodeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NodeBalancersApi#getNodeBalancerNode");
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
| **nodeBalancerId** | **Integer**| The ID of the NodeBalancer to access. | |
| **configId** | **Integer**| The ID of the Config to access | |
| **nodeId** | **Integer**| The ID of the Node to access | |

### Return type

[**NodeBalancerNode**](NodeBalancerNode.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A paginated list of NodeBalancer nodes. |  -  |
| **0** | Error |  -  |

<a id="getNodeBalancers"></a>
# **getNodeBalancers**
> GetLinodeNodeBalancers200Response getNodeBalancers(page, pageSize)

NodeBalancers List

Returns a paginated list of NodeBalancers you have access to. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NodeBalancersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    NodeBalancersApi apiInstance = new NodeBalancersApi(defaultClient);
    Integer page = 1; // Integer | The page of a collection to return.
    Integer pageSize = 100; // Integer | The number of items to return per page.
    try {
      GetLinodeNodeBalancers200Response result = apiInstance.getNodeBalancers(page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NodeBalancersApi#getNodeBalancers");
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
| **page** | **Integer**| The page of a collection to return. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return per page. | [optional] [default to 100] |

### Return type

[**GetLinodeNodeBalancers200Response**](GetLinodeNodeBalancers200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A paginated list of NodeBalancers. |  -  |
| **0** | Error |  -  |

<a id="nodebalancersNodeBalancerIdStatsGet"></a>
# **nodebalancersNodeBalancerIdStatsGet**
> NodeBalancerStats nodebalancersNodeBalancerIdStatsGet(nodeBalancerId)

NodeBalancer Statistics View

Returns detailed statistics about the requested NodeBalancer. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NodeBalancersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    NodeBalancersApi apiInstance = new NodeBalancersApi(defaultClient);
    Integer nodeBalancerId = 56; // Integer | The ID of the NodeBalancer to access.
    try {
      NodeBalancerStats result = apiInstance.nodebalancersNodeBalancerIdStatsGet(nodeBalancerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NodeBalancersApi#nodebalancersNodeBalancerIdStatsGet");
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
| **nodeBalancerId** | **Integer**| The ID of the NodeBalancer to access. | |

### Return type

[**NodeBalancerStats**](NodeBalancerStats.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested stats. |  -  |
| **0** | Error |  -  |

<a id="rebuildNodeBalancerConfig"></a>
# **rebuildNodeBalancerConfig**
> NodeBalancerConfig rebuildNodeBalancerConfig(nodeBalancerId, configId, rebuildNodeBalancerConfigRequest)

Config Rebuild

Rebuilds a NodeBalancer Config and its Nodes that you have permission to modify.  Use this command to update a NodeBalancer&#39;s Config and Nodes with a single request. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NodeBalancersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    NodeBalancersApi apiInstance = new NodeBalancersApi(defaultClient);
    Integer nodeBalancerId = 56; // Integer | The ID of the NodeBalancer to access.
    Integer configId = 56; // Integer | The ID of the Config to access.
    RebuildNodeBalancerConfigRequest rebuildNodeBalancerConfigRequest = new RebuildNodeBalancerConfigRequest(); // RebuildNodeBalancerConfigRequest | Information about the NodeBalancer Config to rebuild. 
    try {
      NodeBalancerConfig result = apiInstance.rebuildNodeBalancerConfig(nodeBalancerId, configId, rebuildNodeBalancerConfigRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NodeBalancersApi#rebuildNodeBalancerConfig");
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
| **nodeBalancerId** | **Integer**| The ID of the NodeBalancer to access. | |
| **configId** | **Integer**| The ID of the Config to access. | |
| **rebuildNodeBalancerConfigRequest** | [**RebuildNodeBalancerConfigRequest**](RebuildNodeBalancerConfigRequest.md)| Information about the NodeBalancer Config to rebuild.  | |

### Return type

[**NodeBalancerConfig**](NodeBalancerConfig.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | NodeBalancer created successfully. |  -  |
| **0** | Error |  -  |

<a id="updateNodeBalancer"></a>
# **updateNodeBalancer**
> NodeBalancer updateNodeBalancer(nodeBalancerId, nodeBalancer)

NodeBalancer Update

Updates information about a NodeBalancer you can access. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NodeBalancersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    NodeBalancersApi apiInstance = new NodeBalancersApi(defaultClient);
    Integer nodeBalancerId = 56; // Integer | The ID of the NodeBalancer to access.
    NodeBalancer nodeBalancer = new NodeBalancer(); // NodeBalancer | The information to update.
    try {
      NodeBalancer result = apiInstance.updateNodeBalancer(nodeBalancerId, nodeBalancer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NodeBalancersApi#updateNodeBalancer");
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
| **nodeBalancerId** | **Integer**| The ID of the NodeBalancer to access. | |
| **nodeBalancer** | [**NodeBalancer**](NodeBalancer.md)| The information to update. | |

### Return type

[**NodeBalancer**](NodeBalancer.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | NodeBalancer updated successfully. |  -  |
| **0** | Error |  -  |

<a id="updateNodeBalancerConfig"></a>
# **updateNodeBalancerConfig**
> NodeBalancerConfig updateNodeBalancerConfig(nodeBalancerId, configId, nodeBalancerConfig)

Config Update

Updates the configuration for a single port on a NodeBalancer. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NodeBalancersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    NodeBalancersApi apiInstance = new NodeBalancersApi(defaultClient);
    Integer nodeBalancerId = 56; // Integer | The ID of the NodeBalancer to access.
    Integer configId = 56; // Integer | The ID of the config to access.
    NodeBalancerConfig nodeBalancerConfig = new NodeBalancerConfig(); // NodeBalancerConfig | The fields to update.
    try {
      NodeBalancerConfig result = apiInstance.updateNodeBalancerConfig(nodeBalancerId, configId, nodeBalancerConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NodeBalancersApi#updateNodeBalancerConfig");
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
| **nodeBalancerId** | **Integer**| The ID of the NodeBalancer to access. | |
| **configId** | **Integer**| The ID of the config to access. | |
| **nodeBalancerConfig** | [**NodeBalancerConfig**](NodeBalancerConfig.md)| The fields to update. | |

### Return type

[**NodeBalancerConfig**](NodeBalancerConfig.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Config updated successfully. |  -  |
| **0** | Error |  -  |

<a id="updateNodeBalancerNode"></a>
# **updateNodeBalancerNode**
> NodeBalancerNode updateNodeBalancerNode(nodeBalancerId, configId, nodeId, nodeBalancerNode)

Node Update

Updates information about a Node, a backend for this NodeBalancer&#39;s configured port. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NodeBalancersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    NodeBalancersApi apiInstance = new NodeBalancersApi(defaultClient);
    Integer nodeBalancerId = 56; // Integer | The ID of the NodeBalancer to access.
    Integer configId = 56; // Integer | The ID of the Config to access
    Integer nodeId = 56; // Integer | The ID of the Node to access
    NodeBalancerNode nodeBalancerNode = new NodeBalancerNode(); // NodeBalancerNode | The fields to update.
    try {
      NodeBalancerNode result = apiInstance.updateNodeBalancerNode(nodeBalancerId, configId, nodeId, nodeBalancerNode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NodeBalancersApi#updateNodeBalancerNode");
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
| **nodeBalancerId** | **Integer**| The ID of the NodeBalancer to access. | |
| **configId** | **Integer**| The ID of the Config to access | |
| **nodeId** | **Integer**| The ID of the Node to access | |
| **nodeBalancerNode** | [**NodeBalancerNode**](NodeBalancerNode.md)| The fields to update. | |

### Return type

[**NodeBalancerNode**](NodeBalancerNode.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Node updated successfully. |  -  |
| **0** | Error |  -  |

