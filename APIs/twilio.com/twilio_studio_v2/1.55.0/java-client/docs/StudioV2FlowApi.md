# StudioV2FlowApi

All URIs are relative to *https://studio.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createFlow**](StudioV2FlowApi.md#createFlow) | **POST** /v2/Flows |  |
| [**deleteFlow**](StudioV2FlowApi.md#deleteFlow) | **DELETE** /v2/Flows/{Sid} |  |
| [**fetchFlow**](StudioV2FlowApi.md#fetchFlow) | **GET** /v2/Flows/{Sid} |  |
| [**listFlow**](StudioV2FlowApi.md#listFlow) | **GET** /v2/Flows |  |
| [**updateFlow**](StudioV2FlowApi.md#updateFlow) | **POST** /v2/Flows/{Sid} |  |


<a id="createFlow"></a>
# **createFlow**
> StudioV2Flow createFlow(definition, friendlyName, status, commitMessage)



Create a Flow.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StudioV2FlowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://studio.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    StudioV2FlowApi apiInstance = new StudioV2FlowApi(defaultClient);
    Object definition = null; // Object | JSON representation of flow definition.
    String friendlyName = "friendlyName_example"; // String | The string that you assigned to describe the Flow.
    FlowEnumStatus status = FlowEnumStatus.fromValue("draft"); // FlowEnumStatus | 
    String commitMessage = "commitMessage_example"; // String | Description of change made in the revision.
    try {
      StudioV2Flow result = apiInstance.createFlow(definition, friendlyName, status, commitMessage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StudioV2FlowApi#createFlow");
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
| **definition** | [**Object**](Object.md)| JSON representation of flow definition. | |
| **friendlyName** | **String**| The string that you assigned to describe the Flow. | |
| **status** | **FlowEnumStatus**|  | [enum: draft, published] |
| **commitMessage** | **String**| Description of change made in the revision. | [optional] |

### Return type

[**StudioV2Flow**](StudioV2Flow.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteFlow"></a>
# **deleteFlow**
> deleteFlow(sid)



Delete a specific Flow.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StudioV2FlowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://studio.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    StudioV2FlowApi apiInstance = new StudioV2FlowApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the Flow resource to delete.
    try {
      apiInstance.deleteFlow(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling StudioV2FlowApi#deleteFlow");
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
| **sid** | **String**| The SID of the Flow resource to delete. | |

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

<a id="fetchFlow"></a>
# **fetchFlow**
> StudioV2Flow fetchFlow(sid)



Retrieve a specific Flow.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StudioV2FlowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://studio.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    StudioV2FlowApi apiInstance = new StudioV2FlowApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the Flow resource to fetch.
    try {
      StudioV2Flow result = apiInstance.fetchFlow(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StudioV2FlowApi#fetchFlow");
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
| **sid** | **String**| The SID of the Flow resource to fetch. | |

### Return type

[**StudioV2Flow**](StudioV2Flow.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listFlow"></a>
# **listFlow**
> ListFlowResponse listFlow(pageSize, page, pageToken)



Retrieve a list of all Flows.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StudioV2FlowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://studio.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    StudioV2FlowApi apiInstance = new StudioV2FlowApi(defaultClient);
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListFlowResponse result = apiInstance.listFlow(pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StudioV2FlowApi#listFlow");
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
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListFlowResponse**](ListFlowResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateFlow"></a>
# **updateFlow**
> StudioV2Flow updateFlow(sid, status, commitMessage, definition, friendlyName)



Update a Flow.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StudioV2FlowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://studio.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    StudioV2FlowApi apiInstance = new StudioV2FlowApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the Flow resource to fetch.
    FlowEnumStatus status = FlowEnumStatus.fromValue("draft"); // FlowEnumStatus | 
    String commitMessage = "commitMessage_example"; // String | Description of change made in the revision.
    Object definition = null; // Object | JSON representation of flow definition.
    String friendlyName = "friendlyName_example"; // String | The string that you assigned to describe the Flow.
    try {
      StudioV2Flow result = apiInstance.updateFlow(sid, status, commitMessage, definition, friendlyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StudioV2FlowApi#updateFlow");
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
| **sid** | **String**| The SID of the Flow resource to fetch. | |
| **status** | **FlowEnumStatus**|  | [enum: draft, published] |
| **commitMessage** | **String**| Description of change made in the revision. | [optional] |
| **definition** | [**Object**](Object.md)| JSON representation of flow definition. | [optional] |
| **friendlyName** | **String**| The string that you assigned to describe the Flow. | [optional] |

### Return type

[**StudioV2Flow**](StudioV2Flow.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

