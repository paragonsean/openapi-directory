# SourceApi

All URIs are relative to *http://airbyte.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**checkConnectionToSource**](SourceApi.md#checkConnectionToSource) | **POST** /v1/sources/check_connection | Check connection to the source |
| [**checkConnectionToSourceForUpdate**](SourceApi.md#checkConnectionToSourceForUpdate) | **POST** /v1/sources/check_connection_for_update | Check connection for a proposed update to a source |
| [**cloneSource**](SourceApi.md#cloneSource) | **POST** /v1/sources/clone | Clone source |
| [**createSource**](SourceApi.md#createSource) | **POST** /v1/sources/create | Create a source |
| [**deleteSource**](SourceApi.md#deleteSource) | **POST** /v1/sources/delete | Delete a source |
| [**discoverSchemaForSource**](SourceApi.md#discoverSchemaForSource) | **POST** /v1/sources/discover_schema | Discover the schema catalog of the source |
| [**getMostRecentSourceActorCatalog**](SourceApi.md#getMostRecentSourceActorCatalog) | **POST** /v1/sources/most_recent_source_actor_catalog | Get most recent ActorCatalog for source |
| [**getSource**](SourceApi.md#getSource) | **POST** /v1/sources/get | Get source |
| [**listSourcesForWorkspace**](SourceApi.md#listSourcesForWorkspace) | **POST** /v1/sources/list | List sources for workspace |
| [**searchSources**](SourceApi.md#searchSources) | **POST** /v1/sources/search | Search sources |
| [**updateSource**](SourceApi.md#updateSource) | **POST** /v1/sources/update | Update a source |
| [**writeDiscoverCatalogResult**](SourceApi.md#writeDiscoverCatalogResult) | **POST** /v1/sources/write_discover_catalog_result | Should only called from worker, to write result from discover activity back to DB. |


<a id="checkConnectionToSource"></a>
# **checkConnectionToSource**
> CheckConnectionRead checkConnectionToSource(sourceIdRequestBody)

Check connection to the source

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    SourceApi apiInstance = new SourceApi(defaultClient);
    SourceIdRequestBody sourceIdRequestBody = new SourceIdRequestBody(); // SourceIdRequestBody | 
    try {
      CheckConnectionRead result = apiInstance.checkConnectionToSource(sourceIdRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourceApi#checkConnectionToSource");
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
| **sourceIdRequestBody** | [**SourceIdRequestBody**](SourceIdRequestBody.md)|  | |

### Return type

[**CheckConnectionRead**](CheckConnectionRead.md)

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

<a id="checkConnectionToSourceForUpdate"></a>
# **checkConnectionToSourceForUpdate**
> CheckConnectionRead checkConnectionToSourceForUpdate(sourceUpdate)

Check connection for a proposed update to a source

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    SourceApi apiInstance = new SourceApi(defaultClient);
    SourceUpdate sourceUpdate = new SourceUpdate(); // SourceUpdate | 
    try {
      CheckConnectionRead result = apiInstance.checkConnectionToSourceForUpdate(sourceUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourceApi#checkConnectionToSourceForUpdate");
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
| **sourceUpdate** | [**SourceUpdate**](SourceUpdate.md)|  | |

### Return type

[**CheckConnectionRead**](CheckConnectionRead.md)

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

<a id="cloneSource"></a>
# **cloneSource**
> SourceRead cloneSource(sourceCloneRequestBody)

Clone source

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    SourceApi apiInstance = new SourceApi(defaultClient);
    SourceCloneRequestBody sourceCloneRequestBody = new SourceCloneRequestBody(); // SourceCloneRequestBody | 
    try {
      SourceRead result = apiInstance.cloneSource(sourceCloneRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourceApi#cloneSource");
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
| **sourceCloneRequestBody** | [**SourceCloneRequestBody**](SourceCloneRequestBody.md)|  | |

### Return type

[**SourceRead**](SourceRead.md)

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

<a id="createSource"></a>
# **createSource**
> SourceRead createSource(sourceCreate)

Create a source

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    SourceApi apiInstance = new SourceApi(defaultClient);
    SourceCreate sourceCreate = new SourceCreate(); // SourceCreate | 
    try {
      SourceRead result = apiInstance.createSource(sourceCreate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourceApi#createSource");
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
| **sourceCreate** | [**SourceCreate**](SourceCreate.md)|  | |

### Return type

[**SourceRead**](SourceRead.md)

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

<a id="deleteSource"></a>
# **deleteSource**
> deleteSource(sourceIdRequestBody)

Delete a source

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    SourceApi apiInstance = new SourceApi(defaultClient);
    SourceIdRequestBody sourceIdRequestBody = new SourceIdRequestBody(); // SourceIdRequestBody | 
    try {
      apiInstance.deleteSource(sourceIdRequestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourceApi#deleteSource");
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
| **sourceIdRequestBody** | [**SourceIdRequestBody**](SourceIdRequestBody.md)|  | |

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

<a id="discoverSchemaForSource"></a>
# **discoverSchemaForSource**
> SourceDiscoverSchemaRead discoverSchemaForSource(sourceDiscoverSchemaRequestBody)

Discover the schema catalog of the source

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    SourceApi apiInstance = new SourceApi(defaultClient);
    SourceDiscoverSchemaRequestBody sourceDiscoverSchemaRequestBody = new SourceDiscoverSchemaRequestBody(); // SourceDiscoverSchemaRequestBody | 
    try {
      SourceDiscoverSchemaRead result = apiInstance.discoverSchemaForSource(sourceDiscoverSchemaRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourceApi#discoverSchemaForSource");
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
| **sourceDiscoverSchemaRequestBody** | [**SourceDiscoverSchemaRequestBody**](SourceDiscoverSchemaRequestBody.md)|  | |

### Return type

[**SourceDiscoverSchemaRead**](SourceDiscoverSchemaRead.md)

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

<a id="getMostRecentSourceActorCatalog"></a>
# **getMostRecentSourceActorCatalog**
> ActorCatalogWithUpdatedAt getMostRecentSourceActorCatalog(sourceIdRequestBody)

Get most recent ActorCatalog for source

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    SourceApi apiInstance = new SourceApi(defaultClient);
    SourceIdRequestBody sourceIdRequestBody = new SourceIdRequestBody(); // SourceIdRequestBody | 
    try {
      ActorCatalogWithUpdatedAt result = apiInstance.getMostRecentSourceActorCatalog(sourceIdRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourceApi#getMostRecentSourceActorCatalog");
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
| **sourceIdRequestBody** | [**SourceIdRequestBody**](SourceIdRequestBody.md)|  | |

### Return type

[**ActorCatalogWithUpdatedAt**](ActorCatalogWithUpdatedAt.md)

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

<a id="getSource"></a>
# **getSource**
> SourceRead getSource(sourceIdRequestBody)

Get source

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    SourceApi apiInstance = new SourceApi(defaultClient);
    SourceIdRequestBody sourceIdRequestBody = new SourceIdRequestBody(); // SourceIdRequestBody | 
    try {
      SourceRead result = apiInstance.getSource(sourceIdRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourceApi#getSource");
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
| **sourceIdRequestBody** | [**SourceIdRequestBody**](SourceIdRequestBody.md)|  | |

### Return type

[**SourceRead**](SourceRead.md)

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

<a id="listSourcesForWorkspace"></a>
# **listSourcesForWorkspace**
> SourceReadList listSourcesForWorkspace(workspaceIdRequestBody)

List sources for workspace

List sources for workspace. Does not return deleted sources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    SourceApi apiInstance = new SourceApi(defaultClient);
    WorkspaceIdRequestBody workspaceIdRequestBody = new WorkspaceIdRequestBody(); // WorkspaceIdRequestBody | 
    try {
      SourceReadList result = apiInstance.listSourcesForWorkspace(workspaceIdRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourceApi#listSourcesForWorkspace");
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
| **workspaceIdRequestBody** | [**WorkspaceIdRequestBody**](WorkspaceIdRequestBody.md)|  | |

### Return type

[**SourceReadList**](SourceReadList.md)

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

<a id="searchSources"></a>
# **searchSources**
> SourceReadList searchSources(sourceSearch)

Search sources

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    SourceApi apiInstance = new SourceApi(defaultClient);
    SourceSearch sourceSearch = new SourceSearch(); // SourceSearch | 
    try {
      SourceReadList result = apiInstance.searchSources(sourceSearch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourceApi#searchSources");
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
| **sourceSearch** | [**SourceSearch**](SourceSearch.md)|  | |

### Return type

[**SourceReadList**](SourceReadList.md)

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

<a id="updateSource"></a>
# **updateSource**
> SourceRead updateSource(sourceUpdate)

Update a source

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    SourceApi apiInstance = new SourceApi(defaultClient);
    SourceUpdate sourceUpdate = new SourceUpdate(); // SourceUpdate | 
    try {
      SourceRead result = apiInstance.updateSource(sourceUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourceApi#updateSource");
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
| **sourceUpdate** | [**SourceUpdate**](SourceUpdate.md)|  | |

### Return type

[**SourceRead**](SourceRead.md)

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

<a id="writeDiscoverCatalogResult"></a>
# **writeDiscoverCatalogResult**
> DiscoverCatalogResult writeDiscoverCatalogResult(sourceDiscoverSchemaWriteRequestBody)

Should only called from worker, to write result from discover activity back to DB.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    SourceApi apiInstance = new SourceApi(defaultClient);
    SourceDiscoverSchemaWriteRequestBody sourceDiscoverSchemaWriteRequestBody = new SourceDiscoverSchemaWriteRequestBody(); // SourceDiscoverSchemaWriteRequestBody | 
    try {
      DiscoverCatalogResult result = apiInstance.writeDiscoverCatalogResult(sourceDiscoverSchemaWriteRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourceApi#writeDiscoverCatalogResult");
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
| **sourceDiscoverSchemaWriteRequestBody** | [**SourceDiscoverSchemaWriteRequestBody**](SourceDiscoverSchemaWriteRequestBody.md)|  | |

### Return type

[**DiscoverCatalogResult**](DiscoverCatalogResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

