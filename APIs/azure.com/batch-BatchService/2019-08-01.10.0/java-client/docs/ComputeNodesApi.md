# ComputeNodesApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**computeNodeAddUser**](ComputeNodesApi.md#computeNodeAddUser) | **POST** /pools/{poolId}/nodes/{nodeId}/users | Adds a user Account to the specified Compute Node. |
| [**computeNodeDeleteUser**](ComputeNodesApi.md#computeNodeDeleteUser) | **DELETE** /pools/{poolId}/nodes/{nodeId}/users/{userName} | Deletes a user Account from the specified Compute Node. |
| [**computeNodeDisableScheduling**](ComputeNodesApi.md#computeNodeDisableScheduling) | **POST** /pools/{poolId}/nodes/{nodeId}/disablescheduling | Disables Task scheduling on the specified Compute Node. |
| [**computeNodeEnableScheduling**](ComputeNodesApi.md#computeNodeEnableScheduling) | **POST** /pools/{poolId}/nodes/{nodeId}/enablescheduling | Enables Task scheduling on the specified Compute Node. |
| [**computeNodeGet**](ComputeNodesApi.md#computeNodeGet) | **GET** /pools/{poolId}/nodes/{nodeId} | Gets information about the specified Compute Node. |
| [**computeNodeGetRemoteDesktop**](ComputeNodesApi.md#computeNodeGetRemoteDesktop) | **GET** /pools/{poolId}/nodes/{nodeId}/rdp | Gets the Remote Desktop Protocol file for the specified Compute Node. |
| [**computeNodeGetRemoteLoginSettings**](ComputeNodesApi.md#computeNodeGetRemoteLoginSettings) | **GET** /pools/{poolId}/nodes/{nodeId}/remoteloginsettings | Gets the settings required for remote login to a Compute Node. |
| [**computeNodeList**](ComputeNodesApi.md#computeNodeList) | **GET** /pools/{poolId}/nodes | Lists the Compute Nodes in the specified Pool. |
| [**computeNodeReboot**](ComputeNodesApi.md#computeNodeReboot) | **POST** /pools/{poolId}/nodes/{nodeId}/reboot | Restarts the specified Compute Node. |
| [**computeNodeReimage**](ComputeNodesApi.md#computeNodeReimage) | **POST** /pools/{poolId}/nodes/{nodeId}/reimage | Reinstalls the operating system on the specified Compute Node. |
| [**computeNodeUpdateUser**](ComputeNodesApi.md#computeNodeUpdateUser) | **PUT** /pools/{poolId}/nodes/{nodeId}/users/{userName} | Updates the password and expiration time of a user Account on the specified Compute Node. |
| [**computeNodeUploadBatchServiceLogs**](ComputeNodesApi.md#computeNodeUploadBatchServiceLogs) | **POST** /pools/{poolId}/nodes/{nodeId}/uploadbatchservicelogs | Upload Azure Batch service log files from the specified Compute Node to Azure Blob Storage. |
| [**poolRemoveNodes**](ComputeNodesApi.md#poolRemoveNodes) | **POST** /pools/{poolId}/removenodes | Removes Compute Nodes from the specified Pool. |


<a id="computeNodeAddUser"></a>
# **computeNodeAddUser**
> computeNodeAddUser(poolId, nodeId, apiVersion, user, timeout, clientRequestId, returnClientRequestId, ocpDate)

Adds a user Account to the specified Compute Node.

You can add a user Account to a Compute Node only when it is in the idle or running state.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComputeNodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ComputeNodesApi apiInstance = new ComputeNodesApi(defaultClient);
    String poolId = "poolId_example"; // String | The ID of the Pool that contains the Compute Node.
    String nodeId = "nodeId_example"; // String | The ID of the machine on which you want to create a user Account.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    ComputeNodeUser user = new ComputeNodeUser(); // ComputeNodeUser | The user Account to be created.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    UUID clientRequestId = UUID.randomUUID(); // UUID | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = false; // Boolean | Whether the server should return the client-request-id in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    try {
      apiInstance.computeNodeAddUser(poolId, nodeId, apiVersion, user, timeout, clientRequestId, returnClientRequestId, ocpDate);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComputeNodesApi#computeNodeAddUser");
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
| **poolId** | **String**| The ID of the Pool that contains the Compute Node. | |
| **nodeId** | **String**| The ID of the machine on which you want to create a user Account. | |
| **apiVersion** | **String**| Client API Version. | |
| **user** | [**ComputeNodeUser**](ComputeNodeUser.md)| The user Account to be created. | |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **UUID**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false] |
| **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json; odata=minimalmetadata
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The request to the Batch service was successful. |  * ETag - The ETag HTTP response header. This is an opaque string. You can use it to detect whether the resource has changed between requests. In particular, you can pass the ETag to one of the If-Modified-Since, If-Unmodified-Since, If-Match or If-None-Match headers. <br>  * client-request-id - The client-request-id provided by the client during the request. This will be returned only if the return-client-request-id parameter was set to true. <br>  * DataServiceId - The OData ID of the resource to which the request applied. <br>  * Last-Modified - The time at which the resource was last modified. <br>  * request-id - A unique identifier for the request that was made to the Batch service. If a request is consistently failing and you have verified that the request is properly formulated, you may use this value to report the error to Microsoft. In your report, include the value of this request ID, the approximate time that the request was made, the Batch Account against which the request was made, and the region that Account resides in. <br>  |
| **0** | The error from the Batch service. |  -  |

<a id="computeNodeDeleteUser"></a>
# **computeNodeDeleteUser**
> computeNodeDeleteUser(poolId, nodeId, userName, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate)

Deletes a user Account from the specified Compute Node.

You can delete a user Account to a Compute Node only when it is in the idle or running state.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComputeNodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ComputeNodesApi apiInstance = new ComputeNodesApi(defaultClient);
    String poolId = "poolId_example"; // String | The ID of the Pool that contains the Compute Node.
    String nodeId = "nodeId_example"; // String | The ID of the machine on which you want to delete a user Account.
    String userName = "userName_example"; // String | The name of the user Account to delete.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    UUID clientRequestId = UUID.randomUUID(); // UUID | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = false; // Boolean | Whether the server should return the client-request-id in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    try {
      apiInstance.computeNodeDeleteUser(poolId, nodeId, userName, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComputeNodesApi#computeNodeDeleteUser");
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
| **poolId** | **String**| The ID of the Pool that contains the Compute Node. | |
| **nodeId** | **String**| The ID of the machine on which you want to delete a user Account. | |
| **userName** | **String**| The name of the user Account to delete. | |
| **apiVersion** | **String**| Client API Version. | |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **UUID**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false] |
| **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request to the Batch service was successful. |  * client-request-id - The client-request-id provided by the client during the request. This will be returned only if the return-client-request-id parameter was set to true. <br>  * request-id - A unique identifier for the request that was made to the Batch service. If a request is consistently failing and you have verified that the request is properly formulated, you may use this value to report the error to Microsoft. In your report, include the value of this request ID, the approximate time that the request was made, the Batch Account against which the request was made, and the region that Account resides in. <br>  |
| **0** | The error from the Batch service. |  -  |

<a id="computeNodeDisableScheduling"></a>
# **computeNodeDisableScheduling**
> computeNodeDisableScheduling(poolId, nodeId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate, nodeDisableSchedulingParameter)

Disables Task scheduling on the specified Compute Node.

You can disable Task scheduling on a Compute Node only if its current scheduling state is enabled.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComputeNodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ComputeNodesApi apiInstance = new ComputeNodesApi(defaultClient);
    String poolId = "poolId_example"; // String | The ID of the Pool that contains the Compute Node.
    String nodeId = "nodeId_example"; // String | The ID of the Compute Node on which you want to disable Task scheduling.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    UUID clientRequestId = UUID.randomUUID(); // UUID | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = false; // Boolean | Whether the server should return the client-request-id in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    NodeDisableSchedulingParameter nodeDisableSchedulingParameter = new NodeDisableSchedulingParameter(); // NodeDisableSchedulingParameter | The parameters for the request.
    try {
      apiInstance.computeNodeDisableScheduling(poolId, nodeId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate, nodeDisableSchedulingParameter);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComputeNodesApi#computeNodeDisableScheduling");
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
| **poolId** | **String**| The ID of the Pool that contains the Compute Node. | |
| **nodeId** | **String**| The ID of the Compute Node on which you want to disable Task scheduling. | |
| **apiVersion** | **String**| Client API Version. | |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **UUID**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false] |
| **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] |
| **nodeDisableSchedulingParameter** | [**NodeDisableSchedulingParameter**](NodeDisableSchedulingParameter.md)| The parameters for the request. | [optional] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json; odata=minimalmetadata
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request to the Batch service was successful. |  * ETag - The ETag HTTP response header. This is an opaque string. You can use it to detect whether the resource has changed between requests. In particular, you can pass the ETag to one of the If-Modified-Since, If-Unmodified-Since, If-Match or If-None-Match headers. <br>  * client-request-id - The client-request-id provided by the client during the request. This will be returned only if the return-client-request-id parameter was set to true. <br>  * DataServiceId - The OData ID of the resource to which the request applied. <br>  * Last-Modified - The time at which the resource was last modified. <br>  * request-id - A unique identifier for the request that was made to the Batch service. If a request is consistently failing and you have verified that the request is properly formulated, you may use this value to report the error to Microsoft. In your report, include the value of this request ID, the approximate time that the request was made, the Batch Account against which the request was made, and the region that Account resides in. <br>  |
| **0** | The error from the Batch service. |  -  |

<a id="computeNodeEnableScheduling"></a>
# **computeNodeEnableScheduling**
> computeNodeEnableScheduling(poolId, nodeId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate)

Enables Task scheduling on the specified Compute Node.

You can enable Task scheduling on a Compute Node only if its current scheduling state is disabled

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComputeNodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ComputeNodesApi apiInstance = new ComputeNodesApi(defaultClient);
    String poolId = "poolId_example"; // String | The ID of the Pool that contains the Compute Node.
    String nodeId = "nodeId_example"; // String | The ID of the Compute Node on which you want to enable Task scheduling.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    UUID clientRequestId = UUID.randomUUID(); // UUID | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = false; // Boolean | Whether the server should return the client-request-id in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    try {
      apiInstance.computeNodeEnableScheduling(poolId, nodeId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComputeNodesApi#computeNodeEnableScheduling");
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
| **poolId** | **String**| The ID of the Pool that contains the Compute Node. | |
| **nodeId** | **String**| The ID of the Compute Node on which you want to enable Task scheduling. | |
| **apiVersion** | **String**| Client API Version. | |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **UUID**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false] |
| **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request to the Batch service was successful. |  * ETag - The ETag HTTP response header. This is an opaque string. You can use it to detect whether the resource has changed between requests. In particular, you can pass the ETag to one of the If-Modified-Since, If-Unmodified-Since, If-Match or If-None-Match headers. <br>  * client-request-id - The client-request-id provided by the client during the request. This will be returned only if the return-client-request-id parameter was set to true. <br>  * DataServiceId - The OData ID of the resource to which the request applied. <br>  * Last-Modified - The time at which the resource was last modified. <br>  * request-id - A unique identifier for the request that was made to the Batch service. If a request is consistently failing and you have verified that the request is properly formulated, you may use this value to report the error to Microsoft. In your report, include the value of this request ID, the approximate time that the request was made, the Batch Account against which the request was made, and the region that Account resides in. <br>  |
| **0** | The error from the Batch service. |  -  |

<a id="computeNodeGet"></a>
# **computeNodeGet**
> ComputeNode computeNodeGet(poolId, nodeId, apiVersion, $select, timeout, clientRequestId, returnClientRequestId, ocpDate)

Gets information about the specified Compute Node.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComputeNodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ComputeNodesApi apiInstance = new ComputeNodesApi(defaultClient);
    String poolId = "poolId_example"; // String | The ID of the Pool that contains the Compute Node.
    String nodeId = "nodeId_example"; // String | The ID of the Compute Node that you want to get information about.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String $select = "$select_example"; // String | An OData $select clause.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    UUID clientRequestId = UUID.randomUUID(); // UUID | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = false; // Boolean | Whether the server should return the client-request-id in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    try {
      ComputeNode result = apiInstance.computeNodeGet(poolId, nodeId, apiVersion, $select, timeout, clientRequestId, returnClientRequestId, ocpDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComputeNodesApi#computeNodeGet");
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
| **poolId** | **String**| The ID of the Pool that contains the Compute Node. | |
| **nodeId** | **String**| The ID of the Compute Node that you want to get information about. | |
| **apiVersion** | **String**| Client API Version. | |
| **$select** | **String**| An OData $select clause. | [optional] |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **UUID**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false] |
| **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] |

### Return type

[**ComputeNode**](ComputeNode.md)

### Authorization

[api_key](../README.md#api_key), [azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A response containing the Compute Node. |  * ETag - The ETag HTTP response header. This is an opaque string. You can use it to detect whether the resource has changed between requests. In particular, you can pass the ETag to one of the If-Modified-Since, If-Unmodified-Since, If-Match or If-None-Match headers. <br>  * client-request-id - The client-request-id provided by the client during the request. This will be returned only if the return-client-request-id parameter was set to true. <br>  * Last-Modified - The time at which the resource was last modified. <br>  * request-id - A unique identifier for the request that was made to the Batch service. If a request is consistently failing and you have verified that the request is properly formulated, you may use this value to report the error to Microsoft. In your report, include the value of this request ID, the approximate time that the request was made, the Batch Account against which the request was made, and the region that Account resides in. <br>  |
| **0** | The error from the Batch service. |  -  |

<a id="computeNodeGetRemoteDesktop"></a>
# **computeNodeGetRemoteDesktop**
> Object computeNodeGetRemoteDesktop(poolId, nodeId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate)

Gets the Remote Desktop Protocol file for the specified Compute Node.

Before you can access a Compute Node by using the RDP file, you must create a user Account on the Compute Node. This API can only be invoked on Pools created with a cloud service configuration. For Pools created with a virtual machine configuration, see the GetRemoteLoginSettings API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComputeNodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ComputeNodesApi apiInstance = new ComputeNodesApi(defaultClient);
    String poolId = "poolId_example"; // String | The ID of the Pool that contains the Compute Node.
    String nodeId = "nodeId_example"; // String | The ID of the Compute Node for which you want to get the Remote Desktop Protocol file.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    UUID clientRequestId = UUID.randomUUID(); // UUID | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = false; // Boolean | Whether the server should return the client-request-id in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    try {
      Object result = apiInstance.computeNodeGetRemoteDesktop(poolId, nodeId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComputeNodesApi#computeNodeGetRemoteDesktop");
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
| **poolId** | **String**| The ID of the Pool that contains the Compute Node. | |
| **nodeId** | **String**| The ID of the Compute Node for which you want to get the Remote Desktop Protocol file. | |
| **apiVersion** | **String**| Client API Version. | |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **UUID**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false] |
| **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] |

### Return type

**Object**

### Authorization

[api_key](../README.md#api_key), [azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A response containing the RDP information. |  * ETag - The ETag HTTP response header. This is an opaque string. You can use it to detect whether the resource has changed between requests. In particular, you can pass the ETag to one of the If-Modified-Since, If-Unmodified-Since, If-Match or If-None-Match headers. <br>  * client-request-id - The client-request-id provided by the client during the request. This will be returned only if the return-client-request-id parameter was set to true. <br>  * Last-Modified - The time at which the resource was last modified. <br>  * request-id - A unique identifier for the request that was made to the Batch service. If a request is consistently failing and you have verified that the request is properly formulated, you may use this value to report the error to Microsoft. In your report, include the value of this request ID, the approximate time that the request was made, the Batch Account against which the request was made, and the region that Account resides in. <br>  |
| **0** | The error from the Batch service. |  -  |

<a id="computeNodeGetRemoteLoginSettings"></a>
# **computeNodeGetRemoteLoginSettings**
> ComputeNodeGetRemoteLoginSettingsResult computeNodeGetRemoteLoginSettings(poolId, nodeId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate)

Gets the settings required for remote login to a Compute Node.

Before you can remotely login to a Compute Node using the remote login settings, you must create a user Account on the Compute Node. This API can be invoked only on Pools created with the virtual machine configuration property. For Pools created with a cloud service configuration, see the GetRemoteDesktop API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComputeNodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ComputeNodesApi apiInstance = new ComputeNodesApi(defaultClient);
    String poolId = "poolId_example"; // String | The ID of the Pool that contains the Compute Node.
    String nodeId = "nodeId_example"; // String | The ID of the Compute Node for which to obtain the remote login settings.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    UUID clientRequestId = UUID.randomUUID(); // UUID | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = false; // Boolean | Whether the server should return the client-request-id in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    try {
      ComputeNodeGetRemoteLoginSettingsResult result = apiInstance.computeNodeGetRemoteLoginSettings(poolId, nodeId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComputeNodesApi#computeNodeGetRemoteLoginSettings");
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
| **poolId** | **String**| The ID of the Pool that contains the Compute Node. | |
| **nodeId** | **String**| The ID of the Compute Node for which to obtain the remote login settings. | |
| **apiVersion** | **String**| Client API Version. | |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **UUID**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false] |
| **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] |

### Return type

[**ComputeNodeGetRemoteLoginSettingsResult**](ComputeNodeGetRemoteLoginSettingsResult.md)

### Authorization

[api_key](../README.md#api_key), [azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A response containing the login settings. |  * ETag - The ETag HTTP response header. This is an opaque string. You can use it to detect whether the resource has changed between requests. In particular, you can pass the ETag to one of the If-Modified-Since, If-Unmodified-Since, If-Match or If-None-Match headers. <br>  * client-request-id - The client-request-id provided by the client during the request. This will be returned only if the return-client-request-id parameter was set to true. <br>  * Last-Modified - The time at which the resource was last modified. <br>  * request-id - A unique identifier for the request that was made to the Batch service. If a request is consistently failing and you have verified that the request is properly formulated, you may use this value to report the error to Microsoft. In your report, include the value of this request ID, the approximate time that the request was made, the Batch Account against which the request was made, and the region that Account resides in. <br>  |
| **0** | The error from the Batch service. |  -  |

<a id="computeNodeList"></a>
# **computeNodeList**
> ComputeNodeListResult computeNodeList(poolId, apiVersion, $filter, $select, maxresults, timeout, clientRequestId, returnClientRequestId, ocpDate)

Lists the Compute Nodes in the specified Pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComputeNodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ComputeNodesApi apiInstance = new ComputeNodesApi(defaultClient);
    String poolId = "poolId_example"; // String | The ID of the Pool from which you want to list Compute Nodes.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String $filter = "$filter_example"; // String | An OData $filter clause. For more information on constructing this filter, see https://docs.microsoft.com/en-us/rest/api/batchservice/odata-filters-in-batch#list-nodes-in-a-pool.
    String $select = "$select_example"; // String | An OData $select clause.
    Integer maxresults = 1000; // Integer | The maximum number of items to return in the response. A maximum of 1000 Compute Nodes can be returned.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    UUID clientRequestId = UUID.randomUUID(); // UUID | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = false; // Boolean | Whether the server should return the client-request-id in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    try {
      ComputeNodeListResult result = apiInstance.computeNodeList(poolId, apiVersion, $filter, $select, maxresults, timeout, clientRequestId, returnClientRequestId, ocpDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComputeNodesApi#computeNodeList");
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
| **poolId** | **String**| The ID of the Pool from which you want to list Compute Nodes. | |
| **apiVersion** | **String**| Client API Version. | |
| **$filter** | **String**| An OData $filter clause. For more information on constructing this filter, see https://docs.microsoft.com/en-us/rest/api/batchservice/odata-filters-in-batch#list-nodes-in-a-pool. | [optional] |
| **$select** | **String**| An OData $select clause. | [optional] |
| **maxresults** | **Integer**| The maximum number of items to return in the response. A maximum of 1000 Compute Nodes can be returned. | [optional] [default to 1000] |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **UUID**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false] |
| **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] |

### Return type

[**ComputeNodeListResult**](ComputeNodeListResult.md)

### Authorization

[api_key](../README.md#api_key), [azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A response containing the list of Compute Nodes. |  * ETag - The ETag HTTP response header. This is an opaque string. You can use it to detect whether the resource has changed between requests. In particular, you can pass the ETag to one of the If-Modified-Since, If-Unmodified-Since, If-Match or If-None-Match headers. <br>  * client-request-id - The client-request-id provided by the client during the request. This will be returned only if the return-client-request-id parameter was set to true. <br>  * Last-Modified - The time at which the resource was last modified. <br>  * request-id - A unique identifier for the request that was made to the Batch service. If a request is consistently failing and you have verified that the request is properly formulated, you may use this value to report the error to Microsoft. In your report, include the value of this request ID, the approximate time that the request was made, the Batch Account against which the request was made, and the region that Account resides in. <br>  |
| **0** | The error from the Batch service. |  -  |

<a id="computeNodeReboot"></a>
# **computeNodeReboot**
> computeNodeReboot(poolId, nodeId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate, nodeRebootParameter)

Restarts the specified Compute Node.

You can restart a Compute Node only if it is in an idle or running state.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComputeNodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ComputeNodesApi apiInstance = new ComputeNodesApi(defaultClient);
    String poolId = "poolId_example"; // String | The ID of the Pool that contains the Compute Node.
    String nodeId = "nodeId_example"; // String | The ID of the Compute Node that you want to restart.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    UUID clientRequestId = UUID.randomUUID(); // UUID | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = false; // Boolean | Whether the server should return the client-request-id in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    NodeRebootParameter nodeRebootParameter = new NodeRebootParameter(); // NodeRebootParameter | The parameters for the request.
    try {
      apiInstance.computeNodeReboot(poolId, nodeId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate, nodeRebootParameter);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComputeNodesApi#computeNodeReboot");
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
| **poolId** | **String**| The ID of the Pool that contains the Compute Node. | |
| **nodeId** | **String**| The ID of the Compute Node that you want to restart. | |
| **apiVersion** | **String**| Client API Version. | |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **UUID**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false] |
| **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] |
| **nodeRebootParameter** | [**NodeRebootParameter**](NodeRebootParameter.md)| The parameters for the request. | [optional] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json; odata=minimalmetadata
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The request to the Batch service was successful. |  * ETag - The ETag HTTP response header. This is an opaque string. You can use it to detect whether the resource has changed between requests. In particular, you can pass the ETag to one of the If-Modified-Since, If-Unmodified-Since, If-Match or If-None-Match headers. <br>  * client-request-id - The client-request-id provided by the client during the request. This will be returned only if the return-client-request-id parameter was set to true. <br>  * DataServiceId - The OData ID of the resource to which the request applied. <br>  * Last-Modified - The time at which the resource was last modified. <br>  * request-id - A unique identifier for the request that was made to the Batch service. If a request is consistently failing and you have verified that the request is properly formulated, you may use this value to report the error to Microsoft. In your report, include the value of this request ID, the approximate time that the request was made, the Batch Account against which the request was made, and the region that Account resides in. <br>  |
| **0** | The error from the Batch service. |  -  |

<a id="computeNodeReimage"></a>
# **computeNodeReimage**
> computeNodeReimage(poolId, nodeId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate, nodeReimageParameter)

Reinstalls the operating system on the specified Compute Node.

You can reinstall the operating system on a Compute Node only if it is in an idle or running state. This API can be invoked only on Pools created with the cloud service configuration property.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComputeNodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ComputeNodesApi apiInstance = new ComputeNodesApi(defaultClient);
    String poolId = "poolId_example"; // String | The ID of the Pool that contains the Compute Node.
    String nodeId = "nodeId_example"; // String | The ID of the Compute Node that you want to restart.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    UUID clientRequestId = UUID.randomUUID(); // UUID | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = false; // Boolean | Whether the server should return the client-request-id in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    NodeReimageParameter nodeReimageParameter = new NodeReimageParameter(); // NodeReimageParameter | The parameters for the request.
    try {
      apiInstance.computeNodeReimage(poolId, nodeId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate, nodeReimageParameter);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComputeNodesApi#computeNodeReimage");
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
| **poolId** | **String**| The ID of the Pool that contains the Compute Node. | |
| **nodeId** | **String**| The ID of the Compute Node that you want to restart. | |
| **apiVersion** | **String**| Client API Version. | |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **UUID**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false] |
| **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] |
| **nodeReimageParameter** | [**NodeReimageParameter**](NodeReimageParameter.md)| The parameters for the request. | [optional] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json; odata=minimalmetadata
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The request to the Batch service was successful. |  * ETag - The ETag HTTP response header. This is an opaque string. You can use it to detect whether the resource has changed between requests. In particular, you can pass the ETag to one of the If-Modified-Since, If-Unmodified-Since, If-Match or If-None-Match headers. <br>  * client-request-id - The client-request-id provided by the client during the request. This will be returned only if the return-client-request-id parameter was set to true. <br>  * DataServiceId - The OData ID of the resource to which the request applied. <br>  * Last-Modified - The time at which the resource was last modified. <br>  * request-id - A unique identifier for the request that was made to the Batch service. If a request is consistently failing and you have verified that the request is properly formulated, you may use this value to report the error to Microsoft. In your report, include the value of this request ID, the approximate time that the request was made, the Batch Account against which the request was made, and the region that Account resides in. <br>  |
| **0** | The error from the Batch service. |  -  |

<a id="computeNodeUpdateUser"></a>
# **computeNodeUpdateUser**
> computeNodeUpdateUser(poolId, nodeId, userName, apiVersion, nodeUpdateUserParameter, timeout, clientRequestId, returnClientRequestId, ocpDate)

Updates the password and expiration time of a user Account on the specified Compute Node.

This operation replaces of all the updatable properties of the Account. For example, if the expiryTime element is not specified, the current value is replaced with the default value, not left unmodified. You can update a user Account on a Compute Node only when it is in the idle or running state.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComputeNodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ComputeNodesApi apiInstance = new ComputeNodesApi(defaultClient);
    String poolId = "poolId_example"; // String | The ID of the Pool that contains the Compute Node.
    String nodeId = "nodeId_example"; // String | The ID of the machine on which you want to update a user Account.
    String userName = "userName_example"; // String | The name of the user Account to update.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    NodeUpdateUserParameter nodeUpdateUserParameter = new NodeUpdateUserParameter(); // NodeUpdateUserParameter | The parameters for the request.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    UUID clientRequestId = UUID.randomUUID(); // UUID | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = false; // Boolean | Whether the server should return the client-request-id in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    try {
      apiInstance.computeNodeUpdateUser(poolId, nodeId, userName, apiVersion, nodeUpdateUserParameter, timeout, clientRequestId, returnClientRequestId, ocpDate);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComputeNodesApi#computeNodeUpdateUser");
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
| **poolId** | **String**| The ID of the Pool that contains the Compute Node. | |
| **nodeId** | **String**| The ID of the machine on which you want to update a user Account. | |
| **userName** | **String**| The name of the user Account to update. | |
| **apiVersion** | **String**| Client API Version. | |
| **nodeUpdateUserParameter** | [**NodeUpdateUserParameter**](NodeUpdateUserParameter.md)| The parameters for the request. | |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **UUID**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false] |
| **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json; odata=minimalmetadata
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request to the Batch service was successful. |  * ETag - The ETag HTTP response header. This is an opaque string. You can use it to detect whether the resource has changed between requests. In particular, you can pass the ETag to one of the If-Modified-Since, If-Unmodified-Since, If-Match or If-None-Match headers. <br>  * client-request-id - The client-request-id provided by the client during the request. This will be returned only if the return-client-request-id parameter was set to true. <br>  * DataServiceId - The OData ID of the resource to which the request applied. <br>  * Last-Modified - The time at which the resource was last modified. <br>  * request-id - A unique identifier for the request that was made to the Batch service. If a request is consistently failing and you have verified that the request is properly formulated, you may use this value to report the error to Microsoft. In your report, include the value of this request ID, the approximate time that the request was made, the Batch Account against which the request was made, and the region that Account resides in. <br>  |
| **0** | The error from the Batch service. |  -  |

<a id="computeNodeUploadBatchServiceLogs"></a>
# **computeNodeUploadBatchServiceLogs**
> UploadBatchServiceLogsResult computeNodeUploadBatchServiceLogs(poolId, nodeId, apiVersion, uploadBatchServiceLogsConfiguration, timeout, clientRequestId, returnClientRequestId, ocpDate)

Upload Azure Batch service log files from the specified Compute Node to Azure Blob Storage.

This is for gathering Azure Batch service log files in an automated fashion from Compute Nodes if you are experiencing an error and wish to escalate to Azure support. The Azure Batch service log files should be shared with Azure support to aid in debugging issues with the Batch service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComputeNodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ComputeNodesApi apiInstance = new ComputeNodesApi(defaultClient);
    String poolId = "poolId_example"; // String | The ID of the Pool that contains the Compute Node.
    String nodeId = "nodeId_example"; // String | The ID of the Compute Node from which you want to upload the Azure Batch service log files.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    UploadBatchServiceLogsConfiguration uploadBatchServiceLogsConfiguration = new UploadBatchServiceLogsConfiguration(); // UploadBatchServiceLogsConfiguration | The Azure Batch service log files upload configuration.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    UUID clientRequestId = UUID.randomUUID(); // UUID | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = false; // Boolean | Whether the server should return the client-request-id in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    try {
      UploadBatchServiceLogsResult result = apiInstance.computeNodeUploadBatchServiceLogs(poolId, nodeId, apiVersion, uploadBatchServiceLogsConfiguration, timeout, clientRequestId, returnClientRequestId, ocpDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComputeNodesApi#computeNodeUploadBatchServiceLogs");
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
| **poolId** | **String**| The ID of the Pool that contains the Compute Node. | |
| **nodeId** | **String**| The ID of the Compute Node from which you want to upload the Azure Batch service log files. | |
| **apiVersion** | **String**| Client API Version. | |
| **uploadBatchServiceLogsConfiguration** | [**UploadBatchServiceLogsConfiguration**](UploadBatchServiceLogsConfiguration.md)| The Azure Batch service log files upload configuration. | |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **UUID**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false] |
| **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] |

### Return type

[**UploadBatchServiceLogsResult**](UploadBatchServiceLogsResult.md)

### Authorization

[api_key](../README.md#api_key), [azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json; odata=minimalmetadata
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request to the Batch service was successful. |  * client-request-id - The client-request-id provided by the client during the request. This will be returned only if the return-client-request-id parameter was set to true. <br>  * request-id - A unique identifier for the request that was made to the Batch service. If a request is consistently failing and you have verified that the request is properly formulated, you may use this value to report the error to Microsoft. In your report, include the value of this request ID, the approximate time that the request was made, the Batch Account against which the request was made, and the region that Account resides in. <br>  |
| **0** | The error from the Batch service. |  -  |

<a id="poolRemoveNodes"></a>
# **poolRemoveNodes**
> poolRemoveNodes(poolId, apiVersion, nodeRemoveParameter, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince)

Removes Compute Nodes from the specified Pool.

This operation can only run when the allocation state of the Pool is steady. When this operation runs, the allocation state changes from steady to resizing.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComputeNodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ComputeNodesApi apiInstance = new ComputeNodesApi(defaultClient);
    String poolId = "poolId_example"; // String | The ID of the Pool from which you want to remove Compute Nodes.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    NodeRemoveParameter nodeRemoveParameter = new NodeRemoveParameter(); // NodeRemoveParameter | The parameters for the request.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    UUID clientRequestId = UUID.randomUUID(); // UUID | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = false; // Boolean | Whether the server should return the client-request-id in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    String ifMatch = "ifMatch_example"; // String | An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service exactly matches the value specified by the client.
    String ifNoneMatch = "ifNoneMatch_example"; // String | An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service does not match the value specified by the client.
    String ifModifiedSince = "ifModifiedSince_example"; // String | A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
    String ifUnmodifiedSince = "ifUnmodifiedSince_example"; // String | A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
    try {
      apiInstance.poolRemoveNodes(poolId, apiVersion, nodeRemoveParameter, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComputeNodesApi#poolRemoveNodes");
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
| **poolId** | **String**| The ID of the Pool from which you want to remove Compute Nodes. | |
| **apiVersion** | **String**| Client API Version. | |
| **nodeRemoveParameter** | [**NodeRemoveParameter**](NodeRemoveParameter.md)| The parameters for the request. | |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **UUID**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false] |
| **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] |
| **ifMatch** | **String**| An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service exactly matches the value specified by the client. | [optional] |
| **ifNoneMatch** | **String**| An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service does not match the value specified by the client. | [optional] |
| **ifModifiedSince** | **String**| A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time. | [optional] |
| **ifUnmodifiedSince** | **String**| A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time. | [optional] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json; odata=minimalmetadata
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The request to the Batch service was successful. |  * ETag - The ETag HTTP response header. This is an opaque string. You can use it to detect whether the resource has changed between requests. In particular, you can pass the ETag to one of the If-Modified-Since, If-Unmodified-Since, If-Match or If-None-Match headers. <br>  * client-request-id - The client-request-id provided by the client during the request. This will be returned only if the return-client-request-id parameter was set to true. <br>  * DataServiceId - The OData ID of the resource to which the request applied. <br>  * Last-Modified - The time at which the resource was last modified. <br>  * request-id - A unique identifier for the request that was made to the Batch service. If a request is consistently failing and you have verified that the request is properly formulated, you may use this value to report the error to Microsoft. In your report, include the value of this request ID, the approximate time that the request was made, the Batch Account against which the request was made, and the region that Account resides in. <br>  |
| **0** | The error from the Batch service. |  -  |

