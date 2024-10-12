# SyncV1SyncMapItemApi

All URIs are relative to *https://sync.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSyncMapItem**](SyncV1SyncMapItemApi.md#createSyncMapItem) | **POST** /v1/Services/{ServiceSid}/Maps/{MapSid}/Items |  |
| [**deleteSyncMapItem**](SyncV1SyncMapItemApi.md#deleteSyncMapItem) | **DELETE** /v1/Services/{ServiceSid}/Maps/{MapSid}/Items/{Key} |  |
| [**fetchSyncMapItem**](SyncV1SyncMapItemApi.md#fetchSyncMapItem) | **GET** /v1/Services/{ServiceSid}/Maps/{MapSid}/Items/{Key} |  |
| [**listSyncMapItem**](SyncV1SyncMapItemApi.md#listSyncMapItem) | **GET** /v1/Services/{ServiceSid}/Maps/{MapSid}/Items |  |
| [**updateSyncMapItem**](SyncV1SyncMapItemApi.md#updateSyncMapItem) | **POST** /v1/Services/{ServiceSid}/Maps/{MapSid}/Items/{Key} |  |


<a id="createSyncMapItem"></a>
# **createSyncMapItem**
> SyncV1ServiceSyncMapSyncMapItem createSyncMapItem(serviceSid, mapSid, data, key, collectionTtl, itemTtl, ttl)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncV1SyncMapItemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sync.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SyncV1SyncMapItemApi apiInstance = new SyncV1SyncMapItemApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) to create the Map Item in.
    String mapSid = "mapSid_example"; // String | The SID of the Sync Map to add the new Map Item to. Can be the Sync Map resource's `sid` or its `unique_name`.
    Object data = null; // Object | A JSON string that represents an arbitrary, schema-less object that the Map Item stores. Can be up to 16 KiB in length.
    String key = "key_example"; // String | The unique, user-defined key for the Map Item. Can be up to 320 characters long.
    Integer collectionTtl = 56; // Integer | How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Map Item's parent Sync Map expires (time-to-live) and is deleted.
    Integer itemTtl = 56; // Integer | How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Map Item expires (time-to-live) and is deleted.
    Integer ttl = 56; // Integer | An alias for `item_ttl`. If both parameters are provided, this value is ignored.
    try {
      SyncV1ServiceSyncMapSyncMapItem result = apiInstance.createSyncMapItem(serviceSid, mapSid, data, key, collectionTtl, itemTtl, ttl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncV1SyncMapItemApi#createSyncMapItem");
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
| **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) to create the Map Item in. | |
| **mapSid** | **String**| The SID of the Sync Map to add the new Map Item to. Can be the Sync Map resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | |
| **data** | [**Object**](Object.md)| A JSON string that represents an arbitrary, schema-less object that the Map Item stores. Can be up to 16 KiB in length. | |
| **key** | **String**| The unique, user-defined key for the Map Item. Can be up to 320 characters long. | |
| **collectionTtl** | **Integer**| How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Map Item&#39;s parent Sync Map expires (time-to-live) and is deleted. | [optional] |
| **itemTtl** | **Integer**| How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Map Item expires (time-to-live) and is deleted. | [optional] |
| **ttl** | **Integer**| An alias for &#x60;item_ttl&#x60;. If both parameters are provided, this value is ignored. | [optional] |

### Return type

[**SyncV1ServiceSyncMapSyncMapItem**](SyncV1ServiceSyncMapSyncMapItem.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteSyncMapItem"></a>
# **deleteSyncMapItem**
> deleteSyncMapItem(serviceSid, mapSid, key, ifMatch)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncV1SyncMapItemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sync.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SyncV1SyncMapItemApi apiInstance = new SyncV1SyncMapItemApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map Item resource to delete.
    String mapSid = "mapSid_example"; // String | The SID of the Sync Map with the Sync Map Item resource to delete. Can be the Sync Map resource's `sid` or its `unique_name`.
    String key = "key_example"; // String | The `key` value of the Sync Map Item resource to delete.
    String ifMatch = "ifMatch_example"; // String | If provided, applies this mutation if (and only if) the “revision” field of this [map item] matches the provided value. This matches the semantics of (and is implemented with) the HTTP [If-Match header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match).
    try {
      apiInstance.deleteSyncMapItem(serviceSid, mapSid, key, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncV1SyncMapItemApi#deleteSyncMapItem");
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
| **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map Item resource to delete. | |
| **mapSid** | **String**| The SID of the Sync Map with the Sync Map Item resource to delete. Can be the Sync Map resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | |
| **key** | **String**| The &#x60;key&#x60; value of the Sync Map Item resource to delete. | |
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

<a id="fetchSyncMapItem"></a>
# **fetchSyncMapItem**
> SyncV1ServiceSyncMapSyncMapItem fetchSyncMapItem(serviceSid, mapSid, key)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncV1SyncMapItemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sync.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SyncV1SyncMapItemApi apiInstance = new SyncV1SyncMapItemApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map Item resource to fetch.
    String mapSid = "mapSid_example"; // String | The SID of the Sync Map with the Sync Map Item resource to fetch. Can be the Sync Map resource's `sid` or its `unique_name`.
    String key = "key_example"; // String | The `key` value of the Sync Map Item resource to fetch.
    try {
      SyncV1ServiceSyncMapSyncMapItem result = apiInstance.fetchSyncMapItem(serviceSid, mapSid, key);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncV1SyncMapItemApi#fetchSyncMapItem");
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
| **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map Item resource to fetch. | |
| **mapSid** | **String**| The SID of the Sync Map with the Sync Map Item resource to fetch. Can be the Sync Map resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | |
| **key** | **String**| The &#x60;key&#x60; value of the Sync Map Item resource to fetch. | |

### Return type

[**SyncV1ServiceSyncMapSyncMapItem**](SyncV1ServiceSyncMapSyncMapItem.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listSyncMapItem"></a>
# **listSyncMapItem**
> ListSyncMapItemResponse listSyncMapItem(serviceSid, mapSid, order, from, bounds, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncV1SyncMapItemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sync.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SyncV1SyncMapItemApi apiInstance = new SyncV1SyncMapItemApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Map Item resources to read.
    String mapSid = "mapSid_example"; // String | The SID of the Sync Map with the Sync Map Item resource to fetch. Can be the Sync Map resource's `sid` or its `unique_name`.
    SyncMapItemEnumQueryResultOrder order = SyncMapItemEnumQueryResultOrder.fromValue("asc"); // SyncMapItemEnumQueryResultOrder | How to order the Map Items returned by their `key` value. Can be: `asc` (ascending) or `desc` (descending) and the default is ascending. Map Items are [ordered lexicographically](https://en.wikipedia.org/wiki/Lexicographical_order) by Item key.
    String from = "from_example"; // String | The `key` of the first Sync Map Item resource to read. See also `bounds`.
    SyncMapItemEnumQueryFromBoundType bounds = SyncMapItemEnumQueryFromBoundType.fromValue("inclusive"); // SyncMapItemEnumQueryFromBoundType | Whether to include the Map Item referenced by the `from` parameter. Can be: `inclusive` to include the Map Item referenced by the `from` parameter or `exclusive` to start with the next Map Item. The default value is `inclusive`.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListSyncMapItemResponse result = apiInstance.listSyncMapItem(serviceSid, mapSid, order, from, bounds, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncV1SyncMapItemApi#listSyncMapItem");
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
| **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Map Item resources to read. | |
| **mapSid** | **String**| The SID of the Sync Map with the Sync Map Item resource to fetch. Can be the Sync Map resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | |
| **order** | **SyncMapItemEnumQueryResultOrder**| How to order the Map Items returned by their &#x60;key&#x60; value. Can be: &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending) and the default is ascending. Map Items are [ordered lexicographically](https://en.wikipedia.org/wiki/Lexicographical_order) by Item key. | [optional] [enum: asc, desc] |
| **from** | **String**| The &#x60;key&#x60; of the first Sync Map Item resource to read. See also &#x60;bounds&#x60;. | [optional] |
| **bounds** | **SyncMapItemEnumQueryFromBoundType**| Whether to include the Map Item referenced by the &#x60;from&#x60; parameter. Can be: &#x60;inclusive&#x60; to include the Map Item referenced by the &#x60;from&#x60; parameter or &#x60;exclusive&#x60; to start with the next Map Item. The default value is &#x60;inclusive&#x60;. | [optional] [enum: inclusive, exclusive] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListSyncMapItemResponse**](ListSyncMapItemResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateSyncMapItem"></a>
# **updateSyncMapItem**
> SyncV1ServiceSyncMapSyncMapItem updateSyncMapItem(serviceSid, mapSid, key, ifMatch, collectionTtl, data, itemTtl, ttl)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncV1SyncMapItemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sync.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SyncV1SyncMapItemApi apiInstance = new SyncV1SyncMapItemApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map Item resource to update.
    String mapSid = "mapSid_example"; // String | The SID of the Sync Map with the Sync Map Item resource to update. Can be the Sync Map resource's `sid` or its `unique_name`.
    String key = "key_example"; // String | The `key` value of the Sync Map Item resource to update. 
    String ifMatch = "ifMatch_example"; // String | If provided, applies this mutation if (and only if) the “revision” field of this [map item] matches the provided value. This matches the semantics of (and is implemented with) the HTTP [If-Match header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match).
    Integer collectionTtl = 56; // Integer | How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Map Item's parent Sync Map expires (time-to-live) and is deleted. This parameter can only be used when the Map Item's `data` or `ttl` is updated in the same request.
    Object data = null; // Object | A JSON string that represents an arbitrary, schema-less object that the Map Item stores. Can be up to 16 KiB in length.
    Integer itemTtl = 56; // Integer | How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Map Item expires (time-to-live) and is deleted.
    Integer ttl = 56; // Integer | An alias for `item_ttl`. If both parameters are provided, this value is ignored.
    try {
      SyncV1ServiceSyncMapSyncMapItem result = apiInstance.updateSyncMapItem(serviceSid, mapSid, key, ifMatch, collectionTtl, data, itemTtl, ttl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncV1SyncMapItemApi#updateSyncMapItem");
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
| **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map Item resource to update. | |
| **mapSid** | **String**| The SID of the Sync Map with the Sync Map Item resource to update. Can be the Sync Map resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | |
| **key** | **String**| The &#x60;key&#x60; value of the Sync Map Item resource to update.  | |
| **ifMatch** | **String**| If provided, applies this mutation if (and only if) the “revision” field of this [map item] matches the provided value. This matches the semantics of (and is implemented with) the HTTP [If-Match header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match). | [optional] |
| **collectionTtl** | **Integer**| How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Map Item&#39;s parent Sync Map expires (time-to-live) and is deleted. This parameter can only be used when the Map Item&#39;s &#x60;data&#x60; or &#x60;ttl&#x60; is updated in the same request. | [optional] |
| **data** | [**Object**](Object.md)| A JSON string that represents an arbitrary, schema-less object that the Map Item stores. Can be up to 16 KiB in length. | [optional] |
| **itemTtl** | **Integer**| How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Map Item expires (time-to-live) and is deleted. | [optional] |
| **ttl** | **Integer**| An alias for &#x60;item_ttl&#x60;. If both parameters are provided, this value is ignored. | [optional] |

### Return type

[**SyncV1ServiceSyncMapSyncMapItem**](SyncV1ServiceSyncMapSyncMapItem.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

