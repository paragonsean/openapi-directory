# ComposeDeploymentApi

All URIs are relative to *http://azure.local:19080*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createComposeDeployment**](ComposeDeploymentApi.md#createComposeDeployment) | **PUT** /ComposeDeployments/$/Create | Creates a Service Fabric compose deployment. |
| [**getComposeDeploymentStatus**](ComposeDeploymentApi.md#getComposeDeploymentStatus) | **GET** /ComposeDeployments/{deploymentName} | Gets information about a Service Fabric compose deployment. |
| [**getComposeDeploymentStatusList**](ComposeDeploymentApi.md#getComposeDeploymentStatusList) | **GET** /ComposeDeployments | Gets the list of compose deployments created in the Service Fabric cluster. |
| [**getComposeDeploymentUpgradeProgress**](ComposeDeploymentApi.md#getComposeDeploymentUpgradeProgress) | **GET** /ComposeDeployments/{deploymentName}/$/GetUpgradeProgress | Gets details for the latest upgrade performed on this Service Fabric compose deployment. |
| [**removeComposeDeployment**](ComposeDeploymentApi.md#removeComposeDeployment) | **POST** /ComposeDeployments/{deploymentName}/$/Delete | Deletes an existing Service Fabric compose deployment from cluster. |
| [**startComposeDeploymentUpgrade**](ComposeDeploymentApi.md#startComposeDeploymentUpgrade) | **POST** /ComposeDeployments/{deploymentName}/$/Upgrade | Starts upgrading a compose deployment in the Service Fabric cluster. |


<a id="createComposeDeployment"></a>
# **createComposeDeployment**
> createComposeDeployment(apiVersion, createComposeDeploymentDescription, timeout)

Creates a Service Fabric compose deployment.

Creates a Service Fabric compose deployment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComposeDeploymentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    ComposeDeploymentApi apiInstance = new ComposeDeploymentApi(defaultClient);
    String apiVersion = "6.0-preview"; // String | The version of the API. This is a required parameter and its value must be \"6.0-preview\".
    CreateComposeDeploymentDescription createComposeDeploymentDescription = new CreateComposeDeploymentDescription(); // CreateComposeDeploymentDescription | Describes the compose deployment that needs to be created.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      apiInstance.createComposeDeployment(apiVersion, createComposeDeploymentDescription, timeout);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComposeDeploymentApi#createComposeDeployment");
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
| **apiVersion** | **String**| The version of the API. This is a required parameter and its value must be \&quot;6.0-preview\&quot;. | [default to 6.0-preview] [enum: 6.0-preview] |
| **createComposeDeploymentDescription** | [**CreateComposeDeploymentDescription**](CreateComposeDeploymentDescription.md)| Describes the compose deployment that needs to be created. | |
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
| **202** | A successful operation will return 202 status code. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getComposeDeploymentStatus"></a>
# **getComposeDeploymentStatus**
> ComposeDeploymentStatusInfo getComposeDeploymentStatus(apiVersion, deploymentName, timeout)

Gets information about a Service Fabric compose deployment.

Returns the status of the compose deployment that was created or in the process of being created in the Service Fabric cluster and whose name matches the one specified as the parameter. The response includes the name, status and other details about the deployment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComposeDeploymentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    ComposeDeploymentApi apiInstance = new ComposeDeploymentApi(defaultClient);
    String apiVersion = "6.0-preview"; // String | The version of the API. This is a required parameter and its value must be \"6.0-preview\".
    String deploymentName = "deploymentName_example"; // String | The identity of the deployment.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      ComposeDeploymentStatusInfo result = apiInstance.getComposeDeploymentStatus(apiVersion, deploymentName, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComposeDeploymentApi#getComposeDeploymentStatus");
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
| **apiVersion** | **String**| The version of the API. This is a required parameter and its value must be \&quot;6.0-preview\&quot;. | [default to 6.0-preview] [enum: 6.0-preview] |
| **deploymentName** | **String**| The identity of the deployment. | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

[**ComposeDeploymentStatusInfo**](ComposeDeploymentStatusInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Information about the compose deployment. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getComposeDeploymentStatusList"></a>
# **getComposeDeploymentStatusList**
> PagedComposeDeploymentStatusInfoList getComposeDeploymentStatusList(apiVersion, continuationToken, maxResults, timeout)

Gets the list of compose deployments created in the Service Fabric cluster.

Gets the status about the compose deployments that were created or in the process of being created in the Service Fabric cluster. The response includes the name, status and other details about the compose deployments. If the list of deployments do not fit in a page, one page of results is returned as well as a continuation token which can be used to get the next page.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComposeDeploymentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    ComposeDeploymentApi apiInstance = new ComposeDeploymentApi(defaultClient);
    String apiVersion = "6.0-preview"; // String | The version of the API. This is a required parameter and its value must be \"6.0-preview\".
    String continuationToken = "continuationToken_example"; // String | The continuation token parameter is used to obtain next set of results. A continuation token with a non empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
    Long maxResults = 0L; // Long | The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged queries includes as much results as possible that fit in the return message.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      PagedComposeDeploymentStatusInfoList result = apiInstance.getComposeDeploymentStatusList(apiVersion, continuationToken, maxResults, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComposeDeploymentApi#getComposeDeploymentStatusList");
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
| **apiVersion** | **String**| The version of the API. This is a required parameter and its value must be \&quot;6.0-preview\&quot;. | [default to 6.0-preview] [enum: 6.0-preview] |
| **continuationToken** | **String**| The continuation token parameter is used to obtain next set of results. A continuation token with a non empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results then the continuation token does not contain a value. The value of this parameter should not be URL encoded. | [optional] |
| **maxResults** | **Long**| The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged queries includes as much results as possible that fit in the return message. | [optional] [default to 0] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

[**PagedComposeDeploymentStatusInfoList**](PagedComposeDeploymentStatusInfoList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of status of compose deployments in the cluster. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getComposeDeploymentUpgradeProgress"></a>
# **getComposeDeploymentUpgradeProgress**
> ComposeDeploymentUpgradeProgressInfo getComposeDeploymentUpgradeProgress(apiVersion, deploymentName, timeout)

Gets details for the latest upgrade performed on this Service Fabric compose deployment.

Returns the information about the state of the compose deployment upgrade along with details to aid debugging application health issues.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComposeDeploymentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    ComposeDeploymentApi apiInstance = new ComposeDeploymentApi(defaultClient);
    String apiVersion = "6.0-preview"; // String | The version of the API. This is a required parameter and its value must be \"6.0-preview\".
    String deploymentName = "deploymentName_example"; // String | The identity of the deployment.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      ComposeDeploymentUpgradeProgressInfo result = apiInstance.getComposeDeploymentUpgradeProgress(apiVersion, deploymentName, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComposeDeploymentApi#getComposeDeploymentUpgradeProgress");
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
| **apiVersion** | **String**| The version of the API. This is a required parameter and its value must be \&quot;6.0-preview\&quot;. | [default to 6.0-preview] [enum: 6.0-preview] |
| **deploymentName** | **String**| The identity of the deployment. | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

[**ComposeDeploymentUpgradeProgressInfo**](ComposeDeploymentUpgradeProgressInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details about the compose deployment upgrade. |  -  |
| **0** | The detailed error response. |  -  |

<a id="removeComposeDeployment"></a>
# **removeComposeDeployment**
> removeComposeDeployment(apiVersion, deploymentName, timeout)

Deletes an existing Service Fabric compose deployment from cluster.

Deletes an existing Service Fabric compose deployment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComposeDeploymentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    ComposeDeploymentApi apiInstance = new ComposeDeploymentApi(defaultClient);
    String apiVersion = "6.0-preview"; // String | The version of the API. This is a required parameter and its value must be \"6.0-preview\".
    String deploymentName = "deploymentName_example"; // String | The identity of the deployment.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      apiInstance.removeComposeDeployment(apiVersion, deploymentName, timeout);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComposeDeploymentApi#removeComposeDeployment");
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
| **apiVersion** | **String**| The version of the API. This is a required parameter and its value must be \&quot;6.0-preview\&quot;. | [default to 6.0-preview] [enum: 6.0-preview] |
| **deploymentName** | **String**| The identity of the deployment. | |
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
| **202** | A successful operation will return 202 status code. |  -  |
| **0** | The detailed error response. |  -  |

<a id="startComposeDeploymentUpgrade"></a>
# **startComposeDeploymentUpgrade**
> startComposeDeploymentUpgrade(apiVersion, deploymentName, composeDeploymentUpgradeDescription, timeout)

Starts upgrading a compose deployment in the Service Fabric cluster.

Validates the supplied upgrade parameters and starts upgrading the deployment if the parameters are valid.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComposeDeploymentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    ComposeDeploymentApi apiInstance = new ComposeDeploymentApi(defaultClient);
    String apiVersion = "6.0-preview"; // String | The version of the API. This is a required parameter and its value must be \"6.0-preview\".
    String deploymentName = "deploymentName_example"; // String | The identity of the deployment.
    ComposeDeploymentUpgradeDescription composeDeploymentUpgradeDescription = new ComposeDeploymentUpgradeDescription(); // ComposeDeploymentUpgradeDescription | Parameters for upgrading compose deployment.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      apiInstance.startComposeDeploymentUpgrade(apiVersion, deploymentName, composeDeploymentUpgradeDescription, timeout);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComposeDeploymentApi#startComposeDeploymentUpgrade");
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
| **apiVersion** | **String**| The version of the API. This is a required parameter and its value must be \&quot;6.0-preview\&quot;. | [default to 6.0-preview] [enum: 6.0-preview] |
| **deploymentName** | **String**| The identity of the deployment. | |
| **composeDeploymentUpgradeDescription** | [**ComposeDeploymentUpgradeDescription**](ComposeDeploymentUpgradeDescription.md)| Parameters for upgrading compose deployment. | |
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
| **202** | A successful response means that the upgrade has started. Use GetComposeDeploymentUpgrade operation to get the status of the upgrade. |  -  |
| **0** | The detailed error response. |  -  |

