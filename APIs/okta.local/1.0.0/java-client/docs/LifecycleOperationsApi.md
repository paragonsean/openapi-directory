# LifecycleOperationsApi

All URIs are relative to *http://okta.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**activateUser**](LifecycleOperationsApi.md#activateUser) | **POST** /api/v1/users/{userId}/lifecycle/activate | Activate User |
| [**deactivateUser**](LifecycleOperationsApi.md#deactivateUser) | **POST** /api/v1/users/{userId}/lifecycle/deactivate | Deactivate User |
| [**resetPassword**](LifecycleOperationsApi.md#resetPassword) | **POST** /api/v1/users/{userId}/lifecycle/reset_password | Reset Password |
| [**setTempPassword**](LifecycleOperationsApi.md#setTempPassword) | **POST** /api/v1/users/{userId}/lifecycle/expire_password | Set Temp Password |
| [**suspendUser**](LifecycleOperationsApi.md#suspendUser) | **POST** /api/v1/users/{userId}/lifecycle/suspend | Suspend User |
| [**unlockUser**](LifecycleOperationsApi.md#unlockUser) | **POST** /api/v1/users/{userId}/lifecycle/unlock | Unlock User |
| [**unsuspendUser**](LifecycleOperationsApi.md#unsuspendUser) | **POST** /api/v1/users/{userId}/lifecycle/unsuspend | Unsuspend User |


<a id="activateUser"></a>
# **activateUser**
> activateUser(userId, sendEmail)

Activate User

Activate User

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LifecycleOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://okta.local");

    LifecycleOperationsApi apiInstance = new LifecycleOperationsApi(defaultClient);
    String userId = "userId_example"; // String | 
    String sendEmail = "false"; // String | 
    try {
      apiInstance.activateUser(userId, sendEmail);
    } catch (ApiException e) {
      System.err.println("Exception when calling LifecycleOperationsApi#activateUser");
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
| **userId** | **String**|  | |
| **sendEmail** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="deactivateUser"></a>
# **deactivateUser**
> deactivateUser(userId)

Deactivate User

Deactivate User

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LifecycleOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://okta.local");

    LifecycleOperationsApi apiInstance = new LifecycleOperationsApi(defaultClient);
    String userId = "userId_example"; // String | 
    try {
      apiInstance.deactivateUser(userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling LifecycleOperationsApi#deactivateUser");
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
| **userId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="resetPassword"></a>
# **resetPassword**
> resetPassword(userId, sendEmail)

Reset Password

Reset Password

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LifecycleOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://okta.local");

    LifecycleOperationsApi apiInstance = new LifecycleOperationsApi(defaultClient);
    String userId = "userId_example"; // String | 
    String sendEmail = "false"; // String | 
    try {
      apiInstance.resetPassword(userId, sendEmail);
    } catch (ApiException e) {
      System.err.println("Exception when calling LifecycleOperationsApi#resetPassword");
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
| **userId** | **String**|  | |
| **sendEmail** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="setTempPassword"></a>
# **setTempPassword**
> setTempPassword(userId, tempPassword)

Set Temp Password

Set Temp Password

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LifecycleOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://okta.local");

    LifecycleOperationsApi apiInstance = new LifecycleOperationsApi(defaultClient);
    String userId = "userId_example"; // String | 
    String tempPassword = "true"; // String | 
    try {
      apiInstance.setTempPassword(userId, tempPassword);
    } catch (ApiException e) {
      System.err.println("Exception when calling LifecycleOperationsApi#setTempPassword");
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
| **userId** | **String**|  | |
| **tempPassword** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="suspendUser"></a>
# **suspendUser**
> suspendUser(userId)

Suspend User

Suspend User

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LifecycleOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://okta.local");

    LifecycleOperationsApi apiInstance = new LifecycleOperationsApi(defaultClient);
    String userId = "userId_example"; // String | 
    try {
      apiInstance.suspendUser(userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling LifecycleOperationsApi#suspendUser");
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
| **userId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="unlockUser"></a>
# **unlockUser**
> unlockUser(userId)

Unlock User

Unlock User

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LifecycleOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://okta.local");

    LifecycleOperationsApi apiInstance = new LifecycleOperationsApi(defaultClient);
    String userId = "userId_example"; // String | 
    try {
      apiInstance.unlockUser(userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling LifecycleOperationsApi#unlockUser");
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
| **userId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="unsuspendUser"></a>
# **unsuspendUser**
> unsuspendUser(userId)

Unsuspend User

Unsuspend User

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LifecycleOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://okta.local");

    LifecycleOperationsApi apiInstance = new LifecycleOperationsApi(defaultClient);
    String userId = "userId_example"; // String | 
    try {
      apiInstance.unsuspendUser(userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling LifecycleOperationsApi#unsuspendUser");
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
| **userId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

