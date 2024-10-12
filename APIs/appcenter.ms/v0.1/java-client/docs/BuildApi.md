# BuildApi

All URIs are relative to *https://api.appcenter.ms*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**branchConfigurationsCreate**](BuildApi.md#branchConfigurationsCreate) | **POST** /v0.1/apps/{owner_name}/{app_name}/branches/{branch}/config |  |
| [**branchConfigurationsDelete**](BuildApi.md#branchConfigurationsDelete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/branches/{branch}/config |  |
| [**branchConfigurationsGet**](BuildApi.md#branchConfigurationsGet) | **GET** /v0.1/apps/{owner_name}/{app_name}/branches/{branch}/config |  |
| [**branchConfigurationsUpdate**](BuildApi.md#branchConfigurationsUpdate) | **PUT** /v0.1/apps/{owner_name}/{app_name}/branches/{branch}/config |  |
| [**buildConfigurationsGet**](BuildApi.md#buildConfigurationsGet) | **GET** /v0.1/apps/{owner_name}/{app_name}/branches/{branch}/export_config |  |
| [**buildsCreate**](BuildApi.md#buildsCreate) | **POST** /v0.1/apps/{owner_name}/{app_name}/branches/{branch}/builds |  |
| [**buildsDistribute**](BuildApi.md#buildsDistribute) | **POST** /v0.1/apps/{owner_name}/{app_name}/builds/{build_id}/distribute |  |
| [**buildsGet**](BuildApi.md#buildsGet) | **GET** /v0.1/apps/{owner_name}/{app_name}/builds/{build_id} |  |
| [**buildsGetDownloadUri**](BuildApi.md#buildsGetDownloadUri) | **GET** /v0.1/apps/{owner_name}/{app_name}/builds/{build_id}/downloads/{download_type} |  |
| [**buildsGetLog**](BuildApi.md#buildsGetLog) | **GET** /v0.1/apps/{owner_name}/{app_name}/builds/{build_id}/logs |  |
| [**buildsGetStatusByAppId**](BuildApi.md#buildsGetStatusByAppId) | **GET** /v0.1/apps/{owner_name}/{app_name}/build_service_status |  |
| [**buildsListBranches**](BuildApi.md#buildsListBranches) | **GET** /v0.1/apps/{owner_name}/{app_name}/branches |  |
| [**buildsListByBranch**](BuildApi.md#buildsListByBranch) | **GET** /v0.1/apps/{owner_name}/{app_name}/branches/{branch}/builds |  |
| [**buildsListToolsetProjects**](BuildApi.md#buildsListToolsetProjects) | **GET** /v0.1/apps/{owner_name}/{app_name}/branches/{branch}/toolset_projects |  |
| [**buildsListToolsets**](BuildApi.md#buildsListToolsets) | **GET** /v0.1/apps/{owner_name}/{app_name}/toolsets |  |
| [**buildsListXamarinSDKBundles**](BuildApi.md#buildsListXamarinSDKBundles) | **GET** /v0.1/apps/{owner_name}/{app_name}/xamarin_sdk_bundles |  |
| [**buildsListXcodeVersions**](BuildApi.md#buildsListXcodeVersions) | **GET** /v0.1/apps/{owner_name}/{app_name}/xcode_versions |  |
| [**buildsUpdate**](BuildApi.md#buildsUpdate) | **PATCH** /v0.1/apps/{owner_name}/{app_name}/builds/{build_id} |  |
| [**buildsWebhook**](BuildApi.md#buildsWebhook) | **POST** /v0.1/public/hooks |  |
| [**commitsListByShaList**](BuildApi.md#commitsListByShaList) | **GET** /v0.1/apps/{owner_name}/{app_name}/commits/batch |  |
| [**fileAssetsCreate**](BuildApi.md#fileAssetsCreate) | **POST** /v0.1/apps/{owner_name}/{app_name}/file_asset |  |
| [**repositoriesList**](BuildApi.md#repositoriesList) | **GET** /v0.1/apps/{owner_name}/{app_name}/source_hosts/{source_host}/repositories |  |
| [**repositoryConfigurationsCreateOrUpdate**](BuildApi.md#repositoryConfigurationsCreateOrUpdate) | **POST** /v0.1/apps/{owner_name}/{app_name}/repo_config |  |
| [**repositoryConfigurationsDelete**](BuildApi.md#repositoryConfigurationsDelete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/repo_config |  |
| [**repositoryConfigurationsList**](BuildApi.md#repositoryConfigurationsList) | **GET** /v0.1/apps/{owner_name}/{app_name}/repo_config |  |


<a id="branchConfigurationsCreate"></a>
# **branchConfigurationsCreate**
> BranchConfigurationsGet200Response branchConfigurationsCreate(branch, ownerName, appName, branchConfigurationsUpdateRequest)



Configures the branch for build

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
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    BuildApi apiInstance = new BuildApi(defaultClient);
    String branch = "branch_example"; // String | The branch name
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    BranchConfigurationsUpdateRequest branchConfigurationsUpdateRequest = new BranchConfigurationsUpdateRequest(); // BranchConfigurationsUpdateRequest | Parameters of the configuration
    try {
      BranchConfigurationsGet200Response result = apiInstance.branchConfigurationsCreate(branch, ownerName, appName, branchConfigurationsUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildApi#branchConfigurationsCreate");
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
| **branch** | **String**| The branch name | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **branchConfigurationsUpdateRequest** | [**BranchConfigurationsUpdateRequest**](BranchConfigurationsUpdateRequest.md)| Parameters of the configuration | |

### Return type

[**BranchConfigurationsGet200Response**](BranchConfigurationsGet200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="branchConfigurationsDelete"></a>
# **branchConfigurationsDelete**
> BranchConfigurationsDelete200Response branchConfigurationsDelete(branch, ownerName, appName, body)



Deletes the branch build configuration

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
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    BuildApi apiInstance = new BuildApi(defaultClient);
    String branch = "branch_example"; // String | The branch name
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    Object body = null; // Object | 
    try {
      BranchConfigurationsDelete200Response result = apiInstance.branchConfigurationsDelete(branch, ownerName, appName, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildApi#branchConfigurationsDelete");
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
| **branch** | **String**| The branch name | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **body** | **Object**|  | [optional] |

### Return type

[**BranchConfigurationsDelete200Response**](BranchConfigurationsDelete200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="branchConfigurationsGet"></a>
# **branchConfigurationsGet**
> BranchConfigurationsGet200Response branchConfigurationsGet(branch, ownerName, appName)



Gets the branch configuration

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
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    BuildApi apiInstance = new BuildApi(defaultClient);
    String branch = "branch_example"; // String | The branch name
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      BranchConfigurationsGet200Response result = apiInstance.branchConfigurationsGet(branch, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildApi#branchConfigurationsGet");
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
| **branch** | **String**| The branch name | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**BranchConfigurationsGet200Response**](BranchConfigurationsGet200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Bad Request |  -  |

<a id="branchConfigurationsUpdate"></a>
# **branchConfigurationsUpdate**
> BranchConfigurationsGet200Response branchConfigurationsUpdate(branch, ownerName, appName, branchConfigurationsUpdateRequest)



Reconfigures the branch for build

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
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    BuildApi apiInstance = new BuildApi(defaultClient);
    String branch = "branch_example"; // String | The branch name
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    BranchConfigurationsUpdateRequest branchConfigurationsUpdateRequest = new BranchConfigurationsUpdateRequest(); // BranchConfigurationsUpdateRequest | Parameters of the configuration
    try {
      BranchConfigurationsGet200Response result = apiInstance.branchConfigurationsUpdate(branch, ownerName, appName, branchConfigurationsUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildApi#branchConfigurationsUpdate");
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
| **branch** | **String**| The branch name | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **branchConfigurationsUpdateRequest** | [**BranchConfigurationsUpdateRequest**](BranchConfigurationsUpdateRequest.md)| Parameters of the configuration | |

### Return type

[**BranchConfigurationsGet200Response**](BranchConfigurationsGet200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="buildConfigurationsGet"></a>
# **buildConfigurationsGet**
> BuildConfigurationsGet200Response buildConfigurationsGet(branch, ownerName, appName, format)



Gets the build configuration in Azure pipeline YAML format

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
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    BuildApi apiInstance = new BuildApi(defaultClient);
    String branch = "branch_example"; // String | The branch name
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    String format = "yaml"; // String | Configuration format
    try {
      BuildConfigurationsGet200Response result = apiInstance.buildConfigurationsGet(branch, ownerName, appName, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildApi#buildConfigurationsGet");
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
| **branch** | **String**| The branch name | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **format** | **String**| Configuration format | [optional] [default to yaml] [enum: yaml, json] |

### Return type

[**BuildConfigurationsGet200Response**](BuildConfigurationsGet200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Bad Request |  -  |

<a id="buildsCreate"></a>
# **buildsCreate**
> BuildsListBranches200ResponseInnerLastBuild buildsCreate(branch, ownerName, appName, buildsCreateRequest)



Create a build

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
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    BuildApi apiInstance = new BuildApi(defaultClient);
    String branch = "branch_example"; // String | The branch name
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    BuildsCreateRequest buildsCreateRequest = new BuildsCreateRequest(); // BuildsCreateRequest | Parameters of the build
    try {
      BuildsListBranches200ResponseInnerLastBuild result = apiInstance.buildsCreate(branch, ownerName, appName, buildsCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildApi#buildsCreate");
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
| **branch** | **String**| The branch name | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **buildsCreateRequest** | [**BuildsCreateRequest**](BuildsCreateRequest.md)| Parameters of the build | [optional] |

### Return type

[**BuildsListBranches200ResponseInnerLastBuild**](BuildsListBranches200ResponseInnerLastBuild.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Created build(s) |  -  |

<a id="buildsDistribute"></a>
# **buildsDistribute**
> BuildsDistribute200Response buildsDistribute(buildId, ownerName, appName, buildsDistributeRequest)



Distribute a build

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
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    BuildApi apiInstance = new BuildApi(defaultClient);
    Integer buildId = 56; // Integer | The build ID
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    BuildsDistributeRequest buildsDistributeRequest = new BuildsDistributeRequest(); // BuildsDistributeRequest | The distribution details
    try {
      BuildsDistribute200Response result = apiInstance.buildsDistribute(buildId, ownerName, appName, buildsDistributeRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildApi#buildsDistribute");
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
| **buildId** | **Integer**| The build ID | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **buildsDistributeRequest** | [**BuildsDistributeRequest**](BuildsDistributeRequest.md)| The distribution details | |

### Return type

[**BuildsDistribute200Response**](BuildsDistribute200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="buildsGet"></a>
# **buildsGet**
> BuildsListBranches200ResponseInnerLastBuild buildsGet(buildId, ownerName, appName)



Returns the build detail for the given build ID

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
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    BuildApi apiInstance = new BuildApi(defaultClient);
    Integer buildId = 56; // Integer | The build ID
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      BuildsListBranches200ResponseInnerLastBuild result = apiInstance.buildsGet(buildId, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildApi#buildsGet");
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
| **buildId** | **Integer**| The build ID | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**BuildsListBranches200ResponseInnerLastBuild**](BuildsListBranches200ResponseInnerLastBuild.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="buildsGetDownloadUri"></a>
# **buildsGetDownloadUri**
> BuildsGetDownloadUri200Response buildsGetDownloadUri(buildId, downloadType, ownerName, appName)



Gets the download URI

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
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    BuildApi apiInstance = new BuildApi(defaultClient);
    Integer buildId = 56; // Integer | The build ID
    String downloadType = "build"; // String | The download type
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      BuildsGetDownloadUri200Response result = apiInstance.buildsGetDownloadUri(buildId, downloadType, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildApi#buildsGetDownloadUri");
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
| **buildId** | **Integer**| The build ID | |
| **downloadType** | **String**| The download type | [enum: build, symbols, logs, mapping, bundle] |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**BuildsGetDownloadUri200Response**](BuildsGetDownloadUri200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="buildsGetLog"></a>
# **buildsGetLog**
> BuildsGetLog200Response buildsGetLog(buildId, ownerName, appName)



Get the build log

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
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    BuildApi apiInstance = new BuildApi(defaultClient);
    Integer buildId = 56; // Integer | The build ID
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      BuildsGetLog200Response result = apiInstance.buildsGetLog(buildId, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildApi#buildsGetLog");
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
| **buildId** | **Integer**| The build ID | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**BuildsGetLog200Response**](BuildsGetLog200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="buildsGetStatusByAppId"></a>
# **buildsGetStatusByAppId**
> BuildsGetStatusByAppId200Response buildsGetStatusByAppId(ownerName, appName)



Application specific build service status

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
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    BuildApi apiInstance = new BuildApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      BuildsGetStatusByAppId200Response result = apiInstance.buildsGetStatusByAppId(ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildApi#buildsGetStatusByAppId");
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

[**BuildsGetStatusByAppId200Response**](BuildsGetStatusByAppId200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. Availability for build service status is stored in response schema. |  -  |
| **0** | Bad Request |  -  |

<a id="buildsListBranches"></a>
# **buildsListBranches**
> List&lt;BuildsListBranches200ResponseInner&gt; buildsListBranches(ownerName, appName)



Returns the list of Git branches for this application

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
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    BuildApi apiInstance = new BuildApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      List<BuildsListBranches200ResponseInner> result = apiInstance.buildsListBranches(ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildApi#buildsListBranches");
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

[**List&lt;BuildsListBranches200ResponseInner&gt;**](BuildsListBranches200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Bad Request |  -  |

<a id="buildsListByBranch"></a>
# **buildsListByBranch**
> List&lt;BuildsListBranches200ResponseInnerLastBuild&gt; buildsListByBranch(branch, ownerName, appName)



Returns the list of builds for the branch

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
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    BuildApi apiInstance = new BuildApi(defaultClient);
    String branch = "branch_example"; // String | The branch name
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      List<BuildsListBranches200ResponseInnerLastBuild> result = apiInstance.buildsListByBranch(branch, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildApi#buildsListByBranch");
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
| **branch** | **String**| The branch name | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**List&lt;BuildsListBranches200ResponseInnerLastBuild&gt;**](BuildsListBranches200ResponseInnerLastBuild.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="buildsListToolsetProjects"></a>
# **buildsListToolsetProjects**
> BuildsListToolsetProjects200Response buildsListToolsetProjects(branch, os, platform, ownerName, appName, maxSearchDepth)



Returns the projects in the repository for the branch, for all toolsets

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
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    BuildApi apiInstance = new BuildApi(defaultClient);
    String branch = "branch_example"; // String | The branch name
    String os = "iOS"; // String | The desired OS for the project scan; normally the same as the app OS
    String platform = "Objective-C-Swift"; // String | The desired platform for the project scan
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    Integer maxSearchDepth = 56; // Integer | The depth of the repository to search for project files
    try {
      BuildsListToolsetProjects200Response result = apiInstance.buildsListToolsetProjects(branch, os, platform, ownerName, appName, maxSearchDepth);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildApi#buildsListToolsetProjects");
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
| **branch** | **String**| The branch name | |
| **os** | **String**| The desired OS for the project scan; normally the same as the app OS | [enum: iOS, Android, Windows, macOS] |
| **platform** | **String**| The desired platform for the project scan | [enum: Objective-C-Swift, React-Native, Xamarin, Java, UWP] |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **maxSearchDepth** | **Integer**| The depth of the repository to search for project files | [optional] |

### Return type

[**BuildsListToolsetProjects200Response**](BuildsListToolsetProjects200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="buildsListToolsets"></a>
# **buildsListToolsets**
> BuildsListToolsets200Response buildsListToolsets(ownerName, appName, tools)



Returns available toolsets for application

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
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    BuildApi apiInstance = new BuildApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    String tools = "xamarin"; // String | Toolset name
    try {
      BuildsListToolsets200Response result = apiInstance.buildsListToolsets(ownerName, appName, tools);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildApi#buildsListToolsets");
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
| **tools** | **String**| Toolset name | [optional] [enum: xamarin, xcode, node] |

### Return type

[**BuildsListToolsets200Response**](BuildsListToolsets200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Bad Request |  -  |

<a id="buildsListXamarinSDKBundles"></a>
# **buildsListXamarinSDKBundles**
> List&lt;BuildsListToolsets200ResponseXamarinInner&gt; buildsListXamarinSDKBundles(ownerName, appName)



Gets the Xamarin SDK bundles available to this app

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
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    BuildApi apiInstance = new BuildApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      List<BuildsListToolsets200ResponseXamarinInner> result = apiInstance.buildsListXamarinSDKBundles(ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildApi#buildsListXamarinSDKBundles");
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

[**List&lt;BuildsListToolsets200ResponseXamarinInner&gt;**](BuildsListToolsets200ResponseXamarinInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Bad Request |  -  |

<a id="buildsListXcodeVersions"></a>
# **buildsListXcodeVersions**
> List&lt;BuildsListToolsets200ResponseXcodeInner&gt; buildsListXcodeVersions(ownerName, appName)



Gets the Xcode versions available to this app

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
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    BuildApi apiInstance = new BuildApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      List<BuildsListToolsets200ResponseXcodeInner> result = apiInstance.buildsListXcodeVersions(ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildApi#buildsListXcodeVersions");
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

[**List&lt;BuildsListToolsets200ResponseXcodeInner&gt;**](BuildsListToolsets200ResponseXcodeInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Bad Request |  -  |

<a id="buildsUpdate"></a>
# **buildsUpdate**
> BuildsListBranches200ResponseInnerLastBuild buildsUpdate(buildId, ownerName, appName, buildsUpdateRequest)



Cancels a build

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
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    BuildApi apiInstance = new BuildApi(defaultClient);
    Integer buildId = 56; // Integer | The build ID
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    BuildsUpdateRequest buildsUpdateRequest = new BuildsUpdateRequest(); // BuildsUpdateRequest | 
    try {
      BuildsListBranches200ResponseInnerLastBuild result = apiInstance.buildsUpdate(buildId, ownerName, appName, buildsUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildApi#buildsUpdate");
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
| **buildId** | **Integer**| The build ID | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **buildsUpdateRequest** | [**BuildsUpdateRequest**](BuildsUpdateRequest.md)|  | |

### Return type

[**BuildsListBranches200ResponseInnerLastBuild**](BuildsListBranches200ResponseInnerLastBuild.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="buildsWebhook"></a>
# **buildsWebhook**
> buildsWebhook(body)



Public webhook sink

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
    defaultClient.setBasePath("https://api.appcenter.ms");

    BuildApi apiInstance = new BuildApi(defaultClient);
    Object body = null; // Object | 
    try {
      apiInstance.buildsWebhook(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildApi#buildsWebhook");
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
| **body** | **Object**|  | [optional] |

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
| **0** | Bad Request |  -  |

<a id="commitsListByShaList"></a>
# **commitsListByShaList**
> List&lt;CommitsListByShaList200ResponseInner&gt; commitsListByShaList(hashes, ownerName, appName)



Returns commit information for a batch of shas

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
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    BuildApi apiInstance = new BuildApi(defaultClient);
    List<String> hashes = Arrays.asList(); // List<String> | A collection of commit SHAs comma-delimited
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      List<CommitsListByShaList200ResponseInner> result = apiInstance.commitsListByShaList(hashes, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildApi#commitsListByShaList");
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
| **hashes** | [**List&lt;String&gt;**](String.md)| A collection of commit SHAs comma-delimited | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**List&lt;CommitsListByShaList200ResponseInner&gt;**](CommitsListByShaList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="fileAssetsCreate"></a>
# **fileAssetsCreate**
> FileAssetsCreate200Response fileAssetsCreate(ownerName, appName, body)



Create a new asset to upload a file

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
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    BuildApi apiInstance = new BuildApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    Object body = null; // Object | 
    try {
      FileAssetsCreate200Response result = apiInstance.fileAssetsCreate(ownerName, appName, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildApi#fileAssetsCreate");
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
| **body** | **Object**|  | [optional] |

### Return type

[**FileAssetsCreate200Response**](FileAssetsCreate200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Bad Request |  -  |

<a id="repositoriesList"></a>
# **repositoriesList**
> List&lt;RepositoriesList200ResponseInner&gt; repositoriesList(sourceHost, ownerName, appName, vstsAccountName, vstsProjectId, serviceConnectionId, form)



Gets the repositories available from the source code host

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
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    BuildApi apiInstance = new BuildApi(defaultClient);
    String sourceHost = "github"; // String | The source host
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    String vstsAccountName = "vstsAccountName_example"; // String | Filter repositories only for specified account and project, \"vstsProjectId\" is required
    String vstsProjectId = "vstsProjectId_example"; // String | Filter repositories only for specified account and project, \"vstsAccountName\" is required
    String serviceConnectionId = "serviceConnectionId_example"; // String | The id of the service connection (private). Required for GitLab self-hosted repositories
    String form = "lite"; // String | The selected form of the object
    try {
      List<RepositoriesList200ResponseInner> result = apiInstance.repositoriesList(sourceHost, ownerName, appName, vstsAccountName, vstsProjectId, serviceConnectionId, form);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildApi#repositoriesList");
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
| **sourceHost** | **String**| The source host | [enum: github, bitbucket, vsts, gitlab] |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **vstsAccountName** | **String**| Filter repositories only for specified account and project, \&quot;vstsProjectId\&quot; is required | [optional] |
| **vstsProjectId** | **String**| Filter repositories only for specified account and project, \&quot;vstsAccountName\&quot; is required | [optional] |
| **serviceConnectionId** | **String**| The id of the service connection (private). Required for GitLab self-hosted repositories | [optional] |
| **form** | **String**| The selected form of the object | [optional] [enum: lite, full] |

### Return type

[**List&lt;RepositoriesList200ResponseInner&gt;**](RepositoriesList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Bad Request |  -  |

<a id="repositoryConfigurationsCreateOrUpdate"></a>
# **repositoryConfigurationsCreateOrUpdate**
> BranchConfigurationsDelete200Response repositoryConfigurationsCreateOrUpdate(ownerName, appName, repositoryConfigurationsCreateOrUpdateRequest)



Configures the repository for build

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
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    BuildApi apiInstance = new BuildApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    RepositoryConfigurationsCreateOrUpdateRequest repositoryConfigurationsCreateOrUpdateRequest = new RepositoryConfigurationsCreateOrUpdateRequest(); // RepositoryConfigurationsCreateOrUpdateRequest | The repository information
    try {
      BranchConfigurationsDelete200Response result = apiInstance.repositoryConfigurationsCreateOrUpdate(ownerName, appName, repositoryConfigurationsCreateOrUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildApi#repositoryConfigurationsCreateOrUpdate");
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
| **repositoryConfigurationsCreateOrUpdateRequest** | [**RepositoryConfigurationsCreateOrUpdateRequest**](RepositoryConfigurationsCreateOrUpdateRequest.md)| The repository information | |

### Return type

[**BranchConfigurationsDelete200Response**](BranchConfigurationsDelete200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Bad Request |  -  |

<a id="repositoryConfigurationsDelete"></a>
# **repositoryConfigurationsDelete**
> BranchConfigurationsDelete200Response repositoryConfigurationsDelete(ownerName, appName)



Removes the configuration for the repository

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
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    BuildApi apiInstance = new BuildApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      BranchConfigurationsDelete200Response result = apiInstance.repositoryConfigurationsDelete(ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildApi#repositoryConfigurationsDelete");
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

[**BranchConfigurationsDelete200Response**](BranchConfigurationsDelete200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Bad Request |  -  |

<a id="repositoryConfigurationsList"></a>
# **repositoryConfigurationsList**
> List&lt;RepositoryConfigurationsList200ResponseInner&gt; repositoryConfigurationsList(ownerName, appName, includeInactive)



Returns the repository build configuration status of the app

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
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    BuildApi apiInstance = new BuildApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    Boolean includeInactive = true; // Boolean | Include inactive configurations if none are active
    try {
      List<RepositoryConfigurationsList200ResponseInner> result = apiInstance.repositoryConfigurationsList(ownerName, appName, includeInactive);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildApi#repositoryConfigurationsList");
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
| **includeInactive** | **Boolean**| Include inactive configurations if none are active | [optional] |

### Return type

[**List&lt;RepositoryConfigurationsList200ResponseInner&gt;**](RepositoryConfigurationsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of repository configurations |  -  |
| **0** | Bad Request |  -  |

