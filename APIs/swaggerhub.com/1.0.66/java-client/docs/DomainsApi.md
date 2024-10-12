# DomainsApi

All URIs are relative to *https://api.swaggerhub.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addDomainCommentReplyV2**](DomainsApi.md#addDomainCommentReplyV2) | **POST** /domains/{owner}/{domain}/{version}/comments/{comment}/replies | Reply to a comment |
| [**addDomainCommentV2**](DomainsApi.md#addDomainCommentV2) | **POST** /domains/{owner}/{domain}/{version}/comments | Add a new comment |
| [**cloneDomain**](DomainsApi.md#cloneDomain) | **POST** /domains/{owner}/{domain}/{version}/clone | Create a new domain version |
| [**deleteDomain**](DomainsApi.md#deleteDomain) | **DELETE** /domains/{owner}/{domain} | Delete a domain |
| [**deleteDomainCommentReplyV2**](DomainsApi.md#deleteDomainCommentReplyV2) | **DELETE** /domains/{owner}/{domain}/{version}/comments/{comment}/replies/{reply} | Delete a comment reply |
| [**deleteDomainCommentV2**](DomainsApi.md#deleteDomainCommentV2) | **DELETE** /domains/{owner}/{domain}/{version}/comments/{comment} | Delete a comment |
| [**deleteDomainVersion**](DomainsApi.md#deleteDomainVersion) | **DELETE** /domains/{owner}/{domain}/{version} | Delete a domain version |
| [**forkDomain**](DomainsApi.md#forkDomain) | **POST** /domains/{owner}/{domain}/{version}/fork | Fork a domain |
| [**getDomainCommentsV2**](DomainsApi.md#getDomainCommentsV2) | **GET** /domains/{owner}/{domain}/{version}/comments | Get comments for the specified domain version |
| [**getDomainDefaultVersion**](DomainsApi.md#getDomainDefaultVersion) | **GET** /domains/{owner}/{domain}/settings/default | Get the default version of a domain |
| [**getDomainDefinition**](DomainsApi.md#getDomainDefinition) | **GET** /domains/{owner}/{domain}/{version} | Get the OpenAPI definition of the specified domain version |
| [**getDomainJsonDefinition**](DomainsApi.md#getDomainJsonDefinition) | **GET** /domains/{owner}/{domain}/{version}/domain.json | Get the OpenAPI definition for the specified domain version in JSON format |
| [**getDomainLifecycleSettings**](DomainsApi.md#getDomainLifecycleSettings) | **GET** /domains/{owner}/{domain}/{version}/settings/lifecycle | Get the published status for the specified domain and version |
| [**getDomainPrivateSettings**](DomainsApi.md#getDomainPrivateSettings) | **GET** /domains/{owner}/{domain}/{version}/settings/private | Get the visibility (public or private) of a domain version |
| [**getDomainVersions**](DomainsApi.md#getDomainVersions) | **GET** /domains/{owner}/{domain} | Get a list of domain versions |
| [**getDomainYamlDefinition**](DomainsApi.md#getDomainYamlDefinition) | **GET** /domains/{owner}/{domain}/{version}/domain.yaml | Get the OpenAPI definition for the specified domain version in YAML format |
| [**getOwnerDomains**](DomainsApi.md#getOwnerDomains) | **GET** /domains/{owner} | Get a list of domains of the specified owner |
| [**renameDomain**](DomainsApi.md#renameDomain) | **POST** /domains/{owner}/{domain}/rename | Rename a domain |
| [**saveDomainDefinition**](DomainsApi.md#saveDomainDefinition) | **POST** /domains/{owner}/{domain} | Create or update a domain |
| [**searchApisAndDomains_0**](DomainsApi.md#searchApisAndDomains_0) | **GET** /specs | Retrieve a list of currently defined APIs, domains, and templates in APIs.json format |
| [**searchDomains**](DomainsApi.md#searchDomains) | **GET** /domains | Search domains |
| [**setDomainCommentStatusV2**](DomainsApi.md#setDomainCommentStatusV2) | **PUT** /domains/{owner}/{domain}/{version}/comments/{comment}/status/{status} | Resolve or reopen a comment |
| [**setDomainDefaultVersion**](DomainsApi.md#setDomainDefaultVersion) | **PUT** /domains/{owner}/{domain}/settings/default | Set the default version for a domain |
| [**setDomainLifecycleSettings**](DomainsApi.md#setDomainLifecycleSettings) | **PUT** /domains/{owner}/{domain}/{version}/settings/lifecycle | Publish or unpublish a domain version |
| [**setDomainPrivateSettings**](DomainsApi.md#setDomainPrivateSettings) | **PUT** /domains/{owner}/{domain}/{version}/settings/private | Set the visibility (public or private) of a domain version |
| [**updateDomainCommentReplyV2**](DomainsApi.md#updateDomainCommentReplyV2) | **PATCH** /domains/{owner}/{domain}/{version}/comments/{comment}/replies/{reply} | Update a comment reply |
| [**updateDomainCommentV2**](DomainsApi.md#updateDomainCommentV2) | **PATCH** /domains/{owner}/{domain}/{version}/comments/{comment} | Update a comment |
| [**updateDomainCommentsV2**](DomainsApi.md#updateDomainCommentsV2) | **POST** /domains/{owner}/{domain}/{version}/comments/batch | Bulk update comments |


<a id="addDomainCommentReplyV2"></a>
# **addDomainCommentReplyV2**
> List&lt;Comment&gt; addDomainCommentReplyV2(owner, domain, version, comment, body)

Reply to a comment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
    String domain = "domain_example"; // String | Domain name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    String comment = "comment_example"; // String | Comment identifier
    NewReply body = new NewReply(); // NewReply | 
    try {
      List<Comment> result = apiInstance.addDomainCommentReplyV2(owner, domain, version, comment, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#addDomainCommentReplyV2");
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
| **owner** | **String**| Domain owner (organization or user, case-sensitive) | |
| **domain** | **String**| Domain name (case-sensitive) | |
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
| **200** | Newly created reply |  -  |
| **400** | Request body invalid |  -  |
| **401** | Access token is not set or invalid |  -  |
| **403** | The comment feature is not available for the organization&#39;s plan, or the authenticating user does not have permission to complete this action |  -  |
| **404** | The specified domain or comment was not found |  -  |

<a id="addDomainCommentV2"></a>
# **addDomainCommentV2**
> ClosableComment addDomainCommentV2(owner, domain, version, body)

Add a new comment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
    String domain = "domain_example"; // String | Domain name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    NewComment body = new NewComment(); // NewComment | 
    try {
      ClosableComment result = apiInstance.addDomainCommentV2(owner, domain, version, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#addDomainCommentV2");
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
| **owner** | **String**| Domain owner (organization or user, case-sensitive) | |
| **domain** | **String**| Domain name (case-sensitive) | |
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
| **200** | Newly created comment for the specified domain |  -  |
| **400** | Request body invalid |  -  |
| **401** | Access token is not set or invalid |  -  |
| **403** | The comment feature is not available for the organization&#39;s plan, or the authenticating user does not have permission to complete this action |  -  |
| **404** | The specified domain was not found |  -  |

<a id="cloneDomain"></a>
# **cloneDomain**
> cloneDomain(owner, domain, version, newVersion)

Create a new domain version

Use this operation to clone an existing domain version as a new version.  Note that the new version is not automatically set as the default version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
    String domain = "domain_example"; // String | Domain name (case-sensitive)
    String version = "version_example"; // String | The version to clone (case-sensitive)
    NewVersion newVersion = new NewVersion(); // NewVersion | An object that contains the new version number and other parameters. The version number must be in the format described in the [documentation](https://support.smartbear.com/swaggerhub/docs/apis/versioning.html#format).
    try {
      apiInstance.cloneDomain(owner, domain, version, newVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#cloneDomain");
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
| **owner** | **String**| Domain owner (organization or user, case-sensitive) | |
| **domain** | **String**| Domain name (case-sensitive) | |
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
| **201** | New domain version was successfully created |  -  |
| **400** | Bad request |  -  |
| **403** | Access denied |  -  |
| **404** | The specified domain or version was not found |  -  |
| **409** | The domain version you are trying to create already exists |  -  |

<a id="deleteDomain"></a>
# **deleteDomain**
> deleteDomain(owner, domain, force)

Delete a domain

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
    String domain = "domain_example"; // String | Domain name (case-sensitive)
    Boolean force = false; // Boolean | If this domain is referenced from other APIs and domains, this parameter must be `true`. Otherwise, the request will be rejected with status code 424.
    try {
      apiInstance.deleteDomain(owner, domain, force);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#deleteDomain");
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
| **owner** | **String**| Domain owner (organization or user, case-sensitive) | |
| **domain** | **String**| Domain name (case-sensitive) | |
| **force** | **Boolean**| If this domain is referenced from other APIs and domains, this parameter must be &#x60;true&#x60;. Otherwise, the request will be rejected with status code 424. | [optional] [default to false] |

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The domain was successfully deleted |  -  |
| **403** | Access denied |  -  |
| **404** | The specified domain not found |  -  |
| **409** | The domain has published versions and can not be deleted |  -  |
| **424** | The domain you are trying to delete is referenced from other APIs and domains. To delete it anyway, repeat the request with the &#x60;force&#x3D;true&#x60; query parameter.  The response body contains a list of APIs and domains that reference this domain. |  -  |

<a id="deleteDomainCommentReplyV2"></a>
# **deleteDomainCommentReplyV2**
> deleteDomainCommentReplyV2(owner, domain, version, comment, reply)

Delete a comment reply

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
    String domain = "domain_example"; // String | Domain name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    String comment = "comment_example"; // String | Comment identifier
    String reply = "reply_example"; // String | Reply identifier
    try {
      apiInstance.deleteDomainCommentReplyV2(owner, domain, version, comment, reply);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#deleteDomainCommentReplyV2");
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
| **owner** | **String**| Domain owner (organization or user, case-sensitive) | |
| **domain** | **String**| Domain name (case-sensitive) | |
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
| **200** | Comment reply was deleted |  -  |
| **401** | Access token is not set or invalid |  -  |
| **403** | The comment feature is not available for the organization&#39;s plan, or the authenticating user does not have permission to complete this action |  -  |
| **404** | The specified domain, comment, or reply was not found |  -  |

<a id="deleteDomainCommentV2"></a>
# **deleteDomainCommentV2**
> deleteDomainCommentV2(owner, domain, version, comment)

Delete a comment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
    String domain = "domain_example"; // String | Domain name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    String comment = "comment_example"; // String | Comment identifier
    try {
      apiInstance.deleteDomainCommentV2(owner, domain, version, comment);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#deleteDomainCommentV2");
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
| **owner** | **String**| Domain owner (organization or user, case-sensitive) | |
| **domain** | **String**| Domain name (case-sensitive) | |
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
| **404** | The specified domain or comment was not found |  -  |

<a id="deleteDomainVersion"></a>
# **deleteDomainVersion**
> deleteDomainVersion(owner, domain, version, force)

Delete a domain version

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
    String domain = "domain_example"; // String | Domain name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    Boolean force = false; // Boolean | If this domain version is referenced from other APIs and domains, this parameter must be `true`. Otherwise, the request will be rejected with status code 424.
    try {
      apiInstance.deleteDomainVersion(owner, domain, version, force);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#deleteDomainVersion");
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
| **owner** | **String**| Domain owner (organization or user, case-sensitive) | |
| **domain** | **String**| Domain name (case-sensitive) | |
| **version** | **String**| Version identifier | |
| **force** | **Boolean**| If this domain version is referenced from other APIs and domains, this parameter must be &#x60;true&#x60;. Otherwise, the request will be rejected with status code 424. | [optional] [default to false] |

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The domain version was successfully deleted |  -  |
| **403** | Access denied |  -  |
| **404** | The specified domain or version was not found |  -  |
| **409** | The domain version is published and can not be deleted or it is the only version of this domain |  -  |
| **424** | The domain version you are trying to delete is referenced from other APIs and domains. To delete it anyway, repeat the request with the &#x60;force&#x3D;true&#x60; query parameter.  The response body contains a list of APIs and domains that reference this domain version. |  -  |

<a id="forkDomain"></a>
# **forkDomain**
> forkDomain(owner, domain, version, forkVersion)

Fork a domain

Creates a [fork](https://support.smartbear.com/swaggerhub/docs/apis/forking-api.html) of the specified domain definition and version. The fork can be created as a new domain, or as a new version in another existing domain.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
    String domain = "domain_example"; // String | Domain name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    ForkVersion forkVersion = new ForkVersion(); // ForkVersion | Fork parameters
    try {
      apiInstance.forkDomain(owner, domain, version, forkVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#forkDomain");
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
| **owner** | **String**| Domain owner (organization or user, case-sensitive) | |
| **domain** | **String**| Domain name (case-sensitive) | |
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
| **201** | The domain was successfully forked |  -  |
| **400** | Some parameters are missing or invalid |  -  |
| **401** | Access token is not set or invalid |  -  |
| **403** | Access denied |  -  |
| **404** | The specified owner or domain was not found |  -  |
| **409** | A domain with the name and version you&#39;re trying to create already exists |  -  |

<a id="getDomainCommentsV2"></a>
# **getDomainCommentsV2**
> List&lt;ClosableComment&gt; getDomainCommentsV2(owner, domain, version)

Get comments for the specified domain version

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
    String domain = "domain_example"; // String | Domain name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    try {
      List<ClosableComment> result = apiInstance.getDomainCommentsV2(owner, domain, version);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#getDomainCommentsV2");
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
| **owner** | **String**| Domain owner (organization or user, case-sensitive) | |
| **domain** | **String**| Domain name (case-sensitive) | |
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
| **200** | Comments for the specified domain version |  -  |
| **204** | No comments were found for the specified domain version |  -  |
| **401** | Access token is not set or invalid |  -  |
| **403** | The comment feature is not available for the organization&#39;s plan, or the authenticating user does not have permission to complete this action |  -  |
| **404** | The specified domain was not found |  -  |

<a id="getDomainDefaultVersion"></a>
# **getDomainDefaultVersion**
> DefaultVersion getDomainDefaultVersion(owner, domain)

Get the default version of a domain

This operation returns the version identifier, such as &#x60;1.0.0&#x60;. To get the definition itself, use &#x60;GET /domains/{owner}/{domain}/{version}&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
    String domain = "domain_example"; // String | Domain name (case-sensitive)
    try {
      DefaultVersion result = apiInstance.getDomainDefaultVersion(owner, domain);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#getDomainDefaultVersion");
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
| **owner** | **String**| Domain owner (organization or user, case-sensitive) | |
| **domain** | **String**| Domain name (case-sensitive) | |

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
| **200** | The default version identifier for this domain |  -  |
| **404** | The specified API was not found. If it is private, make sure the request is authenticated. |  -  |

<a id="getDomainDefinition"></a>
# **getDomainDefinition**
> Object getDomainDefinition(owner, domain, version)

Get the OpenAPI definition of the specified domain version

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
    String domain = "domain_example"; // String | Domain name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    try {
      Object result = apiInstance.getDomainDefinition(owner, domain, version);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#getDomainDefinition");
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
| **owner** | **String**| Domain owner (organization or user, case-sensitive) | |
| **domain** | **String**| Domain name (case-sensitive) | |
| **version** | **String**| Version identifier | |

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
| **200** | OpenAPI definition of a domain in the requested format (YAML or JSON) |  -  |
| **404** | The specified domain or version was not found. If it is private, make sure the request is authenticated and the authenticating user has access to this API. |  -  |

<a id="getDomainJsonDefinition"></a>
# **getDomainJsonDefinition**
> Object getDomainJsonDefinition(owner, domain, version)

Get the OpenAPI definition for the specified domain version in JSON format

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
    String domain = "domain_example"; // String | Domain name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    try {
      Object result = apiInstance.getDomainJsonDefinition(owner, domain, version);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#getDomainJsonDefinition");
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
| **owner** | **String**| Domain owner (organization or user, case-sensitive) | |
| **domain** | **String**| Domain name (case-sensitive) | |
| **version** | **String**| Version identifier | |

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
| **200** | Domain definition in JSON format |  -  |
| **404** | The specified domain or version was not found. If it is private, make sure the request is authenticated and the authenticating user has access to this API. |  -  |

<a id="getDomainLifecycleSettings"></a>
# **getDomainLifecycleSettings**
> LifecycleSettings getDomainLifecycleSettings(owner, domain, version)

Get the published status for the specified domain and version

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
    String domain = "domain_example"; // String | Domain name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    try {
      LifecycleSettings result = apiInstance.getDomainLifecycleSettings(owner, domain, version);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#getDomainLifecycleSettings");
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
| **owner** | **String**| Domain owner (organization or user, case-sensitive) | |
| **domain** | **String**| Domain name (case-sensitive) | |
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
| **200** | The published status of this domain version |  -  |
| **401** | Access token is not set or invalid |  -  |
| **404** | The specified domain or version was not found |  -  |

<a id="getDomainPrivateSettings"></a>
# **getDomainPrivateSettings**
> VisibilitySettings getDomainPrivateSettings(owner, domain, version)

Get the visibility (public or private) of a domain version

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
    String domain = "domain_example"; // String | Domain name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    try {
      VisibilitySettings result = apiInstance.getDomainPrivateSettings(owner, domain, version);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#getDomainPrivateSettings");
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
| **owner** | **String**| Domain owner (organization or user, case-sensitive) | |
| **domain** | **String**| Domain name (case-sensitive) | |
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
| **200** | The response body indicates whether this domain version is private (&#x60;true&#x60;) or public (&#x60;false&#x60;) |  -  |
| **401** | Access token is not set or invalid |  -  |
| **404** | The specified domain or version was not found |  -  |

<a id="getDomainVersions"></a>
# **getDomainVersions**
> ApisJson getDomainVersions(owner, domain)

Get a list of domain versions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
    String domain = "domain_example"; // String | Domain name (case-sensitive)
    try {
      ApisJson result = apiInstance.getDomainVersions(owner, domain);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#getDomainVersions");
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
| **owner** | **String**| Domain owner (organization or user, case-sensitive) | |
| **domain** | **String**| Domain name (case-sensitive) | |

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
| **200** | A list of domain versions in APIs.json format |  -  |
| **404** | The specified domain was not found. If it is private, make sure the request is authenticated and the authenticating user has access to this API. |  -  |

<a id="getDomainYamlDefinition"></a>
# **getDomainYamlDefinition**
> Object getDomainYamlDefinition(owner, domain, version)

Get the OpenAPI definition for the specified domain version in YAML format

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
    String domain = "domain_example"; // String | Domain name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    try {
      Object result = apiInstance.getDomainYamlDefinition(owner, domain, version);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#getDomainYamlDefinition");
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
| **owner** | **String**| Domain owner (organization or user, case-sensitive) | |
| **domain** | **String**| Domain name (case-sensitive) | |
| **version** | **String**| Version identifier | |

### Return type

**Object**

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Domain definition in YAML format |  -  |
| **404** | The specified domain or version was not found. If it is private, make sure the request is authenticated and the authenticating user has access to this API. |  -  |

<a id="getOwnerDomains"></a>
# **getOwnerDomains**
> ApisJson getOwnerDomains(owner, page, limit, sort, order)

Get a list of domains of the specified owner

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
    Integer page = 0; // Integer | Page to return
    Integer limit = 10; // Integer | Number of results per page (1 .. 100)
    String sort = "NAME"; // String | Sort criteria of result set: * NAME * UPDATED * CREATED * OWNER * BEST_MATCH - by relevance * TITLE - by `info.title` 
    String order = "ASC"; // String | Sort order
    try {
      ApisJson result = apiInstance.getOwnerDomains(owner, page, limit, sort, order);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#getOwnerDomains");
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
| **owner** | **String**| Domain owner (organization or user, case-sensitive) | |
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
| **200** | A list of domains in APIs.json format |  -  |

<a id="renameDomain"></a>
# **renameDomain**
> renameDomain(owner, domain, newName, force)

Rename a domain

The new name must follow the [naming rules](https://support.smartbear.com/swaggerhub/docs/apis/creating-api.html).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
    String domain = "domain_example"; // String | Domain name (case-sensitive)
    String newName = "newName_example"; // String | New name
    Boolean force = false; // Boolean | If this domain is referenced from other APIs and domains, this parameter must be true. Otherwise, the request will be rejected with status code 424.
    try {
      apiInstance.renameDomain(owner, domain, newName, force);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#renameDomain");
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
| **owner** | **String**| Domain owner (organization or user, case-sensitive) | |
| **domain** | **String**| Domain name (case-sensitive) | |
| **newName** | **String**| New name | |
| **force** | **Boolean**| If this domain is referenced from other APIs and domains, this parameter must be true. Otherwise, the request will be rejected with status code 424. | [optional] [default to false] |

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The domain was successfully renamed |  -  |
| **401** | Access token is not set or invalid |  -  |
| **403** | Access denied (insufficient user permissions) |  -  |
| **409** | An API or domain with the new name already exists, or the new and old names are the same |  -  |
| **424** | The domain you are trying to rename is referenced from other APIs or domains. Renaming the domain will break the references in those definitions. To rename the domain anyway, repeat the request with the &#x60;force&#x3D;true&#x60; query parameter.  The response body contains a list of APIs and domains that reference this domain. |  -  |

<a id="saveDomainDefinition"></a>
# **saveDomainDefinition**
> saveDomainDefinition(owner, domain, isPrivate, version, force, definition)

Create or update a domain

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
    String domain = "domain_example"; // String | Domain name (case-sensitive)
    Boolean isPrivate = false; // Boolean | Specifies whether the domain has to be private
    String version = "version_example"; // String | Domain version. If omitted, will be taken from the `info.version` field in the definition.
    Boolean force = true; // Boolean | Force update
    String definition = "definition_example"; // String | OpenAPI definition of this domain
    try {
      apiInstance.saveDomainDefinition(owner, domain, isPrivate, version, force, definition);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#saveDomainDefinition");
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
| **owner** | **String**| Domain owner (organization or user, case-sensitive) | |
| **domain** | **String**| Domain name (case-sensitive) | |
| **isPrivate** | **Boolean**| Specifies whether the domain has to be private | [optional] [default to false] |
| **version** | **String**| Domain version. If omitted, will be taken from the &#x60;info.version&#x60; field in the definition. | [optional] |
| **force** | **Boolean**| Force update | [optional] |
| **definition** | **String**| OpenAPI definition of this domain | [optional] |

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
| **200** | The domain was successfully saved |  -  |
| **201** | New domain was successfully saved |  -  |
| **205** | The domain was successfully saved and should be reloaded |  -  |
| **400** | Possible reasons:   * Some parameter values are invalid, or the provided OpenAPI domain definition is invalid.  * The specified &#x60;projectName&#x60; does not exist in the &#x60;owner&#x60; organization.  * Cannot create a new domain because an API with this name already exists in the &#x60;owner&#x60; account. Try a different name. |  -  |
| **403** | Maximum number of domains reached |  -  |
| **409** | Cannot overwrite a published domain version |  -  |
| **415** | Invalid content type |  -  |

<a id="searchApisAndDomains_0"></a>
# **searchApisAndDomains_0**
> ApisJson searchApisAndDomains_0(specType, visibility, state, owner, query, page, limit, sort, order)

Retrieve a list of currently defined APIs, domains, and templates in APIs.json format

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
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
      ApisJson result = apiInstance.searchApisAndDomains_0(specType, visibility, state, owner, query, page, limit, sort, order);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#searchApisAndDomains_0");
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

<a id="searchDomains"></a>
# **searchDomains**
> searchDomains(query, state, page, limit, sort, order)

Search domains

This is a convenience alias for &#x60;GET /specs?specType&#x3D;DOMAIN&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String query = "query_example"; // String | Free text query to match
    String state = "ALL"; // String | Matches against published state of the spec: * UNPUBLISHED - spec is a draft, a work in progress * PUBLISHED - spec is a stable version ready for consuming from client applications * ANY - either PUBLISHED or UNPUBLISHED 
    Integer page = 0; // Integer | Page to return
    Integer limit = 10; // Integer | Number of results per page (1 .. 100)
    String sort = "NAME"; // String | Sort criteria of result set: * NAME * UPDATED * CREATED * OWNER * BEST_MATCH - by relevance * TITLE - by `info.title` 
    String order = "ASC"; // String | Sort order
    try {
      apiInstance.searchDomains(query, state, page, limit, sort, order);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#searchDomains");
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

<a id="setDomainCommentStatusV2"></a>
# **setDomainCommentStatusV2**
> setDomainCommentStatusV2(owner, domain, version, comment, status)

Resolve or reopen a comment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
    String domain = "domain_example"; // String | Domain name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    String comment = "comment_example"; // String | Comment identifier
    String status = "OPEN"; // String | Comment status
    try {
      apiInstance.setDomainCommentStatusV2(owner, domain, version, comment, status);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#setDomainCommentStatusV2");
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
| **owner** | **String**| Domain owner (organization or user, case-sensitive) | |
| **domain** | **String**| Domain name (case-sensitive) | |
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
| **404** | The specified domain or comment was not found |  -  |

<a id="setDomainDefaultVersion"></a>
# **setDomainDefaultVersion**
> setDomainDefaultVersion(owner, domain, defaultVersion)

Set the default version for a domain

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
    String domain = "domain_example"; // String | Domain name (case-sensitive)
    DefaultVersion defaultVersion = new DefaultVersion(); // DefaultVersion | An object that specifies the default version for this domain
    try {
      apiInstance.setDomainDefaultVersion(owner, domain, defaultVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#setDomainDefaultVersion");
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
| **owner** | **String**| Domain owner (organization or user, case-sensitive) | |
| **domain** | **String**| Domain name (case-sensitive) | |
| **defaultVersion** | [**DefaultVersion**](DefaultVersion.md)| An object that specifies the default version for this domain | |

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
| **404** | The specified domain or version was not found |  -  |

<a id="setDomainLifecycleSettings"></a>
# **setDomainLifecycleSettings**
> setDomainLifecycleSettings(owner, domain, version, settings, force)

Publish or unpublish a domain version

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
    String domain = "domain_example"; // String | Domain name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    LifecycleSettings settings = new LifecycleSettings(); // LifecycleSettings | An object that specifies the new `published` state: `true` means published, `false` - unpublished
    Boolean force = false; // Boolean | To publish a domain that references other _unpublished_ domains, this parameter must be `true`. Otherwise, the request will be rejected with status code 424.
    try {
      apiInstance.setDomainLifecycleSettings(owner, domain, version, settings, force);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#setDomainLifecycleSettings");
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
| **owner** | **String**| Domain owner (organization or user, case-sensitive) | |
| **domain** | **String**| Domain name (case-sensitive) | |
| **version** | **String**| Version identifier | |
| **settings** | [**LifecycleSettings**](LifecycleSettings.md)| An object that specifies the new &#x60;published&#x60; state: &#x60;true&#x60; means published, &#x60;false&#x60; - unpublished | |
| **force** | **Boolean**| To publish a domain that references other _unpublished_ domains, this parameter must be &#x60;true&#x60;. Otherwise, the request will be rejected with status code 424. | [optional] [default to false] |

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
| **200** | Successfully published or unpublished the domain |  -  |
| **401** | Access token is not set or invalid |  -  |
| **403** | Access denied (insufficient user permissions) |  -  |
| **404** | The specified domain or version was not found |  -  |
| **424** | The domain version you are trying to publish contains references to other _unpublished_ domains. If those domains change, it may affect your domain. To publish the domain anyway, repeat the request with the &#x60;force&#x3D;true&#x60; query parameter.  The response body contains a list of unpublished domains referenced from this domain. |  -  |

<a id="setDomainPrivateSettings"></a>
# **setDomainPrivateSettings**
> setDomainPrivateSettings(owner, domain, version, settings, force)

Set the visibility (public or private) of a domain version

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
    String domain = "domain_example"; // String | Domain name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    VisibilitySettings settings = new VisibilitySettings(); // VisibilitySettings | An object that specifies the new visibility level: `true` means private, `false` - public
    Boolean force = false; // Boolean | To change the visibility from _public_ to _private_ in case this domain is referenced from other _public_ definitions, this parameter must be `true`. Otherwise, the request will be rejected with status code 424.
    try {
      apiInstance.setDomainPrivateSettings(owner, domain, version, settings, force);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#setDomainPrivateSettings");
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
| **owner** | **String**| Domain owner (organization or user, case-sensitive) | |
| **domain** | **String**| Domain name (case-sensitive) | |
| **version** | **String**| Version identifier | |
| **settings** | [**VisibilitySettings**](VisibilitySettings.md)| An object that specifies the new visibility level: &#x60;true&#x60; means private, &#x60;false&#x60; - public | |
| **force** | **Boolean**| To change the visibility from _public_ to _private_ in case this domain is referenced from other _public_ definitions, this parameter must be &#x60;true&#x60;. Otherwise, the request will be rejected with status code 424. | [optional] [default to false] |

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
| **200** | Domain visibility was updated |  -  |
| **401** | Access token is not set or invalid |  -  |
| **403** | Access denied (insufficient user permissions) |  -  |
| **404** | The specified domain or version was not found |  -  |
| **424** | The domain version you are trying to make _private_ is referenced from other _public_ definitions. Changing domain visibility may affect those definitions. To proceed anyway, repeat the request with the &#x60;force&#x3D;true&#x60; query parameter.  The response body contains a list of APIs and domains that may be affected by this change. |  -  |

<a id="updateDomainCommentReplyV2"></a>
# **updateDomainCommentReplyV2**
> Comment updateDomainCommentReplyV2(owner, domain, version, comment, reply, body)

Update a comment reply

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
    String domain = "domain_example"; // String | Domain name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    String comment = "comment_example"; // String | Comment identifier
    String reply = "reply_example"; // String | Reply identifier
    CommentPatch body = new CommentPatch(); // CommentPatch | 
    try {
      Comment result = apiInstance.updateDomainCommentReplyV2(owner, domain, version, comment, reply, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#updateDomainCommentReplyV2");
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
| **owner** | **String**| Domain owner (organization or user, case-sensitive) | |
| **domain** | **String**| Domain name (case-sensitive) | |
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
| **200** | Comment reply was updated |  -  |
| **400** | Request body invalid |  -  |
| **401** | Access token is not set or invalid |  -  |
| **403** | The comment feature is not available for the organization&#39;s plan, or the authenticating user does not have permission to complete this action |  -  |
| **404** | The specified domain, comment, or reply was not found |  -  |

<a id="updateDomainCommentV2"></a>
# **updateDomainCommentV2**
> ClosableComment updateDomainCommentV2(owner, domain, version, comment, body)

Update a comment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
    String domain = "domain_example"; // String | Domain name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    String comment = "comment_example"; // String | Comment identifier
    ClosableCommentPatch body = new ClosableCommentPatch(); // ClosableCommentPatch | 
    try {
      ClosableComment result = apiInstance.updateDomainCommentV2(owner, domain, version, comment, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#updateDomainCommentV2");
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
| **owner** | **String**| Domain owner (organization or user, case-sensitive) | |
| **domain** | **String**| Domain name (case-sensitive) | |
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
| **404** | The specified domain or comment was not found |  -  |

<a id="updateDomainCommentsV2"></a>
# **updateDomainCommentsV2**
> updateDomainCommentsV2(owner, domain, version, body)

Bulk update comments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
    String domain = "domain_example"; // String | Domain name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    CommentsBatch body = new CommentsBatch(); // CommentsBatch | 
    try {
      apiInstance.updateDomainCommentsV2(owner, domain, version, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#updateDomainCommentsV2");
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
| **owner** | **String**| Domain owner (organization or user, case-sensitive) | |
| **domain** | **String**| Domain name (case-sensitive) | |
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
| **404** | The specified domain, comment, or reply was not found |  -  |

