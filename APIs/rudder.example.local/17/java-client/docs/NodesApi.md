# NodesApi

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**applyPolicy**](NodesApi.md#applyPolicy) | **POST** /nodes/{nodeId}/applyPolicy | Trigger an agent run |
| [**applyPolicyAllNodes**](NodesApi.md#applyPolicyAllNodes) | **POST** /nodes/applyPolicy | Trigger an agent run on all nodes |
| [**changePendingNodeStatus**](NodesApi.md#changePendingNodeStatus) | **POST** /nodes/pending/{nodeId} | Update pending Node status |
| [**createNodes**](NodesApi.md#createNodes) | **PUT** /nodes | Create one or several new nodes |
| [**deleteNode**](NodesApi.md#deleteNode) | **DELETE** /nodes/{nodeId} | Delete a node |
| [**getNodesStatus**](NodesApi.md#getNodesStatus) | **GET** /nodes/status | Get nodes acceptation status |
| [**listAcceptedNodes**](NodesApi.md#listAcceptedNodes) | **GET** /nodes | List managed nodes |
| [**listPendingNodes**](NodesApi.md#listPendingNodes) | **GET** /nodes/pending | List pending nodes |
| [**nodeDetails**](NodesApi.md#nodeDetails) | **GET** /nodes/{nodeId} | Get information about a node |
| [**nodeInheritedProperties**](NodesApi.md#nodeInheritedProperties) | **GET** /nodes/{nodeId}/inheritedProperties | Get inherited node properties for a node |
| [**updateNode**](NodesApi.md#updateNode) | **POST** /nodes/{nodeId} | Update node settings and properties |


<a id="applyPolicy"></a>
# **applyPolicy**
> String applyPolicy(nodeId)

Trigger an agent run

This API allows to trigger an agent run on the target node. Response is a stream of the actual agent run on the node.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    NodesApi apiInstance = new NodesApi(defaultClient);
    String nodeId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Id of the target node
    try {
      String result = apiInstance.applyPolicy(nodeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NodesApi#applyPolicy");
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
| **nodeId** | **String**| Id of the target node | |

### Return type

**String**

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Agent output |  -  |

<a id="applyPolicyAllNodes"></a>
# **applyPolicyAllNodes**
> ApplyPolicyAllNodes200Response applyPolicyAllNodes()

Trigger an agent run on all nodes

This API allows to trigger an agent run on all nodes. Response contains a json stating if agent could be started on each node, but not if the run went fine and do not display any output from it. You can see the result of the run in Rudder web interface or in the each agent logs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    NodesApi apiInstance = new NodesApi(defaultClient);
    try {
      ApplyPolicyAllNodes200Response result = apiInstance.applyPolicyAllNodes();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NodesApi#applyPolicyAllNodes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApplyPolicyAllNodes200Response**](ApplyPolicyAllNodes200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Result |  -  |

<a id="changePendingNodeStatus"></a>
# **changePendingNodeStatus**
> ChangePendingNodeStatus200Response changePendingNodeStatus(nodeId, changePendingNodeStatusRequest)

Update pending Node status

Accept or refuse a pending node

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    NodesApi apiInstance = new NodesApi(defaultClient);
    String nodeId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Id of the target node
    ChangePendingNodeStatusRequest changePendingNodeStatusRequest = new ChangePendingNodeStatusRequest(); // ChangePendingNodeStatusRequest | 
    try {
      ChangePendingNodeStatus200Response result = apiInstance.changePendingNodeStatus(nodeId, changePendingNodeStatusRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NodesApi#changePendingNodeStatus");
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
| **nodeId** | **String**| Id of the target node | |
| **changePendingNodeStatusRequest** | [**ChangePendingNodeStatusRequest**](ChangePendingNodeStatusRequest.md)|  | [optional] |

### Return type

[**ChangePendingNodeStatus200Response**](ChangePendingNodeStatus200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Nodes |  -  |

<a id="createNodes"></a>
# **createNodes**
> CreateNodes200Response createNodes(nodeAddInner)

Create one or several new nodes

Use the provided array of node information to create new nodes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    NodesApi apiInstance = new NodesApi(defaultClient);
    List<NodeAddInner> nodeAddInner = Arrays.asList(); // List<NodeAddInner> | 
    try {
      CreateNodes200Response result = apiInstance.createNodes(nodeAddInner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NodesApi#createNodes");
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
| **nodeAddInner** | [**List&lt;NodeAddInner&gt;**](NodeAddInner.md)|  | |

### Return type

[**CreateNodes200Response**](CreateNodes200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Creation information |  -  |

<a id="deleteNode"></a>
# **deleteNode**
> DeleteNode200Response deleteNode(nodeId, mode)

Delete a node

Remove a node from the Rudder server. It won&#39;t be managed anymore.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    NodesApi apiInstance = new NodesApi(defaultClient);
    String nodeId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Id of the target node
    String mode = "move"; // String | Deletion mode to use, either move to trash ('move', default) or erase ('erase')
    try {
      DeleteNode200Response result = apiInstance.deleteNode(nodeId, mode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NodesApi#deleteNode");
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
| **nodeId** | **String**| Id of the target node | |
| **mode** | **String**| Deletion mode to use, either move to trash (&#39;move&#39;, default) or erase (&#39;erase&#39;) | [optional] [default to move] [enum: move, erase] |

### Return type

[**DeleteNode200Response**](DeleteNode200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Nodes |  -  |

<a id="getNodesStatus"></a>
# **getNodesStatus**
> GetNodesStatus200Response getNodesStatus(ids)

Get nodes acceptation status

Get acceptation status (pending, accepted, deleted, unknown) of a list of nodes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    NodesApi apiInstance = new NodesApi(defaultClient);
    String ids = "default"; // String | Comma separated list of node Ids
    try {
      GetNodesStatus200Response result = apiInstance.getNodesStatus(ids);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NodesApi#getNodesStatus");
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
| **ids** | **String**| Comma separated list of node Ids | [default to default] |

### Return type

[**GetNodesStatus200Response**](GetNodesStatus200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | nodes |  -  |

<a id="listAcceptedNodes"></a>
# **listAcceptedNodes**
> ListAcceptedNodes200Response listAcceptedNodes(include, query, where, composition, select)

List managed nodes

Get information about the nodes managed by the target server

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    NodesApi apiInstance = new NodesApi(defaultClient);
    String include = "default"; // String | Level of information to include from the node inventory. Some base levels are defined (**minimal**, **default**, **full**). You can add fields you want to a base level by adding them to the list, possible values are keys from json answer. If you don't provide a base level, they will be added to `default` level, so if you only want os details, use `minimal,os` as the value for this parameter. * **minimal** includes: `id`, `hostname` and `status` * **default** includes **minimal** plus `architectureDescription`, `description`, `ipAddresses`, `lastRunDate`, `lastInventoryDate`, `machine`, `os`, `managementTechnology`, `policyServerId`, `properties` (be careful! Only node own properties, if you also need inherited properties, look at the dedicated `/nodes/{id}/inheritedProperties` endpoint), `policyMode `, `ram` and `timezone` * **full** includes: **default** plus `accounts`, `bios`, `controllers`, `environmentVariables`, `fileSystems`, `managementTechnologyDetails`, `memories`, `networkInterfaces`, `ports`, `processes`, `processors`, `slots`, `software`, `sound`, `storage`, `videos` and `virtualMachines`
    Object query = null; // Object | The criterion you want to find for your nodes. Replaces the `where`, `composition` and `select` parameters in a single parameter.
    List<Object> where = null; // List<Object> | The criterion you want to find for your nodes
    String composition = "and"; // String | Boolean operator to use between each  `where` criteria.
    String select = "node"; // String | What kind of data we want to include. Here we can get policy servers/relay by setting `nodeAndPolicyServer`. Only used if `where` is defined.
    try {
      ListAcceptedNodes200Response result = apiInstance.listAcceptedNodes(include, query, where, composition, select);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NodesApi#listAcceptedNodes");
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
| **include** | **String**| Level of information to include from the node inventory. Some base levels are defined (**minimal**, **default**, **full**). You can add fields you want to a base level by adding them to the list, possible values are keys from json answer. If you don&#39;t provide a base level, they will be added to &#x60;default&#x60; level, so if you only want os details, use &#x60;minimal,os&#x60; as the value for this parameter. * **minimal** includes: &#x60;id&#x60;, &#x60;hostname&#x60; and &#x60;status&#x60; * **default** includes **minimal** plus &#x60;architectureDescription&#x60;, &#x60;description&#x60;, &#x60;ipAddresses&#x60;, &#x60;lastRunDate&#x60;, &#x60;lastInventoryDate&#x60;, &#x60;machine&#x60;, &#x60;os&#x60;, &#x60;managementTechnology&#x60;, &#x60;policyServerId&#x60;, &#x60;properties&#x60; (be careful! Only node own properties, if you also need inherited properties, look at the dedicated &#x60;/nodes/{id}/inheritedProperties&#x60; endpoint), &#x60;policyMode &#x60;, &#x60;ram&#x60; and &#x60;timezone&#x60; * **full** includes: **default** plus &#x60;accounts&#x60;, &#x60;bios&#x60;, &#x60;controllers&#x60;, &#x60;environmentVariables&#x60;, &#x60;fileSystems&#x60;, &#x60;managementTechnologyDetails&#x60;, &#x60;memories&#x60;, &#x60;networkInterfaces&#x60;, &#x60;ports&#x60;, &#x60;processes&#x60;, &#x60;processors&#x60;, &#x60;slots&#x60;, &#x60;software&#x60;, &#x60;sound&#x60;, &#x60;storage&#x60;, &#x60;videos&#x60; and &#x60;virtualMachines&#x60; | [optional] [default to default] |
| **query** | [**Object**](.md)| The criterion you want to find for your nodes. Replaces the &#x60;where&#x60;, &#x60;composition&#x60; and &#x60;select&#x60; parameters in a single parameter. | [optional] |
| **where** | [**List&lt;Object&gt;**](Object.md)| The criterion you want to find for your nodes | [optional] |
| **composition** | **String**| Boolean operator to use between each  &#x60;where&#x60; criteria. | [optional] [default to and] [enum: and, or] |
| **select** | **String**| What kind of data we want to include. Here we can get policy servers/relay by setting &#x60;nodeAndPolicyServer&#x60;. Only used if &#x60;where&#x60; is defined. | [optional] [default to node] |

### Return type

[**ListAcceptedNodes200Response**](ListAcceptedNodes200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Nodes |  -  |

<a id="listPendingNodes"></a>
# **listPendingNodes**
> ListPendingNodes200Response listPendingNodes(include, query, where, composition, select)

List pending nodes

Get information about the nodes pending acceptation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    NodesApi apiInstance = new NodesApi(defaultClient);
    String include = "default"; // String | Level of information to include from the node inventory. Some base levels are defined (**minimal**, **default**, **full**). You can add fields you want to a base level by adding them to the list, possible values are keys from json answer. If you don't provide a base level, they will be added to `default` level, so if you only want os details, use `minimal,os` as the value for this parameter. * **minimal** includes: `id`, `hostname` and `status` * **default** includes **minimal** plus `architectureDescription`, `description`, `ipAddresses`, `lastRunDate`, `lastInventoryDate`, `machine`, `os`, `managementTechnology`, `policyServerId`, `properties` (be careful! Only node own properties, if you also need inherited properties, look at the dedicated `/nodes/{id}/inheritedProperties` endpoint), `policyMode `, `ram` and `timezone` * **full** includes: **default** plus `accounts`, `bios`, `controllers`, `environmentVariables`, `fileSystems`, `managementTechnologyDetails`, `memories`, `networkInterfaces`, `ports`, `processes`, `processors`, `slots`, `software`, `sound`, `storage`, `videos` and `virtualMachines`
    Object query = null; // Object | The criterion you want to find for your nodes. Replaces the `where`, `composition` and `select` parameters in a single parameter.
    List<Object> where = null; // List<Object> | The criterion you want to find for your nodes
    String composition = "and"; // String | Boolean operator to use between each  `where` criteria.
    String select = "node"; // String | What kind of data we want to include. Here we can get policy servers/relay by setting `nodeAndPolicyServer`. Only used if `where` is defined.
    try {
      ListPendingNodes200Response result = apiInstance.listPendingNodes(include, query, where, composition, select);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NodesApi#listPendingNodes");
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
| **include** | **String**| Level of information to include from the node inventory. Some base levels are defined (**minimal**, **default**, **full**). You can add fields you want to a base level by adding them to the list, possible values are keys from json answer. If you don&#39;t provide a base level, they will be added to &#x60;default&#x60; level, so if you only want os details, use &#x60;minimal,os&#x60; as the value for this parameter. * **minimal** includes: &#x60;id&#x60;, &#x60;hostname&#x60; and &#x60;status&#x60; * **default** includes **minimal** plus &#x60;architectureDescription&#x60;, &#x60;description&#x60;, &#x60;ipAddresses&#x60;, &#x60;lastRunDate&#x60;, &#x60;lastInventoryDate&#x60;, &#x60;machine&#x60;, &#x60;os&#x60;, &#x60;managementTechnology&#x60;, &#x60;policyServerId&#x60;, &#x60;properties&#x60; (be careful! Only node own properties, if you also need inherited properties, look at the dedicated &#x60;/nodes/{id}/inheritedProperties&#x60; endpoint), &#x60;policyMode &#x60;, &#x60;ram&#x60; and &#x60;timezone&#x60; * **full** includes: **default** plus &#x60;accounts&#x60;, &#x60;bios&#x60;, &#x60;controllers&#x60;, &#x60;environmentVariables&#x60;, &#x60;fileSystems&#x60;, &#x60;managementTechnologyDetails&#x60;, &#x60;memories&#x60;, &#x60;networkInterfaces&#x60;, &#x60;ports&#x60;, &#x60;processes&#x60;, &#x60;processors&#x60;, &#x60;slots&#x60;, &#x60;software&#x60;, &#x60;sound&#x60;, &#x60;storage&#x60;, &#x60;videos&#x60; and &#x60;virtualMachines&#x60; | [optional] [default to default] |
| **query** | [**Object**](.md)| The criterion you want to find for your nodes. Replaces the &#x60;where&#x60;, &#x60;composition&#x60; and &#x60;select&#x60; parameters in a single parameter. | [optional] |
| **where** | [**List&lt;Object&gt;**](Object.md)| The criterion you want to find for your nodes | [optional] |
| **composition** | **String**| Boolean operator to use between each  &#x60;where&#x60; criteria. | [optional] [default to and] [enum: and, or] |
| **select** | **String**| What kind of data we want to include. Here we can get policy servers/relay by setting &#x60;nodeAndPolicyServer&#x60;. Only used if &#x60;where&#x60; is defined. | [optional] [default to node] |

### Return type

[**ListPendingNodes200Response**](ListPendingNodes200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Nodes |  -  |

<a id="nodeDetails"></a>
# **nodeDetails**
> NodeDetails200Response nodeDetails(nodeId, include)

Get information about a node

Get details about a given node

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    NodesApi apiInstance = new NodesApi(defaultClient);
    String nodeId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Id of the target node
    String include = "default"; // String | Level of information to include from the node inventory. Some base levels are defined (**minimal**, **default**, **full**). You can add fields you want to a base level by adding them to the list, possible values are keys from json answer. If you don't provide a base level, they will be added to `default` level, so if you only want os details, use `minimal,os` as the value for this parameter. * **minimal** includes: `id`, `hostname` and `status` * **default** includes **minimal** plus `architectureDescription`, `description`, `ipAddresses`, `lastRunDate`, `lastInventoryDate`, `machine`, `os`, `managementTechnology`, `policyServerId`, `properties` (be careful! Only node own properties, if you also need inherited properties, look at the dedicated `/nodes/{id}/inheritedProperties` endpoint), `policyMode `, `ram` and `timezone` * **full** includes: **default** plus `accounts`, `bios`, `controllers`, `environmentVariables`, `fileSystems`, `managementTechnologyDetails`, `memories`, `networkInterfaces`, `ports`, `processes`, `processors`, `slots`, `software`, `sound`, `storage`, `videos` and `virtualMachines`
    try {
      NodeDetails200Response result = apiInstance.nodeDetails(nodeId, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NodesApi#nodeDetails");
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
| **nodeId** | **String**| Id of the target node | |
| **include** | **String**| Level of information to include from the node inventory. Some base levels are defined (**minimal**, **default**, **full**). You can add fields you want to a base level by adding them to the list, possible values are keys from json answer. If you don&#39;t provide a base level, they will be added to &#x60;default&#x60; level, so if you only want os details, use &#x60;minimal,os&#x60; as the value for this parameter. * **minimal** includes: &#x60;id&#x60;, &#x60;hostname&#x60; and &#x60;status&#x60; * **default** includes **minimal** plus &#x60;architectureDescription&#x60;, &#x60;description&#x60;, &#x60;ipAddresses&#x60;, &#x60;lastRunDate&#x60;, &#x60;lastInventoryDate&#x60;, &#x60;machine&#x60;, &#x60;os&#x60;, &#x60;managementTechnology&#x60;, &#x60;policyServerId&#x60;, &#x60;properties&#x60; (be careful! Only node own properties, if you also need inherited properties, look at the dedicated &#x60;/nodes/{id}/inheritedProperties&#x60; endpoint), &#x60;policyMode &#x60;, &#x60;ram&#x60; and &#x60;timezone&#x60; * **full** includes: **default** plus &#x60;accounts&#x60;, &#x60;bios&#x60;, &#x60;controllers&#x60;, &#x60;environmentVariables&#x60;, &#x60;fileSystems&#x60;, &#x60;managementTechnologyDetails&#x60;, &#x60;memories&#x60;, &#x60;networkInterfaces&#x60;, &#x60;ports&#x60;, &#x60;processes&#x60;, &#x60;processors&#x60;, &#x60;slots&#x60;, &#x60;software&#x60;, &#x60;sound&#x60;, &#x60;storage&#x60;, &#x60;videos&#x60; and &#x60;virtualMachines&#x60; | [optional] [default to default] |

### Return type

[**NodeDetails200Response**](NodeDetails200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Nodes |  -  |

<a id="nodeInheritedProperties"></a>
# **nodeInheritedProperties**
> NodeInheritedProperties200Response nodeInheritedProperties(nodeId)

Get inherited node properties for a node

This API returns all node properties for a node, including group inherited ones.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    NodesApi apiInstance = new NodesApi(defaultClient);
    String nodeId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Id of the target node
    try {
      NodeInheritedProperties200Response result = apiInstance.nodeInheritedProperties(nodeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NodesApi#nodeInheritedProperties");
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
| **nodeId** | **String**| Id of the target node | |

### Return type

[**NodeInheritedProperties200Response**](NodeInheritedProperties200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Node |  -  |

<a id="updateNode"></a>
# **updateNode**
> UpdateNode200Response updateNode(nodeId, nodeSettings)

Update node settings and properties

Update node settings and properties

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    NodesApi apiInstance = new NodesApi(defaultClient);
    String nodeId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Id of the target node
    NodeSettings nodeSettings = new NodeSettings(); // NodeSettings | 
    try {
      UpdateNode200Response result = apiInstance.updateNode(nodeId, nodeSettings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NodesApi#updateNode");
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
| **nodeId** | **String**| Id of the target node | |
| **nodeSettings** | [**NodeSettings**](NodeSettings.md)|  | [optional] |

### Return type

[**UpdateNode200Response**](UpdateNode200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Nodes |  -  |

