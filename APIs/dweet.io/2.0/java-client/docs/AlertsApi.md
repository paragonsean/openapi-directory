# AlertsApi

All URIs are relative to *https://dweet.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createAlertGET**](AlertsApi.md#createAlertGET) | **GET** /alert/{who}/when/{thing}/{condition} | Create an alert for a thing. A thing must be locked before an alert can be set. |
| [**getAlert**](AlertsApi.md#getAlert) | **GET** /get/alert/for/{thing} | Get the alert attached to a thing. |
| [**removeAlert**](AlertsApi.md#removeAlert) | **GET** /remove/alert/for/{thing} | Remove an alert for a thing. |


<a id="createAlertGET"></a>
# **createAlertGET**
> createAlertGET(who, thing, condition, key)

Create an alert for a thing. A thing must be locked before an alert can be set.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dweet.io");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String who = "who_example"; // String | A comma separated list of Email addresses to send the alert to.
    String thing = "thing_example"; // String | A unique name of a thing. It is recommended that you use a GUID as to avoid name collisions.
    String condition = "condition_example"; // String | A condition that returns a string or a true value if a condition is met.
    String key = "key_example"; // String | A valid key for a locked thing. If the thing is not locked, this can be ignored.
    try {
      apiInstance.createAlertGET(who, thing, condition, key);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#createAlertGET");
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
| **who** | **String**| A comma separated list of Email addresses to send the alert to. | |
| **thing** | **String**| A unique name of a thing. It is recommended that you use a GUID as to avoid name collisions. | |
| **condition** | **String**| A condition that returns a string or a true value if a condition is met. | |
| **key** | **String**| A valid key for a locked thing. If the thing is not locked, this can be ignored. | |

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

<a id="getAlert"></a>
# **getAlert**
> getAlert(thing, key)

Get the alert attached to a thing.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dweet.io");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String thing = "thing_example"; // String | A unique name of a thing.
    String key = "key_example"; // String | A valid key for a locked thing. If the thing is not locked, this can be ignored.
    try {
      apiInstance.getAlert(thing, key);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#getAlert");
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
| **key** | **String**| A valid key for a locked thing. If the thing is not locked, this can be ignored. | |

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

<a id="removeAlert"></a>
# **removeAlert**
> removeAlert(thing, key)

Remove an alert for a thing.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dweet.io");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String thing = "thing_example"; // String | A unique name of a thing.
    String key = "key_example"; // String | A valid key for a locked thing. If the thing is not locked, this can be ignored.
    try {
      apiInstance.removeAlert(thing, key);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#removeAlert");
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
| **key** | **String**| A valid key for a locked thing. If the thing is not locked, this can be ignored. | |

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

