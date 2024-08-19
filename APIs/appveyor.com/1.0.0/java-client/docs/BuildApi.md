# BuildApi

All URIs are relative to *https://ci.appveyor.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelBuild**](BuildApi.md#cancelBuild) | **DELETE** /builds/{accountName}/{projectSlug}/{buildVersion} | Cancel build |
| [**getBuildArtifact**](BuildApi.md#getBuildArtifact) | **GET** /buildjobs/{jobId}/artifacts/{artifactFileName} | Download build artifact |
| [**getBuildArtifacts**](BuildApi.md#getBuildArtifacts) | **GET** /buildjobs/{jobId}/artifacts | Get build artifacts |
| [**getBuildLog**](BuildApi.md#getBuildLog) | **GET** /buildjobs/{jobId}/log | Download build log |
| [**reRunBuild**](BuildApi.md#reRunBuild) | **PUT** /builds | Re-run build |
| [**startBuild**](BuildApi.md#startBuild) | **POST** /builds | Start build of branch most recent commit |


<a id="cancelBuild"></a>
# **cancelBuild**
> cancelBuild(accountName, projectSlug, buildVersion)

Cancel build

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ci.appveyor.com/api");
    
    // Configure API key authorization: apiToken
    ApiKeyAuth apiToken = (ApiKeyAuth) defaultClient.getAuthentication("apiToken");
    apiToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiToken.setApiKeyPrefix("Token");

    BuildApi apiInstance = new BuildApi(defaultClient);
    String accountName = "accountName_example"; // String | AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the `accountName` property of `UserAccount`.
    String projectSlug = "projectSlug_example"; // String | Project Slug
    String buildVersion = "buildVersion_example"; // String | Build Version (`version` property of `Build`)
    try {
      apiInstance.cancelBuild(accountName, projectSlug, buildVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildApi#cancelBuild");
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

<a id="getBuildArtifact"></a>
# **getBuildArtifact**
> File getBuildArtifact(jobId, artifactFileName)

Download build artifact

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ci.appveyor.com/api");

    BuildApi apiInstance = new BuildApi(defaultClient);
    String jobId = "jobId_example"; // String | Build ID (`jobId` property of `BuildJob`)
    String artifactFileName = "artifactFileName_example"; // String | File name (or path) of a build artifact file. Corresponds to the `fileName` property of `ArtifactModel`. URL-encoding of slashes in parameter values is optional.
    try {
      File result = apiInstance.getBuildArtifact(jobId, artifactFileName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildApi#getBuildArtifact");
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
| **jobId** | **String**| Build ID (&#x60;jobId&#x60; property of &#x60;BuildJob&#x60;) | |
| **artifactFileName** | **String**| File name (or path) of a build artifact file. Corresponds to the &#x60;fileName&#x60; property of &#x60;ArtifactModel&#x60;. URL-encoding of slashes in parameter values is optional. | |

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

<a id="getBuildArtifacts"></a>
# **getBuildArtifacts**
> List&lt;ArtifactModel&gt; getBuildArtifacts(jobId)

Get build artifacts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ci.appveyor.com/api");

    BuildApi apiInstance = new BuildApi(defaultClient);
    String jobId = "jobId_example"; // String | Build ID (`jobId` property of `BuildJob`)
    try {
      List<ArtifactModel> result = apiInstance.getBuildArtifacts(jobId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildApi#getBuildArtifacts");
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
| **jobId** | **String**| Build ID (&#x60;jobId&#x60; property of &#x60;BuildJob&#x60;) | |

### Return type

[**List&lt;ArtifactModel&gt;**](ArtifactModel.md)

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

<a id="getBuildLog"></a>
# **getBuildLog**
> File getBuildLog(jobId)

Download build log

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ci.appveyor.com/api");

    BuildApi apiInstance = new BuildApi(defaultClient);
    String jobId = "jobId_example"; // String | Build ID (`jobId` property of `BuildJob`)
    try {
      File result = apiInstance.getBuildLog(jobId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildApi#getBuildLog");
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
| **jobId** | **String**| Build ID (&#x60;jobId&#x60; property of &#x60;BuildJob&#x60;) | |

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
| **200** | Success. Note:  Response content is plain text sent with Content-Type application/octet-stream. |  -  |
| **0** | Error |  -  |

<a id="reRunBuild"></a>
# **reRunBuild**
> Build reRunBuild(body)

Re-run build

If &#x60;reRunIncomplete&#x60; is &#x60;true&#x60; and all jobs in the referenced build completed successfully, a 500 Internal Server Error is returned with the message \&quot;No failed or cancelled jobs in build with ID {buildId}\&quot;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ci.appveyor.com/api");
    
    // Configure API key authorization: apiToken
    ApiKeyAuth apiToken = (ApiKeyAuth) defaultClient.getAuthentication("apiToken");
    apiToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiToken.setApiKeyPrefix("Token");

    BuildApi apiInstance = new BuildApi(defaultClient);
    ReRunBuildRequest body = new ReRunBuildRequest(); // ReRunBuildRequest | 
    try {
      Build result = apiInstance.reRunBuild(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildApi#reRunBuild");
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
| **body** | [**ReRunBuildRequest**](ReRunBuildRequest.md)|  | |

### Return type

[**Build**](Build.md)

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

<a id="startBuild"></a>
# **startBuild**
> Build startBuild(body)

Start build of branch most recent commit

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ci.appveyor.com/api");
    
    // Configure API key authorization: apiToken
    ApiKeyAuth apiToken = (ApiKeyAuth) defaultClient.getAuthentication("apiToken");
    apiToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiToken.setApiKeyPrefix("Token");

    BuildApi apiInstance = new BuildApi(defaultClient);
    BuildStartRequest body = new BuildStartRequest(); // BuildStartRequest | 
    try {
      Build result = apiInstance.startBuild(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildApi#startBuild");
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
| **body** | [**BuildStartRequest**](BuildStartRequest.md)|  | |

### Return type

[**Build**](Build.md)

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

