# ResourcesApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**requestSubscriptionScopes**](ResourcesApi.md#requestSubscriptionScopes) | **GET** /v4/resources/user/notifications/scopes | Request list of subscription scopes |
| [**requestUserAvatar**](ResourcesApi.md#requestUserAvatar) | **GET** /v4/resources/users/{user_id}/avatar/{uuid} | Request user avatar |


<a id="requestSubscriptionScopes"></a>
# **requestSubscriptionScopes**
> NotificationScopeList requestSubscriptionScopes()

Request list of subscription scopes

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.20.0&lt;/h3&gt;  ### Description: Retrieve a list of subscription scopes.  ### Precondition: Authenticated user.  ### Postcondition: List of scopes is returned.  ### Further Information: None.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    try {
      NotificationScopeList result = apiInstance.requestSubscriptionScopes();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#requestSubscriptionScopes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NotificationScopeList**](NotificationScopeList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **406** | Not Acceptable |  -  |

<a id="requestUserAvatar"></a>
# **requestUserAvatar**
> Avatar requestUserAvatar(uuid, userId)

Request user avatar

### Description: Get user avatar.  ### Precondition: Valid user ID and avatar UUID  ### Postcondition: Avatar is returned.  ### Further Information: None.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String uuid = "uuid_example"; // String | UUID of the avatar
    Long userId = 56L; // Long | User ID
    try {
      Avatar result = apiInstance.requestUserAvatar(uuid, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#requestUserAvatar");
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
| **uuid** | **String**| UUID of the avatar | |
| **userId** | **Long**| User ID | |

### Return type

[**Avatar**](Avatar.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |

