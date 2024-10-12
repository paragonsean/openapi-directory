# IdentityApi

All URIs are relative to *https://api.xero.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteConnection**](IdentityApi.md#deleteConnection) | **DELETE** /Connections/{id} | Deletes a connection for this user (i.e. disconnect a tenant) |
| [**getConnections**](IdentityApi.md#getConnections) | **GET** /Connections | Retrieves the connections for this user |


<a id="deleteConnection"></a>
# **deleteConnection**
> deleteConnection(id)

Deletes a connection for this user (i.e. disconnect a tenant)

Override the base server url that include version

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    IdentityApi apiInstance = new IdentityApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | Unique identifier for retrieving single object
    try {
      apiInstance.deleteConnection(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentityApi#deleteConnection");
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
| **id** | **UUID**| Unique identifier for retrieving single object | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success - connection has been deleted no content returned |  -  |
| **404** | Resource not found |  -  |

<a id="getConnections"></a>
# **getConnections**
> List&lt;Connection&gt; getConnections(authEventId)

Retrieves the connections for this user

Override the base server url that include version

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    IdentityApi apiInstance = new IdentityApi(defaultClient);
    UUID authEventId = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Filter by authEventId
    try {
      List<Connection> result = apiInstance.getConnections(authEventId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentityApi#getConnections");
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
| **authEventId** | **UUID**| Filter by authEventId | [optional] |

### Return type

[**List&lt;Connection&gt;**](Connection.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Connections array with 0 to n Connection |  -  |

