# CommandsApi

All URIs are relative to *https://demo.traccar.org/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**commandsGet**](CommandsApi.md#commandsGet) | **GET** /commands | Fetch a list of Saved Commands |
| [**commandsIdDelete**](CommandsApi.md#commandsIdDelete) | **DELETE** /commands/{id} | Delete a Saved Command |
| [**commandsIdPut**](CommandsApi.md#commandsIdPut) | **PUT** /commands/{id} | Update a Saved Command |
| [**commandsPost**](CommandsApi.md#commandsPost) | **POST** /commands | Create a Saved Command |
| [**commandsSendGet**](CommandsApi.md#commandsSendGet) | **GET** /commands/send | Fetch a list of Saved Commands supported by Device at the moment |
| [**commandsSendPost**](CommandsApi.md#commandsSendPost) | **POST** /commands/send | Dispatch commands to device |
| [**commandsTypesGet**](CommandsApi.md#commandsTypesGet) | **GET** /commands/types | Fetch a list of available Commands for the Device or all possible Commands if Device ommited |


<a id="commandsGet"></a>
# **commandsGet**
> List&lt;Command&gt; commandsGet(all, userId, deviceId, groupId, refresh)

Fetch a list of Saved Commands

Without params, it returns a list of Saved Commands the user has access to

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommandsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.traccar.org/api");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CommandsApi apiInstance = new CommandsApi(defaultClient);
    Boolean all = true; // Boolean | Can only be used by admins or managers to fetch all entities
    Integer userId = 56; // Integer | Standard users can use this only with their own _userId_
    Integer deviceId = 56; // Integer | Standard users can use this only with _deviceId_s, they have access to
    Integer groupId = 56; // Integer | Standard users can use this only with _groupId_s, they have access to
    Boolean refresh = true; // Boolean | 
    try {
      List<Command> result = apiInstance.commandsGet(all, userId, deviceId, groupId, refresh);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommandsApi#commandsGet");
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
| **all** | **Boolean**| Can only be used by admins or managers to fetch all entities | [optional] |
| **userId** | **Integer**| Standard users can use this only with their own _userId_ | [optional] |
| **deviceId** | **Integer**| Standard users can use this only with _deviceId_s, they have access to | [optional] |
| **groupId** | **Integer**| Standard users can use this only with _groupId_s, they have access to | [optional] |
| **refresh** | **Boolean**|  | [optional] |

### Return type

[**List&lt;Command&gt;**](Command.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="commandsIdDelete"></a>
# **commandsIdDelete**
> commandsIdDelete(id)

Delete a Saved Command

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommandsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.traccar.org/api");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CommandsApi apiInstance = new CommandsApi(defaultClient);
    Integer id = 56; // Integer | 
    try {
      apiInstance.commandsIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommandsApi#commandsIdDelete");
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
| **id** | **Integer**|  | |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="commandsIdPut"></a>
# **commandsIdPut**
> Command commandsIdPut(id, body)

Update a Saved Command

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommandsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.traccar.org/api");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CommandsApi apiInstance = new CommandsApi(defaultClient);
    Integer id = 56; // Integer | 
    Command body = new Command(); // Command | 
    try {
      Command result = apiInstance.commandsIdPut(id, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommandsApi#commandsIdPut");
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
| **id** | **Integer**|  | |
| **body** | [**Command**](Command.md)|  | |

### Return type

[**Command**](Command.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="commandsPost"></a>
# **commandsPost**
> Command commandsPost(body)

Create a Saved Command

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommandsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.traccar.org/api");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CommandsApi apiInstance = new CommandsApi(defaultClient);
    Command body = new Command(); // Command | 
    try {
      Command result = apiInstance.commandsPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommandsApi#commandsPost");
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
| **body** | [**Command**](Command.md)|  | |

### Return type

[**Command**](Command.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="commandsSendGet"></a>
# **commandsSendGet**
> List&lt;Command&gt; commandsSendGet(deviceId)

Fetch a list of Saved Commands supported by Device at the moment

Return a list of saved commands linked to Device and its groups, filtered by current Device protocol support

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommandsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.traccar.org/api");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CommandsApi apiInstance = new CommandsApi(defaultClient);
    Integer deviceId = 56; // Integer | Standard users can use this only with _deviceId_s, they have access to
    try {
      List<Command> result = apiInstance.commandsSendGet(deviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommandsApi#commandsSendGet");
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
| **deviceId** | **Integer**| Standard users can use this only with _deviceId_s, they have access to | [optional] |

### Return type

[**List&lt;Command&gt;**](Command.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Could happen when the user doesn&#39;t have permission for the device |  -  |

<a id="commandsSendPost"></a>
# **commandsSendPost**
> Command commandsSendPost(body)

Dispatch commands to device

Dispatch a new command or Saved Command if _body.id_ set

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommandsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.traccar.org/api");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CommandsApi apiInstance = new CommandsApi(defaultClient);
    Command body = new Command(); // Command | 
    try {
      Command result = apiInstance.commandsSendPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommandsApi#commandsSendPost");
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
| **body** | [**Command**](Command.md)|  | |

### Return type

[**Command**](Command.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Command sent |  -  |
| **202** | Command queued |  -  |
| **400** | Could happen when the user doesn&#39;t have permission or an incorrect command _type_ for the device |  -  |

<a id="commandsTypesGet"></a>
# **commandsTypesGet**
> List&lt;CommandType&gt; commandsTypesGet(deviceId, protocol, textChannel)

Fetch a list of available Commands for the Device or all possible Commands if Device ommited

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommandsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.traccar.org/api");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CommandsApi apiInstance = new CommandsApi(defaultClient);
    Integer deviceId = 56; // Integer | Internal device identifier. Only works if device has already reported some locations
    String protocol = "protocol_example"; // String | Protocol name. Can be used instead of device id
    Boolean textChannel = true; // Boolean | When `true` return SMS commands. If not specified or `false` return data commands
    try {
      List<CommandType> result = apiInstance.commandsTypesGet(deviceId, protocol, textChannel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommandsApi#commandsTypesGet");
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
| **deviceId** | **Integer**| Internal device identifier. Only works if device has already reported some locations | [optional] |
| **protocol** | **String**| Protocol name. Can be used instead of device id | [optional] |
| **textChannel** | **Boolean**| When &#x60;true&#x60; return SMS commands. If not specified or &#x60;false&#x60; return data commands | [optional] |

### Return type

[**List&lt;CommandType&gt;**](CommandType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Could happen when trying to fetch from a device the user does not have permission |  -  |

