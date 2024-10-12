# ProjectApi

All URIs are relative to *https://ci.appveyor.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addProject**](ProjectApi.md#addProject) | **POST** /projects | Add project |
| [**deleteProject**](ProjectApi.md#deleteProject) | **DELETE** /projects/{accountName}/{projectSlug} | Delete project |
| [**deleteProjectBuildCache**](ProjectApi.md#deleteProjectBuildCache) | **DELETE** /projects/{accountName}/{projectSlug}/buildcache | Delete project build cache |
| [**encryptValue**](ProjectApi.md#encryptValue) | **POST** /account/encrypt | Encrypt a value for use in StoredValue. |
| [**getProjectArtifact**](ProjectApi.md#getProjectArtifact) | **GET** /projects/{accountName}/{projectSlug}/artifacts/{artifactFileName} | Get last successful build artifact |
| [**getProjectBranchStatusBadge**](ProjectApi.md#getProjectBranchStatusBadge) | **GET** /projects/status/{statusBadgeId}/branch/{buildBranch} | Get project branch status badge image |
| [**getProjectBuildByVersion**](ProjectApi.md#getProjectBuildByVersion) | **GET** /projects/{accountName}/{projectSlug}/build/{buildVersion} | Get project build by version |
| [**getProjectDeployments**](ProjectApi.md#getProjectDeployments) | **GET** /projects/{accountName}/{projectSlug}/deployments | Get project deployments |
| [**getProjectEnvironmentVariables**](ProjectApi.md#getProjectEnvironmentVariables) | **GET** /projects/{accountName}/{projectSlug}/settings/environment-variables | Get project environment variables |
| [**getProjectHistory**](ProjectApi.md#getProjectHistory) | **GET** /projects/{accountName}/{projectSlug}/history | Get project history |
| [**getProjectLastBuild**](ProjectApi.md#getProjectLastBuild) | **GET** /projects/{accountName}/{projectSlug} | Get project last build |
| [**getProjectLastBuildBranch**](ProjectApi.md#getProjectLastBuildBranch) | **GET** /projects/{accountName}/{projectSlug}/branch/{buildBranch} | Get project last branch build |
| [**getProjectSettings**](ProjectApi.md#getProjectSettings) | **GET** /projects/{accountName}/{projectSlug}/settings | Get project settings |
| [**getProjectSettingsYaml**](ProjectApi.md#getProjectSettingsYaml) | **GET** /projects/{accountName}/{projectSlug}/settings/yaml | Get project settings in YAML |
| [**getProjectStatusBadge**](ProjectApi.md#getProjectStatusBadge) | **GET** /projects/status/{statusBadgeId} | Get project status badge image |
| [**getProjects**](ProjectApi.md#getProjects) | **GET** /projects | Get projects |
| [**getPublicProjectStatusBadge**](ProjectApi.md#getPublicProjectStatusBadge) | **GET** /projects/status/{badgeRepoProvider}/{repoAccountName}/{repoSlug} | Get status badge image for a project with a public repository |
| [**updateProject**](ProjectApi.md#updateProject) | **PUT** /projects | Update project |
| [**updateProjectBuildNumber**](ProjectApi.md#updateProjectBuildNumber) | **PUT** /projects/{accountName}/{projectSlug}/settings/build-number | Update project build number |
| [**updateProjectEnvironmentVariables**](ProjectApi.md#updateProjectEnvironmentVariables) | **PUT** /projects/{accountName}/{projectSlug}/settings/environment-variables | Update project environment variables |
| [**updateProjectSettingsYaml**](ProjectApi.md#updateProjectSettingsYaml) | **PUT** /projects/{accountName}/{projectSlug}/settings/yaml | Update project settings in YAML |


<a id="addProject"></a>
# **addProject**
> Project addProject(body)

Add project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ci.appveyor.com/api");
    
    // Configure API key authorization: apiToken
    ApiKeyAuth apiToken = (ApiKeyAuth) defaultClient.getAuthentication("apiToken");
    apiToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiToken.setApiKeyPrefix("Token");

    ProjectApi apiInstance = new ProjectApi(defaultClient);
    ProjectAddition body = new ProjectAddition(); // ProjectAddition | 
    try {
      Project result = apiInstance.addProject(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApi#addProject");
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
| **body** | [**ProjectAddition**](ProjectAddition.md)|  | |

### Return type

[**Project**](Project.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="deleteProject"></a>
# **deleteProject**
> deleteProject(accountName, projectSlug)

Delete project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ci.appveyor.com/api");
    
    // Configure API key authorization: apiToken
    ApiKeyAuth apiToken = (ApiKeyAuth) defaultClient.getAuthentication("apiToken");
    apiToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiToken.setApiKeyPrefix("Token");

    ProjectApi apiInstance = new ProjectApi(defaultClient);
    String accountName = "accountName_example"; // String | AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the `accountName` property of `UserAccount`.
    String projectSlug = "projectSlug_example"; // String | Project Slug
    try {
      apiInstance.deleteProject(accountName, projectSlug);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApi#deleteProject");
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
| **accountName** | **String**| AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;. | |
| **projectSlug** | **String**| Project Slug | |

### Return type

null (empty response body)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **0** | Error |  -  |

<a id="deleteProjectBuildCache"></a>
# **deleteProjectBuildCache**
> deleteProjectBuildCache(accountName, projectSlug)

Delete project build cache

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ci.appveyor.com/api");
    
    // Configure API key authorization: apiToken
    ApiKeyAuth apiToken = (ApiKeyAuth) defaultClient.getAuthentication("apiToken");
    apiToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiToken.setApiKeyPrefix("Token");

    ProjectApi apiInstance = new ProjectApi(defaultClient);
    String accountName = "accountName_example"; // String | AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the `accountName` property of `UserAccount`.
    String projectSlug = "projectSlug_example"; // String | Project Slug
    try {
      apiInstance.deleteProjectBuildCache(accountName, projectSlug);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApi#deleteProjectBuildCache");
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
| **accountName** | **String**| AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;. | |
| **projectSlug** | **String**| Project Slug | |

### Return type

null (empty response body)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **0** | Error |  -  |

<a id="encryptValue"></a>
# **encryptValue**
> String encryptValue(body)

Encrypt a value for use in StoredValue.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ci.appveyor.com/api");
    
    // Configure API key authorization: apiToken
    ApiKeyAuth apiToken = (ApiKeyAuth) defaultClient.getAuthentication("apiToken");
    apiToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiToken.setApiKeyPrefix("Token");

    ProjectApi apiInstance = new ProjectApi(defaultClient);
    EncryptRequest body = new EncryptRequest(); // EncryptRequest | 
    try {
      String result = apiInstance.encryptValue(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApi#encryptValue");
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
| **body** | [**EncryptRequest**](EncryptRequest.md)|  | |

### Return type

**String**

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="getProjectArtifact"></a>
# **getProjectArtifact**
> File getProjectArtifact(accountName, projectSlug, artifactFileName, branch, tag, job, all, pr)

Get last successful build artifact

The &#x60;job&#x60; parameter is mandatory if the build contains multiple jobs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ci.appveyor.com/api");

    ProjectApi apiInstance = new ProjectApi(defaultClient);
    String accountName = "accountName_example"; // String | AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the `accountName` property of `UserAccount`.
    String projectSlug = "projectSlug_example"; // String | Project Slug
    String artifactFileName = "artifactFileName_example"; // String | File name (or path) of a build artifact file. Corresponds to the `fileName` property of `ArtifactModel`. URL-encoding of slashes in parameter values is optional.
    String branch = "branch_example"; // String | Repository Branch
    String tag = "tag_example"; // String | A git (or other VCS) tag
    String job = "job_example"; // String | Name of the build job.
    Boolean all = false; // Boolean | Include not only `successful`, but also jobs with `failed`, and `cancelled` status.
    Boolean pr = true; // Boolean | Include PR builds in the search results? `true` - take artifact from PR builds only; `false` - do not look for artifact in PR builds; default/unspecified - look for artifact in both PR an non-PR builds. 
    try {
      File result = apiInstance.getProjectArtifact(accountName, projectSlug, artifactFileName, branch, tag, job, all, pr);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApi#getProjectArtifact");
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
| **accountName** | **String**| AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;. | |
| **projectSlug** | **String**| Project Slug | |
| **artifactFileName** | **String**| File name (or path) of a build artifact file. Corresponds to the &#x60;fileName&#x60; property of &#x60;ArtifactModel&#x60;. URL-encoding of slashes in parameter values is optional. | |
| **branch** | **String**| Repository Branch | [optional] |
| **tag** | **String**| A git (or other VCS) tag | [optional] |
| **job** | **String**| Name of the build job. | [optional] |
| **all** | **Boolean**| Include not only &#x60;successful&#x60;, but also jobs with &#x60;failed&#x60;, and &#x60;cancelled&#x60; status. | [optional] [default to false] |
| **pr** | **Boolean**| Include PR builds in the search results? &#x60;true&#x60; - take artifact from PR builds only; &#x60;false&#x60; - do not look for artifact in PR builds; default/unspecified - look for artifact in both PR an non-PR builds.  | [optional] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="getProjectBranchStatusBadge"></a>
# **getProjectBranchStatusBadge**
> File getProjectBranchStatusBadge(statusBadgeId, buildBranch, svg, retina, passingText, failingText, pendingText)

Get project branch status badge image

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ci.appveyor.com/api");

    ProjectApi apiInstance = new ProjectApi(defaultClient);
    String statusBadgeId = "statusBadgeId_example"; // String | ID of the status badge (`statusBadgeId` from `ProjectWithConfiguration`).
    String buildBranch = "buildBranch_example"; // String | Build Branch
    Boolean svg = false; // Boolean | Return an SVG image instead of PNG?  Exclusive with `retina`.
    Boolean retina = false; // Boolean | Return a larger image suitable for retina displays?  Exclusive with `svg`.
    String passingText = "passingText_example"; // String | Text to show in badge when build is passing.
    String failingText = "failingText_example"; // String | Text to show in badge when build is failing.
    String pendingText = "pendingText_example"; // String | Text to show in badge when build is pending.
    try {
      File result = apiInstance.getProjectBranchStatusBadge(statusBadgeId, buildBranch, svg, retina, passingText, failingText, pendingText);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApi#getProjectBranchStatusBadge");
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
| **statusBadgeId** | **String**| ID of the status badge (&#x60;statusBadgeId&#x60; from &#x60;ProjectWithConfiguration&#x60;). | |
| **buildBranch** | **String**| Build Branch | |
| **svg** | **Boolean**| Return an SVG image instead of PNG?  Exclusive with &#x60;retina&#x60;. | [optional] [default to false] |
| **retina** | **Boolean**| Return a larger image suitable for retina displays?  Exclusive with &#x60;svg&#x60;. | [optional] [default to false] |
| **passingText** | **String**| Text to show in badge when build is passing. | [optional] |
| **failingText** | **String**| Text to show in badge when build is failing. | [optional] |
| **pendingText** | **String**| Text to show in badge when build is pending. | [optional] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/svg+xml, image/png

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="getProjectBuildByVersion"></a>
# **getProjectBuildByVersion**
> ProjectBuildResults getProjectBuildByVersion(accountName, projectSlug, buildVersion)

Get project build by version

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ci.appveyor.com/api");

    ProjectApi apiInstance = new ProjectApi(defaultClient);
    String accountName = "accountName_example"; // String | AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the `accountName` property of `UserAccount`.
    String projectSlug = "projectSlug_example"; // String | Project Slug
    String buildVersion = "buildVersion_example"; // String | Build Version (`version` property of `Build`)
    try {
      ProjectBuildResults result = apiInstance.getProjectBuildByVersion(accountName, projectSlug, buildVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApi#getProjectBuildByVersion");
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
| **accountName** | **String**| AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;. | |
| **projectSlug** | **String**| Project Slug | |
| **buildVersion** | **String**| Build Version (&#x60;version&#x60; property of &#x60;Build&#x60;) | |

### Return type

[**ProjectBuildResults**](ProjectBuildResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="getProjectDeployments"></a>
# **getProjectDeployments**
> ProjectDeploymentsResults getProjectDeployments(accountName, projectSlug, recordsNumber)

Get project deployments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ci.appveyor.com/api");
    
    // Configure API key authorization: apiToken
    ApiKeyAuth apiToken = (ApiKeyAuth) defaultClient.getAuthentication("apiToken");
    apiToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiToken.setApiKeyPrefix("Token");

    ProjectApi apiInstance = new ProjectApi(defaultClient);
    String accountName = "accountName_example"; // String | AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the `accountName` property of `UserAccount`.
    String projectSlug = "projectSlug_example"; // String | Project Slug
    Integer recordsNumber = 56; // Integer | Number of results to include in the response. getProjectDeployments is documented to have a maximum of 20. It currently returns 500 Internal Server Error for recordsNumber <= 5. In the past it has returned 500 Internal Server Error for many different values which did not match the value used by the ci.appveyor.com web interface at the time.  As of 2018-09-08, the value used by the web interface is 10.
    try {
      ProjectDeploymentsResults result = apiInstance.getProjectDeployments(accountName, projectSlug, recordsNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApi#getProjectDeployments");
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
| **accountName** | **String**| AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;. | |
| **projectSlug** | **String**| Project Slug | |
| **recordsNumber** | **Integer**| Number of results to include in the response. getProjectDeployments is documented to have a maximum of 20. It currently returns 500 Internal Server Error for recordsNumber &lt;&#x3D; 5. In the past it has returned 500 Internal Server Error for many different values which did not match the value used by the ci.appveyor.com web interface at the time.  As of 2018-09-08, the value used by the web interface is 10. | |

### Return type

[**ProjectDeploymentsResults**](ProjectDeploymentsResults.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="getProjectEnvironmentVariables"></a>
# **getProjectEnvironmentVariables**
> List&lt;StoredNameValue&gt; getProjectEnvironmentVariables(accountName, projectSlug)

Get project environment variables

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ci.appveyor.com/api");
    
    // Configure API key authorization: apiToken
    ApiKeyAuth apiToken = (ApiKeyAuth) defaultClient.getAuthentication("apiToken");
    apiToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiToken.setApiKeyPrefix("Token");

    ProjectApi apiInstance = new ProjectApi(defaultClient);
    String accountName = "accountName_example"; // String | AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the `accountName` property of `UserAccount`.
    String projectSlug = "projectSlug_example"; // String | Project Slug
    try {
      List<StoredNameValue> result = apiInstance.getProjectEnvironmentVariables(accountName, projectSlug);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApi#getProjectEnvironmentVariables");
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
| **accountName** | **String**| AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;. | |
| **projectSlug** | **String**| Project Slug | |

### Return type

[**List&lt;StoredNameValue&gt;**](StoredNameValue.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="getProjectHistory"></a>
# **getProjectHistory**
> ProjectHistory getProjectHistory(accountName, projectSlug, recordsNumber, startBuildId, branch)

Get project history

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ci.appveyor.com/api");

    ProjectApi apiInstance = new ProjectApi(defaultClient);
    String accountName = "accountName_example"; // String | AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the `accountName` property of `UserAccount`.
    String projectSlug = "projectSlug_example"; // String | Project Slug
    Integer recordsNumber = 56; // Integer | Number of results to include in the response. getProjectDeployments is documented to have a maximum of 20. It currently returns 500 Internal Server Error for recordsNumber <= 5. In the past it has returned 500 Internal Server Error for many different values which did not match the value used by the ci.appveyor.com web interface at the time.  As of 2018-09-08, the value used by the web interface is 10.
    Integer startBuildId = 56; // Integer | Maximum `buildId` to include in the results (exclusive).
    String branch = "branch_example"; // String | Repository Branch
    try {
      ProjectHistory result = apiInstance.getProjectHistory(accountName, projectSlug, recordsNumber, startBuildId, branch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApi#getProjectHistory");
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
| **accountName** | **String**| AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;. | |
| **projectSlug** | **String**| Project Slug | |
| **recordsNumber** | **Integer**| Number of results to include in the response. getProjectDeployments is documented to have a maximum of 20. It currently returns 500 Internal Server Error for recordsNumber &lt;&#x3D; 5. In the past it has returned 500 Internal Server Error for many different values which did not match the value used by the ci.appveyor.com web interface at the time.  As of 2018-09-08, the value used by the web interface is 10. | |
| **startBuildId** | **Integer**| Maximum &#x60;buildId&#x60; to include in the results (exclusive). | [optional] |
| **branch** | **String**| Repository Branch | [optional] |

### Return type

[**ProjectHistory**](ProjectHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="getProjectLastBuild"></a>
# **getProjectLastBuild**
> ProjectBuildResults getProjectLastBuild(accountName, projectSlug)

Get project last build

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ci.appveyor.com/api");

    ProjectApi apiInstance = new ProjectApi(defaultClient);
    String accountName = "accountName_example"; // String | AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the `accountName` property of `UserAccount`.
    String projectSlug = "projectSlug_example"; // String | Project Slug
    try {
      ProjectBuildResults result = apiInstance.getProjectLastBuild(accountName, projectSlug);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApi#getProjectLastBuild");
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
| **accountName** | **String**| AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;. | |
| **projectSlug** | **String**| Project Slug | |

### Return type

[**ProjectBuildResults**](ProjectBuildResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="getProjectLastBuildBranch"></a>
# **getProjectLastBuildBranch**
> ProjectBuildResults getProjectLastBuildBranch(accountName, projectSlug, buildBranch)

Get project last branch build

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ci.appveyor.com/api");

    ProjectApi apiInstance = new ProjectApi(defaultClient);
    String accountName = "accountName_example"; // String | AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the `accountName` property of `UserAccount`.
    String projectSlug = "projectSlug_example"; // String | Project Slug
    String buildBranch = "buildBranch_example"; // String | Build Branch
    try {
      ProjectBuildResults result = apiInstance.getProjectLastBuildBranch(accountName, projectSlug, buildBranch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApi#getProjectLastBuildBranch");
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
| **accountName** | **String**| AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;. | |
| **projectSlug** | **String**| Project Slug | |
| **buildBranch** | **String**| Build Branch | |

### Return type

[**ProjectBuildResults**](ProjectBuildResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="getProjectSettings"></a>
# **getProjectSettings**
> ProjectSettingsResults getProjectSettings(accountName, projectSlug)

Get project settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ci.appveyor.com/api");
    
    // Configure API key authorization: apiToken
    ApiKeyAuth apiToken = (ApiKeyAuth) defaultClient.getAuthentication("apiToken");
    apiToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiToken.setApiKeyPrefix("Token");

    ProjectApi apiInstance = new ProjectApi(defaultClient);
    String accountName = "accountName_example"; // String | AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the `accountName` property of `UserAccount`.
    String projectSlug = "projectSlug_example"; // String | Project Slug
    try {
      ProjectSettingsResults result = apiInstance.getProjectSettings(accountName, projectSlug);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApi#getProjectSettings");
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
| **accountName** | **String**| AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;. | |
| **projectSlug** | **String**| Project Slug | |

### Return type

[**ProjectSettingsResults**](ProjectSettingsResults.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="getProjectSettingsYaml"></a>
# **getProjectSettingsYaml**
> String getProjectSettingsYaml(accountName, projectSlug)

Get project settings in YAML

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ci.appveyor.com/api");
    
    // Configure API key authorization: apiToken
    ApiKeyAuth apiToken = (ApiKeyAuth) defaultClient.getAuthentication("apiToken");
    apiToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiToken.setApiKeyPrefix("Token");

    ProjectApi apiInstance = new ProjectApi(defaultClient);
    String accountName = "accountName_example"; // String | AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the `accountName` property of `UserAccount`.
    String projectSlug = "projectSlug_example"; // String | Project Slug
    try {
      String result = apiInstance.getProjectSettingsYaml(accountName, projectSlug);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApi#getProjectSettingsYaml");
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
| **accountName** | **String**| AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;. | |
| **projectSlug** | **String**| Project Slug | |

### Return type

**String**

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success  The schema type of this response could be specified as &#x60;file&#x60; to denote opaque binary data.  The generated Java code for &#x60;file&#x60; saves the response as a temporary file, making it a little more difficult to use and less efficient for common cases.  If &#x60;string&#x60; causes problems for other generators, can switch to &#x60;file&#x60; type.  |  -  |
| **0** | Error |  -  |

<a id="getProjectStatusBadge"></a>
# **getProjectStatusBadge**
> File getProjectStatusBadge(statusBadgeId, svg, retina, passingText, failingText, pendingText)

Get project status badge image

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ci.appveyor.com/api");

    ProjectApi apiInstance = new ProjectApi(defaultClient);
    String statusBadgeId = "statusBadgeId_example"; // String | ID of the status badge (`statusBadgeId` from `ProjectWithConfiguration`).
    Boolean svg = false; // Boolean | Return an SVG image instead of PNG?  Exclusive with `retina`.
    Boolean retina = false; // Boolean | Return a larger image suitable for retina displays?  Exclusive with `svg`.
    String passingText = "passingText_example"; // String | Text to show in badge when build is passing.
    String failingText = "failingText_example"; // String | Text to show in badge when build is failing.
    String pendingText = "pendingText_example"; // String | Text to show in badge when build is pending.
    try {
      File result = apiInstance.getProjectStatusBadge(statusBadgeId, svg, retina, passingText, failingText, pendingText);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApi#getProjectStatusBadge");
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
| **statusBadgeId** | **String**| ID of the status badge (&#x60;statusBadgeId&#x60; from &#x60;ProjectWithConfiguration&#x60;). | |
| **svg** | **Boolean**| Return an SVG image instead of PNG?  Exclusive with &#x60;retina&#x60;. | [optional] [default to false] |
| **retina** | **Boolean**| Return a larger image suitable for retina displays?  Exclusive with &#x60;svg&#x60;. | [optional] [default to false] |
| **passingText** | **String**| Text to show in badge when build is passing. | [optional] |
| **failingText** | **String**| Text to show in badge when build is failing. | [optional] |
| **pendingText** | **String**| Text to show in badge when build is pending. | [optional] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/svg+xml, image/png

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="getProjects"></a>
# **getProjects**
> List&lt;Project&gt; getProjects()

Get projects

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ci.appveyor.com/api");
    
    // Configure API key authorization: apiToken
    ApiKeyAuth apiToken = (ApiKeyAuth) defaultClient.getAuthentication("apiToken");
    apiToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiToken.setApiKeyPrefix("Token");

    ProjectApi apiInstance = new ProjectApi(defaultClient);
    try {
      List<Project> result = apiInstance.getProjects();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApi#getProjects");
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

[**List&lt;Project&gt;**](Project.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="getPublicProjectStatusBadge"></a>
# **getPublicProjectStatusBadge**
> File getPublicProjectStatusBadge(badgeRepoProvider, repoAccountName, repoSlug, branch, svg, retina, passingText, failingText, pendingText)

Get status badge image for a project with a public repository

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ci.appveyor.com/api");

    ProjectApi apiInstance = new ProjectApi(defaultClient);
    String badgeRepoProvider = "bitBucket"; // String | Repository provider supported for badges
    String repoAccountName = "repoAccountName_example"; // String | Account name with repository provider
    String repoSlug = "repoSlug_example"; // String | Slug (URL component) of repository.
    String branch = "branch_example"; // String | Repository Branch
    Boolean svg = false; // Boolean | Return an SVG image instead of PNG?  Exclusive with `retina`.
    Boolean retina = false; // Boolean | Return a larger image suitable for retina displays?  Exclusive with `svg`.
    String passingText = "passingText_example"; // String | Text to show in badge when build is passing.
    String failingText = "failingText_example"; // String | Text to show in badge when build is failing.
    String pendingText = "pendingText_example"; // String | Text to show in badge when build is pending.
    try {
      File result = apiInstance.getPublicProjectStatusBadge(badgeRepoProvider, repoAccountName, repoSlug, branch, svg, retina, passingText, failingText, pendingText);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApi#getPublicProjectStatusBadge");
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
| **badgeRepoProvider** | **String**| Repository provider supported for badges | [enum: bitBucket, gitHub] |
| **repoAccountName** | **String**| Account name with repository provider | |
| **repoSlug** | **String**| Slug (URL component) of repository. | |
| **branch** | **String**| Repository Branch | [optional] |
| **svg** | **Boolean**| Return an SVG image instead of PNG?  Exclusive with &#x60;retina&#x60;. | [optional] [default to false] |
| **retina** | **Boolean**| Return a larger image suitable for retina displays?  Exclusive with &#x60;svg&#x60;. | [optional] [default to false] |
| **passingText** | **String**| Text to show in badge when build is passing. | [optional] |
| **failingText** | **String**| Text to show in badge when build is failing. | [optional] |
| **pendingText** | **String**| Text to show in badge when build is pending. | [optional] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/svg+xml, image/png

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="updateProject"></a>
# **updateProject**
> updateProject(body)

Update project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ci.appveyor.com/api");
    
    // Configure API key authorization: apiToken
    ApiKeyAuth apiToken = (ApiKeyAuth) defaultClient.getAuthentication("apiToken");
    apiToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiToken.setApiKeyPrefix("Token");

    ProjectApi apiInstance = new ProjectApi(defaultClient);
    ProjectWithConfiguration body = new ProjectWithConfiguration(); // ProjectWithConfiguration | 
    try {
      apiInstance.updateProject(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApi#updateProject");
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
| **body** | [**ProjectWithConfiguration**](ProjectWithConfiguration.md)|  | |

### Return type

null (empty response body)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **0** | Error |  -  |

<a id="updateProjectBuildNumber"></a>
# **updateProjectBuildNumber**
> updateProjectBuildNumber(accountName, projectSlug, body)

Update project build number

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ci.appveyor.com/api");
    
    // Configure API key authorization: apiToken
    ApiKeyAuth apiToken = (ApiKeyAuth) defaultClient.getAuthentication("apiToken");
    apiToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiToken.setApiKeyPrefix("Token");

    ProjectApi apiInstance = new ProjectApi(defaultClient);
    String accountName = "accountName_example"; // String | AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the `accountName` property of `UserAccount`.
    String projectSlug = "projectSlug_example"; // String | Project Slug
    ProjectBuildNumberUpdate body = new ProjectBuildNumberUpdate(); // ProjectBuildNumberUpdate | 
    try {
      apiInstance.updateProjectBuildNumber(accountName, projectSlug, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApi#updateProjectBuildNumber");
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
| **accountName** | **String**| AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;. | |
| **projectSlug** | **String**| Project Slug | |
| **body** | [**ProjectBuildNumberUpdate**](ProjectBuildNumberUpdate.md)|  | |

### Return type

null (empty response body)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **0** | Error |  -  |

<a id="updateProjectEnvironmentVariables"></a>
# **updateProjectEnvironmentVariables**
> updateProjectEnvironmentVariables(accountName, projectSlug, body)

Update project environment variables

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ci.appveyor.com/api");
    
    // Configure API key authorization: apiToken
    ApiKeyAuth apiToken = (ApiKeyAuth) defaultClient.getAuthentication("apiToken");
    apiToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiToken.setApiKeyPrefix("Token");

    ProjectApi apiInstance = new ProjectApi(defaultClient);
    String accountName = "accountName_example"; // String | AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the `accountName` property of `UserAccount`.
    String projectSlug = "projectSlug_example"; // String | Project Slug
    List<StoredNameValue> body = Arrays.asList(); // List<StoredNameValue> | 
    try {
      apiInstance.updateProjectEnvironmentVariables(accountName, projectSlug, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApi#updateProjectEnvironmentVariables");
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
| **accountName** | **String**| AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;. | |
| **projectSlug** | **String**| Project Slug | |
| **body** | [**List&lt;StoredNameValue&gt;**](StoredNameValue.md)|  | |

### Return type

null (empty response body)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **0** | Error |  -  |

<a id="updateProjectSettingsYaml"></a>
# **updateProjectSettingsYaml**
> updateProjectSettingsYaml(accountName, projectSlug, body)

Update project settings in YAML

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ci.appveyor.com/api");
    
    // Configure API key authorization: apiToken
    ApiKeyAuth apiToken = (ApiKeyAuth) defaultClient.getAuthentication("apiToken");
    apiToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiToken.setApiKeyPrefix("Token");

    ProjectApi apiInstance = new ProjectApi(defaultClient);
    String accountName = "accountName_example"; // String | AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the `accountName` property of `UserAccount`.
    String projectSlug = "projectSlug_example"; // String | Project Slug
    File body = new File("/path/to/file"); // File | The body of requests should contain YAML data.  It is unclear how to specify this since the OpenAPI spec requires `schema` without `type` for `in: body` parameters and does not allow `type: file` in `schema`.  See https://github.com/OAI/OpenAPI-Specification/issues/326 swagger-codegen (for Java, probably others) allows a binary string body parameter with non-application/json `consumes` to be passed through in the request body without conversion to JSON. 
    try {
      apiInstance.updateProjectSettingsYaml(accountName, projectSlug, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectApi#updateProjectSettingsYaml");
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
| **accountName** | **String**| AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;. | |
| **projectSlug** | **String**| Project Slug | |
| **body** | **File**| The body of requests should contain YAML data.  It is unclear how to specify this since the OpenAPI spec requires &#x60;schema&#x60; without &#x60;type&#x60; for &#x60;in: body&#x60; parameters and does not allow &#x60;type: file&#x60; in &#x60;schema&#x60;.  See https://github.com/OAI/OpenAPI-Specification/issues/326 swagger-codegen (for Java, probably others) allows a binary string body parameter with non-application/json &#x60;consumes&#x60; to be passed through in the request body without conversion to JSON.  | |

### Return type

null (empty response body)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **0** | Error |  -  |

