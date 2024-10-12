# StateApi

All URIs are relative to *http://airbyte.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createOrUpdateState**](StateApi.md#createOrUpdateState) | **POST** /v1/state/create_or_update | Create or update the state for a connection. |
| [**getState**](StateApi.md#getState) | **POST** /v1/state/get | Fetch the current state for a connection. |


<a id="createOrUpdateState"></a>
# **createOrUpdateState**
> ConnectionState createOrUpdateState(connectionStateCreateOrUpdate)

Create or update the state for a connection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    StateApi apiInstance = new StateApi(defaultClient);
    ConnectionStateCreateOrUpdate connectionStateCreateOrUpdate = new ConnectionStateCreateOrUpdate(); // ConnectionStateCreateOrUpdate | 
    try {
      ConnectionState result = apiInstance.createOrUpdateState(connectionStateCreateOrUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StateApi#createOrUpdateState");
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
| **connectionStateCreateOrUpdate** | [**ConnectionStateCreateOrUpdate**](ConnectionStateCreateOrUpdate.md)|  | |

### Return type

[**ConnectionState**](ConnectionState.md)

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

<a id="getState"></a>
# **getState**
> ConnectionState getState(connectionIdRequestBody)

Fetch the current state for a connection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    StateApi apiInstance = new StateApi(defaultClient);
    ConnectionIdRequestBody connectionIdRequestBody = new ConnectionIdRequestBody(); // ConnectionIdRequestBody | 
    try {
      ConnectionState result = apiInstance.getState(connectionIdRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StateApi#getState");
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

[**ConnectionState**](ConnectionState.md)

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

