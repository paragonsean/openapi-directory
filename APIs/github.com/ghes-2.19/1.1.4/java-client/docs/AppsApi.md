# AppsApi

All URIs are relative to *http://HOSTNAME/api/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appsAddRepoToInstallation**](AppsApi.md#appsAddRepoToInstallation) | **PUT** /user/installations/{installation_id}/repositories/{repository_id} | Add a repository to an app installation |
| [**appsCreateContentAttachment**](AppsApi.md#appsCreateContentAttachment) | **POST** /repos/{owner}/{repo}/content_references/{content_reference_id}/attachments | Create a content attachment |
| [**appsCreateFromManifest**](AppsApi.md#appsCreateFromManifest) | **POST** /app-manifests/{code}/conversions | Create a GitHub App from a manifest |
| [**appsCreateInstallationAccessToken**](AppsApi.md#appsCreateInstallationAccessToken) | **POST** /app/installations/{installation_id}/access_tokens | Create an installation access token for an app |
| [**appsDeleteInstallation**](AppsApi.md#appsDeleteInstallation) | **DELETE** /app/installations/{installation_id} | Delete an installation for the authenticated app |
| [**appsGetAuthenticated**](AppsApi.md#appsGetAuthenticated) | **GET** /app | Get the authenticated app |
| [**appsGetBySlug**](AppsApi.md#appsGetBySlug) | **GET** /apps/{app_slug} | Get an app |
| [**appsGetInstallation**](AppsApi.md#appsGetInstallation) | **GET** /app/installations/{installation_id} | Get an installation for the authenticated app |
| [**appsGetOrgInstallation**](AppsApi.md#appsGetOrgInstallation) | **GET** /orgs/{org}/installation | Get an organization installation for the authenticated app |
| [**appsGetRepoInstallation**](AppsApi.md#appsGetRepoInstallation) | **GET** /repos/{owner}/{repo}/installation | Get a repository installation for the authenticated app |
| [**appsGetUserInstallation**](AppsApi.md#appsGetUserInstallation) | **GET** /users/{username}/installation | Get a user installation for the authenticated app |
| [**appsListInstallationReposForAuthenticatedUser**](AppsApi.md#appsListInstallationReposForAuthenticatedUser) | **GET** /user/installations/{installation_id}/repositories | List repositories accessible to the user access token |
| [**appsListInstallations**](AppsApi.md#appsListInstallations) | **GET** /app/installations | List installations for the authenticated app |
| [**appsListInstallationsForAuthenticatedUser**](AppsApi.md#appsListInstallationsForAuthenticatedUser) | **GET** /user/installations | List app installations accessible to the user access token |
| [**appsListReposAccessibleToInstallation**](AppsApi.md#appsListReposAccessibleToInstallation) | **GET** /installation/repositories | List repositories accessible to the app installation |
| [**appsRemoveRepoFromInstallation**](AppsApi.md#appsRemoveRepoFromInstallation) | **DELETE** /user/installations/{installation_id}/repositories/{repository_id} | Remove a repository from an app installation |


<a id="appsAddRepoToInstallation"></a>
# **appsAddRepoToInstallation**
> appsAddRepoToInstallation(installationId, repositoryId)

Add a repository to an app installation

Add a single repository to an installation. The authenticated user must have admin access to the repository.  You must use a personal access token (which you can create via the [command line](https://docs.github.com/enterprise-server@2.19/github/authenticating-to-github/creating-a-personal-access-token) or [Basic Authentication](https://docs.github.com/enterprise-server@2.19/rest/overview/other-authentication-methods#basic-authentication)) to access this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    AppsApi apiInstance = new AppsApi(defaultClient);
    Integer installationId = 56; // Integer | installation_id parameter
    Integer repositoryId = 56; // Integer | 
    try {
      apiInstance.appsAddRepoToInstallation(installationId, repositoryId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsAddRepoToInstallation");
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
| **installationId** | **Integer**| installation_id parameter | |
| **repositoryId** | **Integer**|  | |

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
| **204** | Response |  -  |
| **304** | Not modified |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |

<a id="appsCreateContentAttachment"></a>
# **appsCreateContentAttachment**
> ContentReferenceAttachment appsCreateContentAttachment(owner, repo, contentReferenceId, appsCreateContentAttachmentRequest)

Create a content attachment

Creates an attachment under a content reference URL in the body or comment of an issue or pull request. Use the &#x60;id&#x60; and &#x60;repository&#x60; &#x60;full_name&#x60; of the content reference from the [&#x60;content_reference&#x60; event](https://docs.github.com/enterprise-server@2.19/webhooks/event-payloads/#content_reference) to create an attachment.  The app must create a content attachment within six hours of the content reference URL being posted. See \&quot;[Using content attachments](https://docs.github.com/enterprise-server@2.19/apps/using-content-attachments/)\&quot; for details about content attachments.  You must use an [installation access token](https://docs.github.com/enterprise-server@2.19/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-an-installation) to access this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String owner = "owner_example"; // String | The owner of the repository. Determined from the `repository` `full_name` of the `content_reference` event.
    String repo = "repo_example"; // String | The name of the repository. Determined from the `repository` `full_name` of the `content_reference` event.
    Integer contentReferenceId = 56; // Integer | The `id` of the `content_reference` event.
    AppsCreateContentAttachmentRequest appsCreateContentAttachmentRequest = new AppsCreateContentAttachmentRequest(); // AppsCreateContentAttachmentRequest | 
    try {
      ContentReferenceAttachment result = apiInstance.appsCreateContentAttachment(owner, repo, contentReferenceId, appsCreateContentAttachmentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsCreateContentAttachment");
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
| **owner** | **String**| The owner of the repository. Determined from the &#x60;repository&#x60; &#x60;full_name&#x60; of the &#x60;content_reference&#x60; event. | |
| **repo** | **String**| The name of the repository. Determined from the &#x60;repository&#x60; &#x60;full_name&#x60; of the &#x60;content_reference&#x60; event. | |
| **contentReferenceId** | **Integer**| The &#x60;id&#x60; of the &#x60;content_reference&#x60; event. | |
| **appsCreateContentAttachmentRequest** | [**AppsCreateContentAttachmentRequest**](AppsCreateContentAttachmentRequest.md)|  | |

### Return type

[**ContentReferenceAttachment**](ContentReferenceAttachment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **304** | Not modified |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **410** | Gone |  -  |
| **415** | Preview header missing |  -  |
| **422** | Validation failed |  -  |

<a id="appsCreateFromManifest"></a>
# **appsCreateFromManifest**
> AppsCreateFromManifest201Response appsCreateFromManifest(code, body)

Create a GitHub App from a manifest

Use this endpoint to complete the handshake necessary when implementing the [GitHub App Manifest flow](https://docs.github.com/enterprise-server@2.19/apps/building-github-apps/creating-github-apps-from-a-manifest/). When you create a GitHub App with the manifest flow, you receive a temporary &#x60;code&#x60; used to retrieve the GitHub App&#39;s &#x60;id&#x60;, &#x60;pem&#x60; (private key), and &#x60;webhook_secret&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String code = "code_example"; // String | 
    Object body = null; // Object | 
    try {
      AppsCreateFromManifest201Response result = apiInstance.appsCreateFromManifest(code, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsCreateFromManifest");
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
| **code** | **String**|  | |
| **body** | **Object**|  | [optional] |

### Return type

[**AppsCreateFromManifest201Response**](AppsCreateFromManifest201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response |  -  |
| **404** | Resource not found |  -  |
| **422** | Validation failed |  -  |

<a id="appsCreateInstallationAccessToken"></a>
# **appsCreateInstallationAccessToken**
> InstallationToken appsCreateInstallationAccessToken(accept, installationId, appsCreateInstallationAccessTokenRequest)

Create an installation access token for an app

Creates an installation access token that enables a GitHub App to make authenticated API requests for the app&#39;s installation on an organization or individual account. Installation tokens expire one hour from the time you create them. Using an expired token produces a status code of &#x60;401 - Unauthorized&#x60;, and requires creating a new installation token. By default the installation token has access to all repositories that the installation can access. To restrict the access to specific repositories, you can provide the &#x60;repository_ids&#x60; when creating the token. When you omit &#x60;repository_ids&#x60;, the response does not contain the &#x60;repositories&#x60; key.  You must use a [JWT](https://docs.github.com/enterprise-server@2.19/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String accept = "application/vnd.github.machine-man-preview+json"; // String | This API is under preview and subject to change.
    Integer installationId = 56; // Integer | installation_id parameter
    AppsCreateInstallationAccessTokenRequest appsCreateInstallationAccessTokenRequest = new AppsCreateInstallationAccessTokenRequest(); // AppsCreateInstallationAccessTokenRequest | 
    try {
      InstallationToken result = apiInstance.appsCreateInstallationAccessToken(accept, installationId, appsCreateInstallationAccessTokenRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsCreateInstallationAccessToken");
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
| **accept** | **String**| This API is under preview and subject to change. | [default to application/vnd.github.machine-man-preview+json] |
| **installationId** | **Integer**| installation_id parameter | |
| **appsCreateInstallationAccessTokenRequest** | [**AppsCreateInstallationAccessTokenRequest**](AppsCreateInstallationAccessTokenRequest.md)|  | [optional] |

### Return type

[**InstallationToken**](InstallationToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response |  -  |
| **401** | Requires authentication |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **415** | Preview header missing |  -  |
| **422** | Validation failed |  -  |

<a id="appsDeleteInstallation"></a>
# **appsDeleteInstallation**
> appsDeleteInstallation(accept, installationId)

Delete an installation for the authenticated app

Uninstalls a GitHub App on a user, organization, or business account. You must use a [JWT](https://docs.github.com/enterprise-server@2.19/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String accept = "application/vnd.github.gambit-preview+json,application/vnd.github.machine-man-preview+json"; // String | This API is under preview and subject to change.
    Integer installationId = 56; // Integer | installation_id parameter
    try {
      apiInstance.appsDeleteInstallation(accept, installationId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsDeleteInstallation");
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
| **accept** | **String**| This API is under preview and subject to change. | [default to application/vnd.github.gambit-preview+json,application/vnd.github.machine-man-preview+json] |
| **installationId** | **Integer**| installation_id parameter | |

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
| **204** | Response |  -  |
| **404** | Resource not found |  -  |

<a id="appsGetAuthenticated"></a>
# **appsGetAuthenticated**
> Integration appsGetAuthenticated()

Get the authenticated app

Returns the GitHub App associated with the authentication credentials used. To see how many app installations are associated with this GitHub App, see the &#x60;installations_count&#x60; in the response. For more details about your app&#39;s installations, see the \&quot;[List installations for the authenticated app](https://docs.github.com/enterprise-server@2.19/rest/reference/apps#list-installations-for-the-authenticated-app)\&quot; endpoint.  You must use a [JWT](https://docs.github.com/enterprise-server@2.19/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    AppsApi apiInstance = new AppsApi(defaultClient);
    try {
      Integration result = apiInstance.appsGetAuthenticated();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsGetAuthenticated");
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

[**Integration**](Integration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="appsGetBySlug"></a>
# **appsGetBySlug**
> Integration appsGetBySlug(appSlug)

Get an app

**Note**: The &#x60;:app_slug&#x60; is just the URL-friendly name of your GitHub App. You can find this on the settings page for your GitHub App (e.g., &#x60;https://github.com/settings/apps/:app_slug&#x60;).  If the GitHub App you specify is public, you can access this endpoint without authenticating. If the GitHub App you specify is private, you must authenticate with a [personal access token](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/) or an [installation access token](https://docs.github.com/enterprise-server@2.19/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-an-installation) to access this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String appSlug = "appSlug_example"; // String | 
    try {
      Integration result = apiInstance.appsGetBySlug(appSlug);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsGetBySlug");
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
| **appSlug** | **String**|  | |

### Return type

[**Integration**](Integration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **415** | Preview header missing |  -  |

<a id="appsGetInstallation"></a>
# **appsGetInstallation**
> InstallationGhes2 appsGetInstallation(accept, installationId)

Get an installation for the authenticated app

Enables an authenticated GitHub App to find an installation&#39;s information using the installation id. The installation&#39;s account type (&#x60;target_type&#x60;) will be either an organization or a user account, depending which account the repository belongs to.  You must use a [JWT](https://docs.github.com/enterprise-server@2.19/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String accept = "application/vnd.github.machine-man-preview+json"; // String | This API is under preview and subject to change.
    Integer installationId = 56; // Integer | installation_id parameter
    try {
      InstallationGhes2 result = apiInstance.appsGetInstallation(accept, installationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsGetInstallation");
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
| **accept** | **String**| This API is under preview and subject to change. | [default to application/vnd.github.machine-man-preview+json] |
| **installationId** | **Integer**| installation_id parameter | |

### Return type

[**InstallationGhes2**](InstallationGhes2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **404** | Resource not found |  -  |
| **415** | Preview header missing |  -  |

<a id="appsGetOrgInstallation"></a>
# **appsGetOrgInstallation**
> InstallationGhes2 appsGetOrgInstallation(accept, org)

Get an organization installation for the authenticated app

Enables an authenticated GitHub App to find the organization&#39;s installation information.  You must use a [JWT](https://docs.github.com/enterprise-server@2.19/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String accept = "application/vnd.github.machine-man-preview+json"; // String | This API is under preview and subject to change.
    String org = "org_example"; // String | 
    try {
      InstallationGhes2 result = apiInstance.appsGetOrgInstallation(accept, org);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsGetOrgInstallation");
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
| **accept** | **String**| This API is under preview and subject to change. | [default to application/vnd.github.machine-man-preview+json] |
| **org** | **String**|  | |

### Return type

[**InstallationGhes2**](InstallationGhes2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="appsGetRepoInstallation"></a>
# **appsGetRepoInstallation**
> InstallationGhes2 appsGetRepoInstallation(accept, owner, repo)

Get a repository installation for the authenticated app

Enables an authenticated GitHub App to find the repository&#39;s installation information. The installation&#39;s account type will be either an organization or a user account, depending which account the repository belongs to.  You must use a [JWT](https://docs.github.com/enterprise-server@2.19/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String accept = "application/vnd.github.machine-man-preview+json"; // String | This API is under preview and subject to change.
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    try {
      InstallationGhes2 result = apiInstance.appsGetRepoInstallation(accept, owner, repo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsGetRepoInstallation");
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
| **accept** | **String**| This API is under preview and subject to change. | [default to application/vnd.github.machine-man-preview+json] |
| **owner** | **String**|  | |
| **repo** | **String**|  | |

### Return type

[**InstallationGhes2**](InstallationGhes2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **301** | Moved permanently |  -  |
| **404** | Resource not found |  -  |

<a id="appsGetUserInstallation"></a>
# **appsGetUserInstallation**
> InstallationGhes2 appsGetUserInstallation(accept, username)

Get a user installation for the authenticated app

Enables an authenticated GitHub App to find the user’s installation information.  You must use a [JWT](https://docs.github.com/enterprise-server@2.19/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String accept = "application/vnd.github.machine-man-preview+json"; // String | This API is under preview and subject to change.
    String username = "username_example"; // String | 
    try {
      InstallationGhes2 result = apiInstance.appsGetUserInstallation(accept, username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsGetUserInstallation");
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
| **accept** | **String**| This API is under preview and subject to change. | [default to application/vnd.github.machine-man-preview+json] |
| **username** | **String**|  | |

### Return type

[**InstallationGhes2**](InstallationGhes2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="appsListInstallationReposForAuthenticatedUser"></a>
# **appsListInstallationReposForAuthenticatedUser**
> AppsListInstallationReposForAuthenticatedUser200Response appsListInstallationReposForAuthenticatedUser(accept, installationId, perPage, page)

List repositories accessible to the user access token

List repositories that the authenticated user has explicit permission (&#x60;:read&#x60;, &#x60;:write&#x60;, or &#x60;:admin&#x60;) to access for an installation.  The authenticated user has explicit permission to access repositories they own, repositories where they are a collaborator, and repositories that they can access through an organization membership.  You must use a [user-to-server OAuth access token](https://docs.github.com/enterprise-server@2.19/apps/building-github-apps/identifying-and-authorizing-users-for-github-apps/#identifying-users-on-your-site), created for a user who has authorized your GitHub App, to access this endpoint.  The access the user has to each repository is included in the hash under the &#x60;permissions&#x60; key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String accept = "application/vnd.github.machine-man-preview+json"; // String | This API is under preview and subject to change.
    Integer installationId = 56; // Integer | installation_id parameter
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      AppsListInstallationReposForAuthenticatedUser200Response result = apiInstance.appsListInstallationReposForAuthenticatedUser(accept, installationId, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsListInstallationReposForAuthenticatedUser");
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
| **accept** | **String**| This API is under preview and subject to change. | [default to application/vnd.github.machine-man-preview+json] |
| **installationId** | **Integer**| installation_id parameter | |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**AppsListInstallationReposForAuthenticatedUser200Response**](AppsListInstallationReposForAuthenticatedUser200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The access the user has to each repository is included in the hash under the &#x60;permissions&#x60; key. |  * Link -  <br>  |
| **304** | Not modified |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |

<a id="appsListInstallations"></a>
# **appsListInstallations**
> List&lt;InstallationGhes2&gt; appsListInstallations(accept, perPage, page)

List installations for the authenticated app

You must use a [JWT](https://docs.github.com/enterprise-server@2.19/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.  The permissions the installation has are included under the &#x60;permissions&#x60; key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String accept = "application/vnd.github.machine-man-preview+json"; // String | This API is under preview and subject to change.
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<InstallationGhes2> result = apiInstance.appsListInstallations(accept, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsListInstallations");
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
| **accept** | **String**| This API is under preview and subject to change. | [default to application/vnd.github.machine-man-preview+json] |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;InstallationGhes2&gt;**](InstallationGhes2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The permissions the installation has are included under the &#x60;permissions&#x60; key. |  * Link -  <br>  |

<a id="appsListInstallationsForAuthenticatedUser"></a>
# **appsListInstallationsForAuthenticatedUser**
> OrgsListAppInstallations200Response appsListInstallationsForAuthenticatedUser(accept, perPage, page)

List app installations accessible to the user access token

Lists installations of your GitHub App that the authenticated user has explicit permission (&#x60;:read&#x60;, &#x60;:write&#x60;, or &#x60;:admin&#x60;) to access.  You must use a [user-to-server OAuth access token](https://docs.github.com/enterprise-server@2.19/apps/building-github-apps/identifying-and-authorizing-users-for-github-apps/#identifying-users-on-your-site), created for a user who has authorized your GitHub App, to access this endpoint.  The authenticated user has explicit permission to access repositories they own, repositories where they are a collaborator, and repositories that they can access through an organization membership.  You can find the permissions for the installation under the &#x60;permissions&#x60; key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String accept = "application/vnd.github.machine-man-preview+json"; // String | This API is under preview and subject to change.
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      OrgsListAppInstallations200Response result = apiInstance.appsListInstallationsForAuthenticatedUser(accept, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsListInstallationsForAuthenticatedUser");
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
| **accept** | **String**| This API is under preview and subject to change. | [default to application/vnd.github.machine-man-preview+json] |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**OrgsListAppInstallations200Response**](OrgsListAppInstallations200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | You can find the permissions for the installation under the &#x60;permissions&#x60; key. |  * Link -  <br>  |
| **304** | Not modified |  -  |
| **401** | Requires authentication |  -  |
| **403** | Forbidden |  -  |
| **415** | Preview header missing |  -  |

<a id="appsListReposAccessibleToInstallation"></a>
# **appsListReposAccessibleToInstallation**
> AppsListReposAccessibleToInstallation200Response appsListReposAccessibleToInstallation(accept, perPage, page)

List repositories accessible to the app installation

List repositories that an app installation can access.  You must use an [installation access token](https://docs.github.com/enterprise-server@2.19/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-an-installation) to access this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String accept = "application/vnd.github.machine-man-preview+json"; // String | This API is under preview and subject to change.
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      AppsListReposAccessibleToInstallation200Response result = apiInstance.appsListReposAccessibleToInstallation(accept, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsListReposAccessibleToInstallation");
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
| **accept** | **String**| This API is under preview and subject to change. | [default to application/vnd.github.machine-man-preview+json] |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**AppsListReposAccessibleToInstallation200Response**](AppsListReposAccessibleToInstallation200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |
| **304** | Not modified |  -  |
| **401** | Requires authentication |  -  |
| **403** | Forbidden |  -  |

<a id="appsRemoveRepoFromInstallation"></a>
# **appsRemoveRepoFromInstallation**
> appsRemoveRepoFromInstallation(installationId, repositoryId)

Remove a repository from an app installation

Remove a single repository from an installation. The authenticated user must have admin access to the repository.  You must use a personal access token (which you can create via the [command line](https://docs.github.com/enterprise-server@2.19/github/authenticating-to-github/creating-a-personal-access-token) or [Basic Authentication](https://docs.github.com/enterprise-server@2.19/rest/overview/other-authentication-methods#basic-authentication)) to access this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    AppsApi apiInstance = new AppsApi(defaultClient);
    Integer installationId = 56; // Integer | installation_id parameter
    Integer repositoryId = 56; // Integer | 
    try {
      apiInstance.appsRemoveRepoFromInstallation(installationId, repositoryId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsRemoveRepoFromInstallation");
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
| **installationId** | **Integer**| installation_id parameter | |
| **repositoryId** | **Integer**|  | |

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
| **204** | Response |  -  |
| **304** | Not modified |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |

