# SystemApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteFeed**](SystemApi.md#deleteFeed) | **DELETE** /system/feeds/{feed} |  |
| [**deleteFeedGroup**](SystemApi.md#deleteFeedGroup) | **DELETE** /system/feeds/{feed}/{group} |  |
| [**deleteService**](SystemApi.md#deleteService) | **DELETE** /system/services/{servicename}/{hostid} | Delete the service config |
| [**describeErrorCodes**](SystemApi.md#describeErrorCodes) | **GET** /system/error_codes | Describe anchore engine error codes. |
| [**describePolicy**](SystemApi.md#describePolicy) | **GET** /system/policy_spec | Describe the policy language spec implemented by this service. |
| [**getServiceDetail**](SystemApi.md#getServiceDetail) | **GET** /system | System status |
| [**getServicesByName**](SystemApi.md#getServicesByName) | **GET** /system/services/{servicename} | Get a service configuration and state |
| [**getServicesByNameAndHost**](SystemApi.md#getServicesByNameAndHost) | **GET** /system/services/{servicename}/{hostid} | Get service config for a specific host |
| [**getStatus**](SystemApi.md#getStatus) | **GET** /status | Service status |
| [**getSystemFeeds**](SystemApi.md#getSystemFeeds) | **GET** /system/feeds | list feeds operations and information |
| [**listServices**](SystemApi.md#listServices) | **GET** /system/services | List system services |
| [**postSystemFeeds**](SystemApi.md#postSystemFeeds) | **POST** /system/feeds | trigger feeds operations |
| [**testWebhook**](SystemApi.md#testWebhook) | **POST** /system/webhooks/{webhook_type}/test | Adds the capabilities to test a webhook delivery for the given notification type |
| [**toggleFeedEnabled**](SystemApi.md#toggleFeedEnabled) | **PUT** /system/feeds/{feed} |  |
| [**toggleGroupEnabled**](SystemApi.md#toggleGroupEnabled) | **PUT** /system/feeds/{feed}/{group} |  |


<a id="deleteFeed"></a>
# **deleteFeed**
> deleteFeed(feed)



Delete the groups and data for the feed and disable the feed itself

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    SystemApi apiInstance = new SystemApi(defaultClient);
    String feed = "feed_example"; // String | 
    try {
      apiInstance.deleteFeed(feed);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemApi#deleteFeed");
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
| **feed** | **String**|  | |

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
| **200** | Successfully deleted |  -  |
| **404** | Not found |  -  |
| **500** | Internal server error processing the request. Retry expected |  -  |

<a id="deleteFeedGroup"></a>
# **deleteFeedGroup**
> deleteFeedGroup(feed, group)



Delete the group data and disable the group itself

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    SystemApi apiInstance = new SystemApi(defaultClient);
    String feed = "feed_example"; // String | 
    String group = "group_example"; // String | 
    try {
      apiInstance.deleteFeedGroup(feed, group);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemApi#deleteFeedGroup");
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
| **feed** | **String**|  | |
| **group** | **String**|  | |

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
| **200** | Successfully deleted |  -  |
| **404** | Not found |  -  |
| **500** | Internal server error processing the request. Retry expected |  -  |

<a id="deleteService"></a>
# **deleteService**
> deleteService(servicename, hostid)

Delete the service config

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    SystemApi apiInstance = new SystemApi(defaultClient);
    String servicename = "servicename_example"; // String | 
    String hostid = "hostid_example"; // String | 
    try {
      apiInstance.deleteService(servicename, hostid);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemApi#deleteService");
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
| **servicename** | **String**|  | |
| **hostid** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Delete success |  -  |
| **500** | Internal error |  -  |

<a id="describeErrorCodes"></a>
# **describeErrorCodes**
> List&lt;AnchoreErrorCode&gt; describeErrorCodes()

Describe anchore engine error codes.

Describe anchore engine error codes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    SystemApi apiInstance = new SystemApi(defaultClient);
    try {
      List<AnchoreErrorCode> result = apiInstance.describeErrorCodes();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemApi#describeErrorCodes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;AnchoreErrorCode&gt;**](AnchoreErrorCode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Error Codes Description |  -  |

<a id="describePolicy"></a>
# **describePolicy**
> List&lt;GateSpec&gt; describePolicy()

Describe the policy language spec implemented by this service.

Get the policy language spec for this service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    SystemApi apiInstance = new SystemApi(defaultClient);
    try {
      List<GateSpec> result = apiInstance.describePolicy();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemApi#describePolicy");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;GateSpec&gt;**](GateSpec.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Policy Language Description |  -  |

<a id="getServiceDetail"></a>
# **getServiceDetail**
> SystemStatusResponse getServiceDetail()

System status

Get the system status including queue lengths

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    SystemApi apiInstance = new SystemApi(defaultClient);
    try {
      SystemStatusResponse result = apiInstance.getServiceDetail();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemApi#getServiceDetail");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemStatusResponse**](SystemStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status listing |  -  |
| **500** | Internal error |  -  |

<a id="getServicesByName"></a>
# **getServicesByName**
> List&lt;Service&gt; getServicesByName(servicename)

Get a service configuration and state

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    SystemApi apiInstance = new SystemApi(defaultClient);
    String servicename = "servicename_example"; // String | 
    try {
      List<Service> result = apiInstance.getServicesByName(servicename);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemApi#getServicesByName");
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
| **servicename** | **String**|  | |

### Return type

[**List&lt;Service&gt;**](Service.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Service Info |  -  |
| **500** | Internal Error |  -  |

<a id="getServicesByNameAndHost"></a>
# **getServicesByNameAndHost**
> List&lt;Service&gt; getServicesByNameAndHost(servicename, hostid)

Get service config for a specific host

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    SystemApi apiInstance = new SystemApi(defaultClient);
    String servicename = "servicename_example"; // String | 
    String hostid = "hostid_example"; // String | 
    try {
      List<Service> result = apiInstance.getServicesByNameAndHost(servicename, hostid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemApi#getServicesByNameAndHost");
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
| **servicename** | **String**|  | |
| **hostid** | **String**|  | |

### Return type

[**List&lt;Service&gt;**](Service.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Listing of registered services |  -  |
| **500** | Internal error |  -  |

<a id="getStatus"></a>
# **getStatus**
> StatusResponse getStatus()

Service status

Get the API service status

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    SystemApi apiInstance = new SystemApi(defaultClient);
    try {
      StatusResponse result = apiInstance.getStatus();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemApi#getStatus");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status listing |  -  |
| **500** | Internal error |  -  |

<a id="getSystemFeeds"></a>
# **getSystemFeeds**
> List&lt;FeedMetadata&gt; getSystemFeeds()

list feeds operations and information

Return a list of feed and their groups along with update and record count information. This data reflects the state of the policy engine, not the upstream feed service itself.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    SystemApi apiInstance = new SystemApi(defaultClient);
    try {
      List<FeedMetadata> result = apiInstance.getSystemFeeds();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemApi#getSystemFeeds");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;FeedMetadata&gt;**](FeedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |
| **500** | Internal Error |  -  |

<a id="listServices"></a>
# **listServices**
> List&lt;Service&gt; listServices()

List system services

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    SystemApi apiInstance = new SystemApi(defaultClient);
    try {
      List<Service> result = apiInstance.listServices();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemApi#listServices");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;Service&gt;**](Service.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Service listing |  -  |
| **500** | Internal Error |  -  |

<a id="postSystemFeeds"></a>
# **postSystemFeeds**
> List&lt;FeedSyncResult&gt; postSystemFeeds(flush, sync)

trigger feeds operations

Execute a synchronous feed sync operation. The response will block until complete, then return the result summary.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    SystemApi apiInstance = new SystemApi(defaultClient);
    Boolean flush = true; // Boolean | instruct system to flush existing data feeds records from anchore-engine
    Boolean sync = true; // Boolean | instruct system to re-sync data feeds
    try {
      List<FeedSyncResult> result = apiInstance.postSystemFeeds(flush, sync);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemApi#postSystemFeeds");
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
| **flush** | **Boolean**| instruct system to flush existing data feeds records from anchore-engine | [optional] |
| **sync** | **Boolean**| instruct system to re-sync data feeds | [optional] |

### Return type

[**List&lt;FeedSyncResult&gt;**](FeedSyncResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Feeds operation success |  -  |
| **500** | Internal Error |  -  |

<a id="testWebhook"></a>
# **testWebhook**
> testWebhook(webhookType, notificationType)

Adds the capabilities to test a webhook delivery for the given notification type

Loads the Webhook configuration for webhook_type, and sends the notification out as a test

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    SystemApi apiInstance = new SystemApi(defaultClient);
    String webhookType = "webhookType_example"; // String | The Webhook Type that we should test
    String notificationType = "tag_update"; // String | What kind of Notification to send
    try {
      apiInstance.testWebhook(webhookType, notificationType);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemApi#testWebhook");
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
| **webhookType** | **String**| The Webhook Type that we should test | |
| **notificationType** | **String**| What kind of Notification to send | [optional] [default to tag_update] [enum: tag_update, analysis_update, vuln_update, policy_eval] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Webhook was sent successfully. Schemas may be found under Models (PolicyEvalNotification, TagUpdateNotification, VulnUpdateNotification, AnalysisUpdateNotification) |  -  |
| **400** | The Webhook failed to send due to misconfiguration |  -  |
| **500** | The Webhook failed to send due to an Internal Error |  -  |

<a id="toggleFeedEnabled"></a>
# **toggleFeedEnabled**
> FeedMetadata toggleFeedEnabled(feed, enabled)



Disable the feed so that it does not sync on subsequent sync operations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    SystemApi apiInstance = new SystemApi(defaultClient);
    String feed = "feed_example"; // String | 
    Boolean enabled = true; // Boolean | 
    try {
      FeedMetadata result = apiInstance.toggleFeedEnabled(feed, enabled);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemApi#toggleFeedEnabled");
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
| **feed** | **String**|  | |
| **enabled** | **Boolean**|  | |

### Return type

[**FeedMetadata**](FeedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | FeedInfo |  -  |
| **400** | Bad request, fix and resend |  -  |
| **500** | Internal server error processing the request. Retry expected |  -  |

<a id="toggleGroupEnabled"></a>
# **toggleGroupEnabled**
> List&lt;FeedMetadata&gt; toggleGroupEnabled(feed, group, enabled)



Disable a specific group within a feed to not sync

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    SystemApi apiInstance = new SystemApi(defaultClient);
    String feed = "feed_example"; // String | 
    String group = "group_example"; // String | 
    Boolean enabled = true; // Boolean | 
    try {
      List<FeedMetadata> result = apiInstance.toggleGroupEnabled(feed, group, enabled);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemApi#toggleGroupEnabled");
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
| **feed** | **String**|  | |
| **group** | **String**|  | |
| **enabled** | **Boolean**|  | |

### Return type

[**List&lt;FeedMetadata&gt;**](FeedMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | FeedInfo listing |  -  |
| **400** | Bad request, fix and resend |  -  |
| **500** | Internal server error processing the request. Retry expected |  -  |

