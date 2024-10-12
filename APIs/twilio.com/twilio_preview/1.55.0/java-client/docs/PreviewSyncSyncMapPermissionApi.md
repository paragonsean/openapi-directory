# PreviewSyncSyncMapPermissionApi

All URIs are relative to *https://preview.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteSyncSyncMapPermission**](PreviewSyncSyncMapPermissionApi.md#deleteSyncSyncMapPermission) | **DELETE** /Sync/Services/{ServiceSid}/Maps/{MapSid}/Permissions/{Identity} |  |
| [**fetchSyncSyncMapPermission**](PreviewSyncSyncMapPermissionApi.md#fetchSyncSyncMapPermission) | **GET** /Sync/Services/{ServiceSid}/Maps/{MapSid}/Permissions/{Identity} |  |
| [**listSyncSyncMapPermission**](PreviewSyncSyncMapPermissionApi.md#listSyncSyncMapPermission) | **GET** /Sync/Services/{ServiceSid}/Maps/{MapSid}/Permissions |  |
| [**updateSyncSyncMapPermission**](PreviewSyncSyncMapPermissionApi.md#updateSyncSyncMapPermission) | **POST** /Sync/Services/{ServiceSid}/Maps/{MapSid}/Permissions/{Identity} |  |


<a id="deleteSyncSyncMapPermission"></a>
# **deleteSyncSyncMapPermission**
> deleteSyncSyncMapPermission(serviceSid, mapSid, identity)



Delete a specific Sync Map Permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewSyncSyncMapPermissionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewSyncSyncMapPermissionApi apiInstance = new PreviewSyncSyncMapPermissionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String mapSid = "mapSid_example"; // String | Identifier of the Sync Map. Either a SID or a unique name.
    String identity = "identity_example"; // String | Arbitrary string identifier representing a user associated with an FPA token, assigned by the developer.
    try {
      apiInstance.deleteSyncSyncMapPermission(serviceSid, mapSid, identity);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewSyncSyncMapPermissionApi#deleteSyncSyncMapPermission");
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
| **mapSid** | **String**| Identifier of the Sync Map. Either a SID or a unique name. | |
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

<a id="fetchSyncSyncMapPermission"></a>
# **fetchSyncSyncMapPermission**
> PreviewSyncServiceSyncMapSyncMapPermission fetchSyncSyncMapPermission(serviceSid, mapSid, identity)



Fetch a specific Sync Map Permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewSyncSyncMapPermissionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewSyncSyncMapPermissionApi apiInstance = new PreviewSyncSyncMapPermissionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String mapSid = "mapSid_example"; // String | Identifier of the Sync Map. Either a SID or a unique name.
    String identity = "identity_example"; // String | Arbitrary string identifier representing a user associated with an FPA token, assigned by the developer.
    try {
      PreviewSyncServiceSyncMapSyncMapPermission result = apiInstance.fetchSyncSyncMapPermission(serviceSid, mapSid, identity);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewSyncSyncMapPermissionApi#fetchSyncSyncMapPermission");
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
| **mapSid** | **String**| Identifier of the Sync Map. Either a SID or a unique name. | |
| **identity** | **String**| Arbitrary string identifier representing a user associated with an FPA token, assigned by the developer. | |

### Return type

[**PreviewSyncServiceSyncMapSyncMapPermission**](PreviewSyncServiceSyncMapSyncMapPermission.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listSyncSyncMapPermission"></a>
# **listSyncSyncMapPermission**
> ListSyncSyncMapPermissionResponse listSyncSyncMapPermission(serviceSid, mapSid, pageSize, page, pageToken)



Retrieve a list of all Permissions applying to a Sync Map.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewSyncSyncMapPermissionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewSyncSyncMapPermissionApi apiInstance = new PreviewSyncSyncMapPermissionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String mapSid = "mapSid_example"; // String | Identifier of the Sync Map. Either a SID or a unique name.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListSyncSyncMapPermissionResponse result = apiInstance.listSyncSyncMapPermission(serviceSid, mapSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewSyncSyncMapPermissionApi#listSyncSyncMapPermission");
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
| **mapSid** | **String**| Identifier of the Sync Map. Either a SID or a unique name. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListSyncSyncMapPermissionResponse**](ListSyncSyncMapPermissionResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateSyncSyncMapPermission"></a>
# **updateSyncSyncMapPermission**
> PreviewSyncServiceSyncMapSyncMapPermission updateSyncSyncMapPermission(serviceSid, mapSid, identity, manage, read, write)



Update an identity&#39;s access to a specific Sync Map.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewSyncSyncMapPermissionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewSyncSyncMapPermissionApi apiInstance = new PreviewSyncSyncMapPermissionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The unique SID identifier of the Sync Service Instance.
    String mapSid = "mapSid_example"; // String | Identifier of the Sync Map. Either a SID or a unique name.
    String identity = "identity_example"; // String | Arbitrary string identifier representing a human user associated with an FPA token, assigned by the developer.
    Boolean manage = true; // Boolean | Boolean flag specifying whether the identity can delete the Sync Map.
    Boolean read = true; // Boolean | Boolean flag specifying whether the identity can read the Sync Map.
    Boolean write = true; // Boolean | Boolean flag specifying whether the identity can create, update and delete Items of the Sync Map.
    try {
      PreviewSyncServiceSyncMapSyncMapPermission result = apiInstance.updateSyncSyncMapPermission(serviceSid, mapSid, identity, manage, read, write);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewSyncSyncMapPermissionApi#updateSyncSyncMapPermission");
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
| **mapSid** | **String**| Identifier of the Sync Map. Either a SID or a unique name. | |
| **identity** | **String**| Arbitrary string identifier representing a human user associated with an FPA token, assigned by the developer. | |
| **manage** | **Boolean**| Boolean flag specifying whether the identity can delete the Sync Map. | |
| **read** | **Boolean**| Boolean flag specifying whether the identity can read the Sync Map. | |
| **write** | **Boolean**| Boolean flag specifying whether the identity can create, update and delete Items of the Sync Map. | |

### Return type

[**PreviewSyncServiceSyncMapSyncMapPermission**](PreviewSyncServiceSyncMapSyncMapPermission.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

