# AutopilotV1ModelBuildApi

All URIs are relative to *https://autopilot.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createModelBuild**](AutopilotV1ModelBuildApi.md#createModelBuild) | **POST** /v1/Assistants/{AssistantSid}/ModelBuilds |  |
| [**deleteModelBuild**](AutopilotV1ModelBuildApi.md#deleteModelBuild) | **DELETE** /v1/Assistants/{AssistantSid}/ModelBuilds/{Sid} |  |
| [**fetchModelBuild**](AutopilotV1ModelBuildApi.md#fetchModelBuild) | **GET** /v1/Assistants/{AssistantSid}/ModelBuilds/{Sid} |  |
| [**listModelBuild**](AutopilotV1ModelBuildApi.md#listModelBuild) | **GET** /v1/Assistants/{AssistantSid}/ModelBuilds |  |
| [**updateModelBuild**](AutopilotV1ModelBuildApi.md#updateModelBuild) | **POST** /v1/Assistants/{AssistantSid}/ModelBuilds/{Sid} |  |


<a id="createModelBuild"></a>
# **createModelBuild**
> AutopilotV1AssistantModelBuild createModelBuild(assistantSid, statusCallback, uniqueName)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutopilotV1ModelBuildApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://autopilot.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    AutopilotV1ModelBuildApi apiInstance = new AutopilotV1ModelBuildApi(defaultClient);
    String assistantSid = "assistantSid_example"; // String | The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the new resource.
    URI statusCallback = new URI(); // URI | The URL we should call using a POST method to send status information to your application.
    String uniqueName = "uniqueName_example"; // String | An application-defined string that uniquely identifies the new resource. This value must be a unique string of no more than 64 characters. It can be used as an alternative to the `sid` in the URL path to address the resource.
    try {
      AutopilotV1AssistantModelBuild result = apiInstance.createModelBuild(assistantSid, statusCallback, uniqueName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutopilotV1ModelBuildApi#createModelBuild");
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
| **statusCallback** | **URI**| The URL we should call using a POST method to send status information to your application. | [optional] |
| **uniqueName** | **String**| An application-defined string that uniquely identifies the new resource. This value must be a unique string of no more than 64 characters. It can be used as an alternative to the &#x60;sid&#x60; in the URL path to address the resource. | [optional] |

### Return type

[**AutopilotV1AssistantModelBuild**](AutopilotV1AssistantModelBuild.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteModelBuild"></a>
# **deleteModelBuild**
> deleteModelBuild(assistantSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutopilotV1ModelBuildApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://autopilot.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    AutopilotV1ModelBuildApi apiInstance = new AutopilotV1ModelBuildApi(defaultClient);
    String assistantSid = "assistantSid_example"; // String | The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resources to delete.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the ModelBuild resource to delete.
    try {
      apiInstance.deleteModelBuild(assistantSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutopilotV1ModelBuildApi#deleteModelBuild");
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
| **sid** | **String**| The Twilio-provided string that uniquely identifies the ModelBuild resource to delete. | |

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

<a id="fetchModelBuild"></a>
# **fetchModelBuild**
> AutopilotV1AssistantModelBuild fetchModelBuild(assistantSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutopilotV1ModelBuildApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://autopilot.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    AutopilotV1ModelBuildApi apiInstance = new AutopilotV1ModelBuildApi(defaultClient);
    String assistantSid = "assistantSid_example"; // String | The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to fetch.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the ModelBuild resource to fetch.
    try {
      AutopilotV1AssistantModelBuild result = apiInstance.fetchModelBuild(assistantSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutopilotV1ModelBuildApi#fetchModelBuild");
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
| **sid** | **String**| The Twilio-provided string that uniquely identifies the ModelBuild resource to fetch. | |

### Return type

[**AutopilotV1AssistantModelBuild**](AutopilotV1AssistantModelBuild.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listModelBuild"></a>
# **listModelBuild**
> ListModelBuildResponse listModelBuild(assistantSid, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutopilotV1ModelBuildApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://autopilot.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    AutopilotV1ModelBuildApi apiInstance = new AutopilotV1ModelBuildApi(defaultClient);
    String assistantSid = "assistantSid_example"; // String | The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resources to read.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListModelBuildResponse result = apiInstance.listModelBuild(assistantSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutopilotV1ModelBuildApi#listModelBuild");
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

[**ListModelBuildResponse**](ListModelBuildResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateModelBuild"></a>
# **updateModelBuild**
> AutopilotV1AssistantModelBuild updateModelBuild(assistantSid, sid, uniqueName)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutopilotV1ModelBuildApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://autopilot.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    AutopilotV1ModelBuildApi apiInstance = new AutopilotV1ModelBuildApi(defaultClient);
    String assistantSid = "assistantSid_example"; // String | The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to update.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the ModelBuild resource to update.
    String uniqueName = "uniqueName_example"; // String | An application-defined string that uniquely identifies the resource. This value must be a unique string of no more than 64 characters. It can be used as an alternative to the `sid` in the URL path to address the resource.
    try {
      AutopilotV1AssistantModelBuild result = apiInstance.updateModelBuild(assistantSid, sid, uniqueName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutopilotV1ModelBuildApi#updateModelBuild");
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
| **sid** | **String**| The Twilio-provided string that uniquely identifies the ModelBuild resource to update. | |
| **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. This value must be a unique string of no more than 64 characters. It can be used as an alternative to the &#x60;sid&#x60; in the URL path to address the resource. | [optional] |

### Return type

[**AutopilotV1AssistantModelBuild**](AutopilotV1AssistantModelBuild.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

