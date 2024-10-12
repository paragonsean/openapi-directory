# ServerManagementApiApi

All URIs are relative to *http://api.postmarkapp.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createServer**](ServerManagementApiApi.md#createServer) | **POST** /servers | Create a Server |
| [**deleteServer**](ServerManagementApiApi.md#deleteServer) | **DELETE** /servers/{serverid} | Delete a Server |
| [**editServerInformation**](ServerManagementApiApi.md#editServerInformation) | **PUT** /servers/{serverid} | Edit a Server |
| [**getServerInformation**](ServerManagementApiApi.md#getServerInformation) | **GET** /servers/{serverid} | Get a Server |
| [**listServers**](ServerManagementApiApi.md#listServers) | **GET** /servers | List servers |


<a id="createServer"></a>
# **createServer**
> ExtendedServerInfo createServer(xPostmarkAccountToken, body)

Create a Server

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerManagementApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    ServerManagementApiApi apiInstance = new ServerManagementApiApi(defaultClient);
    String xPostmarkAccountToken = "xPostmarkAccountToken_example"; // String | The token associated with the Account on which this request will operate.
    CreateServerPayload body = new CreateServerPayload(); // CreateServerPayload | 
    try {
      ExtendedServerInfo result = apiInstance.createServer(xPostmarkAccountToken, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerManagementApiApi#createServer");
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
| **xPostmarkAccountToken** | **String**| The token associated with the Account on which this request will operate. | |
| **body** | [**CreateServerPayload**](CreateServerPayload.md)|  | [optional] |

### Return type

[**ExtendedServerInfo**](ExtendedServerInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="deleteServer"></a>
# **deleteServer**
> deleteServer(xPostmarkAccountToken, serverid)

Delete a Server

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerManagementApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    ServerManagementApiApi apiInstance = new ServerManagementApiApi(defaultClient);
    String xPostmarkAccountToken = "xPostmarkAccountToken_example"; // String | The token associated with the Account on which this request will operate.
    Integer serverid = 56; // Integer | The ID of the Server that should be deleted.
    try {
      apiInstance.deleteServer(xPostmarkAccountToken, serverid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerManagementApiApi#deleteServer");
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
| **xPostmarkAccountToken** | **String**| The token associated with the Account on which this request will operate. | |
| **serverid** | **Integer**| The ID of the Server that should be deleted. | |

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
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="editServerInformation"></a>
# **editServerInformation**
> ExtendedServerInfo editServerInformation(xPostmarkAccountToken, serverid, body)

Edit a Server

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerManagementApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    ServerManagementApiApi apiInstance = new ServerManagementApiApi(defaultClient);
    String xPostmarkAccountToken = "xPostmarkAccountToken_example"; // String | The token associated with the Account on which this request will operate.
    Integer serverid = 56; // Integer | The ID of the Server to update.
    EditServerPayload body = new EditServerPayload(); // EditServerPayload | 
    try {
      ExtendedServerInfo result = apiInstance.editServerInformation(xPostmarkAccountToken, serverid, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerManagementApiApi#editServerInformation");
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
| **xPostmarkAccountToken** | **String**| The token associated with the Account on which this request will operate. | |
| **serverid** | **Integer**| The ID of the Server to update. | |
| **body** | [**EditServerPayload**](EditServerPayload.md)|  | [optional] |

### Return type

[**ExtendedServerInfo**](ExtendedServerInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="getServerInformation"></a>
# **getServerInformation**
> ExtendedServerInfo getServerInformation(xPostmarkAccountToken, serverid)

Get a Server

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerManagementApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    ServerManagementApiApi apiInstance = new ServerManagementApiApi(defaultClient);
    String xPostmarkAccountToken = "xPostmarkAccountToken_example"; // String | The token associated with the Account on which this request will operate.
    Integer serverid = 56; // Integer | The ID of the Server to get.
    try {
      ExtendedServerInfo result = apiInstance.getServerInformation(xPostmarkAccountToken, serverid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerManagementApiApi#getServerInformation");
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
| **xPostmarkAccountToken** | **String**| The token associated with the Account on which this request will operate. | |
| **serverid** | **Integer**| The ID of the Server to get. | |

### Return type

[**ExtendedServerInfo**](ExtendedServerInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="listServers"></a>
# **listServers**
> ServerListingResponse listServers(xPostmarkAccountToken, count, offset, name)

List servers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerManagementApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    ServerManagementApiApi apiInstance = new ServerManagementApiApi(defaultClient);
    String xPostmarkAccountToken = "xPostmarkAccountToken_example"; // String | The token associated with the Account on which this request will operate.
    Integer count = 56; // Integer | Number of servers to return per request.
    Integer offset = 56; // Integer | Number of servers to skip.
    String name = "name_example"; // String | Filter by a specific server name
    try {
      ServerListingResponse result = apiInstance.listServers(xPostmarkAccountToken, count, offset, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerManagementApiApi#listServers");
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
| **xPostmarkAccountToken** | **String**| The token associated with the Account on which this request will operate. | |
| **count** | **Integer**| Number of servers to return per request. | |
| **offset** | **Integer**| Number of servers to skip. | |
| **name** | **String**| Filter by a specific server name | [optional] |

### Return type

[**ServerListingResponse**](ServerListingResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

