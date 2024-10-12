# FaultsApi

All URIs are relative to *http://azure.local:19080*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelOperation**](FaultsApi.md#cancelOperation) | **POST** /Faults/$/Cancel | Cancels a user-induced fault operation. |
| [**getDataLossProgress**](FaultsApi.md#getDataLossProgress) | **GET** /Faults/Services/{serviceId}/$/GetPartitions/{partitionId}/$/GetDataLossProgress | Gets the progress of a partition data loss operation started using the StartDataLoss API. |
| [**getFaultOperationList**](FaultsApi.md#getFaultOperationList) | **GET** /Faults/ | Gets a list of user-induced fault operations filtered by provided input. |
| [**getNodeTransitionProgress**](FaultsApi.md#getNodeTransitionProgress) | **GET** /Faults/Nodes/{nodeName}/$/GetTransitionProgress | Gets the progress of an operation started using StartNodeTransition. |
| [**getPartitionRestartProgress**](FaultsApi.md#getPartitionRestartProgress) | **GET** /Faults/Services/{serviceId}/$/GetPartitions/{partitionId}/$/GetRestartProgress | Gets the progress of a PartitionRestart operation started using StartPartitionRestart. |
| [**getQuorumLossProgress**](FaultsApi.md#getQuorumLossProgress) | **GET** /Faults/Services/{serviceId}/$/GetPartitions/{partitionId}/$/GetQuorumLossProgress | Gets the progress of a quorum loss operation on a partition started using the StartQuorumLoss API. |
| [**startDataLoss**](FaultsApi.md#startDataLoss) | **POST** /Faults/Services/{serviceId}/$/GetPartitions/{partitionId}/$/StartDataLoss | This API will induce data loss for the specified partition. It will trigger a call to the OnDataLossAsync API of the partition. |
| [**startNodeTransition**](FaultsApi.md#startNodeTransition) | **POST** /Faults/Nodes/{nodeName}/$/StartTransition/ | Starts or stops a cluster node. |
| [**startPartitionRestart**](FaultsApi.md#startPartitionRestart) | **POST** /Faults/Services/{serviceId}/$/GetPartitions/{partitionId}/$/StartRestart | This API will restart some or all replicas or instances of the specified partition. |
| [**startQuorumLoss**](FaultsApi.md#startQuorumLoss) | **POST** /Faults/Services/{serviceId}/$/GetPartitions/{partitionId}/$/StartQuorumLoss | Induces quorum loss for a given stateful service partition. |


<a id="cancelOperation"></a>
# **cancelOperation**
> cancelOperation(apiVersion, operationId, force, timeout)

Cancels a user-induced fault operation.

The following is a list of APIs that start fault operations that may be cancelled using CancelOperation - - StartDataLoss - StartQuorumLoss - StartPartitionRestart - StartNodeTransition  If force is false, then the specified user-induced operation will be gracefully stopped and cleaned up.  If force is true, the command will be aborted, and some internal state may be left behind.  Specifying force as true should be used with care.  Calling this API with force set to true is not allowed until this API has already been called on the same test command with force set to false first, or unless the test command already has an OperationState of OperationState.RollingBack. Clarification: OperationState.RollingBack means that the system will/is be cleaning up internal system state caused by executing the command.  It will not restore data if the test command was to cause data loss.  For example, if you call StartDataLoss then call this API, the system will only clean up internal state from running the command. It will not restore the target partition&#39;s data, if the command progressed far enough to cause data loss.  Important note:  if this API is invoked with force&#x3D;&#x3D;true, internal state may be left behind.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FaultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    FaultsApi apiInstance = new FaultsApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    UUID operationId = UUID.randomUUID(); // UUID | A GUID that identifies a call of this API.  This is passed into the corresponding GetProgress API
    Boolean force = false; // Boolean | Indicates whether to gracefully rollback and clean up internal system state modified by executing the user-induced operation.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      apiInstance.cancelOperation(apiVersion, operationId, force, timeout);
    } catch (ApiException e) {
      System.err.println("Exception when calling FaultsApi#cancelOperation");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to 6.0] [enum: 6.0] |
| **operationId** | **UUID**| A GUID that identifies a call of this API.  This is passed into the corresponding GetProgress API | |
| **force** | **Boolean**| Indicates whether to gracefully rollback and clean up internal system state modified by executing the user-induced operation. | [default to false] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

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

<a id="getDataLossProgress"></a>
# **getDataLossProgress**
> PartitionDataLossProgress getDataLossProgress(apiVersion, serviceId, partitionId, operationId, timeout)

Gets the progress of a partition data loss operation started using the StartDataLoss API.

Gets the progress of a data loss operation started with StartDataLoss, using the OperationId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FaultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    FaultsApi apiInstance = new FaultsApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    String serviceId = "serviceId_example"; // String | The identity of the service. This is typically the full name of the service without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the service name is \"fabric:/myapp/app1/svc1\", the service identity would be \"myapp~app1~svc1\" in 6.0+ and \"myapp/app1/svc1\" in previous versions.
    UUID partitionId = UUID.randomUUID(); // UUID | The identity of the partition.
    UUID operationId = UUID.randomUUID(); // UUID | A GUID that identifies a call of this API.  This is passed into the corresponding GetProgress API
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      PartitionDataLossProgress result = apiInstance.getDataLossProgress(apiVersion, serviceId, partitionId, operationId, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FaultsApi#getDataLossProgress");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to 6.0] [enum: 6.0] |
| **serviceId** | **String**| The identity of the service. This is typically the full name of the service without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the service name is \&quot;fabric:/myapp/app1/svc1\&quot;, the service identity would be \&quot;myapp~app1~svc1\&quot; in 6.0+ and \&quot;myapp/app1/svc1\&quot; in previous versions. | |
| **partitionId** | **UUID**| The identity of the partition. | |
| **operationId** | **UUID**| A GUID that identifies a call of this API.  This is passed into the corresponding GetProgress API | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

[**PartitionDataLossProgress**](PartitionDataLossProgress.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Information about the progress of the partition data loss operation. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getFaultOperationList"></a>
# **getFaultOperationList**
> List&lt;OperationStatus&gt; getFaultOperationList(apiVersion, typeFilter, stateFilter, timeout)

Gets a list of user-induced fault operations filtered by provided input.

Gets the a list of user-induced fault operations filtered by provided input.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FaultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    FaultsApi apiInstance = new FaultsApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    Integer typeFilter = 65535; // Integer | Used to filter on OperationType for user-induced operations. 65535 - select all 1     - select PartitionDataLoss. 2     - select PartitionQuorumLoss. 4     - select PartitionRestart. 8     - select NodeTransition.
    Integer stateFilter = 65535; // Integer | Used to filter on OperationState's for user-induced operations. 65535 - select All 1     - select Running 2     - select RollingBack 8     - select Completed 16    - select Faulted 32    - select Cancelled 64    - select ForceCancelled
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      List<OperationStatus> result = apiInstance.getFaultOperationList(apiVersion, typeFilter, stateFilter, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FaultsApi#getFaultOperationList");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to 6.0] [enum: 6.0] |
| **typeFilter** | **Integer**| Used to filter on OperationType for user-induced operations. 65535 - select all 1     - select PartitionDataLoss. 2     - select PartitionQuorumLoss. 4     - select PartitionRestart. 8     - select NodeTransition. | [default to 65535] |
| **stateFilter** | **Integer**| Used to filter on OperationState&#39;s for user-induced operations. 65535 - select All 1     - select Running 2     - select RollingBack 8     - select Completed 16    - select Faulted 32    - select Cancelled 64    - select ForceCancelled | [default to 65535] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

[**List&lt;OperationStatus&gt;**](OperationStatus.md)

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

<a id="getNodeTransitionProgress"></a>
# **getNodeTransitionProgress**
> NodeTransitionProgress getNodeTransitionProgress(apiVersion, nodeName, operationId, timeout)

Gets the progress of an operation started using StartNodeTransition.

Gets the progress of an operation started with StartNodeTransition using the provided OperationId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FaultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    FaultsApi apiInstance = new FaultsApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    String nodeName = "nodeName_example"; // String | The name of the node.
    UUID operationId = UUID.randomUUID(); // UUID | A GUID that identifies a call of this API.  This is passed into the corresponding GetProgress API
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      NodeTransitionProgress result = apiInstance.getNodeTransitionProgress(apiVersion, nodeName, operationId, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FaultsApi#getNodeTransitionProgress");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to 6.0] [enum: 6.0] |
| **nodeName** | **String**| The name of the node. | |
| **operationId** | **UUID**| A GUID that identifies a call of this API.  This is passed into the corresponding GetProgress API | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

[**NodeTransitionProgress**](NodeTransitionProgress.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Information about the progress of a node transition operation. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getPartitionRestartProgress"></a>
# **getPartitionRestartProgress**
> PartitionRestartProgress getPartitionRestartProgress(apiVersion, serviceId, partitionId, operationId, timeout)

Gets the progress of a PartitionRestart operation started using StartPartitionRestart.

Gets the progress of a PartitionRestart started with StartPartitionRestart using the provided OperationId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FaultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    FaultsApi apiInstance = new FaultsApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    String serviceId = "serviceId_example"; // String | The identity of the service. This is typically the full name of the service without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the service name is \"fabric:/myapp/app1/svc1\", the service identity would be \"myapp~app1~svc1\" in 6.0+ and \"myapp/app1/svc1\" in previous versions.
    UUID partitionId = UUID.randomUUID(); // UUID | The identity of the partition.
    UUID operationId = UUID.randomUUID(); // UUID | A GUID that identifies a call of this API.  This is passed into the corresponding GetProgress API
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      PartitionRestartProgress result = apiInstance.getPartitionRestartProgress(apiVersion, serviceId, partitionId, operationId, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FaultsApi#getPartitionRestartProgress");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to 6.0] [enum: 6.0] |
| **serviceId** | **String**| The identity of the service. This is typically the full name of the service without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the service name is \&quot;fabric:/myapp/app1/svc1\&quot;, the service identity would be \&quot;myapp~app1~svc1\&quot; in 6.0+ and \&quot;myapp/app1/svc1\&quot; in previous versions. | |
| **partitionId** | **UUID**| The identity of the partition. | |
| **operationId** | **UUID**| A GUID that identifies a call of this API.  This is passed into the corresponding GetProgress API | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

[**PartitionRestartProgress**](PartitionRestartProgress.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Information about the progress of a partition restart operation. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getQuorumLossProgress"></a>
# **getQuorumLossProgress**
> PartitionQuorumLossProgress getQuorumLossProgress(apiVersion, serviceId, partitionId, operationId, timeout)

Gets the progress of a quorum loss operation on a partition started using the StartQuorumLoss API.

Gets the progress of a quorum loss operation started with StartQuorumLoss, using the provided OperationId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FaultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    FaultsApi apiInstance = new FaultsApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    String serviceId = "serviceId_example"; // String | The identity of the service. This is typically the full name of the service without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the service name is \"fabric:/myapp/app1/svc1\", the service identity would be \"myapp~app1~svc1\" in 6.0+ and \"myapp/app1/svc1\" in previous versions.
    UUID partitionId = UUID.randomUUID(); // UUID | The identity of the partition.
    UUID operationId = UUID.randomUUID(); // UUID | A GUID that identifies a call of this API.  This is passed into the corresponding GetProgress API
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      PartitionQuorumLossProgress result = apiInstance.getQuorumLossProgress(apiVersion, serviceId, partitionId, operationId, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FaultsApi#getQuorumLossProgress");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to 6.0] [enum: 6.0] |
| **serviceId** | **String**| The identity of the service. This is typically the full name of the service without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the service name is \&quot;fabric:/myapp/app1/svc1\&quot;, the service identity would be \&quot;myapp~app1~svc1\&quot; in 6.0+ and \&quot;myapp/app1/svc1\&quot; in previous versions. | |
| **partitionId** | **UUID**| The identity of the partition. | |
| **operationId** | **UUID**| A GUID that identifies a call of this API.  This is passed into the corresponding GetProgress API | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

[**PartitionQuorumLossProgress**](PartitionQuorumLossProgress.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Information about the progress of a partition quorum loss operation. |  -  |
| **0** | The detailed error response. |  -  |

<a id="startDataLoss"></a>
# **startDataLoss**
> startDataLoss(apiVersion, serviceId, partitionId, operationId, dataLossMode, timeout)

This API will induce data loss for the specified partition. It will trigger a call to the OnDataLossAsync API of the partition.

This API will induce data loss for the specified partition. It will trigger a call to the OnDataLoss API of the partition. Actual data loss will depend on the specified DataLossMode PartialDataLoss - Only a quorum of replicas are removed and OnDataLoss is triggered for the partition but actual data loss depends on the presence of in-flight replication. FullDataLoss - All replicas are removed hence all data is lost and OnDataLoss is triggered.  This API should only be called with a stateful service as the target.  Calling this API with a system service as the target is not advised.  Note:  Once this API has been called, it cannot be reversed. Calling CancelOperation will only stop execution and clean up internal system state. It will not restore data if the command has progressed far enough to cause data loss.  Call the GetDataLossProgress API with the same OperationId to return information on the operation started with this API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FaultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    FaultsApi apiInstance = new FaultsApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    String serviceId = "serviceId_example"; // String | The identity of the service. This is typically the full name of the service without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the service name is \"fabric:/myapp/app1/svc1\", the service identity would be \"myapp~app1~svc1\" in 6.0+ and \"myapp/app1/svc1\" in previous versions.
    UUID partitionId = UUID.randomUUID(); // UUID | The identity of the partition.
    UUID operationId = UUID.randomUUID(); // UUID | A GUID that identifies a call of this API.  This is passed into the corresponding GetProgress API
    String dataLossMode = "Invalid"; // String | This enum is passed to the StartDataLoss API to indicate what type of data loss to induce.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      apiInstance.startDataLoss(apiVersion, serviceId, partitionId, operationId, dataLossMode, timeout);
    } catch (ApiException e) {
      System.err.println("Exception when calling FaultsApi#startDataLoss");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to 6.0] [enum: 6.0] |
| **serviceId** | **String**| The identity of the service. This is typically the full name of the service without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the service name is \&quot;fabric:/myapp/app1/svc1\&quot;, the service identity would be \&quot;myapp~app1~svc1\&quot; in 6.0+ and \&quot;myapp/app1/svc1\&quot; in previous versions. | |
| **partitionId** | **UUID**| The identity of the partition. | |
| **operationId** | **UUID**| A GUID that identifies a call of this API.  This is passed into the corresponding GetProgress API | |
| **dataLossMode** | **String**| This enum is passed to the StartDataLoss API to indicate what type of data loss to induce. | [enum: Invalid, PartialDataLoss, FullDataLoss] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

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
| **202** | A 202 status code indicates the operation was accepted.  Call the GetDataLossProgress API to get the progress. |  -  |
| **0** | The detailed error response. |  -  |

<a id="startNodeTransition"></a>
# **startNodeTransition**
> startNodeTransition(apiVersion, nodeName, operationId, nodeTransitionType, nodeInstanceId, stopDurationInSeconds, timeout)

Starts or stops a cluster node.

Starts or stops a cluster node.  A cluster node is a process, not the OS instance itself.  To start a node, pass in \&quot;Start\&quot; for the NodeTransitionType parameter. To stop a node, pass in \&quot;Stop\&quot; for the NodeTransitionType parameter.  This API starts the operation - when the API returns the node may not have finished transitioning yet. Call GetNodeTransitionProgress with the same OperationId to get the progress of the operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FaultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    FaultsApi apiInstance = new FaultsApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    String nodeName = "nodeName_example"; // String | The name of the node.
    UUID operationId = UUID.randomUUID(); // UUID | A GUID that identifies a call of this API.  This is passed into the corresponding GetProgress API
    String nodeTransitionType = "Invalid"; // String | Indicates the type of transition to perform.  NodeTransitionType.Start will start a stopped node.  NodeTransitionType.Stop will stop a node that is up.
    String nodeInstanceId = "nodeInstanceId_example"; // String | The node instance ID of the target node.  This can be determined through GetNodeInfo API.
    Integer stopDurationInSeconds = 56; // Integer | The duration, in seconds, to keep the node stopped.  The minimum value is 600, the maximum is 14400.  After this time expires, the node will automatically come back up.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      apiInstance.startNodeTransition(apiVersion, nodeName, operationId, nodeTransitionType, nodeInstanceId, stopDurationInSeconds, timeout);
    } catch (ApiException e) {
      System.err.println("Exception when calling FaultsApi#startNodeTransition");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to 6.0] [enum: 6.0] |
| **nodeName** | **String**| The name of the node. | |
| **operationId** | **UUID**| A GUID that identifies a call of this API.  This is passed into the corresponding GetProgress API | |
| **nodeTransitionType** | **String**| Indicates the type of transition to perform.  NodeTransitionType.Start will start a stopped node.  NodeTransitionType.Stop will stop a node that is up. | [enum: Invalid, Start, Stop] |
| **nodeInstanceId** | **String**| The node instance ID of the target node.  This can be determined through GetNodeInfo API. | |
| **stopDurationInSeconds** | **Integer**| The duration, in seconds, to keep the node stopped.  The minimum value is 600, the maximum is 14400.  After this time expires, the node will automatically come back up. | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

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
| **202** | A 202 status code indicates the operation was accepted.  Call the GetNodeTransitionProgress API to get the progress. |  -  |
| **0** | The detailed error response. |  -  |

<a id="startPartitionRestart"></a>
# **startPartitionRestart**
> startPartitionRestart(apiVersion, serviceId, partitionId, operationId, restartPartitionMode, timeout)

This API will restart some or all replicas or instances of the specified partition.

This API is useful for testing failover.  If used to target a stateless service partition, RestartPartitionMode must be AllReplicasOrInstances.  Call the GetPartitionRestartProgress API using the same OperationId to get the progress.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FaultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    FaultsApi apiInstance = new FaultsApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    String serviceId = "serviceId_example"; // String | The identity of the service. This is typically the full name of the service without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the service name is \"fabric:/myapp/app1/svc1\", the service identity would be \"myapp~app1~svc1\" in 6.0+ and \"myapp/app1/svc1\" in previous versions.
    UUID partitionId = UUID.randomUUID(); // UUID | The identity of the partition.
    UUID operationId = UUID.randomUUID(); // UUID | A GUID that identifies a call of this API.  This is passed into the corresponding GetProgress API
    String restartPartitionMode = "Invalid"; // String | Describe which partitions to restart.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      apiInstance.startPartitionRestart(apiVersion, serviceId, partitionId, operationId, restartPartitionMode, timeout);
    } catch (ApiException e) {
      System.err.println("Exception when calling FaultsApi#startPartitionRestart");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to 6.0] [enum: 6.0] |
| **serviceId** | **String**| The identity of the service. This is typically the full name of the service without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the service name is \&quot;fabric:/myapp/app1/svc1\&quot;, the service identity would be \&quot;myapp~app1~svc1\&quot; in 6.0+ and \&quot;myapp/app1/svc1\&quot; in previous versions. | |
| **partitionId** | **UUID**| The identity of the partition. | |
| **operationId** | **UUID**| A GUID that identifies a call of this API.  This is passed into the corresponding GetProgress API | |
| **restartPartitionMode** | **String**| Describe which partitions to restart. | [enum: Invalid, AllReplicasOrInstances, OnlyActiveSecondaries] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

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
| **202** | A 202 status code indicates the operation was accepted.  Call the GetPartitionRestartProgress API to get the progress. |  -  |
| **0** | The detailed error response. |  -  |

<a id="startQuorumLoss"></a>
# **startQuorumLoss**
> startQuorumLoss(apiVersion, serviceId, partitionId, operationId, quorumLossMode, quorumLossDuration, timeout)

Induces quorum loss for a given stateful service partition.

Induces quorum loss for a given stateful service partition.  This API is useful for a temporary quorum loss situation on your service.  Call the GetQuorumLossProgress API with the same OperationId to return information on the operation started with this API.  This can only be called on stateful persisted (HasPersistedState&#x3D;&#x3D;true) services.  Do not use this API on stateless services or stateful in-memory only services.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FaultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    FaultsApi apiInstance = new FaultsApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    String serviceId = "serviceId_example"; // String | The identity of the service. This is typically the full name of the service without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the service name is \"fabric:/myapp/app1/svc1\", the service identity would be \"myapp~app1~svc1\" in 6.0+ and \"myapp/app1/svc1\" in previous versions.
    UUID partitionId = UUID.randomUUID(); // UUID | The identity of the partition.
    UUID operationId = UUID.randomUUID(); // UUID | A GUID that identifies a call of this API.  This is passed into the corresponding GetProgress API
    String quorumLossMode = "Invalid"; // String | This enum is passed to the StartQuorumLoss API to indicate what type of quorum loss to induce.
    Integer quorumLossDuration = 56; // Integer | The amount of time for which the partition will be kept in quorum loss.  This must be specified in seconds.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      apiInstance.startQuorumLoss(apiVersion, serviceId, partitionId, operationId, quorumLossMode, quorumLossDuration, timeout);
    } catch (ApiException e) {
      System.err.println("Exception when calling FaultsApi#startQuorumLoss");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to 6.0] [enum: 6.0] |
| **serviceId** | **String**| The identity of the service. This is typically the full name of the service without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the service name is \&quot;fabric:/myapp/app1/svc1\&quot;, the service identity would be \&quot;myapp~app1~svc1\&quot; in 6.0+ and \&quot;myapp/app1/svc1\&quot; in previous versions. | |
| **partitionId** | **UUID**| The identity of the partition. | |
| **operationId** | **UUID**| A GUID that identifies a call of this API.  This is passed into the corresponding GetProgress API | |
| **quorumLossMode** | **String**| This enum is passed to the StartQuorumLoss API to indicate what type of quorum loss to induce. | [enum: Invalid, QuorumReplicas, AllReplicas] |
| **quorumLossDuration** | **Integer**| The amount of time for which the partition will be kept in quorum loss.  This must be specified in seconds. | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

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
| **202** | A 202 status code indicates the operation was accepted.  Call the GetQuorumLossProgress API to get the progress. |  -  |
| **0** | The detailed error response. |  -  |

