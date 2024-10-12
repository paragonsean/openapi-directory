# ServicePackageApi

All URIs are relative to *http://azure.local:19080*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deployedServicePackageToNode**](ServicePackageApi.md#deployedServicePackageToNode) | **POST** /Nodes/{nodeName}/$/DeployServicePackage | Downloads packages associated with specified service manifest to image cache on specified node. |
| [**getDeployedServicePackageHealth**](ServicePackageApi.md#getDeployedServicePackageHealth) | **GET** /Nodes/{nodeName}/$/GetApplications/{applicationId}/$/GetServicePackages/{servicePackageName}/$/GetHealth | Gets the information about health of an service package for a specific application deployed for a Service Fabric node and application. |
| [**getDeployedServicePackageHealthUsingPolicy**](ServicePackageApi.md#getDeployedServicePackageHealthUsingPolicy) | **POST** /Nodes/{nodeName}/$/GetApplications/{applicationId}/$/GetServicePackages/{servicePackageName}/$/GetHealth | Gets the information about health of service package for a specific application deployed on a Service Fabric node using the specified policy. |
| [**getDeployedServicePackageInfoList**](ServicePackageApi.md#getDeployedServicePackageInfoList) | **GET** /Nodes/{nodeName}/$/GetApplications/{applicationId}/$/GetServicePackages | Gets the list of service packages deployed on a Service Fabric node. |
| [**getDeployedServicePackageInfoListByName**](ServicePackageApi.md#getDeployedServicePackageInfoListByName) | **GET** /Nodes/{nodeName}/$/GetApplications/{applicationId}/$/GetServicePackages/{servicePackageName} | Gets the list of service packages deployed on a Service Fabric node matching exactly the specified name. |
| [**reportDeployedServicePackageHealth**](ServicePackageApi.md#reportDeployedServicePackageHealth) | **POST** /Nodes/{nodeName}/$/GetApplications/{applicationId}/$/GetServicePackages/{servicePackageName}/$/ReportHealth | Sends a health report on the Service Fabric deployed service package. |


<a id="deployedServicePackageToNode"></a>
# **deployedServicePackageToNode**
> deployedServicePackageToNode(apiVersion, nodeName, deployServicePackageToNodeDescription, timeout)

Downloads packages associated with specified service manifest to image cache on specified node.

Downloads packages associated with specified service manifest to image cache on specified node. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicePackageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    ServicePackageApi apiInstance = new ServicePackageApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
    String nodeName = "nodeName_example"; // String | The name of the node.
    DeployServicePackageToNodeDescription deployServicePackageToNodeDescription = new DeployServicePackageToNodeDescription(); // DeployServicePackageToNodeDescription | Describes information for deploying a service package to a Service Fabric node.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      apiInstance.deployedServicePackageToNode(apiVersion, nodeName, deployServicePackageToNodeDescription, timeout);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicePackageApi#deployedServicePackageToNode");
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
| **deployServicePackageToNodeDescription** | [**DeployServicePackageToNodeDescription**](DeployServicePackageToNodeDescription.md)| Describes information for deploying a service package to a Service Fabric node. | |
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

<a id="getDeployedServicePackageHealth"></a>
# **getDeployedServicePackageHealth**
> DeployedServicePackageHealth getDeployedServicePackageHealth(apiVersion, nodeName, applicationId, servicePackageName, eventsHealthStateFilter, timeout)

Gets the information about health of an service package for a specific application deployed for a Service Fabric node and application.

Gets the information about health of service package for a specific application deployed on a Service Fabric node. Use EventsHealthStateFilter to optionally filter for the collection of HealthEvent objects reported on the deployed service package based on health state.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicePackageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    ServicePackageApi apiInstance = new ServicePackageApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
    String nodeName = "nodeName_example"; // String | The name of the node.
    String applicationId = "applicationId_example"; // String | The identity of the application. This is typically the full name of the application without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the application name is \"fabric://myapp/app1\", the application identity would be \"myapp~app1\" in 6.0+ and \"myapp/app1\" in previous versions.
    String servicePackageName = "servicePackageName_example"; // String | The name of the service package.
    Integer eventsHealthStateFilter = 0; // Integer | Allows filtering the collection of HealthEvent objects returned based on health state. The possible values for this parameter include integer value of one of the following health states. Only events that match the filter are returned. All events are used to evaluate the aggregated health state. If not specified, all entries are returned. The state values are flag based enumeration, so the value could be a combination of these value obtained using bitwise 'OR' operator. For example, If the provided value is 6 then all of the events with HealthState value of OK (2) and Warning (4) are returned.  - Default - Default value. Matches any HealthState. The value is zero. - None - Filter that doesn't match any HealthState value. Used in order to return no results on a given collection of states. The value is 1. - Ok - Filter that matches input with HealthState value Ok. The value is 2. - Warning - Filter that matches input with HealthState value Warning. The value is 4. - Error - Filter that matches input with HealthState value Error. The value is 8. - All - Filter that matches input with any HealthState value. The value is 65535. 
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      DeployedServicePackageHealth result = apiInstance.getDeployedServicePackageHealth(apiVersion, nodeName, applicationId, servicePackageName, eventsHealthStateFilter, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicePackageApi#getDeployedServicePackageHealth");
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
| **applicationId** | **String**| The identity of the application. This is typically the full name of the application without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the application name is \&quot;fabric://myapp/app1\&quot;, the application identity would be \&quot;myapp~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions. | |
| **servicePackageName** | **String**| The name of the service package. | |
| **eventsHealthStateFilter** | **Integer**| Allows filtering the collection of HealthEvent objects returned based on health state. The possible values for this parameter include integer value of one of the following health states. Only events that match the filter are returned. All events are used to evaluate the aggregated health state. If not specified, all entries are returned. The state values are flag based enumeration, so the value could be a combination of these value obtained using bitwise &#39;OR&#39; operator. For example, If the provided value is 6 then all of the events with HealthState value of OK (2) and Warning (4) are returned.  - Default - Default value. Matches any HealthState. The value is zero. - None - Filter that doesn&#39;t match any HealthState value. Used in order to return no results on a given collection of states. The value is 1. - Ok - Filter that matches input with HealthState value Ok. The value is 2. - Warning - Filter that matches input with HealthState value Warning. The value is 4. - Error - Filter that matches input with HealthState value Error. The value is 8. - All - Filter that matches input with any HealthState value. The value is 65535.  | [optional] [default to 0] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

[**DeployedServicePackageHealth**](DeployedServicePackageHealth.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful operation will return 200 status code and the health information of the deployed service package for a specific node and application. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getDeployedServicePackageHealthUsingPolicy"></a>
# **getDeployedServicePackageHealthUsingPolicy**
> DeployedServicePackageHealth getDeployedServicePackageHealthUsingPolicy(apiVersion, nodeName, applicationId, servicePackageName, eventsHealthStateFilter, timeout, applicationHealthPolicy)

Gets the information about health of service package for a specific application deployed on a Service Fabric node using the specified policy.

Gets the information about health of an service package for a specific application deployed on a Service Fabric node. using the specified policy. Use EventsHealthStateFilter to optionally filter for the collection of HealthEvent objects reported on the deployed service package based on health state. Use ApplicationHealthPolicy to optionally override the health policies used to evaluate the health. This API only uses &#39;ConsiderWarningAsError&#39; field of the ApplicationHealthPolicy. The rest of the fields are ignored while evaluating the health of the deployed service package. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicePackageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    ServicePackageApi apiInstance = new ServicePackageApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
    String nodeName = "nodeName_example"; // String | The name of the node.
    String applicationId = "applicationId_example"; // String | The identity of the application. This is typically the full name of the application without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the application name is \"fabric://myapp/app1\", the application identity would be \"myapp~app1\" in 6.0+ and \"myapp/app1\" in previous versions.
    String servicePackageName = "servicePackageName_example"; // String | The name of the service package.
    Integer eventsHealthStateFilter = 0; // Integer | Allows filtering the collection of HealthEvent objects returned based on health state. The possible values for this parameter include integer value of one of the following health states. Only events that match the filter are returned. All events are used to evaluate the aggregated health state. If not specified, all entries are returned. The state values are flag based enumeration, so the value could be a combination of these value obtained using bitwise 'OR' operator. For example, If the provided value is 6 then all of the events with HealthState value of OK (2) and Warning (4) are returned.  - Default - Default value. Matches any HealthState. The value is zero. - None - Filter that doesn't match any HealthState value. Used in order to return no results on a given collection of states. The value is 1. - Ok - Filter that matches input with HealthState value Ok. The value is 2. - Warning - Filter that matches input with HealthState value Warning. The value is 4. - Error - Filter that matches input with HealthState value Error. The value is 8. - All - Filter that matches input with any HealthState value. The value is 65535. 
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    ApplicationHealthPolicy applicationHealthPolicy = new ApplicationHealthPolicy(); // ApplicationHealthPolicy | Describes the health policies used to evaluate the health of an application or one of its children. If not present, the health evaluation uses the health policy from application manifest or the default health policy. 
    try {
      DeployedServicePackageHealth result = apiInstance.getDeployedServicePackageHealthUsingPolicy(apiVersion, nodeName, applicationId, servicePackageName, eventsHealthStateFilter, timeout, applicationHealthPolicy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicePackageApi#getDeployedServicePackageHealthUsingPolicy");
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
| **applicationId** | **String**| The identity of the application. This is typically the full name of the application without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the application name is \&quot;fabric://myapp/app1\&quot;, the application identity would be \&quot;myapp~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions. | |
| **servicePackageName** | **String**| The name of the service package. | |
| **eventsHealthStateFilter** | **Integer**| Allows filtering the collection of HealthEvent objects returned based on health state. The possible values for this parameter include integer value of one of the following health states. Only events that match the filter are returned. All events are used to evaluate the aggregated health state. If not specified, all entries are returned. The state values are flag based enumeration, so the value could be a combination of these value obtained using bitwise &#39;OR&#39; operator. For example, If the provided value is 6 then all of the events with HealthState value of OK (2) and Warning (4) are returned.  - Default - Default value. Matches any HealthState. The value is zero. - None - Filter that doesn&#39;t match any HealthState value. Used in order to return no results on a given collection of states. The value is 1. - Ok - Filter that matches input with HealthState value Ok. The value is 2. - Warning - Filter that matches input with HealthState value Warning. The value is 4. - Error - Filter that matches input with HealthState value Error. The value is 8. - All - Filter that matches input with any HealthState value. The value is 65535.  | [optional] [default to 0] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |
| **applicationHealthPolicy** | [**ApplicationHealthPolicy**](ApplicationHealthPolicy.md)| Describes the health policies used to evaluate the health of an application or one of its children. If not present, the health evaluation uses the health policy from application manifest or the default health policy.  | [optional] |

### Return type

[**DeployedServicePackageHealth**](DeployedServicePackageHealth.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful operation will return 200 status code and the health information of the deployed service package for a specific node and application. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getDeployedServicePackageInfoList"></a>
# **getDeployedServicePackageInfoList**
> List&lt;DeployedServicePackageInfo&gt; getDeployedServicePackageInfoList(apiVersion, nodeName, applicationId, timeout)

Gets the list of service packages deployed on a Service Fabric node.

Returns the information about the service packages deployed on a Service Fabric node for the given application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicePackageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    ServicePackageApi apiInstance = new ServicePackageApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
    String nodeName = "nodeName_example"; // String | The name of the node.
    String applicationId = "applicationId_example"; // String | The identity of the application. This is typically the full name of the application without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the application name is \"fabric://myapp/app1\", the application identity would be \"myapp~app1\" in 6.0+ and \"myapp/app1\" in previous versions.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      List<DeployedServicePackageInfo> result = apiInstance.getDeployedServicePackageInfoList(apiVersion, nodeName, applicationId, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicePackageApi#getDeployedServicePackageInfoList");
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
| **applicationId** | **String**| The identity of the application. This is typically the full name of the application without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the application name is \&quot;fabric://myapp/app1\&quot;, the application identity would be \&quot;myapp~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions. | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

[**List&lt;DeployedServicePackageInfo&gt;**](DeployedServicePackageInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful operation will return 200 status code and the list of deployed service packages information. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getDeployedServicePackageInfoListByName"></a>
# **getDeployedServicePackageInfoListByName**
> getDeployedServicePackageInfoListByName(apiVersion, nodeName, applicationId, servicePackageName, timeout)

Gets the list of service packages deployed on a Service Fabric node matching exactly the specified name.

Returns the information about the service packages deployed on a Service Fabric node for the given application. These results are of service packages whose name match exactly the service package name specified as the parameter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicePackageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    ServicePackageApi apiInstance = new ServicePackageApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
    String nodeName = "nodeName_example"; // String | The name of the node.
    String applicationId = "applicationId_example"; // String | The identity of the application. This is typically the full name of the application without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the application name is \"fabric://myapp/app1\", the application identity would be \"myapp~app1\" in 6.0+ and \"myapp/app1\" in previous versions.
    String servicePackageName = "servicePackageName_example"; // String | The name of the service package.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      apiInstance.getDeployedServicePackageInfoListByName(apiVersion, nodeName, applicationId, servicePackageName, timeout);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicePackageApi#getDeployedServicePackageInfoListByName");
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
| **applicationId** | **String**| The identity of the application. This is typically the full name of the application without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the application name is \&quot;fabric://myapp/app1\&quot;, the application identity would be \&quot;myapp~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions. | |
| **servicePackageName** | **String**| The name of the service package. | |
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
| **200** | A successful operation will return 200 status code and the list of deployed service packages information. |  -  |
| **204** | An empty response is returned if the specified service package from the application is not deployed on the node. |  -  |
| **0** | The detailed error response. |  -  |

<a id="reportDeployedServicePackageHealth"></a>
# **reportDeployedServicePackageHealth**
> reportDeployedServicePackageHealth(apiVersion, nodeName, applicationId, servicePackageName, healthInformation, immediate, timeout)

Sends a health report on the Service Fabric deployed service package.

Reports health state of the service package of the application deployed on a Service Fabric node. The report must contain the information about the source of the health report and property on which it is reported. The report is sent to a Service Fabric gateway Service, which forwards to the health store. The report may be accepted by the gateway, but rejected by the health store after extra validation. For example, the health store may reject the report because of an invalid parameter, like a stale sequence number. To see whether the report was applied in the health store, get deployed service package health and check that the report appears in the HealthEvents section. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicePackageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    ServicePackageApi apiInstance = new ServicePackageApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
    String nodeName = "nodeName_example"; // String | The name of the node.
    String applicationId = "applicationId_example"; // String | The identity of the application. This is typically the full name of the application without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the application name is \"fabric://myapp/app1\", the application identity would be \"myapp~app1\" in 6.0+ and \"myapp/app1\" in previous versions.
    String servicePackageName = "servicePackageName_example"; // String | The name of the service package.
    HealthInformation healthInformation = new HealthInformation(); // HealthInformation | Describes the health information for the health report. This information needs to be present in all of the health reports sent to the health manager.
    Boolean immediate = false; // Boolean | A flag which indicates whether the report should be sent immediately. A health report is sent to a Service Fabric gateway Application, which forwards to the health store. If Immediate is set to true, the report is sent immediately from Http Gateway to the health store, regardless of the fabric client settings that the Http Gateway Application is using. This is useful for critical reports that should be sent as soon as possible. Depending on timing and other conditions, sending the report may still fail, for example if the Http Gateway is closed or the message doesn't reach the Gateway. If Immediate is set to false, the report is sent based on the health client settings from the Http Gateway. Therefore, it will be batched according to the HealthReportSendInterval configuration. This is the recommended setting because it allows the health client to optimize health reporting messages to health store as well as health report processing. By default, reports are not sent immediately. 
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      apiInstance.reportDeployedServicePackageHealth(apiVersion, nodeName, applicationId, servicePackageName, healthInformation, immediate, timeout);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicePackageApi#reportDeployedServicePackageHealth");
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
| **applicationId** | **String**| The identity of the application. This is typically the full name of the application without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the application name is \&quot;fabric://myapp/app1\&quot;, the application identity would be \&quot;myapp~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions. | |
| **servicePackageName** | **String**| The name of the service package. | |
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

