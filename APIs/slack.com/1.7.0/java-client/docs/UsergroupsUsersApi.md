# UsergroupsUsersApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**usergroupsUsersList**](UsergroupsUsersApi.md#usergroupsUsersList) | **GET** /usergroups.users.list |  |
| [**usergroupsUsersUpdate**](UsergroupsUsersApi.md#usergroupsUsersUpdate) | **POST** /usergroups.users.update |  |


<a id="usergroupsUsersList"></a>
# **usergroupsUsersList**
> UsergroupsUsersListSchema usergroupsUsersList(token, usergroup, includeDisabled)



List all users in a User Group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsergroupsUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    UsergroupsUsersApi apiInstance = new UsergroupsUsersApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `usergroups:read`
    String usergroup = "usergroup_example"; // String | The encoded ID of the User Group to update.
    Boolean includeDisabled = true; // Boolean | Allow results that involve disabled User Groups.
    try {
      UsergroupsUsersListSchema result = apiInstance.usergroupsUsersList(token, usergroup, includeDisabled);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsergroupsUsersApi#usergroupsUsersList");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;usergroups:read&#x60; | |
| **usergroup** | **String**| The encoded ID of the User Group to update. | |
| **includeDisabled** | **Boolean**| Allow results that involve disabled User Groups. | [optional] |

### Return type

[**UsergroupsUsersListSchema**](UsergroupsUsersListSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Standard success response when used with a user token |  -  |
| **0** | Standard failure response when used with an invalid token |  -  |

<a id="usergroupsUsersUpdate"></a>
# **usergroupsUsersUpdate**
> UsergroupsUsersUpdateSchema usergroupsUsersUpdate(token, usergroup, users, includeCount)



Update the list of users for a User Group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsergroupsUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    UsergroupsUsersApi apiInstance = new UsergroupsUsersApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `usergroups:write`
    String usergroup = "usergroup_example"; // String | The encoded ID of the User Group to update.
    String users = "users_example"; // String | A comma separated string of encoded user IDs that represent the entire list of users for the User Group.
    Boolean includeCount = true; // Boolean | Include the number of users in the User Group.
    try {
      UsergroupsUsersUpdateSchema result = apiInstance.usergroupsUsersUpdate(token, usergroup, users, includeCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsergroupsUsersApi#usergroupsUsersUpdate");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;usergroups:write&#x60; | |
| **usergroup** | **String**| The encoded ID of the User Group to update. | |
| **users** | **String**| A comma separated string of encoded user IDs that represent the entire list of users for the User Group. | |
| **includeCount** | **Boolean**| Include the number of users in the User Group. | [optional] |

### Return type

[**UsergroupsUsersUpdateSchema**](UsergroupsUsersUpdateSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

