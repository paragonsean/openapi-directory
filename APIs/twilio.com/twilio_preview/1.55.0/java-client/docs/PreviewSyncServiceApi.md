# PreviewSyncServiceApi

All URIs are relative to *https://preview.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSyncService**](PreviewSyncServiceApi.md#createSyncService) | **POST** /Sync/Services |  |
| [**deleteSyncService**](PreviewSyncServiceApi.md#deleteSyncService) | **DELETE** /Sync/Services/{Sid} |  |
| [**fetchSyncService**](PreviewSyncServiceApi.md#fetchSyncService) | **GET** /Sync/Services/{Sid} |  |
| [**listSyncService**](PreviewSyncServiceApi.md#listSyncService) | **GET** /Sync/Services |  |
| [**updateSyncService**](PreviewSyncServiceApi.md#updateSyncService) | **POST** /Sync/Services/{Sid} |  |


<a id="createSyncService"></a>
# **createSyncService**
> PreviewSyncService createSyncService(aclEnabled, friendlyName, reachabilityWebhooksEnabled, webhookUrl)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewSyncServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewSyncServiceApi apiInstance = new PreviewSyncServiceApi(defaultClient);
    Boolean aclEnabled = true; // Boolean | 
    String friendlyName = "friendlyName_example"; // String | 
    Boolean reachabilityWebhooksEnabled = true; // Boolean | 
    URI webhookUrl = new URI(); // URI | 
    try {
      PreviewSyncService result = apiInstance.createSyncService(aclEnabled, friendlyName, reachabilityWebhooksEnabled, webhookUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewSyncServiceApi#createSyncService");
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
| **aclEnabled** | **Boolean**|  | [optional] |
| **friendlyName** | **String**|  | [optional] |
| **reachabilityWebhooksEnabled** | **Boolean**|  | [optional] |
| **webhookUrl** | **URI**|  | [optional] |

### Return type

[**PreviewSyncService**](PreviewSyncService.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteSyncService"></a>
# **deleteSyncService**
> deleteSyncService(sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewSyncServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewSyncServiceApi apiInstance = new PreviewSyncServiceApi(defaultClient);
    String sid = "sid_example"; // String | 
    try {
      apiInstance.deleteSyncService(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewSyncServiceApi#deleteSyncService");
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
| **sid** | **String**|  | |

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

<a id="fetchSyncService"></a>
# **fetchSyncService**
> PreviewSyncService fetchSyncService(sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewSyncServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewSyncServiceApi apiInstance = new PreviewSyncServiceApi(defaultClient);
    String sid = "sid_example"; // String | 
    try {
      PreviewSyncService result = apiInstance.fetchSyncService(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewSyncServiceApi#fetchSyncService");
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
| **sid** | **String**|  | |

### Return type

[**PreviewSyncService**](PreviewSyncService.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listSyncService"></a>
# **listSyncService**
> ListSyncServiceResponse listSyncService(pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewSyncServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewSyncServiceApi apiInstance = new PreviewSyncServiceApi(defaultClient);
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListSyncServiceResponse result = apiInstance.listSyncService(pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewSyncServiceApi#listSyncService");
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

[**ListSyncServiceResponse**](ListSyncServiceResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateSyncService"></a>
# **updateSyncService**
> PreviewSyncService updateSyncService(sid, aclEnabled, friendlyName, reachabilityWebhooksEnabled, webhookUrl)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewSyncServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewSyncServiceApi apiInstance = new PreviewSyncServiceApi(defaultClient);
    String sid = "sid_example"; // String | 
    Boolean aclEnabled = true; // Boolean | 
    String friendlyName = "friendlyName_example"; // String | 
    Boolean reachabilityWebhooksEnabled = true; // Boolean | 
    URI webhookUrl = new URI(); // URI | 
    try {
      PreviewSyncService result = apiInstance.updateSyncService(sid, aclEnabled, friendlyName, reachabilityWebhooksEnabled, webhookUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewSyncServiceApi#updateSyncService");
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
| **sid** | **String**|  | |
| **aclEnabled** | **Boolean**|  | [optional] |
| **friendlyName** | **String**|  | [optional] |
| **reachabilityWebhooksEnabled** | **Boolean**|  | [optional] |
| **webhookUrl** | **URI**|  | [optional] |

### Return type

[**PreviewSyncService**](PreviewSyncService.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

