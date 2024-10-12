# GroupsSubscriptionApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**joinGroup**](GroupsSubscriptionApi.md#joinGroup) | **PUT** /users/{user_id}/groups/{group_id} | Add a user to a group |
| [**joinGroupAlt1**](GroupsSubscriptionApi.md#joinGroupAlt1) | **PUT** /me/groups/{group_id} | Add a user to a group |
| [**leaveGroup**](GroupsSubscriptionApi.md#leaveGroup) | **DELETE** /users/{user_id}/groups/{group_id} | Remove a user from a group |
| [**leaveGroupAlt1**](GroupsSubscriptionApi.md#leaveGroupAlt1) | **DELETE** /me/groups/{group_id} | Remove a user from a group |


<a id="joinGroup"></a>
# **joinGroup**
> joinGroup(groupId, userId)

Add a user to a group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsSubscriptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupsSubscriptionApi apiInstance = new GroupsSubscriptionApi(defaultClient);
    BigDecimal groupId = new BigDecimal("1108"); // BigDecimal | The ID of the group.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    try {
      apiInstance.joinGroup(groupId, userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsSubscriptionApi#joinGroup");
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
| **groupId** | **BigDecimal**| The ID of the group. | |
| **userId** | **BigDecimal**| The ID of the user. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The user joined the group. |  -  |
| **403** | * The authenticated user can&#39;t join groups. * The group prohibits the authenticated user from joining, either because the group is not public or because the group&#39;s privacy setting is &#x60;members&#x60;. |  -  |

<a id="joinGroupAlt1"></a>
# **joinGroupAlt1**
> joinGroupAlt1(groupId)

Add a user to a group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsSubscriptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupsSubscriptionApi apiInstance = new GroupsSubscriptionApi(defaultClient);
    BigDecimal groupId = new BigDecimal("1108"); // BigDecimal | The ID of the group.
    try {
      apiInstance.joinGroupAlt1(groupId);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsSubscriptionApi#joinGroupAlt1");
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
| **groupId** | **BigDecimal**| The ID of the group. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The user joined the group. |  -  |
| **403** | * The authenticated user can&#39;t join groups. * The group prohibits the authenticated user from joining, either because the group is not public or because the group&#39;s privacy setting is &#x60;members&#x60;. |  -  |

<a id="leaveGroup"></a>
# **leaveGroup**
> leaveGroup(groupId, userId)

Remove a user from a group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsSubscriptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupsSubscriptionApi apiInstance = new GroupsSubscriptionApi(defaultClient);
    BigDecimal groupId = new BigDecimal("1108"); // BigDecimal | The ID of the group.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    try {
      apiInstance.leaveGroup(groupId, userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsSubscriptionApi#leaveGroup");
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
| **groupId** | **BigDecimal**| The ID of the group. | |
| **userId** | **BigDecimal**| The ID of the user. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The user left the group. |  -  |
| **403** | The authenticated user owns the group. To remove this user, first apply a new group owner through PATCH. |  -  |

<a id="leaveGroupAlt1"></a>
# **leaveGroupAlt1**
> leaveGroupAlt1(groupId)

Remove a user from a group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsSubscriptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GroupsSubscriptionApi apiInstance = new GroupsSubscriptionApi(defaultClient);
    BigDecimal groupId = new BigDecimal("1108"); // BigDecimal | The ID of the group.
    try {
      apiInstance.leaveGroupAlt1(groupId);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsSubscriptionApi#leaveGroupAlt1");
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
| **groupId** | **BigDecimal**| The ID of the group. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The user left the group. |  -  |
| **403** | The authenticated user owns the group. To remove this user, first apply a new group owner through PATCH. |  -  |

