# LocksApi

All URIs are relative to *https://dweet.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**lockThing**](LocksApi.md#lockThing) | **GET** /lock/{thing} | Reserve and lock a thing. |
| [**removeLock**](LocksApi.md#removeLock) | **GET** /remove/lock/{lock} | Remove a lock from thing. |
| [**unlockThing**](LocksApi.md#unlockThing) | **GET** /unlock/{thing} | Unlock a thing. |


<a id="lockThing"></a>
# **lockThing**
> lockThing(thing, lock, key)

Reserve and lock a thing.

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
    defaultClient.setBasePath("https://dweet.io");

    LocksApi apiInstance = new LocksApi(defaultClient);
    String thing = "thing_example"; // String | A unique name of a thing.
    String lock = "lock_example"; // String | A valid dweet.io lock.
    String key = "key_example"; // String | A valid dweet.io master key.
    try {
      apiInstance.lockThing(thing, lock, key);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocksApi#lockThing");
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
| **thing** | **String**| A unique name of a thing. | |
| **lock** | **String**| A valid dweet.io lock. | |
| **key** | **String**| A valid dweet.io master key. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="removeLock"></a>
# **removeLock**
> removeLock(lock, key)

Remove a lock from thing.

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
    defaultClient.setBasePath("https://dweet.io");

    LocksApi apiInstance = new LocksApi(defaultClient);
    String lock = "lock_example"; // String | A valid dweet.io lock.
    String key = "key_example"; // String | A valid dweet.io master key.
    try {
      apiInstance.removeLock(lock, key);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocksApi#removeLock");
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
| **lock** | **String**| A valid dweet.io lock. | |
| **key** | **String**| A valid dweet.io master key. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="unlockThing"></a>
# **unlockThing**
> unlockThing(thing, key)

Unlock a thing.

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
    defaultClient.setBasePath("https://dweet.io");

    LocksApi apiInstance = new LocksApi(defaultClient);
    String thing = "thing_example"; // String | A unique name of a thing.
    String key = "key_example"; // String | A valid dweet.io master key.
    try {
      apiInstance.unlockThing(thing, key);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocksApi#unlockThing");
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
| **thing** | **String**| A unique name of a thing. | |
| **key** | **String**| A valid dweet.io master key. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

