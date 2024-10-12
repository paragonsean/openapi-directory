# CallsApi

All URIs are relative to *https://api.vonage.com/t/vbc.prod/vis/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**callAnswer**](CallsApi.md#callAnswer) | **PUT** /self/calls/{id}/answer | Answer call (On supported devices) |
| [**callHold**](CallsApi.md#callHold) | **PUT** /self/calls/{id}/hold | Put call on hold |
| [**callTransfer**](CallsApi.md#callTransfer) | **POST** /self/calls/{id}/transfer | Transfer call |
| [**callUnold**](CallsApi.md#callUnold) | **DELETE** /self/calls/{id}/hold | Unhold |
| [**callVMTransfer**](CallsApi.md#callVMTransfer) | **PUT** /self/calls/{id}/vmtransfer | Send call to voicemail |
| [**createCall**](CallsApi.md#createCall) | **POST** /self/calls | Place a call |
| [**destroyCall**](CallsApi.md#destroyCall) | **DELETE** /self/calls/{id} | End a call |
| [**getCallsCount**](CallsApi.md#getCallsCount) | **GET** /self/calls/count | Get calls count |
| [**getRoles**](CallsApi.md#getRoles) | **GET** /self/calls/{id} | Get a call |
| [**listCalls**](CallsApi.md#listCalls) | **GET** /self/calls | List active calls |


<a id="callAnswer"></a>
# **callAnswer**
> Call callAnswer(id)

Answer call (On supported devices)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vonage.com/t/vbc.prod/vis/v1");

    CallsApi apiInstance = new CallsApi(defaultClient);
    String id = "id_example"; // String | Unique identifier of the call
    try {
      Call result = apiInstance.callAnswer(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#callAnswer");
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
| **id** | **String**| Unique identifier of the call | |

### Return type

[**Call**](Call.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful |  -  |
| **400** | Bad Request: The client should not repeat the request without modifications |  -  |
| **401** | Unauthorized: Invalid access token |  -  |
| **403** | Forbidden: The user has no rights to access the resource(s) |  -  |
| **408** | Timeout: The client may repeat the request without modifications |  -  |
| **422** | Validation Error |  -  |
| **500** | Internal Server Error |  -  |
| **502** | Bad Gateway |  -  |

<a id="callHold"></a>
# **callHold**
> Call callHold(id)

Put call on hold

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vonage.com/t/vbc.prod/vis/v1");

    CallsApi apiInstance = new CallsApi(defaultClient);
    String id = "id_example"; // String | Unique identifier of the call
    try {
      Call result = apiInstance.callHold(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#callHold");
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
| **id** | **String**| Unique identifier of the call | |

### Return type

[**Call**](Call.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful |  -  |
| **400** | Bad Request: The client should not repeat the request without modifications |  -  |
| **401** | Unauthorized: Invalid access token |  -  |
| **403** | Forbidden: The user has no rights to access the resource(s) |  -  |
| **408** | Timeout: The client may repeat the request without modifications |  -  |
| **422** | Validation Error |  -  |
| **500** | Internal Server Error |  -  |
| **502** | Bad Gateway |  -  |

<a id="callTransfer"></a>
# **callTransfer**
> Call callTransfer(id, callTransfer)

Transfer call

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vonage.com/t/vbc.prod/vis/v1");

    CallsApi apiInstance = new CallsApi(defaultClient);
    String id = "id_example"; // String | Unique identifier of the call
    CallTransfer callTransfer = new CallTransfer(); // CallTransfer | Call transfer parameters
    try {
      Call result = apiInstance.callTransfer(id, callTransfer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#callTransfer");
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
| **id** | **String**| Unique identifier of the call | |
| **callTransfer** | [**CallTransfer**](CallTransfer.md)| Call transfer parameters | |

### Return type

[**Call**](Call.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful |  -  |
| **400** | Bad Request: The client should not repeat the request without modifications |  -  |
| **401** | Unauthorized: Invalid access token |  -  |
| **403** | Forbidden: The user has no rights to access the resource(s) |  -  |
| **408** | Timeout: The client may repeat the request without modifications |  -  |
| **422** | Validation Error |  -  |
| **500** | Internal Server Error |  -  |
| **502** | Bad Gateway |  -  |

<a id="callUnold"></a>
# **callUnold**
> Call callUnold(id)

Unhold

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vonage.com/t/vbc.prod/vis/v1");

    CallsApi apiInstance = new CallsApi(defaultClient);
    String id = "id_example"; // String | Unique identifier of the call
    try {
      Call result = apiInstance.callUnold(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#callUnold");
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
| **id** | **String**| Unique identifier of the call | |

### Return type

[**Call**](Call.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful |  -  |
| **400** | Bad Request: The client should not repeat the request without modifications |  -  |
| **401** | Unauthorized: Invalid access token |  -  |
| **403** | Forbidden: The user has no rights to access the resource(s) |  -  |
| **408** | Timeout: The client may repeat the request without modifications |  -  |
| **422** | Validation Error |  -  |
| **500** | Internal Server Error |  -  |
| **502** | Bad Gateway |  -  |

<a id="callVMTransfer"></a>
# **callVMTransfer**
> Call callVMTransfer(id)

Send call to voicemail

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vonage.com/t/vbc.prod/vis/v1");

    CallsApi apiInstance = new CallsApi(defaultClient);
    String id = "id_example"; // String | Unique identifier of the call
    try {
      Call result = apiInstance.callVMTransfer(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#callVMTransfer");
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
| **id** | **String**| Unique identifier of the call | |

### Return type

[**Call**](Call.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful |  -  |
| **400** | Bad Request: The client should not repeat the request without modifications |  -  |
| **401** | Unauthorized: Invalid access token |  -  |
| **403** | Forbidden: The user has no rights to access the resource(s) |  -  |
| **408** | Timeout: The client may repeat the request without modifications |  -  |
| **422** | Validation Error |  -  |
| **500** | Internal Server Error |  -  |
| **502** | Bad Gateway |  -  |

<a id="createCall"></a>
# **createCall**
> List&lt;Call&gt; createCall(callCreate)

Place a call

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vonage.com/t/vbc.prod/vis/v1");

    CallsApi apiInstance = new CallsApi(defaultClient);
    CallCreate callCreate = new CallCreate(); // CallCreate | Place call parameters
    try {
      List<Call> result = apiInstance.createCall(callCreate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#createCall");
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
| **callCreate** | [**CallCreate**](CallCreate.md)| Place call parameters | |

### Return type

[**List&lt;Call&gt;**](Call.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful |  -  |
| **400** | Bad Request: The client should not repeat the request without modifications |  -  |
| **401** | Unauthorized: Invalid access token |  -  |
| **403** | Forbidden: The user has no rights to access the resource(s) |  -  |
| **408** | Timeout: The client may repeat the request without modifications |  -  |
| **422** | Validation Error |  -  |
| **500** | Internal Server Error |  -  |
| **502** | Bad Gateway |  -  |

<a id="destroyCall"></a>
# **destroyCall**
> List&lt;Call&gt; destroyCall(id)

End a call

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vonage.com/t/vbc.prod/vis/v1");

    CallsApi apiInstance = new CallsApi(defaultClient);
    String id = "id_example"; // String | Unique identifier of the call
    try {
      List<Call> result = apiInstance.destroyCall(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#destroyCall");
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
| **id** | **String**| Unique identifier of the call | |

### Return type

[**List&lt;Call&gt;**](Call.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful |  -  |
| **400** | Bad Request: The client should not repeat the request without modifications |  -  |
| **401** | Unauthorized: Invalid access token |  -  |
| **403** | Forbidden: The user has no rights to access the resource(s) |  -  |
| **408** | Timeout: The client may repeat the request without modifications |  -  |
| **422** | Validation Error |  -  |
| **500** | Internal Server Error |  -  |
| **502** | Bad Gateway |  -  |

<a id="getCallsCount"></a>
# **getCallsCount**
> EventsCount getCallsCount(fromDate, toDate, direction, states)

Get calls count

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vonage.com/t/vbc.prod/vis/v1");

    CallsApi apiInstance = new CallsApi(defaultClient);
    Integer fromDate = 56; // Integer | Return calls that occurred after this point in time
    Integer toDate = 56; // Integer | Return calls that occurred before this point in time
    String direction = "INBOUND"; // String | Filter by call direction. For multiple criteria, seperate values by a comma.
    String states = "INITIALIZING"; // String | Filter calls by state. For multiple criteria, seperate values by a comma.
    try {
      EventsCount result = apiInstance.getCallsCount(fromDate, toDate, direction, states);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#getCallsCount");
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
| **fromDate** | **Integer**| Return calls that occurred after this point in time | [optional] |
| **toDate** | **Integer**| Return calls that occurred before this point in time | [optional] |
| **direction** | **String**| Filter by call direction. For multiple criteria, seperate values by a comma. | [optional] [enum: INBOUND, OUTBOUND] |
| **states** | **String**| Filter calls by state. For multiple criteria, seperate values by a comma. | [optional] [default to ACTIVE] [enum: INITIALIZING, RINGING, ACTIVE, HELD, REMOTE_HELD] |

### Return type

[**EventsCount**](EventsCount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful |  -  |
| **400** | Bad Request: The client should not repeat the request without modifications |  -  |
| **401** | Unauthorized: Invalid access token |  -  |
| **403** | Forbidden: The user has no rights to access the resource(s) |  -  |
| **408** | Timeout: The client may repeat the request without modifications |  -  |
| **422** | Validation Error |  -  |
| **500** | Internal Server Error |  -  |
| **502** | Bad Gateway |  -  |

<a id="getRoles"></a>
# **getRoles**
> List&lt;Call&gt; getRoles(id)

Get a call

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vonage.com/t/vbc.prod/vis/v1");

    CallsApi apiInstance = new CallsApi(defaultClient);
    String id = "id_example"; // String | Unique identifier of the call
    try {
      List<Call> result = apiInstance.getRoles(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#getRoles");
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
| **id** | **String**| Unique identifier of the call | |

### Return type

[**List&lt;Call&gt;**](Call.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful |  -  |
| **400** | Bad Request: The client should not repeat the request without modifications |  -  |
| **401** | Unauthorized: Invalid access token |  -  |
| **403** | Forbidden: The user has no rights to access the resource(s) |  -  |
| **408** | Timeout: The client may repeat the request without modifications |  -  |
| **422** | Validation Error |  -  |
| **500** | Internal Server Error |  -  |
| **502** | Bad Gateway |  -  |

<a id="listCalls"></a>
# **listCalls**
> List&lt;Call&gt; listCalls(fromDate, toDate, direction, states, offset, size, order, sort)

List active calls

Lists currently active calls

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vonage.com/t/vbc.prod/vis/v1");

    CallsApi apiInstance = new CallsApi(defaultClient);
    Integer fromDate = 56; // Integer | Return calls that occurred after this point in time
    Integer toDate = 56; // Integer | Return calls that occurred before this point in time
    String direction = "INBOUND"; // String | Filter by call direction. For multiple criteria, seperate values by a comma.
    String states = "INITIALIZING"; // String | Filter calls by state. For multiple criteria, seperate values by a comma.
    Long offset = 56L; // Long | Page number of calls to return
    Integer size = 20; // Integer | Return this amount of calls in the response
    String order = "DESC"; // String | Sort in either ascending or descending order
    String sort = "sort_example"; // String | Sort calls by property
    try {
      List<Call> result = apiInstance.listCalls(fromDate, toDate, direction, states, offset, size, order, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#listCalls");
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
| **fromDate** | **Integer**| Return calls that occurred after this point in time | [optional] |
| **toDate** | **Integer**| Return calls that occurred before this point in time | [optional] |
| **direction** | **String**| Filter by call direction. For multiple criteria, seperate values by a comma. | [optional] [enum: INBOUND, OUTBOUND] |
| **states** | **String**| Filter calls by state. For multiple criteria, seperate values by a comma. | [optional] [default to ACTIVE] [enum: INITIALIZING, RINGING, ACTIVE, HELD, REMOTE_HELD] |
| **offset** | **Long**| Page number of calls to return | [optional] |
| **size** | **Integer**| Return this amount of calls in the response | [optional] [default to 20] |
| **order** | **String**| Sort in either ascending or descending order | [optional] [default to ASC] [enum: DESC, ASC] |
| **sort** | **String**| Sort calls by property | [optional] |

### Return type

[**List&lt;Call&gt;**](Call.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful |  -  |
| **400** | Bad Request: The client should not repeat the request without modifications |  -  |
| **401** | Unauthorized: Invalid access token |  -  |
| **403** | Forbidden: The user has no rights to access the resource(s) |  -  |
| **408** | Timeout: The client may repeat the request without modifications |  -  |
| **422** | Validation Error |  -  |
| **500** | Internal Server Error |  -  |
| **502** | Bad Gateway |  -  |

