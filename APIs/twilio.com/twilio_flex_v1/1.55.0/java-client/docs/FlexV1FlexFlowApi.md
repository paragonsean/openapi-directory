# FlexV1FlexFlowApi

All URIs are relative to *https://flex-api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createFlexFlow**](FlexV1FlexFlowApi.md#createFlexFlow) | **POST** /v1/FlexFlows |  |
| [**deleteFlexFlow**](FlexV1FlexFlowApi.md#deleteFlexFlow) | **DELETE** /v1/FlexFlows/{Sid} |  |
| [**fetchFlexFlow**](FlexV1FlexFlowApi.md#fetchFlexFlow) | **GET** /v1/FlexFlows/{Sid} |  |
| [**listFlexFlow**](FlexV1FlexFlowApi.md#listFlexFlow) | **GET** /v1/FlexFlows |  |
| [**updateFlexFlow**](FlexV1FlexFlowApi.md#updateFlexFlow) | **POST** /v1/FlexFlows/{Sid} |  |


<a id="createFlexFlow"></a>
# **createFlexFlow**
> FlexV1FlexFlow createFlexFlow(channelType, chatServiceSid, friendlyName, contactIdentity, enabled, integrationChannel, integrationCreationOnMessage, integrationFlowSid, integrationPriority, integrationRetryCount, integrationTimeout, integrationUrl, integrationWorkflowSid, integrationWorkspaceSid, integrationType, janitorEnabled, longLived)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1FlexFlowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1FlexFlowApi apiInstance = new FlexV1FlexFlowApi(defaultClient);
    FlexFlowEnumChannelType channelType = FlexFlowEnumChannelType.fromValue("web"); // FlexFlowEnumChannelType | 
    String chatServiceSid = "chatServiceSid_example"; // String | The SID of the chat service.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the Flex Flow resource.
    String contactIdentity = "contactIdentity_example"; // String | The channel contact's Identity.
    Boolean enabled = true; // Boolean | Whether the new Flex Flow is enabled.
    String integrationChannel = "integrationChannel_example"; // String | The Task Channel SID (TCXXXX) or unique name (e.g., `sms`) to use for the Task that will be created. Applicable and required when `integrationType` is `task`. The default value is `default`.
    Boolean integrationCreationOnMessage = true; // Boolean | In the context of outbound messaging, defines whether to create a Task immediately (and therefore reserve the conversation to current agent), or delay Task creation until the customer sends the first response. Set to false to create immediately, true to delay Task creation. This setting is only applicable for outbound messaging.
    String integrationFlowSid = "integrationFlowSid_example"; // String | The SID of the Studio Flow. Required when `integrationType` is `studio`.
    Integer integrationPriority = 56; // Integer | The Task priority of a new Task. The default priority is 0. Optional when `integrationType` is `task`, not applicable otherwise.
    Integer integrationRetryCount = 56; // Integer | The number of times to retry the Studio Flow or webhook in case of failure. Takes integer values from 0 to 3 with the default being 3. Optional when `integrationType` is `studio` or `external`, not applicable otherwise.
    Integer integrationTimeout = 56; // Integer | The Task timeout in seconds for a new Task. Default is 86,400 seconds (24 hours). Optional when `integrationType` is `task`, not applicable otherwise.
    URI integrationUrl = new URI(); // URI | The URL of the external webhook. Required when `integrationType` is `external`.
    String integrationWorkflowSid = "integrationWorkflowSid_example"; // String | The Workflow SID for a new Task. Required when `integrationType` is `task`.
    String integrationWorkspaceSid = "integrationWorkspaceSid_example"; // String | The Workspace SID for a new Task. Required when `integrationType` is `task`.
    FlexFlowEnumIntegrationType integrationType = FlexFlowEnumIntegrationType.fromValue("studio"); // FlexFlowEnumIntegrationType | 
    Boolean janitorEnabled = true; // Boolean | When enabled, the Messaging Channel Janitor will remove active Proxy sessions if the associated Task is deleted outside of the Flex UI. Defaults to `false`.
    Boolean longLived = true; // Boolean | When enabled, Flex will keep the chat channel active so that it may be used for subsequent interactions with a contact identity. Defaults to `false`.
    try {
      FlexV1FlexFlow result = apiInstance.createFlexFlow(channelType, chatServiceSid, friendlyName, contactIdentity, enabled, integrationChannel, integrationCreationOnMessage, integrationFlowSid, integrationPriority, integrationRetryCount, integrationTimeout, integrationUrl, integrationWorkflowSid, integrationWorkspaceSid, integrationType, janitorEnabled, longLived);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1FlexFlowApi#createFlexFlow");
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
| **channelType** | **FlexFlowEnumChannelType**|  | [enum: web, sms, facebook, whatsapp, line, custom] |
| **chatServiceSid** | **String**| The SID of the chat service. | |
| **friendlyName** | **String**| A descriptive string that you create to describe the Flex Flow resource. | |
| **contactIdentity** | **String**| The channel contact&#39;s Identity. | [optional] |
| **enabled** | **Boolean**| Whether the new Flex Flow is enabled. | [optional] |
| **integrationChannel** | **String**| The Task Channel SID (TCXXXX) or unique name (e.g., &#x60;sms&#x60;) to use for the Task that will be created. Applicable and required when &#x60;integrationType&#x60; is &#x60;task&#x60;. The default value is &#x60;default&#x60;. | [optional] |
| **integrationCreationOnMessage** | **Boolean**| In the context of outbound messaging, defines whether to create a Task immediately (and therefore reserve the conversation to current agent), or delay Task creation until the customer sends the first response. Set to false to create immediately, true to delay Task creation. This setting is only applicable for outbound messaging. | [optional] |
| **integrationFlowSid** | **String**| The SID of the Studio Flow. Required when &#x60;integrationType&#x60; is &#x60;studio&#x60;. | [optional] |
| **integrationPriority** | **Integer**| The Task priority of a new Task. The default priority is 0. Optional when &#x60;integrationType&#x60; is &#x60;task&#x60;, not applicable otherwise. | [optional] |
| **integrationRetryCount** | **Integer**| The number of times to retry the Studio Flow or webhook in case of failure. Takes integer values from 0 to 3 with the default being 3. Optional when &#x60;integrationType&#x60; is &#x60;studio&#x60; or &#x60;external&#x60;, not applicable otherwise. | [optional] |
| **integrationTimeout** | **Integer**| The Task timeout in seconds for a new Task. Default is 86,400 seconds (24 hours). Optional when &#x60;integrationType&#x60; is &#x60;task&#x60;, not applicable otherwise. | [optional] |
| **integrationUrl** | **URI**| The URL of the external webhook. Required when &#x60;integrationType&#x60; is &#x60;external&#x60;. | [optional] |
| **integrationWorkflowSid** | **String**| The Workflow SID for a new Task. Required when &#x60;integrationType&#x60; is &#x60;task&#x60;. | [optional] |
| **integrationWorkspaceSid** | **String**| The Workspace SID for a new Task. Required when &#x60;integrationType&#x60; is &#x60;task&#x60;. | [optional] |
| **integrationType** | **FlexFlowEnumIntegrationType**|  | [optional] [enum: studio, external, task] |
| **janitorEnabled** | **Boolean**| When enabled, the Messaging Channel Janitor will remove active Proxy sessions if the associated Task is deleted outside of the Flex UI. Defaults to &#x60;false&#x60;. | [optional] |
| **longLived** | **Boolean**| When enabled, Flex will keep the chat channel active so that it may be used for subsequent interactions with a contact identity. Defaults to &#x60;false&#x60;. | [optional] |

### Return type

[**FlexV1FlexFlow**](FlexV1FlexFlow.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteFlexFlow"></a>
# **deleteFlexFlow**
> deleteFlexFlow(sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1FlexFlowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1FlexFlowApi apiInstance = new FlexV1FlexFlowApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the Flex Flow resource to delete.
    try {
      apiInstance.deleteFlexFlow(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1FlexFlowApi#deleteFlexFlow");
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
| **sid** | **String**| The SID of the Flex Flow resource to delete. | |

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

<a id="fetchFlexFlow"></a>
# **fetchFlexFlow**
> FlexV1FlexFlow fetchFlexFlow(sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1FlexFlowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1FlexFlowApi apiInstance = new FlexV1FlexFlowApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the Flex Flow resource to fetch.
    try {
      FlexV1FlexFlow result = apiInstance.fetchFlexFlow(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1FlexFlowApi#fetchFlexFlow");
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
| **sid** | **String**| The SID of the Flex Flow resource to fetch. | |

### Return type

[**FlexV1FlexFlow**](FlexV1FlexFlow.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listFlexFlow"></a>
# **listFlexFlow**
> ListFlexFlowResponse listFlexFlow(friendlyName, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1FlexFlowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1FlexFlowApi apiInstance = new FlexV1FlexFlowApi(defaultClient);
    String friendlyName = "friendlyName_example"; // String | The `friendly_name` of the Flex Flow resources to read.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListFlexFlowResponse result = apiInstance.listFlexFlow(friendlyName, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1FlexFlowApi#listFlexFlow");
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
| **friendlyName** | **String**| The &#x60;friendly_name&#x60; of the Flex Flow resources to read. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListFlexFlowResponse**](ListFlexFlowResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateFlexFlow"></a>
# **updateFlexFlow**
> FlexV1FlexFlow updateFlexFlow(sid, channelType, chatServiceSid, contactIdentity, enabled, friendlyName, integrationChannel, integrationCreationOnMessage, integrationFlowSid, integrationPriority, integrationRetryCount, integrationTimeout, integrationUrl, integrationWorkflowSid, integrationWorkspaceSid, integrationType, janitorEnabled, longLived)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1FlexFlowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1FlexFlowApi apiInstance = new FlexV1FlexFlowApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the Flex Flow resource to update.
    FlexFlowEnumChannelType channelType = FlexFlowEnumChannelType.fromValue("web"); // FlexFlowEnumChannelType | 
    String chatServiceSid = "chatServiceSid_example"; // String | The SID of the chat service.
    String contactIdentity = "contactIdentity_example"; // String | The channel contact's Identity.
    Boolean enabled = true; // Boolean | Whether the new Flex Flow is enabled.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the Flex Flow resource.
    String integrationChannel = "integrationChannel_example"; // String | The Task Channel SID (TCXXXX) or unique name (e.g., `sms`) to use for the Task that will be created. Applicable and required when `integrationType` is `task`. The default value is `default`.
    Boolean integrationCreationOnMessage = true; // Boolean | In the context of outbound messaging, defines whether to create a Task immediately (and therefore reserve the conversation to current agent), or delay Task creation until the customer sends the first response. Set to false to create immediately, true to delay Task creation. This setting is only applicable for outbound messaging.
    String integrationFlowSid = "integrationFlowSid_example"; // String | The SID of the Studio Flow. Required when `integrationType` is `studio`.
    Integer integrationPriority = 56; // Integer | The Task priority of a new Task. The default priority is 0. Optional when `integrationType` is `task`, not applicable otherwise.
    Integer integrationRetryCount = 56; // Integer | The number of times to retry the Studio Flow or webhook in case of failure. Takes integer values from 0 to 3 with the default being 3. Optional when `integrationType` is `studio` or `external`, not applicable otherwise.
    Integer integrationTimeout = 56; // Integer | The Task timeout in seconds for a new Task. Default is 86,400 seconds (24 hours). Optional when `integrationType` is `task`, not applicable otherwise.
    URI integrationUrl = new URI(); // URI | The URL of the external webhook. Required when `integrationType` is `external`.
    String integrationWorkflowSid = "integrationWorkflowSid_example"; // String | The Workflow SID for a new Task. Required when `integrationType` is `task`.
    String integrationWorkspaceSid = "integrationWorkspaceSid_example"; // String | The Workspace SID for a new Task. Required when `integrationType` is `task`.
    FlexFlowEnumIntegrationType integrationType = FlexFlowEnumIntegrationType.fromValue("studio"); // FlexFlowEnumIntegrationType | 
    Boolean janitorEnabled = true; // Boolean | When enabled, the Messaging Channel Janitor will remove active Proxy sessions if the associated Task is deleted outside of the Flex UI. Defaults to `false`.
    Boolean longLived = true; // Boolean | When enabled, Flex will keep the chat channel active so that it may be used for subsequent interactions with a contact identity. Defaults to `false`.
    try {
      FlexV1FlexFlow result = apiInstance.updateFlexFlow(sid, channelType, chatServiceSid, contactIdentity, enabled, friendlyName, integrationChannel, integrationCreationOnMessage, integrationFlowSid, integrationPriority, integrationRetryCount, integrationTimeout, integrationUrl, integrationWorkflowSid, integrationWorkspaceSid, integrationType, janitorEnabled, longLived);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1FlexFlowApi#updateFlexFlow");
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
| **sid** | **String**| The SID of the Flex Flow resource to update. | |
| **channelType** | **FlexFlowEnumChannelType**|  | [optional] [enum: web, sms, facebook, whatsapp, line, custom] |
| **chatServiceSid** | **String**| The SID of the chat service. | [optional] |
| **contactIdentity** | **String**| The channel contact&#39;s Identity. | [optional] |
| **enabled** | **Boolean**| Whether the new Flex Flow is enabled. | [optional] |
| **friendlyName** | **String**| A descriptive string that you create to describe the Flex Flow resource. | [optional] |
| **integrationChannel** | **String**| The Task Channel SID (TCXXXX) or unique name (e.g., &#x60;sms&#x60;) to use for the Task that will be created. Applicable and required when &#x60;integrationType&#x60; is &#x60;task&#x60;. The default value is &#x60;default&#x60;. | [optional] |
| **integrationCreationOnMessage** | **Boolean**| In the context of outbound messaging, defines whether to create a Task immediately (and therefore reserve the conversation to current agent), or delay Task creation until the customer sends the first response. Set to false to create immediately, true to delay Task creation. This setting is only applicable for outbound messaging. | [optional] |
| **integrationFlowSid** | **String**| The SID of the Studio Flow. Required when &#x60;integrationType&#x60; is &#x60;studio&#x60;. | [optional] |
| **integrationPriority** | **Integer**| The Task priority of a new Task. The default priority is 0. Optional when &#x60;integrationType&#x60; is &#x60;task&#x60;, not applicable otherwise. | [optional] |
| **integrationRetryCount** | **Integer**| The number of times to retry the Studio Flow or webhook in case of failure. Takes integer values from 0 to 3 with the default being 3. Optional when &#x60;integrationType&#x60; is &#x60;studio&#x60; or &#x60;external&#x60;, not applicable otherwise. | [optional] |
| **integrationTimeout** | **Integer**| The Task timeout in seconds for a new Task. Default is 86,400 seconds (24 hours). Optional when &#x60;integrationType&#x60; is &#x60;task&#x60;, not applicable otherwise. | [optional] |
| **integrationUrl** | **URI**| The URL of the external webhook. Required when &#x60;integrationType&#x60; is &#x60;external&#x60;. | [optional] |
| **integrationWorkflowSid** | **String**| The Workflow SID for a new Task. Required when &#x60;integrationType&#x60; is &#x60;task&#x60;. | [optional] |
| **integrationWorkspaceSid** | **String**| The Workspace SID for a new Task. Required when &#x60;integrationType&#x60; is &#x60;task&#x60;. | [optional] |
| **integrationType** | **FlexFlowEnumIntegrationType**|  | [optional] [enum: studio, external, task] |
| **janitorEnabled** | **Boolean**| When enabled, the Messaging Channel Janitor will remove active Proxy sessions if the associated Task is deleted outside of the Flex UI. Defaults to &#x60;false&#x60;. | [optional] |
| **longLived** | **Boolean**| When enabled, Flex will keep the chat channel active so that it may be used for subsequent interactions with a contact identity. Defaults to &#x60;false&#x60;. | [optional] |

### Return type

[**FlexV1FlexFlow**](FlexV1FlexFlow.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

