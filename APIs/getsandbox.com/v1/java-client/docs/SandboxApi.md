# SandboxApi

All URIs are relative to *https://getsandbox.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSandbox**](SandboxApi.md#createSandbox) | **POST** /1/sandboxes | createSandbox |
| [**deleteSandbox**](SandboxApi.md#deleteSandbox) | **DELETE** /1/sandboxes/{sandboxName} | deleteSandbox |
| [**deleteSandboxState**](SandboxApi.md#deleteSandboxState) | **DELETE** /1/sandboxes/{sandboxName}/state | deleteSandboxState |
| [**forkSandbox**](SandboxApi.md#forkSandbox) | **GET** /1/sandboxes/{sandboxName}/fork | forkSandbox |
| [**getSandbox**](SandboxApi.md#getSandbox) | **GET** /1/sandboxes/{sandboxName} | getSandbox |
| [**getSandboxState**](SandboxApi.md#getSandboxState) | **GET** /1/sandboxes/{sandboxName}/state | getSandboxState |
| [**getSandboxes**](SandboxApi.md#getSandboxes) | **GET** /1/sandboxes | getSandboxes |
| [**updateSandbox**](SandboxApi.md#updateSandbox) | **PUT** /1/sandboxes/{sandboxName} | updateSandbox |


<a id="createSandbox"></a>
# **createSandbox**
> Sandbox createSandbox(body)

createSandbox

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SandboxApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://getsandbox.com/api");

    SandboxApi apiInstance = new SandboxApi(defaultClient);
    CreateSandbox body = new CreateSandbox(); // CreateSandbox | Sandbox to be created
    try {
      Sandbox result = apiInstance.createSandbox(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SandboxApi#createSandbox");
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
| **body** | [**CreateSandbox**](CreateSandbox.md)| Sandbox to be created | |

### Return type

[**Sandbox**](Sandbox.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="deleteSandbox"></a>
# **deleteSandbox**
> deleteSandbox(sandboxName)

deleteSandbox

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SandboxApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://getsandbox.com/api");

    SandboxApi apiInstance = new SandboxApi(defaultClient);
    String sandboxName = "sandboxName_example"; // String | Name of the Sandbox
    try {
      apiInstance.deleteSandbox(sandboxName);
    } catch (ApiException e) {
      System.err.println("Exception when calling SandboxApi#deleteSandbox");
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
| **sandboxName** | **String**| Name of the Sandbox | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | successful operation |  -  |

<a id="deleteSandboxState"></a>
# **deleteSandboxState**
> deleteSandboxState(sandboxName)

deleteSandboxState

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SandboxApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://getsandbox.com/api");

    SandboxApi apiInstance = new SandboxApi(defaultClient);
    String sandboxName = "sandboxName_example"; // String | Name of the Sandbox
    try {
      apiInstance.deleteSandboxState(sandboxName);
    } catch (ApiException e) {
      System.err.println("Exception when calling SandboxApi#deleteSandboxState");
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
| **sandboxName** | **String**| Name of the Sandbox | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | successful operation |  -  |

<a id="forkSandbox"></a>
# **forkSandbox**
> Sandbox forkSandbox(sandboxName)

forkSandbox

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SandboxApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://getsandbox.com/api");

    SandboxApi apiInstance = new SandboxApi(defaultClient);
    String sandboxName = "sandboxName_example"; // String | Name of the Sandbox
    try {
      Sandbox result = apiInstance.forkSandbox(sandboxName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SandboxApi#forkSandbox");
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
| **sandboxName** | **String**| Name of the Sandbox | |

### Return type

[**Sandbox**](Sandbox.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getSandbox"></a>
# **getSandbox**
> Sandbox getSandbox(sandboxName)

getSandbox

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SandboxApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://getsandbox.com/api");

    SandboxApi apiInstance = new SandboxApi(defaultClient);
    String sandboxName = "sandboxName_example"; // String | Name of the Sandbox
    try {
      Sandbox result = apiInstance.getSandbox(sandboxName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SandboxApi#getSandbox");
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
| **sandboxName** | **String**| Name of the Sandbox | |

### Return type

[**Sandbox**](Sandbox.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getSandboxState"></a>
# **getSandboxState**
> getSandboxState(sandboxName)

getSandboxState

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SandboxApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://getsandbox.com/api");

    SandboxApi apiInstance = new SandboxApi(defaultClient);
    String sandboxName = "sandboxName_example"; // String | Name of the Sandbox
    try {
      apiInstance.getSandboxState(sandboxName);
    } catch (ApiException e) {
      System.err.println("Exception when calling SandboxApi#getSandboxState");
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
| **sandboxName** | **String**| Name of the Sandbox | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | successful operation |  -  |

<a id="getSandboxes"></a>
# **getSandboxes**
> List&lt;Sandbox&gt; getSandboxes(filterType)

getSandboxes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SandboxApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://getsandbox.com/api");

    SandboxApi apiInstance = new SandboxApi(defaultClient);
    String filterType = "filterType_example"; // String | 
    try {
      List<Sandbox> result = apiInstance.getSandboxes(filterType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SandboxApi#getSandboxes");
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
| **filterType** | **String**|  | [optional] |

### Return type

[**List&lt;Sandbox&gt;**](Sandbox.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="updateSandbox"></a>
# **updateSandbox**
> Sandbox updateSandbox(sandboxName, body)

updateSandbox

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SandboxApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://getsandbox.com/api");

    SandboxApi apiInstance = new SandboxApi(defaultClient);
    String sandboxName = "sandboxName_example"; // String | Name of the Sandbox
    Sandbox body = new Sandbox(); // Sandbox | Fields to updated on given Sandbox
    try {
      Sandbox result = apiInstance.updateSandbox(sandboxName, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SandboxApi#updateSandbox");
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
| **sandboxName** | **String**| Name of the Sandbox | |
| **body** | [**Sandbox**](Sandbox.md)| Fields to updated on given Sandbox | |

### Return type

[**Sandbox**](Sandbox.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

