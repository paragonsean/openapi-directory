# PreviewSyncDocumentPermissionApi

All URIs are relative to *https://preview.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteSyncDocumentPermission**](PreviewSyncDocumentPermissionApi.md#deleteSyncDocumentPermission) | **DELETE** /Sync/Services/{ServiceSid}/Documents/{DocumentSid}/Permissions/{Identity} |  |
| [**fetchSyncDocumentPermission**](PreviewSyncDocumentPermissionApi.md#fetchSyncDocumentPermission) | **GET** /Sync/Services/{ServiceSid}/Documents/{DocumentSid}/Permissions/{Identity} |  |
| [**listSyncDocumentPermission**](PreviewSyncDocumentPermissionApi.md#listSyncDocumentPermission) | **GET** /Sync/Services/{ServiceSid}/Documents/{DocumentSid}/Permissions |  |
| [**updateSyncDocumentPermission**](PreviewSyncDocumentPermissionApi.md#updateSyncDocumentPermission) | **POST** /Sync/Services/{ServiceSid}/Documents/{DocumentSid}/Permissions/{Identity} |  |


<a id="deleteSyncDocumentPermission"></a>
# **deleteSyncDocumentPermission**
> deleteSyncDocumentPermission(serviceSid, documentSid, identity)



Delete a specific Sync Document Permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewSyncDocumentPermissionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewSyncDocumentPermissionApi apiInstance = new PreviewSyncDocumentPermissionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String documentSid = "documentSid_example"; // String | Identifier of the Sync Document. Either a SID or a unique name.
    String identity = "identity_example"; // String | Arbitrary string identifier representing a user associated with an FPA token, assigned by the developer.
    try {
      apiInstance.deleteSyncDocumentPermission(serviceSid, documentSid, identity);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewSyncDocumentPermissionApi#deleteSyncDocumentPermission");
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
| **documentSid** | **String**| Identifier of the Sync Document. Either a SID or a unique name. | |
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

<a id="fetchSyncDocumentPermission"></a>
# **fetchSyncDocumentPermission**
> PreviewSyncServiceDocumentDocumentPermission fetchSyncDocumentPermission(serviceSid, documentSid, identity)



Fetch a specific Sync Document Permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewSyncDocumentPermissionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewSyncDocumentPermissionApi apiInstance = new PreviewSyncDocumentPermissionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String documentSid = "documentSid_example"; // String | Identifier of the Sync Document. Either a SID or a unique name.
    String identity = "identity_example"; // String | Arbitrary string identifier representing a user associated with an FPA token, assigned by the developer.
    try {
      PreviewSyncServiceDocumentDocumentPermission result = apiInstance.fetchSyncDocumentPermission(serviceSid, documentSid, identity);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewSyncDocumentPermissionApi#fetchSyncDocumentPermission");
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
| **documentSid** | **String**| Identifier of the Sync Document. Either a SID or a unique name. | |
| **identity** | **String**| Arbitrary string identifier representing a user associated with an FPA token, assigned by the developer. | |

### Return type

[**PreviewSyncServiceDocumentDocumentPermission**](PreviewSyncServiceDocumentDocumentPermission.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listSyncDocumentPermission"></a>
# **listSyncDocumentPermission**
> ListSyncDocumentPermissionResponse listSyncDocumentPermission(serviceSid, documentSid, pageSize, page, pageToken)



Retrieve a list of all Permissions applying to a Sync Document.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewSyncDocumentPermissionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewSyncDocumentPermissionApi apiInstance = new PreviewSyncDocumentPermissionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String documentSid = "documentSid_example"; // String | Identifier of the Sync Document. Either a SID or a unique name.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListSyncDocumentPermissionResponse result = apiInstance.listSyncDocumentPermission(serviceSid, documentSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewSyncDocumentPermissionApi#listSyncDocumentPermission");
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
| **documentSid** | **String**| Identifier of the Sync Document. Either a SID or a unique name. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListSyncDocumentPermissionResponse**](ListSyncDocumentPermissionResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateSyncDocumentPermission"></a>
# **updateSyncDocumentPermission**
> PreviewSyncServiceDocumentDocumentPermission updateSyncDocumentPermission(serviceSid, documentSid, identity, manage, read, write)



Update an identity&#39;s access to a specific Sync Document.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewSyncDocumentPermissionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewSyncDocumentPermissionApi apiInstance = new PreviewSyncDocumentPermissionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The unique SID identifier of the Sync Service Instance.
    String documentSid = "documentSid_example"; // String | Identifier of the Sync Document. Either a SID or a unique name.
    String identity = "identity_example"; // String | Arbitrary string identifier representing a human user associated with an FPA token, assigned by the developer.
    Boolean manage = true; // Boolean | Boolean flag specifying whether the identity can delete the Sync Document.
    Boolean read = true; // Boolean | Boolean flag specifying whether the identity can read the Sync Document.
    Boolean write = true; // Boolean | Boolean flag specifying whether the identity can update the Sync Document.
    try {
      PreviewSyncServiceDocumentDocumentPermission result = apiInstance.updateSyncDocumentPermission(serviceSid, documentSid, identity, manage, read, write);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewSyncDocumentPermissionApi#updateSyncDocumentPermission");
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
| **documentSid** | **String**| Identifier of the Sync Document. Either a SID or a unique name. | |
| **identity** | **String**| Arbitrary string identifier representing a human user associated with an FPA token, assigned by the developer. | |
| **manage** | **Boolean**| Boolean flag specifying whether the identity can delete the Sync Document. | |
| **read** | **Boolean**| Boolean flag specifying whether the identity can read the Sync Document. | |
| **write** | **Boolean**| Boolean flag specifying whether the identity can update the Sync Document. | |

### Return type

[**PreviewSyncServiceDocumentDocumentPermission**](PreviewSyncServiceDocumentDocumentPermission.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

