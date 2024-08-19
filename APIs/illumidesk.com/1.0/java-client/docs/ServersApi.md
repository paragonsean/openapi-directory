# ServersApi

All URIs are relative to *https://api.illumidesk.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**serversOptionsResourcesRead**](ServersApi.md#serversOptionsResourcesRead) | **GET** /v1/servers/options/server-size/{size}/ | Get a server size by id |
| [**serversOptionsServerSizeCreate**](ServersApi.md#serversOptionsServerSizeCreate) | **POST** /v1/servers/options/server-size/ | Create a new server size item |
| [**serversOptionsServerSizeDelete**](ServersApi.md#serversOptionsServerSizeDelete) | **DELETE** /v1/servers/options/server-size/{size}/ | Delete a server size by id |
| [**serversOptionsServerSizeReplace**](ServersApi.md#serversOptionsServerSizeReplace) | **PUT** /v1/servers/options/server-size/{size}/ | Replace a server size by id |
| [**serversOptionsServerSizeUpdate**](ServersApi.md#serversOptionsServerSizeUpdate) | **PATCH** /v1/servers/options/server-size/{size}/ | Update a server size by id |
| [**serversOptionsSizesList**](ServersApi.md#serversOptionsSizesList) | **GET** /v1/servers/options/server-size/ | Retrieve available server sizes |


<a id="serversOptionsResourcesRead"></a>
# **serversOptionsResourcesRead**
> ServerSize serversOptionsResourcesRead(size)

Get a server size by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ServersApi apiInstance = new ServersApi(defaultClient);
    String size = "size_example"; // String | Server size unique identifier expressed as UUID or name.
    try {
      ServerSize result = apiInstance.serversOptionsResourcesRead(size);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServersApi#serversOptionsResourcesRead");
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
| **size** | **String**| Server size unique identifier expressed as UUID or name. | |

### Return type

[**ServerSize**](ServerSize.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Environment resource retrieved. |  -  |
| **404** | Environment resource not found. |  -  |

<a id="serversOptionsServerSizeCreate"></a>
# **serversOptionsServerSizeCreate**
> ServerSize serversOptionsServerSizeCreate(serversizeData)

Create a new server size item

Only super users with on-premises version have acceess to this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ServersApi apiInstance = new ServersApi(defaultClient);
    ServerSizeData serversizeData = new ServerSizeData(); // ServerSizeData | 
    try {
      ServerSize result = apiInstance.serversOptionsServerSizeCreate(serversizeData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServersApi#serversOptionsServerSizeCreate");
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
| **serversizeData** | [**ServerSizeData**](ServerSizeData.md)|  | [optional] |

### Return type

[**ServerSize**](ServerSize.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | ServerSize created. This operation is available only to super users. |  -  |
| **400** | Invalid data supplied |  -  |

<a id="serversOptionsServerSizeDelete"></a>
# **serversOptionsServerSizeDelete**
> serversOptionsServerSizeDelete(size)

Delete a server size by id

Only super users with on-premises version have acceess to this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ServersApi apiInstance = new ServersApi(defaultClient);
    String size = "size_example"; // String | Server size unique identifier expressed as UUID or name.
    try {
      apiInstance.serversOptionsServerSizeDelete(size);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServersApi#serversOptionsServerSizeDelete");
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
| **size** | **String**| Server size unique identifier expressed as UUID or name. | |

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Server size deleted. This operation is available only to super users |  -  |
| **404** | ServerSize not found. |  -  |

<a id="serversOptionsServerSizeReplace"></a>
# **serversOptionsServerSizeReplace**
> ServerSize serversOptionsServerSizeReplace(size, serversizeData)

Replace a server size by id

Only super users with on-premises version have acceess to this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ServersApi apiInstance = new ServersApi(defaultClient);
    String size = "size_example"; // String | Server size unique identifier expressed as UUID or name.
    ServerSizeData serversizeData = new ServerSizeData(); // ServerSizeData | 
    try {
      ServerSize result = apiInstance.serversOptionsServerSizeReplace(size, serversizeData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServersApi#serversOptionsServerSizeReplace");
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
| **size** | **String**| Server size unique identifier expressed as UUID or name. | |
| **serversizeData** | [**ServerSizeData**](ServerSizeData.md)|  | [optional] |

### Return type

[**ServerSize**](ServerSize.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Server size replaced. This operation is available only to super users. |  -  |
| **400** | Invalid data supplied. |  -  |
| **404** | ServerSize not found |  -  |

<a id="serversOptionsServerSizeUpdate"></a>
# **serversOptionsServerSizeUpdate**
> ServerSize serversOptionsServerSizeUpdate(size, serversizeData)

Update a server size by id

Only super users with on-premises version have acceess to this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ServersApi apiInstance = new ServersApi(defaultClient);
    String size = "size_example"; // String | Server size unique identifier expressed as UUID or name.
    ServerSizeData serversizeData = new ServerSizeData(); // ServerSizeData | 
    try {
      ServerSize result = apiInstance.serversOptionsServerSizeUpdate(size, serversizeData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServersApi#serversOptionsServerSizeUpdate");
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
| **size** | **String**| Server size unique identifier expressed as UUID or name. | |
| **serversizeData** | [**ServerSizeData**](ServerSizeData.md)|  | [optional] |

### Return type

[**ServerSize**](ServerSize.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Server size updated. This operation is available only to super users. |  -  |
| **400** | Invalid data supplied. |  -  |
| **404** | Server size not found. |  -  |

<a id="serversOptionsSizesList"></a>
# **serversOptionsSizesList**
> List&lt;ServerSize&gt; serversOptionsSizesList(limit, offset, ordering)

Retrieve available server sizes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ServersApi apiInstance = new ServersApi(defaultClient);
    String limit = "limit_example"; // String | Set limit when retrieving items.
    String offset = "offset_example"; // String | Offset when retrieving items.
    String ordering = "ordering_example"; // String | Set order when retrieving items.
    try {
      List<ServerSize> result = apiInstance.serversOptionsSizesList(limit, offset, ordering);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServersApi#serversOptionsSizesList");
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
| **limit** | **String**| Set limit when retrieving items. | [optional] |
| **offset** | **String**| Offset when retrieving items. | [optional] |
| **ordering** | **String**| Set order when retrieving items. | [optional] |

### Return type

[**List&lt;ServerSize&gt;**](ServerSize.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Server size list. |  -  |

