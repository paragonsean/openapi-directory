# UsersApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteOrganizationUser_1**](UsersApi.md#deleteOrganizationUser_1) | **DELETE** /organizations/{organizationId}/users/{userId} | Delete a user and all of its authentication methods. |
| [**getNetworkSmUserDeviceProfiles_1**](UsersApi.md#getNetworkSmUserDeviceProfiles_1) | **GET** /networks/{networkId}/sm/users/{userId}/deviceProfiles | Get the profiles associated with a user |
| [**getNetworkSmUserSoftwares_1**](UsersApi.md#getNetworkSmUserSoftwares_1) | **GET** /networks/{networkId}/sm/users/{userId}/softwares | Get a list of softwares associated with a user |
| [**getNetworkSmUsers_1**](UsersApi.md#getNetworkSmUsers_1) | **GET** /networks/{networkId}/sm/users | List the owners in an SM network with various specified fields and filters |


<a id="deleteOrganizationUser_1"></a>
# **deleteOrganizationUser_1**
> deleteOrganizationUser_1(organizationId, userId)

Delete a user and all of its authentication methods.

Delete a user and all of its authentication methods.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String userId = "userId_example"; // String | 
    try {
      apiInstance.deleteOrganizationUser_1(organizationId, userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#deleteOrganizationUser_1");
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
| **organizationId** | **String**|  | |
| **userId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful operation |  -  |

<a id="getNetworkSmUserDeviceProfiles_1"></a>
# **getNetworkSmUserDeviceProfiles_1**
> List&lt;GetNetworkSmDeviceDeviceProfiles200ResponseInner&gt; getNetworkSmUserDeviceProfiles_1(networkId, userId)

Get the profiles associated with a user

Get the profiles associated with a user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String userId = "userId_example"; // String | 
    try {
      List<GetNetworkSmDeviceDeviceProfiles200ResponseInner> result = apiInstance.getNetworkSmUserDeviceProfiles_1(networkId, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getNetworkSmUserDeviceProfiles_1");
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
| **networkId** | **String**|  | |
| **userId** | **String**|  | |

### Return type

[**List&lt;GetNetworkSmDeviceDeviceProfiles200ResponseInner&gt;**](GetNetworkSmDeviceDeviceProfiles200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSmUserSoftwares_1"></a>
# **getNetworkSmUserSoftwares_1**
> List&lt;GetNetworkSmDeviceSoftwares200ResponseInner&gt; getNetworkSmUserSoftwares_1(networkId, userId)

Get a list of softwares associated with a user

Get a list of softwares associated with a user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String userId = "userId_example"; // String | 
    try {
      List<GetNetworkSmDeviceSoftwares200ResponseInner> result = apiInstance.getNetworkSmUserSoftwares_1(networkId, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getNetworkSmUserSoftwares_1");
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
| **networkId** | **String**|  | |
| **userId** | **String**|  | |

### Return type

[**List&lt;GetNetworkSmDeviceSoftwares200ResponseInner&gt;**](GetNetworkSmDeviceSoftwares200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSmUsers_1"></a>
# **getNetworkSmUsers_1**
> List&lt;GetNetworkSmUsers200ResponseInner&gt; getNetworkSmUsers_1(networkId, ids, usernames, emails, scope)

List the owners in an SM network with various specified fields and filters

List the owners in an SM network with various specified fields and filters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    List<String> ids = Arrays.asList(); // List<String> | Filter users by id(s).
    List<String> usernames = Arrays.asList(); // List<String> | Filter users by username(s).
    List<String> emails = Arrays.asList(); // List<String> | Filter users by email(s).
    List<String> scope = Arrays.asList(); // List<String> | Specifiy a scope (one of all, none, withAny, withAll, withoutAny, withoutAll) and a set of tags.
    try {
      List<GetNetworkSmUsers200ResponseInner> result = apiInstance.getNetworkSmUsers_1(networkId, ids, usernames, emails, scope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getNetworkSmUsers_1");
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
| **networkId** | **String**|  | |
| **ids** | [**List&lt;String&gt;**](String.md)| Filter users by id(s). | [optional] |
| **usernames** | [**List&lt;String&gt;**](String.md)| Filter users by username(s). | [optional] |
| **emails** | [**List&lt;String&gt;**](String.md)| Filter users by email(s). | [optional] |
| **scope** | [**List&lt;String&gt;**](String.md)| Specifiy a scope (one of all, none, withAny, withAll, withoutAny, withoutAll) and a set of tags. | [optional] |

### Return type

[**List&lt;GetNetworkSmUsers200ResponseInner&gt;**](GetNetworkSmUsers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

