# OperationApi

All URIs are relative to *http://airbyte.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**checkOperation**](OperationApi.md#checkOperation) | **POST** /v1/operations/check | Check if an operation to be created is valid |
| [**createOperation**](OperationApi.md#createOperation) | **POST** /v1/operations/create | Create an operation to be applied as part of a connection pipeline |
| [**deleteOperation**](OperationApi.md#deleteOperation) | **POST** /v1/operations/delete | Delete an operation |
| [**getOperation**](OperationApi.md#getOperation) | **POST** /v1/operations/get | Returns an operation |
| [**listOperationsForConnection**](OperationApi.md#listOperationsForConnection) | **POST** /v1/operations/list | Returns all operations for a connection. |
| [**updateOperation**](OperationApi.md#updateOperation) | **POST** /v1/operations/update | Update an operation |


<a id="checkOperation"></a>
# **checkOperation**
> CheckOperationRead checkOperation(operatorConfiguration)

Check if an operation to be created is valid

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    OperationApi apiInstance = new OperationApi(defaultClient);
    OperatorConfiguration operatorConfiguration = new OperatorConfiguration(); // OperatorConfiguration | 
    try {
      CheckOperationRead result = apiInstance.checkOperation(operatorConfiguration);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperationApi#checkOperation");
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
| **operatorConfiguration** | [**OperatorConfiguration**](OperatorConfiguration.md)|  | |

### Return type

[**CheckOperationRead**](CheckOperationRead.md)

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

<a id="createOperation"></a>
# **createOperation**
> OperationRead createOperation(operationCreate)

Create an operation to be applied as part of a connection pipeline

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    OperationApi apiInstance = new OperationApi(defaultClient);
    OperationCreate operationCreate = new OperationCreate(); // OperationCreate | 
    try {
      OperationRead result = apiInstance.createOperation(operationCreate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperationApi#createOperation");
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
| **operationCreate** | [**OperationCreate**](OperationCreate.md)|  | |

### Return type

[**OperationRead**](OperationRead.md)

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

<a id="deleteOperation"></a>
# **deleteOperation**
> deleteOperation(operationIdRequestBody)

Delete an operation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    OperationApi apiInstance = new OperationApi(defaultClient);
    OperationIdRequestBody operationIdRequestBody = new OperationIdRequestBody(); // OperationIdRequestBody | 
    try {
      apiInstance.deleteOperation(operationIdRequestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperationApi#deleteOperation");
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
| **operationIdRequestBody** | [**OperationIdRequestBody**](OperationIdRequestBody.md)|  | |

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

<a id="getOperation"></a>
# **getOperation**
> OperationRead getOperation(operationIdRequestBody)

Returns an operation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    OperationApi apiInstance = new OperationApi(defaultClient);
    OperationIdRequestBody operationIdRequestBody = new OperationIdRequestBody(); // OperationIdRequestBody | 
    try {
      OperationRead result = apiInstance.getOperation(operationIdRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperationApi#getOperation");
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
| **operationIdRequestBody** | [**OperationIdRequestBody**](OperationIdRequestBody.md)|  | |

### Return type

[**OperationRead**](OperationRead.md)

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

<a id="listOperationsForConnection"></a>
# **listOperationsForConnection**
> OperationReadList listOperationsForConnection(connectionIdRequestBody)

Returns all operations for a connection.

List operations for connection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    OperationApi apiInstance = new OperationApi(defaultClient);
    ConnectionIdRequestBody connectionIdRequestBody = new ConnectionIdRequestBody(); // ConnectionIdRequestBody | 
    try {
      OperationReadList result = apiInstance.listOperationsForConnection(connectionIdRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperationApi#listOperationsForConnection");
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

[**OperationReadList**](OperationReadList.md)

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

<a id="updateOperation"></a>
# **updateOperation**
> OperationRead updateOperation(operationUpdate)

Update an operation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    OperationApi apiInstance = new OperationApi(defaultClient);
    OperationUpdate operationUpdate = new OperationUpdate(); // OperationUpdate | 
    try {
      OperationRead result = apiInstance.updateOperation(operationUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperationApi#updateOperation");
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
| **operationUpdate** | [**OperationUpdate**](OperationUpdate.md)|  | |

### Return type

[**OperationRead**](OperationRead.md)

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

