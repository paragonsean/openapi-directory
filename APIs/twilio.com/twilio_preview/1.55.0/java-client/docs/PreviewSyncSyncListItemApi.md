# PreviewSyncSyncListItemApi

All URIs are relative to *https://preview.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSyncSyncListItem**](PreviewSyncSyncListItemApi.md#createSyncSyncListItem) | **POST** /Sync/Services/{ServiceSid}/Lists/{ListSid}/Items |  |
| [**deleteSyncSyncListItem**](PreviewSyncSyncListItemApi.md#deleteSyncSyncListItem) | **DELETE** /Sync/Services/{ServiceSid}/Lists/{ListSid}/Items/{Index} |  |
| [**fetchSyncSyncListItem**](PreviewSyncSyncListItemApi.md#fetchSyncSyncListItem) | **GET** /Sync/Services/{ServiceSid}/Lists/{ListSid}/Items/{Index} |  |
| [**listSyncSyncListItem**](PreviewSyncSyncListItemApi.md#listSyncSyncListItem) | **GET** /Sync/Services/{ServiceSid}/Lists/{ListSid}/Items |  |
| [**updateSyncSyncListItem**](PreviewSyncSyncListItemApi.md#updateSyncSyncListItem) | **POST** /Sync/Services/{ServiceSid}/Lists/{ListSid}/Items/{Index} |  |


<a id="createSyncSyncListItem"></a>
# **createSyncSyncListItem**
> PreviewSyncServiceSyncListSyncListItem createSyncSyncListItem(serviceSid, listSid, data)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewSyncSyncListItemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewSyncSyncListItemApi apiInstance = new PreviewSyncSyncListItemApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String listSid = "listSid_example"; // String | 
    Object data = null; // Object | 
    try {
      PreviewSyncServiceSyncListSyncListItem result = apiInstance.createSyncSyncListItem(serviceSid, listSid, data);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewSyncSyncListItemApi#createSyncSyncListItem");
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
| **listSid** | **String**|  | |
| **data** | [**Object**](Object.md)|  | |

### Return type

[**PreviewSyncServiceSyncListSyncListItem**](PreviewSyncServiceSyncListSyncListItem.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteSyncSyncListItem"></a>
# **deleteSyncSyncListItem**
> deleteSyncSyncListItem(serviceSid, listSid, index, ifMatch)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewSyncSyncListItemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewSyncSyncListItemApi apiInstance = new PreviewSyncSyncListItemApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String listSid = "listSid_example"; // String | 
    Integer index = 56; // Integer | 
    String ifMatch = "ifMatch_example"; // String | The If-Match HTTP request header
    try {
      apiInstance.deleteSyncSyncListItem(serviceSid, listSid, index, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewSyncSyncListItemApi#deleteSyncSyncListItem");
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
| **listSid** | **String**|  | |
| **index** | **Integer**|  | |
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

<a id="fetchSyncSyncListItem"></a>
# **fetchSyncSyncListItem**
> PreviewSyncServiceSyncListSyncListItem fetchSyncSyncListItem(serviceSid, listSid, index)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewSyncSyncListItemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewSyncSyncListItemApi apiInstance = new PreviewSyncSyncListItemApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String listSid = "listSid_example"; // String | 
    Integer index = 56; // Integer | 
    try {
      PreviewSyncServiceSyncListSyncListItem result = apiInstance.fetchSyncSyncListItem(serviceSid, listSid, index);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewSyncSyncListItemApi#fetchSyncSyncListItem");
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
| **listSid** | **String**|  | |
| **index** | **Integer**|  | |

### Return type

[**PreviewSyncServiceSyncListSyncListItem**](PreviewSyncServiceSyncListSyncListItem.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listSyncSyncListItem"></a>
# **listSyncSyncListItem**
> ListSyncSyncListItemResponse listSyncSyncListItem(serviceSid, listSid, order, from, bounds, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewSyncSyncListItemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewSyncSyncListItemApi apiInstance = new PreviewSyncSyncListItemApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String listSid = "listSid_example"; // String | 
    SyncListItemEnumQueryResultOrder order = SyncListItemEnumQueryResultOrder.fromValue("asc"); // SyncListItemEnumQueryResultOrder | 
    String from = "from_example"; // String | 
    SyncListItemEnumQueryFromBoundType bounds = SyncListItemEnumQueryFromBoundType.fromValue("inclusive"); // SyncListItemEnumQueryFromBoundType | 
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListSyncSyncListItemResponse result = apiInstance.listSyncSyncListItem(serviceSid, listSid, order, from, bounds, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewSyncSyncListItemApi#listSyncSyncListItem");
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
| **listSid** | **String**|  | |
| **order** | **SyncListItemEnumQueryResultOrder**|  | [optional] [enum: asc, desc] |
| **from** | **String**|  | [optional] |
| **bounds** | **SyncListItemEnumQueryFromBoundType**|  | [optional] [enum: inclusive, exclusive] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListSyncSyncListItemResponse**](ListSyncSyncListItemResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateSyncSyncListItem"></a>
# **updateSyncSyncListItem**
> PreviewSyncServiceSyncListSyncListItem updateSyncSyncListItem(serviceSid, listSid, index, data, ifMatch)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewSyncSyncListItemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewSyncSyncListItemApi apiInstance = new PreviewSyncSyncListItemApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String listSid = "listSid_example"; // String | 
    Integer index = 56; // Integer | 
    Object data = null; // Object | 
    String ifMatch = "ifMatch_example"; // String | The If-Match HTTP request header
    try {
      PreviewSyncServiceSyncListSyncListItem result = apiInstance.updateSyncSyncListItem(serviceSid, listSid, index, data, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewSyncSyncListItemApi#updateSyncSyncListItem");
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
| **listSid** | **String**|  | |
| **index** | **Integer**|  | |
| **data** | [**Object**](Object.md)|  | |
| **ifMatch** | **String**| The If-Match HTTP request header | [optional] |

### Return type

[**PreviewSyncServiceSyncListSyncListItem**](PreviewSyncServiceSyncListSyncListItem.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

