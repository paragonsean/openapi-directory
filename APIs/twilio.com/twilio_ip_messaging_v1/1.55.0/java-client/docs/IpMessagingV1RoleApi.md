# IpMessagingV1RoleApi

All URIs are relative to *https://ip-messaging.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createRole**](IpMessagingV1RoleApi.md#createRole) | **POST** /v1/Services/{ServiceSid}/Roles |  |
| [**deleteRole**](IpMessagingV1RoleApi.md#deleteRole) | **DELETE** /v1/Services/{ServiceSid}/Roles/{Sid} |  |
| [**fetchRole**](IpMessagingV1RoleApi.md#fetchRole) | **GET** /v1/Services/{ServiceSid}/Roles/{Sid} |  |
| [**listRole**](IpMessagingV1RoleApi.md#listRole) | **GET** /v1/Services/{ServiceSid}/Roles |  |
| [**updateRole**](IpMessagingV1RoleApi.md#updateRole) | **POST** /v1/Services/{ServiceSid}/Roles/{Sid} |  |


<a id="createRole"></a>
# **createRole**
> IpMessagingV1ServiceRole createRole(serviceSid, friendlyName, permission, type)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV1RoleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV1RoleApi apiInstance = new IpMessagingV1RoleApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String friendlyName = "friendlyName_example"; // String | 
    List<String> permission = Arrays.asList(); // List<String> | 
    RoleEnumRoleType type = RoleEnumRoleType.fromValue("channel"); // RoleEnumRoleType | 
    try {
      IpMessagingV1ServiceRole result = apiInstance.createRole(serviceSid, friendlyName, permission, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV1RoleApi#createRole");
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
| **friendlyName** | **String**|  | |
| **permission** | [**List&lt;String&gt;**](String.md)|  | |
| **type** | **RoleEnumRoleType**|  | [enum: channel, deployment] |

### Return type

[**IpMessagingV1ServiceRole**](IpMessagingV1ServiceRole.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteRole"></a>
# **deleteRole**
> deleteRole(serviceSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV1RoleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV1RoleApi apiInstance = new IpMessagingV1RoleApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String sid = "sid_example"; // String | 
    try {
      apiInstance.deleteRole(serviceSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV1RoleApi#deleteRole");
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
| **sid** | **String**|  | |

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

<a id="fetchRole"></a>
# **fetchRole**
> IpMessagingV1ServiceRole fetchRole(serviceSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV1RoleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV1RoleApi apiInstance = new IpMessagingV1RoleApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String sid = "sid_example"; // String | 
    try {
      IpMessagingV1ServiceRole result = apiInstance.fetchRole(serviceSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV1RoleApi#fetchRole");
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
| **sid** | **String**|  | |

### Return type

[**IpMessagingV1ServiceRole**](IpMessagingV1ServiceRole.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listRole"></a>
# **listRole**
> ListRoleResponse listRole(serviceSid, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV1RoleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV1RoleApi apiInstance = new IpMessagingV1RoleApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListRoleResponse result = apiInstance.listRole(serviceSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV1RoleApi#listRole");
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
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListRoleResponse**](ListRoleResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateRole"></a>
# **updateRole**
> IpMessagingV1ServiceRole updateRole(serviceSid, sid, permission)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV1RoleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV1RoleApi apiInstance = new IpMessagingV1RoleApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String sid = "sid_example"; // String | 
    List<String> permission = Arrays.asList(); // List<String> | 
    try {
      IpMessagingV1ServiceRole result = apiInstance.updateRole(serviceSid, sid, permission);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV1RoleApi#updateRole");
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
| **sid** | **String**|  | |
| **permission** | [**List&lt;String&gt;**](String.md)|  | |

### Return type

[**IpMessagingV1ServiceRole**](IpMessagingV1ServiceRole.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

