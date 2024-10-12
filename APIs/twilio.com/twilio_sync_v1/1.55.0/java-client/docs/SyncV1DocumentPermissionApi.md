# SyncV1DocumentPermissionApi

All URIs are relative to *https://sync.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteDocumentPermission**](SyncV1DocumentPermissionApi.md#deleteDocumentPermission) | **DELETE** /v1/Services/{ServiceSid}/Documents/{DocumentSid}/Permissions/{Identity} |  |
| [**fetchDocumentPermission**](SyncV1DocumentPermissionApi.md#fetchDocumentPermission) | **GET** /v1/Services/{ServiceSid}/Documents/{DocumentSid}/Permissions/{Identity} |  |
| [**listDocumentPermission**](SyncV1DocumentPermissionApi.md#listDocumentPermission) | **GET** /v1/Services/{ServiceSid}/Documents/{DocumentSid}/Permissions |  |
| [**updateDocumentPermission**](SyncV1DocumentPermissionApi.md#updateDocumentPermission) | **POST** /v1/Services/{ServiceSid}/Documents/{DocumentSid}/Permissions/{Identity} |  |


<a id="deleteDocumentPermission"></a>
# **deleteDocumentPermission**
> deleteDocumentPermission(serviceSid, documentSid, identity)



Delete a specific Sync Document Permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncV1DocumentPermissionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sync.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SyncV1DocumentPermissionApi apiInstance = new SyncV1DocumentPermissionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Document Permission resource to delete.
    String documentSid = "documentSid_example"; // String | The SID of the Sync Document with the Document Permission resource to delete. Can be the Document resource's `sid` or its `unique_name`.
    String identity = "identity_example"; // String | The application-defined string that uniquely identifies the User's Document Permission resource to delete.
    try {
      apiInstance.deleteDocumentPermission(serviceSid, documentSid, identity);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncV1DocumentPermissionApi#deleteDocumentPermission");
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
| **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Document Permission resource to delete. | |
| **documentSid** | **String**| The SID of the Sync Document with the Document Permission resource to delete. Can be the Document resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | |
| **identity** | **String**| The application-defined string that uniquely identifies the User&#39;s Document Permission resource to delete. | |

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

<a id="fetchDocumentPermission"></a>
# **fetchDocumentPermission**
> SyncV1ServiceDocumentDocumentPermission fetchDocumentPermission(serviceSid, documentSid, identity)



Fetch a specific Sync Document Permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncV1DocumentPermissionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sync.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SyncV1DocumentPermissionApi apiInstance = new SyncV1DocumentPermissionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Document Permission resource to fetch.
    String documentSid = "documentSid_example"; // String | The SID of the Sync Document with the Document Permission resource to fetch. Can be the Document resource's `sid` or its `unique_name`.
    String identity = "identity_example"; // String | The application-defined string that uniquely identifies the User's Document Permission resource to fetch.
    try {
      SyncV1ServiceDocumentDocumentPermission result = apiInstance.fetchDocumentPermission(serviceSid, documentSid, identity);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncV1DocumentPermissionApi#fetchDocumentPermission");
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
| **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Document Permission resource to fetch. | |
| **documentSid** | **String**| The SID of the Sync Document with the Document Permission resource to fetch. Can be the Document resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | |
| **identity** | **String**| The application-defined string that uniquely identifies the User&#39;s Document Permission resource to fetch. | |

### Return type

[**SyncV1ServiceDocumentDocumentPermission**](SyncV1ServiceDocumentDocumentPermission.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listDocumentPermission"></a>
# **listDocumentPermission**
> ListDocumentPermissionResponse listDocumentPermission(serviceSid, documentSid, pageSize, page, pageToken)



Retrieve a list of all Permissions applying to a Sync Document.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncV1DocumentPermissionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sync.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SyncV1DocumentPermissionApi apiInstance = new SyncV1DocumentPermissionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Document Permission resources to read.
    String documentSid = "documentSid_example"; // String | The SID of the Sync Document with the Document Permission resources to read. Can be the Document resource's `sid` or its `unique_name`.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListDocumentPermissionResponse result = apiInstance.listDocumentPermission(serviceSid, documentSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncV1DocumentPermissionApi#listDocumentPermission");
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
| **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Document Permission resources to read. | |
| **documentSid** | **String**| The SID of the Sync Document with the Document Permission resources to read. Can be the Document resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListDocumentPermissionResponse**](ListDocumentPermissionResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateDocumentPermission"></a>
# **updateDocumentPermission**
> SyncV1ServiceDocumentDocumentPermission updateDocumentPermission(serviceSid, documentSid, identity, manage, read, write)



Update an identity&#39;s access to a specific Sync Document.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncV1DocumentPermissionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sync.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SyncV1DocumentPermissionApi apiInstance = new SyncV1DocumentPermissionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Document Permission resource to update.
    String documentSid = "documentSid_example"; // String | The SID of the Sync Document with the Document Permission resource to update. Can be the Document resource's `sid` or its `unique_name`.
    String identity = "identity_example"; // String | The application-defined string that uniquely identifies the User's Document Permission resource to update.
    Boolean manage = true; // Boolean | Whether the identity can delete the Sync Document. Default value is `false`.
    Boolean read = true; // Boolean | Whether the identity can read the Sync Document. Default value is `false`.
    Boolean write = true; // Boolean | Whether the identity can update the Sync Document. Default value is `false`.
    try {
      SyncV1ServiceDocumentDocumentPermission result = apiInstance.updateDocumentPermission(serviceSid, documentSid, identity, manage, read, write);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncV1DocumentPermissionApi#updateDocumentPermission");
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
| **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Document Permission resource to update. | |
| **documentSid** | **String**| The SID of the Sync Document with the Document Permission resource to update. Can be the Document resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | |
| **identity** | **String**| The application-defined string that uniquely identifies the User&#39;s Document Permission resource to update. | |
| **manage** | **Boolean**| Whether the identity can delete the Sync Document. Default value is &#x60;false&#x60;. | |
| **read** | **Boolean**| Whether the identity can read the Sync Document. Default value is &#x60;false&#x60;. | |
| **write** | **Boolean**| Whether the identity can update the Sync Document. Default value is &#x60;false&#x60;. | |

### Return type

[**SyncV1ServiceDocumentDocumentPermission**](SyncV1ServiceDocumentDocumentPermission.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

