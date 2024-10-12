# DestinationDefinitionApi

All URIs are relative to *http://airbyte.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCustomDestinationDefinition**](DestinationDefinitionApi.md#createCustomDestinationDefinition) | **POST** /v1/destination_definitions/create_custom | Creates a custom destinationDefinition for the given workspace |
| [**deleteDestinationDefinition**](DestinationDefinitionApi.md#deleteDestinationDefinition) | **POST** /v1/destination_definitions/delete | Delete a destination definition |
| [**getDestinationDefinition**](DestinationDefinitionApi.md#getDestinationDefinition) | **POST** /v1/destination_definitions/get | Get destinationDefinition |
| [**getDestinationDefinitionForWorkspace**](DestinationDefinitionApi.md#getDestinationDefinitionForWorkspace) | **POST** /v1/destination_definitions/get_for_workspace | Get a destinationDefinition that is configured for the given workspace |
| [**grantDestinationDefinitionToWorkspace**](DestinationDefinitionApi.md#grantDestinationDefinitionToWorkspace) | **POST** /v1/destination_definitions/grant_definition | grant a private, non-custom destinationDefinition to a given workspace |
| [**listDestinationDefinitions**](DestinationDefinitionApi.md#listDestinationDefinitions) | **POST** /v1/destination_definitions/list | List all the destinationDefinitions the current Airbyte deployment is configured to use |
| [**listDestinationDefinitionsForWorkspace**](DestinationDefinitionApi.md#listDestinationDefinitionsForWorkspace) | **POST** /v1/destination_definitions/list_for_workspace | List all the destinationDefinitions the given workspace is configured to use |
| [**listLatestDestinationDefinitions**](DestinationDefinitionApi.md#listLatestDestinationDefinitions) | **POST** /v1/destination_definitions/list_latest | List the latest destinationDefinitions Airbyte supports |
| [**listPrivateDestinationDefinitions**](DestinationDefinitionApi.md#listPrivateDestinationDefinitions) | **POST** /v1/destination_definitions/list_private | List all private, non-custom destinationDefinitions, and for each indicate whether the given workspace has a grant for using the definition. Used by admins to view and modify a given workspace&#39;s grants. |
| [**revokeDestinationDefinitionFromWorkspace**](DestinationDefinitionApi.md#revokeDestinationDefinitionFromWorkspace) | **POST** /v1/destination_definitions/revoke_definition | revoke a grant to a private, non-custom destinationDefinition from a given workspace |
| [**updateDestinationDefinition**](DestinationDefinitionApi.md#updateDestinationDefinition) | **POST** /v1/destination_definitions/update | Update destinationDefinition |


<a id="createCustomDestinationDefinition"></a>
# **createCustomDestinationDefinition**
> DestinationDefinitionRead createCustomDestinationDefinition(customDestinationDefinitionCreate)

Creates a custom destinationDefinition for the given workspace

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DestinationDefinitionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    DestinationDefinitionApi apiInstance = new DestinationDefinitionApi(defaultClient);
    CustomDestinationDefinitionCreate customDestinationDefinitionCreate = new CustomDestinationDefinitionCreate(); // CustomDestinationDefinitionCreate | 
    try {
      DestinationDefinitionRead result = apiInstance.createCustomDestinationDefinition(customDestinationDefinitionCreate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DestinationDefinitionApi#createCustomDestinationDefinition");
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
| **customDestinationDefinitionCreate** | [**CustomDestinationDefinitionCreate**](CustomDestinationDefinitionCreate.md)|  | [optional] |

### Return type

[**DestinationDefinitionRead**](DestinationDefinitionRead.md)

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

<a id="deleteDestinationDefinition"></a>
# **deleteDestinationDefinition**
> deleteDestinationDefinition(destinationDefinitionIdRequestBody)

Delete a destination definition

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DestinationDefinitionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    DestinationDefinitionApi apiInstance = new DestinationDefinitionApi(defaultClient);
    DestinationDefinitionIdRequestBody destinationDefinitionIdRequestBody = new DestinationDefinitionIdRequestBody(); // DestinationDefinitionIdRequestBody | 
    try {
      apiInstance.deleteDestinationDefinition(destinationDefinitionIdRequestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling DestinationDefinitionApi#deleteDestinationDefinition");
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
| **destinationDefinitionIdRequestBody** | [**DestinationDefinitionIdRequestBody**](DestinationDefinitionIdRequestBody.md)|  | |

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

<a id="getDestinationDefinition"></a>
# **getDestinationDefinition**
> DestinationDefinitionRead getDestinationDefinition(destinationDefinitionIdRequestBody)

Get destinationDefinition

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DestinationDefinitionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    DestinationDefinitionApi apiInstance = new DestinationDefinitionApi(defaultClient);
    DestinationDefinitionIdRequestBody destinationDefinitionIdRequestBody = new DestinationDefinitionIdRequestBody(); // DestinationDefinitionIdRequestBody | 
    try {
      DestinationDefinitionRead result = apiInstance.getDestinationDefinition(destinationDefinitionIdRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DestinationDefinitionApi#getDestinationDefinition");
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
| **destinationDefinitionIdRequestBody** | [**DestinationDefinitionIdRequestBody**](DestinationDefinitionIdRequestBody.md)|  | |

### Return type

[**DestinationDefinitionRead**](DestinationDefinitionRead.md)

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

<a id="getDestinationDefinitionForWorkspace"></a>
# **getDestinationDefinitionForWorkspace**
> DestinationDefinitionRead getDestinationDefinitionForWorkspace(destinationDefinitionIdWithWorkspaceId)

Get a destinationDefinition that is configured for the given workspace

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DestinationDefinitionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    DestinationDefinitionApi apiInstance = new DestinationDefinitionApi(defaultClient);
    DestinationDefinitionIdWithWorkspaceId destinationDefinitionIdWithWorkspaceId = new DestinationDefinitionIdWithWorkspaceId(); // DestinationDefinitionIdWithWorkspaceId | 
    try {
      DestinationDefinitionRead result = apiInstance.getDestinationDefinitionForWorkspace(destinationDefinitionIdWithWorkspaceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DestinationDefinitionApi#getDestinationDefinitionForWorkspace");
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
| **destinationDefinitionIdWithWorkspaceId** | [**DestinationDefinitionIdWithWorkspaceId**](DestinationDefinitionIdWithWorkspaceId.md)|  | |

### Return type

[**DestinationDefinitionRead**](DestinationDefinitionRead.md)

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

<a id="grantDestinationDefinitionToWorkspace"></a>
# **grantDestinationDefinitionToWorkspace**
> PrivateDestinationDefinitionRead grantDestinationDefinitionToWorkspace(destinationDefinitionIdWithWorkspaceId)

grant a private, non-custom destinationDefinition to a given workspace

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DestinationDefinitionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    DestinationDefinitionApi apiInstance = new DestinationDefinitionApi(defaultClient);
    DestinationDefinitionIdWithWorkspaceId destinationDefinitionIdWithWorkspaceId = new DestinationDefinitionIdWithWorkspaceId(); // DestinationDefinitionIdWithWorkspaceId | 
    try {
      PrivateDestinationDefinitionRead result = apiInstance.grantDestinationDefinitionToWorkspace(destinationDefinitionIdWithWorkspaceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DestinationDefinitionApi#grantDestinationDefinitionToWorkspace");
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
| **destinationDefinitionIdWithWorkspaceId** | [**DestinationDefinitionIdWithWorkspaceId**](DestinationDefinitionIdWithWorkspaceId.md)|  | |

### Return type

[**PrivateDestinationDefinitionRead**](PrivateDestinationDefinitionRead.md)

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

<a id="listDestinationDefinitions"></a>
# **listDestinationDefinitions**
> DestinationDefinitionReadList listDestinationDefinitions()

List all the destinationDefinitions the current Airbyte deployment is configured to use

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DestinationDefinitionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    DestinationDefinitionApi apiInstance = new DestinationDefinitionApi(defaultClient);
    try {
      DestinationDefinitionReadList result = apiInstance.listDestinationDefinitions();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DestinationDefinitionApi#listDestinationDefinitions");
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

[**DestinationDefinitionReadList**](DestinationDefinitionReadList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="listDestinationDefinitionsForWorkspace"></a>
# **listDestinationDefinitionsForWorkspace**
> DestinationDefinitionReadList listDestinationDefinitionsForWorkspace(workspaceIdRequestBody)

List all the destinationDefinitions the given workspace is configured to use

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DestinationDefinitionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    DestinationDefinitionApi apiInstance = new DestinationDefinitionApi(defaultClient);
    WorkspaceIdRequestBody workspaceIdRequestBody = new WorkspaceIdRequestBody(); // WorkspaceIdRequestBody | 
    try {
      DestinationDefinitionReadList result = apiInstance.listDestinationDefinitionsForWorkspace(workspaceIdRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DestinationDefinitionApi#listDestinationDefinitionsForWorkspace");
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

[**DestinationDefinitionReadList**](DestinationDefinitionReadList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="listLatestDestinationDefinitions"></a>
# **listLatestDestinationDefinitions**
> DestinationDefinitionReadList listLatestDestinationDefinitions()

List the latest destinationDefinitions Airbyte supports

Guaranteed to retrieve the latest information on supported destinations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DestinationDefinitionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    DestinationDefinitionApi apiInstance = new DestinationDefinitionApi(defaultClient);
    try {
      DestinationDefinitionReadList result = apiInstance.listLatestDestinationDefinitions();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DestinationDefinitionApi#listLatestDestinationDefinitions");
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

[**DestinationDefinitionReadList**](DestinationDefinitionReadList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="listPrivateDestinationDefinitions"></a>
# **listPrivateDestinationDefinitions**
> PrivateDestinationDefinitionReadList listPrivateDestinationDefinitions(workspaceIdRequestBody)

List all private, non-custom destinationDefinitions, and for each indicate whether the given workspace has a grant for using the definition. Used by admins to view and modify a given workspace&#39;s grants.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DestinationDefinitionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    DestinationDefinitionApi apiInstance = new DestinationDefinitionApi(defaultClient);
    WorkspaceIdRequestBody workspaceIdRequestBody = new WorkspaceIdRequestBody(); // WorkspaceIdRequestBody | 
    try {
      PrivateDestinationDefinitionReadList result = apiInstance.listPrivateDestinationDefinitions(workspaceIdRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DestinationDefinitionApi#listPrivateDestinationDefinitions");
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

[**PrivateDestinationDefinitionReadList**](PrivateDestinationDefinitionReadList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="revokeDestinationDefinitionFromWorkspace"></a>
# **revokeDestinationDefinitionFromWorkspace**
> revokeDestinationDefinitionFromWorkspace(destinationDefinitionIdWithWorkspaceId)

revoke a grant to a private, non-custom destinationDefinition from a given workspace

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DestinationDefinitionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    DestinationDefinitionApi apiInstance = new DestinationDefinitionApi(defaultClient);
    DestinationDefinitionIdWithWorkspaceId destinationDefinitionIdWithWorkspaceId = new DestinationDefinitionIdWithWorkspaceId(); // DestinationDefinitionIdWithWorkspaceId | 
    try {
      apiInstance.revokeDestinationDefinitionFromWorkspace(destinationDefinitionIdWithWorkspaceId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DestinationDefinitionApi#revokeDestinationDefinitionFromWorkspace");
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
| **destinationDefinitionIdWithWorkspaceId** | [**DestinationDefinitionIdWithWorkspaceId**](DestinationDefinitionIdWithWorkspaceId.md)|  | |

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

<a id="updateDestinationDefinition"></a>
# **updateDestinationDefinition**
> DestinationDefinitionRead updateDestinationDefinition(destinationDefinitionUpdate)

Update destinationDefinition

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DestinationDefinitionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    DestinationDefinitionApi apiInstance = new DestinationDefinitionApi(defaultClient);
    DestinationDefinitionUpdate destinationDefinitionUpdate = new DestinationDefinitionUpdate(); // DestinationDefinitionUpdate | 
    try {
      DestinationDefinitionRead result = apiInstance.updateDestinationDefinition(destinationDefinitionUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DestinationDefinitionApi#updateDestinationDefinition");
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
| **destinationDefinitionUpdate** | [**DestinationDefinitionUpdate**](DestinationDefinitionUpdate.md)|  | |

### Return type

[**DestinationDefinitionRead**](DestinationDefinitionRead.md)

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

