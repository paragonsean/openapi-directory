# PropertiesApi

All URIs are relative to *https://api.bitbucket.org/2.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteCommitHostedPropertyValue**](PropertiesApi.md#deleteCommitHostedPropertyValue) | **DELETE** /repositories/{workspace}/{repo_slug}/commit/{commit}/properties/{app_key}/{property_name} | Delete a commit application property |
| [**deletePullRequestHostedPropertyValue**](PropertiesApi.md#deletePullRequestHostedPropertyValue) | **DELETE** /repositories/{workspace}/{repo_slug}/pullrequests/{pullrequest_id}/properties/{app_key}/{property_name} | Delete a pull request application property |
| [**deleteRepositoryHostedPropertyValue**](PropertiesApi.md#deleteRepositoryHostedPropertyValue) | **DELETE** /repositories/{workspace}/{repo_slug}/properties/{app_key}/{property_name} | Delete a repository application property |
| [**deleteUserHostedPropertyValue**](PropertiesApi.md#deleteUserHostedPropertyValue) | **DELETE** /users/{selected_user}/properties/{app_key}/{property_name} | Delete a user application property |
| [**getCommitHostedPropertyValue**](PropertiesApi.md#getCommitHostedPropertyValue) | **GET** /repositories/{workspace}/{repo_slug}/commit/{commit}/properties/{app_key}/{property_name} | Get a commit application property |
| [**getPullRequestHostedPropertyValue**](PropertiesApi.md#getPullRequestHostedPropertyValue) | **GET** /repositories/{workspace}/{repo_slug}/pullrequests/{pullrequest_id}/properties/{app_key}/{property_name} | Get a pull request application property |
| [**getRepositoryHostedPropertyValue**](PropertiesApi.md#getRepositoryHostedPropertyValue) | **GET** /repositories/{workspace}/{repo_slug}/properties/{app_key}/{property_name} | Get a repository application property |
| [**retrieveUserHostedPropertyValue**](PropertiesApi.md#retrieveUserHostedPropertyValue) | **GET** /users/{selected_user}/properties/{app_key}/{property_name} | Get a user application property |
| [**updateCommitHostedPropertyValue**](PropertiesApi.md#updateCommitHostedPropertyValue) | **PUT** /repositories/{workspace}/{repo_slug}/commit/{commit}/properties/{app_key}/{property_name} | Update a commit application property |
| [**updatePullRequestHostedPropertyValue**](PropertiesApi.md#updatePullRequestHostedPropertyValue) | **PUT** /repositories/{workspace}/{repo_slug}/pullrequests/{pullrequest_id}/properties/{app_key}/{property_name} | Update a pull request application property |
| [**updateRepositoryHostedPropertyValue**](PropertiesApi.md#updateRepositoryHostedPropertyValue) | **PUT** /repositories/{workspace}/{repo_slug}/properties/{app_key}/{property_name} | Update a repository application property |
| [**updateUserHostedPropertyValue**](PropertiesApi.md#updateUserHostedPropertyValue) | **PUT** /users/{selected_user}/properties/{app_key}/{property_name} | Update a user application property |


<a id="deleteCommitHostedPropertyValue"></a>
# **deleteCommitHostedPropertyValue**
> deleteCommitHostedPropertyValue(workspace, repoSlug, commit, appKey, propertyName)

Delete a commit application property

Delete an [application property](/cloud/bitbucket/application-properties/) value stored against a commit.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PropertiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PropertiesApi apiInstance = new PropertiesApi(defaultClient);
    String workspace = "workspace_example"; // String | The repository container; either the workspace slug or the UUID in curly braces.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String commit = "commit_example"; // String | The commit.
    String appKey = "appKey_example"; // String | The key of the Connect app.
    String propertyName = "propertyName_example"; // String | The name of the property.
    try {
      apiInstance.deleteCommitHostedPropertyValue(workspace, repoSlug, commit, appKey, propertyName);
    } catch (ApiException e) {
      System.err.println("Exception when calling PropertiesApi#deleteCommitHostedPropertyValue");
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
| **workspace** | **String**| The repository container; either the workspace slug or the UUID in curly braces. | |
| **repoSlug** | **String**| The repository. | |
| **commit** | **String**| The commit. | |
| **appKey** | **String**| The key of the Connect app. | |
| **propertyName** | **String**| The name of the property. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | An empty response. |  -  |

<a id="deletePullRequestHostedPropertyValue"></a>
# **deletePullRequestHostedPropertyValue**
> deletePullRequestHostedPropertyValue(workspace, repoSlug, pullrequestId, appKey, propertyName)

Delete a pull request application property

Delete an [application property](/cloud/bitbucket/application-properties/) value stored against a pull request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PropertiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PropertiesApi apiInstance = new PropertiesApi(defaultClient);
    String workspace = "workspace_example"; // String | The repository container; either the workspace slug or the UUID in curly braces.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String pullrequestId = "pullrequestId_example"; // String | The pull request ID.
    String appKey = "appKey_example"; // String | The key of the Connect app.
    String propertyName = "propertyName_example"; // String | The name of the property.
    try {
      apiInstance.deletePullRequestHostedPropertyValue(workspace, repoSlug, pullrequestId, appKey, propertyName);
    } catch (ApiException e) {
      System.err.println("Exception when calling PropertiesApi#deletePullRequestHostedPropertyValue");
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
| **workspace** | **String**| The repository container; either the workspace slug or the UUID in curly braces. | |
| **repoSlug** | **String**| The repository. | |
| **pullrequestId** | **String**| The pull request ID. | |
| **appKey** | **String**| The key of the Connect app. | |
| **propertyName** | **String**| The name of the property. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | An empty response. |  -  |

<a id="deleteRepositoryHostedPropertyValue"></a>
# **deleteRepositoryHostedPropertyValue**
> deleteRepositoryHostedPropertyValue(workspace, repoSlug, appKey, propertyName)

Delete a repository application property

Delete an [application property](/cloud/bitbucket/application-properties/) value stored against a repository.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PropertiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PropertiesApi apiInstance = new PropertiesApi(defaultClient);
    String workspace = "workspace_example"; // String | The repository container; either the workspace slug or the UUID in curly braces.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String appKey = "appKey_example"; // String | The key of the Connect app.
    String propertyName = "propertyName_example"; // String | The name of the property.
    try {
      apiInstance.deleteRepositoryHostedPropertyValue(workspace, repoSlug, appKey, propertyName);
    } catch (ApiException e) {
      System.err.println("Exception when calling PropertiesApi#deleteRepositoryHostedPropertyValue");
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
| **workspace** | **String**| The repository container; either the workspace slug or the UUID in curly braces. | |
| **repoSlug** | **String**| The repository. | |
| **appKey** | **String**| The key of the Connect app. | |
| **propertyName** | **String**| The name of the property. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | An empty response. |  -  |

<a id="deleteUserHostedPropertyValue"></a>
# **deleteUserHostedPropertyValue**
> deleteUserHostedPropertyValue(selectedUser, appKey, propertyName)

Delete a user application property

Delete an [application property](/cloud/bitbucket/application-properties/) value stored against a user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PropertiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PropertiesApi apiInstance = new PropertiesApi(defaultClient);
    String selectedUser = "selectedUser_example"; // String | Either the UUID of the account surrounded by curly-braces, for example `{account UUID}`, OR an Atlassian Account ID.
    String appKey = "appKey_example"; // String | The key of the Connect app.
    String propertyName = "propertyName_example"; // String | The name of the property.
    try {
      apiInstance.deleteUserHostedPropertyValue(selectedUser, appKey, propertyName);
    } catch (ApiException e) {
      System.err.println("Exception when calling PropertiesApi#deleteUserHostedPropertyValue");
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
| **selectedUser** | **String**| Either the UUID of the account surrounded by curly-braces, for example &#x60;{account UUID}&#x60;, OR an Atlassian Account ID. | |
| **appKey** | **String**| The key of the Connect app. | |
| **propertyName** | **String**| The name of the property. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | An empty response. |  -  |

<a id="getCommitHostedPropertyValue"></a>
# **getCommitHostedPropertyValue**
> ApplicationProperty getCommitHostedPropertyValue(workspace, repoSlug, commit, appKey, propertyName)

Get a commit application property

Retrieve an [application property](/cloud/bitbucket/application-properties/) value stored against a commit.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PropertiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PropertiesApi apiInstance = new PropertiesApi(defaultClient);
    String workspace = "workspace_example"; // String | The repository container; either the workspace slug or the UUID in curly braces.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String commit = "commit_example"; // String | The commit.
    String appKey = "appKey_example"; // String | The key of the Connect app.
    String propertyName = "propertyName_example"; // String | The name of the property.
    try {
      ApplicationProperty result = apiInstance.getCommitHostedPropertyValue(workspace, repoSlug, commit, appKey, propertyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PropertiesApi#getCommitHostedPropertyValue");
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
| **workspace** | **String**| The repository container; either the workspace slug or the UUID in curly braces. | |
| **repoSlug** | **String**| The repository. | |
| **commit** | **String**| The commit. | |
| **appKey** | **String**| The key of the Connect app. | |
| **propertyName** | **String**| The name of the property. | |

### Return type

[**ApplicationProperty**](ApplicationProperty.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The value of the property. |  -  |

<a id="getPullRequestHostedPropertyValue"></a>
# **getPullRequestHostedPropertyValue**
> ApplicationProperty getPullRequestHostedPropertyValue(workspace, repoSlug, pullrequestId, appKey, propertyName)

Get a pull request application property

Retrieve an [application property](/cloud/bitbucket/application-properties/) value stored against a pull request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PropertiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PropertiesApi apiInstance = new PropertiesApi(defaultClient);
    String workspace = "workspace_example"; // String | The repository container; either the workspace slug or the UUID in curly braces.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String pullrequestId = "pullrequestId_example"; // String | The pull request ID.
    String appKey = "appKey_example"; // String | The key of the Connect app.
    String propertyName = "propertyName_example"; // String | The name of the property.
    try {
      ApplicationProperty result = apiInstance.getPullRequestHostedPropertyValue(workspace, repoSlug, pullrequestId, appKey, propertyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PropertiesApi#getPullRequestHostedPropertyValue");
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
| **workspace** | **String**| The repository container; either the workspace slug or the UUID in curly braces. | |
| **repoSlug** | **String**| The repository. | |
| **pullrequestId** | **String**| The pull request ID. | |
| **appKey** | **String**| The key of the Connect app. | |
| **propertyName** | **String**| The name of the property. | |

### Return type

[**ApplicationProperty**](ApplicationProperty.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The value of the property. |  -  |

<a id="getRepositoryHostedPropertyValue"></a>
# **getRepositoryHostedPropertyValue**
> ApplicationProperty getRepositoryHostedPropertyValue(workspace, repoSlug, appKey, propertyName)

Get a repository application property

Retrieve an [application property](/cloud/bitbucket/application-properties/) value stored against a repository.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PropertiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PropertiesApi apiInstance = new PropertiesApi(defaultClient);
    String workspace = "workspace_example"; // String | The repository container; either the workspace slug or the UUID in curly braces.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String appKey = "appKey_example"; // String | The key of the Connect app.
    String propertyName = "propertyName_example"; // String | The name of the property.
    try {
      ApplicationProperty result = apiInstance.getRepositoryHostedPropertyValue(workspace, repoSlug, appKey, propertyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PropertiesApi#getRepositoryHostedPropertyValue");
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
| **workspace** | **String**| The repository container; either the workspace slug or the UUID in curly braces. | |
| **repoSlug** | **String**| The repository. | |
| **appKey** | **String**| The key of the Connect app. | |
| **propertyName** | **String**| The name of the property. | |

### Return type

[**ApplicationProperty**](ApplicationProperty.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The value of the property. |  -  |

<a id="retrieveUserHostedPropertyValue"></a>
# **retrieveUserHostedPropertyValue**
> ApplicationProperty retrieveUserHostedPropertyValue(selectedUser, appKey, propertyName)

Get a user application property

Retrieve an [application property](/cloud/bitbucket/application-properties/) value stored against a user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PropertiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PropertiesApi apiInstance = new PropertiesApi(defaultClient);
    String selectedUser = "selectedUser_example"; // String | Either the UUID of the account surrounded by curly-braces, for example `{account UUID}`, OR an Atlassian Account ID.
    String appKey = "appKey_example"; // String | The key of the Connect app.
    String propertyName = "propertyName_example"; // String | The name of the property.
    try {
      ApplicationProperty result = apiInstance.retrieveUserHostedPropertyValue(selectedUser, appKey, propertyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PropertiesApi#retrieveUserHostedPropertyValue");
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
| **selectedUser** | **String**| Either the UUID of the account surrounded by curly-braces, for example &#x60;{account UUID}&#x60;, OR an Atlassian Account ID. | |
| **appKey** | **String**| The key of the Connect app. | |
| **propertyName** | **String**| The name of the property. | |

### Return type

[**ApplicationProperty**](ApplicationProperty.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The value of the property. |  -  |

<a id="updateCommitHostedPropertyValue"></a>
# **updateCommitHostedPropertyValue**
> updateCommitHostedPropertyValue(workspace, repoSlug, commit, appKey, propertyName, applicationProperty)

Update a commit application property

Update an [application property](/cloud/bitbucket/application-properties/) value stored against a commit.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PropertiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PropertiesApi apiInstance = new PropertiesApi(defaultClient);
    String workspace = "workspace_example"; // String | The repository container; either the workspace slug or the UUID in curly braces.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String commit = "commit_example"; // String | The commit.
    String appKey = "appKey_example"; // String | The key of the Connect app.
    String propertyName = "propertyName_example"; // String | The name of the property.
    ApplicationProperty applicationProperty = new ApplicationProperty(); // ApplicationProperty | The application property to create or update.
    try {
      apiInstance.updateCommitHostedPropertyValue(workspace, repoSlug, commit, appKey, propertyName, applicationProperty);
    } catch (ApiException e) {
      System.err.println("Exception when calling PropertiesApi#updateCommitHostedPropertyValue");
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
| **workspace** | **String**| The repository container; either the workspace slug or the UUID in curly braces. | |
| **repoSlug** | **String**| The repository. | |
| **commit** | **String**| The commit. | |
| **appKey** | **String**| The key of the Connect app. | |
| **propertyName** | **String**| The name of the property. | |
| **applicationProperty** | [**ApplicationProperty**](ApplicationProperty.md)| The application property to create or update. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | An empty response. |  -  |

<a id="updatePullRequestHostedPropertyValue"></a>
# **updatePullRequestHostedPropertyValue**
> updatePullRequestHostedPropertyValue(workspace, repoSlug, pullrequestId, appKey, propertyName, applicationProperty)

Update a pull request application property

Update an [application property](/cloud/bitbucket/application-properties/) value stored against a pull request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PropertiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PropertiesApi apiInstance = new PropertiesApi(defaultClient);
    String workspace = "workspace_example"; // String | The repository container; either the workspace slug or the UUID in curly braces.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String pullrequestId = "pullrequestId_example"; // String | The pull request ID.
    String appKey = "appKey_example"; // String | The key of the Connect app.
    String propertyName = "propertyName_example"; // String | The name of the property.
    ApplicationProperty applicationProperty = new ApplicationProperty(); // ApplicationProperty | The application property to create or update.
    try {
      apiInstance.updatePullRequestHostedPropertyValue(workspace, repoSlug, pullrequestId, appKey, propertyName, applicationProperty);
    } catch (ApiException e) {
      System.err.println("Exception when calling PropertiesApi#updatePullRequestHostedPropertyValue");
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
| **workspace** | **String**| The repository container; either the workspace slug or the UUID in curly braces. | |
| **repoSlug** | **String**| The repository. | |
| **pullrequestId** | **String**| The pull request ID. | |
| **appKey** | **String**| The key of the Connect app. | |
| **propertyName** | **String**| The name of the property. | |
| **applicationProperty** | [**ApplicationProperty**](ApplicationProperty.md)| The application property to create or update. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | An empty response. |  -  |

<a id="updateRepositoryHostedPropertyValue"></a>
# **updateRepositoryHostedPropertyValue**
> updateRepositoryHostedPropertyValue(workspace, repoSlug, appKey, propertyName, applicationProperty)

Update a repository application property

Update an [application property](/cloud/bitbucket/application-properties/) value stored against a repository.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PropertiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PropertiesApi apiInstance = new PropertiesApi(defaultClient);
    String workspace = "workspace_example"; // String | The repository container; either the workspace slug or the UUID in curly braces.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String appKey = "appKey_example"; // String | The key of the Connect app.
    String propertyName = "propertyName_example"; // String | The name of the property.
    ApplicationProperty applicationProperty = new ApplicationProperty(); // ApplicationProperty | The application property to create or update.
    try {
      apiInstance.updateRepositoryHostedPropertyValue(workspace, repoSlug, appKey, propertyName, applicationProperty);
    } catch (ApiException e) {
      System.err.println("Exception when calling PropertiesApi#updateRepositoryHostedPropertyValue");
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
| **workspace** | **String**| The repository container; either the workspace slug or the UUID in curly braces. | |
| **repoSlug** | **String**| The repository. | |
| **appKey** | **String**| The key of the Connect app. | |
| **propertyName** | **String**| The name of the property. | |
| **applicationProperty** | [**ApplicationProperty**](ApplicationProperty.md)| The application property to create or update. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | An empty response. |  -  |

<a id="updateUserHostedPropertyValue"></a>
# **updateUserHostedPropertyValue**
> updateUserHostedPropertyValue(selectedUser, appKey, propertyName, applicationProperty)

Update a user application property

Update an [application property](/cloud/bitbucket/application-properties/) value stored against a user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PropertiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    PropertiesApi apiInstance = new PropertiesApi(defaultClient);
    String selectedUser = "selectedUser_example"; // String | Either the UUID of the account surrounded by curly-braces, for example `{account UUID}`, OR an Atlassian Account ID.
    String appKey = "appKey_example"; // String | The key of the Connect app.
    String propertyName = "propertyName_example"; // String | The name of the property.
    ApplicationProperty applicationProperty = new ApplicationProperty(); // ApplicationProperty | The application property to create or update.
    try {
      apiInstance.updateUserHostedPropertyValue(selectedUser, appKey, propertyName, applicationProperty);
    } catch (ApiException e) {
      System.err.println("Exception when calling PropertiesApi#updateUserHostedPropertyValue");
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
| **selectedUser** | **String**| Either the UUID of the account surrounded by curly-braces, for example &#x60;{account UUID}&#x60;, OR an Atlassian Account ID. | |
| **appKey** | **String**| The key of the Connect app. | |
| **propertyName** | **String**| The name of the property. | |
| **applicationProperty** | [**ApplicationProperty**](ApplicationProperty.md)| The application property to create or update. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | An empty response. |  -  |

