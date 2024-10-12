# LocksApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteLock**](LocksApi.md#deleteLock) | **DELETE** /locks/{key} | Unlocks a key-value. |
| [**putLock**](LocksApi.md#putLock) | **PUT** /locks/{key} | Locks a key-value. |


<a id="deleteLock"></a>
# **deleteLock**
> KeyValue deleteLock(key, apiVersion, label, syncToken, ifMatch, ifNoneMatch)

Unlocks a key-value.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    LocksApi apiInstance = new LocksApi(defaultClient);
    String key = "key_example"; // String | The key of the key-value to unlock.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String label = "label_example"; // String | The label, if any, of the key-value to unlock.
    String syncToken = "syncToken_example"; // String | Used to guarantee real-time consistency between requests.
    String ifMatch = "ifMatch_example"; // String | Used to perform an operation only if the targeted resource's etag matches the value provided.
    String ifNoneMatch = "ifNoneMatch_example"; // String | Used to perform an operation only if the targeted resource's etag does not match the value provided.
    try {
      KeyValue result = apiInstance.deleteLock(key, apiVersion, label, syncToken, ifMatch, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocksApi#deleteLock");
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
| **key** | **String**| The key of the key-value to unlock. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **label** | **String**| The label, if any, of the key-value to unlock. | [optional] |
| **syncToken** | **String**| Used to guarantee real-time consistency between requests. | [optional] |
| **ifMatch** | **String**| Used to perform an operation only if the targeted resource&#39;s etag matches the value provided. | [optional] |
| **ifNoneMatch** | **String**| Used to perform an operation only if the targeted resource&#39;s etag does not match the value provided. | [optional] |

### Return type

[**KeyValue**](KeyValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.microsoft.appconfig.kv+json, application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  * ETag - An identifier representing the returned state of the resource. <br>  * Sync-Token - Enables real-time consistency between requests by providing the returned value in the next request made to the server. <br>  |
| **0** | Error response describing why the operation failed |  -  |

<a id="putLock"></a>
# **putLock**
> KeyValue putLock(key, apiVersion, label, syncToken, ifMatch, ifNoneMatch)

Locks a key-value.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    LocksApi apiInstance = new LocksApi(defaultClient);
    String key = "key_example"; // String | The key of the key-value to lock.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String label = "label_example"; // String | The label, if any, of the key-value to lock.
    String syncToken = "syncToken_example"; // String | Used to guarantee real-time consistency between requests.
    String ifMatch = "ifMatch_example"; // String | Used to perform an operation only if the targeted resource's etag matches the value provided.
    String ifNoneMatch = "ifNoneMatch_example"; // String | Used to perform an operation only if the targeted resource's etag does not match the value provided.
    try {
      KeyValue result = apiInstance.putLock(key, apiVersion, label, syncToken, ifMatch, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocksApi#putLock");
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
| **key** | **String**| The key of the key-value to lock. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **label** | **String**| The label, if any, of the key-value to lock. | [optional] |
| **syncToken** | **String**| Used to guarantee real-time consistency between requests. | [optional] |
| **ifMatch** | **String**| Used to perform an operation only if the targeted resource&#39;s etag matches the value provided. | [optional] |
| **ifNoneMatch** | **String**| Used to perform an operation only if the targeted resource&#39;s etag does not match the value provided. | [optional] |

### Return type

[**KeyValue**](KeyValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.microsoft.appconfig.kv+json, application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  * ETag - An identifier representing the returned state of the resource. <br>  * Sync-Token - Enables real-time consistency between requests by providing the returned value in the next request made to the server. <br>  |
| **0** | Error response describing why the operation failed |  -  |

