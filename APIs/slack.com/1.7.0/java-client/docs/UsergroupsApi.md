# UsergroupsApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**usergroupsCreate**](UsergroupsApi.md#usergroupsCreate) | **POST** /usergroups.create |  |
| [**usergroupsDisable**](UsergroupsApi.md#usergroupsDisable) | **POST** /usergroups.disable |  |
| [**usergroupsEnable**](UsergroupsApi.md#usergroupsEnable) | **POST** /usergroups.enable |  |
| [**usergroupsList**](UsergroupsApi.md#usergroupsList) | **GET** /usergroups.list |  |
| [**usergroupsUpdate**](UsergroupsApi.md#usergroupsUpdate) | **POST** /usergroups.update |  |
| [**usergroupsUsersList_0**](UsergroupsApi.md#usergroupsUsersList_0) | **GET** /usergroups.users.list |  |
| [**usergroupsUsersUpdate_0**](UsergroupsApi.md#usergroupsUsersUpdate_0) | **POST** /usergroups.users.update |  |


<a id="usergroupsCreate"></a>
# **usergroupsCreate**
> UsergroupsCreateSchema usergroupsCreate(token, name, channels, description, handle, includeCount)



Create a User Group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsergroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    UsergroupsApi apiInstance = new UsergroupsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `usergroups:write`
    String name = "name_example"; // String | A name for the User Group. Must be unique among User Groups.
    String channels = "channels_example"; // String | A comma separated string of encoded channel IDs for which the User Group uses as a default.
    String description = "description_example"; // String | A short description of the User Group.
    String handle = "handle_example"; // String | A mention handle. Must be unique among channels, users and User Groups.
    Boolean includeCount = true; // Boolean | Include the number of users in each User Group.
    try {
      UsergroupsCreateSchema result = apiInstance.usergroupsCreate(token, name, channels, description, handle, includeCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsergroupsApi#usergroupsCreate");
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
| **name** | **String**| A name for the User Group. Must be unique among User Groups. | |
| **channels** | **String**| A comma separated string of encoded channel IDs for which the User Group uses as a default. | [optional] |
| **description** | **String**| A short description of the User Group. | [optional] |
| **handle** | **String**| A mention handle. Must be unique among channels, users and User Groups. | [optional] |
| **includeCount** | **Boolean**| Include the number of users in each User Group. | [optional] |

### Return type

[**UsergroupsCreateSchema**](UsergroupsCreateSchema.md)

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

<a id="usergroupsDisable"></a>
# **usergroupsDisable**
> UsergroupsDisableSchema usergroupsDisable(token, usergroup, includeCount)



Disable an existing User Group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsergroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    UsergroupsApi apiInstance = new UsergroupsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `usergroups:write`
    String usergroup = "usergroup_example"; // String | The encoded ID of the User Group to disable.
    Boolean includeCount = true; // Boolean | Include the number of users in the User Group.
    try {
      UsergroupsDisableSchema result = apiInstance.usergroupsDisable(token, usergroup, includeCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsergroupsApi#usergroupsDisable");
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
| **usergroup** | **String**| The encoded ID of the User Group to disable. | |
| **includeCount** | **Boolean**| Include the number of users in the User Group. | [optional] |

### Return type

[**UsergroupsDisableSchema**](UsergroupsDisableSchema.md)

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

<a id="usergroupsEnable"></a>
# **usergroupsEnable**
> UsergroupsEnableSchema usergroupsEnable(token, usergroup, includeCount)



Enable a User Group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsergroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    UsergroupsApi apiInstance = new UsergroupsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `usergroups:write`
    String usergroup = "usergroup_example"; // String | The encoded ID of the User Group to enable.
    Boolean includeCount = true; // Boolean | Include the number of users in the User Group.
    try {
      UsergroupsEnableSchema result = apiInstance.usergroupsEnable(token, usergroup, includeCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsergroupsApi#usergroupsEnable");
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
| **usergroup** | **String**| The encoded ID of the User Group to enable. | |
| **includeCount** | **Boolean**| Include the number of users in the User Group. | [optional] |

### Return type

[**UsergroupsEnableSchema**](UsergroupsEnableSchema.md)

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

<a id="usergroupsList"></a>
# **usergroupsList**
> UsergroupsListSchema usergroupsList(token, includeUsers, includeCount, includeDisabled)



List all User Groups for a team

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsergroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    UsergroupsApi apiInstance = new UsergroupsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `usergroups:read`
    Boolean includeUsers = true; // Boolean | Include the list of users for each User Group.
    Boolean includeCount = true; // Boolean | Include the number of users in each User Group.
    Boolean includeDisabled = true; // Boolean | Include disabled User Groups.
    try {
      UsergroupsListSchema result = apiInstance.usergroupsList(token, includeUsers, includeCount, includeDisabled);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsergroupsApi#usergroupsList");
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
| **includeUsers** | **Boolean**| Include the list of users for each User Group. | [optional] |
| **includeCount** | **Boolean**| Include the number of users in each User Group. | [optional] |
| **includeDisabled** | **Boolean**| Include disabled User Groups. | [optional] |

### Return type

[**UsergroupsListSchema**](UsergroupsListSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="usergroupsUpdate"></a>
# **usergroupsUpdate**
> UsergroupsUpdateSchema usergroupsUpdate(token, usergroup, channels, description, handle, includeCount, name)



Update an existing User Group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsergroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    UsergroupsApi apiInstance = new UsergroupsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `usergroups:write`
    String usergroup = "usergroup_example"; // String | The encoded ID of the User Group to update.
    String channels = "channels_example"; // String | A comma separated string of encoded channel IDs for which the User Group uses as a default.
    String description = "description_example"; // String | A short description of the User Group.
    String handle = "handle_example"; // String | A mention handle. Must be unique among channels, users and User Groups.
    Boolean includeCount = true; // Boolean | Include the number of users in the User Group.
    String name = "name_example"; // String | A name for the User Group. Must be unique among User Groups.
    try {
      UsergroupsUpdateSchema result = apiInstance.usergroupsUpdate(token, usergroup, channels, description, handle, includeCount, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsergroupsApi#usergroupsUpdate");
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
| **channels** | **String**| A comma separated string of encoded channel IDs for which the User Group uses as a default. | [optional] |
| **description** | **String**| A short description of the User Group. | [optional] |
| **handle** | **String**| A mention handle. Must be unique among channels, users and User Groups. | [optional] |
| **includeCount** | **Boolean**| Include the number of users in the User Group. | [optional] |
| **name** | **String**| A name for the User Group. Must be unique among User Groups. | [optional] |

### Return type

[**UsergroupsUpdateSchema**](UsergroupsUpdateSchema.md)

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

<a id="usergroupsUsersList_0"></a>
# **usergroupsUsersList_0**
> UsergroupsUsersListSchema usergroupsUsersList_0(token, usergroup, includeDisabled)



List all users in a User Group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsergroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    UsergroupsApi apiInstance = new UsergroupsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `usergroups:read`
    String usergroup = "usergroup_example"; // String | The encoded ID of the User Group to update.
    Boolean includeDisabled = true; // Boolean | Allow results that involve disabled User Groups.
    try {
      UsergroupsUsersListSchema result = apiInstance.usergroupsUsersList_0(token, usergroup, includeDisabled);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsergroupsApi#usergroupsUsersList_0");
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

<a id="usergroupsUsersUpdate_0"></a>
# **usergroupsUsersUpdate_0**
> UsergroupsUsersUpdateSchema usergroupsUsersUpdate_0(token, usergroup, users, includeCount)



Update the list of users for a User Group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsergroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    UsergroupsApi apiInstance = new UsergroupsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `usergroups:write`
    String usergroup = "usergroup_example"; // String | The encoded ID of the User Group to update.
    String users = "users_example"; // String | A comma separated string of encoded user IDs that represent the entire list of users for the User Group.
    Boolean includeCount = true; // Boolean | Include the number of users in the User Group.
    try {
      UsergroupsUsersUpdateSchema result = apiInstance.usergroupsUsersUpdate_0(token, usergroup, users, includeCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsergroupsApi#usergroupsUsersUpdate_0");
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

