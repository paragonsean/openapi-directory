# CodePackageApi

All URIs are relative to *http://azure.local:19080*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDeployedCodePackageInfoList**](CodePackageApi.md#getDeployedCodePackageInfoList) | **GET** /Nodes/{nodeName}/$/GetApplications/{applicationId}/$/GetCodePackages | Gets the list of code packages deployed on a Service Fabric node. |
| [**restartDeployedCodePackage**](CodePackageApi.md#restartDeployedCodePackage) | **POST** /Nodes/{nodeName}/$/GetApplications/{applicationId}/$/GetCodePackages/$/Restart | Restarts a code package deployed on a Service Fabric node in a cluster. |


<a id="getDeployedCodePackageInfoList"></a>
# **getDeployedCodePackageInfoList**
> List&lt;DeployedCodePackageInfo&gt; getDeployedCodePackageInfoList(apiVersion, nodeName, applicationId, serviceManifestName, codePackageName, timeout)

Gets the list of code packages deployed on a Service Fabric node.

Gets the list of code packages deployed on a Service Fabric node for the given application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CodePackageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    CodePackageApi apiInstance = new CodePackageApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
    String nodeName = "nodeName_example"; // String | The name of the node.
    String applicationId = "applicationId_example"; // String | The identity of the application. This is typically the full name of the application without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the application name is \"fabric://myapp/app1\", the application identity would be \"myapp~app1\" in 6.0+ and \"myapp/app1\" in previous versions.
    String serviceManifestName = "serviceManifestName_example"; // String | The name of a service manifest registered as part of an application type in a Service Fabric cluster.
    String codePackageName = "codePackageName_example"; // String | The name of code package specified in service manifest registered as part of an application type in a Service Fabric cluster.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      List<DeployedCodePackageInfo> result = apiInstance.getDeployedCodePackageInfoList(apiVersion, nodeName, applicationId, serviceManifestName, codePackageName, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CodePackageApi#getDeployedCodePackageInfoList");
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
| **serviceManifestName** | **String**| The name of a service manifest registered as part of an application type in a Service Fabric cluster. | [optional] |
| **codePackageName** | **String**| The name of code package specified in service manifest registered as part of an application type in a Service Fabric cluster. | [optional] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

[**List&lt;DeployedCodePackageInfo&gt;**](DeployedCodePackageInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful operation will return 200 status code and the list of deployed code packages information. |  -  |
| **0** | The detailed error response. |  -  |

<a id="restartDeployedCodePackage"></a>
# **restartDeployedCodePackage**
> restartDeployedCodePackage(apiVersion, nodeName, applicationId, restartDeployedCodePackageDescription, timeout)

Restarts a code package deployed on a Service Fabric node in a cluster.

Restarts a code package deployed on a Service Fabric node in a cluster. This aborts the code package process, which will restart all the user service replicas hosted in that process.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CodePackageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    CodePackageApi apiInstance = new CodePackageApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
    String nodeName = "nodeName_example"; // String | The name of the node.
    String applicationId = "applicationId_example"; // String | The identity of the application. This is typically the full name of the application without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the application name is \"fabric://myapp/app1\", the application identity would be \"myapp~app1\" in 6.0+ and \"myapp/app1\" in previous versions.
    RestartDeployedCodePackageDescription restartDeployedCodePackageDescription = new RestartDeployedCodePackageDescription(); // RestartDeployedCodePackageDescription | Describes the deployed code package on Service Fabric node to restart.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      apiInstance.restartDeployedCodePackage(apiVersion, nodeName, applicationId, restartDeployedCodePackageDescription, timeout);
    } catch (ApiException e) {
      System.err.println("Exception when calling CodePackageApi#restartDeployedCodePackage");
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
| **restartDeployedCodePackageDescription** | [**RestartDeployedCodePackageDescription**](RestartDeployedCodePackageDescription.md)| Describes the deployed code package on Service Fabric node to restart. | |
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

