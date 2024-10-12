# SourceDefinitionApi

All URIs are relative to *http://airbyte.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCustomSourceDefinition**](SourceDefinitionApi.md#createCustomSourceDefinition) | **POST** /v1/source_definitions/create_custom | Creates a custom sourceDefinition for the given workspace |
| [**deleteSourceDefinition**](SourceDefinitionApi.md#deleteSourceDefinition) | **POST** /v1/source_definitions/delete | Delete a source definition |
| [**getSourceDefinition**](SourceDefinitionApi.md#getSourceDefinition) | **POST** /v1/source_definitions/get | Get source |
| [**getSourceDefinitionForWorkspace**](SourceDefinitionApi.md#getSourceDefinitionForWorkspace) | **POST** /v1/source_definitions/get_for_workspace | Get a sourceDefinition that is configured for the given workspace |
| [**grantSourceDefinitionToWorkspace**](SourceDefinitionApi.md#grantSourceDefinitionToWorkspace) | **POST** /v1/source_definitions/grant_definition | grant a private, non-custom sourceDefinition to a given workspace |
| [**listLatestSourceDefinitions**](SourceDefinitionApi.md#listLatestSourceDefinitions) | **POST** /v1/source_definitions/list_latest | List the latest sourceDefinitions Airbyte supports |
| [**listPrivateSourceDefinitions**](SourceDefinitionApi.md#listPrivateSourceDefinitions) | **POST** /v1/source_definitions/list_private | List all private, non-custom sourceDefinitions, and for each indicate whether the given workspace has a grant for using the definition. Used by admins to view and modify a given workspace&#39;s grants. |
| [**listSourceDefinitions**](SourceDefinitionApi.md#listSourceDefinitions) | **POST** /v1/source_definitions/list | List all the sourceDefinitions the current Airbyte deployment is configured to use |
| [**listSourceDefinitionsForWorkspace**](SourceDefinitionApi.md#listSourceDefinitionsForWorkspace) | **POST** /v1/source_definitions/list_for_workspace | List all the sourceDefinitions the given workspace is configured to use |
| [**revokeSourceDefinitionFromWorkspace**](SourceDefinitionApi.md#revokeSourceDefinitionFromWorkspace) | **POST** /v1/source_definitions/revoke_definition | revoke a grant to a private, non-custom sourceDefinition from a given workspace |
| [**updateSourceDefinition**](SourceDefinitionApi.md#updateSourceDefinition) | **POST** /v1/source_definitions/update | Update a sourceDefinition |


<a id="createCustomSourceDefinition"></a>
# **createCustomSourceDefinition**
> SourceDefinitionRead createCustomSourceDefinition(customSourceDefinitionCreate)

Creates a custom sourceDefinition for the given workspace

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourceDefinitionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    SourceDefinitionApi apiInstance = new SourceDefinitionApi(defaultClient);
    CustomSourceDefinitionCreate customSourceDefinitionCreate = new CustomSourceDefinitionCreate(); // CustomSourceDefinitionCreate | 
    try {
      SourceDefinitionRead result = apiInstance.createCustomSourceDefinition(customSourceDefinitionCreate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourceDefinitionApi#createCustomSourceDefinition");
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
| **customSourceDefinitionCreate** | [**CustomSourceDefinitionCreate**](CustomSourceDefinitionCreate.md)|  | [optional] |

### Return type

[**SourceDefinitionRead**](SourceDefinitionRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **422** | Input failed validation |  -  |

<a id="deleteSourceDefinition"></a>
# **deleteSourceDefinition**
> deleteSourceDefinition(sourceDefinitionIdRequestBody)

Delete a source definition

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourceDefinitionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    SourceDefinitionApi apiInstance = new SourceDefinitionApi(defaultClient);
    SourceDefinitionIdRequestBody sourceDefinitionIdRequestBody = new SourceDefinitionIdRequestBody(); // SourceDefinitionIdRequestBody | 
    try {
      apiInstance.deleteSourceDefinition(sourceDefinitionIdRequestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourceDefinitionApi#deleteSourceDefinition");
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
| **sourceDefinitionIdRequestBody** | [**SourceDefinitionIdRequestBody**](SourceDefinitionIdRequestBody.md)|  | |

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
| **204** | The resource was deleted successfully. |  -  |
| **404** | Object with given id was not found. |  -  |
| **422** | Input failed validation |  -  |

<a id="getSourceDefinition"></a>
# **getSourceDefinition**
> SourceDefinitionRead getSourceDefinition(sourceDefinitionIdRequestBody)

Get source

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourceDefinitionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    SourceDefinitionApi apiInstance = new SourceDefinitionApi(defaultClient);
    SourceDefinitionIdRequestBody sourceDefinitionIdRequestBody = new SourceDefinitionIdRequestBody(); // SourceDefinitionIdRequestBody | 
    try {
      SourceDefinitionRead result = apiInstance.getSourceDefinition(sourceDefinitionIdRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourceDefinitionApi#getSourceDefinition");
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
| **sourceDefinitionIdRequestBody** | [**SourceDefinitionIdRequestBody**](SourceDefinitionIdRequestBody.md)|  | |

### Return type

[**SourceDefinitionRead**](SourceDefinitionRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **404** | Object with given id was not found. |  -  |
| **422** | Input failed validation |  -  |

<a id="getSourceDefinitionForWorkspace"></a>
# **getSourceDefinitionForWorkspace**
> SourceDefinitionRead getSourceDefinitionForWorkspace(sourceDefinitionIdWithWorkspaceId)

Get a sourceDefinition that is configured for the given workspace

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourceDefinitionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    SourceDefinitionApi apiInstance = new SourceDefinitionApi(defaultClient);
    SourceDefinitionIdWithWorkspaceId sourceDefinitionIdWithWorkspaceId = new SourceDefinitionIdWithWorkspaceId(); // SourceDefinitionIdWithWorkspaceId | 
    try {
      SourceDefinitionRead result = apiInstance.getSourceDefinitionForWorkspace(sourceDefinitionIdWithWorkspaceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourceDefinitionApi#getSourceDefinitionForWorkspace");
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
| **sourceDefinitionIdWithWorkspaceId** | [**SourceDefinitionIdWithWorkspaceId**](SourceDefinitionIdWithWorkspaceId.md)|  | |

### Return type

[**SourceDefinitionRead**](SourceDefinitionRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **404** | Object with given id was not found. |  -  |
| **422** | Input failed validation |  -  |

<a id="grantSourceDefinitionToWorkspace"></a>
# **grantSourceDefinitionToWorkspace**
> PrivateSourceDefinitionRead grantSourceDefinitionToWorkspace(sourceDefinitionIdWithWorkspaceId)

grant a private, non-custom sourceDefinition to a given workspace

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourceDefinitionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    SourceDefinitionApi apiInstance = new SourceDefinitionApi(defaultClient);
    SourceDefinitionIdWithWorkspaceId sourceDefinitionIdWithWorkspaceId = new SourceDefinitionIdWithWorkspaceId(); // SourceDefinitionIdWithWorkspaceId | 
    try {
      PrivateSourceDefinitionRead result = apiInstance.grantSourceDefinitionToWorkspace(sourceDefinitionIdWithWorkspaceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourceDefinitionApi#grantSourceDefinitionToWorkspace");
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
| **sourceDefinitionIdWithWorkspaceId** | [**SourceDefinitionIdWithWorkspaceId**](SourceDefinitionIdWithWorkspaceId.md)|  | |

### Return type

[**PrivateSourceDefinitionRead**](PrivateSourceDefinitionRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **404** | Object with given id was not found. |  -  |
| **422** | Input failed validation |  -  |

<a id="listLatestSourceDefinitions"></a>
# **listLatestSourceDefinitions**
> SourceDefinitionReadList listLatestSourceDefinitions()

List the latest sourceDefinitions Airbyte supports

Guaranteed to retrieve the latest information on supported sources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourceDefinitionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    SourceDefinitionApi apiInstance = new SourceDefinitionApi(defaultClient);
    try {
      SourceDefinitionReadList result = apiInstance.listLatestSourceDefinitions();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourceDefinitionApi#listLatestSourceDefinitions");
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

[**SourceDefinitionReadList**](SourceDefinitionReadList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="listPrivateSourceDefinitions"></a>
# **listPrivateSourceDefinitions**
> PrivateSourceDefinitionReadList listPrivateSourceDefinitions(workspaceIdRequestBody)

List all private, non-custom sourceDefinitions, and for each indicate whether the given workspace has a grant for using the definition. Used by admins to view and modify a given workspace&#39;s grants.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourceDefinitionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    SourceDefinitionApi apiInstance = new SourceDefinitionApi(defaultClient);
    WorkspaceIdRequestBody workspaceIdRequestBody = new WorkspaceIdRequestBody(); // WorkspaceIdRequestBody | 
    try {
      PrivateSourceDefinitionReadList result = apiInstance.listPrivateSourceDefinitions(workspaceIdRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourceDefinitionApi#listPrivateSourceDefinitions");
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
| **workspaceIdRequestBody** | [**WorkspaceIdRequestBody**](WorkspaceIdRequestBody.md)|  | [optional] |

### Return type

[**PrivateSourceDefinitionReadList**](PrivateSourceDefinitionReadList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="listSourceDefinitions"></a>
# **listSourceDefinitions**
> SourceDefinitionReadList listSourceDefinitions()

List all the sourceDefinitions the current Airbyte deployment is configured to use

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourceDefinitionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    SourceDefinitionApi apiInstance = new SourceDefinitionApi(defaultClient);
    try {
      SourceDefinitionReadList result = apiInstance.listSourceDefinitions();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourceDefinitionApi#listSourceDefinitions");
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

[**SourceDefinitionReadList**](SourceDefinitionReadList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="listSourceDefinitionsForWorkspace"></a>
# **listSourceDefinitionsForWorkspace**
> SourceDefinitionReadList listSourceDefinitionsForWorkspace(workspaceIdRequestBody)

List all the sourceDefinitions the given workspace is configured to use

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourceDefinitionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    SourceDefinitionApi apiInstance = new SourceDefinitionApi(defaultClient);
    WorkspaceIdRequestBody workspaceIdRequestBody = new WorkspaceIdRequestBody(); // WorkspaceIdRequestBody | 
    try {
      SourceDefinitionReadList result = apiInstance.listSourceDefinitionsForWorkspace(workspaceIdRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourceDefinitionApi#listSourceDefinitionsForWorkspace");
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
| **workspaceIdRequestBody** | [**WorkspaceIdRequestBody**](WorkspaceIdRequestBody.md)|  | [optional] |

### Return type

[**SourceDefinitionReadList**](SourceDefinitionReadList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="revokeSourceDefinitionFromWorkspace"></a>
# **revokeSourceDefinitionFromWorkspace**
> revokeSourceDefinitionFromWorkspace(sourceDefinitionIdWithWorkspaceId)

revoke a grant to a private, non-custom sourceDefinition from a given workspace

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourceDefinitionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    SourceDefinitionApi apiInstance = new SourceDefinitionApi(defaultClient);
    SourceDefinitionIdWithWorkspaceId sourceDefinitionIdWithWorkspaceId = new SourceDefinitionIdWithWorkspaceId(); // SourceDefinitionIdWithWorkspaceId | 
    try {
      apiInstance.revokeSourceDefinitionFromWorkspace(sourceDefinitionIdWithWorkspaceId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourceDefinitionApi#revokeSourceDefinitionFromWorkspace");
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
| **sourceDefinitionIdWithWorkspaceId** | [**SourceDefinitionIdWithWorkspaceId**](SourceDefinitionIdWithWorkspaceId.md)|  | |

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
| **204** | The resource was deleted successfully. |  -  |
| **404** | Object with given id was not found. |  -  |
| **422** | Input failed validation |  -  |

<a id="updateSourceDefinition"></a>
# **updateSourceDefinition**
> SourceDefinitionRead updateSourceDefinition(sourceDefinitionUpdate)

Update a sourceDefinition

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourceDefinitionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    SourceDefinitionApi apiInstance = new SourceDefinitionApi(defaultClient);
    SourceDefinitionUpdate sourceDefinitionUpdate = new SourceDefinitionUpdate(); // SourceDefinitionUpdate | 
    try {
      SourceDefinitionRead result = apiInstance.updateSourceDefinition(sourceDefinitionUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourceDefinitionApi#updateSourceDefinition");
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
| **sourceDefinitionUpdate** | [**SourceDefinitionUpdate**](SourceDefinitionUpdate.md)|  | [optional] |

### Return type

[**SourceDefinitionRead**](SourceDefinitionRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **404** | Object with given id was not found. |  -  |
| **422** | Input failed validation |  -  |

