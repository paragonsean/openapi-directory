# NodeApi

All URIs are relative to *http://azure.local:19080*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**disableNode**](NodeApi.md#disableNode) | **POST** /Nodes/{nodeName}/$/Deactivate | Deactivate a Service Fabric cluster node with the specified deactivation intent. |
| [**enableNode**](NodeApi.md#enableNode) | **POST** /Nodes/{nodeName}/$/Activate | Activate a Service Fabric cluster node which is currently deactivated. |
| [**getNodeHealth**](NodeApi.md#getNodeHealth) | **GET** /Nodes/{nodeName}/$/GetHealth | Gets the health of a Service Fabric node. |
| [**getNodeHealthUsingPolicy**](NodeApi.md#getNodeHealthUsingPolicy) | **POST** /Nodes/{nodeName}/$/GetHealth | Gets the health of a Service Fabric node, by using the specified health policy. |
| [**getNodeInfo**](NodeApi.md#getNodeInfo) | **GET** /Nodes/{nodeName} | Gets the list of nodes in the Service Fabric cluster. |
| [**getNodeInfoList**](NodeApi.md#getNodeInfoList) | **GET** /Nodes | Gets the list of nodes in the Service Fabric cluster. |
| [**getNodeLoadInfo**](NodeApi.md#getNodeLoadInfo) | **GET** /Nodes/{nodeName}/$/GetLoadInformation | Gets the load information of a Service Fabric node. |
| [**removeNodeState**](NodeApi.md#removeNodeState) | **POST** /Nodes/{nodeName}/$/RemoveNodeState | Notifies Service Fabric that the persisted state on a node has been permanently removed or lost. |
| [**reportNodeHealth**](NodeApi.md#reportNodeHealth) | **POST** /Nodes/{nodeName}/$/ReportHealth | Sends a health report on the Service Fabric node. |
| [**restartNode**](NodeApi.md#restartNode) | **POST** /Nodes/{nodeName}/$/Restart | Restarts a Service Fabric cluster node. |


<a id="disableNode"></a>
# **disableNode**
> disableNode(apiVersion, nodeName, deactivationIntentDescription, timeout)

Deactivate a Service Fabric cluster node with the specified deactivation intent.

Deactivate a Service Fabric cluster node with the specified deactivation intent. Once the deactivation is in progress, the deactivation intent can be increased, but not decreased (for example, a node which is was deactivated with the Pause intent can be deactivated further with Restart, but not the other way around. Nodes may be reactivated using the Activate a node operation any time after they are deactivated. If the deactivation is not complete this will cancel the deactivation. A node which goes down and comes back up while deactivated will still need to be reactivated before services will be placed on that node.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    NodeApi apiInstance = new NodeApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
    String nodeName = "nodeName_example"; // String | The name of the node.
    DeactivationIntentDescription deactivationIntentDescription = new DeactivationIntentDescription(); // DeactivationIntentDescription | Describes the intent or reason for deactivating the node.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      apiInstance.disableNode(apiVersion, nodeName, deactivationIntentDescription, timeout);
    } catch (ApiException e) {
      System.err.println("Exception when calling NodeApi#disableNode");
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
| **apiVersion** | **String**| The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;. | [default to 6.0] [enum: 6.0] |
| **nodeName** | **String**| The name of the node. | |
| **deactivationIntentDescription** | [**DeactivationIntentDescription**](DeactivationIntentDescription.md)| Describes the intent or reason for deactivating the node. | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful operation will return 200 status code. |  -  |
| **0** | The detailed error response. |  -  |

<a id="enableNode"></a>
# **enableNode**
> enableNode(apiVersion, nodeName, timeout)

Activate a Service Fabric cluster node which is currently deactivated.

Activates a Service Fabric cluster node which is currently deactivated. Once activated, the node will again become a viable target for placing new replicas, and any deactivated replicas remaining on the node will be reactivated.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    NodeApi apiInstance = new NodeApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
    String nodeName = "nodeName_example"; // String | The name of the node.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      apiInstance.enableNode(apiVersion, nodeName, timeout);
    } catch (ApiException e) {
      System.err.println("Exception when calling NodeApi#enableNode");
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
| **apiVersion** | **String**| The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;. | [default to 6.0] [enum: 6.0] |
| **nodeName** | **String**| The name of the node. | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful operation will return 200 status code. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getNodeHealth"></a>
# **getNodeHealth**
> NodeHealth getNodeHealth(apiVersion, nodeName, eventsHealthStateFilter, timeout)

Gets the health of a Service Fabric node.

Gets the health of a Service Fabric node. Use EventsHealthStateFilter to filter the collection of health events reported on the node based on the health state. If the node that you specify by name does not exist in the health store, this returns an error.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    NodeApi apiInstance = new NodeApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
    String nodeName = "nodeName_example"; // String | The name of the node.
    Integer eventsHealthStateFilter = 0; // Integer | Allows filtering the collection of HealthEvent objects returned based on health state. The possible values for this parameter include integer value of one of the following health states. Only events that match the filter are returned. All events are used to evaluate the aggregated health state. If not specified, all entries are returned. The state values are flag based enumeration, so the value could be a combination of these value obtained using bitwise 'OR' operator. For example, If the provided value is 6 then all of the events with HealthState value of OK (2) and Warning (4) are returned.  - Default - Default value. Matches any HealthState. The value is zero. - None - Filter that doesn't match any HealthState value. Used in order to return no results on a given collection of states. The value is 1. - Ok - Filter that matches input with HealthState value Ok. The value is 2. - Warning - Filter that matches input with HealthState value Warning. The value is 4. - Error - Filter that matches input with HealthState value Error. The value is 8. - All - Filter that matches input with any HealthState value. The value is 65535. 
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      NodeHealth result = apiInstance.getNodeHealth(apiVersion, nodeName, eventsHealthStateFilter, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NodeApi#getNodeHealth");
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
| **apiVersion** | **String**| The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;. | [default to 6.0] [enum: 6.0] |
| **nodeName** | **String**| The name of the node. | |
| **eventsHealthStateFilter** | **Integer**| Allows filtering the collection of HealthEvent objects returned based on health state. The possible values for this parameter include integer value of one of the following health states. Only events that match the filter are returned. All events are used to evaluate the aggregated health state. If not specified, all entries are returned. The state values are flag based enumeration, so the value could be a combination of these value obtained using bitwise &#39;OR&#39; operator. For example, If the provided value is 6 then all of the events with HealthState value of OK (2) and Warning (4) are returned.  - Default - Default value. Matches any HealthState. The value is zero. - None - Filter that doesn&#39;t match any HealthState value. Used in order to return no results on a given collection of states. The value is 1. - Ok - Filter that matches input with HealthState value Ok. The value is 2. - Warning - Filter that matches input with HealthState value Warning. The value is 4. - Error - Filter that matches input with HealthState value Error. The value is 8. - All - Filter that matches input with any HealthState value. The value is 65535.  | [optional] [default to 0] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

[**NodeHealth**](NodeHealth.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful operation will return 200 status code and the requested node health information. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getNodeHealthUsingPolicy"></a>
# **getNodeHealthUsingPolicy**
> NodeHealth getNodeHealthUsingPolicy(apiVersion, nodeName, eventsHealthStateFilter, timeout, clusterHealthPolicy)

Gets the health of a Service Fabric node, by using the specified health policy.

Gets the health of a Service Fabric node. Use EventsHealthStateFilter to filter the collection of health events reported on the node based on the health state. Use ClusterHealthPolicy in the POST body to override the health policies used to evaluate the health. If the node that you specify by name does not exist in the health store, this returns an error.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    NodeApi apiInstance = new NodeApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
    String nodeName = "nodeName_example"; // String | The name of the node.
    Integer eventsHealthStateFilter = 0; // Integer | Allows filtering the collection of HealthEvent objects returned based on health state. The possible values for this parameter include integer value of one of the following health states. Only events that match the filter are returned. All events are used to evaluate the aggregated health state. If not specified, all entries are returned. The state values are flag based enumeration, so the value could be a combination of these value obtained using bitwise 'OR' operator. For example, If the provided value is 6 then all of the events with HealthState value of OK (2) and Warning (4) are returned.  - Default - Default value. Matches any HealthState. The value is zero. - None - Filter that doesn't match any HealthState value. Used in order to return no results on a given collection of states. The value is 1. - Ok - Filter that matches input with HealthState value Ok. The value is 2. - Warning - Filter that matches input with HealthState value Warning. The value is 4. - Error - Filter that matches input with HealthState value Error. The value is 8. - All - Filter that matches input with any HealthState value. The value is 65535. 
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    ClusterHealthPolicy clusterHealthPolicy = new ClusterHealthPolicy(); // ClusterHealthPolicy | Describes the health policies used to evaluate the health of a cluster or node. If not present, the health evaluation uses the health policy from cluster manifest or the default health policy.
    try {
      NodeHealth result = apiInstance.getNodeHealthUsingPolicy(apiVersion, nodeName, eventsHealthStateFilter, timeout, clusterHealthPolicy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NodeApi#getNodeHealthUsingPolicy");
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
| **apiVersion** | **String**| The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;. | [default to 6.0] [enum: 6.0] |
| **nodeName** | **String**| The name of the node. | |
| **eventsHealthStateFilter** | **Integer**| Allows filtering the collection of HealthEvent objects returned based on health state. The possible values for this parameter include integer value of one of the following health states. Only events that match the filter are returned. All events are used to evaluate the aggregated health state. If not specified, all entries are returned. The state values are flag based enumeration, so the value could be a combination of these value obtained using bitwise &#39;OR&#39; operator. For example, If the provided value is 6 then all of the events with HealthState value of OK (2) and Warning (4) are returned.  - Default - Default value. Matches any HealthState. The value is zero. - None - Filter that doesn&#39;t match any HealthState value. Used in order to return no results on a given collection of states. The value is 1. - Ok - Filter that matches input with HealthState value Ok. The value is 2. - Warning - Filter that matches input with HealthState value Warning. The value is 4. - Error - Filter that matches input with HealthState value Error. The value is 8. - All - Filter that matches input with any HealthState value. The value is 65535.  | [optional] [default to 0] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |
| **clusterHealthPolicy** | [**ClusterHealthPolicy**](ClusterHealthPolicy.md)| Describes the health policies used to evaluate the health of a cluster or node. If not present, the health evaluation uses the health policy from cluster manifest or the default health policy. | [optional] |

### Return type

[**NodeHealth**](NodeHealth.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful operation will return 200 status code and the requested node health information. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getNodeInfo"></a>
# **getNodeInfo**
> NodeInfo getNodeInfo(apiVersion, nodeName, timeout)

Gets the list of nodes in the Service Fabric cluster.

Gets the information about a specific node in the Service Fabric Cluster.The respons include the name, status, id, health, uptime and other details about the node.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    NodeApi apiInstance = new NodeApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
    String nodeName = "nodeName_example"; // String | The name of the node.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      NodeInfo result = apiInstance.getNodeInfo(apiVersion, nodeName, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NodeApi#getNodeInfo");
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
| **apiVersion** | **String**| The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;. | [default to 6.0] [enum: 6.0] |
| **nodeName** | **String**| The name of the node. | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

[**NodeInfo**](NodeInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful operation will return information about the node with the specified nodeName. |  -  |
| **204** | An empty response is returned if the specified nodeName is not found. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getNodeInfoList"></a>
# **getNodeInfoList**
> PagedNodeInfoList getNodeInfoList(apiVersion, continuationToken, nodeStatusFilter, timeout)

Gets the list of nodes in the Service Fabric cluster.

The Nodes endpoint returns information about the nodes in the Service Fabric Cluster. The respons include the name, status, id, health, uptime and other details about the node.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    NodeApi apiInstance = new NodeApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
    String continuationToken = "continuationToken_example"; // String | The continuation token parameter is used to obtain next set of results. A continuation token with a non empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
    String nodeStatusFilter = "default"; // String | Allows filtering the nodes based on the NodeStatus. Only the nodes that are matching the specified filter value will be returned. The filter value can be one of the following.    - default - This filter value will match all of the nodes excepts the ones with with status as Unknown or Removed.   - all - This filter value will match all of the nodes.   - up - This filter value will match nodes that are Up.   - down - This filter value will match nodes that are Down.   - enabling - This filter value will match nodes that are in the process of being enabled with status as Enabling.   - disabling - This filter value will match nodes that are in the process of being disabled with status as Disabling.   - disabled - This filter value will match nodes that are Disabled.   - unknown - This filter value will match nodes whose status is Unknown. A node would be in Unknown state if Service Fabric does not have authoritative information about that node. This can happen if the system learns about a node at runtime.   - removed - This filter value will match nodes whose status is Removed. These are the nodes that are removed from the cluster using the RemoveNodeState API. 
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      PagedNodeInfoList result = apiInstance.getNodeInfoList(apiVersion, continuationToken, nodeStatusFilter, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NodeApi#getNodeInfoList");
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
| **apiVersion** | **String**| The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;. | [default to 6.0] [enum: 6.0] |
| **continuationToken** | **String**| The continuation token parameter is used to obtain next set of results. A continuation token with a non empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results then the continuation token does not contain a value. The value of this parameter should not be URL encoded. | [optional] |
| **nodeStatusFilter** | **String**| Allows filtering the nodes based on the NodeStatus. Only the nodes that are matching the specified filter value will be returned. The filter value can be one of the following.    - default - This filter value will match all of the nodes excepts the ones with with status as Unknown or Removed.   - all - This filter value will match all of the nodes.   - up - This filter value will match nodes that are Up.   - down - This filter value will match nodes that are Down.   - enabling - This filter value will match nodes that are in the process of being enabled with status as Enabling.   - disabling - This filter value will match nodes that are in the process of being disabled with status as Disabling.   - disabled - This filter value will match nodes that are Disabled.   - unknown - This filter value will match nodes whose status is Unknown. A node would be in Unknown state if Service Fabric does not have authoritative information about that node. This can happen if the system learns about a node at runtime.   - removed - This filter value will match nodes whose status is Removed. These are the nodes that are removed from the cluster using the RemoveNodeState API.  | [optional] [default to default] [enum: default, all, up, down, enabling, disabling, disabled, unknown, removed] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

[**PagedNodeInfoList**](PagedNodeInfoList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of nodes in the cluster. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getNodeLoadInfo"></a>
# **getNodeLoadInfo**
> NodeLoadInfo getNodeLoadInfo(apiVersion, nodeName, timeout)

Gets the load information of a Service Fabric node.

Gets the load information of a Service Fabric node.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    NodeApi apiInstance = new NodeApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
    String nodeName = "nodeName_example"; // String | The name of the node.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      NodeLoadInfo result = apiInstance.getNodeLoadInfo(apiVersion, nodeName, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NodeApi#getNodeLoadInfo");
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
| **apiVersion** | **String**| The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;. | [default to 6.0] [enum: 6.0] |
| **nodeName** | **String**| The name of the node. | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

[**NodeLoadInfo**](NodeLoadInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful operation will return 200 status code and the requested node load information. |  -  |
| **0** | The detailed error response. |  -  |

<a id="removeNodeState"></a>
# **removeNodeState**
> removeNodeState(apiVersion, nodeName, timeout)

Notifies Service Fabric that the persisted state on a node has been permanently removed or lost.

Notifies Service Fabric that the persisted state on a node has been permanently removed or lost.  This implies that it is not possible to recover the persisted state of that node. This generally happens if a hard disk has been wiped clean, or if a hard disk crashes. The node has to be down for this operation to be successful. This operation lets Service Fabric know that the replicas on that node no longer exist, and that Service Fabric should stop waiting for those replicas to come back up. Do not run this cmdlet if the state on the node has not been removed and the node can comes back up with its state intact.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    NodeApi apiInstance = new NodeApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
    String nodeName = "nodeName_example"; // String | The name of the node.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      apiInstance.removeNodeState(apiVersion, nodeName, timeout);
    } catch (ApiException e) {
      System.err.println("Exception when calling NodeApi#removeNodeState");
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
| **apiVersion** | **String**| The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;. | [default to 6.0] [enum: 6.0] |
| **nodeName** | **String**| The name of the node. | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful operation will return 200 status code. |  -  |
| **0** | The detailed error response. |  -  |

<a id="reportNodeHealth"></a>
# **reportNodeHealth**
> reportNodeHealth(apiVersion, nodeName, healthInformation, immediate, timeout)

Sends a health report on the Service Fabric node.

Reports health state of the specified Service Fabric node. The report must contain the information about the source of the health report and property on which it is reported. The report is sent to a Service Fabric gateway node, which forwards to the health store. The report may be accepted by the gateway, but rejected by the health store after extra validation. For example, the health store may reject the report because of an invalid parameter, like a stale sequence number. To see whether the report was applied in the health store, run GetNodeHealth and check that the report appears in the HealthEvents section. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    NodeApi apiInstance = new NodeApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
    String nodeName = "nodeName_example"; // String | The name of the node.
    HealthInformation healthInformation = new HealthInformation(); // HealthInformation | Describes the health information for the health report. This information needs to be present in all of the health reports sent to the health manager.
    Boolean immediate = false; // Boolean | A flag which indicates whether the report should be sent immediately. A health report is sent to a Service Fabric gateway Application, which forwards to the health store. If Immediate is set to true, the report is sent immediately from Http Gateway to the health store, regardless of the fabric client settings that the Http Gateway Application is using. This is useful for critical reports that should be sent as soon as possible. Depending on timing and other conditions, sending the report may still fail, for example if the Http Gateway is closed or the message doesn't reach the Gateway. If Immediate is set to false, the report is sent based on the health client settings from the Http Gateway. Therefore, it will be batched according to the HealthReportSendInterval configuration. This is the recommended setting because it allows the health client to optimize health reporting messages to health store as well as health report processing. By default, reports are not sent immediately. 
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      apiInstance.reportNodeHealth(apiVersion, nodeName, healthInformation, immediate, timeout);
    } catch (ApiException e) {
      System.err.println("Exception when calling NodeApi#reportNodeHealth");
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
| **apiVersion** | **String**| The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;. | [default to 6.0] [enum: 6.0] |
| **nodeName** | **String**| The name of the node. | |
| **healthInformation** | [**HealthInformation**](HealthInformation.md)| Describes the health information for the health report. This information needs to be present in all of the health reports sent to the health manager. | |
| **immediate** | **Boolean**| A flag which indicates whether the report should be sent immediately. A health report is sent to a Service Fabric gateway Application, which forwards to the health store. If Immediate is set to true, the report is sent immediately from Http Gateway to the health store, regardless of the fabric client settings that the Http Gateway Application is using. This is useful for critical reports that should be sent as soon as possible. Depending on timing and other conditions, sending the report may still fail, for example if the Http Gateway is closed or the message doesn&#39;t reach the Gateway. If Immediate is set to false, the report is sent based on the health client settings from the Http Gateway. Therefore, it will be batched according to the HealthReportSendInterval configuration. This is the recommended setting because it allows the health client to optimize health reporting messages to health store as well as health report processing. By default, reports are not sent immediately.  | [optional] [default to false] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful operation will return 200 status code. |  -  |
| **0** | The detailed error response. |  -  |

<a id="restartNode"></a>
# **restartNode**
> restartNode(apiVersion, nodeName, restartNodeDescription, timeout)

Restarts a Service Fabric cluster node.

Restarts a Service Fabric cluster node that is already started.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    NodeApi apiInstance = new NodeApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
    String nodeName = "nodeName_example"; // String | The name of the node.
    RestartNodeDescription restartNodeDescription = new RestartNodeDescription(); // RestartNodeDescription | The instance of the node to be restarted and a flag indicating the need to take dump of the fabric process.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      apiInstance.restartNode(apiVersion, nodeName, restartNodeDescription, timeout);
    } catch (ApiException e) {
      System.err.println("Exception when calling NodeApi#restartNode");
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
| **apiVersion** | **String**| The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;. | [default to 6.0] [enum: 6.0] |
| **nodeName** | **String**| The name of the node. | |
| **restartNodeDescription** | [**RestartNodeDescription**](RestartNodeDescription.md)| The instance of the node to be restarted and a flag indicating the need to take dump of the fabric process. | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful operation will return 200 status code. A successful operation means that the restart command was received by the node and it is in the process of restarting. Check the status of the node by calling GetNode operation. |  -  |
| **0** | The detailed error response. |  -  |

