# PreviewSyncSyncListPermissionApi

All URIs are relative to *https://preview.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteSyncSyncListPermission**](PreviewSyncSyncListPermissionApi.md#deleteSyncSyncListPermission) | **DELETE** /Sync/Services/{ServiceSid}/Lists/{ListSid}/Permissions/{Identity} |  |
| [**fetchSyncSyncListPermission**](PreviewSyncSyncListPermissionApi.md#fetchSyncSyncListPermission) | **GET** /Sync/Services/{ServiceSid}/Lists/{ListSid}/Permissions/{Identity} |  |
| [**listSyncSyncListPermission**](PreviewSyncSyncListPermissionApi.md#listSyncSyncListPermission) | **GET** /Sync/Services/{ServiceSid}/Lists/{ListSid}/Permissions |  |
| [**updateSyncSyncListPermission**](PreviewSyncSyncListPermissionApi.md#updateSyncSyncListPermission) | **POST** /Sync/Services/{ServiceSid}/Lists/{ListSid}/Permissions/{Identity} |  |


<a id="deleteSyncSyncListPermission"></a>
# **deleteSyncSyncListPermission**
> deleteSyncSyncListPermission(serviceSid, listSid, identity)



Delete a specific Sync List Permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewSyncSyncListPermissionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewSyncSyncListPermissionApi apiInstance = new PreviewSyncSyncListPermissionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String listSid = "listSid_example"; // String | Identifier of the Sync List. Either a SID or a unique name.
    String identity = "identity_example"; // String | Arbitrary string identifier representing a user associated with an FPA token, assigned by the developer.
    try {
      apiInstance.deleteSyncSyncListPermission(serviceSid, listSid, identity);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewSyncSyncListPermissionApi#deleteSyncSyncListPermission");
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
| **listSid** | **String**| Identifier of the Sync List. Either a SID or a unique name. | |
| **identity** | **String**| Arbitrary string identifier representing a user associated with an FPA token, assigned by the developer. | |

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

<a id="fetchSyncSyncListPermission"></a>
# **fetchSyncSyncListPermission**
> PreviewSyncServiceSyncListSyncListPermission fetchSyncSyncListPermission(serviceSid, listSid, identity)



Fetch a specific Sync List Permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewSyncSyncListPermissionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewSyncSyncListPermissionApi apiInstance = new PreviewSyncSyncListPermissionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String listSid = "listSid_example"; // String | Identifier of the Sync List. Either a SID or a unique name.
    String identity = "identity_example"; // String | Arbitrary string identifier representing a user associated with an FPA token, assigned by the developer.
    try {
      PreviewSyncServiceSyncListSyncListPermission result = apiInstance.fetchSyncSyncListPermission(serviceSid, listSid, identity);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewSyncSyncListPermissionApi#fetchSyncSyncListPermission");
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
| **listSid** | **String**| Identifier of the Sync List. Either a SID or a unique name. | |
| **identity** | **String**| Arbitrary string identifier representing a user associated with an FPA token, assigned by the developer. | |

### Return type

[**PreviewSyncServiceSyncListSyncListPermission**](PreviewSyncServiceSyncListSyncListPermission.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listSyncSyncListPermission"></a>
# **listSyncSyncListPermission**
> ListSyncSyncListPermissionResponse listSyncSyncListPermission(serviceSid, listSid, pageSize, page, pageToken)



Retrieve a list of all Permissions applying to a Sync List.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewSyncSyncListPermissionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewSyncSyncListPermissionApi apiInstance = new PreviewSyncSyncListPermissionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String listSid = "listSid_example"; // String | Identifier of the Sync List. Either a SID or a unique name.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListSyncSyncListPermissionResponse result = apiInstance.listSyncSyncListPermission(serviceSid, listSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewSyncSyncListPermissionApi#listSyncSyncListPermission");
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
| **listSid** | **String**| Identifier of the Sync List. Either a SID or a unique name. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListSyncSyncListPermissionResponse**](ListSyncSyncListPermissionResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateSyncSyncListPermission"></a>
# **updateSyncSyncListPermission**
> PreviewSyncServiceSyncListSyncListPermission updateSyncSyncListPermission(serviceSid, listSid, identity, manage, read, write)



Update an identity&#39;s access to a specific Sync List.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewSyncSyncListPermissionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewSyncSyncListPermissionApi apiInstance = new PreviewSyncSyncListPermissionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The unique SID identifier of the Sync Service Instance.
    String listSid = "listSid_example"; // String | Identifier of the Sync List. Either a SID or a unique name.
    String identity = "identity_example"; // String | Arbitrary string identifier representing a human user associated with an FPA token, assigned by the developer.
    Boolean manage = true; // Boolean | Boolean flag specifying whether the identity can delete the Sync List.
    Boolean read = true; // Boolean | Boolean flag specifying whether the identity can read the Sync List.
    Boolean write = true; // Boolean | Boolean flag specifying whether the identity can create, update and delete Items of the Sync List.
    try {
      PreviewSyncServiceSyncListSyncListPermission result = apiInstance.updateSyncSyncListPermission(serviceSid, listSid, identity, manage, read, write);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewSyncSyncListPermissionApi#updateSyncSyncListPermission");
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
| **serviceSid** | **String**| The unique SID identifier of the Sync Service Instance. | |
| **listSid** | **String**| Identifier of the Sync List. Either a SID or a unique name. | |
| **identity** | **String**| Arbitrary string identifier representing a human user associated with an FPA token, assigned by the developer. | |
| **manage** | **Boolean**| Boolean flag specifying whether the identity can delete the Sync List. | |
| **read** | **Boolean**| Boolean flag specifying whether the identity can read the Sync List. | |
| **write** | **Boolean**| Boolean flag specifying whether the identity can create, update and delete Items of the Sync List. | |

### Return type

[**PreviewSyncServiceSyncListSyncListPermission**](PreviewSyncServiceSyncListSyncListPermission.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

