# PreviewSyncSyncMapItemApi

All URIs are relative to *https://preview.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSyncSyncMapItem**](PreviewSyncSyncMapItemApi.md#createSyncSyncMapItem) | **POST** /Sync/Services/{ServiceSid}/Maps/{MapSid}/Items |  |
| [**deleteSyncSyncMapItem**](PreviewSyncSyncMapItemApi.md#deleteSyncSyncMapItem) | **DELETE** /Sync/Services/{ServiceSid}/Maps/{MapSid}/Items/{Key} |  |
| [**fetchSyncSyncMapItem**](PreviewSyncSyncMapItemApi.md#fetchSyncSyncMapItem) | **GET** /Sync/Services/{ServiceSid}/Maps/{MapSid}/Items/{Key} |  |
| [**listSyncSyncMapItem**](PreviewSyncSyncMapItemApi.md#listSyncSyncMapItem) | **GET** /Sync/Services/{ServiceSid}/Maps/{MapSid}/Items |  |
| [**updateSyncSyncMapItem**](PreviewSyncSyncMapItemApi.md#updateSyncSyncMapItem) | **POST** /Sync/Services/{ServiceSid}/Maps/{MapSid}/Items/{Key} |  |


<a id="createSyncSyncMapItem"></a>
# **createSyncSyncMapItem**
> PreviewSyncServiceSyncMapSyncMapItem createSyncSyncMapItem(serviceSid, mapSid, data, key)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewSyncSyncMapItemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewSyncSyncMapItemApi apiInstance = new PreviewSyncSyncMapItemApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String mapSid = "mapSid_example"; // String | 
    Object data = null; // Object | 
    String key = "key_example"; // String | 
    try {
      PreviewSyncServiceSyncMapSyncMapItem result = apiInstance.createSyncSyncMapItem(serviceSid, mapSid, data, key);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewSyncSyncMapItemApi#createSyncSyncMapItem");
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
| **serviceSid** | **String**|  | |
| **mapSid** | **String**|  | |
| **data** | [**Object**](Object.md)|  | |
| **key** | **String**|  | |

### Return type

[**PreviewSyncServiceSyncMapSyncMapItem**](PreviewSyncServiceSyncMapSyncMapItem.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteSyncSyncMapItem"></a>
# **deleteSyncSyncMapItem**
> deleteSyncSyncMapItem(serviceSid, mapSid, key, ifMatch)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewSyncSyncMapItemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewSyncSyncMapItemApi apiInstance = new PreviewSyncSyncMapItemApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String mapSid = "mapSid_example"; // String | 
    String key = "key_example"; // String | 
    String ifMatch = "ifMatch_example"; // String | The If-Match HTTP request header
    try {
      apiInstance.deleteSyncSyncMapItem(serviceSid, mapSid, key, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewSyncSyncMapItemApi#deleteSyncSyncMapItem");
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
| **serviceSid** | **String**|  | |
| **mapSid** | **String**|  | |
| **key** | **String**|  | |
| **ifMatch** | **String**| The If-Match HTTP request header | [optional] |

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

<a id="fetchSyncSyncMapItem"></a>
# **fetchSyncSyncMapItem**
> PreviewSyncServiceSyncMapSyncMapItem fetchSyncSyncMapItem(serviceSid, mapSid, key)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewSyncSyncMapItemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewSyncSyncMapItemApi apiInstance = new PreviewSyncSyncMapItemApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String mapSid = "mapSid_example"; // String | 
    String key = "key_example"; // String | 
    try {
      PreviewSyncServiceSyncMapSyncMapItem result = apiInstance.fetchSyncSyncMapItem(serviceSid, mapSid, key);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewSyncSyncMapItemApi#fetchSyncSyncMapItem");
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
| **serviceSid** | **String**|  | |
| **mapSid** | **String**|  | |
| **key** | **String**|  | |

### Return type

[**PreviewSyncServiceSyncMapSyncMapItem**](PreviewSyncServiceSyncMapSyncMapItem.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listSyncSyncMapItem"></a>
# **listSyncSyncMapItem**
> ListSyncSyncMapItemResponse listSyncSyncMapItem(serviceSid, mapSid, order, from, bounds, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewSyncSyncMapItemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewSyncSyncMapItemApi apiInstance = new PreviewSyncSyncMapItemApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String mapSid = "mapSid_example"; // String | 
    SyncMapItemEnumQueryResultOrder order = SyncMapItemEnumQueryResultOrder.fromValue("asc"); // SyncMapItemEnumQueryResultOrder | 
    String from = "from_example"; // String | 
    SyncMapItemEnumQueryFromBoundType bounds = SyncMapItemEnumQueryFromBoundType.fromValue("inclusive"); // SyncMapItemEnumQueryFromBoundType | 
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListSyncSyncMapItemResponse result = apiInstance.listSyncSyncMapItem(serviceSid, mapSid, order, from, bounds, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewSyncSyncMapItemApi#listSyncSyncMapItem");
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
| **serviceSid** | **String**|  | |
| **mapSid** | **String**|  | |
| **order** | **SyncMapItemEnumQueryResultOrder**|  | [optional] [enum: asc, desc] |
| **from** | **String**|  | [optional] |
| **bounds** | **SyncMapItemEnumQueryFromBoundType**|  | [optional] [enum: inclusive, exclusive] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListSyncSyncMapItemResponse**](ListSyncSyncMapItemResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateSyncSyncMapItem"></a>
# **updateSyncSyncMapItem**
> PreviewSyncServiceSyncMapSyncMapItem updateSyncSyncMapItem(serviceSid, mapSid, key, data, ifMatch)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewSyncSyncMapItemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewSyncSyncMapItemApi apiInstance = new PreviewSyncSyncMapItemApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String mapSid = "mapSid_example"; // String | 
    String key = "key_example"; // String | 
    Object data = null; // Object | 
    String ifMatch = "ifMatch_example"; // String | The If-Match HTTP request header
    try {
      PreviewSyncServiceSyncMapSyncMapItem result = apiInstance.updateSyncSyncMapItem(serviceSid, mapSid, key, data, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewSyncSyncMapItemApi#updateSyncSyncMapItem");
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
| **serviceSid** | **String**|  | |
| **mapSid** | **String**|  | |
| **key** | **String**|  | |
| **data** | [**Object**](Object.md)|  | |
| **ifMatch** | **String**| The If-Match HTTP request header | [optional] |

### Return type

[**PreviewSyncServiceSyncMapSyncMapItem**](PreviewSyncServiceSyncMapSyncMapItem.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

