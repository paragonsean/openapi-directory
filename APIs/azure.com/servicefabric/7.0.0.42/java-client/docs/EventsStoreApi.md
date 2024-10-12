# EventsStoreApi

All URIs are relative to *http://azure.local:19080*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getApplicationEventList**](EventsStoreApi.md#getApplicationEventList) | **GET** /EventsStore/Applications/{applicationId}/$/Events | Gets an Application-related events. |
| [**getApplicationsEventList**](EventsStoreApi.md#getApplicationsEventList) | **GET** /EventsStore/Applications/Events | Gets all Applications-related events. |
| [**getClusterEventList**](EventsStoreApi.md#getClusterEventList) | **GET** /EventsStore/Cluster/Events | Gets all Cluster-related events. |
| [**getContainersEventList**](EventsStoreApi.md#getContainersEventList) | **GET** /EventsStore/Containers/Events | Gets all Containers-related events. |
| [**getCorrelatedEventList**](EventsStoreApi.md#getCorrelatedEventList) | **GET** /EventsStore/CorrelatedEvents/{eventInstanceId}/$/Events | Gets all correlated events for a given event. |
| [**getNodeEventList**](EventsStoreApi.md#getNodeEventList) | **GET** /EventsStore/Nodes/{nodeName}/$/Events | Gets a Node-related events. |
| [**getNodesEventList**](EventsStoreApi.md#getNodesEventList) | **GET** /EventsStore/Nodes/Events | Gets all Nodes-related Events. |
| [**getPartitionEventList**](EventsStoreApi.md#getPartitionEventList) | **GET** /EventsStore/Partitions/{partitionId}/$/Events | Gets a Partition-related events. |
| [**getPartitionReplicaEventList**](EventsStoreApi.md#getPartitionReplicaEventList) | **GET** /EventsStore/Partitions/{partitionId}/$/Replicas/{replicaId}/$/Events | Gets a Partition Replica-related events. |
| [**getPartitionReplicasEventList**](EventsStoreApi.md#getPartitionReplicasEventList) | **GET** /EventsStore/Partitions/{partitionId}/$/Replicas/Events | Gets all Replicas-related events for a Partition. |
| [**getPartitionsEventList**](EventsStoreApi.md#getPartitionsEventList) | **GET** /EventsStore/Partitions/Events | Gets all Partitions-related events. |
| [**getServiceEventList**](EventsStoreApi.md#getServiceEventList) | **GET** /EventsStore/Services/{serviceId}/$/Events | Gets a Service-related events. |
| [**getServicesEventList**](EventsStoreApi.md#getServicesEventList) | **GET** /EventsStore/Services/Events | Gets all Services-related events. |


<a id="getApplicationEventList"></a>
# **getApplicationEventList**
> List&lt;ApplicationEvent&gt; getApplicationEventList(apiVersion, applicationId, startTimeUtc, endTimeUtc, timeout, eventsTypesFilter, excludeAnalysisEvents, skipCorrelationLookup)

Gets an Application-related events.

The response is list of ApplicationEvent objects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsStoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    EventsStoreApi apiInstance = new EventsStoreApi(defaultClient);
    String apiVersion = "6.4"; // String | The version of the API. This parameter is required and its value must be '6.4'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    String applicationId = "applicationId_example"; // String | The identity of the application. This is typically the full name of the application without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the application name is \"fabric:/myapp/app1\", the application identity would be \"myapp~app1\" in 6.0+ and \"myapp/app1\" in previous versions.
    String startTimeUtc = "startTimeUtc_example"; // String | The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    String endTimeUtc = "endTimeUtc_example"; // String | The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    String eventsTypesFilter = "eventsTypesFilter_example"; // String | This is a comma separated string specifying the types of FabricEvents that should only be included in the response.
    Boolean excludeAnalysisEvents = true; // Boolean | This param disables the retrieval of AnalysisEvents if true is passed.
    Boolean skipCorrelationLookup = true; // Boolean | This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated.
    try {
      List<ApplicationEvent> result = apiInstance.getApplicationEventList(apiVersion, applicationId, startTimeUtc, endTimeUtc, timeout, eventsTypesFilter, excludeAnalysisEvents, skipCorrelationLookup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsStoreApi#getApplicationEventList");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to 6.4] [enum: 6.4] |
| **applicationId** | **String**| The identity of the application. This is typically the full name of the application without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the application name is \&quot;fabric:/myapp/app1\&quot;, the application identity would be \&quot;myapp~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions. | |
| **startTimeUtc** | **String**| The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | |
| **endTimeUtc** | **String**| The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |
| **eventsTypesFilter** | **String**| This is a comma separated string specifying the types of FabricEvents that should only be included in the response. | [optional] |
| **excludeAnalysisEvents** | **Boolean**| This param disables the retrieval of AnalysisEvents if true is passed. | [optional] |
| **skipCorrelationLookup** | **Boolean**| This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated. | [optional] |

### Return type

[**List&lt;ApplicationEvent&gt;**](ApplicationEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of events objects with base type ApplicationEvent. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getApplicationsEventList"></a>
# **getApplicationsEventList**
> List&lt;ApplicationEvent&gt; getApplicationsEventList(apiVersion, startTimeUtc, endTimeUtc, timeout, eventsTypesFilter, excludeAnalysisEvents, skipCorrelationLookup)

Gets all Applications-related events.

The response is list of ApplicationEvent objects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsStoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    EventsStoreApi apiInstance = new EventsStoreApi(defaultClient);
    String apiVersion = "6.4"; // String | The version of the API. This parameter is required and its value must be '6.4'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    String startTimeUtc = "startTimeUtc_example"; // String | The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    String endTimeUtc = "endTimeUtc_example"; // String | The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    String eventsTypesFilter = "eventsTypesFilter_example"; // String | This is a comma separated string specifying the types of FabricEvents that should only be included in the response.
    Boolean excludeAnalysisEvents = true; // Boolean | This param disables the retrieval of AnalysisEvents if true is passed.
    Boolean skipCorrelationLookup = true; // Boolean | This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated.
    try {
      List<ApplicationEvent> result = apiInstance.getApplicationsEventList(apiVersion, startTimeUtc, endTimeUtc, timeout, eventsTypesFilter, excludeAnalysisEvents, skipCorrelationLookup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsStoreApi#getApplicationsEventList");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to 6.4] [enum: 6.4] |
| **startTimeUtc** | **String**| The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | |
| **endTimeUtc** | **String**| The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |
| **eventsTypesFilter** | **String**| This is a comma separated string specifying the types of FabricEvents that should only be included in the response. | [optional] |
| **excludeAnalysisEvents** | **Boolean**| This param disables the retrieval of AnalysisEvents if true is passed. | [optional] |
| **skipCorrelationLookup** | **Boolean**| This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated. | [optional] |

### Return type

[**List&lt;ApplicationEvent&gt;**](ApplicationEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of events objects with base type ApplicationEvent. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getClusterEventList"></a>
# **getClusterEventList**
> List&lt;ClusterEvent&gt; getClusterEventList(apiVersion, startTimeUtc, endTimeUtc, timeout, eventsTypesFilter, excludeAnalysisEvents, skipCorrelationLookup)

Gets all Cluster-related events.

The response is list of ClusterEvent objects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsStoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    EventsStoreApi apiInstance = new EventsStoreApi(defaultClient);
    String apiVersion = "6.4"; // String | The version of the API. This parameter is required and its value must be '6.4'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    String startTimeUtc = "startTimeUtc_example"; // String | The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    String endTimeUtc = "endTimeUtc_example"; // String | The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    String eventsTypesFilter = "eventsTypesFilter_example"; // String | This is a comma separated string specifying the types of FabricEvents that should only be included in the response.
    Boolean excludeAnalysisEvents = true; // Boolean | This param disables the retrieval of AnalysisEvents if true is passed.
    Boolean skipCorrelationLookup = true; // Boolean | This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated.
    try {
      List<ClusterEvent> result = apiInstance.getClusterEventList(apiVersion, startTimeUtc, endTimeUtc, timeout, eventsTypesFilter, excludeAnalysisEvents, skipCorrelationLookup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsStoreApi#getClusterEventList");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to 6.4] [enum: 6.4] |
| **startTimeUtc** | **String**| The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | |
| **endTimeUtc** | **String**| The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |
| **eventsTypesFilter** | **String**| This is a comma separated string specifying the types of FabricEvents that should only be included in the response. | [optional] |
| **excludeAnalysisEvents** | **Boolean**| This param disables the retrieval of AnalysisEvents if true is passed. | [optional] |
| **skipCorrelationLookup** | **Boolean**| This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated. | [optional] |

### Return type

[**List&lt;ClusterEvent&gt;**](ClusterEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of events objects with base type ClusterEvent. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getContainersEventList"></a>
# **getContainersEventList**
> List&lt;ContainerInstanceEvent&gt; getContainersEventList(apiVersion, startTimeUtc, endTimeUtc, timeout, eventsTypesFilter, excludeAnalysisEvents, skipCorrelationLookup)

Gets all Containers-related events.

The response is list of ContainerInstanceEvent objects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsStoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    EventsStoreApi apiInstance = new EventsStoreApi(defaultClient);
    String apiVersion = "6.2-preview"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
    String startTimeUtc = "startTimeUtc_example"; // String | The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    String endTimeUtc = "endTimeUtc_example"; // String | The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    String eventsTypesFilter = "eventsTypesFilter_example"; // String | This is a comma separated string specifying the types of FabricEvents that should only be included in the response.
    Boolean excludeAnalysisEvents = true; // Boolean | This param disables the retrieval of AnalysisEvents if true is passed.
    Boolean skipCorrelationLookup = true; // Boolean | This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated.
    try {
      List<ContainerInstanceEvent> result = apiInstance.getContainersEventList(apiVersion, startTimeUtc, endTimeUtc, timeout, eventsTypesFilter, excludeAnalysisEvents, skipCorrelationLookup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsStoreApi#getContainersEventList");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to 6.2-preview] [enum: 6.2-preview] |
| **startTimeUtc** | **String**| The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | |
| **endTimeUtc** | **String**| The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |
| **eventsTypesFilter** | **String**| This is a comma separated string specifying the types of FabricEvents that should only be included in the response. | [optional] |
| **excludeAnalysisEvents** | **Boolean**| This param disables the retrieval of AnalysisEvents if true is passed. | [optional] |
| **skipCorrelationLookup** | **Boolean**| This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated. | [optional] |

### Return type

[**List&lt;ContainerInstanceEvent&gt;**](ContainerInstanceEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of events objects with base type ContainerInstanceEvent. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getCorrelatedEventList"></a>
# **getCorrelatedEventList**
> List&lt;FabricEvent&gt; getCorrelatedEventList(apiVersion, eventInstanceId, timeout)

Gets all correlated events for a given event.

The response is list of FabricEvents.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsStoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    EventsStoreApi apiInstance = new EventsStoreApi(defaultClient);
    String apiVersion = "6.4"; // String | The version of the API. This parameter is required and its value must be '6.4'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    String eventInstanceId = "eventInstanceId_example"; // String | The EventInstanceId.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      List<FabricEvent> result = apiInstance.getCorrelatedEventList(apiVersion, eventInstanceId, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsStoreApi#getCorrelatedEventList");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to 6.4] [enum: 6.4] |
| **eventInstanceId** | **String**| The EventInstanceId. | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

[**List&lt;FabricEvent&gt;**](FabricEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of events objects with base type FabricEvent. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getNodeEventList"></a>
# **getNodeEventList**
> List&lt;NodeEvent&gt; getNodeEventList(apiVersion, nodeName, startTimeUtc, endTimeUtc, timeout, eventsTypesFilter, excludeAnalysisEvents, skipCorrelationLookup)

Gets a Node-related events.

The response is list of NodeEvent objects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsStoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    EventsStoreApi apiInstance = new EventsStoreApi(defaultClient);
    String apiVersion = "6.4"; // String | The version of the API. This parameter is required and its value must be '6.4'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    String nodeName = "nodeName_example"; // String | The name of the node.
    String startTimeUtc = "startTimeUtc_example"; // String | The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    String endTimeUtc = "endTimeUtc_example"; // String | The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    String eventsTypesFilter = "eventsTypesFilter_example"; // String | This is a comma separated string specifying the types of FabricEvents that should only be included in the response.
    Boolean excludeAnalysisEvents = true; // Boolean | This param disables the retrieval of AnalysisEvents if true is passed.
    Boolean skipCorrelationLookup = true; // Boolean | This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated.
    try {
      List<NodeEvent> result = apiInstance.getNodeEventList(apiVersion, nodeName, startTimeUtc, endTimeUtc, timeout, eventsTypesFilter, excludeAnalysisEvents, skipCorrelationLookup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsStoreApi#getNodeEventList");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to 6.4] [enum: 6.4] |
| **nodeName** | **String**| The name of the node. | |
| **startTimeUtc** | **String**| The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | |
| **endTimeUtc** | **String**| The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |
| **eventsTypesFilter** | **String**| This is a comma separated string specifying the types of FabricEvents that should only be included in the response. | [optional] |
| **excludeAnalysisEvents** | **Boolean**| This param disables the retrieval of AnalysisEvents if true is passed. | [optional] |
| **skipCorrelationLookup** | **Boolean**| This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated. | [optional] |

### Return type

[**List&lt;NodeEvent&gt;**](NodeEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of events objects with base type NodeEvent. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getNodesEventList"></a>
# **getNodesEventList**
> List&lt;NodeEvent&gt; getNodesEventList(apiVersion, startTimeUtc, endTimeUtc, timeout, eventsTypesFilter, excludeAnalysisEvents, skipCorrelationLookup)

Gets all Nodes-related Events.

The response is list of NodeEvent objects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsStoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    EventsStoreApi apiInstance = new EventsStoreApi(defaultClient);
    String apiVersion = "6.4"; // String | The version of the API. This parameter is required and its value must be '6.4'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    String startTimeUtc = "startTimeUtc_example"; // String | The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    String endTimeUtc = "endTimeUtc_example"; // String | The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    String eventsTypesFilter = "eventsTypesFilter_example"; // String | This is a comma separated string specifying the types of FabricEvents that should only be included in the response.
    Boolean excludeAnalysisEvents = true; // Boolean | This param disables the retrieval of AnalysisEvents if true is passed.
    Boolean skipCorrelationLookup = true; // Boolean | This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated.
    try {
      List<NodeEvent> result = apiInstance.getNodesEventList(apiVersion, startTimeUtc, endTimeUtc, timeout, eventsTypesFilter, excludeAnalysisEvents, skipCorrelationLookup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsStoreApi#getNodesEventList");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to 6.4] [enum: 6.4] |
| **startTimeUtc** | **String**| The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | |
| **endTimeUtc** | **String**| The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |
| **eventsTypesFilter** | **String**| This is a comma separated string specifying the types of FabricEvents that should only be included in the response. | [optional] |
| **excludeAnalysisEvents** | **Boolean**| This param disables the retrieval of AnalysisEvents if true is passed. | [optional] |
| **skipCorrelationLookup** | **Boolean**| This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated. | [optional] |

### Return type

[**List&lt;NodeEvent&gt;**](NodeEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of events objects with base type NodeEvent. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getPartitionEventList"></a>
# **getPartitionEventList**
> List&lt;PartitionEvent&gt; getPartitionEventList(apiVersion, partitionId, startTimeUtc, endTimeUtc, timeout, eventsTypesFilter, excludeAnalysisEvents, skipCorrelationLookup)

Gets a Partition-related events.

The response is list of PartitionEvent objects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsStoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    EventsStoreApi apiInstance = new EventsStoreApi(defaultClient);
    String apiVersion = "6.4"; // String | The version of the API. This parameter is required and its value must be '6.4'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    UUID partitionId = UUID.randomUUID(); // UUID | The identity of the partition.
    String startTimeUtc = "startTimeUtc_example"; // String | The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    String endTimeUtc = "endTimeUtc_example"; // String | The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    String eventsTypesFilter = "eventsTypesFilter_example"; // String | This is a comma separated string specifying the types of FabricEvents that should only be included in the response.
    Boolean excludeAnalysisEvents = true; // Boolean | This param disables the retrieval of AnalysisEvents if true is passed.
    Boolean skipCorrelationLookup = true; // Boolean | This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated.
    try {
      List<PartitionEvent> result = apiInstance.getPartitionEventList(apiVersion, partitionId, startTimeUtc, endTimeUtc, timeout, eventsTypesFilter, excludeAnalysisEvents, skipCorrelationLookup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsStoreApi#getPartitionEventList");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to 6.4] [enum: 6.4] |
| **partitionId** | **UUID**| The identity of the partition. | |
| **startTimeUtc** | **String**| The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | |
| **endTimeUtc** | **String**| The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |
| **eventsTypesFilter** | **String**| This is a comma separated string specifying the types of FabricEvents that should only be included in the response. | [optional] |
| **excludeAnalysisEvents** | **Boolean**| This param disables the retrieval of AnalysisEvents if true is passed. | [optional] |
| **skipCorrelationLookup** | **Boolean**| This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated. | [optional] |

### Return type

[**List&lt;PartitionEvent&gt;**](PartitionEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of events objects with base type PartitionEvent. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getPartitionReplicaEventList"></a>
# **getPartitionReplicaEventList**
> List&lt;ReplicaEvent&gt; getPartitionReplicaEventList(apiVersion, partitionId, replicaId, startTimeUtc, endTimeUtc, timeout, eventsTypesFilter, excludeAnalysisEvents, skipCorrelationLookup)

Gets a Partition Replica-related events.

The response is list of ReplicaEvent objects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsStoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    EventsStoreApi apiInstance = new EventsStoreApi(defaultClient);
    String apiVersion = "6.4"; // String | The version of the API. This parameter is required and its value must be '6.4'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    UUID partitionId = UUID.randomUUID(); // UUID | The identity of the partition.
    String replicaId = "replicaId_example"; // String | The identifier of the replica.
    String startTimeUtc = "startTimeUtc_example"; // String | The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    String endTimeUtc = "endTimeUtc_example"; // String | The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    String eventsTypesFilter = "eventsTypesFilter_example"; // String | This is a comma separated string specifying the types of FabricEvents that should only be included in the response.
    Boolean excludeAnalysisEvents = true; // Boolean | This param disables the retrieval of AnalysisEvents if true is passed.
    Boolean skipCorrelationLookup = true; // Boolean | This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated.
    try {
      List<ReplicaEvent> result = apiInstance.getPartitionReplicaEventList(apiVersion, partitionId, replicaId, startTimeUtc, endTimeUtc, timeout, eventsTypesFilter, excludeAnalysisEvents, skipCorrelationLookup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsStoreApi#getPartitionReplicaEventList");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to 6.4] [enum: 6.4] |
| **partitionId** | **UUID**| The identity of the partition. | |
| **replicaId** | **String**| The identifier of the replica. | |
| **startTimeUtc** | **String**| The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | |
| **endTimeUtc** | **String**| The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |
| **eventsTypesFilter** | **String**| This is a comma separated string specifying the types of FabricEvents that should only be included in the response. | [optional] |
| **excludeAnalysisEvents** | **Boolean**| This param disables the retrieval of AnalysisEvents if true is passed. | [optional] |
| **skipCorrelationLookup** | **Boolean**| This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated. | [optional] |

### Return type

[**List&lt;ReplicaEvent&gt;**](ReplicaEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of events objects with base type ReplicaEvent. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getPartitionReplicasEventList"></a>
# **getPartitionReplicasEventList**
> List&lt;ReplicaEvent&gt; getPartitionReplicasEventList(apiVersion, partitionId, startTimeUtc, endTimeUtc, timeout, eventsTypesFilter, excludeAnalysisEvents, skipCorrelationLookup)

Gets all Replicas-related events for a Partition.

The response is list of ReplicaEvent objects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsStoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    EventsStoreApi apiInstance = new EventsStoreApi(defaultClient);
    String apiVersion = "6.4"; // String | The version of the API. This parameter is required and its value must be '6.4'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    UUID partitionId = UUID.randomUUID(); // UUID | The identity of the partition.
    String startTimeUtc = "startTimeUtc_example"; // String | The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    String endTimeUtc = "endTimeUtc_example"; // String | The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    String eventsTypesFilter = "eventsTypesFilter_example"; // String | This is a comma separated string specifying the types of FabricEvents that should only be included in the response.
    Boolean excludeAnalysisEvents = true; // Boolean | This param disables the retrieval of AnalysisEvents if true is passed.
    Boolean skipCorrelationLookup = true; // Boolean | This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated.
    try {
      List<ReplicaEvent> result = apiInstance.getPartitionReplicasEventList(apiVersion, partitionId, startTimeUtc, endTimeUtc, timeout, eventsTypesFilter, excludeAnalysisEvents, skipCorrelationLookup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsStoreApi#getPartitionReplicasEventList");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to 6.4] [enum: 6.4] |
| **partitionId** | **UUID**| The identity of the partition. | |
| **startTimeUtc** | **String**| The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | |
| **endTimeUtc** | **String**| The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |
| **eventsTypesFilter** | **String**| This is a comma separated string specifying the types of FabricEvents that should only be included in the response. | [optional] |
| **excludeAnalysisEvents** | **Boolean**| This param disables the retrieval of AnalysisEvents if true is passed. | [optional] |
| **skipCorrelationLookup** | **Boolean**| This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated. | [optional] |

### Return type

[**List&lt;ReplicaEvent&gt;**](ReplicaEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of events objects with base type ReplicaEvent. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getPartitionsEventList"></a>
# **getPartitionsEventList**
> List&lt;PartitionEvent&gt; getPartitionsEventList(apiVersion, startTimeUtc, endTimeUtc, timeout, eventsTypesFilter, excludeAnalysisEvents, skipCorrelationLookup)

Gets all Partitions-related events.

The response is list of PartitionEvent objects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsStoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    EventsStoreApi apiInstance = new EventsStoreApi(defaultClient);
    String apiVersion = "6.4"; // String | The version of the API. This parameter is required and its value must be '6.4'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    String startTimeUtc = "startTimeUtc_example"; // String | The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    String endTimeUtc = "endTimeUtc_example"; // String | The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    String eventsTypesFilter = "eventsTypesFilter_example"; // String | This is a comma separated string specifying the types of FabricEvents that should only be included in the response.
    Boolean excludeAnalysisEvents = true; // Boolean | This param disables the retrieval of AnalysisEvents if true is passed.
    Boolean skipCorrelationLookup = true; // Boolean | This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated.
    try {
      List<PartitionEvent> result = apiInstance.getPartitionsEventList(apiVersion, startTimeUtc, endTimeUtc, timeout, eventsTypesFilter, excludeAnalysisEvents, skipCorrelationLookup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsStoreApi#getPartitionsEventList");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to 6.4] [enum: 6.4] |
| **startTimeUtc** | **String**| The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | |
| **endTimeUtc** | **String**| The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |
| **eventsTypesFilter** | **String**| This is a comma separated string specifying the types of FabricEvents that should only be included in the response. | [optional] |
| **excludeAnalysisEvents** | **Boolean**| This param disables the retrieval of AnalysisEvents if true is passed. | [optional] |
| **skipCorrelationLookup** | **Boolean**| This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated. | [optional] |

### Return type

[**List&lt;PartitionEvent&gt;**](PartitionEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of events objects with base type PartitionEvent. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getServiceEventList"></a>
# **getServiceEventList**
> List&lt;ServiceEvent&gt; getServiceEventList(apiVersion, serviceId, startTimeUtc, endTimeUtc, timeout, eventsTypesFilter, excludeAnalysisEvents, skipCorrelationLookup)

Gets a Service-related events.

The response is list of ServiceEvent objects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsStoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    EventsStoreApi apiInstance = new EventsStoreApi(defaultClient);
    String apiVersion = "6.4"; // String | The version of the API. This parameter is required and its value must be '6.4'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    String serviceId = "serviceId_example"; // String | The identity of the service. This ID is typically the full name of the service without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the service name is \"fabric:/myapp/app1/svc1\", the service identity would be \"myapp~app1~svc1\" in 6.0+ and \"myapp/app1/svc1\" in previous versions.
    String startTimeUtc = "startTimeUtc_example"; // String | The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    String endTimeUtc = "endTimeUtc_example"; // String | The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    String eventsTypesFilter = "eventsTypesFilter_example"; // String | This is a comma separated string specifying the types of FabricEvents that should only be included in the response.
    Boolean excludeAnalysisEvents = true; // Boolean | This param disables the retrieval of AnalysisEvents if true is passed.
    Boolean skipCorrelationLookup = true; // Boolean | This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated.
    try {
      List<ServiceEvent> result = apiInstance.getServiceEventList(apiVersion, serviceId, startTimeUtc, endTimeUtc, timeout, eventsTypesFilter, excludeAnalysisEvents, skipCorrelationLookup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsStoreApi#getServiceEventList");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to 6.4] [enum: 6.4] |
| **serviceId** | **String**| The identity of the service. This ID is typically the full name of the service without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the service name is \&quot;fabric:/myapp/app1/svc1\&quot;, the service identity would be \&quot;myapp~app1~svc1\&quot; in 6.0+ and \&quot;myapp/app1/svc1\&quot; in previous versions. | |
| **startTimeUtc** | **String**| The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | |
| **endTimeUtc** | **String**| The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |
| **eventsTypesFilter** | **String**| This is a comma separated string specifying the types of FabricEvents that should only be included in the response. | [optional] |
| **excludeAnalysisEvents** | **Boolean**| This param disables the retrieval of AnalysisEvents if true is passed. | [optional] |
| **skipCorrelationLookup** | **Boolean**| This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated. | [optional] |

### Return type

[**List&lt;ServiceEvent&gt;**](ServiceEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of events objects with base type ServiceEvent. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getServicesEventList"></a>
# **getServicesEventList**
> List&lt;ServiceEvent&gt; getServicesEventList(apiVersion, startTimeUtc, endTimeUtc, timeout, eventsTypesFilter, excludeAnalysisEvents, skipCorrelationLookup)

Gets all Services-related events.

The response is list of ServiceEvent objects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsStoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    EventsStoreApi apiInstance = new EventsStoreApi(defaultClient);
    String apiVersion = "6.4"; // String | The version of the API. This parameter is required and its value must be '6.4'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    String startTimeUtc = "startTimeUtc_example"; // String | The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    String endTimeUtc = "endTimeUtc_example"; // String | The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    String eventsTypesFilter = "eventsTypesFilter_example"; // String | This is a comma separated string specifying the types of FabricEvents that should only be included in the response.
    Boolean excludeAnalysisEvents = true; // Boolean | This param disables the retrieval of AnalysisEvents if true is passed.
    Boolean skipCorrelationLookup = true; // Boolean | This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated.
    try {
      List<ServiceEvent> result = apiInstance.getServicesEventList(apiVersion, startTimeUtc, endTimeUtc, timeout, eventsTypesFilter, excludeAnalysisEvents, skipCorrelationLookup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsStoreApi#getServicesEventList");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to 6.4] [enum: 6.4] |
| **startTimeUtc** | **String**| The start time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | |
| **endTimeUtc** | **String**| The end time of a lookup query in ISO UTC yyyy-MM-ddTHH:mm:ssZ. | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |
| **eventsTypesFilter** | **String**| This is a comma separated string specifying the types of FabricEvents that should only be included in the response. | [optional] |
| **excludeAnalysisEvents** | **Boolean**| This param disables the retrieval of AnalysisEvents if true is passed. | [optional] |
| **skipCorrelationLookup** | **Boolean**| This param disables the search of CorrelatedEvents information if true is passed. otherwise the CorrelationEvents get processed and HasCorrelatedEvents field in every FabricEvent gets populated. | [optional] |

### Return type

[**List&lt;ServiceEvent&gt;**](ServiceEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of events objects with base type ServiceEvent. |  -  |
| **0** | The detailed error response. |  -  |

