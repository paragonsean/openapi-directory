# SyncV1SyncMapPermissionApi

All URIs are relative to *https://sync.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteSyncMapPermission**](SyncV1SyncMapPermissionApi.md#deleteSyncMapPermission) | **DELETE** /v1/Services/{ServiceSid}/Maps/{MapSid}/Permissions/{Identity} |  |
| [**fetchSyncMapPermission**](SyncV1SyncMapPermissionApi.md#fetchSyncMapPermission) | **GET** /v1/Services/{ServiceSid}/Maps/{MapSid}/Permissions/{Identity} |  |
| [**listSyncMapPermission**](SyncV1SyncMapPermissionApi.md#listSyncMapPermission) | **GET** /v1/Services/{ServiceSid}/Maps/{MapSid}/Permissions |  |
| [**updateSyncMapPermission**](SyncV1SyncMapPermissionApi.md#updateSyncMapPermission) | **POST** /v1/Services/{ServiceSid}/Maps/{MapSid}/Permissions/{Identity} |  |


<a id="deleteSyncMapPermission"></a>
# **deleteSyncMapPermission**
> deleteSyncMapPermission(serviceSid, mapSid, identity)



Delete a specific Sync Map Permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncV1SyncMapPermissionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sync.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SyncV1SyncMapPermissionApi apiInstance = new SyncV1SyncMapPermissionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map Permission resource to delete. Can be the Service's `sid` value or `default`.
    String mapSid = "mapSid_example"; // String | The SID of the Sync Map with the Sync Map Permission resource to delete. Can be the Sync Map resource's `sid` or its `unique_name`.
    String identity = "identity_example"; // String | The application-defined string that uniquely identifies the User's Sync Map Permission resource to delete.
    try {
      apiInstance.deleteSyncMapPermission(serviceSid, mapSid, identity);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncV1SyncMapPermissionApi#deleteSyncMapPermission");
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
| **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map Permission resource to delete. Can be the Service&#39;s &#x60;sid&#x60; value or &#x60;default&#x60;. | |
| **mapSid** | **String**| The SID of the Sync Map with the Sync Map Permission resource to delete. Can be the Sync Map resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | |
| **identity** | **String**| The application-defined string that uniquely identifies the User&#39;s Sync Map Permission resource to delete. | |

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

<a id="fetchSyncMapPermission"></a>
# **fetchSyncMapPermission**
> SyncV1ServiceSyncMapSyncMapPermission fetchSyncMapPermission(serviceSid, mapSid, identity)



Fetch a specific Sync Map Permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncV1SyncMapPermissionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sync.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SyncV1SyncMapPermissionApi apiInstance = new SyncV1SyncMapPermissionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map Permission resource to fetch. Can be the Service's `sid` value or `default`.
    String mapSid = "mapSid_example"; // String | The SID of the Sync Map with the Sync Map Permission resource to fetch. Can be the Sync Map resource's `sid` or its `unique_name`.
    String identity = "identity_example"; // String | The application-defined string that uniquely identifies the User's Sync Map Permission resource to fetch.
    try {
      SyncV1ServiceSyncMapSyncMapPermission result = apiInstance.fetchSyncMapPermission(serviceSid, mapSid, identity);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncV1SyncMapPermissionApi#fetchSyncMapPermission");
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
| **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map Permission resource to fetch. Can be the Service&#39;s &#x60;sid&#x60; value or &#x60;default&#x60;. | |
| **mapSid** | **String**| The SID of the Sync Map with the Sync Map Permission resource to fetch. Can be the Sync Map resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | |
| **identity** | **String**| The application-defined string that uniquely identifies the User&#39;s Sync Map Permission resource to fetch. | |

### Return type

[**SyncV1ServiceSyncMapSyncMapPermission**](SyncV1ServiceSyncMapSyncMapPermission.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listSyncMapPermission"></a>
# **listSyncMapPermission**
> ListSyncMapPermissionResponse listSyncMapPermission(serviceSid, mapSid, pageSize, page, pageToken)



Retrieve a list of all Permissions applying to a Sync Map.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncV1SyncMapPermissionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sync.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SyncV1SyncMapPermissionApi apiInstance = new SyncV1SyncMapPermissionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map Permission resources to read. Can be the Service's `sid` value or `default`.
    String mapSid = "mapSid_example"; // String | The SID of the Sync Map with the Permission resources to read. Can be the Sync Map resource's `sid` or its `unique_name`.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListSyncMapPermissionResponse result = apiInstance.listSyncMapPermission(serviceSid, mapSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncV1SyncMapPermissionApi#listSyncMapPermission");
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
| **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map Permission resources to read. Can be the Service&#39;s &#x60;sid&#x60; value or &#x60;default&#x60;. | |
| **mapSid** | **String**| The SID of the Sync Map with the Permission resources to read. Can be the Sync Map resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListSyncMapPermissionResponse**](ListSyncMapPermissionResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateSyncMapPermission"></a>
# **updateSyncMapPermission**
> SyncV1ServiceSyncMapSyncMapPermission updateSyncMapPermission(serviceSid, mapSid, identity, manage, read, write)



Update an identity&#39;s access to a specific Sync Map.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncV1SyncMapPermissionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sync.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SyncV1SyncMapPermissionApi apiInstance = new SyncV1SyncMapPermissionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map Permission resource to update. Can be the Service's `sid` value or `default`.
    String mapSid = "mapSid_example"; // String | The SID of the Sync Map with the Sync Map Permission resource to update. Can be the Sync Map resource's `sid` or its `unique_name`.
    String identity = "identity_example"; // String | The application-defined string that uniquely identifies the User's Sync Map Permission resource to update.
    Boolean manage = true; // Boolean | Whether the identity can delete the Sync Map. Default value is `false`.
    Boolean read = true; // Boolean | Whether the identity can read the Sync Map and its Items. Default value is `false`.
    Boolean write = true; // Boolean | Whether the identity can create, update, and delete Items in the Sync Map. Default value is `false`.
    try {
      SyncV1ServiceSyncMapSyncMapPermission result = apiInstance.updateSyncMapPermission(serviceSid, mapSid, identity, manage, read, write);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncV1SyncMapPermissionApi#updateSyncMapPermission");
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
| **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map Permission resource to update. Can be the Service&#39;s &#x60;sid&#x60; value or &#x60;default&#x60;. | |
| **mapSid** | **String**| The SID of the Sync Map with the Sync Map Permission resource to update. Can be the Sync Map resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | |
| **identity** | **String**| The application-defined string that uniquely identifies the User&#39;s Sync Map Permission resource to update. | |
| **manage** | **Boolean**| Whether the identity can delete the Sync Map. Default value is &#x60;false&#x60;. | |
| **read** | **Boolean**| Whether the identity can read the Sync Map and its Items. Default value is &#x60;false&#x60;. | |
| **write** | **Boolean**| Whether the identity can create, update, and delete Items in the Sync Map. Default value is &#x60;false&#x60;. | |

### Return type

[**SyncV1ServiceSyncMapSyncMapPermission**](SyncV1ServiceSyncMapSyncMapPermission.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

