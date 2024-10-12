# SyncV1SyncListItemApi

All URIs are relative to *https://sync.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSyncListItem**](SyncV1SyncListItemApi.md#createSyncListItem) | **POST** /v1/Services/{ServiceSid}/Lists/{ListSid}/Items |  |
| [**deleteSyncListItem**](SyncV1SyncListItemApi.md#deleteSyncListItem) | **DELETE** /v1/Services/{ServiceSid}/Lists/{ListSid}/Items/{Index} |  |
| [**fetchSyncListItem**](SyncV1SyncListItemApi.md#fetchSyncListItem) | **GET** /v1/Services/{ServiceSid}/Lists/{ListSid}/Items/{Index} |  |
| [**listSyncListItem**](SyncV1SyncListItemApi.md#listSyncListItem) | **GET** /v1/Services/{ServiceSid}/Lists/{ListSid}/Items |  |
| [**updateSyncListItem**](SyncV1SyncListItemApi.md#updateSyncListItem) | **POST** /v1/Services/{ServiceSid}/Lists/{ListSid}/Items/{Index} |  |


<a id="createSyncListItem"></a>
# **createSyncListItem**
> SyncV1ServiceSyncListSyncListItem createSyncListItem(serviceSid, listSid, data, collectionTtl, itemTtl, ttl)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncV1SyncListItemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sync.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SyncV1SyncListItemApi apiInstance = new SyncV1SyncListItemApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) to create the new List Item in.
    String listSid = "listSid_example"; // String | The SID of the Sync List to add the new List Item to. Can be the Sync List resource's `sid` or its `unique_name`.
    Object data = null; // Object | A JSON string that represents an arbitrary, schema-less object that the List Item stores. Can be up to 16 KiB in length.
    Integer collectionTtl = 56; // Integer | How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the List Item's parent Sync List expires (time-to-live) and is deleted.
    Integer itemTtl = 56; // Integer | How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the List Item expires (time-to-live) and is deleted.
    Integer ttl = 56; // Integer | An alias for `item_ttl`. If both parameters are provided, this value is ignored.
    try {
      SyncV1ServiceSyncListSyncListItem result = apiInstance.createSyncListItem(serviceSid, listSid, data, collectionTtl, itemTtl, ttl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncV1SyncListItemApi#createSyncListItem");
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
| **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) to create the new List Item in. | |
| **listSid** | **String**| The SID of the Sync List to add the new List Item to. Can be the Sync List resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | |
| **data** | [**Object**](Object.md)| A JSON string that represents an arbitrary, schema-less object that the List Item stores. Can be up to 16 KiB in length. | |
| **collectionTtl** | **Integer**| How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the List Item&#39;s parent Sync List expires (time-to-live) and is deleted. | [optional] |
| **itemTtl** | **Integer**| How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the List Item expires (time-to-live) and is deleted. | [optional] |
| **ttl** | **Integer**| An alias for &#x60;item_ttl&#x60;. If both parameters are provided, this value is ignored. | [optional] |

### Return type

[**SyncV1ServiceSyncListSyncListItem**](SyncV1ServiceSyncListSyncListItem.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteSyncListItem"></a>
# **deleteSyncListItem**
> deleteSyncListItem(serviceSid, listSid, index, ifMatch)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncV1SyncListItemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sync.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SyncV1SyncListItemApi apiInstance = new SyncV1SyncListItemApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync List Item resource to delete.
    String listSid = "listSid_example"; // String | The SID of the Sync List with the Sync List Item resource to delete. Can be the Sync List resource's `sid` or its `unique_name`.
    Integer index = 56; // Integer | The index of the Sync List Item resource to delete.
    String ifMatch = "ifMatch_example"; // String | If provided, applies this mutation if (and only if) the “revision” field of this [map item] matches the provided value. This matches the semantics of (and is implemented with) the HTTP [If-Match header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match).
    try {
      apiInstance.deleteSyncListItem(serviceSid, listSid, index, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncV1SyncListItemApi#deleteSyncListItem");
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
| **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync List Item resource to delete. | |
| **listSid** | **String**| The SID of the Sync List with the Sync List Item resource to delete. Can be the Sync List resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | |
| **index** | **Integer**| The index of the Sync List Item resource to delete. | |
| **ifMatch** | **String**| If provided, applies this mutation if (and only if) the “revision” field of this [map item] matches the provided value. This matches the semantics of (and is implemented with) the HTTP [If-Match header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match). | [optional] |

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

<a id="fetchSyncListItem"></a>
# **fetchSyncListItem**
> SyncV1ServiceSyncListSyncListItem fetchSyncListItem(serviceSid, listSid, index)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncV1SyncListItemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sync.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SyncV1SyncListItemApi apiInstance = new SyncV1SyncListItemApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync List Item resource to fetch.
    String listSid = "listSid_example"; // String | The SID of the Sync List with the Sync List Item resource to fetch. Can be the Sync List resource's `sid` or its `unique_name`.
    Integer index = 56; // Integer | The index of the Sync List Item resource to fetch.
    try {
      SyncV1ServiceSyncListSyncListItem result = apiInstance.fetchSyncListItem(serviceSid, listSid, index);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncV1SyncListItemApi#fetchSyncListItem");
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
| **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync List Item resource to fetch. | |
| **listSid** | **String**| The SID of the Sync List with the Sync List Item resource to fetch. Can be the Sync List resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | |
| **index** | **Integer**| The index of the Sync List Item resource to fetch. | |

### Return type

[**SyncV1ServiceSyncListSyncListItem**](SyncV1ServiceSyncListSyncListItem.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listSyncListItem"></a>
# **listSyncListItem**
> ListSyncListItemResponse listSyncListItem(serviceSid, listSid, order, from, bounds, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncV1SyncListItemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sync.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SyncV1SyncListItemApi apiInstance = new SyncV1SyncListItemApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the List Item resources to read.
    String listSid = "listSid_example"; // String | The SID of the Sync List with the List Items to read. Can be the Sync List resource's `sid` or its `unique_name`.
    SyncListItemEnumQueryResultOrder order = SyncListItemEnumQueryResultOrder.fromValue("asc"); // SyncListItemEnumQueryResultOrder | How to order the List Items returned by their `index` value. Can be: `asc` (ascending) or `desc` (descending) and the default is ascending.
    String from = "from_example"; // String | The `index` of the first Sync List Item resource to read. See also `bounds`.
    SyncListItemEnumQueryFromBoundType bounds = SyncListItemEnumQueryFromBoundType.fromValue("inclusive"); // SyncListItemEnumQueryFromBoundType | Whether to include the List Item referenced by the `from` parameter. Can be: `inclusive` to include the List Item referenced by the `from` parameter or `exclusive` to start with the next List Item. The default value is `inclusive`.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListSyncListItemResponse result = apiInstance.listSyncListItem(serviceSid, listSid, order, from, bounds, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncV1SyncListItemApi#listSyncListItem");
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
| **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the List Item resources to read. | |
| **listSid** | **String**| The SID of the Sync List with the List Items to read. Can be the Sync List resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | |
| **order** | **SyncListItemEnumQueryResultOrder**| How to order the List Items returned by their &#x60;index&#x60; value. Can be: &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending) and the default is ascending. | [optional] [enum: asc, desc] |
| **from** | **String**| The &#x60;index&#x60; of the first Sync List Item resource to read. See also &#x60;bounds&#x60;. | [optional] |
| **bounds** | **SyncListItemEnumQueryFromBoundType**| Whether to include the List Item referenced by the &#x60;from&#x60; parameter. Can be: &#x60;inclusive&#x60; to include the List Item referenced by the &#x60;from&#x60; parameter or &#x60;exclusive&#x60; to start with the next List Item. The default value is &#x60;inclusive&#x60;. | [optional] [enum: inclusive, exclusive] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListSyncListItemResponse**](ListSyncListItemResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateSyncListItem"></a>
# **updateSyncListItem**
> SyncV1ServiceSyncListSyncListItem updateSyncListItem(serviceSid, listSid, index, ifMatch, collectionTtl, data, itemTtl, ttl)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncV1SyncListItemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sync.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SyncV1SyncListItemApi apiInstance = new SyncV1SyncListItemApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync List Item resource to update.
    String listSid = "listSid_example"; // String | The SID of the Sync List with the Sync List Item resource to update. Can be the Sync List resource's `sid` or its `unique_name`.
    Integer index = 56; // Integer | The index of the Sync List Item resource to update.
    String ifMatch = "ifMatch_example"; // String | If provided, applies this mutation if (and only if) the “revision” field of this [map item] matches the provided value. This matches the semantics of (and is implemented with) the HTTP [If-Match header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match).
    Integer collectionTtl = 56; // Integer | How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the List Item's parent Sync List expires (time-to-live) and is deleted. This parameter can only be used when the List Item's `data` or `ttl` is updated in the same request.
    Object data = null; // Object | A JSON string that represents an arbitrary, schema-less object that the List Item stores. Can be up to 16 KiB in length.
    Integer itemTtl = 56; // Integer | How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the List Item expires (time-to-live) and is deleted.
    Integer ttl = 56; // Integer | An alias for `item_ttl`. If both parameters are provided, this value is ignored.
    try {
      SyncV1ServiceSyncListSyncListItem result = apiInstance.updateSyncListItem(serviceSid, listSid, index, ifMatch, collectionTtl, data, itemTtl, ttl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncV1SyncListItemApi#updateSyncListItem");
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
| **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync List Item resource to update. | |
| **listSid** | **String**| The SID of the Sync List with the Sync List Item resource to update. Can be the Sync List resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | |
| **index** | **Integer**| The index of the Sync List Item resource to update. | |
| **ifMatch** | **String**| If provided, applies this mutation if (and only if) the “revision” field of this [map item] matches the provided value. This matches the semantics of (and is implemented with) the HTTP [If-Match header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match). | [optional] |
| **collectionTtl** | **Integer**| How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the List Item&#39;s parent Sync List expires (time-to-live) and is deleted. This parameter can only be used when the List Item&#39;s &#x60;data&#x60; or &#x60;ttl&#x60; is updated in the same request. | [optional] |
| **data** | [**Object**](Object.md)| A JSON string that represents an arbitrary, schema-less object that the List Item stores. Can be up to 16 KiB in length. | [optional] |
| **itemTtl** | **Integer**| How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the List Item expires (time-to-live) and is deleted. | [optional] |
| **ttl** | **Integer**| An alias for &#x60;item_ttl&#x60;. If both parameters are provided, this value is ignored. | [optional] |

### Return type

[**SyncV1ServiceSyncListSyncListItem**](SyncV1ServiceSyncListSyncListItem.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

