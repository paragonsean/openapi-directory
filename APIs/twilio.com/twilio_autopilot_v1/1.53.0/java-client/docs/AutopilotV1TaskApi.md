# AutopilotV1TaskApi

All URIs are relative to *https://autopilot.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createTask**](AutopilotV1TaskApi.md#createTask) | **POST** /v1/Assistants/{AssistantSid}/Tasks |  |
| [**deleteTask**](AutopilotV1TaskApi.md#deleteTask) | **DELETE** /v1/Assistants/{AssistantSid}/Tasks/{Sid} |  |
| [**fetchTask**](AutopilotV1TaskApi.md#fetchTask) | **GET** /v1/Assistants/{AssistantSid}/Tasks/{Sid} |  |
| [**listTask**](AutopilotV1TaskApi.md#listTask) | **GET** /v1/Assistants/{AssistantSid}/Tasks |  |
| [**updateTask**](AutopilotV1TaskApi.md#updateTask) | **POST** /v1/Assistants/{AssistantSid}/Tasks/{Sid} |  |


<a id="createTask"></a>
# **createTask**
> AutopilotV1AssistantTask createTask(assistantSid, uniqueName, actions, actionsUrl, friendlyName)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutopilotV1TaskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://autopilot.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    AutopilotV1TaskApi apiInstance = new AutopilotV1TaskApi(defaultClient);
    String assistantSid = "assistantSid_example"; // String | The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the new resource.
    String uniqueName = "uniqueName_example"; // String | An application-defined string that uniquely identifies the new resource. It can be used as an alternative to the `sid` in the URL path to address the resource. This value must be unique and 64 characters or less in length.
    Object actions = null; // Object | The JSON string that specifies the [actions](https://www.twilio.com/docs/autopilot/actions) that instruct the Assistant on how to perform the task. It is optional and not unique.
    URI actionsUrl = new URI(); // URI | The URL from which the Assistant can fetch actions.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the new resource. It is not unique and can be up to 255 characters long.
    try {
      AutopilotV1AssistantTask result = apiInstance.createTask(assistantSid, uniqueName, actions, actionsUrl, friendlyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutopilotV1TaskApi#createTask");
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
| **assistantSid** | **String**| The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the new resource. | |
| **uniqueName** | **String**| An application-defined string that uniquely identifies the new resource. It can be used as an alternative to the &#x60;sid&#x60; in the URL path to address the resource. This value must be unique and 64 characters or less in length. | |
| **actions** | [**Object**](Object.md)| The JSON string that specifies the [actions](https://www.twilio.com/docs/autopilot/actions) that instruct the Assistant on how to perform the task. It is optional and not unique. | [optional] |
| **actionsUrl** | **URI**| The URL from which the Assistant can fetch actions. | [optional] |
| **friendlyName** | **String**| A descriptive string that you create to describe the new resource. It is not unique and can be up to 255 characters long. | [optional] |

### Return type

[**AutopilotV1AssistantTask**](AutopilotV1AssistantTask.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteTask"></a>
# **deleteTask**
> deleteTask(assistantSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutopilotV1TaskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://autopilot.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    AutopilotV1TaskApi apiInstance = new AutopilotV1TaskApi(defaultClient);
    String assistantSid = "assistantSid_example"; // String | The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resources to delete.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Task resource to delete.
    try {
      apiInstance.deleteTask(assistantSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutopilotV1TaskApi#deleteTask");
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
| **assistantSid** | **String**| The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resources to delete. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Task resource to delete. | |

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

<a id="fetchTask"></a>
# **fetchTask**
> AutopilotV1AssistantTask fetchTask(assistantSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutopilotV1TaskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://autopilot.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    AutopilotV1TaskApi apiInstance = new AutopilotV1TaskApi(defaultClient);
    String assistantSid = "assistantSid_example"; // String | The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to fetch.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Task resource to fetch.
    try {
      AutopilotV1AssistantTask result = apiInstance.fetchTask(assistantSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutopilotV1TaskApi#fetchTask");
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
| **assistantSid** | **String**| The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to fetch. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Task resource to fetch. | |

### Return type

[**AutopilotV1AssistantTask**](AutopilotV1AssistantTask.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listTask"></a>
# **listTask**
> ListTaskResponse listTask(assistantSid, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutopilotV1TaskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://autopilot.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    AutopilotV1TaskApi apiInstance = new AutopilotV1TaskApi(defaultClient);
    String assistantSid = "assistantSid_example"; // String | The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resources to read.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListTaskResponse result = apiInstance.listTask(assistantSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutopilotV1TaskApi#listTask");
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
| **assistantSid** | **String**| The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resources to read. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListTaskResponse**](ListTaskResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateTask"></a>
# **updateTask**
> AutopilotV1AssistantTask updateTask(assistantSid, sid, actions, actionsUrl, friendlyName, uniqueName)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutopilotV1TaskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://autopilot.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    AutopilotV1TaskApi apiInstance = new AutopilotV1TaskApi(defaultClient);
    String assistantSid = "assistantSid_example"; // String | The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to update.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Task resource to update.
    Object actions = null; // Object | The JSON string that specifies the [actions](https://www.twilio.com/docs/autopilot/actions) that instruct the Assistant on how to perform the task.
    URI actionsUrl = new URI(); // URI | The URL from which the Assistant can fetch actions.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
    String uniqueName = "uniqueName_example"; // String | An application-defined string that uniquely identifies the resource. This value must be 64 characters or less in length and be unique. It can be used as an alternative to the `sid` in the URL path to address the resource.
    try {
      AutopilotV1AssistantTask result = apiInstance.updateTask(assistantSid, sid, actions, actionsUrl, friendlyName, uniqueName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutopilotV1TaskApi#updateTask");
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
| **assistantSid** | **String**| The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to update. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Task resource to update. | |
| **actions** | [**Object**](Object.md)| The JSON string that specifies the [actions](https://www.twilio.com/docs/autopilot/actions) that instruct the Assistant on how to perform the task. | [optional] |
| **actionsUrl** | **URI**| The URL from which the Assistant can fetch actions. | [optional] |
| **friendlyName** | **String**| A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long. | [optional] |
| **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. This value must be 64 characters or less in length and be unique. It can be used as an alternative to the &#x60;sid&#x60; in the URL path to address the resource. | [optional] |

### Return type

[**AutopilotV1AssistantTask**](AutopilotV1AssistantTask.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

