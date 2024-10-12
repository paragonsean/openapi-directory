# SyncV1SyncMapApi

All URIs are relative to *https://sync.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSyncMap**](SyncV1SyncMapApi.md#createSyncMap) | **POST** /v1/Services/{ServiceSid}/Maps |  |
| [**deleteSyncMap**](SyncV1SyncMapApi.md#deleteSyncMap) | **DELETE** /v1/Services/{ServiceSid}/Maps/{Sid} |  |
| [**fetchSyncMap**](SyncV1SyncMapApi.md#fetchSyncMap) | **GET** /v1/Services/{ServiceSid}/Maps/{Sid} |  |
| [**listSyncMap**](SyncV1SyncMapApi.md#listSyncMap) | **GET** /v1/Services/{ServiceSid}/Maps |  |
| [**updateSyncMap**](SyncV1SyncMapApi.md#updateSyncMap) | **POST** /v1/Services/{ServiceSid}/Maps/{Sid} |  |


<a id="createSyncMap"></a>
# **createSyncMap**
> SyncV1ServiceSyncMap createSyncMap(serviceSid, collectionTtl, ttl, uniqueName)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncV1SyncMapApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sync.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SyncV1SyncMapApi apiInstance = new SyncV1SyncMapApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) to create the Sync Map in.
    Integer collectionTtl = 56; // Integer | How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Sync Map expires (time-to-live) and is deleted.
    Integer ttl = 56; // Integer | An alias for `collection_ttl`. If both parameters are provided, this value is ignored.
    String uniqueName = "uniqueName_example"; // String | An application-defined string that uniquely identifies the resource. It can be used as an alternative to the `sid` in the URL path to address the resource.
    try {
      SyncV1ServiceSyncMap result = apiInstance.createSyncMap(serviceSid, collectionTtl, ttl, uniqueName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncV1SyncMapApi#createSyncMap");
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
| **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) to create the Sync Map in. | |
| **collectionTtl** | **Integer**| How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Sync Map expires (time-to-live) and is deleted. | [optional] |
| **ttl** | **Integer**| An alias for &#x60;collection_ttl&#x60;. If both parameters are provided, this value is ignored. | [optional] |
| **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. It can be used as an alternative to the &#x60;sid&#x60; in the URL path to address the resource. | [optional] |

### Return type

[**SyncV1ServiceSyncMap**](SyncV1ServiceSyncMap.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteSyncMap"></a>
# **deleteSyncMap**
> deleteSyncMap(serviceSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncV1SyncMapApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sync.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SyncV1SyncMapApi apiInstance = new SyncV1SyncMapApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map resource to delete.
    String sid = "sid_example"; // String | The SID of the Sync Map resource to delete. Can be the Sync Map's `sid` or its `unique_name`.
    try {
      apiInstance.deleteSyncMap(serviceSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncV1SyncMapApi#deleteSyncMap");
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
| **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map resource to delete. | |
| **sid** | **String**| The SID of the Sync Map resource to delete. Can be the Sync Map&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | |

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

<a id="fetchSyncMap"></a>
# **fetchSyncMap**
> SyncV1ServiceSyncMap fetchSyncMap(serviceSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncV1SyncMapApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sync.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SyncV1SyncMapApi apiInstance = new SyncV1SyncMapApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map resource to fetch.
    String sid = "sid_example"; // String | The SID of the Sync Map resource to fetch. Can be the Sync Map's `sid` or its `unique_name`.
    try {
      SyncV1ServiceSyncMap result = apiInstance.fetchSyncMap(serviceSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncV1SyncMapApi#fetchSyncMap");
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
| **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map resource to fetch. | |
| **sid** | **String**| The SID of the Sync Map resource to fetch. Can be the Sync Map&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | |

### Return type

[**SyncV1ServiceSyncMap**](SyncV1ServiceSyncMap.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listSyncMap"></a>
# **listSyncMap**
> ListSyncMapResponse listSyncMap(serviceSid, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncV1SyncMapApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sync.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SyncV1SyncMapApi apiInstance = new SyncV1SyncMapApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map resources to read.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListSyncMapResponse result = apiInstance.listSyncMap(serviceSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncV1SyncMapApi#listSyncMap");
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
| **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map resources to read. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListSyncMapResponse**](ListSyncMapResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateSyncMap"></a>
# **updateSyncMap**
> SyncV1ServiceSyncMap updateSyncMap(serviceSid, sid, collectionTtl, ttl)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncV1SyncMapApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sync.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SyncV1SyncMapApi apiInstance = new SyncV1SyncMapApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map resource to update.
    String sid = "sid_example"; // String | The SID of the Sync Map resource to update. Can be the Sync Map's `sid` or its `unique_name`.
    Integer collectionTtl = 56; // Integer | How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Sync Map expires (time-to-live) and is deleted.
    Integer ttl = 56; // Integer | An alias for `collection_ttl`. If both parameters are provided, this value is ignored.
    try {
      SyncV1ServiceSyncMap result = apiInstance.updateSyncMap(serviceSid, sid, collectionTtl, ttl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncV1SyncMapApi#updateSyncMap");
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
| **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map resource to update. | |
| **sid** | **String**| The SID of the Sync Map resource to update. Can be the Sync Map&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | |
| **collectionTtl** | **Integer**| How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Sync Map expires (time-to-live) and is deleted. | [optional] |
| **ttl** | **Integer**| An alias for &#x60;collection_ttl&#x60;. If both parameters are provided, this value is ignored. | [optional] |

### Return type

[**SyncV1ServiceSyncMap**](SyncV1ServiceSyncMap.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

