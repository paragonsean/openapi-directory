# ApisApi

All URIs are relative to *https://api.swaggerhub.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addApiCommentReplyV2**](ApisApi.md#addApiCommentReplyV2) | **POST** /apis/{owner}/{api}/{version}/comments/{comment}/replies | Reply to a comment |
| [**addApiCommentV2**](ApisApi.md#addApiCommentV2) | **POST** /apis/{owner}/{api}/{version}/comments | Add a new comment |
| [**cloneApi**](ApisApi.md#cloneApi) | **POST** /apis/{owner}/{api}/{version}/clone | Create a new API version |
| [**deleteApi**](ApisApi.md#deleteApi) | **DELETE** /apis/{owner}/{api} | Delete an API |
| [**deleteApiCommentReplyV2**](ApisApi.md#deleteApiCommentReplyV2) | **DELETE** /apis/{owner}/{api}/{version}/comments/{comment}/replies/{reply} | Delete a comment reply |
| [**deleteApiCommentV2**](ApisApi.md#deleteApiCommentV2) | **DELETE** /apis/{owner}/{api}/{version}/comments/{comment} | Delete a comment |
| [**deleteApiVersion**](ApisApi.md#deleteApiVersion) | **DELETE** /apis/{owner}/{api}/{version} | Delete an API version |
| [**forkApi**](ApisApi.md#forkApi) | **POST** /apis/{owner}/{api}/{version}/fork | Fork an API |
| [**getApiCommentsV2**](ApisApi.md#getApiCommentsV2) | **GET** /apis/{owner}/{api}/{version}/comments | Get comments for the specified API version |
| [**getApiDefaultVersion**](ApisApi.md#getApiDefaultVersion) | **GET** /apis/{owner}/{api}/settings/default | Get the default version of an API |
| [**getApiVersions**](ApisApi.md#getApiVersions) | **GET** /apis/{owner}/{api} | Get a list of API versions |
| [**getDefinition**](ApisApi.md#getDefinition) | **GET** /apis/{owner}/{api}/{version} | Get the OpenAPI definition of the specified API version |
| [**getJsonDefinition**](ApisApi.md#getJsonDefinition) | **GET** /apis/{owner}/{api}/{version}/swagger.json | Get the OpenAPI definition for the specified API version in JSON format |
| [**getLifecycleSettings**](ApisApi.md#getLifecycleSettings) | **GET** /apis/{owner}/{api}/{version}/settings/lifecycle | Get the published status for the specified API and version |
| [**getOwnerApis**](ApisApi.md#getOwnerApis) | **GET** /apis/{owner} | Get a list of APIs of the specified owner |
| [**getPrivateSettings**](ApisApi.md#getPrivateSettings) | **GET** /apis/{owner}/{api}/{version}/settings/private | Get the visibility (public or private) of API version |
| [**getStandardizationErrors**](ApisApi.md#getStandardizationErrors) | **GET** /apis/{owner}/{api}/{version}/standardization | Retrieve the standardization errors for a given API definition |
| [**getValidation**](ApisApi.md#getValidation) | **GET** /apis/{owner}/{api}/{version}/validation | Deprecated Get API Standardization errors and warnings |
| [**getYamlDefinition**](ApisApi.md#getYamlDefinition) | **GET** /apis/{owner}/{api}/{version}/swagger.yaml | Get the OpenAPI definition for the specified API version in YAML format |
| [**renameApi**](ApisApi.md#renameApi) | **POST** /apis/{owner}/{api}/rename | Rename an API |
| [**saveDefinition**](ApisApi.md#saveDefinition) | **POST** /apis/{owner}/{api} | Create or update an API |
| [**searchApis**](ApisApi.md#searchApis) | **GET** /apis | Search APIs |
| [**searchApisAndDomains**](ApisApi.md#searchApisAndDomains) | **GET** /specs | Retrieve a list of currently defined APIs, domains, and templates in APIs.json format |
| [**setApiCommentStatusV2**](ApisApi.md#setApiCommentStatusV2) | **PUT** /apis/{owner}/{api}/{version}/comments/{comment}/status/{status} | Resolve or reopen a comment |
| [**setApiDefaultVersion**](ApisApi.md#setApiDefaultVersion) | **PUT** /apis/{owner}/{api}/settings/default | Set the default API version |
| [**setLifecycleSettings**](ApisApi.md#setLifecycleSettings) | **PUT** /apis/{owner}/{api}/{version}/settings/lifecycle | Publish or unpublish an API version |
| [**setPrivateSettings**](ApisApi.md#setPrivateSettings) | **PUT** /apis/{owner}/{api}/{version}/settings/private | Set the visibility (public or private) of an API version |
| [**updateApiCommentReplyV2**](ApisApi.md#updateApiCommentReplyV2) | **PATCH** /apis/{owner}/{api}/{version}/comments/{comment}/replies/{reply} | Update a comment reply |
| [**updateApiCommentV2**](ApisApi.md#updateApiCommentV2) | **PATCH** /apis/{owner}/{api}/{version}/comments/{comment} | Update a comment |
| [**updateApiCommentsV2**](ApisApi.md#updateApiCommentsV2) | **POST** /apis/{owner}/{api}/{version}/comments/batch | Bulk update comments |


<a id="addApiCommentReplyV2"></a>
# **addApiCommentReplyV2**
> List&lt;Comment&gt; addApiCommentReplyV2(owner, api, version, comment, body)

Reply to a comment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
    String api = "api_example"; // String | API name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    String comment = "comment_example"; // String | Comment identifier
    NewReply body = new NewReply(); // NewReply | 
    try {
      List<Comment> result = apiInstance.addApiCommentReplyV2(owner, api, version, comment, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#addApiCommentReplyV2");
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
| **owner** | **String**| API owner (organization or user, case-sensitive) | |
| **api** | **String**| API name (case-sensitive) | |
| **version** | **String**| Version identifier | |
| **comment** | **String**| Comment identifier | |
| **body** | [**NewReply**](NewReply.md)|  | |

### Return type

[**List&lt;Comment&gt;**](Comment.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Newly created reply |  -  |
| **400** | Request body invalid |  -  |
| **401** | Access token is not set or invalid |  -  |
| **403** | The comment feature is not available for the organization&#39;s plan, or the authenticating user does not have permission to complete this action |  -  |
| **404** | The specified API or comment was not found |  -  |

<a id="addApiCommentV2"></a>
# **addApiCommentV2**
> ClosableComment addApiCommentV2(owner, api, version, body)

Add a new comment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
    String api = "api_example"; // String | API name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    NewComment body = new NewComment(); // NewComment | 
    try {
      ClosableComment result = apiInstance.addApiCommentV2(owner, api, version, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#addApiCommentV2");
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
| **owner** | **String**| API owner (organization or user, case-sensitive) | |
| **api** | **String**| API name (case-sensitive) | |
| **version** | **String**| Version identifier | |
| **body** | [**NewComment**](NewComment.md)|  | |

### Return type

[**ClosableComment**](ClosableComment.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Newly created comment for the specified API |  -  |
| **400** | Request body invalid |  -  |
| **401** | Access token is not set or invalid |  -  |
| **403** | The comment feature is not available for the organization&#39;s plan, or the authenticating user does not have permission to complete this action |  -  |
| **404** | The specified API was not found |  -  |

<a id="cloneApi"></a>
# **cloneApi**
> cloneApi(owner, api, version, newVersion)

Create a new API version

Use this operation to clone an existing API version as a new version. The new version will have the same YAML content but with updated &#x60;info.version&#x60;.  **Note:** Comments, integrations, and codegen options are not copied to the new version. The default version also remains unchanged.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
    String api = "api_example"; // String | API name (case-sensitive)
    String version = "version_example"; // String | The version to clone (case-sensitive)
    NewVersion newVersion = new NewVersion(); // NewVersion | An object that contains the new version number and other parameters. The version number must be in the format described in the [documentation](https://support.smartbear.com/swaggerhub/docs/apis/versioning.html#format).
    try {
      apiInstance.cloneApi(owner, api, version, newVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#cloneApi");
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
| **owner** | **String**| API owner (organization or user, case-sensitive) | |
| **api** | **String**| API name (case-sensitive) | |
| **version** | **String**| The version to clone (case-sensitive) | |
| **newVersion** | [**NewVersion**](NewVersion.md)| An object that contains the new version number and other parameters. The version number must be in the format described in the [documentation](https://support.smartbear.com/swaggerhub/docs/apis/versioning.html#format). | |

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | New API version was successfully created |  -  |
| **400** | Bad request |  -  |
| **403** | Access denied |  -  |
| **404** | The specified API or version was not found |  -  |
| **409** | The API version you are trying to create already exists |  -  |

<a id="deleteApi"></a>
# **deleteApi**
> deleteApi(owner, api)

Delete an API

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
    String api = "api_example"; // String | API name (case-sensitive)
    try {
      apiInstance.deleteApi(owner, api);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#deleteApi");
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
| **owner** | **String**| API owner (organization or user, case-sensitive) | |
| **api** | **String**| API name (case-sensitive) | |

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The API was successfully deleted |  -  |
| **403** | Access denied |  -  |
| **404** | The specified API not found |  -  |
| **409** | The API has published versions and cannot be deleted |  -  |

<a id="deleteApiCommentReplyV2"></a>
# **deleteApiCommentReplyV2**
> deleteApiCommentReplyV2(owner, api, version, comment, reply)

Delete a comment reply

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
    String api = "api_example"; // String | API name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    String comment = "comment_example"; // String | Comment identifier
    String reply = "reply_example"; // String | Reply identifier
    try {
      apiInstance.deleteApiCommentReplyV2(owner, api, version, comment, reply);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#deleteApiCommentReplyV2");
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
| **owner** | **String**| API owner (organization or user, case-sensitive) | |
| **api** | **String**| API name (case-sensitive) | |
| **version** | **String**| Version identifier | |
| **comment** | **String**| Comment identifier | |
| **reply** | **String**| Reply identifier | |

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Сomment reply was deleted |  -  |
| **401** | Access token is not set or invalid |  -  |
| **403** | The comment feature is not available for the organization&#39;s plan, or the authenticating user does not have permission to complete this action |  -  |
| **404** | The specified API, comment, or reply was not found |  -  |

<a id="deleteApiCommentV2"></a>
# **deleteApiCommentV2**
> deleteApiCommentV2(owner, api, version, comment)

Delete a comment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
    String api = "api_example"; // String | API name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    String comment = "comment_example"; // String | Comment identifier
    try {
      apiInstance.deleteApiCommentV2(owner, api, version, comment);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#deleteApiCommentV2");
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
| **owner** | **String**| API owner (organization or user, case-sensitive) | |
| **api** | **String**| API name (case-sensitive) | |
| **version** | **String**| Version identifier | |
| **comment** | **String**| Comment identifier | |

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Comment was deleted |  -  |
| **401** | Access token is not set or invalid |  -  |
| **403** | The comment feature is not available for the organization&#39;s plan, or the authenticating user does not have permission to complete this action |  -  |
| **404** | The specified API or comment was not found |  -  |

<a id="deleteApiVersion"></a>
# **deleteApiVersion**
> deleteApiVersion(owner, api, version)

Delete an API version

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
    String api = "api_example"; // String | API name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    try {
      apiInstance.deleteApiVersion(owner, api, version);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#deleteApiVersion");
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
| **owner** | **String**| API owner (organization or user, case-sensitive) | |
| **api** | **String**| API name (case-sensitive) | |
| **version** | **String**| Version identifier | |

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The API version was successfully deleted |  -  |
| **403** | Access denied |  -  |
| **404** | The specified API was not found |  -  |
| **409** | The API version is published and cannot be deleted or it is the only version of this API |  -  |

<a id="forkApi"></a>
# **forkApi**
> forkApi(owner, api, version, forkVersion)

Fork an API

Creates a [fork](https://support.smartbear.com/swaggerhub/docs/apis/forking-api.html) of the specified API definition and version. The fork can be created as a new API, or as a new version in another existing API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
    String api = "api_example"; // String | API name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    ForkVersion forkVersion = new ForkVersion(); // ForkVersion | Fork parameters
    try {
      apiInstance.forkApi(owner, api, version, forkVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#forkApi");
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
| **owner** | **String**| API owner (organization or user, case-sensitive) | |
| **api** | **String**| API name (case-sensitive) | |
| **version** | **String**| Version identifier | |
| **forkVersion** | [**ForkVersion**](ForkVersion.md)| Fork parameters | |

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The API was successfully forked |  -  |
| **400** | Some parameters are missing or invalid |  -  |
| **401** | Access token is not set or invalid |  -  |
| **403** | Access denied |  -  |
| **404** | The specified owner or API was not found |  -  |
| **409** | An API with the name and version you&#39;re trying to create already exists |  -  |

<a id="getApiCommentsV2"></a>
# **getApiCommentsV2**
> List&lt;ClosableComment&gt; getApiCommentsV2(owner, api, version)

Get comments for the specified API version

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
    String api = "api_example"; // String | API name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    try {
      List<ClosableComment> result = apiInstance.getApiCommentsV2(owner, api, version);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#getApiCommentsV2");
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
| **owner** | **String**| API owner (organization or user, case-sensitive) | |
| **api** | **String**| API name (case-sensitive) | |
| **version** | **String**| Version identifier | |

### Return type

[**List&lt;ClosableComment&gt;**](ClosableComment.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Comments for the specified API |  -  |
| **204** | No comments were found for the specified API |  -  |
| **401** | Access token is not set or invalid |  -  |
| **403** | The comment feature is not available for the organization&#39;s plan, or the authenticating user does not have permission to complete this action |  -  |
| **404** | The specified API was not found |  -  |

<a id="getApiDefaultVersion"></a>
# **getApiDefaultVersion**
> DefaultVersion getApiDefaultVersion(owner, api)

Get the default version of an API

This operation returns the version identifier, such as &#x60;1.0.0&#x60;. To get the definition itself, use &#x60;GET /apis/{owner}/{api}/{version}&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
    String api = "api_example"; // String | API name (case-sensitive)
    try {
      DefaultVersion result = apiInstance.getApiDefaultVersion(owner, api);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#getApiDefaultVersion");
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
| **owner** | **String**| API owner (organization or user, case-sensitive) | |
| **api** | **String**| API name (case-sensitive) | |

### Return type

[**DefaultVersion**](DefaultVersion.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The default version identifier for this API |  -  |
| **404** | The specified API was not found. If it is private, make sure the request is authenticated and the authenticating user has access to this API. |  -  |

<a id="getApiVersions"></a>
# **getApiVersions**
> ApisJson getApiVersions(owner, api)

Get a list of API versions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
    String api = "api_example"; // String | API name (case-sensitive)
    try {
      ApisJson result = apiInstance.getApiVersions(owner, api);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#getApiVersions");
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
| **owner** | **String**| API owner (organization or user, case-sensitive) | |
| **api** | **String**| API name (case-sensitive) | |

### Return type

[**ApisJson**](ApisJson.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of API versions in APIs.json format |  -  |
| **404** | The specified API was not found. If it is private, make sure the request is authenticated and the authenticating user has access to this API. |  -  |

<a id="getDefinition"></a>
# **getDefinition**
> Object getDefinition(owner, api, version, resolved, flatten)

Get the OpenAPI definition of the specified API version

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
    String api = "api_example"; // String | API name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    Boolean resolved = false; // Boolean | Set to true to get the resolved version of the API definition. The content of all external $refs will be included in the resulting file.
    Boolean flatten = false; // Boolean | If set to `true`, it creates models from inline schemas in OpenAPI definition. AsyncAPI definitions cannot be flattened.
    try {
      Object result = apiInstance.getDefinition(owner, api, version, resolved, flatten);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#getDefinition");
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
| **owner** | **String**| API owner (organization or user, case-sensitive) | |
| **api** | **String**| API name (case-sensitive) | |
| **version** | **String**| Version identifier | |
| **resolved** | **Boolean**| Set to true to get the resolved version of the API definition. The content of all external $refs will be included in the resulting file. | [optional] [default to false] |
| **flatten** | **Boolean**| If set to &#x60;true&#x60;, it creates models from inline schemas in OpenAPI definition. AsyncAPI definitions cannot be flattened. | [optional] [default to false] |

### Return type

**Object**

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OpenAPI definition in the requested format (YAML or JSON) |  -  |
| **400** | Could not generate resolved definition due to syntax errors in the definition |  -  |
| **404** | The specified API or version was not found. If it is private, make sure the request is authenticated and the authenticating user has access to this API. |  -  |

<a id="getJsonDefinition"></a>
# **getJsonDefinition**
> Object getJsonDefinition(owner, api, version, resolved, flatten)

Get the OpenAPI definition for the specified API version in JSON format

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
    String api = "api_example"; // String | API name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    Boolean resolved = false; // Boolean | Set to true to get the resolved version of the API definition. The content of all external $refs will be included in the resulting file.
    Boolean flatten = false; // Boolean | If set to `true`, it creates models from inline schemas in OpenAPI definition. AsyncAPI definitions cannot be flattened.
    try {
      Object result = apiInstance.getJsonDefinition(owner, api, version, resolved, flatten);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#getJsonDefinition");
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
| **owner** | **String**| API owner (organization or user, case-sensitive) | |
| **api** | **String**| API name (case-sensitive) | |
| **version** | **String**| Version identifier | |
| **resolved** | **Boolean**| Set to true to get the resolved version of the API definition. The content of all external $refs will be included in the resulting file. | [optional] [default to false] |
| **flatten** | **Boolean**| If set to &#x60;true&#x60;, it creates models from inline schemas in OpenAPI definition. AsyncAPI definitions cannot be flattened. | [optional] [default to false] |

### Return type

**Object**

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OpenAPI definition in JSON format |  -  |
| **400** | Could not generate resolved definition due to syntax errors in the definition |  -  |
| **404** | The specified API or version was not found. If it is private, make sure the request is authenticated and the authenticating user has access to this API. |  -  |

<a id="getLifecycleSettings"></a>
# **getLifecycleSettings**
> LifecycleSettings getLifecycleSettings(owner, api, version)

Get the published status for the specified API and version

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
    String api = "api_example"; // String | API name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    try {
      LifecycleSettings result = apiInstance.getLifecycleSettings(owner, api, version);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#getLifecycleSettings");
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
| **owner** | **String**| API owner (organization or user, case-sensitive) | |
| **api** | **String**| API name (case-sensitive) | |
| **version** | **String**| Version identifier | |

### Return type

[**LifecycleSettings**](LifecycleSettings.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The published status of this API version |  -  |
| **401** | Access token is not set or invalid |  -  |
| **404** | The specified API or version was not found. If it is private, make sure the request is authenticated and the authenticating user has access to this API. |  -  |

<a id="getOwnerApis"></a>
# **getOwnerApis**
> ApisJson getOwnerApis(owner, page, limit, sort, order)

Get a list of APIs of the specified owner

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
    Integer page = 0; // Integer | Page to return
    Integer limit = 10; // Integer | Number of results per page (1 .. 100)
    String sort = "NAME"; // String | Sort criteria of result set: * NAME * UPDATED * CREATED * OWNER * BEST_MATCH - by relevance * TITLE - by `info.title` 
    String order = "ASC"; // String | Sort order
    try {
      ApisJson result = apiInstance.getOwnerApis(owner, page, limit, sort, order);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#getOwnerApis");
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
| **owner** | **String**| API owner (organization or user, case-sensitive) | |
| **page** | **Integer**| Page to return | [optional] [default to 0] |
| **limit** | **Integer**| Number of results per page (1 .. 100) | [optional] [default to 10] |
| **sort** | **String**| Sort criteria of result set: * NAME * UPDATED * CREATED * OWNER * BEST_MATCH - by relevance * TITLE - by &#x60;info.title&#x60;  | [optional] [default to NAME] [enum: NAME, UPDATED, CREATED, OWNER, BEST_MATCH, TITLE] |
| **order** | **String**| Sort order | [optional] [default to ASC] [enum: ASC, DESC] |

### Return type

[**ApisJson**](ApisJson.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of APIs in APIs.json format |  -  |

<a id="getPrivateSettings"></a>
# **getPrivateSettings**
> VisibilitySettings getPrivateSettings(owner, api, version)

Get the visibility (public or private) of API version

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
    String api = "api_example"; // String | API name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    try {
      VisibilitySettings result = apiInstance.getPrivateSettings(owner, api, version);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#getPrivateSettings");
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
| **owner** | **String**| API owner (organization or user, case-sensitive) | |
| **api** | **String**| API name (case-sensitive) | |
| **version** | **String**| Version identifier | |

### Return type

[**VisibilitySettings**](VisibilitySettings.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response body indicates whether this API version is private (&#x60;true&#x60;) or public (&#x60;false&#x60;) |  -  |
| **401** | Access token is not set or invalid |  -  |
| **404** | The specified API or version was not found |  -  |

<a id="getStandardizationErrors"></a>
# **getStandardizationErrors**
> StandardizationResult getStandardizationErrors(owner, api, version)

Retrieve the standardization errors for a given API definition

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
    String api = "api_example"; // String | 
    String version = "version_example"; // String | Version identifier
    try {
      StandardizationResult result = apiInstance.getStandardizationErrors(owner, api, version);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#getStandardizationErrors");
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
| **owner** | **String**| API owner (organization or user, case-sensitive) | |
| **api** | **String**|  | |
| **version** | **String**| Version identifier | |

### Return type

[**StandardizationResult**](StandardizationResult.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a list of standardization errors for the given API definition  |  -  |
| **400** |  |  -  |
| **404** |  |  -  |

<a id="getValidation"></a>
# **getValidation**
> ValidationResult getValidation(owner, api, version)

Deprecated Get API Standardization errors and warnings

**Note:** This endpoint is deprecated. Use the following new endpoint instead: GET /apis/{owner}/{api}/{version}/standardization   If your organization has [API standardization](https://support.smartbear.com/swaggerhub/docs/organizations/api-standardization.html) configured, you can use this operation to validate a specific API version and get a list of errors or warnings with line numbers.  This operation checks for standardization errors only and does not return OpenAPI syntax errors (such as misspelled keywords) or YAML syntax errors.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String owner = "owner_example"; // String | Organization name (case-sensitive)
    String api = "api_example"; // String | API name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    try {
      ValidationResult result = apiInstance.getValidation(owner, api, version);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#getValidation");
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
| **owner** | **String**| Organization name (case-sensitive) | |
| **api** | **String**| API name (case-sensitive) | |
| **version** | **String**| Version identifier | |

### Return type

[**ValidationResult**](ValidationResult.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An object that contains a list of standardization errors and warnings found in the specified API version. Error information includes line numbers, severity (error or warning), and error messages. If no standardization errors or warnings are found, an empty validation array is returned. |  -  |
| **403** | Access denied |  -  |
| **404** | The specified API or version was not found, or standardization is not enabled for this organization. |  -  |

<a id="getYamlDefinition"></a>
# **getYamlDefinition**
> Object getYamlDefinition(owner, api, version, resolved, flatten)

Get the OpenAPI definition for the specified API version in YAML format

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
    String api = "api_example"; // String | API name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    Boolean resolved = false; // Boolean | Set to true to get the resolved version of the API definition. The content of all external $refs will be included in the resulting file.
    Boolean flatten = false; // Boolean | If set to `true`, it creates models from inline schemas in OpenAPI definition. AsyncAPI definitions cannot be flattened.
    try {
      Object result = apiInstance.getYamlDefinition(owner, api, version, resolved, flatten);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#getYamlDefinition");
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
| **owner** | **String**| API owner (organization or user, case-sensitive) | |
| **api** | **String**| API name (case-sensitive) | |
| **version** | **String**| Version identifier | |
| **resolved** | **Boolean**| Set to true to get the resolved version of the API definition. The content of all external $refs will be included in the resulting file. | [optional] [default to false] |
| **flatten** | **Boolean**| If set to &#x60;true&#x60;, it creates models from inline schemas in OpenAPI definition. AsyncAPI definitions cannot be flattened. | [optional] [default to false] |

### Return type

**Object**

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yaml, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OpenAPI definition in YAML format |  -  |
| **400** | Could not generate resolved definition due to syntax errors in the definition |  -  |
| **404** | The specified API or version was not found. If it is private, make sure the request is authenticated and the authenticating user has access to this API. |  -  |

<a id="renameApi"></a>
# **renameApi**
> renameApi(owner, api, newName)

Rename an API

The new name must follow the [naming rules](https://support.smartbear.com/swaggerhub/docs/apis/creating-api.html).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
    String api = "api_example"; // String | API name (case-sensitive)
    String newName = "newName_example"; // String | New name
    try {
      apiInstance.renameApi(owner, api, newName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#renameApi");
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
| **owner** | **String**| API owner (organization or user, case-sensitive) | |
| **api** | **String**| API name (case-sensitive) | |
| **newName** | **String**| New name | |

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The API was successfully renamed |  -  |
| **401** | Access token is not set or invalid |  -  |
| **403** | Access denied (insufficient user permissions) |  -  |
| **404** | The specified owner or API was not found |  -  |
| **409** | An API or domain with the new name already exists, or the new and old names are the same |  -  |

<a id="saveDefinition"></a>
# **saveDefinition**
> saveDefinition(owner, api, definition, isPrivate, version, force)

Create or update an API

Use this operation to create a new API or update an existing API by uploading its OpenAPI definition in YAML or JSON format. The authenticating user must have permissions to create or update APIs in the specified &#x60;owner&#x60; account.  The API name and version must follow SwaggerHub naming rules, otherwise the request will be rejected. Refer to:    * [API name format](https://support.smartbear.com/swaggerhub/docs/apis/creating-api.html)  * [Version format](https://support.smartbear.com/swaggerhub/docs/apis/versioning.html#format)   When a new version of an existing API is created, it does not automatically become the default version. You can use &#x60;PUT /apis/{owner}/{api}/settings/default&#x60; to set the default version.  ### cURL example Line breaks are added for readability.      curl -X POST \&quot;https://api.swaggerhub.com/apis/OWNER/API_TO_CREATE_OR_UPDATE\&quot;          -H \&quot;Authorization: SWAGGERHUB_API_KEY\&quot;          -H \&quot;Content-Type: application/yaml\&quot;          --data-binary @C:\\work\\swagger.yaml  **Note:** Use &#x60;--data-binary&#x60; (not &#x60;-d&#x60;) when uploading YAML files using cURL, and remember to specify the correct &#x60;Content-Type&#x60; header.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String owner = "owner_example"; // String | API owner name (organization or user name, case-sensitive)
    String api = "api_example"; // String | API name (case-sensitive)
    String definition = "definition_example"; // String | OpenAPI definition in the YAML or JSON format. The content must be syntactically valid YAML or JSON.
    Boolean isPrivate = false; // Boolean | Whether to make the API private (`true`) or public (`false`)
    String version = "version_example"; // String | API version to create or update. If omitted, the version is extracted from the `info.version` field of the provided OpenAPI definition.  Either the `version` parameter or the `info.version` value must be specified, otherwise the request will be rejected. If both are specified, the `version` parameter overrides the `info.version` value.  If this API version already exists, it will be updated with the new definition (unless that version has been published - in this case the update will be rejected).
    Boolean force = true; // Boolean | Force update
    try {
      apiInstance.saveDefinition(owner, api, definition, isPrivate, version, force);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#saveDefinition");
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
| **owner** | **String**| API owner name (organization or user name, case-sensitive) | |
| **api** | **String**| API name (case-sensitive) | |
| **definition** | **String**| OpenAPI definition in the YAML or JSON format. The content must be syntactically valid YAML or JSON. | |
| **isPrivate** | **Boolean**| Whether to make the API private (&#x60;true&#x60;) or public (&#x60;false&#x60;) | [optional] [default to false] |
| **version** | **String**| API version to create or update. If omitted, the version is extracted from the &#x60;info.version&#x60; field of the provided OpenAPI definition.  Either the &#x60;version&#x60; parameter or the &#x60;info.version&#x60; value must be specified, otherwise the request will be rejected. If both are specified, the &#x60;version&#x60; parameter overrides the &#x60;info.version&#x60; value.  If this API version already exists, it will be updated with the new definition (unless that version has been published - in this case the update will be rejected). | [optional] |
| **force** | **Boolean**| Force update | [optional] |

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Existing API version was successfully updated |  -  |
| **201** | New API or version was successfully created |  -  |
| **205** | This status is returned when updating existing API versions that use [API Auto Mocking](https://support.smartbear.com/swaggerhub/docs/integrations/api-auto-mocking.html) with the \&quot;Update host setting\&quot; option enabled. Status 205 means the uploaded definition was successfully saved, and its &#x60;servers&#x60; or &#x60;host&#x60;+&#x60;basePath&#x60; values were automatically updated to point to the mock server.  The client can download the updated definition from SwaggerHub by using &#x60;GET /apis/{owner}/{api}&#x60;. |  -  |
| **400** | Possible reasons:   * Some parameter values are invalid, or the provided OpenAPI definition is invalid.  * The specified &#x60;projectName&#x60; does not exist in the &#x60;owner&#x60; organization, or the authenticating user does not have access to this project.  * Cannot create a new API because a domain with this name already exists in the &#x60;owner&#x60; account. Try a different name. |  -  |
| **401** | Access token is not set or invalid |  -  |
| **403** | Maximum number of APIs reached |  -  |
| **404** | The specified owner was not found |  -  |
| **409** | Cannot overwrite a published API version |  -  |
| **415** | Invalid content type |  -  |

<a id="searchApis"></a>
# **searchApis**
> searchApis(query, state, page, limit, sort, order)

Search APIs

This is a convenience alias for &#x60;GET /specs?specType&#x3D;API&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String query = "query_example"; // String | Free text query to match
    String state = "ALL"; // String | Matches against published state of the spec: * UNPUBLISHED - spec is a draft, a work in progress * PUBLISHED - spec is a stable version ready for consuming from client applications * ANY - either PUBLISHED or UNPUBLISHED 
    Integer page = 0; // Integer | Page to return
    Integer limit = 10; // Integer | Number of results per page (1 .. 100)
    String sort = "NAME"; // String | Sort criteria of result set: * NAME * UPDATED * CREATED * OWNER * BEST_MATCH - by relevance * TITLE - by `info.title` 
    String order = "ASC"; // String | Sort order
    try {
      apiInstance.searchApis(query, state, page, limit, sort, order);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#searchApis");
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
| **query** | **String**| Free text query to match | [optional] |
| **state** | **String**| Matches against published state of the spec: * UNPUBLISHED - spec is a draft, a work in progress * PUBLISHED - spec is a stable version ready for consuming from client applications * ANY - either PUBLISHED or UNPUBLISHED  | [optional] [default to ALL] [enum: ALL, PUBLISHED, UNPUBLISHED] |
| **page** | **Integer**| Page to return | [optional] [default to 0] |
| **limit** | **Integer**| Number of results per page (1 .. 100) | [optional] [default to 10] |
| **sort** | **String**| Sort criteria of result set: * NAME * UPDATED * CREATED * OWNER * BEST_MATCH - by relevance * TITLE - by &#x60;info.title&#x60;  | [optional] [default to NAME] [enum: NAME, UPDATED, CREATED, OWNER, BEST_MATCH, TITLE] |
| **order** | **String**| Sort order | [optional] [default to ASC] [enum: ASC, DESC] |

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **303** | Redirect to &#x60;GET /specs&#x60;, with all query parameters preserved |  * Location -  <br>  |

<a id="searchApisAndDomains"></a>
# **searchApisAndDomains**
> ApisJson searchApisAndDomains(specType, visibility, state, owner, query, page, limit, sort, order)

Retrieve a list of currently defined APIs, domains, and templates in APIs.json format

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String specType = "API"; // String | Type of definitions to search: * API - APIs only * DOMAIN - domains only * TEMPLATE - templates only * ANY - APIs, domains, and templates 
    String visibility = "PUBLIC"; // String | The visibility of a definition in SwaggerHub: * PUBLIC - can be viewed by anyone * PRIVATE - can only be viewed by you or your organization and those that you are collaborating with or have shared it with * ANY - either PUBLIC or PRIVATE 
    String state = "ALL"; // String | Matches against published state of the spec: * UNPUBLISHED - spec is a draft, a work in progress * PUBLISHED - spec is a stable version ready for consuming from client applications * ANY - either PUBLISHED or UNPUBLISHED 
    String owner = "owner_example"; // String | API or domain owner. Can be username or organization name. Case-sensitive.
    String query = "query_example"; // String | Free text query to match
    Integer page = 0; // Integer | Page to return
    Integer limit = 10; // Integer | Number of results per page (1 .. 100)
    String sort = "NAME"; // String | Sort criteria of result set: * NAME * UPDATED * CREATED * OWNER * BEST_MATCH - by relevance * TITLE - by `info.title` 
    String order = "ASC"; // String | Sort order
    try {
      ApisJson result = apiInstance.searchApisAndDomains(specType, visibility, state, owner, query, page, limit, sort, order);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#searchApisAndDomains");
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
| **specType** | **String**| Type of definitions to search: * API - APIs only * DOMAIN - domains only * TEMPLATE - templates only * ANY - APIs, domains, and templates  | [optional] [default to ANY] [enum: API, DOMAIN, TEMPLATE, ANY] |
| **visibility** | **String**| The visibility of a definition in SwaggerHub: * PUBLIC - can be viewed by anyone * PRIVATE - can only be viewed by you or your organization and those that you are collaborating with or have shared it with * ANY - either PUBLIC or PRIVATE  | [optional] [default to ANY] [enum: PUBLIC, PRIVATE, ANY] |
| **state** | **String**| Matches against published state of the spec: * UNPUBLISHED - spec is a draft, a work in progress * PUBLISHED - spec is a stable version ready for consuming from client applications * ANY - either PUBLISHED or UNPUBLISHED  | [optional] [default to ALL] [enum: ALL, PUBLISHED, UNPUBLISHED] |
| **owner** | **String**| API or domain owner. Can be username or organization name. Case-sensitive. | [optional] |
| **query** | **String**| Free text query to match | [optional] |
| **page** | **Integer**| Page to return | [optional] [default to 0] |
| **limit** | **Integer**| Number of results per page (1 .. 100) | [optional] [default to 10] |
| **sort** | **String**| Sort criteria of result set: * NAME * UPDATED * CREATED * OWNER * BEST_MATCH - by relevance * TITLE - by &#x60;info.title&#x60;  | [optional] [default to NAME] [enum: NAME, UPDATED, CREATED, OWNER, BEST_MATCH, TITLE] |
| **order** | **String**| Sort order | [optional] [default to ASC] [enum: ASC, DESC] |

### Return type

[**ApisJson**](ApisJson.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of APIs, domains, and templates in APIs.json format |  -  |

<a id="setApiCommentStatusV2"></a>
# **setApiCommentStatusV2**
> setApiCommentStatusV2(owner, api, version, comment, status)

Resolve or reopen a comment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
    String api = "api_example"; // String | API name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    String comment = "comment_example"; // String | Comment identifier
    String status = "OPEN"; // String | Comment status
    try {
      apiInstance.setApiCommentStatusV2(owner, api, version, comment, status);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#setApiCommentStatusV2");
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
| **owner** | **String**| API owner (organization or user, case-sensitive) | |
| **api** | **String**| API name (case-sensitive) | |
| **version** | **String**| Version identifier | |
| **comment** | **String**| Comment identifier | |
| **status** | **String**| Comment status | [enum: OPEN, RESOLVED] |

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Comment status was updated |  -  |
| **400** | Request body invalid |  -  |
| **401** | Access token is not set or invalid |  -  |
| **403** | The comment feature is not available for the organization&#39;s plan, or the authenticating user does not have permission to complete this action |  -  |
| **404** | The specified API or comment was not found |  -  |

<a id="setApiDefaultVersion"></a>
# **setApiDefaultVersion**
> setApiDefaultVersion(owner, api, defaultVersion)

Set the default API version

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
    String api = "api_example"; // String | API name (case-sensitive)
    DefaultVersion defaultVersion = new DefaultVersion(); // DefaultVersion | An object that specifies the default version for this API
    try {
      apiInstance.setApiDefaultVersion(owner, api, defaultVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#setApiDefaultVersion");
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
| **owner** | **String**| API owner (organization or user, case-sensitive) | |
| **api** | **String**| API name (case-sensitive) | |
| **defaultVersion** | [**DefaultVersion**](DefaultVersion.md)| An object that specifies the default version for this API | |

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The default version was successfully changed |  -  |
| **401** | Access token is not set or invalid |  -  |
| **403** | Access denied (insufficient user permissions) |  -  |
| **404** | The specified API or version was not found |  -  |

<a id="setLifecycleSettings"></a>
# **setLifecycleSettings**
> setLifecycleSettings(owner, api, version, settings, force)

Publish or unpublish an API version

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
    String api = "api_example"; // String | API name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    LifecycleSettings settings = new LifecycleSettings(); // LifecycleSettings | An object that specifies the new `published` state: `true` means published, `false` - unpublished
    Boolean force = false; // Boolean | To publish an API that references _unpublished_ domains, this parameter must be `true`. Otherwise, the request will be rejected with status code 424.
    try {
      apiInstance.setLifecycleSettings(owner, api, version, settings, force);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#setLifecycleSettings");
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
| **owner** | **String**| API owner (organization or user, case-sensitive) | |
| **api** | **String**| API name (case-sensitive) | |
| **version** | **String**| Version identifier | |
| **settings** | [**LifecycleSettings**](LifecycleSettings.md)| An object that specifies the new &#x60;published&#x60; state: &#x60;true&#x60; means published, &#x60;false&#x60; - unpublished | |
| **force** | **Boolean**| To publish an API that references _unpublished_ domains, this parameter must be &#x60;true&#x60;. Otherwise, the request will be rejected with status code 424. | [optional] [default to false] |

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully published or unpublished the API |  -  |
| **400** | The API definition contains [standardization](https://support.smartbear.com/swaggerhub/docs/organizations/api-standardization.html) errors which prevent it from being published. |  -  |
| **401** | Access token is not set or invalid |  -  |
| **403** | Access denied (insufficient user permissions) |  -  |
| **404** | The specified API or version was not found |  -  |
| **424** | The API version you are trying to publish contains references to _unpublished_ domains. If those domains change, it may affect your API. To publish the API anyway, repeat the request with the &#x60;force&#x3D;true&#x60; query parameter.  The response body contains a list of unpublished domains referenced from this API. |  -  |

<a id="setPrivateSettings"></a>
# **setPrivateSettings**
> setPrivateSettings(owner, api, version, settings)

Set the visibility (public or private) of an API version

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
    String api = "api_example"; // String | API name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    VisibilitySettings settings = new VisibilitySettings(); // VisibilitySettings | An object that specifies the new visibility level: `true` means private, `false` - public
    try {
      apiInstance.setPrivateSettings(owner, api, version, settings);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#setPrivateSettings");
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
| **owner** | **String**| API owner (organization or user, case-sensitive) | |
| **api** | **String**| API name (case-sensitive) | |
| **version** | **String**| Version identifier | |
| **settings** | [**VisibilitySettings**](VisibilitySettings.md)| An object that specifies the new visibility level: &#x60;true&#x60; means private, &#x60;false&#x60; - public | |

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | API visibility was updated |  -  |
| **401** | Access token is not set or invalid |  -  |
| **403** | Access denied (insufficient user permissions) |  -  |
| **404** | The specified API or version was not found |  -  |

<a id="updateApiCommentReplyV2"></a>
# **updateApiCommentReplyV2**
> Comment updateApiCommentReplyV2(owner, api, version, comment, reply, body)

Update a comment reply

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
    String api = "api_example"; // String | API name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    String comment = "comment_example"; // String | Comment identifier
    String reply = "reply_example"; // String | Reply identifier
    CommentPatch body = new CommentPatch(); // CommentPatch | 
    try {
      Comment result = apiInstance.updateApiCommentReplyV2(owner, api, version, comment, reply, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#updateApiCommentReplyV2");
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
| **owner** | **String**| API owner (organization or user, case-sensitive) | |
| **api** | **String**| API name (case-sensitive) | |
| **version** | **String**| Version identifier | |
| **comment** | **String**| Comment identifier | |
| **reply** | **String**| Reply identifier | |
| **body** | [**CommentPatch**](CommentPatch.md)|  | [optional] |

### Return type

[**Comment**](Comment.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Сomment reply was updated |  -  |
| **400** | Request body invalid |  -  |
| **401** | Access token is not set or invalid |  -  |
| **403** | The comment feature is not available for the organization&#39;s plan, or the authenticating user does not have permission to complete this action |  -  |
| **404** | The specified API, comment, or reply was not found |  -  |

<a id="updateApiCommentV2"></a>
# **updateApiCommentV2**
> ClosableComment updateApiCommentV2(owner, api, version, comment, body)

Update a comment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
    String api = "api_example"; // String | API name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    String comment = "comment_example"; // String | Comment identifier
    ClosableCommentPatch body = new ClosableCommentPatch(); // ClosableCommentPatch | 
    try {
      ClosableComment result = apiInstance.updateApiCommentV2(owner, api, version, comment, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#updateApiCommentV2");
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
| **owner** | **String**| API owner (organization or user, case-sensitive) | |
| **api** | **String**| API name (case-sensitive) | |
| **version** | **String**| Version identifier | |
| **comment** | **String**| Comment identifier | |
| **body** | [**ClosableCommentPatch**](ClosableCommentPatch.md)|  | [optional] |

### Return type

[**ClosableComment**](ClosableComment.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Comment was updated |  -  |
| **400** | Request body invalid |  -  |
| **401** | Access token is not set or invalid |  -  |
| **403** | The comment feature is not available for the organization&#39;s plan, or the authenticating user does not have permission to complete this action |  -  |
| **404** | The specified API or comment was not found |  -  |

<a id="updateApiCommentsV2"></a>
# **updateApiCommentsV2**
> updateApiCommentsV2(owner, api, version, body)

Bulk update comments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
    String api = "api_example"; // String | API name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    CommentsBatch body = new CommentsBatch(); // CommentsBatch | 
    try {
      apiInstance.updateApiCommentsV2(owner, api, version, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#updateApiCommentsV2");
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
| **owner** | **String**| API owner (organization or user, case-sensitive) | |
| **api** | **String**| API name (case-sensitive) | |
| **version** | **String**| Version identifier | |
| **body** | [**CommentsBatch**](CommentsBatch.md)|  | |

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Comments were updated |  -  |
| **400** | Request body invalid |  -  |
| **401** | Access token is not set or invalid |  -  |
| **403** | The comment feature is not available for the organization&#39;s plan, or the authenticating user does not have permission to complete this action |  -  |
| **404** | The specified API, comment, or reply was not found |  -  |

