# WebBackendApi

All URIs are relative to *http://airbyte.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getStateType**](WebBackendApi.md#getStateType) | **POST** /v1/web_backend/state/get_type | Fetch the current state type for a connection. |
| [**webBackendCheckUpdates**](WebBackendApi.md#webBackendCheckUpdates) | **POST** /v1/web_backend/check_updates | Returns a summary of source and destination definitions that could be updated. |
| [**webBackendCreateConnection**](WebBackendApi.md#webBackendCreateConnection) | **POST** /v1/web_backend/connections/create | Create a connection |
| [**webBackendGetConnection**](WebBackendApi.md#webBackendGetConnection) | **POST** /v1/web_backend/connections/get | Get a connection |
| [**webBackendGetWorkspaceState**](WebBackendApi.md#webBackendGetWorkspaceState) | **POST** /v1/web_backend/workspace/state | Returns the current state of a workspace |
| [**webBackendListConnectionsForWorkspace**](WebBackendApi.md#webBackendListConnectionsForWorkspace) | **POST** /v1/web_backend/connections/list | Returns all non-deleted connections for a workspace. |
| [**webBackendListGeographies**](WebBackendApi.md#webBackendListGeographies) | **POST** /v1/web_backend/geographies/list | Returns available geographies can be selected to run data syncs in a particular geography. The &#39;auto&#39; entry indicates that the sync will be automatically assigned to a geography according to the platform default behavior. Entries other than &#39;auto&#39; are two-letter country codes that follow the ISO 3166-1 alpha-2 standard.  |
| [**webBackendUpdateConnection**](WebBackendApi.md#webBackendUpdateConnection) | **POST** /v1/web_backend/connections/update | Update a connection |


<a id="getStateType"></a>
# **getStateType**
> ConnectionStateType getStateType(connectionIdRequestBody)

Fetch the current state type for a connection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebBackendApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    WebBackendApi apiInstance = new WebBackendApi(defaultClient);
    ConnectionIdRequestBody connectionIdRequestBody = new ConnectionIdRequestBody(); // ConnectionIdRequestBody | 
    try {
      ConnectionStateType result = apiInstance.getStateType(connectionIdRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebBackendApi#getStateType");
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
| **connectionIdRequestBody** | [**ConnectionIdRequestBody**](ConnectionIdRequestBody.md)|  | |

### Return type

[**ConnectionStateType**](ConnectionStateType.md)

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

<a id="webBackendCheckUpdates"></a>
# **webBackendCheckUpdates**
> WebBackendCheckUpdatesRead webBackendCheckUpdates()

Returns a summary of source and destination definitions that could be updated.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebBackendApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    WebBackendApi apiInstance = new WebBackendApi(defaultClient);
    try {
      WebBackendCheckUpdatesRead result = apiInstance.webBackendCheckUpdates();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebBackendApi#webBackendCheckUpdates");
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

[**WebBackendCheckUpdatesRead**](WebBackendCheckUpdatesRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="webBackendCreateConnection"></a>
# **webBackendCreateConnection**
> WebBackendConnectionRead webBackendCreateConnection(webBackendConnectionCreate)

Create a connection

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebBackendApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    WebBackendApi apiInstance = new WebBackendApi(defaultClient);
    WebBackendConnectionCreate webBackendConnectionCreate = new WebBackendConnectionCreate(); // WebBackendConnectionCreate | 
    try {
      WebBackendConnectionRead result = apiInstance.webBackendCreateConnection(webBackendConnectionCreate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebBackendApi#webBackendCreateConnection");
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
| **webBackendConnectionCreate** | [**WebBackendConnectionCreate**](WebBackendConnectionCreate.md)|  | |

### Return type

[**WebBackendConnectionRead**](WebBackendConnectionRead.md)

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

<a id="webBackendGetConnection"></a>
# **webBackendGetConnection**
> WebBackendConnectionRead webBackendGetConnection(webBackendConnectionRequestBody)

Get a connection

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebBackendApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    WebBackendApi apiInstance = new WebBackendApi(defaultClient);
    WebBackendConnectionRequestBody webBackendConnectionRequestBody = new WebBackendConnectionRequestBody(); // WebBackendConnectionRequestBody | 
    try {
      WebBackendConnectionRead result = apiInstance.webBackendGetConnection(webBackendConnectionRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebBackendApi#webBackendGetConnection");
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
| **webBackendConnectionRequestBody** | [**WebBackendConnectionRequestBody**](WebBackendConnectionRequestBody.md)|  | |

### Return type

[**WebBackendConnectionRead**](WebBackendConnectionRead.md)

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

<a id="webBackendGetWorkspaceState"></a>
# **webBackendGetWorkspaceState**
> WebBackendWorkspaceStateResult webBackendGetWorkspaceState(webBackendWorkspaceState)

Returns the current state of a workspace

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebBackendApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    WebBackendApi apiInstance = new WebBackendApi(defaultClient);
    WebBackendWorkspaceState webBackendWorkspaceState = new WebBackendWorkspaceState(); // WebBackendWorkspaceState | 
    try {
      WebBackendWorkspaceStateResult result = apiInstance.webBackendGetWorkspaceState(webBackendWorkspaceState);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebBackendApi#webBackendGetWorkspaceState");
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
| **webBackendWorkspaceState** | [**WebBackendWorkspaceState**](WebBackendWorkspaceState.md)|  | [optional] |

### Return type

[**WebBackendWorkspaceStateResult**](WebBackendWorkspaceStateResult.md)

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

<a id="webBackendListConnectionsForWorkspace"></a>
# **webBackendListConnectionsForWorkspace**
> WebBackendConnectionReadList webBackendListConnectionsForWorkspace(webBackendConnectionListRequestBody)

Returns all non-deleted connections for a workspace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebBackendApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    WebBackendApi apiInstance = new WebBackendApi(defaultClient);
    WebBackendConnectionListRequestBody webBackendConnectionListRequestBody = new WebBackendConnectionListRequestBody(); // WebBackendConnectionListRequestBody | 
    try {
      WebBackendConnectionReadList result = apiInstance.webBackendListConnectionsForWorkspace(webBackendConnectionListRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebBackendApi#webBackendListConnectionsForWorkspace");
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
| **webBackendConnectionListRequestBody** | [**WebBackendConnectionListRequestBody**](WebBackendConnectionListRequestBody.md)|  | |

### Return type

[**WebBackendConnectionReadList**](WebBackendConnectionReadList.md)

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

<a id="webBackendListGeographies"></a>
# **webBackendListGeographies**
> WebBackendGeographiesListResult webBackendListGeographies()

Returns available geographies can be selected to run data syncs in a particular geography. The &#39;auto&#39; entry indicates that the sync will be automatically assigned to a geography according to the platform default behavior. Entries other than &#39;auto&#39; are two-letter country codes that follow the ISO 3166-1 alpha-2 standard. 

Returns all available geographies in which a data sync can run.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebBackendApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    WebBackendApi apiInstance = new WebBackendApi(defaultClient);
    try {
      WebBackendGeographiesListResult result = apiInstance.webBackendListGeographies();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebBackendApi#webBackendListGeographies");
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

[**WebBackendGeographiesListResult**](WebBackendGeographiesListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="webBackendUpdateConnection"></a>
# **webBackendUpdateConnection**
> WebBackendConnectionRead webBackendUpdateConnection(webBackendConnectionUpdate)

Update a connection

Apply a patch-style update to a connection. Only fields present on the update request body will be updated. Any operations that lack an ID will be created. Then, the newly created operationId will be applied to the connection along with the rest of the operationIds in the request body. Apply a patch-style update to a connection. Only fields present on the update request body will be updated. Note that if a catalog is present in the request body, the connection&#39;s entire catalog will be replaced with the catalog from the request. This means that to modify a single stream, the entire new catalog containing the updated stream needs to be sent. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebBackendApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    WebBackendApi apiInstance = new WebBackendApi(defaultClient);
    WebBackendConnectionUpdate webBackendConnectionUpdate = new WebBackendConnectionUpdate(); // WebBackendConnectionUpdate | 
    try {
      WebBackendConnectionRead result = apiInstance.webBackendUpdateConnection(webBackendConnectionUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebBackendApi#webBackendUpdateConnection");
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
| **webBackendConnectionUpdate** | [**WebBackendConnectionUpdate**](WebBackendConnectionUpdate.md)|  | |

### Return type

[**WebBackendConnectionRead**](WebBackendConnectionRead.md)

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

