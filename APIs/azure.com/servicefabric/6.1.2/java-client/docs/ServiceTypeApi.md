# ServiceTypeApi

All URIs are relative to *http://azure.local:19080*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDeployedServiceTypeInfoByName**](ServiceTypeApi.md#getDeployedServiceTypeInfoByName) | **GET** /Nodes/{nodeName}/$/GetApplications/{applicationId}/$/GetServiceTypes/{serviceTypeName} | Gets the information about a specified service type of the application deployed on a node in a Service Fabric cluster. |
| [**getDeployedServiceTypeInfoList**](ServiceTypeApi.md#getDeployedServiceTypeInfoList) | **GET** /Nodes/{nodeName}/$/GetApplications/{applicationId}/$/GetServiceTypes | Gets the list containing the information about service types from the applications deployed on a node in a Service Fabric cluster. |
| [**getServiceManifest**](ServiceTypeApi.md#getServiceManifest) | **GET** /ApplicationTypes/{applicationTypeName}/$/GetServiceManifest | Gets the manifest describing a service type. |
| [**getServiceTypeInfoList**](ServiceTypeApi.md#getServiceTypeInfoList) | **GET** /ApplicationTypes/{applicationTypeName}/$/GetServiceTypes | Gets the list containing the information about service types that are supported by a provisioned application type in a Service Fabric cluster. |


<a id="getDeployedServiceTypeInfoByName"></a>
# **getDeployedServiceTypeInfoByName**
> List&lt;DeployedServiceTypeInfo&gt; getDeployedServiceTypeInfoByName(apiVersion, nodeName, applicationId, serviceTypeName, serviceManifestName, timeout)

Gets the information about a specified service type of the application deployed on a node in a Service Fabric cluster.

Gets the list containing the information about a specific service type from the applications deployed on a node in a Service Fabric cluster. The response includes the name of the service type, its registration status, the code package that registered it and activation id of the service package. Each entry represents one activation of a service type, differentiated by the activation id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    ServiceTypeApi apiInstance = new ServiceTypeApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of this API. This is a required parameter and its value must be \"6.0\".  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. 
    String nodeName = "nodeName_example"; // String | The name of the node.
    String applicationId = "applicationId_example"; // String | The identity of the application. This is typically the full name of the application without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the application name is \"fabric:/myapp/app1\", the application identity would be \"myapp~app1\" in 6.0+ and \"myapp/app1\" in previous versions. 
    String serviceTypeName = "serviceTypeName_example"; // String | Specifies the name of a Service Fabric service type.
    String serviceManifestName = "serviceManifestName_example"; // String | The name of the service manifest to filter the list of deployed service type information. If specified, the response will only contain the information about service types that are defined in this service manifest.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      List<DeployedServiceTypeInfo> result = apiInstance.getDeployedServiceTypeInfoByName(apiVersion, nodeName, applicationId, serviceTypeName, serviceManifestName, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceTypeApi#getDeployedServiceTypeInfoByName");
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
| **apiVersion** | **String**| The version of this API. This is a required parameter and its value must be \&quot;6.0\&quot;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.  | [default to 6.0] [enum: 6.0] |
| **nodeName** | **String**| The name of the node. | |
| **applicationId** | **String**| The identity of the application. This is typically the full name of the application without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the application name is \&quot;fabric:/myapp/app1\&quot;, the application identity would be \&quot;myapp~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions.  | |
| **serviceTypeName** | **String**| Specifies the name of a Service Fabric service type. | |
| **serviceManifestName** | **String**| The name of the service manifest to filter the list of deployed service type information. If specified, the response will only contain the information about service types that are defined in this service manifest. | [optional] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

[**List&lt;DeployedServiceTypeInfo&gt;**](DeployedServiceTypeInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Information about service types of an application deployed on a node. |  -  |
| **204** | An empty response is returned if the specified service type of the application is not deployed on the node. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getDeployedServiceTypeInfoList"></a>
# **getDeployedServiceTypeInfoList**
> List&lt;DeployedServiceTypeInfo&gt; getDeployedServiceTypeInfoList(apiVersion, nodeName, applicationId, serviceManifestName, timeout)

Gets the list containing the information about service types from the applications deployed on a node in a Service Fabric cluster.

Gets the list containing the information about service types from the applications deployed on a node in a Service Fabric cluster. The response includes the name of the service type, its registration status, the code package that registered it and activation id of the service package.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    ServiceTypeApi apiInstance = new ServiceTypeApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of this API. This is a required parameter and its value must be \"6.0\".  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. 
    String nodeName = "nodeName_example"; // String | The name of the node.
    String applicationId = "applicationId_example"; // String | The identity of the application. This is typically the full name of the application without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the application name is \"fabric:/myapp/app1\", the application identity would be \"myapp~app1\" in 6.0+ and \"myapp/app1\" in previous versions. 
    String serviceManifestName = "serviceManifestName_example"; // String | The name of the service manifest to filter the list of deployed service type information. If specified, the response will only contain the information about service types that are defined in this service manifest.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      List<DeployedServiceTypeInfo> result = apiInstance.getDeployedServiceTypeInfoList(apiVersion, nodeName, applicationId, serviceManifestName, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceTypeApi#getDeployedServiceTypeInfoList");
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
| **apiVersion** | **String**| The version of this API. This is a required parameter and its value must be \&quot;6.0\&quot;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.  | [default to 6.0] [enum: 6.0] |
| **nodeName** | **String**| The name of the node. | |
| **applicationId** | **String**| The identity of the application. This is typically the full name of the application without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the application name is \&quot;fabric:/myapp/app1\&quot;, the application identity would be \&quot;myapp~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions.  | |
| **serviceManifestName** | **String**| The name of the service manifest to filter the list of deployed service type information. If specified, the response will only contain the information about service types that are defined in this service manifest. | [optional] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

[**List&lt;DeployedServiceTypeInfo&gt;**](DeployedServiceTypeInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of information about service types of an application deployed on a node. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getServiceManifest"></a>
# **getServiceManifest**
> ServiceTypeManifest getServiceManifest(apiVersion, applicationTypeName, applicationTypeVersion, serviceManifestName, timeout)

Gets the manifest describing a service type.

Gets the manifest describing a service type. The response contains the service manifest XML as a string.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    ServiceTypeApi apiInstance = new ServiceTypeApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of this API. This is a required parameter and its value must be \"6.0\".  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. 
    String applicationTypeName = "applicationTypeName_example"; // String | The name of the application type.
    String applicationTypeVersion = "applicationTypeVersion_example"; // String | The version of the application type.
    String serviceManifestName = "serviceManifestName_example"; // String | The name of a service manifest registered as part of an application type in a Service Fabric cluster.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      ServiceTypeManifest result = apiInstance.getServiceManifest(apiVersion, applicationTypeName, applicationTypeVersion, serviceManifestName, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceTypeApi#getServiceManifest");
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
| **apiVersion** | **String**| The version of this API. This is a required parameter and its value must be \&quot;6.0\&quot;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.  | [default to 6.0] [enum: 6.0] |
| **applicationTypeName** | **String**| The name of the application type. | |
| **applicationTypeVersion** | **String**| The version of the application type. | |
| **serviceManifestName** | **String**| The name of a service manifest registered as part of an application type in a Service Fabric cluster. | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

[**ServiceTypeManifest**](ServiceTypeManifest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Information about the service type. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getServiceTypeInfoList"></a>
# **getServiceTypeInfoList**
> List&lt;ServiceTypeInfo&gt; getServiceTypeInfoList(apiVersion, applicationTypeName, applicationTypeVersion, timeout)

Gets the list containing the information about service types that are supported by a provisioned application type in a Service Fabric cluster.

Gets the list containing the information about service types that are supported by a provisioned application type in a Service Fabric cluster. The response includes the name of the service type, the name and version of the service manifest the type is defined in, kind (stateless or stateless) of the service type and other information about it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    ServiceTypeApi apiInstance = new ServiceTypeApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of this API. This is a required parameter and its value must be \"6.0\".  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. 
    String applicationTypeName = "applicationTypeName_example"; // String | The name of the application type.
    String applicationTypeVersion = "applicationTypeVersion_example"; // String | The version of the application type.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      List<ServiceTypeInfo> result = apiInstance.getServiceTypeInfoList(apiVersion, applicationTypeName, applicationTypeVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceTypeApi#getServiceTypeInfoList");
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
| **apiVersion** | **String**| The version of this API. This is a required parameter and its value must be \&quot;6.0\&quot;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.  | [default to 6.0] [enum: 6.0] |
| **applicationTypeName** | **String**| The name of the application type. | |
| **applicationTypeVersion** | **String**| The version of the application type. | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

[**List&lt;ServiceTypeInfo&gt;**](ServiceTypeInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of service types that are supported by a provisioned application type. |  -  |
| **0** | The detailed error response. |  -  |

