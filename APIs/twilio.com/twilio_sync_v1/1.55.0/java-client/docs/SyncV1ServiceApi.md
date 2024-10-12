# SyncV1ServiceApi

All URIs are relative to *https://sync.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createService**](SyncV1ServiceApi.md#createService) | **POST** /v1/Services |  |
| [**deleteService**](SyncV1ServiceApi.md#deleteService) | **DELETE** /v1/Services/{Sid} |  |
| [**fetchService**](SyncV1ServiceApi.md#fetchService) | **GET** /v1/Services/{Sid} |  |
| [**listService**](SyncV1ServiceApi.md#listService) | **GET** /v1/Services |  |
| [**updateService**](SyncV1ServiceApi.md#updateService) | **POST** /v1/Services/{Sid} |  |


<a id="createService"></a>
# **createService**
> SyncV1Service createService(aclEnabled, friendlyName, reachabilityDebouncingEnabled, reachabilityDebouncingWindow, reachabilityWebhooksEnabled, webhookUrl, webhooksFromRestEnabled)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncV1ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sync.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SyncV1ServiceApi apiInstance = new SyncV1ServiceApi(defaultClient);
    Boolean aclEnabled = true; // Boolean | Whether token identities in the Service must be granted access to Sync objects by using the [Permissions](https://www.twilio.com/docs/sync/api/sync-permissions) resource.
    String friendlyName = "friendlyName_example"; // String | A string that you assign to describe the resource.
    Boolean reachabilityDebouncingEnabled = true; // Boolean | Whether every `endpoint_disconnected` event should occur after a configurable delay. The default is `false`, where the `endpoint_disconnected` event occurs immediately after disconnection. When `true`, intervening reconnections can prevent the `endpoint_disconnected` event.
    Integer reachabilityDebouncingWindow = 56; // Integer | The reachability event delay in milliseconds if `reachability_debouncing_enabled` = `true`.  Must be between 1,000 and 30,000 and defaults to 5,000. This is the number of milliseconds after the last running client disconnects, and a Sync identity is declared offline, before the `webhook_url` is called if all endpoints remain offline. A reconnection from the same identity by any endpoint during this interval prevents the call to `webhook_url`.
    Boolean reachabilityWebhooksEnabled = true; // Boolean | Whether the service instance should call `webhook_url` when client endpoints connect to Sync. The default is `false`.
    URI webhookUrl = new URI(); // URI | The URL we should call when Sync objects are manipulated.
    Boolean webhooksFromRestEnabled = true; // Boolean | Whether the Service instance should call `webhook_url` when the REST API is used to update Sync objects. The default is `false`.
    try {
      SyncV1Service result = apiInstance.createService(aclEnabled, friendlyName, reachabilityDebouncingEnabled, reachabilityDebouncingWindow, reachabilityWebhooksEnabled, webhookUrl, webhooksFromRestEnabled);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncV1ServiceApi#createService");
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
| **aclEnabled** | **Boolean**| Whether token identities in the Service must be granted access to Sync objects by using the [Permissions](https://www.twilio.com/docs/sync/api/sync-permissions) resource. | [optional] |
| **friendlyName** | **String**| A string that you assign to describe the resource. | [optional] |
| **reachabilityDebouncingEnabled** | **Boolean**| Whether every &#x60;endpoint_disconnected&#x60; event should occur after a configurable delay. The default is &#x60;false&#x60;, where the &#x60;endpoint_disconnected&#x60; event occurs immediately after disconnection. When &#x60;true&#x60;, intervening reconnections can prevent the &#x60;endpoint_disconnected&#x60; event. | [optional] |
| **reachabilityDebouncingWindow** | **Integer**| The reachability event delay in milliseconds if &#x60;reachability_debouncing_enabled&#x60; &#x3D; &#x60;true&#x60;.  Must be between 1,000 and 30,000 and defaults to 5,000. This is the number of milliseconds after the last running client disconnects, and a Sync identity is declared offline, before the &#x60;webhook_url&#x60; is called if all endpoints remain offline. A reconnection from the same identity by any endpoint during this interval prevents the call to &#x60;webhook_url&#x60;. | [optional] |
| **reachabilityWebhooksEnabled** | **Boolean**| Whether the service instance should call &#x60;webhook_url&#x60; when client endpoints connect to Sync. The default is &#x60;false&#x60;. | [optional] |
| **webhookUrl** | **URI**| The URL we should call when Sync objects are manipulated. | [optional] |
| **webhooksFromRestEnabled** | **Boolean**| Whether the Service instance should call &#x60;webhook_url&#x60; when the REST API is used to update Sync objects. The default is &#x60;false&#x60;. | [optional] |

### Return type

[**SyncV1Service**](SyncV1Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteService"></a>
# **deleteService**
> deleteService(sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncV1ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sync.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SyncV1ServiceApi apiInstance = new SyncV1ServiceApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the Service resource to delete.
    try {
      apiInstance.deleteService(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncV1ServiceApi#deleteService");
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
| **sid** | **String**| The SID of the Service resource to delete. | |

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

<a id="fetchService"></a>
# **fetchService**
> SyncV1Service fetchService(sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncV1ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sync.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SyncV1ServiceApi apiInstance = new SyncV1ServiceApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the Service resource to fetch.
    try {
      SyncV1Service result = apiInstance.fetchService(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncV1ServiceApi#fetchService");
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
| **sid** | **String**| The SID of the Service resource to fetch. | |

### Return type

[**SyncV1Service**](SyncV1Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listService"></a>
# **listService**
> ListServiceResponse listService(pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncV1ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sync.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SyncV1ServiceApi apiInstance = new SyncV1ServiceApi(defaultClient);
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListServiceResponse result = apiInstance.listService(pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncV1ServiceApi#listService");
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

[**ListServiceResponse**](ListServiceResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateService"></a>
# **updateService**
> SyncV1Service updateService(sid, aclEnabled, friendlyName, reachabilityDebouncingEnabled, reachabilityDebouncingWindow, reachabilityWebhooksEnabled, webhookUrl, webhooksFromRestEnabled)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncV1ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sync.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SyncV1ServiceApi apiInstance = new SyncV1ServiceApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the Service resource to update.
    Boolean aclEnabled = true; // Boolean | Whether token identities in the Service must be granted access to Sync objects by using the [Permissions](https://www.twilio.com/docs/sync/api/sync-permissions) resource.
    String friendlyName = "friendlyName_example"; // String | A string that you assign to describe the resource.
    Boolean reachabilityDebouncingEnabled = true; // Boolean | Whether every `endpoint_disconnected` event should occur after a configurable delay. The default is `false`, where the `endpoint_disconnected` event occurs immediately after disconnection. When `true`, intervening reconnections can prevent the `endpoint_disconnected` event.
    Integer reachabilityDebouncingWindow = 56; // Integer | The reachability event delay in milliseconds if `reachability_debouncing_enabled` = `true`.  Must be between 1,000 and 30,000 and defaults to 5,000. This is the number of milliseconds after the last running client disconnects, and a Sync identity is declared offline, before the webhook is called if all endpoints remain offline. A reconnection from the same identity by any endpoint during this interval prevents the webhook from being called.
    Boolean reachabilityWebhooksEnabled = true; // Boolean | Whether the service instance should call `webhook_url` when client endpoints connect to Sync. The default is `false`.
    URI webhookUrl = new URI(); // URI | The URL we should call when Sync objects are manipulated.
    Boolean webhooksFromRestEnabled = true; // Boolean | Whether the Service instance should call `webhook_url` when the REST API is used to update Sync objects. The default is `false`.
    try {
      SyncV1Service result = apiInstance.updateService(sid, aclEnabled, friendlyName, reachabilityDebouncingEnabled, reachabilityDebouncingWindow, reachabilityWebhooksEnabled, webhookUrl, webhooksFromRestEnabled);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncV1ServiceApi#updateService");
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
| **sid** | **String**| The SID of the Service resource to update. | |
| **aclEnabled** | **Boolean**| Whether token identities in the Service must be granted access to Sync objects by using the [Permissions](https://www.twilio.com/docs/sync/api/sync-permissions) resource. | [optional] |
| **friendlyName** | **String**| A string that you assign to describe the resource. | [optional] |
| **reachabilityDebouncingEnabled** | **Boolean**| Whether every &#x60;endpoint_disconnected&#x60; event should occur after a configurable delay. The default is &#x60;false&#x60;, where the &#x60;endpoint_disconnected&#x60; event occurs immediately after disconnection. When &#x60;true&#x60;, intervening reconnections can prevent the &#x60;endpoint_disconnected&#x60; event. | [optional] |
| **reachabilityDebouncingWindow** | **Integer**| The reachability event delay in milliseconds if &#x60;reachability_debouncing_enabled&#x60; &#x3D; &#x60;true&#x60;.  Must be between 1,000 and 30,000 and defaults to 5,000. This is the number of milliseconds after the last running client disconnects, and a Sync identity is declared offline, before the webhook is called if all endpoints remain offline. A reconnection from the same identity by any endpoint during this interval prevents the webhook from being called. | [optional] |
| **reachabilityWebhooksEnabled** | **Boolean**| Whether the service instance should call &#x60;webhook_url&#x60; when client endpoints connect to Sync. The default is &#x60;false&#x60;. | [optional] |
| **webhookUrl** | **URI**| The URL we should call when Sync objects are manipulated. | [optional] |
| **webhooksFromRestEnabled** | **Boolean**| Whether the Service instance should call &#x60;webhook_url&#x60; when the REST API is used to update Sync objects. The default is &#x60;false&#x60;. | [optional] |

### Return type

[**SyncV1Service**](SyncV1Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

