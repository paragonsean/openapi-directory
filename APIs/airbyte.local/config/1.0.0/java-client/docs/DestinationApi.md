# DestinationApi

All URIs are relative to *http://airbyte.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**checkConnectionToDestination**](DestinationApi.md#checkConnectionToDestination) | **POST** /v1/destinations/check_connection | Check connection to the destination |
| [**checkConnectionToDestinationForUpdate**](DestinationApi.md#checkConnectionToDestinationForUpdate) | **POST** /v1/destinations/check_connection_for_update | Check connection for a proposed update to a destination |
| [**cloneDestination**](DestinationApi.md#cloneDestination) | **POST** /v1/destinations/clone | Clone destination |
| [**createDestination**](DestinationApi.md#createDestination) | **POST** /v1/destinations/create | Create a destination |
| [**deleteDestination**](DestinationApi.md#deleteDestination) | **POST** /v1/destinations/delete | Delete the destination |
| [**getDestination**](DestinationApi.md#getDestination) | **POST** /v1/destinations/get | Get configured destination |
| [**listDestinationsForWorkspace**](DestinationApi.md#listDestinationsForWorkspace) | **POST** /v1/destinations/list | List configured destinations for a workspace |
| [**searchDestinations**](DestinationApi.md#searchDestinations) | **POST** /v1/destinations/search | Search destinations |
| [**updateDestination**](DestinationApi.md#updateDestination) | **POST** /v1/destinations/update | Update a destination |


<a id="checkConnectionToDestination"></a>
# **checkConnectionToDestination**
> CheckConnectionRead checkConnectionToDestination(destinationIdRequestBody)

Check connection to the destination

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DestinationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    DestinationApi apiInstance = new DestinationApi(defaultClient);
    DestinationIdRequestBody destinationIdRequestBody = new DestinationIdRequestBody(); // DestinationIdRequestBody | 
    try {
      CheckConnectionRead result = apiInstance.checkConnectionToDestination(destinationIdRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DestinationApi#checkConnectionToDestination");
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
| **destinationIdRequestBody** | [**DestinationIdRequestBody**](DestinationIdRequestBody.md)|  | |

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

<a id="checkConnectionToDestinationForUpdate"></a>
# **checkConnectionToDestinationForUpdate**
> CheckConnectionRead checkConnectionToDestinationForUpdate(destinationUpdate)

Check connection for a proposed update to a destination

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DestinationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    DestinationApi apiInstance = new DestinationApi(defaultClient);
    DestinationUpdate destinationUpdate = new DestinationUpdate(); // DestinationUpdate | 
    try {
      CheckConnectionRead result = apiInstance.checkConnectionToDestinationForUpdate(destinationUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DestinationApi#checkConnectionToDestinationForUpdate");
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
| **destinationUpdate** | [**DestinationUpdate**](DestinationUpdate.md)|  | |

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

<a id="cloneDestination"></a>
# **cloneDestination**
> DestinationRead cloneDestination(destinationCloneRequestBody)

Clone destination

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DestinationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    DestinationApi apiInstance = new DestinationApi(defaultClient);
    DestinationCloneRequestBody destinationCloneRequestBody = new DestinationCloneRequestBody(); // DestinationCloneRequestBody | 
    try {
      DestinationRead result = apiInstance.cloneDestination(destinationCloneRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DestinationApi#cloneDestination");
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
| **destinationCloneRequestBody** | [**DestinationCloneRequestBody**](DestinationCloneRequestBody.md)|  | |

### Return type

[**DestinationRead**](DestinationRead.md)

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

<a id="createDestination"></a>
# **createDestination**
> DestinationRead createDestination(destinationCreate)

Create a destination

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DestinationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    DestinationApi apiInstance = new DestinationApi(defaultClient);
    DestinationCreate destinationCreate = new DestinationCreate(); // DestinationCreate | 
    try {
      DestinationRead result = apiInstance.createDestination(destinationCreate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DestinationApi#createDestination");
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
| **destinationCreate** | [**DestinationCreate**](DestinationCreate.md)|  | |

### Return type

[**DestinationRead**](DestinationRead.md)

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

<a id="deleteDestination"></a>
# **deleteDestination**
> deleteDestination(destinationIdRequestBody)

Delete the destination

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DestinationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    DestinationApi apiInstance = new DestinationApi(defaultClient);
    DestinationIdRequestBody destinationIdRequestBody = new DestinationIdRequestBody(); // DestinationIdRequestBody | 
    try {
      apiInstance.deleteDestination(destinationIdRequestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling DestinationApi#deleteDestination");
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
| **destinationIdRequestBody** | [**DestinationIdRequestBody**](DestinationIdRequestBody.md)|  | |

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

<a id="getDestination"></a>
# **getDestination**
> DestinationRead getDestination(destinationIdRequestBody)

Get configured destination

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DestinationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    DestinationApi apiInstance = new DestinationApi(defaultClient);
    DestinationIdRequestBody destinationIdRequestBody = new DestinationIdRequestBody(); // DestinationIdRequestBody | 
    try {
      DestinationRead result = apiInstance.getDestination(destinationIdRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DestinationApi#getDestination");
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
| **destinationIdRequestBody** | [**DestinationIdRequestBody**](DestinationIdRequestBody.md)|  | |

### Return type

[**DestinationRead**](DestinationRead.md)

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

<a id="listDestinationsForWorkspace"></a>
# **listDestinationsForWorkspace**
> DestinationReadList listDestinationsForWorkspace(workspaceIdRequestBody)

List configured destinations for a workspace

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DestinationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    DestinationApi apiInstance = new DestinationApi(defaultClient);
    WorkspaceIdRequestBody workspaceIdRequestBody = new WorkspaceIdRequestBody(); // WorkspaceIdRequestBody | 
    try {
      DestinationReadList result = apiInstance.listDestinationsForWorkspace(workspaceIdRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DestinationApi#listDestinationsForWorkspace");
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

[**DestinationReadList**](DestinationReadList.md)

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

<a id="searchDestinations"></a>
# **searchDestinations**
> DestinationReadList searchDestinations(destinationSearch)

Search destinations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DestinationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    DestinationApi apiInstance = new DestinationApi(defaultClient);
    DestinationSearch destinationSearch = new DestinationSearch(); // DestinationSearch | 
    try {
      DestinationReadList result = apiInstance.searchDestinations(destinationSearch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DestinationApi#searchDestinations");
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
| **destinationSearch** | [**DestinationSearch**](DestinationSearch.md)|  | |

### Return type

[**DestinationReadList**](DestinationReadList.md)

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

<a id="updateDestination"></a>
# **updateDestination**
> DestinationRead updateDestination(destinationUpdate)

Update a destination

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DestinationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    DestinationApi apiInstance = new DestinationApi(defaultClient);
    DestinationUpdate destinationUpdate = new DestinationUpdate(); // DestinationUpdate | 
    try {
      DestinationRead result = apiInstance.updateDestination(destinationUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DestinationApi#updateDestination");
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
| **destinationUpdate** | [**DestinationUpdate**](DestinationUpdate.md)|  | |

### Return type

[**DestinationRead**](DestinationRead.md)

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

