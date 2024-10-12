# StudioV1ExecutionApi

All URIs are relative to *https://studio.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createExecution**](StudioV1ExecutionApi.md#createExecution) | **POST** /v1/Flows/{FlowSid}/Executions |  |
| [**deleteExecution**](StudioV1ExecutionApi.md#deleteExecution) | **DELETE** /v1/Flows/{FlowSid}/Executions/{Sid} |  |
| [**fetchExecution**](StudioV1ExecutionApi.md#fetchExecution) | **GET** /v1/Flows/{FlowSid}/Executions/{Sid} |  |
| [**listExecution**](StudioV1ExecutionApi.md#listExecution) | **GET** /v1/Flows/{FlowSid}/Executions |  |
| [**updateExecution**](StudioV1ExecutionApi.md#updateExecution) | **POST** /v1/Flows/{FlowSid}/Executions/{Sid} |  |


<a id="createExecution"></a>
# **createExecution**
> StudioV1FlowExecution createExecution(flowSid, from, to, parameters)



Triggers a new Execution for the Flow

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StudioV1ExecutionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://studio.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    StudioV1ExecutionApi apiInstance = new StudioV1ExecutionApi(defaultClient);
    String flowSid = "flowSid_example"; // String | The SID of the Excecution's Flow.
    String from = "from_example"; // String | The Twilio phone number to send messages or initiate calls from during the Flow's Execution. Available as variable `{{flow.channel.address}}`. For SMS, this can also be a Messaging Service SID.
    String to = "to_example"; // String | The Contact phone number to start a Studio Flow Execution, available as variable `{{contact.channel.address}}`.
    Object parameters = null; // Object | JSON data that will be added to the Flow's context and that can be accessed as variables inside your Flow. For example, if you pass in `Parameters={\\\"name\\\":\\\"Zeke\\\"}`, a widget in your Flow can reference the variable `{{flow.data.name}}`, which returns \\\"Zeke\\\". Note: the JSON value must explicitly be passed as a string, not as a hash object. Depending on your particular HTTP library, you may need to add quotes or URL encode the JSON string.
    try {
      StudioV1FlowExecution result = apiInstance.createExecution(flowSid, from, to, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StudioV1ExecutionApi#createExecution");
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
| **flowSid** | **String**| The SID of the Excecution&#39;s Flow. | |
| **from** | **String**| The Twilio phone number to send messages or initiate calls from during the Flow&#39;s Execution. Available as variable &#x60;{{flow.channel.address}}&#x60;. For SMS, this can also be a Messaging Service SID. | |
| **to** | **String**| The Contact phone number to start a Studio Flow Execution, available as variable &#x60;{{contact.channel.address}}&#x60;. | |
| **parameters** | [**Object**](Object.md)| JSON data that will be added to the Flow&#39;s context and that can be accessed as variables inside your Flow. For example, if you pass in &#x60;Parameters&#x3D;{\\\&quot;name\\\&quot;:\\\&quot;Zeke\\\&quot;}&#x60;, a widget in your Flow can reference the variable &#x60;{{flow.data.name}}&#x60;, which returns \\\&quot;Zeke\\\&quot;. Note: the JSON value must explicitly be passed as a string, not as a hash object. Depending on your particular HTTP library, you may need to add quotes or URL encode the JSON string. | [optional] |

### Return type

[**StudioV1FlowExecution**](StudioV1FlowExecution.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteExecution"></a>
# **deleteExecution**
> deleteExecution(flowSid, sid)



Delete the Execution and all Steps relating to it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StudioV1ExecutionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://studio.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    StudioV1ExecutionApi apiInstance = new StudioV1ExecutionApi(defaultClient);
    String flowSid = "flowSid_example"; // String | The SID of the Flow with the Execution resources to delete.
    String sid = "sid_example"; // String | The SID of the Execution resource to delete.
    try {
      apiInstance.deleteExecution(flowSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling StudioV1ExecutionApi#deleteExecution");
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
| **flowSid** | **String**| The SID of the Flow with the Execution resources to delete. | |
| **sid** | **String**| The SID of the Execution resource to delete. | |

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The resource was deleted successfully. |  -  |

<a id="fetchExecution"></a>
# **fetchExecution**
> StudioV1FlowExecution fetchExecution(flowSid, sid)



Retrieve an Execution

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StudioV1ExecutionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://studio.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    StudioV1ExecutionApi apiInstance = new StudioV1ExecutionApi(defaultClient);
    String flowSid = "flowSid_example"; // String | The SID of the Flow with the Execution resource to fetch
    String sid = "sid_example"; // String | The SID of the Execution resource to fetch.
    try {
      StudioV1FlowExecution result = apiInstance.fetchExecution(flowSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StudioV1ExecutionApi#fetchExecution");
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
| **flowSid** | **String**| The SID of the Flow with the Execution resource to fetch | |
| **sid** | **String**| The SID of the Execution resource to fetch. | |

### Return type

[**StudioV1FlowExecution**](StudioV1FlowExecution.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listExecution"></a>
# **listExecution**
> ListExecutionResponse listExecution(flowSid, dateCreatedFrom, dateCreatedTo, pageSize, page, pageToken)



Retrieve a list of all Executions for the Flow.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StudioV1ExecutionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://studio.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    StudioV1ExecutionApi apiInstance = new StudioV1ExecutionApi(defaultClient);
    String flowSid = "flowSid_example"; // String | The SID of the Flow with the Execution resources to read.
    OffsetDateTime dateCreatedFrom = OffsetDateTime.now(); // OffsetDateTime | Only show Execution resources starting on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time, given as `YYYY-MM-DDThh:mm:ss-hh:mm`.
    OffsetDateTime dateCreatedTo = OffsetDateTime.now(); // OffsetDateTime | Only show Execution resources starting before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time, given as `YYYY-MM-DDThh:mm:ss-hh:mm`.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListExecutionResponse result = apiInstance.listExecution(flowSid, dateCreatedFrom, dateCreatedTo, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StudioV1ExecutionApi#listExecution");
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
| **flowSid** | **String**| The SID of the Flow with the Execution resources to read. | |
| **dateCreatedFrom** | **OffsetDateTime**| Only show Execution resources starting on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time, given as &#x60;YYYY-MM-DDThh:mm:ss-hh:mm&#x60;. | [optional] |
| **dateCreatedTo** | **OffsetDateTime**| Only show Execution resources starting before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time, given as &#x60;YYYY-MM-DDThh:mm:ss-hh:mm&#x60;. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListExecutionResponse**](ListExecutionResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateExecution"></a>
# **updateExecution**
> StudioV1FlowExecution updateExecution(flowSid, sid, status)



Update the status of an Execution to &#x60;ended&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StudioV1ExecutionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://studio.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    StudioV1ExecutionApi apiInstance = new StudioV1ExecutionApi(defaultClient);
    String flowSid = "flowSid_example"; // String | The SID of the Flow with the Execution resources to update.
    String sid = "sid_example"; // String | The SID of the Execution resource to update.
    ExecutionEnumStatus status = ExecutionEnumStatus.fromValue("active"); // ExecutionEnumStatus | 
    try {
      StudioV1FlowExecution result = apiInstance.updateExecution(flowSid, sid, status);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StudioV1ExecutionApi#updateExecution");
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
| **flowSid** | **String**| The SID of the Flow with the Execution resources to update. | |
| **sid** | **String**| The SID of the Execution resource to update. | |
| **status** | **ExecutionEnumStatus**|  | [enum: active, ended] |

### Return type

[**StudioV1FlowExecution**](StudioV1FlowExecution.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

