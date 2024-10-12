# CodepushApi

All URIs are relative to *https://api.appcenter.ms*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**codePushAcquisitionGetAcquisitionStatus**](CodepushApi.md#codePushAcquisitionGetAcquisitionStatus) | **GET** /v0.1/public/codepush/status |  |
| [**codePushAcquisitionUpdateCheck**](CodepushApi.md#codePushAcquisitionUpdateCheck) | **GET** /v0.1/public/codepush/update_check |  |
| [**codePushAcquisitionUpdateDeployStatus**](CodepushApi.md#codePushAcquisitionUpdateDeployStatus) | **POST** /v0.1/public/codepush/report_status/deploy |  |
| [**codePushAcquisitionUpdateDownloadStatus**](CodepushApi.md#codePushAcquisitionUpdateDownloadStatus) | **POST** /v0.1/public/codepush/report_status/download |  |
| [**codePushDeploymentMetricsGet**](CodepushApi.md#codePushDeploymentMetricsGet) | **GET** /v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name}/metrics |  |
| [**codePushDeploymentReleaseRollback**](CodepushApi.md#codePushDeploymentReleaseRollback) | **POST** /v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name}/rollback_release |  |
| [**codePushDeploymentReleasesCreate**](CodepushApi.md#codePushDeploymentReleasesCreate) | **POST** /v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name}/releases |  |
| [**codePushDeploymentReleasesDelete**](CodepushApi.md#codePushDeploymentReleasesDelete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name}/releases |  |
| [**codePushDeploymentReleasesGet**](CodepushApi.md#codePushDeploymentReleasesGet) | **GET** /v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name}/releases |  |
| [**codePushDeploymentUploadCreate**](CodepushApi.md#codePushDeploymentUploadCreate) | **POST** /v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name}/uploads |  |
| [**codePushDeploymentsCreate**](CodepushApi.md#codePushDeploymentsCreate) | **POST** /v0.1/apps/{owner_name}/{app_name}/deployments |  |
| [**codePushDeploymentsDelete**](CodepushApi.md#codePushDeploymentsDelete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name} |  |
| [**codePushDeploymentsGet**](CodepushApi.md#codePushDeploymentsGet) | **GET** /v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name} |  |
| [**codePushDeploymentsList**](CodepushApi.md#codePushDeploymentsList) | **GET** /v0.1/apps/{owner_name}/{app_name}/deployments |  |
| [**codePushDeploymentsPromote**](CodepushApi.md#codePushDeploymentsPromote) | **POST** /v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name}/promote_release/{promote_deployment_name} |  |
| [**codePushDeploymentsUpdate**](CodepushApi.md#codePushDeploymentsUpdate) | **PATCH** /v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name} |  |
| [**deploymentReleasesUpdate**](CodepushApi.md#deploymentReleasesUpdate) | **PATCH** /v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name}/releases/{release_label} |  |
| [**legacyCodePushAcquisitionUpdateCheck**](CodepushApi.md#legacyCodePushAcquisitionUpdateCheck) | **GET** /v0.1/legacy/updateCheck |  |
| [**legacyCodePushAcquisitionUpdateDownloadStatus**](CodepushApi.md#legacyCodePushAcquisitionUpdateDownloadStatus) | **POST** /v0.1/legacy/reportStatus/download |  |
| [**legacyCodePushAcquisitionUpdateInstallsStatus**](CodepushApi.md#legacyCodePushAcquisitionUpdateInstallsStatus) | **POST** /v0.1/legacy/reportStatus/deploy |  |


<a id="codePushAcquisitionGetAcquisitionStatus"></a>
# **codePushAcquisitionGetAcquisitionStatus**
> CodePushAcquisitionGetAcquisitionStatus200Response codePushAcquisitionGetAcquisitionStatus()



Returns the acquisition service status to the caller

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CodepushApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");

    CodepushApi apiInstance = new CodepushApi(defaultClient);
    try {
      CodePushAcquisitionGetAcquisitionStatus200Response result = apiInstance.codePushAcquisitionGetAcquisitionStatus();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CodepushApi#codePushAcquisitionGetAcquisitionStatus");
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

[**CodePushAcquisitionGetAcquisitionStatus200Response**](CodePushAcquisitionGetAcquisitionStatus200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="codePushAcquisitionUpdateCheck"></a>
# **codePushAcquisitionUpdateCheck**
> CodePushAcquisitionUpdateCheck200Response codePushAcquisitionUpdateCheck(deploymentKey, appVersion, packageHash, label, clientUniqueId, isCompanion, previousLabelOrAppVersion, previousDeploymentKey)



Check for updates

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CodepushApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");

    CodepushApi apiInstance = new CodepushApi(defaultClient);
    String deploymentKey = "deploymentKey_example"; // String | 
    String appVersion = "appVersion_example"; // String | 
    String packageHash = "packageHash_example"; // String | 
    String label = "label_example"; // String | 
    String clientUniqueId = "clientUniqueId_example"; // String | 
    Boolean isCompanion = true; // Boolean | 
    String previousLabelOrAppVersion = "previousLabelOrAppVersion_example"; // String | 
    String previousDeploymentKey = "previousDeploymentKey_example"; // String | 
    try {
      CodePushAcquisitionUpdateCheck200Response result = apiInstance.codePushAcquisitionUpdateCheck(deploymentKey, appVersion, packageHash, label, clientUniqueId, isCompanion, previousLabelOrAppVersion, previousDeploymentKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CodepushApi#codePushAcquisitionUpdateCheck");
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
| **deploymentKey** | **String**|  | |
| **appVersion** | **String**|  | |
| **packageHash** | **String**|  | [optional] |
| **label** | **String**|  | [optional] |
| **clientUniqueId** | **String**|  | [optional] |
| **isCompanion** | **Boolean**|  | [optional] |
| **previousLabelOrAppVersion** | **String**|  | [optional] |
| **previousDeploymentKey** | **String**|  | [optional] |

### Return type

[**CodePushAcquisitionUpdateCheck200Response**](CodePushAcquisitionUpdateCheck200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="codePushAcquisitionUpdateDeployStatus"></a>
# **codePushAcquisitionUpdateDeployStatus**
> codePushAcquisitionUpdateDeployStatus(codePushAcquisitionUpdateDeployStatusRequest)



Report Deployment status metric

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CodepushApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");

    CodepushApi apiInstance = new CodepushApi(defaultClient);
    CodePushAcquisitionUpdateDeployStatusRequest codePushAcquisitionUpdateDeployStatusRequest = new CodePushAcquisitionUpdateDeployStatusRequest(); // CodePushAcquisitionUpdateDeployStatusRequest | Deployment status metric properties
    try {
      apiInstance.codePushAcquisitionUpdateDeployStatus(codePushAcquisitionUpdateDeployStatusRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling CodepushApi#codePushAcquisitionUpdateDeployStatus");
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
| **codePushAcquisitionUpdateDeployStatusRequest** | [**CodePushAcquisitionUpdateDeployStatusRequest**](CodePushAcquisitionUpdateDeployStatusRequest.md)| Deployment status metric properties | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="codePushAcquisitionUpdateDownloadStatus"></a>
# **codePushAcquisitionUpdateDownloadStatus**
> codePushAcquisitionUpdateDownloadStatus(codePushAcquisitionUpdateDeployStatusRequest)



Report download of specified release

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CodepushApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");

    CodepushApi apiInstance = new CodepushApi(defaultClient);
    CodePushAcquisitionUpdateDeployStatusRequest codePushAcquisitionUpdateDeployStatusRequest = new CodePushAcquisitionUpdateDeployStatusRequest(); // CodePushAcquisitionUpdateDeployStatusRequest | Deployment status metric properties
    try {
      apiInstance.codePushAcquisitionUpdateDownloadStatus(codePushAcquisitionUpdateDeployStatusRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling CodepushApi#codePushAcquisitionUpdateDownloadStatus");
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
| **codePushAcquisitionUpdateDeployStatusRequest** | [**CodePushAcquisitionUpdateDeployStatusRequest**](CodePushAcquisitionUpdateDeployStatusRequest.md)| Deployment status metric properties | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="codePushDeploymentMetricsGet"></a>
# **codePushDeploymentMetricsGet**
> List&lt;CodePushDeploymentMetricsGet200ResponseInner&gt; codePushDeploymentMetricsGet(deploymentName, ownerName, appName)



Gets all releases metrics for specified Deployment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CodepushApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CodepushApi apiInstance = new CodepushApi(defaultClient);
    String deploymentName = "deploymentName_example"; // String | deployment name
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      List<CodePushDeploymentMetricsGet200ResponseInner> result = apiInstance.codePushDeploymentMetricsGet(deploymentName, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CodepushApi#codePushDeploymentMetricsGet");
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
| **deploymentName** | **String**| deployment name | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**List&lt;CodePushDeploymentMetricsGet200ResponseInner&gt;**](CodePushDeploymentMetricsGet200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="codePushDeploymentReleaseRollback"></a>
# **codePushDeploymentReleaseRollback**
> CodePushDeploymentsList200ResponseInnerLatestRelease codePushDeploymentReleaseRollback(deploymentName, ownerName, appName, codePushDeploymentReleaseRollbackRequest)



Rollback the latest or a specific release for an app deployment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CodepushApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CodepushApi apiInstance = new CodepushApi(defaultClient);
    String deploymentName = "deploymentName_example"; // String | deployment name
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    CodePushDeploymentReleaseRollbackRequest codePushDeploymentReleaseRollbackRequest = new CodePushDeploymentReleaseRollbackRequest(); // CodePushDeploymentReleaseRollbackRequest | The specific release label that you want to rollback to
    try {
      CodePushDeploymentsList200ResponseInnerLatestRelease result = apiInstance.codePushDeploymentReleaseRollback(deploymentName, ownerName, appName, codePushDeploymentReleaseRollbackRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CodepushApi#codePushDeploymentReleaseRollback");
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
| **deploymentName** | **String**| deployment name | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **codePushDeploymentReleaseRollbackRequest** | [**CodePushDeploymentReleaseRollbackRequest**](CodePushDeploymentReleaseRollbackRequest.md)| The specific release label that you want to rollback to | [optional] |

### Return type

[**CodePushDeploymentsList200ResponseInnerLatestRelease**](CodePushDeploymentsList200ResponseInnerLatestRelease.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **0** | Error |  -  |

<a id="codePushDeploymentReleasesCreate"></a>
# **codePushDeploymentReleasesCreate**
> CodePushDeploymentsList200ResponseInnerLatestRelease codePushDeploymentReleasesCreate(deploymentName, ownerName, appName, codePushDeploymentReleasesCreateRequest)



Create a new CodePush release for the specified deployment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CodepushApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CodepushApi apiInstance = new CodepushApi(defaultClient);
    String deploymentName = "deploymentName_example"; // String | deployment name
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    CodePushDeploymentReleasesCreateRequest codePushDeploymentReleasesCreateRequest = new CodePushDeploymentReleasesCreateRequest(); // CodePushDeploymentReleasesCreateRequest | The necessary information required to download the bundle and being the release process.
    try {
      CodePushDeploymentsList200ResponseInnerLatestRelease result = apiInstance.codePushDeploymentReleasesCreate(deploymentName, ownerName, appName, codePushDeploymentReleasesCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CodepushApi#codePushDeploymentReleasesCreate");
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
| **deploymentName** | **String**| deployment name | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **codePushDeploymentReleasesCreateRequest** | [**CodePushDeploymentReleasesCreateRequest**](CodePushDeploymentReleasesCreateRequest.md)| The necessary information required to download the bundle and being the release process. | |

### Return type

[**CodePushDeploymentsList200ResponseInnerLatestRelease**](CodePushDeploymentsList200ResponseInnerLatestRelease.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **0** | Error |  -  |

<a id="codePushDeploymentReleasesDelete"></a>
# **codePushDeploymentReleasesDelete**
> codePushDeploymentReleasesDelete(deploymentName, ownerName, appName)



Clears a Deployment of releases

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CodepushApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CodepushApi apiInstance = new CodepushApi(defaultClient);
    String deploymentName = "deploymentName_example"; // String | deployment name
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      apiInstance.codePushDeploymentReleasesDelete(deploymentName, ownerName, appName);
    } catch (ApiException e) {
      System.err.println("Exception when calling CodepushApi#codePushDeploymentReleasesDelete");
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
| **deploymentName** | **String**| deployment name | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **0** | Error |  -  |

<a id="codePushDeploymentReleasesGet"></a>
# **codePushDeploymentReleasesGet**
> List&lt;CodePushDeploymentsList200ResponseInnerLatestRelease&gt; codePushDeploymentReleasesGet(deploymentName, ownerName, appName)



Gets the history of releases on a Deployment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CodepushApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CodepushApi apiInstance = new CodepushApi(defaultClient);
    String deploymentName = "deploymentName_example"; // String | deployment name
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      List<CodePushDeploymentsList200ResponseInnerLatestRelease> result = apiInstance.codePushDeploymentReleasesGet(deploymentName, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CodepushApi#codePushDeploymentReleasesGet");
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
| **deploymentName** | **String**| deployment name | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**List&lt;CodePushDeploymentsList200ResponseInnerLatestRelease&gt;**](CodePushDeploymentsList200ResponseInnerLatestRelease.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="codePushDeploymentUploadCreate"></a>
# **codePushDeploymentUploadCreate**
> CodePushDeploymentUploadCreate200Response codePushDeploymentUploadCreate(deploymentName, ownerName, appName)



Create a new CodePush release upload for the specified deployment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CodepushApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CodepushApi apiInstance = new CodepushApi(defaultClient);
    String deploymentName = "deploymentName_example"; // String | deployment name
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      CodePushDeploymentUploadCreate200Response result = apiInstance.codePushDeploymentUploadCreate(deploymentName, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CodepushApi#codePushDeploymentUploadCreate");
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
| **deploymentName** | **String**| deployment name | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**CodePushDeploymentUploadCreate200Response**](CodePushDeploymentUploadCreate200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="codePushDeploymentsCreate"></a>
# **codePushDeploymentsCreate**
> CodePushDeploymentsList200ResponseInner codePushDeploymentsCreate(ownerName, appName, codePushDeploymentsList200ResponseInner)



Creates a CodePush Deployment for the given app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CodepushApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CodepushApi apiInstance = new CodepushApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    CodePushDeploymentsList200ResponseInner codePushDeploymentsList200ResponseInner = new CodePushDeploymentsList200ResponseInner(); // CodePushDeploymentsList200ResponseInner | Deployment to be created
    try {
      CodePushDeploymentsList200ResponseInner result = apiInstance.codePushDeploymentsCreate(ownerName, appName, codePushDeploymentsList200ResponseInner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CodepushApi#codePushDeploymentsCreate");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **codePushDeploymentsList200ResponseInner** | [**CodePushDeploymentsList200ResponseInner**](CodePushDeploymentsList200ResponseInner.md)| Deployment to be created | |

### Return type

[**CodePushDeploymentsList200ResponseInner**](CodePushDeploymentsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **0** | Error |  -  |

<a id="codePushDeploymentsDelete"></a>
# **codePushDeploymentsDelete**
> codePushDeploymentsDelete(deploymentName, ownerName, appName, body)



Deletes a CodePush Deployment for the given app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CodepushApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CodepushApi apiInstance = new CodepushApi(defaultClient);
    String deploymentName = "deploymentName_example"; // String | deployment name
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    Object body = null; // Object | 
    try {
      apiInstance.codePushDeploymentsDelete(deploymentName, ownerName, appName, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling CodepushApi#codePushDeploymentsDelete");
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
| **deploymentName** | **String**| deployment name | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **body** | **Object**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **0** | Error |  -  |

<a id="codePushDeploymentsGet"></a>
# **codePushDeploymentsGet**
> CodePushDeploymentsList200ResponseInner codePushDeploymentsGet(deploymentName, ownerName, appName)



Gets a CodePush Deployment for the given app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CodepushApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CodepushApi apiInstance = new CodepushApi(defaultClient);
    String deploymentName = "deploymentName_example"; // String | deployment name
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      CodePushDeploymentsList200ResponseInner result = apiInstance.codePushDeploymentsGet(deploymentName, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CodepushApi#codePushDeploymentsGet");
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
| **deploymentName** | **String**| deployment name | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**CodePushDeploymentsList200ResponseInner**](CodePushDeploymentsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="codePushDeploymentsList"></a>
# **codePushDeploymentsList**
> List&lt;CodePushDeploymentsList200ResponseInner&gt; codePushDeploymentsList(ownerName, appName)



Gets a list of CodePush deployments for the given app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CodepushApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CodepushApi apiInstance = new CodepushApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      List<CodePushDeploymentsList200ResponseInner> result = apiInstance.codePushDeploymentsList(ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CodepushApi#codePushDeploymentsList");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**List&lt;CodePushDeploymentsList200ResponseInner&gt;**](CodePushDeploymentsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="codePushDeploymentsPromote"></a>
# **codePushDeploymentsPromote**
> CodePushDeploymentsList200ResponseInnerLatestRelease codePushDeploymentsPromote(deploymentName, promoteDeploymentName, ownerName, appName, codePushDeploymentsPromoteRequest)



Promote one release (default latest one) from one deployment to another

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CodepushApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CodepushApi apiInstance = new CodepushApi(defaultClient);
    String deploymentName = "deploymentName_example"; // String | deployment name
    String promoteDeploymentName = "promoteDeploymentName_example"; // String | deployment name
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    CodePushDeploymentsPromoteRequest codePushDeploymentsPromoteRequest = new CodePushDeploymentsPromoteRequest(); // CodePushDeploymentsPromoteRequest | Release to be promoted, only needs to provide optional fields, description, label, disabled, mandatory, rollout, targetBinaryVersion
    try {
      CodePushDeploymentsList200ResponseInnerLatestRelease result = apiInstance.codePushDeploymentsPromote(deploymentName, promoteDeploymentName, ownerName, appName, codePushDeploymentsPromoteRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CodepushApi#codePushDeploymentsPromote");
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
| **deploymentName** | **String**| deployment name | |
| **promoteDeploymentName** | **String**| deployment name | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **codePushDeploymentsPromoteRequest** | [**CodePushDeploymentsPromoteRequest**](CodePushDeploymentsPromoteRequest.md)| Release to be promoted, only needs to provide optional fields, description, label, disabled, mandatory, rollout, targetBinaryVersion | [optional] |

### Return type

[**CodePushDeploymentsList200ResponseInnerLatestRelease**](CodePushDeploymentsList200ResponseInnerLatestRelease.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Promote a new release to the target deployment, return this new release. |  -  |
| **0** | Error |  -  |

<a id="codePushDeploymentsUpdate"></a>
# **codePushDeploymentsUpdate**
> codePushDeploymentsUpdate(deploymentName, ownerName, appName, codePushDeploymentsUpdateRequest)



Modifies a CodePush Deployment for the given app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CodepushApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CodepushApi apiInstance = new CodepushApi(defaultClient);
    String deploymentName = "deploymentName_example"; // String | deployment name
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    CodePushDeploymentsUpdateRequest codePushDeploymentsUpdateRequest = new CodePushDeploymentsUpdateRequest(); // CodePushDeploymentsUpdateRequest | Deployment modification. All fields are optional and only provided fields will get updated.
    try {
      apiInstance.codePushDeploymentsUpdate(deploymentName, ownerName, appName, codePushDeploymentsUpdateRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling CodepushApi#codePushDeploymentsUpdate");
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
| **deploymentName** | **String**| deployment name | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **codePushDeploymentsUpdateRequest** | [**CodePushDeploymentsUpdateRequest**](CodePushDeploymentsUpdateRequest.md)| Deployment modification. All fields are optional and only provided fields will get updated. | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **0** | Error |  -  |

<a id="deploymentReleasesUpdate"></a>
# **deploymentReleasesUpdate**
> CodePushDeploymentsList200ResponseInnerLatestRelease deploymentReleasesUpdate(deploymentName, releaseLabel, ownerName, appName, deploymentReleasesUpdateRequest)



Modifies a CodePush release metadata under the given Deployment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CodepushApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CodepushApi apiInstance = new CodepushApi(defaultClient);
    String deploymentName = "deploymentName_example"; // String | deployment name
    String releaseLabel = "releaseLabel_example"; // String | release label
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    DeploymentReleasesUpdateRequest deploymentReleasesUpdateRequest = new DeploymentReleasesUpdateRequest(); // DeploymentReleasesUpdateRequest | Release modification. All fields are optional and only provided fields will get updated.
    try {
      CodePushDeploymentsList200ResponseInnerLatestRelease result = apiInstance.deploymentReleasesUpdate(deploymentName, releaseLabel, ownerName, appName, deploymentReleasesUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CodepushApi#deploymentReleasesUpdate");
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
| **deploymentName** | **String**| deployment name | |
| **releaseLabel** | **String**| release label | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **deploymentReleasesUpdateRequest** | [**DeploymentReleasesUpdateRequest**](DeploymentReleasesUpdateRequest.md)| Release modification. All fields are optional and only provided fields will get updated. | |

### Return type

[**CodePushDeploymentsList200ResponseInnerLatestRelease**](CodePushDeploymentsList200ResponseInnerLatestRelease.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **204** | Nothing to patch |  -  |
| **0** | Error |  -  |

<a id="legacyCodePushAcquisitionUpdateCheck"></a>
# **legacyCodePushAcquisitionUpdateCheck**
> LegacyCodePushAcquisitionUpdateCheck200Response legacyCodePushAcquisitionUpdateCheck(deploymentKey, appVersion, packageHash, label, clientUniqueId, isCompanion)



Check for updates

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CodepushApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CodepushApi apiInstance = new CodepushApi(defaultClient);
    String deploymentKey = "deploymentKey_example"; // String | 
    String appVersion = "appVersion_example"; // String | 
    String packageHash = "packageHash_example"; // String | 
    String label = "label_example"; // String | 
    String clientUniqueId = "clientUniqueId_example"; // String | 
    String isCompanion = "isCompanion_example"; // String | 
    try {
      LegacyCodePushAcquisitionUpdateCheck200Response result = apiInstance.legacyCodePushAcquisitionUpdateCheck(deploymentKey, appVersion, packageHash, label, clientUniqueId, isCompanion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CodepushApi#legacyCodePushAcquisitionUpdateCheck");
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
| **deploymentKey** | **String**|  | [optional] |
| **appVersion** | **String**|  | [optional] |
| **packageHash** | **String**|  | [optional] |
| **label** | **String**|  | [optional] |
| **clientUniqueId** | **String**|  | [optional] |
| **isCompanion** | **String**|  | [optional] |

### Return type

[**LegacyCodePushAcquisitionUpdateCheck200Response**](LegacyCodePushAcquisitionUpdateCheck200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="legacyCodePushAcquisitionUpdateDownloadStatus"></a>
# **legacyCodePushAcquisitionUpdateDownloadStatus**
> legacyCodePushAcquisitionUpdateDownloadStatus(legacyCodePushAcquisitionUpdateInstallsStatusRequest)



Report download of specified release

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CodepushApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CodepushApi apiInstance = new CodepushApi(defaultClient);
    LegacyCodePushAcquisitionUpdateInstallsStatusRequest legacyCodePushAcquisitionUpdateInstallsStatusRequest = new LegacyCodePushAcquisitionUpdateInstallsStatusRequest(); // LegacyCodePushAcquisitionUpdateInstallsStatusRequest | Deployment status metric properties
    try {
      apiInstance.legacyCodePushAcquisitionUpdateDownloadStatus(legacyCodePushAcquisitionUpdateInstallsStatusRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling CodepushApi#legacyCodePushAcquisitionUpdateDownloadStatus");
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
| **legacyCodePushAcquisitionUpdateInstallsStatusRequest** | [**LegacyCodePushAcquisitionUpdateInstallsStatusRequest**](LegacyCodePushAcquisitionUpdateInstallsStatusRequest.md)| Deployment status metric properties | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="legacyCodePushAcquisitionUpdateInstallsStatus"></a>
# **legacyCodePushAcquisitionUpdateInstallsStatus**
> legacyCodePushAcquisitionUpdateInstallsStatus(legacyCodePushAcquisitionUpdateInstallsStatusRequest)



Report deploy of specified release

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CodepushApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CodepushApi apiInstance = new CodepushApi(defaultClient);
    LegacyCodePushAcquisitionUpdateInstallsStatusRequest legacyCodePushAcquisitionUpdateInstallsStatusRequest = new LegacyCodePushAcquisitionUpdateInstallsStatusRequest(); // LegacyCodePushAcquisitionUpdateInstallsStatusRequest | Deployment status metric properties
    try {
      apiInstance.legacyCodePushAcquisitionUpdateInstallsStatus(legacyCodePushAcquisitionUpdateInstallsStatusRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling CodepushApi#legacyCodePushAcquisitionUpdateInstallsStatus");
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
| **legacyCodePushAcquisitionUpdateInstallsStatusRequest** | [**LegacyCodePushAcquisitionUpdateInstallsStatusRequest**](LegacyCodePushAcquisitionUpdateInstallsStatusRequest.md)| Deployment status metric properties | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

