# SyncV1SyncListPermissionApi

All URIs are relative to *https://sync.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteSyncListPermission**](SyncV1SyncListPermissionApi.md#deleteSyncListPermission) | **DELETE** /v1/Services/{ServiceSid}/Lists/{ListSid}/Permissions/{Identity} |  |
| [**fetchSyncListPermission**](SyncV1SyncListPermissionApi.md#fetchSyncListPermission) | **GET** /v1/Services/{ServiceSid}/Lists/{ListSid}/Permissions/{Identity} |  |
| [**listSyncListPermission**](SyncV1SyncListPermissionApi.md#listSyncListPermission) | **GET** /v1/Services/{ServiceSid}/Lists/{ListSid}/Permissions |  |
| [**updateSyncListPermission**](SyncV1SyncListPermissionApi.md#updateSyncListPermission) | **POST** /v1/Services/{ServiceSid}/Lists/{ListSid}/Permissions/{Identity} |  |


<a id="deleteSyncListPermission"></a>
# **deleteSyncListPermission**
> deleteSyncListPermission(serviceSid, listSid, identity)



Delete a specific Sync List Permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncV1SyncListPermissionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sync.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SyncV1SyncListPermissionApi apiInstance = new SyncV1SyncListPermissionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync List Permission resource to delete.
    String listSid = "listSid_example"; // String | The SID of the Sync List with the Sync List Permission resource to delete. Can be the Sync List resource's `sid` or its `unique_name`.
    String identity = "identity_example"; // String | The application-defined string that uniquely identifies the User's Sync List Permission resource to delete.
    try {
      apiInstance.deleteSyncListPermission(serviceSid, listSid, identity);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncV1SyncListPermissionApi#deleteSyncListPermission");
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
| **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync List Permission resource to delete. | |
| **listSid** | **String**| The SID of the Sync List with the Sync List Permission resource to delete. Can be the Sync List resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | |
| **identity** | **String**| The application-defined string that uniquely identifies the User&#39;s Sync List Permission resource to delete. | |

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

<a id="fetchSyncListPermission"></a>
# **fetchSyncListPermission**
> SyncV1ServiceSyncListSyncListPermission fetchSyncListPermission(serviceSid, listSid, identity)



Fetch a specific Sync List Permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncV1SyncListPermissionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sync.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SyncV1SyncListPermissionApi apiInstance = new SyncV1SyncListPermissionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync List Permission resource to fetch.
    String listSid = "listSid_example"; // String | The SID of the Sync List with the Sync List Permission resource to fetch. Can be the Sync List resource's `sid` or its `unique_name`.
    String identity = "identity_example"; // String | The application-defined string that uniquely identifies the User's Sync List Permission resource to fetch.
    try {
      SyncV1ServiceSyncListSyncListPermission result = apiInstance.fetchSyncListPermission(serviceSid, listSid, identity);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncV1SyncListPermissionApi#fetchSyncListPermission");
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
| **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync List Permission resource to fetch. | |
| **listSid** | **String**| The SID of the Sync List with the Sync List Permission resource to fetch. Can be the Sync List resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | |
| **identity** | **String**| The application-defined string that uniquely identifies the User&#39;s Sync List Permission resource to fetch. | |

### Return type

[**SyncV1ServiceSyncListSyncListPermission**](SyncV1ServiceSyncListSyncListPermission.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listSyncListPermission"></a>
# **listSyncListPermission**
> ListSyncListPermissionResponse listSyncListPermission(serviceSid, listSid, pageSize, page, pageToken)



Retrieve a list of all Permissions applying to a Sync List.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncV1SyncListPermissionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sync.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SyncV1SyncListPermissionApi apiInstance = new SyncV1SyncListPermissionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync List Permission resources to read.
    String listSid = "listSid_example"; // String | The SID of the Sync List with the Sync List Permission resources to read. Can be the Sync List resource's `sid` or its `unique_name`.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListSyncListPermissionResponse result = apiInstance.listSyncListPermission(serviceSid, listSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncV1SyncListPermissionApi#listSyncListPermission");
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
| **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync List Permission resources to read. | |
| **listSid** | **String**| The SID of the Sync List with the Sync List Permission resources to read. Can be the Sync List resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListSyncListPermissionResponse**](ListSyncListPermissionResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateSyncListPermission"></a>
# **updateSyncListPermission**
> SyncV1ServiceSyncListSyncListPermission updateSyncListPermission(serviceSid, listSid, identity, manage, read, write)



Update an identity&#39;s access to a specific Sync List.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncV1SyncListPermissionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sync.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SyncV1SyncListPermissionApi apiInstance = new SyncV1SyncListPermissionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync List Permission resource to update.
    String listSid = "listSid_example"; // String | The SID of the Sync List with the Sync List Permission resource to update. Can be the Sync List resource's `sid` or its `unique_name`.
    String identity = "identity_example"; // String | The application-defined string that uniquely identifies the User's Sync List Permission resource to update.
    Boolean manage = true; // Boolean | Whether the identity can delete the Sync List. Default value is `false`.
    Boolean read = true; // Boolean | Whether the identity can read the Sync List and its Items. Default value is `false`.
    Boolean write = true; // Boolean | Whether the identity can create, update, and delete Items in the Sync List. Default value is `false`.
    try {
      SyncV1ServiceSyncListSyncListPermission result = apiInstance.updateSyncListPermission(serviceSid, listSid, identity, manage, read, write);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncV1SyncListPermissionApi#updateSyncListPermission");
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
| **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync List Permission resource to update. | |
| **listSid** | **String**| The SID of the Sync List with the Sync List Permission resource to update. Can be the Sync List resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | |
| **identity** | **String**| The application-defined string that uniquely identifies the User&#39;s Sync List Permission resource to update. | |
| **manage** | **Boolean**| Whether the identity can delete the Sync List. Default value is &#x60;false&#x60;. | |
| **read** | **Boolean**| Whether the identity can read the Sync List and its Items. Default value is &#x60;false&#x60;. | |
| **write** | **Boolean**| Whether the identity can create, update, and delete Items in the Sync List. Default value is &#x60;false&#x60;. | |

### Return type

[**SyncV1ServiceSyncListSyncListPermission**](SyncV1ServiceSyncListSyncListPermission.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

